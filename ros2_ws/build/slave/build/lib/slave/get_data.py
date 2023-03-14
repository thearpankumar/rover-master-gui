import rclpy
from std_msgs.msg import String
from rclpy.node import Node
import serial

class Rover(Node):
    
    def __init__(self):
        super().__init__('rover_code')
        
        # port1 = '/dev/ttyUSB0'
        # baudrate1 = 9600
        # port2 = '/dev/ttyUSB1'
        # baudrate2 = 9600
        
        # self.saber1 = serial.Serial(port=port1, baudrate=baudrate1)
        # self.saber2 = serial.Serial(port=port2, baudrate=baudrate2)
        
        self.saber1Motor1 = 64
        self.saber1Motor2 = 192
        self.saber2Motor1 = 64
        self.saber2Motor2 = 192
        
        self.stop()
        
        self.subscription = self.create_subscription(String, 'commands', self.message_callback, 10)

    def message_callback(self, msg):
        #print('Received message: "%s"' % msg.data)
        self.cmd(msg)
        
    def user_input(self):
        while rclpy.ok:
            msg = input("Enter directions/stop: ")
            self.cmd(msg)
        self.stop()
    
    def cmd(self,data):
        if data == "forward":
            self.forward()
        elif data == "backward":
            self.backward()
        elif data == "left":
            self.left()
        elif data == "right":
            self.right()
        else:
            print("invalid")
            
    def forward(self):
        
        self.saber1Motor1 += 5
        if self.saber1Motor1 > 127:
            self.saber1Motor1 = 127
        output = bytes([self.saber1Motor1])
        # self.saber1.write(output)
        print("saber1Motor1 speed = ", self.saber1Motor1, " = ", output)
        
        self.saber1Motor2 += 5
        if self.saber1Motor2 > 255:
            self.saber1Motor2 = 255
        output = bytes([self.saber1Motor2])
        # self.saber1.write(output)
        print("saber1Motor2 speed = ", self.saber1Motor2, " = ", output)
        
        self.saber2Motor1 += 5
        if self.saber2Motor1 > 127:
            self.saber2Motor1 = 127
        output = bytes([self.saber2Motor1])
        # self.saber2.write(output)
        print("saber2Motor1 speed = ", self.saber2Motor1, " = ", output)
        
        self.saber2Motor2 += 5
        if self.saber2Motor2 > 255:
            self.saber2Motor2 = 255
        output = bytes([self.saber2Motor2])
        # self.saber2.write(output)
        print("saber2Motor2peed = ", self.saber2Motor2, " = ", output)
        
    def backward(self):
        
        self.saber1Motor1 -= 5
        if self.saber1Motor1 < 1:
            self.saber1Motor1 = 1
        output = bytes([self.saber1Motor1])
        # self.saber1.write(output)
        print("saber1Motor1 speed = ", self.saber1Motor1, " = ", output)
        
        self.saber1Motor2 -= 5
        if self.saber1Motor2 < 128:
            self.saber1Motor2 = 128
        output = bytes([self.saber1Motor2])
        # self.saber1.write(output)
        print("saber1Motor2 speed = ", self.saber1Motor2, " = ", output)
        
        self.saber2Motor1 -= 5
        if self.saber2Motor1 < 1:
            self.saber2Motor1 = 1
        output = bytes([self.saber2Motor1])
        # self.saber2.write(output)
        print("saber2Motor1 speed = ", self.saber2Motor1, " = ", output)
        
        self.saber2Motor2 -= 5
        if self.saber2Motor2 < 128:
            self.saber2Motor2 = 128
        output = bytes([self.saber2Motor2])
        # self.saber2.write(output)
        print("saber2Motor2peed = ", self.saber2Motor2, " = ", output)
        
    def left(self):
        
        self.saber1Motor1 = 127
        # if self.saber1Motor1 > 127:
        #     self.saber1Motor1 = 127
        output = bytes([self.saber1Motor1])
        # self.saber1.write(output)
        print("saber1Motor1 speed = ", self.saber1Motor1, " = ", output)
        
        self.saber1Motor2 = 255
        # if self.saber1Motor2 > 255:
        #     self.saber1Motor2 = 255
        output = bytes([self.saber1Motor2])
        # self.saber1.write(output)
        print("saber1Motor2 speed = ", self.saber1Motor2, " = ", output)
        
        self.saber2Motor1 = 1
        # if self.saber2Motor1 > 127:
        #     self.saber2Motor1 = 127
        output = bytes([self.saber2Motor1])
        # self.saber2.write(output)
        print("saber2Motor1 speed = ", self.saber2Motor1, " = ", output)
        
        self.saber2Motor2 = 128
        # if self.saber2Motor2 > 255:
        #     self.saber2Motor2 = 255
        output = bytes([self.saber2Motor2])
        # self.saber2.write(output)
        print("saber2Motor2peed = ", self.saber2Motor2, " = ", output)
        
    def right(self):
        
        self.saber1Motor1 = 1
        # if self.saber1Motor1 > 127:
        #     self.saber1Motor1 = 127
        output = bytes([self.saber1Motor1])
        # self.saber1.write(output)
        print("saber1Motor1 speed = ", self.saber1Motor1, " = ", output)
        
        self.saber1Motor2 = 128
        # if self.saber1Motor2 > 255:
        #     self.saber1Motor2 = 255
        output = bytes([self.saber1Motor2])
        # self.saber1.write(output)
        print("saber1Motor2 speed = ", self.saber1Motor2, " = ", output)
        
        self.saber2Motor1 = 127
        # if self.saber2Motor1 > 127:
        #     self.saber2Motor1 = 127
        output = bytes([self.saber2Motor1])
        # self.saber2.write(output)
        print("saber2Motor1 speed = ", self.saber2Motor1, " = ", output)
        
        self.saber2Motor2 = 255
        # if self.saber2Motor2 > 255:
        #     self.saber2Motor2 = 255
        output = bytes([self.saber2Motor2])
        # self.saber2.write(output)
        print("saber2Motor2peed = ", self.saber2Motor2, " = ", output)
            
    def stop(self):
        # self.saber1.write(bytes([0]))
        # self.saber2.write(bytes([0]))
        print("stop")
                
def main(args=None):
    rclpy.init()

    node = Rover()
    # subscription = node.create_subscription(String, 'commands', message_callback, 10)
    node.user_input()
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()

