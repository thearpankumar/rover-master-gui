from inputs import get_gamepad
import math
import threading
import rclpy
from rclpy.node import Node
from std_msgs.msg import String

#command to run estanblish the connection
print("estanblish connection : ros2 run my_publisher my_publisher_node --ros-args --remap my_topic:=http://192.168.1.100:8000/my_topic")

"""
    MOTOR 1 : 
        1 = full  reverse 
        64 = stop 
        127 full forward
        64 - 1 increase full reverse 
        65 128 increase to full forward
   MOTOR 2 :
        128 = full reverse 
        192 = stop
        255 = full forward
        192 - 128 increase reverse 
        129 - 255 increase forward
"""

"""
def speed_calc1(val):
    #print("this is val ", val, "type : val ", type(val))
    if 0 > val >= -1:
        val = val * -1
        percentage = (val / 1) * 100
        print("this is val ", val)
        returnspeed = (percentage / 100) * 64
        print("this is after val ", returnspeed)
        return int(64 - returnspeed)
    elif 0 < val <= 1:
        percentage = (val / 1) * 100
        print("this is val ", val)
        returnspeed = (percentage / 100) * 64
        print("this is after val ", returnspeed)
        return int(65 + returnspeed)

def speed_calc2(val):
    if 0 > val >= -1:
        val = val * -1
        percentage = (val / 1) * 100
        print("this is val ", val)
        returnspeed = (percentage / 100) * 64
        print("return", returnspeed)
        return int(192 - returnspeed)
    elif 0 < val <= 1:
        percentage = (val / 1) * 100
        print("this is val ", val)
        returnspeed = (percentage / 100) * 64
        print("return", returnspeed)
        return int(192 + returnspeed)"""

class XboxController(object):
    MAX_TRIG_VAL = math.pow(2, 8)
    MAX_JOY_VAL = math.pow(2, 15)
    MOTOR_POSITION_OLDA = 0
    MOTOR_POSITION_OLDB = 0
    CURRENT_SPEED_MOTORA = 64
    CURRENT_SPEED_MOTORB = 192

    def __init__(self):
        self.LeftJoystickY = 0
        self.LeftJoystickX = 0
        self.RightJoystickY = 0
        self.RightJoystickX = 0
        self.motor_name = ""

        self._monitor_thread = threading.Thread(target=self._monitor_controller, args=())
        self._monitor_thread.daemon = True
        self._monitor_thread.start()

    @staticmethod
    def speed_calc1(val):
        # print("this is val ", val, "type : val ", type(val))
        if 0 > val >= -1:
            val = val * -1
            percentage = (val / 1) * 100
            print("this is val ", val)
            returnspeed = (percentage / 100) * 64
            print("this is after val ", returnspeed)
            return int(64 - returnspeed)
        elif 0 < val <= 1:
            percentage = (val / 1) * 100
            print("this is val ", val)
            returnspeed = (percentage / 100) * 64
            print("this is after val ", returnspeed)
            return int(65 + returnspeed)

    @staticmethod
    def speed_calc2(val):
        if 0 > val >= -1:
            val = val * -1
            percentage = (val / 1) * 100
            print("this is val ", val)
            returnspeed = (percentage / 100) * 64
            print("return", returnspeed)
            return int(192 - returnspeed)
        elif 0 < val <= 1:
            percentage = (val / 1) * 100
            print("this is val ", val)
            returnspeed = (percentage / 100) * 64
            print("return", returnspeed)
            return int(192 + returnspeed)

    def acceleration(self, motor_name):
        val = self
        self.motor_name = motor_name
        motor_acceleration = 1
        motor_speed_limit = [1, 127, 128, 255]
        print(f"This motor ia accelerating right now : {self.motor_name}")
        if self.motor_name == "A":
            current_value1 = val
            # Comparing old and new position of joystick
            if XboxController.MOTOR_POSITION_OLDA >= current_value1:
                # Checking if we are now sending the wrong values
                if XboxController.CURRENT_SPEED_MOTORA < motor_speed_limit[1]:
                    # Giving motor acceleration
                    XboxController.CURRENT_SPEED_MOTORA += motor_acceleration
                    main("right"+str(XboxController.CURRENT_SPEED_MOTORA))
                    #Sabertooth_Serial.write(struct.pack(">B", XboxController.CURRENT_SPEED_MOTORA))
                    XboxController.MOTOR_POSITION_OLDA = current_value1
                # If reached the limit sending constant speed
                else:
                    main("right"+str(127))
                    #Sabertooth_Serial.write(struct.pack(">B", 127))
            # Same code to decelerate
            elif XboxController.MOTOR_POSITION_OLDA < current_value1:
                if XboxController.CURRENT_SPEED_MOTORA > motor_speed_limit[0]:
                    XboxController.CURRENT_SPEED_MOTORA -= motor_acceleration
                    #Sabertooth_Serial.write(struct.pack(">B", XboxController.CURRENT_SPEED_MOTORA))
                    main("right"+str(XboxController.CURRENT_SPEED_MOTORA))
                    XboxController.MOTOR_POSITION_OLDA = current_value1
                else:
                    main("right"+str(1))
                    #Sabertooth_Serial.write(struct.pack(">B", 1))
        elif self.motor_name == "B":
            current_value2 = val
            if XboxController.MOTOR_POSITION_OLDB >= current_value2:
                if XboxController.CURRENT_SPEED_MOTORB < motor_speed_limit[3]:
                    XboxController.CURRENT_SPEED_MOTORB += motor_acceleration
                    main("right"+str(XboxController.CURRENT_SPEED_MOTORB))
                    #Sabertooth_Serial.write(struct.pack(">B", XboxController.CURRENT_SPEED_MOTORB))
                    XboxController.MOTOR_POSITION_OLDA = current_value2
                else:
                    main("right"+str(255))
                    #Sabertooth_Serial.write(struct.pack(">B", 255))
            elif XboxController.MOTOR_POSITION_OLDB < current_value2:
                if XboxController.CURRENT_SPEED_MOTORB > motor_speed_limit[2]:
                    XboxController.CURRENT_SPEED_MOTORB -= motor_acceleration
                    main("right"+str(XboxController.CURRENT_SPEED_MOTORB))
                    #Sabertooth_Serial.write(struct.pack(">B", XboxController.CURRENT_SPEED_MOTORB))
                    XboxController.MOTOR_POSITION_OLDA = current_value2
                else:
                    main("right"+str(128))
                    #Sabertooth_Serial.write(struct.pack(">B", 128))
        else:
            print("Give correct Motor name")

    def read(self):  # return the buttons/triggers that you care about in this methode

        Leftjoystick = self.LeftJoystickY
        LeftJoystickX = self.LeftJoystickX
        RightJoystickY = self.RightJoystickY
        RightJoystickX = self.RightJoystickX

        # Left Joystick
        if 0 > Leftjoystick >= -1:
            print("UP", Leftjoystick)
            bytearray0 = XboxController.speed_calc1(Leftjoystick)
            print("type byte : ", type(bytearray0))
            main("left"+str(bytearray0))
            #Sabertooth_Serial.write(struct.pack(">B", bytearray0))
        elif 0 < Leftjoystick <= 1:
            print("DOWN", Leftjoystick)
            bytearray0 = XboxController.speed_calc1(Leftjoystick)
            print("type byte : ", type(bytearray0))
            main("left"+str(bytearray0))
            #Sabertooth_Serial.write(struct.pack(">B", bytearray0))
        if 0 > LeftJoystickX >= -1:
            print("LEFT", LeftJoystickX)
            bytearray0 = XboxController.speed_calc2(LeftJoystickX)
            print("type byte : ", type(bytearray0))
            main("left"+str(bytearray0))
            #Sabertooth_Serial.write(struct.pack(">B", bytearray0))
        elif 0 < LeftJoystickX <= 1:
            print("RIGHT", LeftJoystickX)
            bytearray0 = XboxController.speed_calc2(LeftJoystickX)
            print("type byte : ", type(bytearray0))
            main("left"+str(bytearray0))
            #Sabertooth_Serial.write(struct.pack(">B", bytearray0))
        if -1 > Leftjoystick > 1 or -1 > LeftJoystickX > 1:
            print("Executing Dead Zone Command")
            if -1 > Leftjoystick > 1:
                print("DEAD LeftUP", Leftjoystick)
                main("left"+str(64))
                #Sabertooth_Serial.write(struct.pack(">B", 64))
            if -1 > LeftJoystickX > 1:
                print("DEAD LeftDown", LeftJoystickX)
                main("left"+str(192))
                #Sabertooth_Serial.write(struct.pack(">B", 192))

        # Right joystick
        if 0 > RightJoystickY >= -1:
            print("UP", RightJoystickY)
            XboxController.acceleration(RightJoystickY, "A")
        elif 0 < RightJoystickY <= 1:
            print("DOWN", RightJoystickY)
            XboxController.acceleration(RightJoystickY, "A")
        if 0 > RightJoystickX >= -1:
            print("LEFT", LeftJoystickX)
            XboxController.acceleration(RightJoystickY, "B")
        elif 0 < RightJoystickX <= 1:
            print("RIGHT", LeftJoystickX)
            XboxController.acceleration(RightJoystickY, "B")
        if -1 > RightJoystickY > 1 or -1 > RightJoystickX > 1:
            print("Executing Dead Zone Command")
            if -1 > RightJoystickY > 1:
                print("DEAD RightUP", RightJoystickY)
                #Sabertooth_Serial.write(struct.pack(">B", 64))
            if -1 > LeftJoystickX > 1:
                print("DEAD RightDown", RightJoystickX)
                #Sabertooth_Serial.write(struct.pack(">B", 192))
        return [type(Leftjoystick), type(LeftJoystickX), type(RightJoystickX), type(RightJoystickY)]

    def _monitor_controller(self):
        while True:
            events = get_gamepad()
            for event in events:
                if event.code == 'ABS_Y':
                    self.LeftJoystickY = event.state / XboxController.MAX_JOY_VAL  # normalize between -1 and 1
                elif event.code == 'ABS_X':
                    self.LeftJoystickX = event.state / XboxController.MAX_JOY_VAL  # normalize between -1 and 1
                elif event.code == 'ABS_RY':
                    self.RightJoystickY = event.state / XboxController.MAX_JOY_VAL  # normalize between -1 and 1
                elif event.code == 'ABS_RX':
                    self.RightJoystickX = event.state / XboxController.MAX_JOY_VAL  # normalize between -1 and 1
                
class ChatPublisher(Node):
    def __init__(self, publisher_ip, publisher_port,args):
        super().__init__('chat_publisher', namespace='/my_namespace',
                         ros_args=['--ros-args', '--remap', '/chat:=http://{}:{}/chat'.format(publisher_ip, publisher_port)])
        self.publisher_ = self.create_publisher(String, 'chat', 10)
        #timer_period = 2  # seconds
        #self.timer = self.create_timer(timer_period, self.timer_callback)
        self.args = args

    #def timer_callback(self):
        msg = String()
        msg.data = self.args
        self.publisher_.publish(msg)
        self.get_logger().info('Publishing: "%s"' % msg.data)

def main(args):
    rclpy.init(args=None)
    publisher_ip = '<publisher_ip>'  # replace with publisher IP address
    publisher_port = '<publisher_port>'  # replace with publisher port
    chat_publisher = ChatPublisher(publisher_ip, publisher_port, args)
    try:
        rclpy.spin(chat_publisher)
    except KeyboardInterrupt:
        pass
    chat_publisher.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    joy = XboxController()
    while True:
        #main()
        print(joy.read())

"""
import rclpy
from rclpy.node import Node
from std_msgs.msg import String


class ChatPublisher(Node):
    def __init__(self):
        super().__init__('chat_publisher')
        self.publisher_ = self.create_publisher(String, 'chat', 10)
        self.timer = self.create_timer(0.5, self.timer_callback)

    def timer_callback(self):
        msg = String()
        msg.data = input("Enter message to send: ")
        self.publisher_.publish(msg)
        self.get_logger().info('Publishing: "%s"' % msg.data)


def main(args=None):
    rclpy.init(args=args)
    chat_publisher = ChatPublisher()
    try:
        rclpy.spin(chat_publisher)
    except KeyboardInterrupt:
        pass
    chat_publisher.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()"""
