#!/usr/bin/env python

#######################THE FIRST POSITION OF THE ROBOT SHOULD BE PROPER###################

import sys
import rospy
import tf
import moveit_commander
import geometry_msgs.msg
import moveit_msgs.msg
from math import pi

# Initialize MoveIt and ROS node
moveit_commander.roscpp_initialize(sys.argv)
rospy.init_node('ur3_move', anonymous=True)

# Initialize robot, scene, and move group
robot = moveit_commander.RobotCommander()
scene = moveit_commander.PlanningSceneInterface()
group_name = "manipulator"
move_group = moveit_commander.MoveGroupCommander(group_name)

# Set the planner to RRTstar
move_group.set_planner_id("RRTstar")

# Set the planner
#move_group.set_planner_id("Cartesian Path Planning") 

# You can also set the planning time
move_group.set_planning_time(15)  # was 10

xx = 1

while not rospy.is_shutdown():

    #Get the current pose of the end effector
    current_pose = move_group.get_current_pose().pose
    
    # Create a list of waypoints
    waypoints = []
    
    if xx % 2 == 1:
        # First target pose (Relative to the current position)
        pose_target = geometry_msgs.msg.Pose()

        # Convert Euler angles to quaternion (you already have this)
        euler = (pi / 180) * -180, 0, 0
        quaternion = tf.transformations.quaternion_from_euler(*euler)

        # Set orientation
        pose_target.orientation.x = quaternion[0]
        pose_target.orientation.y = quaternion[1]
        pose_target.orientation.z = quaternion[2]
        pose_target.orientation.w = quaternion[3]
        
        # Define position relative to current pose
        pose_target.position.x = 0.4  # Set desired position
        pose_target.position.y = 0.15
        pose_target.position.z = current_pose.position.z
    
        waypoints.append(pose_target)

        pose_target2 = geometry_msgs.msg.Pose()
        pose_target2.position.x = pose_target.position.x  # Keep X from the previous target
        pose_target2.position.y = pose_target.position.y  # Keep Y from the previous target
        pose_target2.position.z = 0.18  
        pose_target2.orientation = pose_target.orientation 
       
        waypoints.append(pose_target2)        

    else:
        # Second target pose (Relative to the current position)
        pose_target = geometry_msgs.msg.Pose()

        # Set orientation (using the same quaternion as before)
        pose_target.orientation.x = quaternion[0]
        pose_target.orientation.y = quaternion[1]
        pose_target.orientation.z = quaternion[2]
        pose_target.orientation.w = quaternion[3]
        
        # Define position relative to current pose
        pose_target.position.x = 0.2
        pose_target.position.y = 0.45
        pose_target.position.z = current_pose.position.z
        
        waypoints.append(pose_target)
    
        # Add second waypoint to move Z to 0.18
        pose_target2 = geometry_msgs.msg.Pose()
        pose_target2.position.x = pose_target.position.x  # Keep X from the previous target
        pose_target2.position.y = pose_target.position.y  # Keep Y from the previous target
        pose_target2.position.z = 0.095  # Set Z to 0.18 meters
        pose_target2.orientation = pose_target.orientation 
       
        waypoints.append(pose_target2)
    # Plan the Cartesian path
    (plan, fraction) = move_group.compute_cartesian_path(
        waypoints,   # waypoints to follow
        0.01,  #0.005 or 0.02      # eef_step: resolution of the path in meters (finer control)
        1.8  #0 means not applied          # jump_threshold: avoid large jumps in joint space
    )

    # Execute the plan
    if fraction > 0.9:  # Only execute if most of the path was planned successfully
        move_group.execute(plan, wait=True)
    
    #move_group.execute(plan, wait=True)

    move_group.stop()
    move_group.clear_pose_targets()

    # Increment xx for alternating between the two poses
    xx += 1

    # Add some sleep to avoid overloading
    rospy.sleep(0.1)

# Shut down MoveIt cleanly
moveit_commander.roscpp_shutdown()

