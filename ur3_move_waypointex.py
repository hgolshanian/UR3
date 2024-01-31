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

pose_goal = Pose()
moveit_commander.roscpp_initialize(sys.argv)
rospy.init_node('ur3_move',anonymous=True)
group = [moveit_commander.MoveGroupCommander("manipulator")]  # ur3 moveit group name: manipulator

def set_pose(x, y, z):
    pose = Pose()
    fi=(pi/180)*-178
    te=0
    si=0
    pose.orientation.w = math.cos (fi/2)*math.cos (te/2)*math.cos (si/2)+math.sin (fi/2)*math.sin (te/2)*math.sin (si/2)
    pose.orientation.x = math.sin (fi/2)*math.cos (te/2)*math.cos (si/2)-math.cos (fi/2)*math.sin (te/2)*math.sin (si/2)
    pose.orientation.y = math.cos (fi/2)*math.sin (te/2)*math.cos (si/2)+math.sin (fi/2)*math.cos (te/2)*math.sin (si/2)
    pose.orientation.z = math.cos (fi/2)*math.cos (te/2)*math.sin (si/2)+math.sin (fi/2)*math.sin (te/2)*math.cos (si/2)
    pose.position.x = x
    pose.position.y = y
    pose.position.z = z
    return pose
    
#start_position = set_pose(0.4, 0.15, 0.2)
#end_position = set_pose(0.2, 0.15, 0.2)    

waypoint1 = set_pose(0.2, 0.45, 0.095)
waypoint2 = set_pose(0.2, 0.45, 0.1)
waypoint3 = set_pose(0.21, 0.45, 0.12)
waypoint4 = set_pose(0.2, 0.45, 0.15)
waypoint5 = set_pose(0.2, 0.45, 0.2)

while not rospy.is_shutdown():  
        
    #group[0].set_pose_target(start_position)
    #group[0].go(wait=True)
    
    #rospy.sleep(2)
    
    waypoints = [waypoint1,waypoint2,waypoint3,waypoint4,waypoint5]

    (plan, fraction) = group[0].compute_cartesian_path(waypoints, 0.01, 0.0)
    group[0].execute(plan, wait=True)
     

 
    #group[0].set_pose_target(end_position)
    #group[0].go(wait=True)
    
    #rospy.sleep(2)



  
'''
pose_goal.orientation.w = 0.0
pose_goal.position.x = 0.4 # red line      0.2   0.2
pose_goal.position.y = 0.15  # green line  0.15   0.15
pose_goal.position.z = 0.5  # blue line   # 0.35   0.6
group[0].set_pose_target(pose_goal)
group[0].go(True)
'''
moveit_commander.roscpp_shutdown()
