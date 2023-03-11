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