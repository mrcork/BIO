from itertools import product

class Die (object):
    def __init__(self,board):
        self.heading = 'top'
        self.orientation = {'up':1,'down':6,'top':2,'bottom':5,'left':3,'right':4}
        self.value = self.orientation['up']
        self.position = (5,5)
        self.board = board
    
    def roll(self):
        '''face_change is a dict that shows where each face will go. 
        The orientation is updated and the value is updated to the value on the top of the die 
        '''
        if self.heading == 'top':
            face_change = dict(zip(['up','down','top','bottom','left','right'],\
                                    ['bottom','top','up','down','left','right']))
            self.position = (self.position[0], (self.position[1]-1) % 11 )
        if self.heading == 'bottom':
            face_change = dict(zip(['up','down','top','bottom','left','right'],\
                                    ['top','bottom','down','up','left','right']))
            self.position = (self.position[0], (self.position[1]+1) % 11)
        if self.heading == 'left':
            face_change = dict(zip(['up','down','top','bottom','left','right'],\
                                    ['right','left','top','bottom','up','down']))
            self.position = ( (self.position[0] - 1 )%11, self.position[1])
        if self.heading == 'right':
            face_change = dict(zip(['up','down','top','bottom','left','right'],\
                                    ['left','right','top','bottom','down','up']))
            self.position = ((self.position[0]+1)%11, self.position[1])
        self.orientation = {face: self.orientation[face_change[face]] for face in face_change}
        self.value = self.orientation['up']
    
    def get_direction(self):
        ''' from the value changes the direction of the heading'''
        if self.board[self.position] == 1 or self.board[self.position] == 6:
            pass
        elif self.board[self.position] == 2:
            clockwise = {'top':'right','right':'bottom','bottom':'left','left':'top'}
            self.heading = clockwise[self.heading]
        elif self.board[self.position] == 5:
            anti_clockwise = {'top':'left','left':'bottom','bottom':'right','right':'top'}
            self.heading = anti_clockwise[self.heading]
        elif self.board[self.position] == 3 or self.board[self.position] == 4:
            opposite = {'top':'bottom','left':'right','bottom':'top','right':'left'}
            self.heading = opposite[self.heading]
    
    def update_board_value(self):
        ''' changes the board value by adding the value on the top of the die 
        and subtracting 6 as necessary'''
        new_val = self.board[self.position] + self.value
        self.board[self.position] = new_val if new_val<=6 else new_val-6

    def __repr__(self):
        grid = ''
        for i in (-1,0,1):
            for j in (-1,0,1):
                if self.board.get((self.position[0]+j,self.position[1]+i)) is not None:
                    grid +=  str(self.board[(self.position[0]+j,self.position[1]+i)]) + ''
                else: 
                    grid += 'X'
            grid = grid.strip() 
            grid += '\n'
        grid = grid[:-1]
        return grid


def generate_board (user_board = None):
    board={(i,j):1 for i,j in product(range(11),range(11))}
    if user_board is not None:
        for coordinate in user_board:
            board[coordinate]=user_board[coordinate]
    return board


def user_input():
    line = []
    board ={}
    for _ in range(3):
        line.append(input().split(' '))
    for i,j in product(range(3),range(3)):
        board[(j+4,i+4)] = int(line[i][j])
    return board


board = generate_board(user_input())
game = Die(board)
n = True
while n:
    n = int(input())
    if n:
        for rolls in range(n):
            game.update_board_value()
            game.get_direction()
            game.roll()
        print(game)

