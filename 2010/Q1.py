def is_anagram(A,B):
  '''expects two numbers
  returns True if anagram else false '''
  A = ''.join(sorted(str(A)))
  B = ''.join(sorted(str(B)))
  return A == B


def anagram_digits(A):
  '''expects a positive int less than 123456789
  returns a list of digits that generate anagrams
  if no anagrams returns 'NO'
  '''
  digits = ''
  for i in range(2,9):
    if is_anagram(A,A*i):
      digits += str(i) + ' '
  return 'NO' if not digits else digits.strip()


A = int(input())
print(anagram_digits(A)) 
