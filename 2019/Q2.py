from collections import deque
import numpy as np 

path = deque()
rotation = {'L':np.array([[0,-1],[1,0]]), 'R':np.array([[0,1],[-1,0]])}
directions = {'F': [0,1], 'L': [-1,0], 'R': [1,0]}
position = [0,0]

path_length, sequence, moves = input().upper().strip().split(' ')
path_length, moves = int(path_length), int(moves)
sequence = sequence*(moves//len(sequence) + 1)
sequence = sequence[:moves]

for i,move in enumerate(sequence):
    path.append(position)
    if i > path_length - 1:
        path.popleft()

    direction = directions[move]
    new_pos = list(np.array(direction) + np.array(position))
    
    if new_pos in path:
        for _ in range(3):
            move += 'R'
            direction = rotation['R'] @ direction
            new_pos = list(np.array(direction) + np.array(position))
            if new_pos not in path:
                break
        else: #if no break i.e. we haven't found a new pos
            break
    
    position = new_pos
    # now update the directions
    for m in move:
        if m in 'RL':
            for d in directions:
                directions[d] = rotation[m] @ directions[d]

print('('+str(position[0])+',' + str(position[1]) + ')')
