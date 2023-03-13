import rclpy
from std_msgs.msg import String
from rclpy.node import Node

class ChatNode(Node):
    
    def __init__(self):
        super.__init__('chat_screen')

        def received_callback(msg):
            print('Received: %s' % msg.data)
        
        def sent_callback(msg):
            print('Sent: %s' % msg.data)
        
        self.received_messages = self.create_subscription(String, 'received_msgs', received_callback, 10)
        self.sent_messages = self.create_subscription(String, 'sent_msgs', sent_callback, 10)

def main(args=None) :
    rclpy.init(args=args)
    
    node = ChatNode()
    
    while rclpy.ok():
        rclpy.spin_once(node)

    node.destroy_node()
    rclpy.shutdown()
    
if __name__ == '__main__':
    main()