#!/usr/bin/env python
import sys
import rospy
import moveit_commander
import moveit_msgs.msg
from moveit_msgs.msg import Constraints, JointConstraint

def main():
    moveit_commander.roscpp_initialize(sys.argv)
    rospy.init_node('ur5_moveit_pilz_planner', anonymous=True)

    robot = moveit_commander.RobotCommander()
    scene = moveit_commander.PlanningSceneInterface()
    group_name = "manipulator"
    move_group = moveit_commander.MoveGroupCommander(group_name)

    # Set the planner to PILZ
    move_group.set_planner_id("PILZ")

    # Define a joint constraint
    joint_constraint = JointConstraint()
    joint_constraint.joint_name = "joint_name"  # specify the joint name
    joint_constraint.position = 0.5  # target position
    joint_constraint.tolerance_above = 0.1
    joint_constraint.tolerance_below = 0.1
    joint_constraint.weight = 1.0

    constraints = Constraints()
    constraints.joint_constraints.append(joint_constraint)
    move_group.set_path_constraints(constraints)

    # Define target pose
    pose_target = geometry_msgs.msg.Pose()
    pose_target.orientation.w = 1.0
    pose_target.position.x = 0.4
    pose_target.position.y = 0.1
    pose_target.position.z = 0.4
    move_group.set_pose_target(pose_target)

    # Plan and execute
    plan = move_group.go(wait=True)
    move_group.stop()
    move_group.clear_pose_targets()

    rospy.sleep(5)
    moveit_commander.roscpp_shutdown()

if __name__ == '__main__':
    main()
