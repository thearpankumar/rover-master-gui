import rclpy
from std_msgs.msg import String

def received_callback(msg):
    print('Received: %s' % msg.data)
    
def sent_callback(msg):
    print('Sent: %s' % msg.data)

def main(args=None) :
    rclpy.init(args=args)
    
    node = rclpy.create_node('chat_screen')
    received_messages = node.create_subscription(String, 'received_msgs', received_callback, 10)
    sent_messages = node.create_subscription(String, 'sent_msgs', sent_callback, 10)
    
    while rclpy.ok():
        rclpy.spin_once(node)

    node.destroy_node()
    rclpy.shutdown()
    
if __name__ == '__main__':
    main()