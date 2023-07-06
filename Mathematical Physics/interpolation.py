import numpy as np 
import matplotlib.pyplot as plt 
import math

x=[1,3,5,7]
y=[24,120,336,720]

def make_list(y : list, iterations = len(y) - 2, c = []):
    a_list = []
    
    n = len(y) - 1
    for i in range(n):
        new = y[i+1] - y[i]
        a_list.append(new)

    c.append(a_list)
    

    if iterations > 0:
        make_list(a_list, iterations=iterations -1,  c = c )
    
    return c

   
new_data_set = make_list(y)

def interpolation(data_set : list , y : list , x : list, z):
    difference = x[1] - x[0]
    a = x[0]
    u = (z - a)/difference

    answer = y[0]
    v = 1
    for i in range(len(data_set)):
        v = v*(u - i)

        
        answer = answer + (v*data_set[i][0])/math.factorial(i+1)
        
    
    return answer

print(interpolation(new_data_set, y = y , x = x , z = 1.5))




    
    

