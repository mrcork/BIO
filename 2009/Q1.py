#regular expressions (regex) would be a good way to solve this...
import re

numbers = ['ONE', 'TWO', 'THREE', 'FOUR',
           'FIVE', 'SIX', 'SEVEN', 'EIGHT', 'NINE']

#create patterns to use regex
patterns = []
for number in numbers:
    word = r'\w*' #some amount of letters
    for letter in number:
        word += letter + r'\w*'
    patterns.append(word)

word = input().upper()

for i,pattern in enumerate(patterns):
    p = re.compile(pattern) #p stands for pattern
    mo = p.search(word) #mo stands for match object
    if mo is not None:
        print(i+1)
        break
else: #this is equivalent to if no break
    print('NO')
