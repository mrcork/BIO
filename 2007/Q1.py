from itertools import combinations

hand = list(map(int,input().split()))

# checks pairs
points = sum(1 for comb in combinations(hand,2) if comb[0] == comb[1])

# checks combinations that sum to 15
for i in range(2,5):
    points += sum(1 for comb in combinations(hand,i) if sum(comb) == 15) 

print(points)