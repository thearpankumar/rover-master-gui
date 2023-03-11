import rclpy
from rclpy.node import Node
from std_msgs.msg import String
import serial
import threading

class SerialChatNode(Node):
    def __init__(self):
        super().__init__('serial_chat')

        port = '/dev/ttyUSB0'
        baudrate = 115200
        
        self.serial = serial.Serial(port, baudrate, timeout=1)
        self.sub = self.create_subscription(String, 'serial_chat', self.callback, 10)
        self.pub = self.create_publisher(String, 'serial_chat', 10)
