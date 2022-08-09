following are the steps to run the project.

1. run the command in catkin_workspace to open rviz and run the python file to execute the motion of robot arm.
--->  roscore
--->  roslaunch panda_moveit_config planning_context.launch
--->  roslaunch panda_moveit_config demo.launch
--->  rosrun panda_moveit_config motion_plan.py
