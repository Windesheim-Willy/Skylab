#!/usr/bin/env python
import rospy
# To which topic on Willy we will subscribe
willy_topic_name ='counter'

from std_msgs.msg import Int32

def callback(msg):
    print msg.data
rospy.init_node('topic_subscriber')
sub = rospy.Subscriber(willy_topic_name, Int32, callback)
rospy.spin()
