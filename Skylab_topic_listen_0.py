#!/usr/bin/env python
import rospy
from std_msgs.msg import Int32
from std_msgs.msg import String
import pandas as pd
from datetime import datetime
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

# To which topic on Willy we will subscribe

willy_topic_name01 ='/interaction/is_active'
willy_topic_name02 ='/interaction/action'
willy_topic_name03 ='/interaction/clear_text'

# Define actions on input over topics

def callback01(msg):
    print msg.data
    dt = datetime.now()
    to_add = [msg.data, dt]
    insn = 'insert into interaction_is_active (status,timestamp) values (%s,%s)'
    print(insn, to_add)
    result = conn.execute(insn,to_add)

def callback02(msg):
    print msg.data
    dt = datetime.now()
    to_add = [msg.data, dt]
    inst = 'insert into interaction_action (activity,timestamp) values (%s,%s)'
    print(insn, to_add)
    result = conn.execute(insn,to_add)

def callback03(msg):
    print msg.data
    dt = datetime.now()
    to_add = [msg.data, dt]
    insn = 'insert into interaction_clear_text (text,timestamp) values (%s,%s)'
    print(insn, to_add)
    result = conn.execute(insn,to_add)

rospy.init_node('ROS_Skylab_Fetcher')

# Store fetched data in Postgres db

sub = rospy.Subscriber(willy_topic_name01, Int32, callback01)
sub = rospy.Subscriber(willy_topic_name02, Int32, callback02)
sub = rospy.Subscriber(willy_topic_name03, String, callback03)

rospy.spin()





