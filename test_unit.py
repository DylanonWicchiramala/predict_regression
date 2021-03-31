#%%
import regression_lab.polynomial_regression as reg

import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
import matplotlib.pyplot as plt
import pylab

import pandas as pd
from clean_dat import data_frame

#%%
print(data_frame)
#%%
t_data = pd.DataFrame()
cur_d = data_frame['Time'][0].day
for d in data_frame.index:
        if data_frame['Time'][d].day == cur_d :
            pass
        else:
            cur_d = data_frame['Time'][d].day
            pass
        
    # %%
print(datetime.date.today())

#%%
fig = plt.figure()
ax = plt.axes(projection='3d')
ax.scatter3D(X1,X2,Y)
plt.show()

#%%
n = np.array([0,1,2,3])
print(n[:-3])
# %%
