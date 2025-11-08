import rclpy
from rclpy.node import Node
import datetime

class SystemTimeNode(Node):
    def __init__(self):
        super().__init__('System_time_node')
        self.timer = self.create_timer(1.0,self.print_time)
        self.get_logger().info("System Time Node started")

    def print_time(self):
        now = datetime.datetime.now().strftime("%H:%M:%S")
        self.get_logger().info(f'Current System Time: {now}')
        
def main(args=None):
    rclpy.init(args=args)
    node = SystemTimeNonde()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
    