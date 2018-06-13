import datetime,time



logi = open('C:\\Users\\User\\Documents\\PYCHARM\\GIT\\testy\\startup.txt', 'a', encoding='utf8')
now = datetime.datetime.now()
print('Uruchomienie windowsa było o godzinie : ',now, file=logi)
logi.close()
time.sleep(5)
