from string import ascii_uppercase as letters

# note letters is now just ABCDEFGHIJKLMNOPQRSTUVWYZ


def encrypt(second_dial, word_to_encrypt):
    ''' expects two strings, a second_dial and a word_to_encrypt
    with each iteration through the letters of the word_to_encrypt
    adds a letter to the encrypted_word and adjusts the dial position 1 place'''
    
    encrypted_word = ''
    for letter in word_to_encrypt:
        encrypt_dict = {letters[i]:second_dial[i] for i in range(26)} # dict comprehension 
        encrypted_word += encrypt_dict[letter]
        second_dial = second_dial[1:] + second_dial[0]

    return encrypted_word


def create_second_dial(n):
    ''' expects an integer n
    iterates through a list of letters A to Z
    moves n places and adds this letter to the dial
    adjusts the position depending on the number of letters left'''

    index = 0
    letters_to_add = list(letters)
    second_dial = ''
    for letter in letters:
        index = (index + n  - 1) % len(letters_to_add)
        second_dial += letters_to_add.pop(index)
    return second_dial


while True:
    n, word = input().split(' ')
    n = int(n)
    second_dial = create_second_dial(n)
    print(second_dial[:6])
    print(encrypt(second_dial, word))
    


    







    

