from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration
from ament_index_python import get_package_share_directory

import os

def generate_launch_description():
    
    ld = LaunchDescription()
    
    control_params = DeclareLaunchArgument('control_params',
                                           default_value = os.path.join(get_package_share_directory('control'), 'config', 'control.yaml'))
    control_node = Node(
        package="control",
        executable="mtb_control_node",
        parameters=[LaunchConfiguration('control_params')]
    )
    
    ld.add_action(control_params)
    ld.add_action(control_node)

    return ld
    