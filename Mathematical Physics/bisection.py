def func(x : float):
    return x**3 - x - 1

def bisection(func, a, b, tolerance = 1e-5, max_iterations = 100):
    if func(a) == 0:
        return a
    elif func(b) == 0:
        return b

    c = (a+b)/2

    if abs(func(c)) < tolerance or max_iterations == 0:
        return c
    elif func(c) * func(a) < 0:
        return bisection(func, a,c, tolerance,max_iterations-1)
    else:
        return bisection(func, c,b, tolerance, max_iterations-1) 
        
print(bisection(func, 1,2))