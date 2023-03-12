import rclpy
from std_msgs.msg import String
from rclpy.node import Node

class SentMsgs(Node):
    def __init__(self):
        super().__init__(self)
        self.pub_sent = self.create_publisher(String, 'sent_msgs', 10)

    def get_user_input(self):
        while rclpy.ok():
            user_input = input('Enter a message to publish: ')
            msg = String()
            msg.data = user_input
            self.pub_sent.publish(msg)
            