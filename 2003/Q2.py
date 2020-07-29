def get_wave_tips(xpos,ypos,starttime,endtime):
    ''' expects 4 integers
    returns a tuple of coordinates that represent the tips of the wave'''
    return ((xpos,ypos - (endtime - starttime)), (xpos,ypos + (endtime - starttime)))


def generate_wave(startwave, walls):
    ''' start wave is a tuple of wave tips i.e. highest and lowest point of the wave
    moves diagonally along the wave 
    if a wall is reached the x direction changes for that diagonal. 
    To save time later - only yield the point on the wave if useful for the print out. 
    i.e. the i,j values are between 4 and -4
    '''
    if any(all(-4<=i<=4 for i in p) for p in startwave):
        yield from startwave
    wave = [startwave[0], startwave[0], startwave[1], startwave[1]]
    ydir = [1,1,-1,-1]
    xdir = [-1,1,-1,1]
    while wave[0] != wave[2]:
        for i, ripple in enumerate(wave):
            wave[i] = (ripple[0]+xdir[i], ripple[1] + ydir[i])
            if wave[i][0] in walls:
                xdir[i] *= -1
                wave[i] = (ripple[0], ripple[1] + ydir[i])
            if abs(sum(wave[i]))<= 8:
                yield wave[i]


def get_print_out(waves, walls):
    grid = {}
    for j in range(4,-5,-1):
        for i in range(-4,5):
            count = 0
            for p in waves:
                if (i,j) in waves[p]:
                    count += 1 if p>0 else -1
            if count == 0:
                grid[(i,j)] = '-' if i not in walls else 'X'
            elif count < 0:
                grid[(i,j)] = 'o'
            else:
                grid[(i,j)] = '*'
            print(grid[(i,j)],end ='')
        print()
    return grid
 

n = int(input())
pebbles = {}
wave_tips = {}
waves = {}

for i in range(1,n+1):
    pebbles[i] = tuple(map(int,input().split())) #tuple is xpos, ypos, time of drop

walls = tuple(map(int,input().split())) # two walls with different x positions
endtime = int(input()) # time of printout

for i in pebbles:
    wave_tips[i] = get_wave_tips(*pebbles[i],endtime) # this is the positive wave from pebble drop
    if endtime - (pebbles[i][2] + 2) >= 0:
        wave_tips[-i] = get_wave_tips(*pebbles[i],endtime - 2) # this is the negative wave from pebble drop

for p in wave_tips:
    waves[p] = set(generate_wave(wave_tips[p],walls))

grid = get_print_out(waves, walls)


