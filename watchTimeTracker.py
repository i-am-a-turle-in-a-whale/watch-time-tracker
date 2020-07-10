

from datetime import datetime
from collections import defaultdict
now = datetime.now()

date_time = now.strftime("%m/%d/%Y")

record = defaultdict(list)

total_time_steve = 0
total_time_michael = 0
def AddWatch(person,minutes,reason):
    if person == 'michael':
#        total_time_michael = total_time_michael + minutes
        record[date_time] = ((minutes,reason))
    elif person == 'steve':
        total_time_steve = total_time_steve + minutes
        record[date_time] = ((total_time_steve,reason))
    else:
        pass
def MinusWatch(person,minutes,reason,time):
    global total_time_steve
    global total_time_michael
    global michael
    global steve
    if person == 'michael':
        total_time_michael = total_time_michael - minutes
        michael.append((total_time_michael, reason,time))
    elif person == 'steve':
        total_time_steve = total_time_steve - minutes
        steve.append((total_time_steve,reason,time))
    else:
        pass
def WatchTimeTracker(person):
    if person == 'michael':
        print( "total time earned for %s right now is %d" %(person ,total_time_michael ))
    else:
        print( "total time earned for %s right now is %d" %(person ,total_time_steve ))


def SaveToFile(person,x):
    file = open(person+'_watch.txt', 'a')
    for k, v in x.items():
        txt = str(k) +',' + str(v)[1:-1]
    file.write(txt)
    file.write('\n')
    file.close()
def readFile(person):
    file = open(person+'_watch.txt', 'r')
    _sum =0
    for line in file.readlines():
        x_list = line.split(',')
        _sum += int(x_list[1])
        _date = x_list[0]
    file.close()
    return (_date,_sum)




AddWatch('michael',60,'+default Hour')
SaveToFile('michael',record)
AddWatch('michael',60,'+default Hour')
SaveToFile('michael',record)
AddWatch('michael',10,'+running')
SaveToFile('michael',record)
WatchTimeTracker('michael')
print(readFile('michael'))
'''AddWatch('michael',10,'+coding',date_time)
AddWatch('michael',45,'+vacuuming',date_time)
MinusWatch('michael',20,'-watch',date_time)'''


#SaveToFile('michael',record)