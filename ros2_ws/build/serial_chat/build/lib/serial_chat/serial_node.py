import rclpy
from rclpy.node import Node
from std_msgs.msg import String
import serial
#import threading

class SerialNode(Node):
    def __init__(self):
        super().__init__('serial_data')

        port = '/dev/ttyUSB0'
        baudrate = 9600
        
        ### self.serial = serial.Serial(port, baudrate, timeout=1)
        self.sub = self.create_subscription(String, 'serial_data', self.callback, 10)
        self.pub_sent = self.create_publisher(String, 'sent_msgs', 10)
        self.pub_received = self.create_publisher(String, 'recieved_msgs', 10)
        
        # self.serial_thread = threading.Thread(target=self.serial_callback)
        # self.serial_thread.start()

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
        
    # def callback(self, msg):
    #     data = msg.data
    #     self.get_logger().info('Received: %s' % data)
    #     self.serial.write((data + '\n').encode('utf-8'))
      
    # def serial_callback(self):
    #     while rclpy.ok():
    #         if self.serial.in_waiting > 0:
    #             data = self.serial.readline().decode('utf-8').strip()
    #             self.get_logger().info('Received: %s' % data)
    #             msg = String()
    #             msg.data = data
    #             self.pub.publish(msg)
    

                
def main(args=None):
    rclpy.init(args=args)
    
    node = SerialNode()
    rclpy.spin(node)
    node.get_user_input()
    # node.serial_thread.join()
    
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()

