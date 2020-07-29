def number_of_block_pals(string):
    '''expects a string 
    base case yields 0 if we only have a single letter string or an empty string
    '''
    if len(string) == 1 or len(string) == 0:
        yield 0
    else:
        for i in range(len(string)//2+1):
            if string[:i] == string[-i:]:
                #print(string[:i],string[i:-i],string[-i:])
                yield 1
                yield from number_of_block_pals(string[i:-i])


word = input().upper()
print(sum(number_of_block_pals(word)))
