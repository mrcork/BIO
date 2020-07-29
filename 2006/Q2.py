def validity_test(password,expressions):
    ''' 
    expects a password and a generator of expressions with the same length as password
    runs through all possible expressions and compares to password
    if a successful expression matches password then it will return 'Yes'
    if no expression is successful it will return 'No'
    '''
    for exp in expressions:
        for i,let in enumerate(exp):
            if let is 'x':
                pass
            elif let is 'u' and password[i]<=password[i-1]:
                    break
            elif let is 'd' and password[i]>=password[i-1]:
                    break
        else:
            # i.e. if no break
            return 'Yes'
    return 'No'


def add_brackets(regex):
    '''adds brackets in the case when a single letter is followed by a * or ?
    at this stage regex should be a string
    '''
    for _ in range(2): # since we know there are at most two instances
        for i,letter in enumerate(regex):
            if letter in "*?" and regex[i-1] != ')':
                regex = regex[:i-1] +'(' + regex[i-1] + ')'+regex[i:]
                break
    return regex


def swap_special_symbols(regex):
    '''regex is now a list. it is useful to swap the * and ? so they preceed
    the expression that they are associated with
    '''
    for i,element in enumerate(regex):
        if element in '*?':
            regex[i-1], regex[i] = regex[i], regex[i-1] 
    return regex


def get_all_expressions(regex):
    ''' gets all_expressions with lengths not much larger than 12 character
    removes the * and ? from the regex
    '''
    all_expressions = ['']
    i=0
    while i< len(regex) :
        if regex[i] not in '*?':
            for j in range(len(all_expressions)):
                all_expressions[j] += regex[i]
        else:
            i += 1
            for j in range(len(all_expressions)):
                all_expressions.append(all_expressions[j]+regex[i])
                if regex[i-1] is '*':
                    for k in range(2,12//len(regex[i])):
                         all_expressions.append(all_expressions[j]+regex[i]*k)
        i+=1
    return all_expressions


regex = input()
testcase1 = input()
testcase2 = input()

regex = add_brackets(regex)
regex = regex.replace('(',' ').replace(')',' ').replace('?','? ').replace('*','* ')
regex = regex.split()
regex = swap_special_symbols(regex)

all_expressions = get_all_expressions(regex)


test1expressions = (exp for exp in all_expressions if len(exp) == len(testcase1))
test2expressions = (exp for exp in all_expressions if len(exp) == len(testcase2))

print(validity_test(testcase1,test1expressions))
print(validity_test(testcase2,test2expressions))