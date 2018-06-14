<<<<<<< HEAD
import requests

device_adress = 'http://192.168.0.229'
#wifi_name = "BigBang"
#wifi_pwd = "501195121"


def response_status(action, r):
    '''Wydrukowanie wynikow'''
    # Response, status etc
    print('\n' + 140 * '-' + '\n')
    print('* {0} dla URL: {1}\n  Kodowanie znaków: {2}\n'.format(action, r.url,r.apparent_encoding))
    print('* ODPOWIEDZ SERWERA:\n{0}'.format(r.text))  # TEXT/HTML
    print('* KOD STATUSU I STATUS:\n[{0} --> {1}]\n'.format(r.status_code, r.reason))  # HTTP
    print('* NAGLOWEK ODPOWIEDZI:\n{0}\n'.format(r.headers))
    print('<!---------koniec-----------!>')






def devive_uptime():
    '''
        Popbranie danych połaczenia
    '''
    #action = 'Device - Get device uptime'
    # ADRESS
    api_adress = '/api / connections'
    url = device_adress + api_adress
    # GET
    r = requests.get(url)
    # Response, status etc
   #response_status(action, r)

device_adress()


=======
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





def connectionList():
    '''Zczytanie listy połaczen webHMI'''
    # ADRESS
    api_adress = '/api/connections'
    url = device_adress + api_adress
    # GET
    r = requests.get(url, headers=headers)
    return r.json()


def registerList():
    '''Zczytanie listy rejestrow webHMI'''
    # ADRESS
    api_adress = '/api/registers/'
    url = device_adress + api_adress
    # GET
    r = requests.get(url, headers=headers)

    return r.json()


def trendList():
    '''Zczytanie listy trendow webHMI'''

    # ADRESS
    api_adress = '/api/trends/'
    url = device_adress + api_adress
    # GET
    r = requests.get(url, headers=headers)

    return r.json()


def graphList():
    '''Zczytanie listy grafow webHMI'''

    # ADRESS
    api_adress = '/api/graphs/'
    url = device_adress + api_adress
    # GET
    r = requests.get(url, headers=headers)

    return r.json()


def getCurValue():
    '''Zczytanie wartosci z rejestru'''

    # ADRESS
    api_adress = '/api/register-values'
    url = device_adress + api_adress
    # GET
    r = requests.get(url, headers=headers)

    return r.json()


def getLocTime():
    '''Zczytanie daty'''

    # ADRESS
    api_adress = '/api/timeinfo'
    url = device_adress + api_adress
    # GET
    r = requests.get(url, headers=headers)

    return r.json()


def getRegLog():
    '''Zczytanie wartosci logow'''

    # ADRESS
    api_adress = '/api/register-log'
    url = device_adress + api_adress
    # GET
    r = requests.get(url, headers=headers)

    return r.json()



>>>>>>> e0defeb6a04f3199d27ffb2502d5b737dbcd273f
