import struct
import serial
import rclpy
from rclpy.node import Node
from std_msgs.msg import String

#to estanblish the connection 
print("estanblish connection : ros2 run my_subscriber my_subscriber_node --ros-args --remap my_topic:=http://192.168.1.100:8000/my_topic")

device_name1 = str(input("Enter device 1 address: "))
device_name2 = str(input("Enter device 2 address: "))
Sabertooth_Serial_motorA = serial.Serial(
    port=device_name1,  # SERIAL PORT on SBC
    baudrate=9600,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS)

Sabertooth_Serial_motorB = serial.Serial(
    port=device_name2,  # SERIAL PORT on SBC
    baudrate=9600,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS)

class ChatSubscriber(Node):
    def __init__(self, subscriber_ip, subscriber_port):
        super().__init__('chat_subscriber', namespace='/my_namespace',
                         ros_args=['--ros-args', '--remap', '/chat:=http://{}:{}/chat'.format(subscriber_ip, subscriber_port)])
        self.subscription = self.create_subscription(String, 'chat', self.listener_callback, 10)
        print(self.subscription)  # prevent unused variable warning
    
    def listener_callback(self, msg):
        self.get_logger().info('Received: "%s"' % msg.data)
        self.data = msg.data
        try:
            if self.data.index("left") == 0:
                Sabertooth_Serial_motorA.write(struct.pack(">B", int(self.data.replace("left"))))
            if self.data.index("right") == 0:
                Sabertooth_Serial_motorA.write(struct.pack(">B", int(self.data.replace("right"))))
        except Exception as E:
            print(E)
            pass

def main(args=None):
    rclpy.init(args=args)
    subscriber_ip = '<subscriber_ip>'  # replace with subscriber IP address
    subscriber_port = '<subscriber_port>'  # replace with subscriber port
    chat_subscriber = ChatSubscriber(subscriber_ip, subscriber_port)
    try:
        rclpy.spin(chat_subscriber)
    except KeyboardInterrupt:
        pass
    chat_subscriber.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()

"""import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class ChatSubscriber(Node):
    def __init__(self):
        super().__init__('chat_subscriber')
        self.subscription = self.create_subscription(String, 'chat', self.listener_callback, 10)
        print("self subscrption", self.subscription)  # prevent unused variable warning

    def listener_callback(self, msg):
        self.get_logger().info('Received: "%s"' % msg.data)
        self.print = self.get_logger().info('Received: "%s"' % msg.data)
        self.data = msg.data
        print(self.data)

def main(args=None):
    rclpy.init(args=args)
    chat_subscriber = ChatSubscriber()
    rclpy.spin(chat_subscriber)
    chat_subscriber.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()"""

