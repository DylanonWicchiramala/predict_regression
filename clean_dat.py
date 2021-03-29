#%%
import numpy as np
import matplotlib.pyplot as plt
import pylab
import datetime
import pandas as pd

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
