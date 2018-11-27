# Start several modules
import psycopg2
import pandas as pd
from sqlalchemy import create_engine
from datetime import datetime
import configparser

config = configparser.ConfigParser()
config.read('willy.ini')
#
postgresql_pwd = config['POSTGRESQL']['PASSWORD_POSTGRESQL'] # PostgreSQL password
#Make connection tot PostgreSQL database
db_string = 'postgresql+psycopg2://postgres:' + postgresql_pwd + '@10.10.1.35/Willy'

# Make connection to database with correct string
conn = create_engine(db_string)

# Execute query on database
df = pd.read_sql_query('Select linear_x, angular_z, timestamp from navigation_geometry ',con=conn)
df.head()
df.dtypes

# Convert timestamp from object to numeric
df['timestamp'] = pd.to_numeric(df['timestamp'])

# Convert timestamp to date
df['timestamp'] = pd.to_datetime(df['timestamp'],unit='ns')
