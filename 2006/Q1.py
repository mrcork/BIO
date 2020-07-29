def anagram_check(A,B):
    ''' expects two strings'''
    A = ''.join(sorted(A))
    B = ''.join(sorted(B))
    return 'Anagrams' if A == B else 'Not Anagrams'

word1 = input().upper()
word2 = input().upper()

print(anagram_check(word1, word2))