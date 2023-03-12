import rclpy
from std_msgs.msg import String

def main(args=None):
    rclpy.init(args=args)

    node = rclpy.create_node('get_commands')
    subscription = node.create_subscription(String, 'commands', message_callback, 10)
    
    
