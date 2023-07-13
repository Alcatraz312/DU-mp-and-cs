import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

def power_law_fit(x, y):
    # Define the power law function
    def power_law(x, A, b):
        return b * x ** A

    # Perform the curve fitting
    popt, pcov = curve_fit(power_law, x, y)

    # Retrieve the estimated parameters
    A = popt[0]
    b = popt[1]

    # Plot the fitted curve
    x_fit = np.linspace(np.min(x), np.max(x), 100)
    y_fit = power_law(x_fit, A, b)

    plt.scatter(x, y, label='Data')
    plt.plot(x_fit, y_fit, 'r', label='Fitted Curve')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()
    plt.show()

    return A, b

# Example usage
x = np.array([1, 2, 3, 4, 5])
y = np.array([2, 4, 8, 16, 32])

A, b = power_law_fit(x, y)