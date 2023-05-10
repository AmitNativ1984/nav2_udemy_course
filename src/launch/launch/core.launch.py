from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch_ros.substitutions import FindPackageShare
from launch.launch_description_sources import PythonLaunchDescriptionSource

def generate_launch_description():
    
    ld = LaunchDescription()
    
    launch_control = IncludeLaunchDescription(
                        PythonLaunchDescriptionSource([
                            FindPackageShare("control"), '/launch', '/control.launch.py'])
    )
    
    launch_state_publisher = IncludeLaunchDescription(
                        PythonLaunchDescriptionSource([
                            FindPackageShare("state_publisher"), '/launch', '/state_publisher.launch.py'])
    )
    
    launch_state_estimation =  IncludeLaunchDescription(
                        PythonLaunchDescriptionSource([
                            FindPackageShare('state_estimation'), '/launch', '/state_estimation.launch.py'])
    )
    
    ld.add_action(launch_control)
    ld.add_action(launch_state_estimation)
    ld.add_action(launch_state_publisher)
    
    return ld
    