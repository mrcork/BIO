def factors(n):
    ''' expects an int n > 1
    generates all factors less than n'''
    for i in range(1,n):
        if n % i == 0:
            yield i


num1 = int(input())
num2 = int(input())

is_amicable = sum(factors(num1)) == num2 and \
              sum(factors(num2)) == num1 and \
              num2 != num1

print('Amicable' if is_amicable else 'Not amicable')