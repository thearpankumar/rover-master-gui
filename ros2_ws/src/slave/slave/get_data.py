import rclpy
from std_msgs.msg import String
from rclpy.node import Node
import serial

class Rover(Node):
    
    def __init__(self):
        super.__init__('rover_code')
        
        port1 = '/dev/ttyUSB0'
        baudrate1 = 9600
        port2 = '/dev/ttyUSB1'
        baudrate2 = 9600
        
        sabertooth1 = serial.Serial(port=port1, baudrate=baudrate1)
        sabertooth2 = serial.Serial(port=port2, baudrate=baudrate2)
        
        self.subscription = self.create_subscription(String, 'commands', message_callback, 10)

        def message_callback(msg):
            #print('Received message: "%s"' % msg.data)
            cmd(msg)
            
        def cmd(data):
            if data == "forward":
                print("forward")
            elif data == "backard":
                print("backard")
            elif data == "left":
                print("left")
            elif data == "right":
                print("right")
            else:
                print("invalid")
                
def main(args=None):
    rclpy.init(args=args)

    node = Rover()
    # subscription = node.create_subscription(String, 'commands', message_callback, 10)
    
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()

