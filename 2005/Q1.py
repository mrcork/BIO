from fractions import Fraction
from decimal import Decimal

# 
num = int(Decimal(input()) * 10000)
den = 10000
print(Fraction(num, den))


# without fraction module
def gcd(a,b):
    """Calculate the Greatest Common Divisor of a and b.
    e.g. 8 , 12 
    becomes 12, 8
    becomes 8, 4
    becomes 4, 0
    returns 4"""
    while b:
        a, b = b, a%b
    return a

#f = gcd(num,den)
#print(num//f,'/',den//f)

