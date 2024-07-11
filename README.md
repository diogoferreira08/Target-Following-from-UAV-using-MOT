# Target-Following-from-UAV-using-MOT
Leveraging multi-object tracking in a target following scenario from a UAV

To run simulation experiments, go to mrs-ctu page and install the mrs-ctu uav system
run:
*   cd /icarus_ws/src/Simulation/one_drone_gps_realsense/
*   ./start.sh

Be sure to properly setup the catkin workspace for simulation and real-world experiments. Also, if using the realsense, install the proper ros package for that.

In the real-world experiments, setup the workspace and run:

*   cd /icarus_ws/src/Real_World_Deployment
*   ./start.sh

This tmux scrip will run the realsense node, the yolov8 node and the follow_target node which is the main function containing the image post processing, control and redetection algorithms.
