#!/usr/bin/env python

import rospy
from std_msgs.msg import String

def talker():
    pub = rospy.Publisher('chatter_py', String, queue_size=10)
    rospy.init_node('talker_py', anonymous=True)

    rate = rospy.Rate(10) # 10hz

    count = 0
    while not rospy.is_shutdown():

        count = count % 255
        hello_str = "hello world %s" % count

        rospy.loginfo_throttle(10, hello_str)

        pub.publish(hello_str)
        rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass