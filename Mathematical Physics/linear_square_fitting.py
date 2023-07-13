import numpy as np
import matplotlib.pyplot as plt

def linear_fit(x, y):
    # Calculate the necessary values
    n = len(x)
    sum_x = np.sum(x)
    sum_y = np.sum(y)
    sum_xy = np.sum(x * y)
    sum_xx = np.sum(x * x)

    # Calculate the slope (a) and the intercept (b)
    a = (n * sum_xy - sum_x * sum_y) / (n * sum_xx - sum_x * sum_x)
    b = (sum_y - a * sum_x) / n

    # Plot the fitted line
    x_fit = np.linspace(np.min(x), np.max(x), 100)
    y_fit = a * x_fit + b

    plt.scatter(x, y, label='Data')
    plt.plot(x_fit, y_fit, 'r', label='Fitted Line')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()
    plt.show()

    return a, b

# Example usage
x = np.array([1, 2, 3, 4, 5])
y = np.array([2, 4, 6, 8, 10])

a, b = linear_fit(x, y)