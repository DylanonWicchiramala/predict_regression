#%%
import regression_lab.polynomial_regression as reg

import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
import matplotlib.pyplot as plt
import pylab

import pandas as pd
from clean_dat import df,dropnull
from mpl_toolkits import mplot3d

#%%
#plt.scatter([df['Time'][i].hour for i in range(len(df['Time'][0:100]))] , df['NOx(GT)'][0:100])
#plt.show()
#%%
col = 'NOx(GT)'
max = (360)
df_new = dropnull(df,col)
#print(df_new.index)
#%%
X1 = np.array([i.hour for i in df_new["Time"][:max]])
X2 = np.array([365*i.year + 31*i.month + i.day for i in df_new["Time"][:max]])
print(X2)
Y = np.array(df_new[col][:max])
reg.regression_plot(X2,Y, degree = 1, margin=0)
plt.show()

# %%
fig = plt.figure()
ax = plt.axes(projection='3d')
ax.scatter3D(X1,X2,Y)
plt.show()