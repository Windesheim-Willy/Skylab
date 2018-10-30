# Make connection tot PostgreSQL database
db_string = 'postgresql+psycopg2://postgres:postgres@192.168.1.2/Yes'
# Make connection to database with correct string
conn = create_engine(db_string)
# Execute query on database
result = pd.read_sql_query('select * from marc_regressie',con=conn)
