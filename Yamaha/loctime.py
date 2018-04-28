import time,datetime


def loc_time():
    localtime = time.strftime("%d.%m.%Y %H:%M:%S")
    znacznik = time.strftime("%d%m%Y_%H_%M")
    data = time.strftime("%d-%m-%Y")
    godzina = time.strftime("%H:%M:%S")
    return localtime, data, godzina, znacznik


def date_time():
    t = datetime.datetime.now()
    #print(t)
    #print('hour  :', t.hour)
    #print('minute:', t.minute)
    #print('second:', t.second)
    #print('microsecond:', t.microsecond)
    #print('tzinfo:', t.tzinfo)
    return t, t.hour,t.minute,t.second

#print(date_time()[0])


'''
>>> import datetime
>>> now = datetime.datetime.now()
>>> datetime.time(now.hour, now.minute, now.second)
datetime.time(11, 23, 44)
'''
