#!/usr/bin/env python
import rospy
from std_msgs.msg import Int64
import random

def talker():
    pub = rospy.Publisher('topic_B', Int64, queue_size=10)
    rospy.init_node('talker', anonymous=True)
    rate = rospy.Rate(1) #1Hz
    while not rospy.is_shutdown():
        num = random.randint(0,1000)
        rospy.loginfo(num);
        pub.publish(num)
        rate.sleep()


if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
