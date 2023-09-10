import os
from langchain.agents import *
from langchain.llms import OpenAI
from langchain.sql_database import SQLDatabase
from langchain.agents.agent_toolkits import SQLDatabaseToolkit

# db_user = "sa"
# db_password = "Amazing@2023"
# db_host = "localhost"
# db_name = "JituUdemy"
db = SQLDatabase.from_uri("mssql+pyodbc://sa:Amazing@2023@localhost/JituUdemy?Trusted_Connection=yes")

# from sqlalchemy import create_engine
# from sqlalchemy.engine.url import URL
# from langchain.sql_database import SQLDatabase

# db_config = {  
#     'drivername': 'mssql+pyodbc',  
#     'username': "sa" + '@' + "localhost",  
#     'password': "Amazing@2023",  
#     'host': "localhost",  
#     'port': 1433,  
#     'database': "JituUdemy",  
#     'query': {'driver': 'ODBC Driver 18 for SQL Server'}  
# }  

# db_url = URL.create(**db_config)
# db = SQLDatabase.from_uri(db_url)

from langchain.chat_models import ChatOpenAI
llm = ChatOpenAI(model_name="gpt-3.5-turbo")

toolkit = SQLDatabaseToolkit(db=db)
agent_executor = create_sql_agent(
    llm=llm,
    toolkit=toolkit,
    verbose=True
)

# # agent_executor.run("How many courses are listed")


# from sqlalchemy import create_engine

# db_user = "sa"
# db_password = "Amazing@2023"
# db_host = "localhost"
# db_name = "KodiAuth"

# # Creating the connection string
# connection_string = f"mssql+pymssql://{db_user}:{db_password}@{db_host}/{db_name}?encrypt=False&trust_server_certificate=True"

# # Creating an SQLAlchemy engine
# engine = create_engine(connection_string)

# # Now you can use the engine to execute SQL queries
# # For example:
# with engine.connect() as connection:
#     result = connection.execute("SELECT * FROM Courses")
#     rows = result.fetchall()
