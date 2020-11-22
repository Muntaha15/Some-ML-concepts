import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt 
dataset =  pd.read_csv('D:\ELLAssDataset\health_data.csv')
X = dataset.iloc[:,:-1].values
y = dataset.iloc[:,-1:]
datasize = X.shape[0]
