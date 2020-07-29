ISBN = input()
sum = 0
for i,digit in enumerate(ISBN[::-1]):
    if digit == '?':
        place = i + 1
    else:
        if digit == "X":
            digit = 10
        sum += (i+1)*int(digit)

remainder = (11-sum%11)%11

for i in range(10):
    if (i*place)%11 == remainder:
        print(i)
        break
else:
    print('X')
