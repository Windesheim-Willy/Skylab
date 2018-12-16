import pandas as pd
import configparser
from sqlalchemy import create_engine
import psycopg2
import matplotlib as plt
import seaborn as sns

sns.set()

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

teprinten  = pd.read_sql_query('select * from navigation_geometry',con=conn)

fig = plt.figure()
plt.barh(teprinten['id'], teprinten['linear_x'], color='blue', align='center')
plt.title('Geometrie van navigatie', fontsize=16)
plt.xlabel('ID', fontsize=13)
plt.ylabel('Lineair X', fontsize=13)
plt.show()
naam = 'geometrie,jpg'
grid.fig.tight_layout(w_pad=1)
fig.savefig(naam)
plt.show()
