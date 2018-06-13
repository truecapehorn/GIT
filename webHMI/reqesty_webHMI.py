import requests, json
import time

USER = 'admin'
PASS = 'admin'
device_adress = 'http://192.168.0.229'
headers = {'X-WH-APIKEY': '72D4E648B82D17655636E19085FB3CFE9554BFCF',
           'Accept': 'application/json',
           'Content-Type': 'application/json',
           'X-WH-CONNS': '1,2',
           'X-WH-START': '1526994016',
           'X-WH-END': '1527052904',
           'X-WH-REG-IDS': '1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16',
           }


def response_status(action, r):
    '''Wydrukowanie wynikow'''
    # Response, status etc
    print('\n' + 140 * '-' + '\n')
    print(
        '* {0} dla URL: {1};\tKodowanie znaków: {2};\t Status: [{3} --> {4}]'.format(action, r.url, r.apparent_encoding,
                                                                                     r.status_code, r.reason))
    print('* Naglowek odpowiedzi: {0}\n'.format(r.headers))
    print('* ODPOWIEDZ SERWERA:\n{0}\n'.format(r.text))  # TEXT/HTML
    print('<!---------koniec-----------!>')


def connectionList():
    '''Zczytanie listy połaczen webHMI'''
    action = 'API - lista połączeń'
    # ADRESS
    api_adress = '/api/connections'
    url = device_adress + api_adress
    # GET
    r = requests.get(url, headers=headers)
    # Response, status etc
    # response_status(action, r)
    return r.json()


def registerList():
    '''Zczytanie listy rejestrow webHMI'''
    action = 'API - lista rejestrow'
    # ADRESS
    api_adress = '/api/registers/'
    url = device_adress + api_adress
    # GET
    r = requests.get(url, headers=headers)
    # Response, status etc
    # response_status(action, r)
    return r.json()


def trendList():
    '''Zczytanie listy trendow webHMI'''
    action = 'API - lista trendow'
    # ADRESS
    api_adress = '/api/trends/'
    url = device_adress + api_adress
    # GET
    r = requests.get(url, headers=headers)
    # Response, status etc
    # response_status(action, r)
    return r.json()


def graphList():
    '''Zczytanie listy grafow webHMI'''
    action = 'API - lista grafow'
    # ADRESS
    api_adress = '/api/graphs/'
    url = device_adress + api_adress
    # GET
    r = requests.get(url, headers=headers)
    # Response, status etc
    # response_status(action, r)
    return r.json()


def getCurValue():
    '''Zczytanie wartosci z rejestru'''
    action = 'API - odczyt wartosci rejstru'
    # ADRESS
    api_adress = '/api/register-values'
    url = device_adress + api_adress
    # GET
    r = requests.get(url, headers=headers)
    # Response, status etc

    # response_status(action, r)
    return r.json()

def getLocTime():
    '''Zczytanie daty'''
    action = 'API - odczyt daty unix time'
    # ADRESS
    api_adress = '/api/timeinfo'
    url = device_adress + api_adress
    # GET
    r = requests.get(url, headers=headers)
    # Response, status etc

    # response_status(action, r)
    return r.json()

def getRegLog():
    '''Zczytanie wartosci logow'''
    action = 'API - odczyt wartosci rejstrw z logow'
    # ADRESS
    api_adress = '/api/register-log'
    url = device_adress + api_adress
    # GET
    r = requests.get(url, headers=headers)
    # Response, status etc

    # response_status(action, r)
    return r.json()



a = 1
dict1 = registerList()
l=[]

while True:
    dict2 = getCurValue()
    print('pomiar ', a)
    #print(getLocTime()['timestamp'])
    timestamp=getLocTime()['timestamp']
    for i in range(len(dict1)):
        ids = dict1[i]['id']
        #print(dict1[i]['title'], dict2[str(ids)]['v'])
        l.append(int(dict2[str(ids)]['v']))

    log = open('log.txt', 'a')
    print(int(timestamp),',',l, file=log)
    log.close()
    l=[]

    time.sleep(0)
    a += 1
    break
#print(getRegLog())

for i in getRegLog():
    if i['r']==2:
        logi = open('logi.txt', 'a')
        print(i['r'], ',', i['t'], ',', i['v'], file=logi)
        logi.close()



