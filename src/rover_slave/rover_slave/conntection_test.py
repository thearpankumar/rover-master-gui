import rclpy
from rclpy.node import Node
from std_msgs.msg import String

#to estanblish the connection 
print("estanblish connection : ros2 run my_subscriber my_subscriber_node --ros-args --remap my_topic:=http://192.168.1.100:8000/my_topic")
class ChatSubscriber(Node):
    def __init__(self, subscriber_ip, subscriber_port):
        super().__init__('chat_subscriber', namespace='/my_namespace',
                         ros_args=['--ros-args', '--remap', '/chat:=http://{}:{}/chat'.format(subscriber_ip, subscriber_port)])
        self.subscription = self.create_subscription(String, 'chat', self.listener_callback, 10)
        print(self.subscription)  # prevent unused variable warning
    
    def listener_callback(self, msg):
        self.get_logger().info('Received: "%s"' % msg.data)
        self.data = msg.data
        print(self.data)

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