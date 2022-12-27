n = int(input())
a = []
#check of n is prime or not
def prime_check(x):
    is_prime = True
    for i in range(2,x):
        if x%i == 0:
            is_prime = False
        
    if is_prime == False:
        return "Not a prime"
    else:
        return "Prime"

print(prime_check(n))


# primes till the number n
for i in range(2,n):
    if prime_check(i) == "Prime":
        a.append(i)

print(f"Prime numbers till number {n} are :",a)

#first n prime numbers
list_of_n_prime = []
counter = 2
while len(list_of_n_prime) <= n:
    if prime_check(counter) == "Prime":
        list_of_n_prime.append(counter)
    counter+=1

print(list_of_n_prime)







        
    





    





