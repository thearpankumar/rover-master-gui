import rclpy
from std_msgs.msg import String

def main(args=None):
    rclpy.init(args=args)

    node = rclpy.create_node('commander')
    publisher = node.create_publisher(String, 'commands', 10)
    
    msg = String()
    msg.data = 'Testing...'
    
    while rclpy.ok():
        publisher.publish(msg)
        node.get_logger().info('Publishing: "%s"' % msg.data)
        rclpy.spin_once(node)
