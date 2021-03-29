#%%
import regression_lab.polynomial_regression as reg

import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
import matplotlib.pyplot as plt
import pylab

import pandas as pd
from clean_dat import df,dropnull

#%%
#plt.scatter([df['Time'][i].hour for i in range(len(df['Time'][0:100]))] , df['NOx(GT)'][0:100])
#plt.show()
#%%
col = 'NOx(GT)'
max = None
df_new = dropnull(df,col)
#print(df_new.index)
#%%
X = np.array([i.hour for i in df_new["Time"][:max]])
# X = np.array([df_new['Time'][i].hour for i in range(len(df_new['Time'][:max]))])
Y = np.array(df_new[col][:max])
reg.regression_plot(X,Y, degree = 1, M=0)
for i in range(1,25):
    reg.regression_plot(X,Y, degree =i, M=0, dataplot = False)
plt.show()

# %%
