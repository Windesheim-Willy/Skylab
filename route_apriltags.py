## start python
Python
import psycopg2
import pandas as pd
from sqlalchemy import create_engine
import seaborn as sns
import matplotlib.pyplot as plt

## connect to database
db_string = 'postgresql+psycopg2://postgres:willy@10.10.1.35/Willy'
conn = create_engine(db_string)

## select navigation_apriltag 
willy_route = pd.read_sql_query('Select * from navigation_apriltag WHERE apriltag <>0 ',con=conn)

## plot counts
counts = willy_route['apriltag'].value_counts().sort_index()
walk=pd.value_counts(willy_route['apriltag']).plot.bar()
walk.set_ylabel('aantal')
walk.set_xlabel('apriltag')
plt.show(walk)







