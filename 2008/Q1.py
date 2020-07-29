n = int(input())
root = int(n**0.5)+1

# generate all non_primes 
# effectively go through the 2 timestable (Starting at 4)
# then the 3 times table (starting at 6)
# then 4 times table  (starting at 8)
# up to the root times table
# not efficient for v.large numbers
non_primes = set(j for i in range(2,root+1) for j in range(i*2,n,i))

primes = set(prime for prime in range(2,n) if prime not in non_primes)

count = (sum(1 for prime in primes if n-prime in primes)+1)//2

print(count)