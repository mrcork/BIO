def person_left(seats,rhyme):
    friends = [i for i in range(seats)]
    friends[0] = seats #this means person n is sitting in seat 0
    place = rhyme % len(friends)
    while len(friends)>1:
        friends.pop((place))
        place = place - 1  #accounts for the removal of a friend
        place = (place + rhyme)%len(friends) # moves the place along by the words in rhyme
    return friends[0]


seats = int(input())
rhyme = int(input())
print(person_left(seats,rhyme))