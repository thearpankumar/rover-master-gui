from inputs import get_gamepad
import math
import threading
import struct
import serial

# import time
# import keyboard
"""
val = 1
percentage = (val / 1) * 100
print("this is val ", val)
returnspeed = (percentage / 100) * 64
print("return", returnspeed)
en = int(192 + returnspeed)
rn = type(en)"""

Sabertooth_Serial = serial.Serial(
    port='/dev/ttyUSB0',  # SERIAL PORT on SBC
    baudrate=9600,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS)

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
        """self.LeftTrigger = 0
        self.RightTrigger = 0
        self.LeftBumper = 0
        self.RightBumper = 0
        self.A = 0
        self.X = 0
        self.Y = 0
        self.B = 0
        self.LeftThumb = 0
        self.RightThumb = 0
        self.Back = 0
        self.Start = 0
        self.LeftDPad = 0
        self.RightDPad = 0
        self.UpDPad = 0
        self.DownDPad = 0"""

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
                    Sabertooth_Serial.write(struct.pack(">B", XboxController.CURRENT_SPEED_MOTORA))
                    XboxController.MOTOR_POSITION_OLDA = current_value1
                # If reached the limit sending constant speed
                else:
                    Sabertooth_Serial.write(struct.pack(">B", 127))
            # Same code to decelerate
            elif XboxController.MOTOR_POSITION_OLDA < current_value1:
                if XboxController.CURRENT_SPEED_MOTORA > motor_speed_limit[0]:
                    XboxController.CURRENT_SPEED_MOTORA -= motor_acceleration
                    Sabertooth_Serial.write(struct.pack(">B", XboxController.CURRENT_SPEED_MOTORA))
                    XboxController.MOTOR_POSITION_OLDA = current_value1
                else:
                    Sabertooth_Serial.write(struct.pack(">B", 1))
        elif self.motor_name == "B":
            current_value2 = val
            if XboxController.MOTOR_POSITION_OLDB >= current_value2:
                if XboxController.CURRENT_SPEED_MOTORB < motor_speed_limit[3]:
                    XboxController.CURRENT_SPEED_MOTORB += motor_acceleration
                    Sabertooth_Serial.write(struct.pack(">B", XboxController.CURRENT_SPEED_MOTORB))
                    XboxController.MOTOR_POSITION_OLDA = current_value2
                else:
                    Sabertooth_Serial.write(struct.pack(">B", 255))
            elif XboxController.MOTOR_POSITION_OLDB < current_value2:
                if XboxController.CURRENT_SPEED_MOTORB > motor_speed_limit[2]:
                    XboxController.CURRENT_SPEED_MOTORB -= motor_acceleration
                    Sabertooth_Serial.write(struct.pack(">B", XboxController.CURRENT_SPEED_MOTORB))
                    XboxController.MOTOR_POSITION_OLDA = current_value2
                else:
                    Sabertooth_Serial.write(struct.pack(">B", 128))
        else:
            print("Give correct Motor name")

    def read(self):  # return the buttons/triggers that you care about in this methode

        Leftjoystick = self.LeftJoystickY
        LeftJoystickX = self.LeftJoystickX
        RightJoystickY = self.RightJoystickY
        RightJoystickX = self.RightJoystickX
        # LeftTrigger = self.LeftTrigger
        # RightTrigger = self.RightTrigger
        # LeftBumper = self.LeftBumper
        # RightBumper = self.RightBumper
        # A = self.A
        # x = self.X
        # Y = self.Y
        # B = self.B
        # LeftThumb = self.LeftThumb
        # RightThumb = self.RightThumb
        # Back = self.Back
        # Start = self.Start
        # LeftPad = self.LeftDPad
        # RightPad = self.RightDPad
        # UpDPad = self.UpDPad
        # DownDPad = self.DownDPad

        # Left Joystick
        if 0 > Leftjoystick >= -1:
            print("UP", Leftjoystick)
            bytearray0 = XboxController.speed_calc1(Leftjoystick)
            print("type byte : ", type(bytearray0))
            Sabertooth_Serial.write(struct.pack(">B", bytearray0))
        elif 0 < Leftjoystick <= 1:
            print("DOWN", Leftjoystick)
            bytearray0 = XboxController.speed_calc1(Leftjoystick)
            print("type byte : ", type(bytearray0))
            Sabertooth_Serial.write(struct.pack(">B", bytearray0))
        if 0 > LeftJoystickX >= -1:
            print("LEFT", LeftJoystickX)
            bytearray0 = XboxController.speed_calc2(LeftJoystickX)
            print("type byte : ", type(bytearray0))
            Sabertooth_Serial.write(struct.pack(">B", bytearray0))
        elif 0 < LeftJoystickX <= 1:
            print("RIGHT", LeftJoystickX)
            bytearray0 = XboxController.speed_calc2(LeftJoystickX)
            print("type byte : ", type(bytearray0))
            Sabertooth_Serial.write(struct.pack(">B", bytearray0))
        if -1 > Leftjoystick > 1 or -1 > LeftJoystickX > 1:
            print("Executing Dead Zone Command")
            if -1 > Leftjoystick > 1:
                print("DEAD LeftUP", Leftjoystick)
                Sabertooth_Serial.write(struct.pack(">B", 64))
            if -1 > LeftJoystickX > 1:
                print("DEAD LeftDown", LeftJoystickX)
                Sabertooth_Serial.write(struct.pack(">B", 192))

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
                Sabertooth_Serial.write(struct.pack(">B", 64))
            if -1 > LeftJoystickX > 1:
                print("DEAD RightDown", RightJoystickX)
                Sabertooth_Serial.write(struct.pack(">B", 192))
        return [type(Leftjoystick), type(LeftJoystickX), type(RightJoystickX), type(RightJoystickY)]

    """ RightJoystickY, RightJoystickX, LeftTrigger, RightTrigger,LeftBumper,
                RightBumper, A, x, Y, B, LeftThumb, RightThumb, Back, Start, LeftPad, RightPad, UpDPad, DownDPad]"""

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
                """elif event.code == 'ABS_Z':
                    self.LeftTrigger = event.state / XboxController.MAX_TRIG_VAL  # normalize between 0 and 1
                elif event.code == 'ABS_RZ':
                    self.RightTrigger = event.state / XboxController.MAX_TRIG_VAL  # normalize between 0 and 1
                elif event.code == 'BTN_TL':
                    self.LeftBumper = event.state
                elif event.code == 'BTN_TR':
                    self.RightBumper = event.state
                elif event.code == 'BTN_SOUTH':
                    self.A = event.state
                elif event.code == 'BTN_NORTH':
                    self.Y = event.state  # previously switched with X
                elif event.code == 'BTN_WEST':
                    self.X = event.state  # previously switched with Y
                elif event.code == 'BTN_EAST':
                    self.B = event.state
                elif event.code == 'BTN_THUMBL':
                    self.LeftThumb = event.state
                elif event.code == 'BTN_THUMBR':
                    self.RightThumb = event.state
                elif event.code == 'BTN_SELECT':
                    self.Back = event.state
                elif event.code == 'BTN_START':
                    self.Start = event.state
                elif event.code == 'BTN_TRIGGER_HAPPY1':
                    self.LeftDPad = event.state
                elif event.code == 'BTN_TRIGGER_HAPPY2':
                    self.RightDPad = event.state
                elif event.code == 'BTN_TRIGGER_HAPPY3':
                    self.UpDPad = event.state
                elif event.code == 'BTN_TRIGGER_HAPPY4':
                    self.DownDPad = event.state"""


if __name__ == '__main__':
    joy = XboxController()
    while True:
        print(joy.read())
