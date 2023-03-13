import rclpy
from rclpy.node import Node
from std_msgs.msg import String
import serial

"""
def main(args=None) :
    rclpy.init(args=args)
    
    port = '/dev/ttyUSB0'
    baudrate = 9600
    
    node = rclpy.create_node('serial_data')
    pub_sent = node.create_publisher(String, 'sent_msgs', 10)
    pub_received = node.create_publisher(String, 'recieved_msgs', 10)
    
    def callback(self, received_data):
        ### received_data = serial.readline().decode().strip()
        pub_received.publish(received_data)
        
    sub = node.create_subscription(String, 'serial_data', callback, 10)
    
    while rclpy.ok():
        user_input = input('Enter a message to publish: ')
        msg = String()
        msg.data = user_input
        ### serial.write(msg.data.encode())
        pub_sent.publish(msg)

    node.destroy_node()
    rclpy.shutdown()
"""

class SerialNode(Node):
    def __init__(self):
        super().__init__('serial_data')

        port = '/dev/ttyUSB0'
        baudrate = 9600
        
        ### self.serial = serial.Serial(port, baudrate, timeout=1)
        self.sub = self.create_subscription(String, 'serial_data', self.callback, 10)
        self.pub_sent = self.create_publisher(String, 'sent_msgs', 10)
        self.pub_received = self.create_publisher(String, 'recieved_msgs', 10)

        self.get_logger().info('SerialNode initialized')
        
    def callback(self, received_data):
        ### received_data = serial.readline().decode().strip()
        self.pub_received.publish(received_data)
        
    def get_user_input(self):
        while rclpy.ok():
            user_input = input('Enter a message to publish: ')
            msg = String()
            msg.data = user_input
            ### serial.write(msg.data.encode())
            self.pub_sent.publish(msg)
        
       
def main(args=None):
    rclpy.init(args=args)
    
    node = SerialNode()
    rclpy.spin(node)
    node.get_user_input()
    
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()

