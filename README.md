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



BIBTEX Citations:

Leveraging Multi-Object Tracking in Vision-based Target Following for Unmanned Aerial Vehicles: conference paper showing simulation results:

@INPROCEEDINGS{10535936,
  author={Ferreira, Diogo and Basiri, Meysam},
  booktitle={2024 IEEE International Conference on Autonomous Robot Systems and Competitions (ICARSC)}, 
  title={Leveraging Multi-Object Tracking in Vision-based Target Following for Unmanned Aerial Vehicles}, 
  year={2024},
  volume={},
  number={},
  pages={88-93},
  keywords={YOLO;Visualization;Target tracking;Three-dimensional displays;Heuristic algorithms;Autonomous aerial vehicles;Solids;UAV;Multi-Object Tracking;YOLOv8;BoT-SORT;Flight Control;MTT},
  doi={10.1109/ICARSC61747.2024.10535936}}

