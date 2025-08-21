#!/usr/bin/env python3
import rospy
from std_msgs.msg import Char
from geometry_msgs.msg import Twist

def callback(msg):
    # Convert received ASCII code back to character
    command = chr(msg.data)
    rospy.loginfo(f"Received through /orders: {command}")   # log received key

    twist = Twist()

    # Reset all velocities before setting
    twist.linear.x = 0
    twist.linear.y = 0
    twist.linear.z = 0
    twist.angular.x = 0
    twist.angular.y = 0
    twist.angular.z = 0

    # Map keyboard commands to robot motion
    if command == 'W':      # forward
        twist.linear.x = 0.33
    elif command == 'S':    # backward
        twist.linear.x = -0.33
    elif command == 'A':    # rotate left
        twist.angular.z = 0.2
    elif command == 'D':    # rotate right
        twist.angular.z = -0.2
    elif command == 'Q':    # strafe left (if supported)
        twist.linear.y = 0.2
    elif command == 'E':    # strafe right (if supported)
        twist.linear.y = -0.2
    else:
        rospy.loginfo(f"Received unknown command: {command}")

    # Publish Twist message
    cmd_pub.publish(twist)
    rospy.loginfo(f"Published Twist -> linear.x: {twist.linear.x}, linear.y: {twist.linear.y}, angular.z: {twist.angular.z}")

def listener():
    rospy.init_node('orders_to_cmdvel', anonymous=True)
    rospy.Subscriber("/orders", Char, callback)
    rospy.spin()

if __name__ == '__main__':
    cmd_pub = rospy.Publisher("/cmd_vel", Twist, queue_size=10)
    listener()
