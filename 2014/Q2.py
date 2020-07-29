from collections import namedtuple


def cycles(G):
    ''' this is an adaptation of the cycles alogirthm from the networkx package
    you can see the original alogirthm at https://github.com/networkx/networkx/blob/master/networkx/algorithms/cycles.py
    '''
    gnodes = set(G.keys())
    cycles = []
    while gnodes:  # loop over connected components
        root = gnodes.pop()
        stack = [root]
        pred = {root: root}
        used = {root: set()}
        while stack:  # walk the spanning tree finding cycles
            z = stack.pop()  # use last-in so cycles easier to find
            zused = used[z]
            for nbr in G[z]:
                if nbr not in used:   # new node
                    pred[nbr] = z
                    stack.append(nbr)
                    used[nbr] = set([z])
                elif nbr == z:          # self loops
                    cycles.append([z])
                elif nbr not in zused:  # found a cycle
                    pn = used[nbr]
                    cycle = [nbr, z]
                    p = pred[z]
                    while p not in pn:
                        cycle.append(p)
                        p = pred[p]
                    cycle.append(p)
                    cycles.append(cycle)
                    used[nbr].add(z)
        gnodes -= set(pred)
    return cycles


def add_edge(path,n1,n2):
    if n1 not in path:
        path[n1] = []
    if n2 not in path:
        path[n2] = []
    path[n1].append(n2)
    path[n2].append(n1)


P = namedtuple('P',['row','col'])

n = int(input())
grid = {}
for i in range(1,2*n,2):
    row = list(map(int,input().split(' ')))
    for k,j in enumerate(range(1,2*n,2)):
        grid[P(i,j)] = row[k]


red_paths = {}
grn_paths = {}

for p in grid:
    if grid[p] == 1:
        add_edge(red_paths, (p.row+1, p.col), (p.row-1, p.col))
        add_edge(grn_paths, (p.row, p.col+1), (p.row, p.col-1))
    elif grid[p] == 2:
        add_edge(grn_paths, (p.row+1, p.col), (p.row-1, p.col))
        add_edge(red_paths, (p.row, p.col+1), (p.row, p.col-1))
    elif grid[p] == 3:
        add_edge(red_paths, (p.row-1, p.col), (p.row, p.col-1))
        add_edge(grn_paths, (p.row+1, p.col), (p.row, p.col+1))
    elif grid[p] == 4:
        add_edge(red_paths, (p.row-1, p.col), (p.row, p.col+1))
        add_edge(grn_paths, (p.row+1, p.col), (p.row, p.col-1))
    elif grid[p] == 5:
        add_edge(grn_paths, (p.row-1, p.col), (p.row, p.col-1))
        add_edge(red_paths, (p.row+1, p.col), (p.row, p.col+1))
    elif grid[p] == 6:
        add_edge(grn_paths, (p.row-1, p.col), (p.row, p.col+1))
        add_edge(red_paths, (p.row+1, p.col), (p.row, p.col-1))


red_cycles = cycles(red_paths)
grn_cycles = cycles(grn_paths)

print(sum(len(cycle) for cycle in red_cycles), end =' ')
print(sum(len(cycle) for cycle in grn_cycles))