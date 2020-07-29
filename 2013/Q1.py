from datetime import timedelta

def get_time_object(x):
    return timedelta(minutes=int(x))

fast = list(map(get_time_object, input().split()))
clock = [timedelta(0)]*2 # two clocks start at midnight

while True:
    for i in range(2):
        clock[i] += timedelta(hours=1) + fast[i] 
        if clock[i].days > 0:
            clock[i] -= timedelta(days=clock[i].days) # brings days back to zero
    if clock[0]==clock[1]:
        break

time = str(clock[0])
print(time[:-3].zfill(5)) #removes seconds fills in a zero if necessary
