from functools import reduce
from operator import mul 

def prime_factors(n):
    ''' expects a positive integer n
    returns a set of unique prime factors'''
    prime_factors = set()
    while n % 2 == 0:
        # keeps dividing by 2 while 2 is a factor
        prime_factors.add(2)
        n //= 2 # equivalent to n = n // 2
    i = 3
    while n > 1:
        while n % i == 0:
            prime_factors.add(i)
            n //= i
        i += 2
    return prime_factors


n = int(input())
product = reduce(mul, prime_factors(n))

print(product)

# could also use
# product = reduce(lamda x, y: x*y, prime_factors(n))
# or
# from numpy import prod
# product = prod(prime_factors(n))

