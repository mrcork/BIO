def find_valid_moves(serial):
    '''expects a serial as a string
    returns a set of valid moves'''
    serial = '0' + serial + '0'

    valid_moves = set()

    for i in range(1,len(serial)-2):
        a = int(serial[i-1])
        b = int(serial[i])
        c = int(serial[i+1])
        d = int(serial[i+2])
        if b<a<c or b>a>c or b>d>c or b<d<c:
            valid_moves.add(serial[1:i] + serial[i+1] + serial[i]+ serial[i+2:-1])

    return valid_moves


def create_tree(serial):
    ''' this creates a tree made up of:
    nodes - the serials
    and edges which connect the nodes if there is a valid move between them
    '''
    def generate_nodes(serial, tree = {}):
        '''Before generating an element we first check if we have seen it before
        if not we will generate a tuple
        the first element is a node
        the second element is the set of connected nodes
        '''
        moves = find_valid_moves(serial)
        if serial in tree:
            # no new serial found from this branch
            pass
        else:
            yield (serial, moves)
            tree[serial] = moves
            for move in moves:
                yield from generate_nodes(move, tree)
    
    return dict(generate_nodes(serial))


def span_tree_1(serial,tree):
    ''' this traverses the tree we previosly created starting from a given serial
    it ends when all nodes in the tree have been visited
    '''
    
    visited = {serial}
    to_visit = set(node for node in tree if node != serial)
    moves = 0

    while to_visit:
        newly_visited = set()
        for node in visited:
            newly_visited.update(tree[node])
        moves+=1                      
        visited.update(newly_visited)
        to_visit.difference_update(visited)
    return moves      


def span_tree_2(serial):

    ''' traverses the next layer of serial numbers
    as we traverse each leyer we add to the counter '''

    visited = {serial}
    visiting = find_valid_moves(serial)
    counter = 0

    while visiting:
        not_yet_visited = set()
        for node in visiting:
            moves = find_valid_moves(node)
            for move in moves:
                if move not in visited and move not in visiting:
                    not_yet_visited.add(move)
        visited.update(visiting)
        visiting = not_yet_visited
        counter += 1
    return counter


if __name__ == '__main__':
    while True:

        input() # the length of the serial seems irrelevant
        serial = input()
        
        tree = create_tree(serial)
        print((span_tree_1(serial,tree)))
        ## This version firsts creates the tree
        ## which is a collection of nodes and edges

        
        print(span_tree_2(serial))
        ## this version just traverses elements and stops when no new elements are found






        
