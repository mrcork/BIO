from itertools import product

ships = [4,3,3,2,2,2,1,1,1,1]
taken = set()
r = 0
a,c,m = tuple(map(int,input().split()))


def Neighbours(point):
    # yields all points around point 
    # also includes point itself
    x,y = point
    for i,j in product((-1,0,1), repeat = 2):
        yield (x+i,y+j)


for ship in ships:
    while True:
        coords = set()
        r = (a*r+c)%m
        x_0,y_0 = x,y = r%10, r//10%10
        r = (a*r+c)%m
        if r %2 ==0:
            i,j = 1, 0
            direction = 'H'
        else:
            i,j = 0, 1
            direction = 'V'
        for _ in range(ship):
            coords.add((x,y))
            if 10<=x or x<0 or 10<=y or y<0:
                break
            elif any(neigh in taken for neigh in Neighbours((x,y))):
                break
            x,y = x+i, y+j
        else:
            taken = taken.union(coords)
            print(x_0,y_0,direction)
            break

