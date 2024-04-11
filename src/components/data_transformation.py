import sys 
import os 
import pandas as pd 
import numpy as np 
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder
from src.exception import CustomException
from src.logger import logging 
from src.utils import Read_SQL_Data,save_obj
from dataclasses import dataclass #type:ignore

@dataclass
class Data_Preprocessing:
    preprocessing_data_obj_file_path=os.path.join("Artifact","preprocessing.pkl")


class DataTransformation:
    def __init__(self):
        self.get_preprocessor_path=Data_Preprocessing()

    def Get_Data_Transformation_Obj(self):
        try:
            numerical_columns = ["writing_score", "reading_score"]
            categorical_columns = [
                    "gender",
                    "race_ethnicity",
                    "parental_level_of_education",
                    "lunch",
                    "test_preparation_course",
                ]
            numeriacal_pipeline=Pipeline(steps=[
                ("SimplerImputer",SimpleImputer(strategy="mean")),
                 ("StandardScaler",StandardScaler())
            ])
            cat_pipeline=Pipeline(steps=[
                ("SimplerImputer",SimpleImputer(strategy="most_frequent")),
                ("OneHotencoding",OneHotEncoder()),
                ("scaler",StandardScaler(with_mean=False))
            ])
            preprocessor=ColumnTransformer([
                ("numerical",numeriacal_pipeline,numerical_columns),
                ("categorical",cat_pipeline,categorical_columns)
            ])
            return preprocessor
        except Exception as e:
            raise CustomException(e,sys)
        
    def initiate_data_transformation(self,train_path,test_path):
        try:
            train_df=pd.read_csv(train_path)
            test_df=pd.read_csv(test_path)
            logging.info("reading the train data and test data")

            preprocessing_obj=self.Get_Data_Transformation_Obj()

            target_column_name="math_score"
            numerical_columns = ["writing_score", "reading_score"]

            #dividing the train into input feature and target feature
            input_feature_train_df=train_df.drop(columns=[target_column_name],axis=1)
            target_feature_train_df=train_df[target_column_name]

            #dividing the test data into input feature and target feature
            input_feature_test_df=test_df.drop(columns=[target_column_name],axis=1)
            target_feature_test_df=test_df[target_column_name]

            logging.info("Applying Preprocessing on training and test dataframe")

            input_feature_train_arr=preprocessing_obj.fit_transform(input_feature_train_df)
            input_feature_test_arr=preprocessing_obj.transform(input_feature_test_df)


            train_arr = np.c_[
                input_feature_train_arr, np.array(target_feature_train_df)
            ]
            test_arr = np.c_[input_feature_test_arr, np.array(target_feature_test_df)]

            logging.info(f"Saved preprocessing object")

            save_obj(

                file_path=self.get_preprocessor_path.preprocessing_data_obj_file_path,
                obj=preprocessing_obj
            )

            return (

                train_arr,
                test_arr,
                self.get_preprocessor_path.preprocessing_data_obj_file_path
            )
             
        except Exception as e :
            raise CustomException(e,sys)
