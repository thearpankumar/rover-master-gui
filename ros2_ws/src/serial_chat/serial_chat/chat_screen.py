import rclpy
from std_msgs.msg import String

def main(args=None) :
    rclpy.init(args=args)
    
    node = rclpy.create_node('chat_screen')
    chat_messages = node.create_subscription(String, 'chat', callback, 10)