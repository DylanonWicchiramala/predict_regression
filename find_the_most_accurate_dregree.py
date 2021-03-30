import clean_dat as dat
import regression_lab.polynomial_regression as reg
import numpy as np

# formula E(x) = min(sum(yi - P^deg(xi)^2))
minEx = 999999999
for deg in range(1, 50):
    sum = 0
    for i in range(len(dat.X1)):
        pxi = reg.regrassion_predict(dat.X1[i], dat.X1, dat.Y, degree=deg)
        yi = dat.Y[i]
        sum += (pxi - yi)**2
        
    print(" dregree " + str(deg) + " : " + str(sum))
    if sum < minEx : minEx = sum ; mindrg = deg
    #elif sum > minEx : break
    
print("most accurate dregree is " + str(mindrg))
print(" Ex : " + str(minEx))
