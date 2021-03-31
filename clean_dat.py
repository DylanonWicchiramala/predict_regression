# %%
import numpy as np
import matplotlib.pyplot as plt
import pylab
import datetime
import pandas as pd

# delete not available data.


def dropnull(df, col=None):
    ind = []
    if col is None:
        for i in range(len(df)):
            if df[i] == -200:
                ind.append(i)
    else:
        for i in range(len(df)):
            if df[col][i] == -200:
                ind.append(i)
    return df.drop(ind)

#import data from csv file
data_frame = pd.read_csv('AirQualityUCI.csv', sep=';',).dropna(axis=1)
data_frame["Time"] = pd.to_datetime(
    data_frame['Date']+data_frame['Time'][:], format="%d/%m/%Y%H.%M.%S")
data_frame = data_frame.drop("Date", axis=1)


