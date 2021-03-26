import regression_lab.polynomial_regression as reg

import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
import matplotlib.pyplot as plt
import pylab

import pandas as pd
from clean_dat import df,head,data,drop

y = np.array(data[13]).astype(float)
y = drop(y)
y = np.reshape(y,(-1,24))
print(np.shape(y))

plt.ylabel('C O')
#plt.scatter(np.arange(len(y)),y , vmin=0,vmax= 2)
reg.regression_plot(np.arange(len(y)), y, degree = 70)
plt.show()
