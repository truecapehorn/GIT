import requests

device_adress = 'http://192.168.0.229'
apikey = '72D4E648B82D17655636E19085FB3CFE9554BFCF'


class Device():
    def __init__(self, device_adress, apikey):
        self.device_adress = device_adress
        self.apikey = apikey

    def api(self, adress):
        self.api_adress = adress[0]
        self.headres = adress[1]

    def displayReaquest(self):
        url = self.device_adress + self.api_adress
        r = requests.get(url, headers=self.headres)
        return r.json()

    def displayTest(self):
        return self.device_adress + self.api_adress, self.headres

    def connectionList(self):
        '''Zczytanie listy połaczen webHMI'''
        api_adress = '/api/connections'
        header = {'X-WH-APIKEY': self.apikey,
                  'Accept': 'application/json',
                  'Content-Type': 'application/json',
                  "Accept - Encoding": "gzip, deflate, sdch",
                  }
        return api_adress, header

    def registerList(self):
        '''Zczytanie listy rejestrow webHMI'''
        api_adress = '/api/registers/'
        header = {'X-WH-APIKEY': self.apikey,
                  'Accept': 'application/json',
                  'Content-Type': 'application/json',
                  "Accept - Encoding": "gzip, deflate, sdch",
                  }
        return api_adress, header

    def trendList(self):
        '''Zczytanie listy trendow webHMI'''
        api_adress = '/api/trends/'
        header = {'X-WH-APIKEY': self.apikey,
                  'Accept': 'application/json',
                  'Content-Type': 'application/json',
                  "Accept - Encoding": "gzip, deflate, sdch",
                  }
        return api_adress, header

    def graphList(self):
        '''Zczytanie listy grafow webHMI'''
        api_adress = '/api/graphs/'
        header = {'X-WH-APIKEY': self.apikey,
                  'Accept': 'application/json',
                  'Content-Type': 'application/json',
                  "Accept - Encoding": "gzip, deflate, sdch",
                  }
        return api_adress, header

    def getCurValue(self):
        '''Zczytanie wartosci z rejestru'''
        api_adress = '/api/register-values'
        header = {'X-WH-APIKEY': self.apikey,
                  'Accept': 'application/json',
                  'Content-Type': 'application/json',
                  'Accept - Encoding': 'gzip, deflate, sdch',
                  'X-WH-CONNS': '1,2',

                  }
        return api_adress, header

    def getLocTime(self):
        '''Zczytanie daty w formacie unix'''
        api_adress = '/api/timeinfo'
        header = {'X-WH-APIKEY': self.apikey,
                  'Accept': 'application/json',
                  'Content-Type': 'application/json',
                  "Accept - Encoding": "gzip, deflate, sdch",
                  }
        return api_adress, header

    def getRegLog(self, start, stop, ids):
        '''Zczytanie wartosci logow'''
        api_adress = '/api/register-log'
        header = {'X-WH-APIKEY': self.apikey,
                  'Accept': 'application/json',
                  'Content-Type': 'application/json',
                  "Accept - Encoding": "gzip, deflate, sdch",
                  'X-WH-START': start,
                  'X-WH-END': stop,
                  'X-WH-REG-IDS': ids,
                  }

        return api_adress, header


webHMI = Device(device_adress, apikey)

webHMI.api(webHMI.getRegLog('123', '456', '1,2,3,4,5,6'))
print(webHMI.displayTest())

webHMI.api(webHMI.getCurValue())
print(webHMI.displayTest())
