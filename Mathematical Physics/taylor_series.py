import math 
import scipy.misc as s
import matplotlib.pyplot as plt
import numpy as np

def func(x):
    return np.sin(x)
number_of_iterations = int(input())
def taylor_swift(x,convergence_point):
    y = 0
    for i in range(number_of_iterations):
        ith_derivative = s.derivative(func,x,n = i,order= 101)
        ith_factorial = math.factorial(i)
        series = (ith_derivative * (x - convergence_point)**i)/ith_factorial
        y += series

    return y

x = np.linspace(1,10)
y = taylor_swift(x,convergence_point= 4)

plt.plot(x,y)
plt.show()





