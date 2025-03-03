import os
import sys
from src.exception import CustomException
from src.logger import logging

import pandas as pd

from sklearn.model_selection import train_test_split

from dataclasses import dataclass
@dataclass
class DataIngestionConfig:
    train_data_path: str = os.path.join('artifacts', "train.csv")
    # trained data is saved in the __path__ of the data folder and the file name is train.csv
    test_data_path: str = os.path.join('artifacts', "test.csv")
    # test data is saved in the __path__ of the data folder and the file name is test.csv
    raw_data_path: str = os.path.join('artifacts', "data.csv")
    
class DataIngestion:
    def __init__(self):
        self.ingestion_config = DataIngestionConfig()
        
    def initiate_data_ingestion(self):
        logging.info("Data ingestion initiated")
        try:
            # pass
            # df = pd.read_csv('E:\_Projects\ml\generic\notebook\data\stud.csv')
            # above wasnt working so used the below code to read the csv file in the df variable i.e. the dataframe
            df = pd.read_csv(r'E:\_Projects\ml\generic\notebook\data\stud.csv')

            
            # reading csv or databases in the df variable
            logging.info("Data ingestion completed for the csv file, Exported/Read the dataset as the dataframe")
            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path), exist_ok = True)
            # creating a directory for the raw data path
            df.to_csv(self.ingestion_config.train_data_path, index=False, header = True)
            # exporting the data to the raw data path
                
            logging.info("Train test split initiated")
            train_set, test_set = train_test_split(df, test_size = 0.2 , random_state = 42)
            # splitting the data into train and test set
            logging.info("Train test split completed")
            train_set.to_csv(self.ingestion_config.train_data_path, index=False, header = True)
            # exporting the train data to the train data path
            test_set.to_csv(self.ingestion_config.test_data_path, index=False, header = True)
            # exporting the test data to the test data path
                
            logging.info("Data ingestion completed")
            return(
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path,
                self.ingestion_config.raw_data_path
            )
        except Exception as e:
            # pass
            raise CustomException(e, sys)
        
        
        
        
if __name__ == '__main__':
    data_ingestion = DataIngestion()
    data_ingestion.initiate_data_ingestion()
    # calling the function to initiate the data ingestion  and export the data to the respective paths