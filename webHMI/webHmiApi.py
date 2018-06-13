import requests
import os, platform


class Api():
    '''Klasa dodajaca urzadzenie webHMI'''

    def __init__(self, device_address, apikey):
        self.device_address = device_address
        self.apikey = apikey

    def make_headers(self, update):
        '''Dodanie nagłowka do requesta'''
        # wspólny nagłówke dla wszystkich
        base_headers = {'X-WH-APIKEY': self.apikey,
                        'Accept': 'application/json',
                        'Content-Type': 'application/json',
                        "Accept - Encoding": "gzip, deflate, sdch",
                        }
        base_headers.update(update)  # dodanie reszty potrzebnych naglowkow
        return base_headers

    def reqGet(self, address):
        '''Request o potrzebne dane'''
        header = self.make_headers(address[1])  # dodanie potrzebnych naglowków
        api_address = address[0]
        url = self.device_address + api_address
        try:
            r = requests.get(url, headers=header, timeout=3)
            return r.json()
        except requests.exceptions.ConnectTimeout:
            print(" Wystapil timeout")
            r = self.displayTest(address)
            return r

    def reqPut(self, address):
        '''Request o zmiane wartosci'''
        header = self.make_headers(address[1])  # dodanie potrzebnych naglowków
        api_address = address[0]
        url = self.device_address + api_address
        try:
            r = requests.put(url, headers=header, data={'value': address[2]}, timeout=3)
            return r.json()
        except requests.exceptions.ConnectTimeout:
            print(" Wystapil timeout")
            r = self.displayTest(address)
            return r

    def displayTest(self, address):
        '''Test zapytania'''
        header = self.make_headers(address[1])
        api_address = address[0]
        return self.device_address + api_address, header

    def pingTest(self):
        '''
        (foo &>/dev/null &), linux
        start /B foo > NUL 2>&1 wind
        '''
        if platform.system().lower() == 'windows':
            resp = os.system('start /B ' + 'ping' + ' -n 1 ' + self.device_address + 'NUL 2>&1')
        else:
            resp = os.system("ping" + " -c 1 " + self.device_address + " >/dev/null 2>&1")
        return resp

    def connectionList(self):
        '''Zczytanie listy połaczen webHMI'''
        api_address = '/api/connections'
        header = {}
        address = (api_address, header)
        r = self.reqGet(address)
        return r

    def registerList(self):
        '''Zczytanie listy rejestrow webHMI'''
        api_address = '/api/registers'
        header = {}
        address = (api_address, header)
        r = self.reqGet(address)
        return r

    def trendList(self):
        '''Zczytanie listy trendow webHMI'''
        api_address = '/api/trends'
        header = {}
        address = (api_address, header)
        r = self.reqGet(address)
        return r

    def graphList(self):
        '''Zczytanie listy grafow webHMI'''
        api_address = '/api/graphs'
        header = {}
        address = (api_address, header)
        r = self.reqGet(address)
        return r

    def getCurValue(self, conns):
        '''Zczytanie wartosci z rejestru'''
        api_address = '/api/register-values'
        header = {'X-WH-CONNS': conns}
        address = (api_address, header)
        r = self.reqGet(address)
        return r

    def getLocTime(self):
        '''Zczytanie daty w formacie unix'''
        api_address = '/api/timeinfo'
        header = {}
        address = (api_address, header)
        r = self.reqGet(address)
        return r

    def getRegLog(self, start, stop, ids):
        '''Zczytanie wartosci logow'''
        api_address = '/api/register-log'
        header = {'X-WH-START': start,
                  'X-WH-END': stop,
                  'X-WH-REG-IDS': ids,
                  }
        address = (api_address, header)
        r = self.reqGet(address)
        return r

    def changeRegVal(self, ids, val):
        '''Zczytanie daty w formacie unix'''
        api_address = '/api/register-values/{0}'.format(ids)
        header = {}
        address = (api_address, header, val)
        r = self.reqPut(address)
        return r


if __name__ == '__main__':
    device_address1 = 'http://192.168.0.229'
    apikey1 = '72D4E648B82D17655636E19085FB3CFE9554BFCF'

    webHMI = Api(device_address1, apikey1)
    locTime = webHMI.connectionList()
    print(locTime)
