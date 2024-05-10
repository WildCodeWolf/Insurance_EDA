import pandas as pd
from enum import Enum

DF = pd.read_csv('data/insurance.csv')

class Col(str, Enum):
    """One of the column names of the dataset."""
    age      = DF.columns[0]
    sex      = DF.columns[1]
    bmi      = DF.columns[2]
    children = DF.columns[3]
    smoker   = DF.columns[4]
    region   = DF.columns[5]
    charges  = DF.columns[6]
    
    def __str__(self):
        return self.value
