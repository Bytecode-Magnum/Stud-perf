from dataclasses import dataclass
import os

@dataclass
class temp:
  train_path=os.path.join('new','train.csv')
  test=os.path.join('new','test.csv')



class new:
  def __init__(self):
    self.ingest=temp()
    print(self.ingest.train_path)


if __name__=="__main__":
  n=new()
  