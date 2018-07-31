"""To jest test dzialania git hub"""

import datetime,time

import sys
filename=sys.argv[0]
logi = open('{}'.format(filename), 'a', encoding='utf8')
now = datetime.datetime.now()
print('Teraz jest godzina : ', now)
print('"""Uruchomienie programu było o godzinie : {}"""\n'.format(now), file=logi)
logi.close()
time.sleep(2)

"""Uruchomienie programu było o godzinie : 2018-07-31 08:59:41.811608"""

"""Uruchomienie programu było o godzinie : 2018-07-31 08:59:47.255920"""

"""Uruchomienie programu było o godzinie : 2018-07-31 08:59:59.681630"""

