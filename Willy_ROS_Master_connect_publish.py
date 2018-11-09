#!/usr/bin/env python
import rospy
from std_msgs.msg import Int32
# To which topic on Willy we will publish
willy_topic_name ='counter'

rospy.init_node('topic_publisher')
pub = rospy.Publisher(willy_topic_name, Int32,queue_size=25)
rate = rospy.Rate(2)
count = 0
while not rospy.is_shutdown():
    pub.publish(count)
    count += 1
    rate.sleep()