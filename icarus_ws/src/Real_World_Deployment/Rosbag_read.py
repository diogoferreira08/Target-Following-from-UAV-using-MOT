#!/usr/bin/env python

import rosbag
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator
import numpy as np
import sys

# Provide the path to your rosbag file
rosbag_path = sys.argv[1]

print(rosbag_path)



# Define the topic name
topic_name = '/rosbag_data'

# Lists to store data
timestamps = []
real_distances = []
real_distances1 = []
real_distances2 = []
real_distances3 = []
estimated_distances = []
horizontal_distance =[]
use_depth_values = []
center_x_values = []
center_y_values = []
error_heading_values = []
error_altitude_values = []
altitude_values = []
controller_error_values = []
control_output_values = []
controller_error_values_abs = []
target_lost_values = []
target_detected_values = []
distance_cnst = []
distance_singer = []
distance_imm = []
target_x = []
target_y = []
estimated_target_x = []
estimated_target_y = []
real_target_x = []
real_target_y = []
uav_x = []
uav_y = []
error_center = []
Vx = []
Vy = []
Vz = []
heading_rate = []

# Read data from rosbag
with rosbag.Bag(rosbag_path, 'r') as bag:
    for topic, msg, t in bag.read_messages(topics=[topic_name]):
        timestamps.append(t.to_sec())
        real_distances.append(np.array(msg.real_distance))
        if len(msg.real_distance) > 0:
            real_distances1.append(msg.real_distance[0])
            #real_distances2.append(msg.real_distance[1])
            #real_distances3.append(msg.real_distance[2])
        else:
            real_distances1.append(0)
            #real_distances2.append(0)
            #real_distances3.append(0)
        distance_imm.append(msg.distance_imm)
        distance_cnst.append(msg.distance_cnst/318.76 - 1)
        distance_singer.append(msg.distance_singer - 240.5)
        error_center.append(np.sqrt((msg.distance_cnst - 320.5)**2 + (msg.distance_singer - 240.5)**2))
        estimated_distances.append(msg.estimated_distance)
        horizontal_distance.append(msg.horizontal_distance)
        use_depth_values.append(msg.use_depth)
        center_x_values.append(abs(msg.center_x - 320.5))
        center_y_values.append(abs(msg.center_y - 240.5))
        error_heading_values.append(msg.error_heading)
        heading_rate.append(-msg.Hdg_rate)
        error_altitude_values.append(msg.error_altitude)
        altitude_values.append(msg.altitude)
        controller_error_values.append(msg.controller_error)
        controller_error_values_abs.append(abs(msg.controller_error))
        control_output_values.append(msg.control_output)
        target_lost_values.append(msg.target_lost)
        target_detected_values.append(msg.target_detected)

        Vx.append(msg.Vx)
        Vy.append(msg.Vy)
        Vz.append(-msg.Vz)


        target_x.append(msg.target_x)
        target_y.append(msg.target_y)
        real_target_x.append(msg.real_target_x)
        real_target_y.append(msg.real_target_y)
        uav_x.append(msg.uav_x)
        uav_y.append(msg.uav_y)
        estimated_target_x.append(msg.estimated_target_x)
        estimated_target_y.append(msg.estimated_target_y)


# Plotting

fig, axes = plt.subplots(nrows=4, ncols=3, figsize=(15, 10))
fig.suptitle('ROS Topic Data Visualization')
# Plot individual data


j= 0
for i in timestamps:
    if target_lost_values[j] == 1:
        break
    else: 
        j = j+1
        continue
init = j



#axes[0, 0].plot(timestamps, real_distances1, label='Real Distance 1')
axes[0, 0].plot(timestamps[init+100:], np.subtract(real_distances1[init+100:],estimated_distances[init+100:]), label='diference')
#axes[0, 0].plot(timestamps, use_depth_values, label='use depth')
#axes[0, 0].plot(timestamps, real_distances2, label='Real Distance 2')
#axes[0, 0].plot(timestamps, real_distances3, label='Real Distance 3')
axes[0, 0].set_title('Real Distance')


axes[0, 1].set_title('Estimated Distance')
axes[0, 1].plot(timestamps, horizontal_distance, label='Horizontal Distance')
axes[0, 1].plot(timestamps[init:], estimated_distances[init:], label='Estimated Distance')
axes[0, 1].plot(timestamps[init:], use_depth_values[init:], label='Use Depth')

axes[0, 2].plot(timestamps[init:], use_depth_values[init:], label='Use Depth')
axes[0, 2].plot(timestamps[init:], controller_error_values_abs[init:], label='Controller Error')
axes[0, 2].set_title('Use Depth')

#axes[1, 0].plot(timestamps, center_x_values, label='Center X')
axes[1, 0].plot(timestamps[init:], distance_cnst[init:], label='Center X KF')
axes[1, 0].plot(timestamps[init:], heading_rate[init:], label='yaw rate')
axes[1, 0].set_title('Center X')
#axes[1, 1].plot(timestamps, center_y_values, label='Center Y')
axes[1, 1].plot(timestamps[init:], distance_singer[init:], label='Center Y KF')
#axes[1, 1].plot(timestamps[init:], distance_singer[init:], label='Center Y KF')
axes[1, 1].set_title('Center Y')

axes[1, 2].plot(timestamps[init:], error_heading_values[init:], label='Error Heading')
axes[1, 2].set_title('Error Heading')

axes[2, 0].plot(timestamps, error_altitude_values, label='Error Altitude')
axes[2, 0].plot(timestamps, Vz, label='Vz')
axes[2, 0].set_title('Error Altitude')
axes[2, 1].plot(timestamps, altitude_values, label='Altitude')
axes[2, 1].set_title('Altitude')
axes[2, 2].plot(timestamps, controller_error_values, label='Controller Error')
axes[2, 2].plot(timestamps, np.zeros(len(timestamps)))
axes[2, 2].set_title('Controller Error')

axes[3, 0].plot(timestamps[init:], control_output_values[init:], label='Control Output')
axes[3, 0].set_title('Control Output')
axes[3, 1].plot(timestamps, target_lost_values, label='Target Lost')
axes[3, 1].set_title('Target Lost')
axes[3, 2].plot(timestamps, target_detected_values, label='Target Detected')
axes[3, 2].set_title('Target Detected')

# Adjust layout
plt.tight_layout(rect=[0, 0.03, 1, 0.95])
for ax in axes.flat:
    ax.xaxis.set_major_locator(MaxNLocator(nbins=5))
    ax.legend()

# Show the plot
plt.show()

'''
plt.figure(1)
plt.plot(timestamps, real_distances1, label='Real Distance 1')
plt.plot(timestamps, estimated_distances, label='Estimated Distance')
plt.plot(timestamps, controller_error_values, label='Controller Error')
plt.plot(timestamps, np.zeros(len(timestamps)))
plt.legend()

plt.figure(5)
#plt.plot(timestamps, center_x_values, label='Center X')
plt.plot(timestamps, error_center, label='Error center')
#plt.set_title('Error center')
plt.legend()

#array of size timestamps of 0
#create an array of size timestamps of 0 
zero_array = np.zeros(len(timestamps))



fig2, axes2 = plt.subplots(nrows=2, ncols=1)
#fig2.suptitle('Real Distance vs Estimated Distance')

#axes2[0, 0].set_title('Real Distance vs Estimated Distance')
end= 0
for i in timestamps:
    if timestamps[end] > 240:
        break
    else: 
        end = end+1
        continue

print(end)
'''
'''
axes2[0].spines['top'].set_visible(False)
axes2[0].spines['right'].set_visible(False)
axes2[0].spines['bottom'].set_visible(True)
axes2[0].spines['left'].set_visible(True)
axes2[1].spines['top'].set_visible(False)
axes2[1].spines['right'].set_visible(False)
axes2[1].spines['bottom'].set_visible(True)
axes2[1].spines['left'].set_visible(True)
'''
'''
plt.figure(11)
#plt.title('Estimated vs Real Distances from the Target')
plt.plot(timestamps[0:], real_distances1[0:], label='Real Distance')
plt.plot(timestamps[init+300:], estimated_distances[init+300:], label='Estimated Distance')
plt.xlabel('Time [s]')
plt.ylabel('Distance [m]')
plt.legend()

plt.figure(12)
#plt.title('Error between Real and Estimated Distances')
plt.plot(timestamps[init+300:], np.subtract(real_distances1[init+300:],estimated_distances[init+300:]), label='Error')
plt.plot(timestamps, zero_array,color='black')
plt.xlabel('Time [s]')
plt.ylabel('Error [m]')
plt.legend()


plt.figure(9)
#plt.title('3D Velocity in the Body Frame',fontsize=8)
plt.plot(timestamps, zero_array,color='black')
plt.plot(timestamps, Vx, label='Velocity X')
plt.plot(timestamps, Vy, label='Velocity Y')
plt.plot(timestamps, Vz, label='Velocity Z')
plt.xlabel('Time [s]')
plt.ylabel('Velocity [m/s]')
plt.legend()



#plt.show()

print(j)
#end = 200000




plt.figure(2)
#plt.plot(uav_x, uav_y, label='UAV')
#plt.plot(target_x[init:], target_y[init:], label='Estimated target pose')
#plt.plot(estimated_target_x[init:], estimated_target_y[init:], label='KF target pose')
plt.plot(real_target_x[init:], real_target_y[init:], label='Real target pose')
plt.plot(uav_x[init:],uav_y[init:], label='UAV POSE')
plt.legend()


ax = plt.figure().add_subplot(projection='3d')
ax.plot(real_target_x[init:end], real_target_y[init:end], 0, zdir='z', label='curve in (x,y)')
ax.plot(uav_x[init:end],uav_y[init:end], altitude_values[init:end], zdir='z', label='curve in (x,y)')
colors = ('r','g','b','k')
ax.view_init(elev = 20, azim= -35, roll=0)


plt.figure()
#plt.plot(uav_x, uav_y, label='UAV')
error_x = np.subtract(real_target_x,estimated_target_x)
error_y = np.subtract(center_y_values,estimated_target_y)
#yoyo = np.add(error_x,error_y)
#error_total = np.sqrt(yoyo)
plt.plot(timestamps[init:], error_x[init:],label='error_x')
plt.plot(timestamps[init:],error_y[init:], label='error_y')
plt.plot(timestamps,uav_x)
plt.plot(timestamps,uav_y)
plt.plot(timestamps,altitude_values)
plt.legend()

plt.figure()
plt.scatter(distance_cnst[init:],distance_singer[init:],label='error_x',s=1)
plt.xlim(-640,+640)
plt.ylim(-360,+360)
plt.legend()


'''
'''
i=0
for j in estimated_distances:
    if use_depth_values[i]==0:
        estimated_distances[i] = 0
        real_distances1[i] =0
    i=i+1

plt.figure()
plt.plot(timestamps, np.subtract(real_distances1,estimated_distances), label='diference')
plt.legend()

plt.figure()
plt.scatter(timestamps,estimated_distances,s=1)
plt.plot(timestamps,real_distances1)
'''
'''

total_distance = 0
total_distance_target = 0
print(timestamps[len(real_target_x)-1])
print(timestamps[init])

uav_x = uav_x[init:len(uav_x)]
uav_y = uav_y[init:len(uav_y)]
altitude_values= altitude_values[init:len(altitude_values)]
real_target_x = real_target_x[init:len(real_target_x)]
real_target_y = real_target_y[init:len(real_target_y)]

for i in range(1,len(uav_x)):
    distance = np.sqrt((uav_x[i]- uav_x[i-1])**2 +(uav_y[i]-uav_y[i-1])**2 + (altitude_values[i]-altitude_values[i-1])**2)
    total_distance += distance

for j in range(1, len(real_target_x)):
    distance_target = np.sqrt((real_target_x[j]- real_target_x[j-1])**2 + (real_target_y[j] - real_target_y[j-1])**2)
    total_distance_target += distance_target


target_lost_values = target_lost_values[init:len(target_lost_values)]
use_depth_values = use_depth_values[init:len(use_depth_values)]

percentage = 100-(sum(1 for elem in target_lost_values if elem==0)/len(target_lost_values))*100

percentage_depth = 100-(sum(1 for elem in use_depth_values if elem==0)/len(use_depth_values))*100

estimation_error = abs(np.subtract(real_distances1[init+100:],estimated_distances[init+100:]))
average_error = sum(estimation_error)/len(estimation_error)


print("TOTAL DISTANCE", total_distance)
print("TOTAL DISTANCE TARGET", total_distance_target)
print("PERCENTAGE TARGET FOUND", percentage)
print("PERCENTAGE DEPTH VALUES", percentage_depth)
print("AVERAGE ESTIMATION ERROR", average_error)



plt.show()
'''

