import rclpy
from rclpy.node import Node
from std_msgs.msg import String  # Message type to send text

class TalkerNode(Node):
    def __init__(self):
        super().__init__('talker_node')
        self.publisher = self.create_publisher(String, 'chatter', 10)
        # "chatter" is the topic name
        # 10 is the message queue size

        # Create a timer to call publish_message() every 1 second
        self.timer = self.create_timer(1.0, self.publish_message)
        self.count = 0  # To keep track of message count
        self.get_logger().info("Publisher node started!")

    def publish_message(self):
        msg = String()
        msg.data = f"Hello ROS 2! Count: {self.count}"
        self.publisher.publish(msg)  # Send the message
        self.get_logger().info(f"Published: '{msg.data}'")
        self.count += 1  # Increment counter

def main(args=None):
    rclpy.init(args=args)
    node = TalkerNode()
    rclpy.spin(node)  # Keep node alive
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
