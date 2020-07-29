import numpy as np 
# np makes it easy to call elements in the array
from itertools import product
from itertools import permutations as perms

def print_grid(grid):
    for i in range(4):
        for j in range(4):
            print(grid[i,j], end ='')
        print()


def get_score(blocks):
    score = 1
    for block in blocks:
        score *= len(block)
    return score


def get_blocks(grid):
    ''' expects a grid and yields each current_block as a set of tuples i,j'''
    block_nodes = set()
    
    def block_finder(node):
        '''expects a node that is part of the current_block and continues to add 
        nodes to the current_block'''
        i,j = node[0], node[1]
        neighbours = ((i+n,j+m) for n,m in perms([-1,0,1],2) if 0<=i+n<4 and 0<=j+m<4 and abs(n+m)==1)
        for neigh in neighbours:
            if grid[node] == grid[neigh] and neigh not in current_block:
                current_block.add(neigh)
                block_finder(neigh)
    
    for j,i in product(range(4), range(4)):
        current_block = set()
        node = (i,j)
        if node not in block_nodes:
            neighbours = ((i+n,j+m) for n,m in perms([-1,0,1],2) if 0<=i+n<4 and 0<=j+m<4 and abs(n+m)==1)
            if any(grid[node] == grid[neigh] for neigh in neighbours):
                current_block.add(node)
                block_finder(node) # this will find the current_block
                block_nodes = block_nodes | current_block
                yield current_block


def remove_blocks(grid,blocks):
    grid_copy = grid.copy()
    for block in blocks:
        for node in block:
            grid_copy[node] = ''
    return grid_copy


def drop_space(grid):
    ''' iterates from the bottom right corner and drops down 
    letters above'''
    grid_copy = grid.copy()
    for j,i in product(reversed(range(4)),reversed(range(1,4))):
        if not grid_copy[i,j]: # if it's an empty string 
            above,k = grid_copy[i-1,j], i-1
            while not above and k>0:
                # works up the grid until we find a non-empty string 
                # or we have run out of rows
                above, k = grid_copy[k-1,j], k-1
            grid_copy[i,j], grid_copy[k,j]= grid_copy[k,j], grid_copy[i,j]
    return grid_copy


def drop_from(above,grid):
    ''' drops letters from above to the grid 
    returns above and grid after all drops '''
    above_copy = above.copy()
    grid_copy = grid.copy()
    for j,i in product(reversed(range(4)),reversed(range(4))):
        if not grid_copy[i,j]:
            grid_copy[i,j] = above_copy[3,j] # drops down the bottom element in above
            above_copy[3,j] = ''
            above_copy = drop_space(above_copy) # ensures that the bottom element in above is available
    return above_copy, grid_copy


grid = []
for _ in range(4):
    grid.append(list(input()))
grid = np.array(grid)

above = grid.copy()
n = int(input())
score = 0
while n:
    for _ in range(n):
        blocks = list(get_blocks(grid))
        if not blocks:
            print(score)
            print('GAME OVER')
            n = 0
            break
        score += get_score(blocks)
        grid = remove_blocks(grid, blocks)
        grid = drop_space(grid)
        above_dropped, grid = drop_from(above,grid)
        _ , above = drop_from(above, above_dropped)
    else:
        # equivelent to if no break
        print_grid(grid)
        print(score)
        n = int(input())