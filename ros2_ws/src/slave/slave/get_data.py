import rclpy
from std_msgs.msg import String
from rclpy.node import Node

class Rover(Node):
    
    def __init__(self):
        super.__init__('rover_code')
        self.subscription = self.create_subscription(String, 'commands', message_callback, 10)

        def message_callback(msg):
            #print('Received message: "%s"' % msg.data)
            cmd()
            
        def cmd(data):
            if data == "forward":
                print("forward")
            elif data == "backard":
                print("backard")
            elif data == "left":
                print("left")
            elif data == "right":
                print("right")

def main(args=None):
    rclpy.init(args=args)

    node = Rover()
    # subscription = node.create_subscription(String, 'commands', message_callback, 10)
    
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()

