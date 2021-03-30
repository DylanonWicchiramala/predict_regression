# %%
import regression_lab.polynomial_regression as reg

import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
import matplotlib.pyplot as plt
import pylab

import pandas as pd
from clean_dat import df, dropnull,col,X1,X2,Y
from mpl_toolkits import mplot3d

# %%
plt.figure(1)
plt.title(col)
plt.xlabel("time(24hrs)")
plt.ylabel(col)
plt.xlim(-0.5, 24)
# plot data
plt.scatter(X1, Y, color="black")
# linear regresstion plot
reg.regression_plot(X1, Y, degree=1, margin=0)
# polynomial regresstion plot
reg.regression_plot(X1, Y, degree=12, margin=0)

# %%
plt.figure(0)
plt.title(col)
plt.xlabel("day of year")
plt.ylabel("Y")
# plot data
plt.scatter(X2, Y)
# linear regresstion plot
reg.regression_plot(X2, Y, degree=1, margin=0)
# polynomial regresstion plot
reg.regression_plot(X2, Y, degree=12, margin=0)
plt.show()