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
        
        saber1 = serial.Serial(port=port1, baudrate=baudrate1)
        saber2 = serial.Serial(port=port2, baudrate=baudrate2)
        
        saber1Motor1 = 64
        saber1Motor2 = 192
        saber2Motor1 = 64
        saber2Motor2 = 192
        
        stop()
        
        self.subscription = self.create_subscription(String, 'commands', message_callback, 10)

        def message_callback(self, msg):
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
                
        def forward():
            
            saber1Motor1 += 5
            if saber1Motor1 > 127:
                saber1Motor1 = 127
            output = bytes([saber1Motor1])
            saber1.write(output)
            print("saber1Motor1 speed = ", saber1Motor1, " = ", output)
            
            saber1Motor2 += 5
            if saber1Motor2 > 255:
                saber1Motor2 = 255
            output = bytes([saber1Motor2])
            saber1.write(output)
            print("saber1Motor2 speed = ", saber1Motor2, " = ", output)
            
            saber2Motor1 += 5
            if saber2Motor1 > 127:
                saber2Motor1 = 127
            output = bytes([saber2Motor1])
            saber2.write(output)
            print("saber2Motor1 speed = ", saber2Motor1, " = ", output)
            
            saber2Motor2 += 5
            if saber2Motor2 > 255:
                saber2Motor2 = 255
            output = bytes([saber2Motor2])
            saber2.write(output)
            print("saber2Motor2peed = ", saber2Motor2, " = ", output)
                
        def stop():
            saber1.write(bytes([0]))
            saber2.write(bytes([0]))
                
def main(args=None):
    rclpy.init(args=args)

    node = Rover()
    # subscription = node.create_subscription(String, 'commands', message_callback, 10)
    
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()

