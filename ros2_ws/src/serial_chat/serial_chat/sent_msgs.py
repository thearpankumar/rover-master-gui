import rclpy
from std_msgs.msg import String
from rclpy.node import Node

class SentMsgs(Node):
    def __init__(self):
        super().__init__(self)
        self.pub_sent = self.create_publisher(String, 'sent_msgs', 10)

        