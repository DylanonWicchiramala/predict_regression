#%%
import numpy as np
import matplotlib.pyplot as plt
import pylab
import datetime
import pandas as pd

# delete not available data.
def dropnull(df,col=None):    
    ind = []
    if col is None :
        for i in range(len(df)): 
            if df[i] == -200: ind.append(i)
    else:
        for i in range(len(df)): 
            if df[col][i] == -200: ind.append(i)
    return df.drop(ind)

df = pd.read_csv('AirQualityUCI.csv', sep=';',).dropna(axis=1)
df["Time"] = pd.to_datetime(df['Date']+df['Time'][:], format="%d/%m/%Y%H.%M.%S")
df = df.drop("Date",axis=1)

# %%
col = 'CO(GT)'
min = None
max = None
# delete not available data.
df_new = dropnull(df, col)
# time in 24hrs.
X1 = np.array([i.hour for i in df_new["Time"][min:max]])
# time in one year
X2 = np.array([31*i.month + i.day for i in df_new["Time"][min:max]])
Y = np.array(df_new[col][min:max])