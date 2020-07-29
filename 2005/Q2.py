n = int(input())
states = [[]]
for i in range(n):
    states.append(input().split())
simulations = int(input())

tape = {0:0}
index = 0
direction = 0 
new_state = 1

for i in range(simulations):
    current_state = states[new_state]
    if index not in tape:
        tape[index] = 0
    triplet = current_state[0] if tape[index] == 0 else current_state[1]
    direction = +1 if triplet[1] == 'R' else -1
    new_value = int(triplet[0])
    tape[index] = new_value
    new_state = int(triplet[2])
    index += direction
    if new_state == 0:
        break
    

for pos in range(index-3,index+4):
    if pos in tape:
        print(tape[pos],end = '')
    else:
        print(0,end='')
print()
print(i+1)
