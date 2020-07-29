from collections import namedtuple

Point = namedtuple('Point',['straight','left','right'])

Network = {'A':Point('D','E','F'), 'B':Point('C','G','H'), 'C':Point('B','I','J'),
           'D':Point('A','K','L'), 'E':Point('A','M','N'), 'F':Point('A','N','O'),
           'G':Point('B','O','P'), 'H':Point('B','P','Q'), 'I':Point('C','Q','R'),
           'J':Point('C','R','S'), 'K':Point('D','S','T'), 'L':Point('D','T','M'),
           'M':Point('U','L','E'), 'N':Point('U','E','F'), 'O':Point('V','F','G'),
           'P':Point('V','G','H'), 'Q':Point('W','H','I'), 'R':Point('W','I','J'),
           'S':Point('X','J','K'), 'T':Point('X','K','L'),
           'U':Point('V','M','N'), 'V':Point('U','O','P'),
           'W':Point('X','Q','R'), 'X':Point('W','S','T')
           }

states = {node:'left' for node in Network}

flipflops = list(input())
start, stop = list(input())
number_of_moves = int(input())

def get_next_node(before,after):
    if Network[after].straight == before: # if we've come from a straight direction
        direction = states[after] # we will leave depending on the state of the current node
        if after in flipflops: # if we're a flip flop node then we must change the state 
            states[after] = next(d for d in ('left','right') if d != states[after])
        return Network[after].__getattribute__(direction)
    elif Network[after].left == before:  # if we've come from a left direction
        if after not in flipflops: # set the state if it's a lazy node 
            states[after] = 'left'
        return Network[after].straight
    elif Network[after].right == before: # if we've come from a right direction
        if after not in flipflops: # set the state if it's a lazy node 
            states[after] = 'right' 
        return Network[after].straight


for _ in range(number_of_moves):
    start, stop = stop, get_next_node(start,stop)

print(start + stop)
