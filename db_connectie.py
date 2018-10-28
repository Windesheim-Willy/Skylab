#Query uitvoeren op de database vanuit voorbewerkte SQL opdracht
db_string = 'postgresql+psycopg2://postgres:postgres@192.168.1.2/Yes'
# Maak connectie naar database met juiste string
conn = create_engine(db_string)
#Query uitvoeren op de database
result = pd.read_sql_query('select * from marc_regressie',con=conn)
