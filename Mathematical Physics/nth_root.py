def func(x,n = 4,A = 81): # A and n are the default given parameters
    return x**n - A     #A is the given number and n is the reciprocal power of A 

#applying bisection method on the above function
def bisection(func, a,b, tolerance = 1e-5, max_iterations = 100):

    if func(a) == 0:
        return a
    elif func(b) == 0:
        return b
    
    c = (a+b)/2

    if abs(func(c)) < tolerance or max_iterations == 0:
        return c
    
    elif func(a) * func(c) < 0 :
        return bisection(func,a,c,tolerance, max_iterations-1)
    
    else:
        return bisection(func,c,b,tolerance,max_iterations-1)
    

print(bisection(func,1,4))
    

