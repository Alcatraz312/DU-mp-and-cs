import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import linregress
#linear regression is the linear approximation of a casual relationship between 2 variables
def linear_relationship(x):
    return 3*x + 4                #defined the linear expression ŷ = b₀ + b₁x₁

x = np.array([1,2,3,4,5])   #sample data
y = linear_relationship(x)    #dependent variable

#calculating the linear least-squares regression for the two sets of measurements.
slope, intercept, r_value, p_value, error = linregress(x,y)   #this module function returns slope, intercept, r value, p value and standard error of a linear relationship
plt.plot(x,y,"o")
plt.plot(x, slope*x + intercept, "r" )
plt.grid()
plt.show()

