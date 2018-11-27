import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
import json
import ssl
import time
from time import sleep
import datetime
from datetime import datetime, date, time
import rospy
from std_msgs.msg import Int32
from std_msgs.msg import String
import pandas as pd
import configparser
from sqlalchemy import create_engine
import psycopg2

config = configparser.ConfigParser()
config.read('willy.ini')
#
postgresql_pwd = config['POSTGRESQL']['PASSWORD_POSTGRESQL'] # PostgreSQL password
#
# # Make connection tot PostgreSQL database
#
db_string = 'postgresql+psycopg2://postgres:' + postgresql_pwd + '@10.10.1.35/Willy'
# # Make connection to database with correct string
#
conn = create_engine(db_string)

translate_table  = pd.read_sql_query('select * from translate_table',con=conn)

print(translate_table)

# Usage: Post status from Willy activity topic to App website every 10 seconds
willy_topic_name01 ='/navigation/current_apriltag'
willy_topic_name02 ='/willy/activity'

c_apriltag = ""
c_activity = ""

def callback01(msg):     # To send data about status of Willy because AprilTag changed
    c_apriltag = msg.data
    # translate c_apriltag to corresponding classroom using translate_table
    translate_table_select = translate_table.loc[translate_table['apriltag'] == c_apriltag]
    translate_table_select_index0 = translate_table_select.reset_index()
    c_classroom = translate_table_select_index0.at[0,'classroom']

    encoded_body = json.dumps({
        "Locatie": c_classroom,
        "Status": c_activity,
    })

    http = urllib3.PoolManager()

    r = http.request('POST', 'http://callwilly-sandbox.mxapps.io/v1/willy/Willy',
                     headers={'Content-Type': 'application/json'},
                     body=encoded_body)
    print(r.read())

def callback02(msg):     # To send data about status of Willy because activity changed
    l_activity = c_activity
    c_activity = str(msg.data)
    # wait 1 minute with status posting when Willy is available after driving to a user call
    if l_activity == "4" and c_activity =="1":
        sleep(60)
        
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
