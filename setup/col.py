import pandas as pd
from enum import Enum

DF = pd.read_csv('data/insurance.csv')

class Col(str, Enum):
    """One of the column names of the dataset."""
    age          = DF.columns[0]
    age2         = '$' + DF.columns[0] + '^2$'
    bmi          = DF.columns[2]
    bmi30        = 'BMI <= 30'
    charges      = DF.columns[6]
    children     = DF.columns[3]
    children_cat = f'{DF.columns[3]} category'
    line         = 'line'
    offsets      = 'offsets'
    region       = DF.columns[5]
    sex          = DF.columns[1]
    smoker       = DF.columns[4]
    
    def __str__(self) -> str:
        return self.value
    
    @staticmethod
    def pythonify(name: str) -> str:
        """Return a python-friendly column name for the given one."""
        return name.lower().replace(' ', '_').replace('#', 'nr')
