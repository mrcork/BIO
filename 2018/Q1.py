from math import ceil


def round_up(num):
    ''' expects a number
    shifts the the number by 8 dp, discards the decimal places
    shifts the number down by 6 place
    takes the ceiling of this number
    divides it by 100 and returns it.
    So 43.000657543332 --> 4300065754.3332 --> 4300065754 --> 43.00065754
    ---> 44
    '''
    num = int(num*10**8)/10**6
    num = ceil(num)/100
    return num


def repay_program(interest, repay):
    '''generator which yields the repayment at each iteration
    starts with debt is 100
    checks if the debt is less than the expected repayment
    then checks if debt is less than 50
    then checks if repayment is less then 50
    otherwise yields the repayment
    '''
    debt = 100
    while debt > 0:
        debt = round_up(debt * interest)
        if debt < debt * repay:
            yield debt
            debt = 0
        elif debt < 50:
            yield debt
            debt = 0
        elif debt * repay < 50:
            yield 50
            debt -= 50
        else:
            yield round_up(debt * repay)
            debt = debt - round_up(debt * repay)




    
while True:
    interest, repay = map(lambda x: int(x)/100, input('').split(' '))
    interest +=1
    print(round_up(sum(repay_program(interest, repay))))
