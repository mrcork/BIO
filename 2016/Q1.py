from fractions import Fraction

def promenade(sequence):
    '''expects a seqence of Ls and Rs
    navigates the sequence updating the previous L, R as necessary
    Ensures that each prev L, R is in simplest form
    Returns a fraction in simplest form
    '''
    prev = {'L':(1,0),'R':(0,1)}
    for d in sequence:
        prev[d] = (prev['L'][0]+prev['R'][0],
                   prev['L'][1]+prev['R'][1])
        f = Fraction(*prev[d]) #unpack prev[d]
        prev[d] = (f.numerator, f.denominator) #ensures simplest form

    return Fraction(prev['L'][0]+prev['R'][0], prev['L'][1]+prev['R'][1])

sequence = input().upper()
f = promenade(sequence)
print(f.numerator, '/', f.denominator) # ensures whole numbers are written as fractions
