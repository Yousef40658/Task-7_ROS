#!/usr/bin/env python3

import rospy
import keyboard                                                
from std_msgs.msg import Char
from enum import Enum





if __name__ == "__main__" :
    #publisher node
    rospy.init_node("Keyboard")
    pub = rospy.Publisher("/orders" ,Char , queue_size= 10)
    rospy.loginfo("Press W/A/S/D/E/Q (ESC to quit)...")

    #to make it more controllable
    rate = rospy.Rate(50)




    while not rospy.is_shutdown() :
        event = keyboard.read_event(suppress=False)                           #waits for key press/release _>no need to press enter
        if event.event_type == keyboard.KEY_DOWN :              #button pressed 
            key = event.name.upper()

            if key in ["W" , "A" , "S" , "D" , "Q" , "E"] :
                pub.publish((ord(key)))                        #ord returns the ASCII of the char

            elif key == 'ESC' :
                break

            else :
                rospy.loginfo("Press W/A/S/D/E/Q (ESC to quit)...")
        
        rate.sleep()

    



