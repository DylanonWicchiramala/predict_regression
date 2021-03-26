import regression_lab.polynomial_regression as reg

import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
import matplotlib.pyplot as plt
import pylab

import pandas as pd
#from clean_dat import df,head,data,drop

#plt.scatter([1,2,3,4] , [1,2,None,4])
reg.regression_plot(np.array([1,2,3,4]) , np.array([1,2,None,4]))
plt.show()