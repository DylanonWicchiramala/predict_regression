#import regression_lab.polynomial_regression as polynomial_regression

import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
import matplotlib.pyplot as plt
import pylab

import pandas as pd

df = pd.read_csv('AirQualityUCI.csv', sep=';',header=None)
df = df.dropna(axis=1)

df_n = df.to_numpy()
df_nc = lambda col: df[col].to_numpy()
