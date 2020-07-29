# defined in the global scope
odds = [0] + list(range(1,10004,2))


def lucky_removal(i):
  '''this function removes every ith element from odds'''
  every = i # moving along 'every' after each removal
  while i < len(odds):
    del(odds[i])
    i += every - 1 # subtract 1 to account for the removal of the ith element


def lucky_gen():
  '''this generator yields all the lucky numbers'''
  yield 1
  i = 2
  while i < len(odds):
    yield odds[i] # yields the next odd number still in odds
    lucky_removal(odds[i]) # this removes every '3rd' odd from odds
    i += 1


def get_values(number,lucky_numbers):
  ''' expects an int <10000 and the lucky numbers
  returns a tuple of the lucky numbers above and below the number
  '''
  for i, lucky in enumerate(lucky_numbers):
    if lucky >= number:
      # moves to the correct place in the lucky number list
      break
  if lucky == number:
    # accounts for our number being in the lucky number list
    return lucky_numbers[i-1], lucky_numbers[i+1]
  else:
    return lucky_numbers[i-1], lucky_numbers[i]


number = int(input(''))
# turn the lucky_gen into a tuple object
lucky_numbers = tuple(lucky_gen())

before, after = get_values(number,lucky_numbers)

print(before,after) 

