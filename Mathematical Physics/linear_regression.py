import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import linregress
#linear regression is the linear approximation of a casual relationship between 2 variables
              
x = np.array([1,2,3,4,5])   #sample data
y = np.array([3,4,6,7,8])    #ŷ = b₀ + b₁x₁

#calculating the linear least-squares regression for the two sets of measurements.
slope, intercept, r_value, p_value, error = linregress(x,y)   #this module function returns slope, intercept, r value, p value and standard error of a linear relationship
plt.plot(x,y,"o")
plt.plot(x, slope*x + intercept, "r" )
plt.grid()
plt.show()

