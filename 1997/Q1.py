numbers = list(range(20)) + [20,30]

words = ['o\'clock','one','two','three','four','five','six',
         'seven','eight','nine','ten','eleven','twelve','thirteen',
         'fourteen','quarter','sixteen','seventeen','eighteen',
         'nineteen','twenty','half']

num_to_word = {numbers[i]:words[i] for i in range(len(numbers))} 

def get_time_string(hour,mins):
    past_or_to = 'past' if mins <= 30 else 'to'
    hour = hour + int(past_or_to is 'to')
    hour = hour if hour <= 12 else hour % 12 # if we do quarter to 1
    mins = mins if mins <= 30 else 60 - mins
    if mins == 0:
        return num_to_word[hour] + ' ' + num_to_word[mins]
    elif 20 < mins < 30:
        return 'twenty-' + num_to_word[mins%20] + ' minutes ' + past_or_to + ' ' + num_to_word[hour]
    elif mins == 15 or mins == 30:
        return num_to_word[mins] + ' ' + past_or_to + ' ' + num_to_word[hour]
    elif mins == 1:
        return num_to_word[mins] + ' minute ' + past_or_to + ' ' + num_to_word[hour]
    else:
        return num_to_word[mins] + ' minutes ' + past_or_to + ' ' + num_to_word[hour]


hour = int(input())
mins = int(input())
print(get_time_string(hour,mins).capitalize())
