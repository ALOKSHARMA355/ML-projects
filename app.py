from src.exception import CustomException 
from src.logger import logging 
import sys



if __name__=="__main__":    
    try:
        a=1/0
    except Exception as e:
        raise CustomException(e,sys)