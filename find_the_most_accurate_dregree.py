from clean_dat import data_frame, dropnull  
import regression_lab.polynomial_regression as reg
import numpy as np

# find the most accurate dregree by least squre method

# determine P^n(x) is polynomial regression dregree n
# formula -> E(x) = sum(yi - P^deg(xi))^2
# least squre formula -> minEx = min(sum(yi - P^deg(xi))^2 for deg [1-50])

col = 'CO(GT)'
min = -365
max = None
# delete not available data.
df_new = dropnull(data_frame, col)
# time in 24hrs.
X1 = np.array([i.hour for i in df_new["Time"][min:max]])
# time in one year
X2 = np.array([31*i.month + i.day for i in df_new["Time"][min:max]])

Y = np.array(df_new[col][min:max])

minEx = float('inf')
# loop through degree.
for current_degree in range(1, 25):
    sum = 0
    # Iterating over data.
    for i in range(len(X1)):
        #pxi = P^current_degree(X[i])
        pxi = reg.regrassion_predict(
            X1[i], X1, Y, degree=current_degree)
        #(yi - P^deg(xi))^2
        sum += (pxi - Y[i])**2

    print(" dregree " + str(current_degree) + " : " + str(sum))
    if sum < minEx:
        minEx = sum
        mindrg = current_degree

print("most accurate dregree is " + str(mindrg))
print(" Ex : " + str(minEx))
