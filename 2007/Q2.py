# this is a graph to represent the moves that can be made
graph = {0: tuple(range(1,9))} # all moves available from the centre (putahi)
for i in range(1,9): # generates all moves available from each kawai 
    before = i-1 if i-1!=0 else 8
    after  = i+1 if i+1!=9 else 1
    graph[i] = (0,before,after)

def get_middle(board,player):
    ''' returns index of the middle piece(s)
    we know there can't be more than 2 middle pieces so it does a left and a right find 
    if no middle pieces found returns an empty tuple'''
    temp_board = ' '+''.join(board[1:])
    if 3*player in temp_board:
        return (temp_board.find(3*player)+1, temp_board.rfind(3*player)+1)
    else:
        return () 

def get_moves(board,player):
    ''' first gets any middle pieces
    then iterates over the pieces that are not 'middle pieces' and sees if there is a move available
    yields tuples of available moves 
    '''
    player = 'O' if player==0 else 'X'
    middle = get_middle(board,player)
    for i,piece in enumerate(board):
        if piece is player and i not in middle:
            for j in graph[i]:
                if board[j] is 'E':
                    yield (i,j)

def make_move(board,move):
    '''board is current board, move is a tuple (i,j)
    swaps board[i] and board[j] and returns it 
    note I created a copy of the board so as not to manipulate the original list object'''
    i,j = move
    temp_board = board[:]
    temp_board[i], temp_board[j] = temp_board[j], temp_board[i]
    return temp_board

def can_win(board,player):
    '''checks if a move is a winning move, i.e. the other player can't move on their next turn'''
    for move in get_moves(board,player):
        temp_board = make_move(board,move)
        if not list(get_moves(temp_board, (player+1)%2)):
            return move  #this will be the left most move

def opponent_can_win(board,player):
    ''' yields moves to be avoided which would lead to opponent being able to win'''
    for move in get_moves(board,player):
        temp_board = make_move(board,move)
        if can_win(temp_board, (player+1)%2) is not None:
            yield move


def play_game(board):
    ''' plays the game and returns the board and winner as a tuple'''
    instruction = input()
    player = 0
    max = 1000
    
    if next(get_moves(board,player), None) is None: # checks if a first move is available
        return board, 2 #player 2 is the winner

    for _ in range(max):
        # checks rule 1
        winning_move = can_win(board,player)
        if winning_move is not None:
            board = make_move(board,winning_move)
            return board, player+1
        # checks rule 2
        avoid = list(opponent_can_win(board,player))
        for move in get_moves(board,player):
            if move not in avoid:
                # this will satisfy both rules 2 and 3
                board = make_move(board,move)
                break
        else:
            # no break means there is no move that will prevent opponenent winning 
            board = make_move(board,avoid[0])

        player = (player+1)%2
        if instruction is 'n':
            print(''.join(board))
            instruction = input()
    # if we've done max iterations then no winner
    return board, None
    

initial_board = list(input().upper())
final_board, winner = play_game(initial_board)

if winner is None:
    print('Draw')
else:
    print(''.join(final_board))
    print('Player {} wins'.format(winner))