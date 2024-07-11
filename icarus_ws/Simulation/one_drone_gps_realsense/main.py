#!/usr/bin/env python

import rospy

from geometry_msgs.msg import Point, PoseStamped, Vector3, TransformStamped
from sensor_msgs.msg import Image, CameraInfo, Imu  # Replace with your target detection message type
from vision_msgs.msg import Detection2DArray
from mrs_msgs.srv import VelocityReferenceStampedSrv
from mrs_msgs.msg import Float64Stamped, VelocityReference, VelocityReferenceStamped, SpeedTrackerCommand
from gazebo_msgs.msg import ModelStates
from mavros_msgs.msg import Altitude
from detection_msgs.msg import PublishData
from filterpy.kalman import KalmanFilter, IMMEstimator
from filterpy.common import Q_discrete_white_noise
import tf2_ros
import tf2_geometry_msgs

import numpy as np
import math
from cv_bridge import CvBridge

import time
import tf
import pyrealsense2 as rs2

class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

class BoundingBox2D:
    def __init__(self, center_x = 0, center_y = 0, size_x = 0, size_y = 0):
        self.center = Point(center_x, center_y)
        self.size_x = size_x
        self.size_y = size_y

class Detected_Object:
	def __init__(self, id, center_x, center_y, size_x, size_y):
		self.id = id
		self.center_x = center_x
		self.center_y = center_y
		self.size_x = size_x
		self.size_y = size_y
	def update(self, id, center_x, center_y, size_x, size_y):
		self.id = id
		self.center_x = center_x
		self.center_y = center_y
		self.size_x = size_x
		self.size_y = size_y

class LostCounter:
	def	__init__(self, counting = False):
		self.counter = 30
		self.counting = counting
		self.lost = False
		print("Lost Counter Initilized")
	def update(self):
		if self.counter > 0:
			self.counter -= 1
			#print("Lost Counter:", self.counter)
			return True
		elif self.counter == 0:
			self.counting = False
			self.lost = True
			return False
	def check_counting(self):
		return self.counting
	def is_lost(self):
		return self.lost

class FollowTarget:
	def __init__(self):
		rospy.init_node('follow_target', anonymous=True)
		print("Node started")

		self.KF = KalmanFilter(dim_x=6, dim_z=4)
		#states = s(t) = (x,y,vx,vy,size_x,size_y)
		self.KF.H =   np.array([[1, 0, 0, 0, 0, 0],
								[0, 1, 0, 0, 0, 0],
								[0, 0, 0, 0, 1, 0],
								[0, 0, 0, 0, 0, 1]])
		
		self.KF.P *= 5  # initial covariance matrix
		# Set the measurement noise covariance matrix
		self.KF.R =   np.array([[2, 0, 0, 0],
								[0, 2, 0, 0],
								[0, 0, 20, 0],
								[0, 0, 0, 20]])
		
		self.KF.Q =   np.array([[2, 0, 0, 0, 0, 0],
								[0, 2, 0, 0, 0, 0],
								[0, 0, 1, 0, 0, 0],
								[0, 0, 0, 1, 0, 0],
								[0, 0, 0, 0, 1, 0],
								[0, 0, 0, 0, 0, 1]])  # process noise
		
		###################

		self.KF_target = KalmanFilter(dim_x=4, dim_z=2)

		# Define the observation matrix
		self.KF_target.H = np.array([[1, 0, 0, 0],
                 					[0, 1, 0, 0]])
		self.KF_target.P *= 5  # initial covariance matrix

		# Set the measurement noise covariance matrix
		self.KF_target.R = np.array([[100, 0],
							  		[0, 100]])
		
		self.KF_target.Q = np.array([[1, 0, 0, 0],
									[0, 1, 0, 0],
									[0, 0, 1, 0],
									[0, 0, 0, 1]])  # process noise
		

		#######________________________########

		self.intrinsics = None

		self.target_position = Point()
		self.target_hdg = 0
		self.altitude = 0
		self.depth = 0
		self.target_detected = False
		self.first_detection = False
		self.bridge = CvBridge()

		self.target_lost = False
		self.target_id = 0
		self.adjustment_period = 60
		self.lost_counter = LostCounter()
		self.velocity_msg = VelocityReference()

		# Initialize variables
		self.previous_error = 0.0  # Previous error	
		self.integral = 0
				
		self.heading = 0
		self.target_hdg = 0

		#Define Gains for controller
		self.kh = 0.3 #good 0.35
		self.kh2 = 0.6

		self.kp_vel = 0.35
		self.kd_vel = 0.0
		self.ki_vel = 0.01

		self.kp_altitude = 0.8 #good 0.8

		self.alpha = 0.10 #low_pass filter
		self.filtered_value = None

		#Parameters for the Slew Rate limiter
		self.max_rate = 0.4
		self.last_update_time = time.time()
		self.last_update_time_KF = time.time()
		self.current_value = 0.0
		self.not_using_depth = True


		self.fx = 0.1  # Focal length in the x-axis (from camera_info)
		self.fy = 0.1  # Focal length in the y-axis (from camera_info)
		self.ppx = 0  # Principal point x-coordinate (from camera_info)
		self.ppy = 0  # Principal point y-coordinate (from camera_info)
		self.camera_width = 1280
		self.camera_height = 720

		self.distance = 0
		self.dist_horizontal = 0
		self.previous_depth = 0

		self.pitch_camera = np.pi/6

		self.pitch = 0
		self.roll = 0
		self.yaw = 0
		self.uav_pose = Point()
		


		# Initialize a list to store recent distance values
		self.recent_distances = []
		self.detected_objects = []
		self.detected_objects_ids = []

		self.bool = True
		self.publish_data = PublishData()
		self.tf_buffer = tf2_ros.Buffer()
		self.tf_listener = tf2_ros.TransformListener(self.tf_buffer)
		# Subscribe to the target detection topic
		self.odemetry_sub = rospy.Subscriber('/uav1/mavros/local_position/pose', PoseStamped, self.odemetry_callback)
		self.distance_sub = rospy.Subscriber("/gazebo/model_states", ModelStates, self.model_states_callback)
		self.altitude_sub = rospy.Subscriber('/uav1/mavros/altitude', Altitude, self.get_altitude)
		self.depth_sub = rospy.Subscriber('/uav1/rgbd_front_pitched/aligned_depth_to_color/image_raw', Image, self.depth_callback)
		self.target_sub = rospy.Subscriber('/detection_result', Detection2DArray, self.target_callback)
		self.position_sub = rospy.Subscriber('/uav1/control_manager/heading', Float64Stamped, self.get_heading)
		self.camera_info_sub = rospy.Subscriber('/uav1/rgbd_front_pitched/color/camera_info', CameraInfo, self.camera_info_callback)
		self.imu_sub = rospy.Subscriber('/uav1/mavros/imu/data', Imu, self.get_IMU)  # Subscribe to the MAVROS IMU topic

		# Publisher for rosbag
		self.publisher = rospy.Publisher('/uav1/rosbag_data', PublishData, queue_size=1)
		self.publish_pose = rospy.Publisher('uav1/target_pose', PoseStamped, queue_size=1)
		self.publish_pose2 = rospy.Publisher('uav1/target_pose2', PoseStamped, queue_size=1)
	
	
	def calculate_relative_distance(self, u,v, target_height):
		# Calculate the inverse of the intrinsic matrix
		K_inv = np.linalg.inv(self.K_intrinsics)

		pitch = np.radians(30)
		R_BC = np.array([
			[0, np.sin(pitch), np.cos(pitch)],
			[1, 0, 0],
			[0, -np.cos(pitch), np.sin(pitch)]
		])

		target_homogeneous_coordinates = np.array([u, v, 1])

		# Convert homogeneous coordinates to normalized image coordinates
		uvw_normalized = K_inv @ target_homogeneous_coordinates

		# Apply rotation to get the target position in the body frame
		p_B = R_BC @ uvw_normalized

		# Extract x, y, and z coordinates of the target in body frame
		xt, yt, zt = p_B

		# Calculate the relative distance using the pinhole imaging model
		distance = target_height / zt * np.sqrt(xt**2 + yt**2)

		return p_B,distance

	def odemetry_callback(self, local_position):
		self.uav_pose = local_position.pose.position

	def transform_coordinates(self, fcu_coordinates):
		
		# Transform the point from the camera frame to the UAV body frame
		source_frame = "uav1/rgbd_front_pitched/aligned_depth_to_color_optical"
		target_frame = "uav1/local_origin"
		#realsense_frame = "uav1/"

		transformed_stamped = self.tf_buffer.lookup_transform(target_frame, source_frame, rospy.Time(0), rospy.Duration(1.0)) 
		world_coordinates = tf2_geometry_msgs.do_transform_pose(fcu_coordinates, transformed_stamped)

		#world_coordinates = self.tf_listener.transformPose(target_frame, fcu_coordinates,source_frame)

		world_x = world_coordinates.pose.position.x
		world_y = world_coordinates.pose.position.y
		return world_x,world_y

	def target_world_coordinates(self, distance, heading):
		d_h = np.sqrt(distance**2 - self.uav_pose.z**2)
		x_target = self.uav_pose.x + d_h * np.cos(heading)
		y_target = self.uav_pose.y + d_h * np.sin(heading)
		return x_target, y_target
	
	def target_coordinates_test(self,distance,center_x,center_y, heading):
		
		z0 = distance*np.sqrt(1/(1+((center_x - self.ppx) /self.fx)))
		h = self.uav_pose.z

		X_camera = (center_x - self.ppx)*z0 /self.fx
		Y_camera = (center_y - self.ppy)*z0 /self.fy
		Z_camera = z0

		print("\ndistance", distance)
		print("center_x", center_x)
		print("center_y", center_y)	
		print("heading", heading)
		

		result = rs2.rs2_deproject_pixel_to_point(self.intrinsics, [center_x, center_y], distance)
		
		#point2 = PoseStamped()
		#point2.pose.position.x = result[0]
		#point2.pose.position.y = result[1]
		#point2.pose.position.z = result[2]
		#point2.header.frame_id="uav1/rgbd_front_pitched/aligned_depth_to_color_optical"
		#self.publish_pose2.publish(point2)
		
		pitch = np.radians(30)
		R_BC = np.array([
			[0, np.sin(pitch), np.cos(pitch)],
			[1, 0, 0],
			[0, np.cos(pitch), np.sin(pitch)]
		])

		R_SB = np.array([
			[np.cos(heading), -np.sin(heading), 0],
			[np.sin(heading), np.cos(heading), 0],
			[0, 0, 1]
		])

		(X_body,Y_body,Z_body) = R_BC.dot((X_camera,Y_camera,Z_camera))
		(X_world_prev,Y_world_prev,Z_world_prev) = R_SB.dot((X_body,Y_body,Z_body))

		target_x = X_world_prev + self.uav_pose.x
		target_y = Y_world_prev + self.uav_pose.y

		
		print("\ncoordinate image frame", X_camera, Y_camera, Z_camera)
		print("coordinate body frame\n", X_body, Y_body, Z_body)


		point = PoseStamped()
		point.pose.position.x = X_camera
		point.pose.position.y = Y_camera
		point.pose.position.z = Z_camera
		point.header.frame_id="uav1/rgbd_front_pitched/aligned_depth_to_color_optical"
		self.publish_pose.publish(point)

		target_x,target_y = self.transform_coordinates(point)

		angle = np.radians(-4)
		target_x_rot = target_x * np.cos(angle) - target_y * np.sin(angle)
		target_y_rot = target_x * np.sin(angle) + target_y * np.cos(angle)

		return target_x_rot,target_y_rot

	def target_world_coordinates_inverse(self, x_target, y_target):
		d_h = np.sqrt((x_target - self.uav_pose.x)**2 + (y_target - self.uav_pose.y)**2)
		distance = np.sqrt(d_h**2 + self.uav_pose.z**2)
		return distance

	def calculate_iou(self, box1, box2):
		# Extract center coordinates and size of the bounding boxes
		x1, y1, w1, h1 = box1
		x2, y2, w2, h2 = box2

		# Calculate the half-width and half-height of each bounding box
		half_w1, half_h1 = w1 / 2, h1 / 2
		half_w2, half_h2 = w2 / 2, h2 / 2

		# Calculate the coordinates of the top-left and bottom-right corners of each bounding box
		x1_tl, y1_tl = x1 - half_w1, y1 - half_h1
		x1_br, y1_br = x1 + half_w1, y1 + half_h1

		x2_tl, y2_tl = x2 - half_w2, y2 - half_h2
		x2_br, y2_br = x2 + half_w2, y2 + half_h2

		# Calculate the intersection coordinates
		x_inter = max(x1_tl, x2_tl)
		y_inter = max(y1_tl, y2_tl)
		x2_inter = min(x1_br, x2_br)
		y2_inter = min(y1_br, y2_br)

		# Calculate the intersection area
		intersection_area = max(0, x2_inter - x_inter) * max(0, y2_inter - y_inter)

		# Calculate the union area
		area1 = w1 * h1
		area2 = w2 * h2
		union_area = area1 + area2 - intersection_area

		# Calculate IoU
		iou = intersection_area / union_area if union_area > 0 else 0

		return iou

	def euclidean_distance(self, x1, y1, x2, y2):
		return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
	
	def get_IMU(self, imu_msg):
		# Extract orientation (roll, pitch, yaw) from MAVROS IMU data
		orientation = imu_msg.orientation
		orientation_list = [orientation.x, orientation.y, orientation.z, orientation.w]
		(self.roll, self.pitch, self.yaw) = tf.transformations.euler_from_quaternion(orientation_list)
		#print("orientation",self.pitch, self.roll, self.yaw)

	def	get_altitude(self, altitude_msg):
		#print("altitude", altitude_msg)
		self.altitude = altitude_msg.amsl

	def translate_to_stabilized_frame(self, depth):
		# Translate depth from camera frame to UAV body frame
		pitch = np.radians(30)
		T_camera_to_body = np.array([
			[1, 0, 0, 0.226],
			[0, np.cos(pitch), -np.sin(pitch), 0],
			[0, np.sin(pitch), np.cos(pitch), -0.089],
			[0, 0, 0, 1]
		])
		depth_body_frame = np.dot(T_camera_to_body, np.array([0, 0, depth, 1]))[2]

		# Translate depth from UAV body frame to UAV stabilized frame
		R = tf.transformations.euler_matrix(self.roll, self.pitch, self.yaw)
		T_body_to_stabilized = np.identity(4)
		T_body_to_stabilized[:3, :3] = R[:3, :3]
		depth_stabilized_frame = np.dot(T_body_to_stabilized, np.array([0, 0, depth_body_frame, 1]))[2]

		return depth_stabilized_frame

	def calculate_distance_uav_frame(self, depth, center_x, center_y, height_uav):
		# Convert camera angle from degrees to radians
		pitch = np.radians(30)

		# Calculate vertical offset (Y) using depth information
		Z = depth
		Y = (center_y - self.ppy) * Z / self.fy

		# Calculate horizontal offset (X)
		X = (center_x - self.ppx) * Z / self.fx

		# Calculate distance (D) from camera to person
		D_camera_frame = np.sqrt(X**2 + Y**2 + height_uav**2)

		#print("D_camera_frame\n", D_camera_frame)

		# Construct the 4x4 homogeneous transformation matrix
		R_pitch = np.array([
			[1, 0, 0],
			[0, np.cos(pitch), -np.sin(pitch)],
			[0, np.sin(pitch), np.cos(pitch)]
		])

		translation = [0.226, 0.0, -0.089]  # Replace with actual translation values
		T = np.zeros((4, 4))
		T[:3, :3] = R_pitch
		T[:3, 3] = translation
		T[3, 3] = 1.0

		# Create a homogeneous coordinate for the person in the camera frame
		P_camera_frame = np.array([X, Y, Z, 1])

		# Apply the transformation to get the person's position in the UAV's body frame
		P_uav_frame = T.dot(P_camera_frame)

		# Extract the transformed position
		X_uav = P_uav_frame[0]
		Y_uav = P_uav_frame[1]
		Z_uav = P_uav_frame[2]

		# Calculate the distance in the UAV's body frame
		D_body_frame = np.sqrt(X_uav**2 + Y_uav**2 + Z_uav**2)

		# Create a 3x1 vector for the distance in the body frame
		distance_vector_body = np.array([0, 0, D_body_frame])

		# Create a 3x3 rotation matrix based on the orientation (roll, pitch, yaw)
		R = tf.transformations.euler_matrix(self.roll, self.pitch, self.yaw)[:3, :3]

		# Transform the distance vector from the body frame to the stabilized frame
		distance_vector_stabilized = np.dot(R, distance_vector_body)

		# Extract the transformed distance along the Z-axis in the stabilized frame
		D_stabilized_frame = distance_vector_stabilized[2]

		#print("D_stabilized_frame\n", D_stabilized_frame)

		return D_stabilized_frame

	def model_states_callback(self, data):
		try:
			uav1_index = data.name.index("uav1")
			actor_walking_index = data.name.index("actor_walking1")
			#actor_walking_index2 = data.name.index("actor_walking1")
			#actor_walking_index3 = data.name.index("actor_walking6")
			#if data.name.index("actor_walking4"):
			#	actor_walking_index4 = data.name.index("actor_walking4")
			#if data.name.index("actor_walking5"):
			#	actor_walking_index5 = data.name.index("actor_walking5")
			#if data.name.index("actor_walking6"):
			#	actor_walking_index6 = data.name.index("actor_walking6")

			uav1_position = data.pose[uav1_index].position
			actor_walking_position = data.pose[actor_walking_index].position
			#actor_walking_position2 = data.pose[actor_walking_index2].position
			#actor_walking_position3 = data.pose[actor_walking_index3].position
		
			distance1 = math.sqrt(
				(uav1_position.x - actor_walking_position.x) ** 2 +
				(uav1_position.y - actor_walking_position.y) ** 2 +
				(uav1_position.z - actor_walking_position.z) ** 2
			)	

			'''
			distance2 = math.sqrt(
				(uav1_position.x - actor_walking_position2.x) ** 2 +
				(uav1_position.y - actor_walking_position2.y) ** 2 +
				(uav1_position.z - actor_walking_position2.z) ** 2
			)
			
			distance3 = math.sqrt(
				(uav1_position.x - actor_walking_position3.x) ** 2 +
				(uav1_position.y - actor_walking_position3.y) ** 2 +
				(uav1_position.z - actor_walking_position3.z) ** 2
			)	
			'''

			self.distance = distance1
			distance = []
			distance.append(distance1)
			#distance.append(distance2)
			#distance.append(distance3)

			self.publish_data.uav_x=uav1_position.x 
			self.publish_data.uav_y=uav1_position.y
			self.publish_data.altitude = uav1_position.z
			self.publish_data.real_target_x=actor_walking_position.x
			self.publish_data.real_target_y=actor_walking_position.y

			#print("UAV POSE\n", uav1_position.x, uav1_position.y, uav1_position.z)
			#print("ACTOR POSE\n", actor_walking_position.x, actor_walking_position.y)

			self.publish_data.real_distance = distance
		except ValueError:
			pass  # Handle the case where the models are not found in the model_states message	
		
	def create_velocity_msg(self, Vx, Vy, Vz, heading_rate, altitude, use_altitude):
		# Create a VelocityReference message
		velocity_msg = VelocityReference()
		velocity_msg.velocity.x = Vx
		velocity_msg.velocity.y = Vy
		velocity_msg.velocity.z = Vz
		velocity_msg.altitude = altitude
		velocity_msg.heading_rate = heading_rate
		velocity_msg.use_altitude = use_altitude#True
		velocity_msg.use_heading_rate = True
		self.target_detected = True

		return velocity_msg

	def get_depth(self,center_x,center_y):
		#DEPTH PART
		# Get depth information within a small neighborhood around the center of the bounding box
		window_size = 5  # Adjust this value as needed
		depth_matrix = None
		if hasattr(self, 'depth_image'):
			depth_matrix = self.depth_image[
			int(center_y) - window_size : int(center_y) + window_size + 1,
			int(center_x) - window_size : int(center_x) + window_size + 1,
			]
		if depth_matrix is None:
			return 0
			
		# Create a copy of the depth_matrix to avoid the read-only error
		depth_matrix_copy = np.copy(depth_matrix)

		# Replace NaN values with a placeholder value (-1.0) in the copy
		depth_matrix_copy[np.isnan(depth_matrix_copy)] = -1.0

		# Calculate the approximate depth to the target by averaging the values in the depth_matrix
		average_depth = np.mean(depth_matrix_copy[depth_matrix_copy != -1.0])

		return average_depth/1000
	
	def RateLimiter(self, new_value):

		self.max_rate = self.max_rate
		current_time = time.time()
		time_elapsed = current_time - self.last_update_time
		self.last_update_time = current_time

		if time_elapsed == 0:
			return self.current_value

		rate_of_change = (new_value - self.current_value) / time_elapsed

		if self.bool:
			self.current_value = 0
			self.bool = False
			return self.current_value

		if abs(rate_of_change) <= self.max_rate:
			# If the rate of change is within the limit, update the current value.
			self.current_value = new_value
			self.last_update_time = current_time
		else:
			# Limit the rate of change.
			sign = 1 if new_value > self.current_value else -1
			self.current_value += sign * self.max_rate * time_elapsed
			self.last_update_time = current_time

		return self.current_value

	def low_pass_filter(self,new_value):
		
		if self.filtered_value is None:
			self.filtered_value = new_value
		else:
			self.filtered_value = self.alpha * new_value + (1 - self.alpha) * self.filtered_value
		return self.filtered_value
	
	def depth_callback(self, msg):
		try:
			self.depth_image = self.bridge.imgmsg_to_cv2(msg, "passthrough")
		except Exception as e:
			rospy.logerr("Error converting depth image: %s", str(e))

	def camera_info_callback(self, cameraInfo):
		self.fx = cameraInfo.K[0]  # Focal length in the x-axis
		self.fy = cameraInfo.K[4]  # Focal length in the y-axis
		self.ppx = cameraInfo.K[2] # Principal point x-coordinate
		self.ppy = cameraInfo.K[5] # Principal point y-coordinate

		#print(msg.K)
		K_array = np.array(cameraInfo.K)
		self.K_intrinsics = K_array.reshape(3, 3)

		try:
			if self.intrinsics:
				return
			self.intrinsics = rs2.intrinsics()
			self.intrinsics.width = cameraInfo.width
			self.intrinsics.height = cameraInfo.height
			self.intrinsics.ppx = cameraInfo.K[2]
			self.intrinsics.ppy = cameraInfo.K[5]
			self.intrinsics.fx = cameraInfo.K[0]
			self.intrinsics.fy = cameraInfo.K[4]
			if cameraInfo.distortion_model == 'plumb_bob':
				self.intrinsics.model = rs2.distortion.brown_conrady
			elif cameraInfo.distortion_model == 'equidistant':
				self.intrinsics.model = rs2.distortion.kannala_brandt4
			self.intrinsics.coeffs = [i for i in cameraInfo.D]
		except:
			pass

	def get_heading(self,heading_msg):
		#print("heading", heading_msg)
		self.heading = heading_msg.value

	def velocity_controller(self, error):
		# Calculate the derivative term
		derivative = error - self.previous_error
		# Calculate the integral term
		self.integral += error 
		#Anti Wind-Up
		if self.integral > 2:
			self.integral = 2
		elif self.integral < -2:
			self.integral = -2

		# Update the previous error for the next iteration
		self.previous_error = error
		# Calculate the PID output			
		control_output = (error * self.kp_vel + self.kd_vel * derivative + self.ki_vel * self.integral)

		#print("integral",self.integral)
		#print("derivative",derivative)

		#Limits for the controller
		if control_output > 4:
			control_output = 4
			self.integral -= error
			#print("output_limited")
		elif control_output < -4:
			control_output = -4
			self.integral -= error
			#print("output_limited")

		#Limit slew rate for precision tracking to reduce oscilations
		control_output = self.RateLimiter(control_output)

		if self.dist_horizontal < 8 and control_output > 0:
			control_output = control_output/2
		elif self.dist_horizontal < 6 and control_output > 0:
			control_output = 0

		print("horizontal distance",self.dist_horizontal)

		self.publish_data.control_output = control_output

		normalized_y = ((self.KF.x[1] / self.ppy) - 1)
		

		Vx = math.cos(self.heading) * control_output
		Vy = math.sin(self.heading) * control_output


		Vz = -self.kh2*normalized_y
		if self.altitude > 9 and Vz > 0:
			Vz = 0
		elif self.altitude < 3 and Vz < 0:
			Vz = 0
		
		velocity_msg = self.create_velocity_msg(Vx, Vy, Vz, self.target_hdg, self.target_altitude, False)

		self.publish_data.Vx = Vx
		self.publish_data.Vy = Vy
		self.publish_data.Vz = Vz

		return velocity_msg

	def Update_Objects(self, data, target_found):
		target_bbox = BoundingBox2D()  
		best_match_value = 0
		best_detection = None
		threshold = 0.1
	
		if not(target_found):
			#print("target not found, following my target", self.target_id)
			my_target = next((obj for obj in self.detected_objects if obj.id == self.target_id ),None)
			my_target_position_increased = (my_target.center_x, my_target.center_y, my_target.size_x + 250, my_target.size_y + 150)

			target_bbox.center.x = self.KF.x[0]
			target_bbox.center.y = self.KF.x[1]
			target_bbox.size_x = self.KF.x[4]
			target_bbox.size_y = self.KF.x[5]
			threshold = 2 * target_bbox.size_y

			#for ii in self.detected_objects:
					#print("not found \n",ii.id)

			if not(self.target_lost) and not(self.lost_counter.check_counting()):
				self.target_lost = True
				self.lost_counter.counting = True
				self.lost_counter.counter = 30
				print("START LOST COUNTER, CHECK =", self.lost_counter.check_counting())
			else:
				self.lost_counter.update()
		else:
			self.lost_counter.counting = False
			self.lost_counter.counter = 30
			self.lost_counter.lost = False
			print("target found, RESET COUNTER, CHECK =", self.lost_counter.check_counting())

		for detection in data.detections:
				bounding_box = detection.bbox
				# Extract the center and size information from the BoundingBox2D message
				id = detection.results[0].id
				center_x = bounding_box.center.x
				center_y = bounding_box.center.y
				size_x = bounding_box.size_x
				size_y = bounding_box.size_y

				#Check if object with the id exists in the local list
				existing_object = next((obj for obj in self.detected_objects if obj.id == id),None)

				if existing_object:
					#Update the existing object with new information
					existing_object.update(id,center_x,center_y,size_x,size_y)
					if existing_object.id == self.target_id:	
						#Get bbox information for control					
						target_bbox = detection.bbox
						self.target_lost = False
				else:
					if target_found:
						#If the object doesn't exist, add it to the local list
						if id != 0:
							new_object = Detected_Object(id,center_x,center_y,size_x,size_y)
							self.detected_objects.append(new_object)
					else:
						#If target is not found, check if the new object matchs the target - IdSwitch
						#This is a new object unrelated to my lost target
						if id!= 0: 
							iou = self.calculate_iou((center_x, center_y, size_x + 250, size_y + 150), my_target_position_increased)
							print("Interception over union:", iou)
							new_object = Detected_Object(id,center_x,center_y,size_x,size_y)
							self.detected_objects.append(new_object)
							if iou > best_match_value:
								best_match_value = iou
								best_detection = detection
								best_id = id
								print("best detection",id)

		# After iterating through all detections, check if the best match has a sufficiently high IoU
		if not(target_found) and best_detection is not None:
			if best_match_value > 0.1:
				#New object matchs the target
				my_target.update(best_id,center_x,center_y,size_x,size_y)
				delete = next((obj for obj in self.detected_objects if obj.id == self.target_id ),None)
				if delete is not None:
					delete.update(999,0,0,0,0)
				self.target_id = best_id
				target_bbox = detection.bbox
				target_found = 1
				self.target_lost = False
				if self.lost_counter.is_lost():
					self.filtered_value = None
					self.bool = True
					self.lost_counter.lost = False
					self.adjustment_period = 10
					print("RESET VALUES")
				self.lost_counter.counting = False
				print("TARGET REDETECTED, RESET COUNTER", self.lost_counter.check_counting(), best_id)
				self.lost_counter.counter = 30
				for ii in self.detected_objects:
					print("\n",ii.id)
			else:
				target_found = 0
				print("No suitable match found.", threshold, best_match_value)				
	
		return target_bbox

	def target_callback(self, data):
		# Process the target detection data and update self.target_position and self.target_detected
		# Extract the bounding box information from the message

		#___________________________________Kalman_Filter_______________________________________	
		#Constante Velocity Model	
		current_time = time.time()
		dt = current_time - self.last_update_time_KF
		self.last_update_time_KF = current_time
		self.KF.F = np.array([[1, 0, dt, 0, 0, 0],
							[0, 1, 0, dt, 0, 0],
							[0, 0, 1, 0, 0, 0],
							[0, 0, 0, 1, 0, 0],
							[0, 0, 0, 0, 1, 0],
							[0, 0, 0, 0, 0, 1]])
		self.KF.predict()

		self.KF_target.F = np.array([[1, 0, dt, 0],
									[0, 1, 0, dt],
									[0, 0, 1, 0],
									[0, 0, 0, 1]])
		
		self.KF_target.predict()

		if not(data.detections or self.target_lost):
			self.KF.update(None)
			self.KF_target.update(None)
		#________________________________________________________________________________________
			

		if not(data.detections) and self.first_detection:
			self.first_detection = True
			self.target_lost = True

		if data.detections or self.target_lost:
			# Loop through all detected objects
			
			

			#Initilize target on first detection
			if not(self.first_detection):
				self.target_id = data.detections[0].results[0].id
				print("target detected id first frame:\n", self.target_id)
				self.first_detection = True
				new_object = Detected_Object(self.target_id,data.detections[0].bbox.center.x,data.detections[0].bbox.center.y,
								 data.detections[0].bbox.size_x,data.detections[0].bbox.size_y)
				self.detected_objects.append(new_object)

			# Check if the target is in the detection message
			target_found = 0
			for detection in data.detections:
				if detection.results[0].id == self.target_id:
					target_found = 1
					#detection.bbox.center.x = self.KF.x[0]
					#print("target detected id:\n", detection.results[0].id)
			#if not(target_found):
			#	pass
					
			self.publish_data.target_lost = target_found
					
			#Update the position of all objects and get target bbox information
			#If target was not found in detection, do Id Switch Recovery
			bounding_box = self.Update_Objects(data, target_found)	

			if bounding_box is not None:
				#Get information from bbox
				center_x = bounding_box.center.x
				center_y = bounding_box.center.y
				size_x = bounding_box.size_x
				size_y = bounding_box.size_y

				if target_found:
					depth = self.get_depth(center_x,center_y)
				else: depth = 0

				#if depth > 4:
				#	size_y = 1450/(depth)

				if not(self.target_lost):
					self.KF.update([center_x, center_y, size_x, size_y])
				self.publish_data.distance_cnst = self.KF.x[0]
				self.publish_data.distance_singer = self.KF.x[1]


				# Convert center coordinates to normalized coordinates (-1 to 1)
				normalized_x = (self.KF.x[0] / self.ppx) - 1
				normalized_y = (self.KF.x[1] / self.ppy) - 1

				size_y = self.KF.x[5]

				#Calculate target heading - put bbox in the center of the frame
				self.target_hdg = - self.kh * (normalized_x)
				
				self.publish_data.error_heading = - self.kh * (normalized_x)
				self.publish_data.id = self.target_id

				# Calculate the error between the target and the center of the image
				self.target_altitude = self.altitude - self.kp_altitude * (normalized_y)# - (self.altitude - 6) * 0.1

				self.publish_data.error_altitude = - self.kp_altitude * (normalized_y)# - (self.altitude - 6) * 0.1

				if self.target_altitude < 3:
					self.target_altitude = 3
				elif self.target_altitude > 10:
					self.target_altitude = 10

				if size_y != 0:
					distance = 1450/(size_y)
				else:
					distance = 10

				#p_B,relative_distance = self.calculate_relative_distance(center_x,center_y,self.uav_pose.z)

				#array_cnst = self.KF.x
				#distance_constante = self.target_world_coordinates_inverse(array_cnst[0], array_cnst[1])
				#self.KF_singer.update([target_x, target_y])
				#array_singer = self.KF_singer.x
				#distance_singer = self.target_world_coordinates_inverse(array_singer[0], array_singer[1])
				#self.imm.update([target_x, target_y])
				#distance_imm = self.target_world_coordinates_inverse(self.imm.x[0], self.imm.x[1])
					

				if target_found:
					depth = self.get_depth(center_x,center_y)
				else: depth = 0

				#value = distance
				self.not_using_depth = True
				
				if depth > 3:
					#result = rs2.rs2_deproject_pixel_to_point(self.intrinsics, [center_x, center_y], depth)
					#target_x, target_y = self.target_coordinates_test(depth,center_x,center_y,self.heading)
					#self.KF_target.update([target_x, target_y])
					#dist = np.sqrt((self.uav_pose.x - self.KF_target.x[0])**2 + (self.uav_pose.y - self.KF_target.x[1])**2 + (self.altitude-1)**2)
					x = (center_x - self.ppx) /self.fx
					y = (center_y - self.ppy) /self.fy
					dist = np.sqrt(x**2 + y**2 + depth**2)
					value = self.low_pass_filter(dist)
						
					self.not_using_depth = False
					#value = 1450/self.KF.x[5]
					#estimated_distance = self.translate_to_stabilized_frame(value)

					print("using depth", depth)				
				else:
					value = self.low_pass_filter(distance)
				
				value = self.low_pass_filter(distance)

				#target_x, target_y = self.target_world_coordinates(value, self.target_hdg)
				#if self.not_using_depth:
				target_x, target_y = self.target_coordinates_test(value,center_x,center_y,self.heading)
				self.KF_target.update([target_x, target_y])

				self.publish_data.target_x = target_x
				self.publish_data.target_y = target_y
				self.publish_data.estimated_target_x = self.KF_target.x[0]
				self.publish_data.estimated_target_y = self.KF_target.x[1]


				#print("---- estimated target pose ----\n", self.KF_target.x[0], self.KF_target.x[1])

				estimated_distance = value
				#print("estimated distance", estimated_distance)
				error = estimated_distance - 11 #2*self.altitude + 1 #11 #

				self.dist_horizontal = np.sqrt(value**2 - (self.altitude)**2)
				



				#self.publish_data.altitude = self.altitude
				self.publish_data.estimated_distance= estimated_distance
				self.publish_data.use_depth = not(self.not_using_depth)
				self.publish_data.center_x = center_x
				self.publish_data.center_y = center_y
				self.publish_data.controller_error = error


				#print("\n target lost = ", self.target_lost)
				#print("self.lost_counter.lost = ", self.lost_counter.lost)
				#print("self.lost_counter.counter = ", self.lost_counter.counter)
				#print("estimated_distance = ", estimated_distance)
				#print("size_y = ", size_y)
				#print("size_x = ", size_x)	



				if (self.adjustment_period > 0):
					if not(self.target_lost):
						print("initial")
						self.adjustment_period -= 1	
					print("ADJUSTING", self.target_id)				
					self.velocity_msg = self.create_velocity_msg(0, 0, 0, self.target_hdg, self.target_altitude, True)
					#print("adjusting", self.target_hdg, self.target_altitude)	

				elif self.target_lost and not(self.lost_counter.check_counting()) and self.lost_counter.is_lost():
					print("---- LOST ----", self.target_id , self.lost_counter.counter)
					
					#self.velocity_msg = self.velocity_controller(0)
					#new_center_x = self.KF.x[0]+self.KF.x[2]*dt
					#new_center_y = self.KF.x[1]+self.KF.x[3]*dt
					#self.KF.update([new_center_x, new_center_y, self.KF.x[4], self.KF.x[5]])
					#self.velocity_msg = self.velocity_controller(0)
					control_output = self.RateLimiter(0)
					self.publish_data.control_output = control_output	
					Vx = math.cos(self.heading) * control_output
					Vy = math.sin(self.heading) * control_output
					self.velocity_msg = self.create_velocity_msg(Vx, Vy, 0, 0, self.lost_altitude, True)
					#self.velocity_msg.altitude = 7
					#self.velocity_msg.heading = self.heading
					#print(self.velocity_msg.velocity.x, self.velocity_msg.velocity.y)
					#self.velocity_msg.use_heading = False
					#print("heading part3 =",self.velocity_msg.heading)
				else:
					if self.target_lost:
						#new_center_x = self.KF.x[0]+self.KF.x[2]*dt
						#new_center_y = self.KF.x[1]+self.KF.x[3]*dt
						#self.KF.update([new_center_x, new_center_y, self.KF.x[4], self.KF.x[5]])
						self.velocity_msg = self.velocity_controller(error - 1)
						self.lost_altitude = self.altitude
						print("---- MISSING ----",  self.target_id , self.lost_counter.counter, error)
						print("designated heading part2 =",self.velocity_msg.heading)
					else:
						self.velocity_msg = self.velocity_controller(error)
						print("---- REGULAR ----", self.target_id)

		else: #not(self.first_detection):
			# Small search algorithm
			self.velocity_msg = self.create_velocity_msg(0, 0, 0, 0.1, 4, True)

	def run(self):
		#rate = rospy.Rate(10)  # 10 Hz
		
		while not rospy.is_shutdown():
			self.publish_data.target_detected = self.target_detected
			self.publisher.publish(self.publish_data)
			if self.target_detected:
			
				# Define the service client to call the /$UAV_NAME/control_manager/goto service
				#service_name = "/uav1/control_manager/goto"  #pass this later to the config file
				service_name = "/uav1/control_manager/velocity_reference"
				rospy.wait_for_service(service_name)
				velocity_service = rospy.ServiceProxy(service_name, VelocityReferenceStampedSrv)
				
				# Create a service client for the /$UAV_NAME/control_manager/goto service
				request = VelocityReferenceStamped()
				request.reference = self.velocity_msg
				request.header.frame_id = "uav1/local_origin"
				#print(request.header.frame_id)
				# Call the service to send the reference values
				try:
					#Call the service
					response = velocity_service(request)
					# Print the response (optional)
					#rospy.loginfo("Service response: %s", response)

				except rospy.ServiceException as e:
					rospy.logerr("Service call failed: %s", e)
		rospy.spin()
		#rate.sleep()

if __name__ == '__main__':
	#try:
	follower = FollowTarget()
	#sleep(5)
	follower.run()
	#except rospy.ROSInterruptException:
	#	pass

