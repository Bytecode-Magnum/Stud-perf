import sys
import pandas as pd
from src.exception import CustomException
from src.utils import load_object
from src.utils import load_object
import os


class PredictPipeline():
  def __init__(self) -> None:
    pass


  def predict(self,df):
    try:
      model_path='./artifacts/model.pkl'
      preprocess_path='./artifacts\proprocessor.pkl'
      print('loading model')
      model=load_object(model_path)
      preprocessor=load_object(preprocess_path)
      print('models loaded')
      df_scaled=preprocessor.transform(df)
      preds=model.predict(df_scaled)
      
      return preds
    

    except Exception as e:
      raise CustomException(e,sys)

