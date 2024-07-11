#!/usr/bin/env python

import rosbag
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator
import numpy as np
'''
# Provide the path to your rosbag file
rosbag_path = 'data/EXP4.bag'



# Define the topic name
topic_name = 'uav1/rosbag_data'

# Lists to store data
timestamps = []
real_distances = []
real_distances1 = []
real_distances2 = []
real_distances3 = []
estimated_distances = []
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

# Read data from rosbag
with rosbag.Bag(rosbag_path, 'r') as bag:
    for topic, msg, t in bag.read_messages(topics=[topic_name]):
        timestamps.append(t.to_sec())
        distance_cnst.append(msg.distance_cnst - 640.5)
        distance_singer.append(msg.distance_singer - 360.5)
        center_x_values.append(abs(msg.center_x - 640.5))
        center_y_values.append(abs(msg.center_y - 360.5))
        target_lost_values.append(msg.target_lost)



j= 0
for i in timestamps:
    if target_lost_values[j] == 1:
        break
    else: 
        j = j+1
        continue
init = j



plt.figure(5)
#plt.plot(timestamps, center_x_values, label='Center X')
plt.plot(timestamps, error_center, label='Error center')
#plt.set_title('Error center')
plt.legend()

plt.figure()
plt.scatter(distance_cnst[init:],distance_singer[init:],label='error_x',s=1)
plt.xlim(-640,+640)
plt.ylim(-360,+360)
plt.legend()

total_distance = 0
total_distance_target = 0
print(timestamps[len(real_target_x)-1])
print(timestamps[init])
'''

import rosbag
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import gaussian_kde
from matplotlib.colors import Normalize
from scipy.ndimage import gaussian_filter
import seaborn as sns


def plot_probability_distribution(x_arrays, y_arrays):
    plt.figure(figsize=(10, 6))
    plt.xlim(-320, 320)
    plt.ylim(-240, 240)
    plt.xlabel('X Position')
    plt.ylabel('Y Position')
    plt.grid(True)
    
    plt.scatter(np.concatenate(x_arrays), np.concatenate(y_arrays),s =1)

    # Create a 2D histogram
    #H, xedges, yedges = np.histogram2d(np.concatenate(x_arrays), np.concatenate(y_arrays), bins=45, range=[[-320, 320], [-240, 240]])
    

    # Convert histogram values to probability (assuming they are counts)
    total_counts = len(np.concatenate(x_arrays))
    #print(len(np.concatenate(x_arrays)))
    #print(sum(H))
    #H = gaussian_filter(H, sigma=0.5)
    #print(H_smooth)
    #probability_H = (H / total_counts)*100

    #print(sum(sum(probability_H)))

    # Plot the histogram
    #sns.heatmap(H, cmap='Spectral')

    #cmap = plt.cm.Spectral
    #plt.imshow(probability_H.T, origin='lower', extent=[xedges[0], xedges[-1], yedges[0], yedges[-1]], cmap=cmap,interpolation='nearest')
    #cbar = plt.colorbar(label='Density distribution (%)')
    #cbar.ax.yaxis.set_tick_params(color='white') 

    #plt.figure(2)
    #plt.scatter(np.concatenate(x_arrays),np.concatenate(y_arrays),s=1)
    #plt.xlim(-640, 640)
    #plt.ylim(-360, 360)

    plt.show()
'''

def plot_probability_distribution(x_arrays, y_arrays):
    fig = plt.figure(figsize=(10, 6))
    fig.patch.set_facecolor('white')  # Set background color to white
    plt.xlim(-640, 640)
    plt.ylim(-360, 360)
    plt.xlabel('X Position')
    plt.ylabel('Y Position')
    plt.grid(True)

    # Calculate the 2D kernel density estimation
    k = gaussian_kde(np.vstack([np.concatenate(x_arrays), np.concatenate(y_arrays)]))
    xi, yi = np.mgrid[-640:640:200j, -360:360:200j]
    zi = k(np.vstack([xi.flatten(), yi.flatten()]))

    # Plot the contour plot
    plt.contourf(xi, yi, zi.reshape(xi.shape), cmap='binary')

    # Customize colorbar
    cbar = plt.colorbar(label='Density')
    cbar.ax.yaxis.set_tick_params(color='red')  # Change color of colorbar ticks to red

    # Plot the points (dots) with larger markersize
    #plt.scatter(np.concatenate(x_arrays), np.concatenate(y_arrays), color='black', marker='o', s=2)  # Adjust 's' for the marker size

    plt.show()
'''
def read_rosbag(rosbag_file):
    x_arrays = []
    y_arrays = []
    topic_name = '/rosbag_data'
    target_lost_values=[]
    center_x = []
    center_y = []
    timestamps = []

    with rosbag.Bag(rosbag_file, 'r') as bag:
        for topic, msg, t in bag.read_messages(topics=[topic_name]):
            # Assuming the message format is consistent
            # Modify this part based on the actual message structure in your rosbag files
            timestamps.append(t.to_sec())
            center_x.append(msg.distance_cnst - 318.76)
            center_y.append(msg.distance_singer - 247.39)
            target_lost_values.append(msg.target_lost)

    j= 0
    for i in timestamps:
        if target_lost_values[j] == 1:
            break
        else: 
            j = j+1
            continue
    init = j
    center_x = center_x[init:]
    center_y = center_y[init:]

    x = [pos for pos in center_x]
    y = [pos for pos in center_y]
    x_arrays.extend(x)
    y_arrays.extend(y)
    return x_arrays, y_arrays

if __name__ == "__main__":
    rosbag_files = ["data/2024-04-16/EXP1.bag", "data/2024-04-16/EXP4.bag"]#, "data/2024-04-16/EXP6.bag", "data/2024-04-16/EXP9.bag", "data/2024-04-16/EXP12.bag"]
    x_arrays_all = []
    y_arrays_all = []

    for rosbag_file in rosbag_files:
        x_arrays, y_arrays = read_rosbag(rosbag_file)
        x_arrays_all.append(x_arrays)
        y_arrays_all.append(y_arrays)

    plot_probability_distribution(x_arrays_all, y_arrays_all)

#plt.show()

