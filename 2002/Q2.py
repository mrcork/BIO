def In(cards):
    ''' expects a list of 8 numbers
    returns a list after an in shuffle
    '''
    new_hand = []
    for i in range(4):
        new_hand.append(cards[i+4])
        new_hand.append(cards[i])
    return new_hand


def Out(cards):
    ''' expects a list of 8 numbers
    returns a list after an in shuffle
    '''
    new_hand = []
    for i in range(4):
        new_hand.append(cards[i])
        new_hand.append(cards[i+4])
    return new_hand


def Break(cards):
    ''' expects a list of 8 numbers
    returns a list after an in shuffle
    '''
    new_hand = cards[1:8] + cards[0:1]
    return new_hand


def matchingBracket(string):
    '''expexts a string starting with a bracket
    returns index of closing bracket
    '''
    count = 0
    for i,ch in enumerate(string):
        if ch is '(':
            count += 1
        elif ch is ')':
            count -= 1
        if count == 0:
            return i

    
def unpack(operations):
    ''' recursive function
    takes a string as input
    base case returns a string of letters without digits
    otherwise finds first instance of a digit, n, and duplicates the bracketed section n times
        or the next operation n times if n is not followed by a bracket
    '''
    if not any(digit in operations for digit in '123456789'):
        return operations
    else:
        for i,op in enumerate(operations):
            if op in '123456789':
                # gets the first instance of a digit
                n = int(op)
                break
        if operations[i+1] is '(':
            close = i+1 + matchingBracket(operations[i+1:]) 
            if close == len(operations)-1:
                return  unpack(operations[0:i] + n*operations[i+2:close])
            else:
                return  unpack(operations[0:i] + n*operations[i+2:close] + operations[close+1:])
        elif i+2 == len(operations):
            return unpack(operations[0:i] + n*operations[i+1:i+2])
        else:
            return unpack(operations[0:i] + n*operations[i+1:i+2] + operations[i+2:])


hand = ['1','2','3','4','5','6','7','8']
operations = unpack(input())
functions = {'b':Break, 'o':Out, 'i':In}

for op in operations:
    hand = functions[op](hand)

print(' '.join(hand))