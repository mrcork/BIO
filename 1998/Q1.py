x = int(input())

def roman(num):
    '''expects an int less than 4000
    returns the roman numeral representation'''
    ints = (1000, 900,  500, 400, 100,  90, 50,  40, 10,  9,   5,  4,   1)
    symbols = ('M',  'CM', 'D', 'CD','C', 'XC','L','XL','X','IX','V','IV','I')
    result = ""
    for i, number in enumerate(ints):
        count = num // number
        result += symbols[i] * count
        num = num % number
    return result


print(roman(x))


