import rclpy
from rclpy.node import Node
from ros2_ws.src.serial_chat.serial_chat.gui import AppGui

class guiNode(Node) :
    def __init__(self):
        super.__init__('guiNode')
        
        self.gui = AppGui()
        
def main(args=None):
    rclpy.init(args=args)
    node = guiNode()

    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
