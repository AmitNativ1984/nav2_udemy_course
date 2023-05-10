from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    
    ld = LaunchDescription()
    
    control_node = Node(
        package="control",
        executable="mtb_control_node"
    )
    
    ld.add_action(control_node)
    return ld
    