import requests

device_adress = 'http://192.168.0.229'
apikey = '72D4E648B82D17655636E19085FB3CFE9554BFCF'


class Device():
    def __init__(self, device_adress, apikey):
        self.device_adress = device_adress
        self.apikey = apikey
        self.headers = {'X-WH-APIKEY': self.apikey,
                        'Accept': 'application/json',
                        'Content-Type': 'application/json',
                        "Accept - Encoding": "gzip, deflate, sdch",
                        }

    def displayReaquest(self, adress):
        self.headers.update(adress[1])
        self.api_adress = adress[0]
        url = self.device_adress + self.api_adress
        r = requests.get(url, headers=self.headers)
        return r.json()

    def displayTest(self, adress):
        self.headers.update(adress[1])
        self.api_adress = adress[0]
        return self.device_adress + self.api_adress, self.headers

    def connectionList(self):
        '''Zczytanie listy połaczen webHMI'''
        api_adress = '/api/connections'
        header = {}
        return api_adress, header

    def registerList(self):
        '''Zczytanie listy rejestrow webHMI'''
        api_adress = '/api/registers/'
        header = {}
        return api_adress, header

    def trendList(self):
        '''Zczytanie listy trendow webHMI'''
        api_adress = '/api/trends/'
        header = {}
        return api_adress, header

    def graphList(self):
        '''Zczytanie listy grafow webHMI'''
        api_adress = '/api/graphs/'
        header = {}
        return api_adress, header

    def getCurValue(self):
        '''Zczytanie wartosci z rejestru'''
        api_adress = '/api/register-values'
        header = {'X-WH-CONNS': '1,2'}
        return api_adress, header

    def getLocTime(self):
        '''Zczytanie daty w formacie unix'''
        api_adress = '/api/timeinfo'
        header = {}
        return api_adress, header

    def getRegLog(self, start, stop, ids):
        '''Zczytanie wartosci logow'''
        api_adress = '/api/register-log'
        header = {'X-WH-START': start,
                  'X-WH-END': stop,
                  'X-WH-REG-IDS': ids,
                  }

        return api_adress, header


webHMI = Device(device_adress, apikey)

regLog = webHMI.getRegLog('123', '456', '1,2,3,4,5,6')
print(webHMI.displayTest(regLog))
curVal = webHMI.getCurValue()
print(webHMI.displayTest(curVal))
regLog = webHMI.getRegLog('333', '444', '1,2,3,4,5,6,7,8,9,10')
print(webHMI.displayTest(regLog))
trendlist = webHMI.trendList()
print(webHMI.displayTest(trendlist))
