import sqlalchemy as db
import pandas as pd
import os
from dotenv import load_dotenv
from pathlib import Path
env_path = Path("/home/ubuntu/bro/.env")
load_dotenv(dotenv_path=env_path)

#connection = db.create_engine(f'mysql+mysqlconnector://{os.getenv("db_username")}:{os.getenv("db_password")}@{os.getenv("db_hostname")}/{os.getenv("db_name")}')
fd = open('bro1.sql', 'r')
sqlFile = fd.read()
fd.close()
    
sqlCommands = """SELECT * FROM feedback"""


df = pd.read_sql_query(sqlCommands, sqlFile)
print(df)

#query = open('bro1.sql', 'r')

# df = pd.read_sql_query(sql_query, connection)
# # change server address info to point at local file instead of url for RDS on aws
# print(df)