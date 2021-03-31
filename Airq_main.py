# %%
import regression_lab.polynomial_regression as reg
import numpy as np
import matplotlib.pyplot as plt
from clean_dat import data_frame, dropnull

# %%
col = 'CO(GT)'
min = -350
max = None
# delete not available data.
df_new = dropnull(data_frame, col)
# time in 24hrs.
X1 = np.array([i.hour for i in df_new["Time"][min:max]])

Y = np.array(df_new[col][min:max])

#%%
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
plt.show()








# %%
# # time in one year
# X2 = np.array([31*i.month + i.day for i in df_new["Time"][min:max]])

# plt.figure(0)
# plt.title(col)
# plt.xlabel("day of year")
# plt.ylabel("Y")
# # plot data and linear regresstion plot
# reg.regression_plot(X2, Y, degree=1, margin=0, dataplot=True)
# # polynomial regresstion plot
# reg.regression_plot(X2, Y, degree=12, margin=0)
# plt.show()