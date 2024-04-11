from src.exception import CustomException 
from src.logger import logging 
from src.components.data_ingestion import DataIngestion
from src.components.data_transformation import DataTransformation
from src.components.model_trainer import ModelTrainer
import sys



if __name__=="__main__":    
    try:
        #data_ingestion_config=DataIngestionConfig()
        data_ingestion=DataIngestion()
        train_data_path,test_data_path=data_ingestion.Inetiate_Data_Ingestion()

        #data_transformation_config=DataTransformationConfig()
        data_transformation=DataTransformation()
        train_arr,test_arr,_=data_transformation.initiate_data_transformation(train_data_path,test_data_path)

        #ModelTrainer

        model_trainer=ModelTrainer()
        print(model_trainer.intiate_model_trainer(train_arr,test_arr))

    except Exception as e:
        raise CustomException(e,sys)