import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
import json
import ssl
import time
import datetime
from datetime import datetime, date, time
import rospy
from std_msgs.msg import Int32
from std_msgs.msg import String
import pandas as pd

# Usage: Post status from Willy activity topic to App website every 10 seconds
willy_topic_name01 ='/navigation/current_apriltag'
willy_topic_name02 ='/willy/activity'

c_classroom = ""
c_activity = ""

def callback01(msg):
    c_classroom = msg.data
    # To send data about status of Willy
    encoded_body = json.dumps({
        "Locatie": c_classroom,
        "Status": c_activity,
    })

    http = urllib3.PoolManager()

    r = http.request('POST', 'http://callwilly-sandbox.mxapps.io/v1/willy/Willy',
                     headers={'Content-Type': 'application/json'},
                     body=encoded_body)
    print(r.read())

def callback02(msg):
    c_activity = msg.data
    # To send data about status of Willy
    encoded_body = json.dumps({
        "Locatie": c_classroom,
        "Status": c_activity,
    })

    http = urllib3.PoolManager()

    r = http.request('POST', 'http://callwilly-sandbox.mxapps.io/v1/willy/Willy',
                     headers={'Content-Type': 'application/json'},
                     body=encoded_body)
    print(r.read())


rospy.init_node('app_post_status')

sub = rospy.Subscriber(willy_topic_name01, String, callback01)
sub = rospy.Subscriber(willy_topic_name02, String, callback02)

rospy.spin()
