convert = { 'pa':'1','re':'2', 
            'ci': '3', 'vo':'4', 
            'mu':'5', 'xa':'6', 
            'ze':'7','bi':'8',
            'so':'9','no':'0'}

lojban = input()
decimal = ''

for i in range(0,len(lojban),2):
    decimal += convert[lojban[i:i+2]]

print(decimal)