import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    package_name = 'scara_description'
    urdf_file_name = 'scara_robot.urdf'

    # Get paths
    urdf_path = os.path.join(get_package_share_directory(package_name), 'urdf', urdf_file_name)
    rviz_config_path = os.path.join(get_package_share_directory(package_name), 'rviz', 'urdf_config.rviz')

    # Read URDF Content
    with open(urdf_path, 'r') as infp:
        robot_desc = infp.read()

    return LaunchDescription([
        # 1. Robot State Publisher Node
        Node(
            package='robot_state_publisher',
            executable='robot_state_publisher',
            name='robot_state_publisher',
            output='screen',
            parameters=[{'robot_description': robot_desc}]
        ),
        # 2. Joint State Publisher GUI Node
        Node(
            package='joint_state_publisher_gui',
            executable='joint_state_publisher_gui',
            name='joint_state_publisher_gui'
        ),
        # 3. RViz2 Node
        Node(
            package='rviz2',
            executable='rviz2',
            name='rviz2',
            output='screen',
            arguments=['-d', rviz_config_path]
        )
    ])
