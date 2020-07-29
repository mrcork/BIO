def decide_letter(pair):
    '''expects a pair of letters and decides which letter will go below the pair'''
    if len(set(pair)) == 1:
        return next(let for let in 'RGB' if let in pair)
    else:
        return next(let for let in 'RGB' if let not in pair)


def Triangle(row):
    '''expects a str of length less than 10
    consisting of uppercase Rs Gs and Bs
    returns the final line of the triangle
    '''
    if len(row) == 1:
        return row
    next_row = ''
    for i in range(len(row)-1):
        next_row += decide_letter(row[i:i+2])
    return Triangle(next_row)


start_row = input().upper()
print(Triangle(start_row))