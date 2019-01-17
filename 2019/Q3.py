from string import ascii_uppercase as alphabet
from math import factorial as f

def nCr(n,r):
    return f(n)//f(r)//f(n-r)


def get_suffix_combs(blocks_to_arrange, must_be_descending):
    ''' uses stars and bars to calculate the combinations
    for each block in blocks to check, whilst it is descending we can arrange the letters amongst
    the letters of must_be_descending
    e.g. to_check_block might be BAC and must_be_descending might be IHGF
    for this block there are 6C2 valid arrangements as BAC is descending for 2 letters
    blocks_to_arrange is a dictionary of all the blocks with initial des_seq_len as Keys 
    and number of blocks as values'''
    k = len(must_be_descending)
    for des_seq_len, num_blocks in blocks_to_arrange.items():
        yield num_blocks*nCr(des_seq_len + k , des_seq_len)


def check_valid_prefix(prefix,check_against):
    ''' first checks if the prefix is a valid block 
    if it is a valid block checks that the sequence of letters which are less than
    the highest value in the suffix are decreasing'''
    if not(check_valid_block(prefix)):
        return False
    should_be_descending = ''.join(letter for letter in prefix if letter<check_against)
    return should_be_descending == ''.join(reversed(sorted(should_be_descending)))


def check_valid_block(block):
    '''first finds the first increasing sequence of length 2 
    if we find a smaller increasing sequence we update the sequence
    if we find an increasing sequence of length 3 return FALSE'''
    inc_seq = [block[0]] #increasing sequence
    min_val = block[0]
    for letter in block:
        if len(inc_seq) == 1 and letter < inc_seq[0]:
            inc_seq[0] = min_val = letter
        elif len(inc_seq) == 1 and letter > inc_seq[0]:
            inc_seq.append(letter)
        elif len(inc_seq) == 2 and letter > inc_seq[1]:
            return False
        elif len(inc_seq) == 2 and inc_seq[0] < letter < inc_seq[1]:
            inc_seq[1] = letter
        elif letter < min_val:
            min_val = letter
        elif letter > min_val:
            inc_seq = [min_val,letter]
    return True


def initial_descending_sequences(n,final=True):
    ''' n is the length of the blocks to get 
    eg DCBA would have an initial descending sequence of length 2
    if final is false will return a list of the totals of the initial descending sequences 
    with the highest length in the 0th place
    when final is True returns a dictionary 
    the Keys are the length of the initial descending seqeuence
    the values are the total number of blocks'''
    if n == 1:
        return [1] if not final else {1:1}
    else:
        descending = []
        total = 0
        for k in initial_descending_sequences(n-1,final=False):
            total += k
            descending.append(total)
        descending.append(total)
        if not final:
            return descending
        else:
            return {des_seq_len:num_blocks for des_seq_len,num_blocks in zip(range(1,n+1),reversed(descending))}


l,prefix = input().upper().split(' ')
l = int(l)
letters = ''.join(letter for letter in alphabet[:l] if letter not in prefix)
prefix_min = min(prefix)

must_be_descending = ''.join(letter for letter in letters if letter > prefix_min)
to_check = ''.join(letter for letter in letters if letter < prefix_min)
check_against = max(must_be_descending) if must_be_descending else ''


if len(prefix) == l:
    # the prefix is the entire block so is it valid?
    if check_valid_block(prefix):
        print(1)
    else:
        print(0)
elif not(check_valid_prefix(prefix,check_against)):
    # is the prefix valid?
    print(0)
elif not to_check:
    # then we only have 1 arrangement in the suffix since all letters must be descending
    print(1)
elif not must_be_descending:
    # then we do not have to consider arranging the to_check blocks amongst the must_be_descending letters
    # so we only need to sum the initial descending sequences from the blocks of to_check 
    print(sum(initial_descending_sequences(len(to_check)).values()))
else:
    # must arrange the blocks from to_check amongst the must_be_descending letters
    # get the blocks from to_check using initial_descending_sequences
    # sum the arrangements of these blocks amongst the must_be_descending letters
    blocks_as_des_seqs = initial_descending_sequences(len(to_check))
    print(sum(get_suffix_combs(blocks_as_des_seqs, must_be_descending)))
