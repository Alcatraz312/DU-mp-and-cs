import numpy as np
from matplotlib import pyplot as plt
import math

angle = int(input("Input an angle in degrees : ")) * math.pi/180
velocity = int(input("Input a velocity (m/sec) : "))
range_ = 2 * ((velocity**2)/2 * (math.sin( 2 * angle))/9.8)
x = np.linspace(start=0, stop=range_ , num= 60)
y = []

for i in x:
    value = (i*math.tan(angle) - (1/2 * 9.8 * (i**2)/((velocity**2) * ((math.cos(angle))**2))))
    y.append(value)

plt.plot(x,y, color = "red")
plt.grid()
plt.xlabel("x")
plt.ylabel("f(x)")
plt.show()

