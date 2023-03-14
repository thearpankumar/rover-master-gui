import rclpy
from rclpy.node import Node
from std_msgs.msg import String

#command to run estanblish the connection
print("estanblish connection : ros2 run my_publisher my_publisher_node --ros-args --remap my_topic:=http://192.168.1.100:8000/my_topic")

class ChatPublisher(Node):
    def __init__(self, publisher_ip, publisher_port):
        super().__init__('chat_publisher', namespace='/my_namespace',
                         ros_args=['--ros-args', '--remap', '/chat:=http://{}:{}/chat'.format(publisher_ip, publisher_port)])
        self.publisher_ = self.create_publisher(String, 'chat', 10)
        timer_period = 2  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)


    def timer_callback(self):
        msg = String()
        msg.data = input("Enter the msg : ")
        self.publisher_.publish(msg)
        self.get_logger().info('Publishing: "%s"' % msg.data)


def main(args=None):
    rclpy.init(args=None)
    publisher_ip = '<publisher_ip>'  # replace with publisher IP address
    publisher_port = '<publisher_port>'  # replace with publisher port
    chat_publisher = ChatPublisher(publisher_ip, publisher_port)
    try:
        rclpy.spin(chat_publisher)
    except KeyboardInterrupt:
        pass
    chat_publisher.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()