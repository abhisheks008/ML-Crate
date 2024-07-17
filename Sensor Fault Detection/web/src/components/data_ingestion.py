import os
import sys
from dataclasses import dataclass

import pandas as pd
from sklearn.model_selection import train_test_split

from src.constant import *
from src.exception import CustomException
from src.logger import logging
from src.utils import export_collection_as_dataframe

@dataclass
class DataIngestionConfig:
    train_data_path:str = os.path.join("artifacts","train.csv")
    raw_data_path:str = os.path.join("artifacts","data.csv")
    test_data_path:str = os.path.join("artifacts","test.csv")
    
class DataIngestion:
    def __init__(self):
        self.ingestion_config = DataIngestionConfig()
        
    def initiate_data_ingestion(self):
        logging.info("Entered initiate_data_ingestion method of DataIngestion class")
        print(os.getcwd())
        try:
            df:pd.DataFrame = export_collection_as_dataframe(db_name=MONGO_DATABASE_NAME,collection_name=MONGO_COLLECTION_NAME)

            logging.info("Exported collection as dataframe")
            
            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path),exist_ok=True)
            
            df.to_csv(self.ingestion_config.raw_data_path,index=False,header=True)
            
            train_set,test_set = train_test_split(df,test_size=0.2,random_state=42)
            
            train_set.to_csv(self.ingestion_config.train_data_path,index=False,header=True)
            
            test_set.to_csv(self.ingestion_config.test_data_path,index=False,header=True)
            
            logging.info("Exited initiate_data_ingestion method of DataIngestion class")
            
            return (self.ingestion_config.train_data_path,self.ingestion_config.test_data_path)
        
        except Exception as e:
            raise CustomException(e,sys)    