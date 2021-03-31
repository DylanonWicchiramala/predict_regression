#%%
import regression_lab.polynomial_regression as reg
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
import matplotlib.pyplot as plt
import pandas as pd
from data import X1,X2,Y,data_frame


#%%
##cof
w1 = str((reg.regrassion_predict(24,X1, Y, degree=1) - reg.regrassion_predict(0,X1, Y, degree=1)) / (24-0))
w0 = str(reg.regrassion_predict(0,X1, Y, degree=1))
print('y = ' + w1 + 'x + ' + w0)
# %%
