import rclpy
from std_msgs.msg import String
from rclpy.node import Node

class NetworkNode(Node):
    
    def __init__(self):
        super.__init__('network_data')
        
        self.publisher = self.create_publisher(String, 'commands', 10)
    
    def send(self):
        while rclpy.ok():
            self.publisher.publish('Hello World')
            
    def forward(self):
        self.publisher.publish('forward')
        
    def backward(self):
        self.publisher.publish('backward')
        
    def left(self):
        self.publisher.publish('left')
        
    def right(self):
        self.publisher.publish('right')
            
    
def main(args=None):
    rclpy.init(args)
    node = NetworkNode()
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
