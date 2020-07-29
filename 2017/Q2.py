from collections import Counter

def generate_graph():
    return {i: {j for j in (i+1, i-1, i+6, i-6) 
                    if not((i%6==0 and j==i+1) or (i%6==1 and j==i-1)) and 0<j<37}
            for i in range(1,37)
            }


def generate_edges(graph):
    '''expects a graph dict
    returns sets of all undirected edges
    each edge is a frozen set which means we don't worry aboud double counting'''
    return {frozenset({node,neigh}) 
                for node,neighbours in graph.items() 
                    for neigh in neighbours
                }


def boxes_repr(boxes):
    display =''
    for j in range(5):
        for i in range(1, 6):
            display+= boxes[6*j+i]+ ' '
        display = display[:-1] +'\n'
    display = display[:-1]
    return display


def move(node, clockwise=True):
    ''' expects a starting node and finds the first free edge according to the strategy
    returns the node (we may have had to look for the next node if all edges taken)
    and returns the edge that was drawn'''
    if clockwise:
        options = (frozenset({node, node+i}) for i in (-6, 1, 6, -1))
    else:
        options = (frozenset({node, node+i}) for i in (-6, -1, 6, 1))
    for edge in options:
        if edge in free_edges:
            free_edges.remove(edge)
            taken_edges.add(edge)
            break
    else: # if no break
        node = node+1 if node!=36 else 1
        return move(node, clockwise)
    return node, edge


def any_boxes(edge, taken='X'):
    if max(edge)-min(edge) == 1: # if we've drawn a horizontal line
        # check box above and below horizontal line
        above = start_node_has_box(min(edge), taken)
        below = start_node_has_box(min(edge)-6, taken)  
        return above or below
    else:
        # check box left and right of horizontal line
        left = start_node_has_box(min(edge)-1,taken)
        right = start_node_has_box(min(edge), taken)
        return left or right


def start_node_has_box(node, taken='X'):
    '''checks to see if there is a box to the right and below node
    puts a taken value in the boxes dict
    return True if a box was found
    '''
    if all(edge in taken_edges for edge in
           [{node, node+1}, {node, node+6},
            {node+1, node+7}, {node+6, node+7}]):
        boxes[node] = taken
        return True
    else:
        return False


def play_game(position1, modifier1, position2, modifier2, max_moves):
    turn = 1
    player = 1
    taken = ('O', 'X')
    position = [position2, position1]
    modifier = (modifier2, modifier1)
    for _ in range(max_moves):
        i = player
        new_pos = (position[i] + modifier[i]) % 36
        position[i] = new_pos if new_pos!=0 else 36
        position[i], edge = move(position[i], clockwise=i)
        if not any_boxes(edge, taken=taken[i]):
            player = (player + 1) % 2


graph = generate_graph()
free_edges = generate_edges(graph)
taken_edges = set()
boxes = {i:'*' for i in range(1,37)}

p1,m1,p2,m2,t = tuple(map(int, input().split(' ')))
play_game(p1,m1,p2,m2,t)

print(boxes_repr(boxes))
print(Counter(boxes.values())['X'], Counter(boxes.values())['O'])