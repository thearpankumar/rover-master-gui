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
        
        self.serial_thread = threading.Thread(target=self.serial_callback)
        self.serial_thread.start()

        self.get_logger().info('SerialChatNode initialized')
        
    def callback(self, msg):
        data = msg.data
        self.get_logger().info('Received: %s' % data)
        self.serial.write((data + '\n').encode('utf-8'))
        
    def serial_callback(self):
        while rclpy.ok():
            if self.serial.in_waiting > 0:
                data = self.serial.readline().decode('utf-8').strip()
                self.get_logger().info('Received: %s' % data)
                msg = String()
                msg.data = data
                self.pub.publish(msg)
