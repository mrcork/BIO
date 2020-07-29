def Fib(a,b,n):
    if n == 1:
        return a
    elif n == 2:
        return b
    for _ in range(n-2):
        a, b = b, (a+b) % 26
    return b
        

alphabet = 'ZABCDEFGHIJKLMNOPQRSTUVWXY' #useful to make z the zeroth index

user = input().upper().split()
n = int(user[2])
a,b = alphabet.find(user[0]), alphabet.find(user[1])

print(alphabet[Fib(a,b,n)])

