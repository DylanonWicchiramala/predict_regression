# %%
import regression_lab.polynomial_regression as reg
import numpy as np
import matplotlib.pyplot as plt
from data import col,X1,Y
from regression_lab.most_accurate_dregree import most_acc_deg

#%%
##plot
plt.figure(1)
plt.title(col + '1 year')
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

#%%
##predict
inp = input("time : ")
time = str(inp)
time = float(time.split('.')[0]) + float(time.split('.')[1])/60
print(str(col) + ' at ' + str(time)+ ' o\'clock is '+ str(reg.regrassion_predict(time,X1, Y, degree=12)))

#%%
##cof
w1 = str((reg.regrassion_predict(24,X1, Y, degree=1) - reg.regrassion_predict(0,X1, Y, degree=1)) / (24-0))
w0 = str(reg.regrassion_predict(0,X1, Y, degree=1))
print('y = ' + w1 + 'x + ' + w0)













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