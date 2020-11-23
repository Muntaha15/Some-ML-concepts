import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt

#reading data from csv file
dataset =  pd.read_csv('D:\ELLAssDataset\health_data.csv')
X = dataset.iloc[:,:-1].values
y = dataset.iloc[:,-1:].values

datasize = dataset.shape[0]
X_train = X[:(datasize*7)//10,:]
y_train = y[:(datasize*7)//10,:]
X_test = X[(datasize*7)//10:,:]
y_test = y[(datasize*7)//10:,:]


