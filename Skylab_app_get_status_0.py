import urllib3
import json
import ssl
import time
import datetime
from datetime import datetime, date, time
import rospy
from std_msgs.msg import Int32
from std_msgs.msg import String
import pandas as pd
from datetime import datetime
import configparser
from sqlalchemy import create_engine
import psycopg2

# Fetch every 10 seconds the location that was called by a user from the App site

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

# print(translate_table)

last_apriltag = ""
print('---------------------------------------------------------------')

# To which topic on Willy we will publish
willy_topic_name01 ='app/user_location'
rospy.init_node('app_get_status')
pub01 = rospy.Publisher(willy_topic_name01, String ,queue_size=25)

http = urllib3.PoolManager()
rate = rospy.Rate(0.1)
while not rospy.is_shutdown():
    status = 0

    while status != 200:
        r = http.request('GET', 'http://callwilly-sandbox.mxapps.io/v1/willy/User')
        status = r.status

    received = json.loads(r.data.decode('utf-8'))
    x = received[0]
    u_location = (x.get("Locatie"))

    a_time = '{date:%Y-%m-%d %H:%M:%S}'.format(date=datetime.now())

    print("Received at " + a_time + " location : " + u_location)
    #print(u_location)

    u_building = u_location[0:1]
    #print(u_building)

    u_floor = u_location[1:2]
    #print(u_floor)

    u_classroom = u_location[3:5]
    #print(u_classroom)

    # translate u_location to corresponding AprilTag using translate_table
    translate_table_select = translate_table.loc[translate_table['classroom'] == u_location]
    translate_table_select_index0 = translate_table_select.reset_index()
    u_apriltag = translate_table_select_index0.at[0,'apriltag']



    # publish AprilTag on topic id apriltag changed
    if last_apriltag != u_apriltag:
        pub01.publish(u_apriltag)
        print("Published on topic " + willy_topic_name01 + " AprilTag number " + u_apriltag)
        last_apriltag = u_apriltag
    else:
        print("Not published on topic " + willy_topic_name01 + " AprilTag number " + u_apriltag + " because Apriltag has not changed")
    print('---------------------------------------------------------------')
    rate.sleep()
