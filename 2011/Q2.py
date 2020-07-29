# thought it might be interesting to play around with namedtuples
from collections import namedtuple

Card = namedtuple('Card', ['value', 'suit'])
Max = namedtuple('Max',['index','neighbour','size'])

def get_pack():
    values = ['A',2,3,4,5,6,7,8,9,'T','J','Q','K']
    values = list(map(str,values))
    suits = ['C','H','S','D']
    cards = [Card(v,s) for s in suits for v in values]
    return cards


def deal(deal_numbers):
    '''expects a starting hand and a list of 5 numbers
    iterates through the hand and adds the relevant card to the deal_hand list
    returns the deal_hand when the orginal hand is empty
    '''
    cards = get_pack()
    deal_hand = []
    i = 0
    while cards:
        for deal_number in deal_numbers:
            if cards:
                i = (i +  deal_number - 1) % len(cards)
                deal_hand.append(cards.pop(i))
    return deal_hand


def strategy1(hand_import):
    ''' iterates through the pack from right to left and makes the right most move available
    then repeats until no moves available'''
    hand = hand_import[:]
    while True:
        for i in reversed(range(len(hand))):
            if i>=1 and (hand[i].value == hand[i-1].value or hand[i].suit == hand[i-1].suit):
                hand[i-1] = hand.pop(i)
                break
            elif i >=3 and (hand[i].value == hand[i-3].value or hand[i].suit == hand[i-3].suit):
                hand[i-3] = hand.pop(i)
                break
        else:
            return hand


def strategy2(hand_import):
    ''' like strategy1 but keeps track of the size of piles and the max_pile created from a move
    after checking all possible moves makes the move that will create the largest pile'''
    hand = hand_import[:]
    piles = list(1 for card in hand)
    while True:
        max_pile = Max(index=None, neighbour=None, size=0) 
        for i in reversed(range(len(hand))):
            if i >= 1 and (hand[i].value == hand[i-1].value or hand[i].suit == hand[i-1].suit):
                if piles[i]+piles[i-1] > max_pile.size:
                    max_pile = Max(index=i, neighbour=i-1, size=piles[i]+piles[i-1])
            if i >=3 and (hand[i].value == hand[i-3].value or hand[i].suit == hand[i-3].suit):
                if piles[i]+piles[i-3] > max_pile.size:
                    max_pile = Max(index=i, neighbour=i-3, size=piles[i]+piles[i-3])
        if max_pile.size==0:
            return hand
        hand[max_pile.neighbour] = hand.pop(max_pile.index)
        piles[max_pile.neighbour] = piles[max_pile.neighbour] + piles.pop(max_pile.index)


def get_moves(hand_import):
    ''' checks the number_of_moves available on a given hand'''
    hand = hand_import[:]
    number_of_moves = 0
    for i in reversed(range(len(hand))):
        if i>=1 and (hand[i].value == hand[i-1].value or hand[i].suit == hand[i-1].suit):
            number_of_moves +=1
        if i >=3 and (hand[i].value == hand[i-3].value or hand[i].suit == hand[i-3].suit):
            number_of_moves +=1
    return number_of_moves


def strategy3(hand_import):
    ''' like strategy1 but for each possible move checks the number of moves that will be available in the next round
    after checking all possible moves makes the move that will create the max_moves in next round'''
    hand = hand_import[:]
    while True:
        max_moves = Max(index=None,neighbour=None,size=0) 
        for i in reversed(range(len(hand))):
            if i>=1 and (hand[i].value == hand[i-1].value or hand[i].suit == hand[i-1].suit):
                moves_availble = get_moves(hand[:i-1]+hand[i:i+1]+hand[i+1:])
                if moves_availble>max_moves.size:
                    max_moves = Max(index=i,neighbour=i-1,size=moves_availble)
            if i >=3 and (hand[i].value == hand[i-3].value or hand[i].suit == hand[i-3].suit):
                moves_availble = get_moves(hand[:i-3]+hand[i:i+1]+hand[i-2:i]+hand[i+1:])
                if moves_availble>max_moves.size:
                    max_moves = Max(index=i,neighbour=i-3,size=moves_availble)
        if max_moves.size == 0: # there will be no more moves after this one
              return strategy1(hand)  
        hand[max_moves.neighbour] = hand.pop(max_moves.index)
    

deal_numbers = list(map(int,input().split(' ')))
hand = deal(deal_numbers)
print(hand[0].value + hand[0].suit,hand[-1].value + hand[-1].suit)

strategies = [strategy1,strategy2,strategy3]
for strategy in strategies:
    played_hand = strategy(hand)
    print(len(played_hand), played_hand[0].value + played_hand[0].suit)