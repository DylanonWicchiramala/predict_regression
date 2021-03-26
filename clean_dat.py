import regression_lab.polynomial_regression as polynomial_regression

import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
import matplotlib.pyplot as plt
import pylab

import pandas as pd


df = pd.read_csv('AirQualityUCI.csv', sep=';',header=None).dropna(axis=1)
df[0] = pd.to_datetime(df[0]+df[1][1:], format="%d/%m/%Y%H.%M.%S")
df = df.drop(1,axis=1)

head = df[0]
data = df[8:]



def drop (y):    
    ind = []
    for i in range(len(y)): 
        if y[i] == np.float(-200): ind.append(i)
    return np.delete(y,ind)
    


print(type(data[1]))
#print(df)
print(data[1])