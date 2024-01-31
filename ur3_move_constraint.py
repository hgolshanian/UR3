#!/usr/bin/env python

# Author: Hyeonjun Park, Ph.D. candidate
# Affiliation: Human-Robot Interaction LAB, Kyung Hee University, South Korea
# koreaphj91@gmail.com
# init: 9 Apr 2019
# revision: 17 Feb 2020


import sys
import rospy
import tf
import moveit_commander  # https://answers.ros.org/question/285216/importerror-no-module-named-moveit_commander/
import random
from geometry_msgs.msg import Pose, Point, Quaternion
import math
from math import pi

import geometry_msgs.msg

################################
# import moveit_msgs.msg
# from moveit_msgs.msg import Constraints, JointConstraint
#################################


#pose_goal = Pose()
moveit_commander.roscpp_initialize(sys.argv)
rospy.init_node('ur3_move',anonymous=True)
#group = [moveit_commander.MoveGroupCommander("manipulator")]  # ur3 moveit group name: manipulator


robot = moveit_commander.RobotCommander()
scene = moveit_commander.PlanningSceneInterface()
group_name = "manipulator"
move_group = moveit_commander.MoveGroupCommander(group_name)

# Set the planner to PILZ
move_group.set_planner_id("PILZ") #LIN

# Define a joint constraint
# joint_constraint = JointConstraint()
# joint_constraint.joint_name = "shoulder_lift_joint"  # specify the joint name
# joint_constraint.position = -0.65 # target position
# joint_constraint.tolerance_above = 0.2
# joint_constraint.tolerance_below = 0.2
# joint_constraint.weight = 1.0

# constraints = Constraints()
# constraints.joint_constraints.append(joint_constraint)
# move_group.set_path_constraints(constraints)

xx = 1

while not rospy.is_shutdown():  
  if(xx%2 == 1):  

    pose_target = geometry_msgs.msg.Pose()
    fi=(pi/180)*-178
    te=0
    si=0
    pose_target.orientation.w = math.cos (fi/2)*math.cos (te/2)*math.cos (si/2)+math.sin (fi/2)*math.sin (te/2)*math.sin (si/2)
    pose_target.orientation.x = math.sin (fi/2)*math.cos (te/2)*math.cos (si/2)-math.cos (fi/2)*math.sin (te/2)*math.sin (si/2)
    pose_target.orientation.y = math.cos (fi/2)*math.sin (te/2)*math.cos (si/2)+math.sin (fi/2)*math.cos (te/2)*math.sin (si/2)
    pose_target.orientation.z = math.cos (fi/2)*math.cos (te/2)*math.sin (si/2)+math.sin (fi/2)*math.sin (te/2)*math.cos (si/2)      
   
    pose_target.position.x = 0.2 # red line      0.2   0.2
    pose_target.position.y = 0.45  # green line  0.15   0.15
    pose_target.position.z = 0.095  # blue line   # 0.35   0.6
    move_group.set_pose_target(pose_target)
    # Plan and execute
    plan = move_group.go(wait=True)
    move_group.stop()
    move_group.clear_pose_targets()
    
    #print(xx)
    rospy.sleep(2)
      
  else:

    pose_target = geometry_msgs.msg.Pose()
    fi=(pi/180)*-178
    te=0
    si=0
    pose_target.orientation.w = math.cos (fi/2)*math.cos (te/2)*math.cos (si/2)+math.sin (fi/2)*math.sin (te/2)*math.sin (si/2)
    pose_target.orientation.x = math.sin (fi/2)*math.cos (te/2)*math.cos (si/2)-math.cos (fi/2)*math.sin (te/2)*math.sin (si/2)
    pose_target.orientation.y = math.cos (fi/2)*math.sin (te/2)*math.cos (si/2)+math.sin (fi/2)*math.cos (te/2)*math.sin (si/2)
    pose_target.orientation.z = math.cos (fi/2)*math.cos (te/2)*math.sin (si/2)+math.sin (fi/2)*math.sin (te/2)*math.cos (si/2)
  
    pose_target.position.x = 0.2 # red line      0.2   0.2
    pose_target.position.y = 0.45  # green line  0.15   0.15
    pose_target.position.z = 0.18  # blue line   # 0.35   0.6
    move_group.set_pose_target(pose_target)
    # Plan and execute
    plan = move_group.go(wait=True)
    move_group.stop()
    move_group.clear_pose_targets()
      
    #print(xx)
    rospy.sleep(2) 

  xx = xx + 1 

  
'''
pose_goal.orientation.w = 0.0
pose_goal.position.x = 0.4 # red line      0.2   0.2
pose_goal.position.y = 0.15  # green line  0.15   0.15
pose_goal.position.z = 0.5  # blue line   # 0.35   0.6
group[0].set_pose_target(pose_goal)
group[0].go(True)
'''
moveit_commander.roscpp_shutdown()