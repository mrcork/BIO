from datetime import date, timedelta    #look up these modules they're great

mayan = list(map(int, input().split()))

calendar = {'baktun': 20*20*18*20, 
            'katun' : 20*18*20,
            'tun'   : 18*20,
            'uinals': 20,
            'day'   : 1
            } # relies on dictionaries being ordered - feature of python 3.6+

start = 2018843 #number of days on 13 20 7 16 3

days = sum(mayan[i]*calendar[period] for i,period in enumerate(calendar))
since_millenium = days - start

new_date = date(2000,1,1) + timedelta(days=since_millenium)

print(new_date.day, new_date.month, new_date.year)
