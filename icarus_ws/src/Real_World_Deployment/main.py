#!/usr/bin/env python

import rospy

from geometry_msgs.msg import Point, PoseStamped, Vector3, TransformStamped, Twist
from sensor_msgs.msg import Image, CameraInfo, Imu
from vision_msgs.msg import Detection2DArray
from std_msgs.msg import Float64
from mrs_msgs.msg import Float64Stamped, VelocityReference, VelocityReferenceStamped, SpeedTrackerCommand
from mavros_msgs.msg import Altitude, State, PositionTarget
from detection_msgs.msg import Publish_Data
from filterpy.kalman import KalmanFilter
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
		self.counter = 10
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
		rospy.init_node('follow_target')
		print("Node started")
		
		self.constant = 1000
		
		self.horizontal_distance = 0

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
		self.altitude = 0
		self.depth = 0
		self.target_detected = False
		self.first_detection = False
		self.bridge = CvBridge()

		self.target_lost = False
		self.target_id = 0
		self.adjustment_period = 10
		self.lost_counter = LostCounter()
		self.velocity_msg = Twist()

		# Initialize variables
		self.previous_error = 0.0  # Previous error	
		self.integral = 0
				
		self.heading = 0
		self.heading_rate = 0

		#Define Gains for controller
		self.kh = 0.3
		self.kp_altitude = 0.6

		self.kp_vel = 0.35
		self.kd_vel = 0.0
		self.ki_vel = 0.01

		#self.kp_altitude2 = 0.8 

		self.alpha = 0.10 #low_pass filter
		self.filtered_value = None

		#Parameters for the Slew Rate limiter
		self.max_rate = 0.5
		self.last_update_time = time.time()
		self.last_update_time_KF = time.time()
		self.current_value = 0.0
		self.not_using_depth = True


		self.fx = 615  # Focal length in the x-axis (from camera_info)
		self.fy = 615  # Focal length in the y-axis (from camera_info)
		self.ppx = 318.76  # Principal point x-coordinate (from camera_info)
		self.ppy = 247.39  # Principal point y-coordinate (from camera_info)
		self.camera_width = 640
		self.camera_height = 480

		self.distance = 0
		self.previous_depth = 0

		self.pitch_camera = np.pi/6

		self.pitch = 0
		self.roll = 0
		self.yaw = 0
		self.uav_pose = Point()


		# Initialize a list to store recent distance values
		self.recent_distances = []
		self.detected_objects = []

		self.current_state = State()
		self.bool = True
		self.publish_data = Publish_Data()

		# Subscribe to the target detection topic
		self.sub_State = rospy.Subscriber("/mavros/state", State, self.checkMode)
		self.altitude_sub = rospy.Subscriber('/mavros/global_position/rel_alt', Float64, self.get_altitude)
		#self.imu_sub = rospy.Subscriber('/mavros/imu/data', Imu, self.get_IMU)  # Subscribe to the MAVROS IMU topic
		#self.position_sub = rospy.Subscriber('mavros/global_position/compass_hdg', Float64, self.get_heading)
		
		self.depth_sub = rospy.Subscriber('/camera/aligned_depth_to_color/image_raw', Image, self.depth_callback)
		self.target_sub = rospy.Subscriber('/detection_result', Detection2DArray, self.target_callback)
		self.camera_info_sub = rospy.Subscriber('/camera/color/camera_info', CameraInfo, self.camera_info_callback)
		
		# Publisher for rosbag
		#self.pub_vel = rospy.Publisher('/mavros/setpoint_velocity/cmd_vel_unstamped', Twist, queue_size=1)
		self.pub_vel = rospy.Publisher('/mavros/setpoint_velocity/cmd_vel_unstamped', Twist, queue_size=1)
		self.publisher = rospy.Publisher('/rosbag_data', Publish_Data, queue_size=1)
		self.pub_rate = rospy.Publisher('/rate_rate',Float64,queue_size=1)
		#self.publish_pose = rospy.Publisher('uav1/target_pose', PoseStamped, queue_size=1)
		#self.publish_pose2 = rospy.Publisher('uav1/target_pose2', PoseStamped, queue_size=1)
	
	
	def checkMode(self, state):
		self.current_state = state
		
	def create_velocity_msg(self, Vx, Vy, Vz, yaw_rate):
		# Create a VelocityReference message	
		velocity_msg = Twist()
		                
		velocity_msg.linear.x = Vx
		velocity_msg.linear.z = - Vz
		velocity_msg.angular.z = yaw_rate

		self.target_detected = True

		return velocity_msg

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

	def get_altitude(self, altitude_msg):
		#print("altitude", altitude_msg)
		self.altitude = altitude_msg.data

	def get_depth(self,center_x,center_y):
		#DEPTH PART
		# Get depth information within a small neighborhood around the center of the bounding box
		window_size = 15  # Adjust this value as needed
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
		self.heading = heading_msg.data

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
		
		if self.horizontal_distance < 6 and control_output > 0:
			control_output = control_output/2
		elif self.horizontal_distance < 4 and control_output > 0:
			control_output = 0

		self.publish_data.control_output = control_output

		normalized_y = ((self.KF.x[1] / self.ppy) - 1)
		

		#Vx = math.cos(self.heading) * control_output
		#Vy = math.sin(self.heading) * control_output


		Vz = self.kp_altitude*normalized_y
		#print("_____Altitude_____",self.altitude)
		if self.altitude > 8 and Vz < 0:
			Vz = 0
		elif self.altitude < 3.5 and Vz > 0:
			Vz = 0
		
		velocity_msg = self.create_velocity_msg(control_output, 0, Vz, self.heading_rate)

		self.publish_data.Vz = Vz

		return velocity_msg

	def Update_Objects(self, data, target_found):
		target_bbox = BoundingBox2D()  
		best_match_value = 0
		best_detection = None
	
		if not(target_found):
			#print("target not found, following my target", self.target_id)
			my_target = next((obj for obj in self.detected_objects if obj.id == self.target_id ),None)
			my_target_position_increased = (my_target.center_x, my_target.center_y, my_target.size_x + 150, my_target.size_y + 100)

			target_bbox.center.x = self.KF.x[0]
			target_bbox.center.y = self.KF.x[1]
			target_bbox.size_x = self.KF.x[4]
			target_bbox.size_y = self.KF.x[5]
			#threshold = 2 * target_bbox.size_y

			if not(self.target_lost) and not(self.lost_counter.check_counting()):
				self.target_lost = True
				self.lost_counter.counting = True
				self.lost_counter.counter = 10
				print("START LOST COUNTER, CHECK =", self.lost_counter.check_counting())
			else:
				self.lost_counter.update()
		else:
			self.lost_counter.counting = False
			self.lost_counter.counter = 10
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
				existing_object = next((obj for obj in self.detected_objects if obj.id == id ),None)

				if existing_object:
					#Update the existing object with new information
					existing_object.update(id,center_x,center_y,size_x,size_y)
					if existing_object.id == self.target_id:	
						#Get bbox information for control					
						target_bbox = detection.bbox
						self.target_lost = False
				else:
					if target_found and id != 0:
						#If the object doesn't exist, add it to the local list
						new_object = Detected_Object(id,center_x,center_y,size_x,size_y)
						self.detected_objects.append(new_object)
					elif id != 0:
						#If target is not found, check if the new object matchs the target - IdSwitch
						iou = self.calculate_iou((center_x, center_y, size_x + 150, size_y + 100), my_target_position_increased)
						#distance = self.euclidean_distance(center_x, center_y, my_target.center_x, my_target.center_y)
						#iou_target_lost = self.calculate_iou((center_x, center_y, size_x + 300, size_y + 300), my_target_position_increased)
						#print("Interception over union:", iou)
						#This is a new object unrelated to my lost target
						new_object = Detected_Object(id,center_x,center_y,size_x,size_y)
						self.detected_objects.append(new_object)
						if iou > best_match_value:
							best_match_value = iou
							best_detection = detection
							best_id = id

		# After iterating through all detections, check if the best match has a sufficiently high IoU
		if not(target_found) and best_detection is not None:
			if best_match_value > 0.1:
				#New object matchs the target
				delete_id = self.target_id
				self.target_id = best_id
				my_target.update(best_id,center_x,center_y,size_x,size_y)
				delete_obj = next((obj for obj in self.detected_objects if obj.id == delete_id),None)
				if delete_obj is not None:	
					delete_obj.update(999,0,0,0,0)	
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
				print("TARGET REDETECTED, RESET COUNTER", self.lost_counter.check_counting(), id)
				self.lost_counter.counter = 10
			else:
				target_found = 0
				print("No suitable match found.", best_match_value)				

		return target_bbox

	def target_callback(self, data):
		# Process the target detection data and update self.target_position and self.target_detected
		# Extract the bounding box information from the message
		
		#if self.current_state.mode != "GUIDED":
		#	return
		
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
				

				if not(self.target_lost):
					self.KF.update([center_x, center_y, size_x, size_y])
				self.publish_data.distance_cnst = self.KF.x[0]
				self.publish_data.distance_singer = self.KF.x[1]


				# Convert center coordinates to normalized coordinates (-1 to 1)
				normalized_x = (self.KF.x[0] / self.ppx) - 1
				normalized_y = (self.KF.x[1] / self.ppy) - 1

				size_y = self.KF.x[5]

				#Calculate target heading - put bbox in the center of the frame
				self.heading = np.deg2rad(self.heading)
				self.heading_rate = - self.kh * (normalized_x)
				
				#print("--- heading ---",self.heading)
				#print("--- new heading ---",self.heading_rate)
				
				self.publish_data.Hdg_rate = - self.kh * (normalized_x)
				self.publish_data.id = self.target_id

				# Calculate the error between the target and the center of the image
				#self.target_altitude = self.altitude - self.kp_altitude2 * (normalized_y)# - (self.altitude - 6) * 0.1
				Vz = self.kp_altitude*normalized_y

				self.publish_data.error_altitude = - self.kp_altitude * (normalized_y)# - (self.altitude - 6) * 0.1

				#if self.target_altitude < 3:
				#	self.target_altitude = 3
				#elif self.target_altitude > 10:
				#	self.target_altitude = 10

				if size_y != 0:
					distance = self.constant/(size_y)
				else:
					distance = 10


				if 1:#target_found:
					#depth = self.get_depth(center_x,center_y)
					depth = self.get_depth(320.5,440.5)
					x = (center_x - self.ppx) / self.fx
					y = (center_y - self.ppy) / self.fy
					dist = np.sqrt( x**2 + y**2 + depth**2)
					self.publish_data.depth = depth
					self.publish_data.depth_distance = dist
					#print("\n______depth _____\n",depth)
					#print("\n______dist _____\n",dist)
				else: depth = 0

				#value = distance
				self.not_using_depth = True
				
				if depth > 3 and depth < 7:

					#result = rs2.rs2_deproject_pixel_to_point(self.intrinsics, [center_x, center_y], depth)
					#target_x, target_y = self.target_coordinates_test(depth,center_x,center_y,self.heading)
					#self.KF_target.update([target_x, target_y])
					#dist = np.sqrt((self.uav_pose.x - self.KF_target.x[0])**2 + (self.uav_pose.y - self.KF_target.x[1])**2 + (self.altitude-1)**2)
					
					
					value = self.low_pass_filter(dist)
					self.not_using_depth = False
					print("using depth")#, depth)				
				else:
					value = self.low_pass_filter(distance)
				
				value = self.low_pass_filter(distance)

				estimated_distance = value
				#print("estimated distance", estimated_distance)
				
				self.horizontal_distance = np.sqrt(estimated_distance**2-self.altitude**2)
				error = estimated_distance - 8 #horizontal_distance - 5 #2*self.altitude + 1 #11 #
				
				

				self.publish_data.horizontal_distance = self.horizontal_distance
				
				
				self.publish_data.altitude = self.altitude
				self.publish_data.estimated_distance= estimated_distance
				self.publish_data.use_depth = not(self.not_using_depth)
				self.publish_data.center_x = center_x
				self.publish_data.center_y = center_y
				self.publish_data.controller_error = error


				#print("\n target lost = ", self.target_lost)
				#print("self.lost_counter.lost = ", self.lost_counter.lost)
				#print("self.lost_counter.counter = ", self.lost_counter.counter)
				#print("estimated_distance = ", estimated_distance)
				#print("size_y = ", size_y,"size_x = ", size_x)


				if (self.adjustment_period > 0):
					if not(self.target_lost):
						#print("initial")
						self.adjustment_period -= 1	
					print("ADJUSTING", self.target_id)				
					self.velocity_msg = self.create_velocity_msg(0, 0, Vz, 0.1*self.heading_rate)
					#print("adjusting", self.heading_rate, self.target_altitude)
					self.publish_data.mode = 0	

				elif self.target_lost and not(self.lost_counter.check_counting()) and self.lost_counter.is_lost():
					print("---- LOST ----", self.target_id , self.lost_counter.counter)		
					control_output = self.RateLimiter(0)
					self.publish_data.control_output = control_output	
					self.velocity_msg = self.create_velocity_msg(control_output, 0, 0, 0)
					self.publish_data.mode = 3
				else:
					if self.target_lost:
						self.velocity_msg = self.velocity_controller(error - 1)
						self.lost_altitude = self.altitude
						print("---- MISSING ----",  self.target_id , self.lost_counter.counter, error)
						#print("designated heading part2 =")
						self.publish_data.mode = 2
					else:
						self.velocity_msg = self.velocity_controller(error)
						print("---- REGULAR ----", self.target_id)
						self.publish_data.mode = 1
						
				#print("Output", self.velocity_msg)

		else: #not(self.first_detection):
			# Small search algorithm
			print("start")
			#self.velocity_msg = self.create_velocity_msg(0, 0, 0, 0.05)

	def run(self):
		while not rospy.is_shutdown():
			self.publish_data.target_detected = self.target_detected
			self.publisher.publish(self.publish_data)
			self.pub_rate.publish(1)

			if self.target_detected and self.current_state.mode == "GUIDED":
				self.pub_vel.publish(self.velocity_msg)
			elif self.current_state.mode != "GUIDED":
				self.first_detection = False
				self.filtered_value = None
				self.bool = True
				self.lost_counter.lost = False
				self.adjustment_period = 10
			else:
				self.velocity_msg = Twist()
		rospy.spin()

if __name__ == '__main__':
	#try:
	follower = FollowTarget()
	#sleep(5)
	follower.run()
	#except rospy.ROSInterruptException:
	#	pass
