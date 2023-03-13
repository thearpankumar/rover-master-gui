import rclpy
from std_msgs.msg import String
from rclpy.node import Node

class NetworkNode(Node):
    
    def __init__(self):
        super.__init__('network_data')
        
        self.publisher = self.create_publisher(String, 'commands', 10)
    
    msg = String()
    msg.data = 'Testing...'
    
    def send(self):
        while rclpy.ok():
            self.publisher.publish('Hello World')
            
    
def main(args=None):
    rclpy.init(args)
    node = NetworkNode()
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
