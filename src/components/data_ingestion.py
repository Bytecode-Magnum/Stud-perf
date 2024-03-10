import os
import sys
from src.exception import CustomException
from src.logger import logging
import pandas as pd
import seaborn as sns
from sklearn.model_selection import train_test_split
from dataclasses import dataclass


#: we are defining the path for the train, test and raw data
#: typically a class nmeed a constructor ie __init__ function, but the dataclass doesnt need, it creates the constructor
#: on its own
@dataclass
class DataIngestionConfig:
  train_data_path:str=os.path.join("artifacts",'train.csv')
  test_data_path:str=os.path.join("artifacts",'test.csv')
  raw_data_path:str=os.path.join("artifacts",'data.csv')
  

class DataIngestion:
  def __init__(self):
    #: this will store the path of all the above arguments of DataInmgestionConfig  ie train_data_path and all info ingestion_config
    self.ingestion_config=DataIngestionConfig()

  def initiate_data_ingestion(self):
    logging.info('Entered the data ingestion method or component')
    try:
      df=pd.read_csv("./notebook\dataset\stud.csv")
      logging.info('read the dataset from dir')
      #: since theor os dirname so it will extarct the dir name of train_data_path
      os.makedirs(os.path.dirname(self.ingestion_config.train_data_path),exist_ok=True) #: creating a directory for training
      df.to_csv(self.ingestion_config.raw_data_path,index=False) #: saved the raw data info csv file with name as data.csv
      logging.info('Train test split intiated')
      train_set,test_set=train_test_split(df,test_size=.2,random_state=43)
      train_set.to_csv(self.ingestion_config.train_data_path,index=False,header=True) #: saved the train data into train.csv
      train_set.to_csv(self.ingestion_config.test_data_path,index=False,header=True)#: test data
      logging.info('ingestion of the data completed')

      return(
        self.ingestion_config.train_data_path,
        self.ingestion_config.test_data_path,
      )
    except Exception as e:
      raise CustomException(e,sys)


if __name__=="__main__":
  obj=DataIngestion()
  obj.initiate_data_ingestion()
