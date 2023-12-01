import os
import sys
from src.exception import CustomException
from src.logger import logging
import pandas as pd
from sklearn.model_selection import train_test_split
from dataclasses import dataclass

#from src.components.data_transformation import DataTransformationConfig
from src.components.data_transformation import DataTransformation


@dataclass
class DataIngestionConfig:
    raw_data_path : str = os.path.join('artifacts','data.csv')
    train_data_path: str = os.path.join('artifacts','train.csv')
    test_data_path : str = os.path.join('artifacts','test.csv')
    

class DataIngestion:
    def __init__(self):
        self.ingestion_config = DataIngestionConfig()
        
    def initiateDataIngestion(self):
        logging.info("Entered the data ingestion method or component")
        try:
            df = pd.read_csv('notebooks/data/laptop_price_cleaned.csv')
            logging.info('Read the dataset as dataframe')

            os.makedirs(os.path.dirname(self.ingestion_config.raw_data_path),exist_ok=True)
            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path),exist_ok=True)
            os.makedirs(os.path.dirname(self.ingestion_config.test_data_path),exist_ok=True)

            df.to_csv(self.ingestion_config.raw_data_path,index=False,header=True) 
            # header = True means the columns will be included in the first line

            logging.info('Train,test,split initiated')
            train_set,test_set = train_test_split(df,test_size=0.2,random_state=42) # train_set -> 80% dataframe , test_set -> 20% dataframe

            train_set.to_csv(self.ingestion_config.train_data_path,index=False,header=True)
            test_set.to_csv(self.ingestion_config.test_data_path,index=False,header=True)

            logging.info("Ingestion of the data is completed")

            return(
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            )

        except Exception as e:
            raise CustomException(e,sys)
        

if __name__=='__main__':
    print('Data Ingestion part!')
    obj = DataIngestion()
    train_data,test_data = obj.initiateDataIngestion()

    print('Data Transformation part!')
    data_transformation = DataTransformation()
    train_arr,test_arr,_ = data_transformation.initiate_data_transformation(train_data,test_data)