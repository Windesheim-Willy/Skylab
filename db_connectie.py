#start several modules
from start_willy import *
from sqlalchemy import create_engine
import psycopg2
# Make connection tot PostgreSQL database
conn_string = "host='10.10.1.35' dbname='Will_test' user='postgres' password='willy'"
conn = psycopg2.connect(conn_string)
cursor = conn.cursor()
# retrieve the records from the database




db_string = 'postgresql+psycopg2://postgres:willy@10.10.1.35/Will_test'
# Make connection to database with correct string

conn = create_engine(db_string)
# Execute query on database
result = pd.read_sql_query('select * from teller',con=conn)
print(result)
