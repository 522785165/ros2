#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from turtlesim.msg import Pose
from std_msgs.msg import String
import math

class NodeSubscribe02(Node):
    def __init__(self,name):
        super().__init__(name)
        self.get_logger().info("大家好，我是%s!" % name)
        # 创建订阅者
        self.command_subscribe_ = self.create_subscription(Pose,"turtle1/pose",self.command_callback,10)

    def command_callback(self,msg):
        lenth=math.sqrt(msg.x**2++msg.y**2)
        rad=math.atan2(msg.y,msg.x)
        angel=math.degrees(rad)
        self.get_logger().info(f'距离：{lenth}角度:{angel}')
      


def main(args=None):
    rclpy.init(args=args) # 初始化rclpy
    node = NodeSubscribe02("topic_subscribe_02")  # 新建一个节点
    rclpy.spin(node) # 保持节点运行，检测是否收到退出指令（Ctrl+C）
    rclpy.shutdown() # 关闭rclpy

