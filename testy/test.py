from loctime import loc_time

import datetime
now = datetime.datetime.now()
print (now.year, now.month, now.day, now.hour, now.minute, now.second)


while True:
    now = datetime.datetime.now()
    print(now.minute, now.second)
    if now.minute==59:
        print('dobra godzina')
        break


