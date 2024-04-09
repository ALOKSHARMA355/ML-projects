from src.exception import CustomException 
from src.logger import logging 
from src.components.data_ingestion import DataIngestion
import sys



if __name__=="__main__":    
    try:
        data_ingestion=DataIngestion()
        data_ingestion.Inetiate_Data_Ingestion()  
    except Exception as e:
        raise CustomException(e,sys)