import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
import json
import ssl
import random
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
while True:
    print("---------------------------------------------------")
    c_apriltag = str(random.randint(0, 21))
    c_activity = str(random.randint(1, 4))

    print("AprilTag: "+ c_apriltag + "  type:")
    # print(type(c_apriltag))
    print("Activity: " + c_activity + "  type:")
    # print(type(c_activity))

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
    # print("Error code: " + r.read())
    print("Classroom: "+ c_classroom + "  type:")
    # print(type(c_classroom))
    # print("Activity: " + c_activity + "  type:")
    # print(type(c_activity))



    waiting_time = random.randint(10, 11)
    print("waiting time = " + str(waiting_time))
    sleep(waiting_time)
