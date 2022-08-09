#! /usr/bin/env python3

import sys
import copy
import rospy
import geometry_msgs.msg
import moveit_commander
import moveit_msgs.msg


def move_panda():
	moveit_commander.roscpp_initialize(sys.argv)
	rospy.init_node('joint_state_publisher', anonymous=True)

	robot = moveit_commander.RobotCommander()
	scene = moveit_commander.PlanningSceneInterface()
	group = moveit_commander.MoveGroupCommander("panda_arm")
	display_trajectory_publisher = rospy.Publisher('/move_group/display_planned_path', moveit_msgs.msg.DisplayTrajectory)


	group.set_named_target("home_pose")
	plan = group.plan()
	group.go(wait=True)
	rospy.sleep(3)

	pose_target = geometry_msgs.msg.Pose()
	pose_target.orientation.w = 0.5
	pose_target.position.x = 0.3
	pose_target.position.y = 0
	pose_target.position.z = 0.6
	group.set_pose_target(pose_target)

	plan = group.plan()
	group.go(wait=True)
	rospy.sleep(2)

	pose_target = geometry_msgs.msg.Pose()
	pose_target.orientation.w = 0.5
	pose_target.position.x = 0.5
	pose_target.position.y = 0
	pose_target.position.z = 0.6
	group.set_pose_target(pose_target)

	plan = group.plan()
	group.go(wait=True)
	rospy.sleep(2)

	pose_target = geometry_msgs.msg.Pose()
	pose_target.orientation.w = 1
	pose_target.position.x = 0.5
	pose_target.position.y = 0
	pose_target.position.z = 0.8
	group.set_pose_target(pose_target)

	plan = group.plan()
	group.go(wait=True)
	rospy.sleep(2)

	pose_target = geometry_msgs.msg.Pose()
	pose_target.orientation.w = 1
	pose_target.position.x = 0.3
	pose_target.position.y = 0
	pose_target.position.z = 0.8
	group.set_pose_target(pose_target)

	plan = group.plan()
	group.go(wait=True)
	rospy.sleep(2)

	pose_target = geometry_msgs.msg.Pose()
	pose_target.orientation.w = 1
	pose_target.position.x = 0.3
	pose_target.position.y = -0.2
	pose_target.position.z = 0.8
	group.set_pose_target(pose_target)

	plan = group.plan()
	group.go(wait=True)
	rospy.sleep(2)

	pose_target = geometry_msgs.msg.Pose()
	pose_target.orientation.w = 1
	pose_target.position.x = 0.5
	pose_target.position.y = -0.2
	pose_target.position.z = 0.8
	group.set_pose_target(pose_target)

	plan = group.plan()
	group.go(wait=True)
	rospy.sleep(2)

	pose_target = geometry_msgs.msg.Pose()
	pose_target.orientation.w = 0.5
	pose_target.position.x = 0.5
	pose_target.position.y = -0.2
	pose_target.position.z = 0.6
	group.set_pose_target(pose_target)

	plan = group.plan()
	group.go(wait=True)
	rospy.sleep(2)

	pose_target = geometry_msgs.msg.Pose()
	pose_target.orientation.w = 0.5
	pose_target.position.x = 0.3
	pose_target.position.y = -0.2
	pose_target.position.z = 0.6
	group.set_pose_target(pose_target)

	plan = group.plan()
	group.go(wait=True)

	group.stop()
	group.clear_pose_targets()
	moveit_commander.roscpp_shutdown()
	moveit_commander.os._exit(0)


if __name__ == "__main__":
	move_panda()




