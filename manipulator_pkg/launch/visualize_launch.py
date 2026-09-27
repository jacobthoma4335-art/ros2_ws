#!/usr/bin/env python3
import os
from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    urdf = os.path.expanduser('~/ros2_ws/src/manipulator_pkg/urdf/two_link.urdf')
    with open(urdf, 'r') as f: robot_desc = f.read()

    return LaunchDescription([
        Node(package='robot_state_publisher', executable='robot_state_publisher', parameters=[{'robot_description': robot_desc}]),
        Node(package='joint_state_publisher_gui', executable='joint_state_publisher_gui'),
        Node(package='rviz2', executable='rviz2')
    ])

