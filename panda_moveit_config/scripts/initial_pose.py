#! /usr/bin/env python

import sys
import copy
import rospy
import geometry_msgs.msg
import moveit_commander
import moveit_msgs.msg

moveit_commander.roscpp_initialize(sys.argv)
rospy.init_node('joint_state_publisher', anonymous=True)

robot = moveit_commander.RobotCommander()
scene = moveit_commander.PlanningSceneInterface()
group = moveit_commander.MoveGroupCommander("panda_arm")
display_trajectory_publisher = rospy.Publisher('/move_group/display_planned_path', moveit_msgs.msg.DisplayTrajectory)

group.set_named_target("home_pose")

plan1 = group.plan()
group.go(wait=True)
moveit_commander.roscpp_shutdown()
