import rclpy
import rclpy.node import Node
from std_msgs.msg import String

class Talker(Node):
    def __init__(self):
        super().__init__('talker')
        self.publisher_ = self.create_publisher(String, 'chatter', 10)
        self.timer = self.create_timer(1.0, self.time_cal;back)

    def timer_callback(self):
        msg = String()
        msg.data = 'Hello from ROS 2 Python'
        self.publisher_.publish(msg)
        self.get_logger().info(f'Publishing: {msg.data}')

    def main(arg=None):
        rclpy.init(args=args)
        node = Talker()
        rclpy.spin(node)
        node.destroy_node()
        rclpy.shutdown()

    if __name__ == '__main__':
        main()
        