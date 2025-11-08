import rclpy
import rclpy.node import Node

class HelloNode(Node):
    def __init__(self):
        super().__init__('hello node')
        self.get_logger().info("Hello Ros 2! I am your First Python Node")

    def main(args=None):
        rcply.init(args=args)
        node = HelloNode()
        rclpy.spin(node)
        node.destroy_node()
        rclpy.shutdown()
    
    if __name__ == '__main__':
        main()
        