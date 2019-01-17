
n = input()
pal = None
k = int(n) +1

# for easy cases iterate (deals with 99999999999)
for _ in range(1000):
    if str(k) == str(k)[::-1]:
        pal = k
        break
    k += 1

if pal is None:
    if len(n) % 2 == 1:
        first_half = n[:len(n)//2+1]
        pal = first_half[:-1] + first_half[::-1]
    else:
        first_half = n[:len(n)//2]
        pal = first_half + first_half[::-1]

    if int(n) >= int(pal):
        first_half = str(int(first_half)+1)
        if len(n) % 2 == 1:
            pal = first_half[:-1] + first_half[::-1]
        else:
            pal = first_half + first_half[::-1]

print(pal)
