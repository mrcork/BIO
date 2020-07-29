import numpy as np

def printBoard(state):
    '''expects an array
    prints the array nicely
    '''
    for i in range(5,-1,-1):
        for j in range(7):
            print(state[i,j],end ='')
        print()


def make_move(j,state,player):
    ''' assumes a move is valid
    expects an int i that represents the column of the move 
    updates the state
    '''
    piece = '*' if player == 0 else 'o'
    state_copy = state.copy()
    i = free_row(j, state)
    state_copy[i,j] = piece
    return state_copy


def check_win(i,j, state, player):
    column = ''.join(state[i,j] for i in range(6))
    row = ''.join(state[i,j] for j in range(7))
    positive_diag = ''.join([state[i+k,j+k] for k in range(-6,7) if i+k>=0 and j+k>=0 and i+k<6 and j+k<7])
    negative_diag = ''.join([state[i+k,j-k] for k in range(-6,7) if i+k>=0 and j-k>=0 and i+k<6 and j-k<7])
    win = '****' if player == 0 else 'oooo'
    return any(win in test for test in (column, row, positive_diag, negative_diag))


def win_column(player,state):
    ''' expects player 1 or player 2 and the current state
    returns the column of the winning move if one is available
    otherwise returns False
    '''
    for j in range(7):
        state_copy = state.copy()
        row = free_row(j, state_copy) 
        if row is not None:
            state_copy = make_move(j,state_copy,player)
            if check_win(row,j, state_copy, player):
                return j


def free_row(j, state):
    ''' expects the current game state 
    returns true if this column is free for a move'''
    for i in range(6):
        if state[i,j] == '-':
            return i


n = int(input()) 
moves = map(lambda x : int(x) - 1, input().split()) 
state = np.array(['-' for i in range(42)]).reshape(6,7)
for i,move in enumerate(moves):
    state = make_move(move, state, i%2)
printBoard(state)

user = input()
while True:
    winning_move = win_column(n%2, state)
    block_move = win_column((n+1)%2,state)
    if winning_move is not None:
        state = make_move(winning_move, state, n%2)
        printBoard(state)
        print('Player',n%2+1,'wins')
        break
    elif block_move is not None:
        state = make_move(block_move, state, n%2)
    else:
        for j in range(7):
            if free_row(j, state) is not None:
                break
        else:
            printBoard(state)
            print('Draw')
            break
        state = make_move(j, state, n%2)
    if user == 'n':
        printBoard(state)
        user = input()
    n += 1

