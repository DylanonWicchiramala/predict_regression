#%%
import regression_lab.polynomial_regression as reg

import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
import matplotlib.pyplot as plt
import pylab

import pandas as pd
from clean_dat import df

#%%
print(df)
#%%
t_data = pd.DataFrame()
cur_d = df['Time'][0].day
for d in df.index:
        if df['Time'][d].day == cur_d :
            pass
        else:
            cur_d = df['Time'][d].day
            pass
        
    # %%
print(datetime.date.today())