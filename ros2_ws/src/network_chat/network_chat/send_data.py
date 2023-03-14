import rclpy
from std_msgs.msg import String
from rclpy.node import Node

class NetworkNode(Node):
    
    def __init__(self):
        super().__init__('network_data')
        
        self.publisher = self.create_publisher(String, 'commands', 10)
    
    def send(self):
        while rclpy.ok():
            msg = input("Enter directions/stop: ")
            self.cmd(msg)
            self.publisher.publish('Hello World')
            
    def cmd(self,data):
        if data == "forward":
            self.forward()
        elif data == "backard":
            self.backward()
        elif data == "left":
            self.left()
        elif data == "right":
            self.right()
        else:
            print("invalid")
            
    def forward(self):
        self.publisher.publish('forward')
        
    def backward(self):
        self.publisher.publish('backward')
        
    def left(self):
        self.publisher.publish('left')
        
    def right(self):
        self.publisher.publish('right')
            
    
def main(args=None):
    rclpy.init()
    node = NetworkNode()
    node.send()
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
