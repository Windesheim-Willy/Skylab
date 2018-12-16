import datetime
import pandas as pd
import configparser
from sqlalchemy import create_engine
import psycopg2
import matplotlib.pyplot as plt
# import seaborn as sns

# sns.set()
def make_picture(table_name, p_title, p_x_ax, p_y_ax, p_xlabel, p_ylabel, p_name):
    teprinten = pd.read_sql_query('select * from ' + table_name, con=conn)
    fig = plt.figure()
    plt.barh(teprinten[p_x_ax], teprinten[p_y_ax], color='blue', align='center')
    plt.title(p_title + " " + datetime.datetime.now().strftime("%d %B , %Y  %H:%M:%S"), fontsize=16)
    plt.xlabel(p_xlabel, fontsize=13)
    plt.ylabel(p_ylabel, fontsize=13)
    fig.savefig(p_name)
    plt.clf()
    plt.cla()
    plt.close()
    plt.gcf().clear()


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

counter = 0
while True:
    make_picture("navigation_geometry", "Geometrie van navigatie", "id", "linear_x", "ID", "Lineair X", "navigation_geometry.png")
    make_picture("navigation_joystick", "Geometrie van joystick", "seq", "nsecs", "Seq", "Nsecs", "navigation_joystick.png")
    print(counter)
    counter += 1
