import numpy as np
import matplotlib.pyplot as plt 
from scipy.optimize import curve_fit

def exponential_fit(x,y):

    def exponent_func(x,a,b):
        return b * np.exp(a*x)
    
    popt , pcov = curve_fit(exponent_func,x,y)
    a = popt[0]
    b = popt[1]

    x_fit = np.linspace(min(x),max(x), num= 100)
    y_fit = exponent_func(x_fit,a,b)

    plt.scatter(x,y)
    plt.plot(x_fit , y_fit)
    plt.show()

    return a , b

x = np.array([1,2,3,4,5])
y = np.array([2,3,8,16,32])

a,b = exponential_fit(x,y)
