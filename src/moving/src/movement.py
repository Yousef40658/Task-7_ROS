#!/usr/bin/env python3
import rospy
from std_msgs.msg import String
from geometry_msgs.msg import Twist

def callback(msg):
    command = msg.data.strip()
    twist = Twist()

    if command == 'W':      # للأمام
        twist.linear.x = 0.33
    elif command == 'S':    # للخلف
        twist.linear.x = -0.33
    elif command == 'A':    # لليسار (دوران)
        twist.angular.z = 0.2
    elif command == 'D':    # لليمين (دوران)
        twist.angular.z = -0.2
    else:
        rospy.loginfo("Received unknown command: %s", command)


    cmd_pub.publish(twist)

def listener():
    rospy.init_node('orders_to_cmdvel', anonymous=True)
    rospy.Subscriber("orders", String, callback)
    rospy.spin()

if __name__ == '__main__':
    cmd_pub = rospy.Publisher("/cmd_vel", Twist, queue_size=10)
    listener()