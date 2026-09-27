import os

from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():

    urdf_file = os.path.join(
        os.path.expanduser('~/ros2_ws/src/my_robot_description'),
        'urdf',
        'my_robot.urdf'
    )

    with open(urdf_file, 'r') as file:
        robot_description = file.read()

    return LaunchDescription([

        Node(
            package='robot_state_publisher',
            executable='robot_state_publisher',
            parameters=[
                {'robot_description': robot_description}
            ]
        ),

        Node(
            package='joint_state_publisher',
            executable='joint_state_publisher'
        ),

        Node(
            package='rviz2',
            executable='rviz2'
        )
    ])
