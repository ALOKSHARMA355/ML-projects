import sys 
import os
from src.logger import logging
from src.exception import CustomException
from src.utils import Read_SQL_Data
import pandas as pd
from dataclasses import dataclass #type:ignore
from sklearn.model_selection import train_test_split

@dataclass
class DataIngestionConfig:
    train_data_path=os.path.join("Artifact","train_data.csv")
    test_data_path=os.path.join("Artifact","test_data.csv")
    student_data_path=os.path.join("Artifact","student.csv")

class DataIngestion:
    def __init__(self):
        self.Ingestion_data_config=DataIngestionConfig()
    
    def Inetiate_Data_Ingestion(self):
        try:
            #Reading data from database
            logging.info("Reading data from database")
            os.makedirs(os.path.dirname(self.Ingestion_data_config.train_data_path),exist_ok=True)
            # df=Read_SQL_Data()
            df=pd.read_csv(os.path.join('notebook/data','student.csv'))

            df.to_csv(self.Ingestion_data_config.student_data_path,index=False,header=True)
            train_set,test_set=train_test_split(df,test_size=0.2,random_state=42)
            train_set.to_csv(self.Ingestion_data_config.train_data_path,index=False,header=True)
            test_set.to_csv(self.Ingestion_data_config.test_data_path,index=False,header=True)

            return(
                self.Ingestion_data_config.train_data_path,
                self.Ingestion_data_config.test_data_path
            )
        except Exception as e:
            raise CustomException(e,sys)
