from itertools import product

p,s,n = tuple(map(int,input().split()))
seq = tuple(map(int,input().split()))
grid = {(i,j):0 for i,j in product(range(5),repeat=2)}

def neighbours(pos):
    x,y = pos
    yield (x+1,y)
    yield (x-1,y)
    yield (x,y+1)
    yield (x,y-1)

def num_to_grid(num):
    num = num-1
    return (num%5, num//5)

def add_person(p):
    pos = num_to_grid(p)
    grid[pos] += 1

def remove_crowding():
    # checks whether any crowd is larger than 4
    # changes the first occurence of a crowd >= 4 and repeats
    while any(crowd>=4 for crowd in grid.values()):
        for pos, crowd in grid.items():
            if crowd >= 4:
                grid[pos] -= 4
                for neigh in neighbours(pos):
                    if neigh not in grid:
                        grid[neigh] = 1
                    else:
                        grid[neigh] += 1
                break

# add people and remove crowding
for i in range(n):
    add_person(p)
    remove_crowding()
    p = (p+seq[i%s])%25
    p = 25 if p == 0 else p

# print the final grid
for j in range(5):
    for i in range(5):
        print(grid[i,j], end = ' ')
    print()
    