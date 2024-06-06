This ROS package computes cubic trajectories calculating position, velocity and acceleration.Every 20 seconds it generates new random points and displays their trajectories via rqt_plot GUI.

To run the package:
1) unzip the folder in your catkin workspace.
2) open ros noetic terminal and type 'cd catkin/ar_week8_test'
3) build with the command 'catkin_make' and 'source devel/setup.bash'
4) to run the file then 'roslaunch ar_week8_test cubic_traj_gen.launch'
