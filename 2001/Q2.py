import numpy as np
from string import ascii_uppercase 

def removeDuplicates(word):
        newword = ''
        for letter in word:
            if letter not in newword:
                newword += letter
        return newword


def grid(word, reverse = False):
    ''' expects a word
    returns a numpy matrix with the word as the secret key
    '''
    word = removeDuplicates(word)
    alphabet = ascii_uppercase.replace('Q','')
    for letter in word:
        alphabet = alphabet.replace(letter,'')
    LETTERS = list(word+alphabet)
    if reverse:
        LETTERS = list(reversed(LETTERS))
    return np.array(LETTERS).reshape(5,5)


def index_pair(letter1, letter2):
    ''' returns index of each letter from a and b'''
    return np.append(np.argwhere(a==letter1), np.argwhere(b==letter2)).reshape(2,2)


def new_letters(letter1,letter2):
    ''' assumse that two letters are not in the same row'''
    index = index_pair(letter1, letter2)
    return a[index[1,0],index[0,1]] + b[index[0,0],index[1,1]]
    

def Encode(word):
    if len(word)%2 == 1:
        word += 'X'
    encoded = ''
    for i in range(0,len(word),2):
        index = index_pair(word[i], word[i+1])
        if index[0,0] == index[1,0]:
            encoded += a[index[0,0],(index[0,1]+1)%5] + b[index[1,0],(index[1,1]+1)%5]
        else:
            encoded += new_letters(word[i],word[i+1])
    return encoded


def Decode(word):
    decoded = ''
    for i in range(0,len(word),2):
        index = index_pair(word[i],word[i+1])
        if index[0,0] == index[1,0]:
            decoded += a[index[0,0],(index[0,1]-1)%5] + b[index[1,0],(index[1,1]-1)%5]
        else:
            decoded += new_letters(word[i],word[i+1])
    if decoded[-1] is 'X':
        decoded = decoded[:-1]
    return decoded


def play(mode):
    if mode == 'Q':
        return
    elif mode == 'E':
        print(Encode(input().upper()))
        play(input().upper())
    elif mode =='D':
        print(Decode(input().upper()))
        play(input().upper())


a = grid(input().upper())
b = grid(input().upper(), reverse=True)


for i in range(5):
    for j in range(5):
        print(a[i,j], end = '')
    print(' ', end ='')
    for j in range(5):
        print(b[i,j], end = '')
    print()

play(input().upper())
# TODO