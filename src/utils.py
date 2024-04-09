import sys
import os
import pandas as pd
from src.logger import logging
from src.exception import CustomException
from dotenv import load_dotenv
import pymysql


load_dotenv()
host=os.getenv("host")
user=os.getenv("user")
password=os.getenv("password")
db=os.getenv('db')

def Read_SQL_Data():
    try:
        logging.info("Reading SQL database started")
        mydb=pymysql.connect(
            host=host,
            user=user, 
            password=password, 
            db=db 
        ) 
        logging.info("connection established %s",mydb)
        df=pd.read_sql_query("Select * from student",mydb)
        print(df.head())

        return df
    except Exception as e:
        raise CustomException(e,sys)