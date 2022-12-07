import numpy as np
import pandas as pd
import matplotlib.pyplot as pd
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from skleaen.preprocessing import Scalar
from sklearn.linear_model import Linear_Regression
from sklearn import train_test_split

dataset = pd.read_csv('salaryies.csv')

x = dataset.iloc[:,:-1].values
y - dataset.iloc[:,-1].values

