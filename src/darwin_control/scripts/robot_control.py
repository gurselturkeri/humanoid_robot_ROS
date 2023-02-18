#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist
import keyboard

def talker(event):
    pub = rospy.Publisher('/darwin/cmd_vel', Twist, queue_size=10)
    rospy.init_node('robotControl', anonymous=True)
    rate = rospy.Rate(10) 

    
    while not rospy.is_shutdown():
        data = Twist()
         
        if event.name == 'w':
            data.linear.x = 0.1


        pub.publish(data)
        rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass