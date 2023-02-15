def recursive_fact(x):
    if x == 0:
        return 1
    else:
        return x * recursive_fact(x-1)
#or
def fact(x):
    a = 1
    for i in range(x):
        a *= x
        x -= 1
    
    return a

m = int(input("Enter the number of red balls : "))
n = int(input("Enter the number of blue balls : "))

total_permutations = fact(m+n)/(fact(m) * fact(n))
print(int(total_permutations))
