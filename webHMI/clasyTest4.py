import requests

device_adress1 = 'http://192.168.0.229'
apikey1 = '1D0DC2F189E5D96EB16AAD59A9A9C2C3C6FE3C0F'

device_adress2 = 'http://192.168.0.22'
apikey2 = '833FFE648B82D17655636E19085FB3CFE9554BFCF'


class Api():
    '''Klasa dodajaca urzadzenie webHMI'''

    def __init__(self, device_adress, apikey):
        self.device_adress = device_adress
        self.apikey = apikey

    def make_headers(self, update):
        '''Dodanie nagłowka do requesta'''
        # wspólny nagłówke dla wszystkich
        base_headers = {'X-WH-APIKEY': self.apikey,
                        'Accept': 'application/json',
                        'Content-Type': 'application/json',
                        "Accept - Encoding": "gzip, deflate, sdch",
                        }
        base_headers.update(update)  # dodanie potrzebnych naglowkow
        return base_headers

    def displayReaquest(self, adress):
        '''Request o potrzebne dane'''
        header = self.make_headers(adress[1])  # dodanie potrzebnych naglowków
        api_adress = adress[0]
        url = self.device_adress + api_adress
        r = requests.get(url, headers=header)
        return r.json()

    def displayTest(self, adress):
        '''Test zapytania'''
        header = self.make_headers(adress[1])
        api_adress = adress[0]
        return self.device_adress + api_adress, header

    def connectionList(self):
        '''Zczytanie listy połaczen webHMI'''
        api_adress = '/api/connections'
        header = {}
        adress=(api_adress,header)
        r=self.displayTest(adress)
        return r

    def registerList(self):
        '''Zczytanie listy rejestrow webHMI'''
        api_adress = '/api/registers'
        header = {}
        adress=(api_adress,header)
        r=self.displayTest(adress)
        return r

    def trendList(self):
        '''Zczytanie listy trendow webHMI'''
        api_adress = '/api/trends'
        header = {}
        adress=(api_adress,header)
        r=self.displayTest(adress)
        return r

    def graphList(self):
        '''Zczytanie listy grafow webHMI'''
        api_adress = '/api/graphs'
        header = {}
        adress=(api_adress,header)
        r=self.displayTest(adress)
        return r

    def getCurValue(self, conns):
        '''Zczytanie wartosci z rejestru'''
        api_adress = '/api/register-values'
        header = {'X-WH-CONNS': conns}
        adress=(api_adress,header)
        r=self.displayTest(adress)
        return r

    def getLocTime(self):
        '''Zczytanie daty w formacie unix'''
        api_adress = '/api/timeinfo'
        header = {}
        adress=(api_adress,header)
        r=self.displayTest(adress)
        return r

    def getRegLog(self, start, stop, ids):
        '''Zczytanie wartosci logow'''
        api_adress = '/api/register-log'
        header = {'X-WH-START': start,
                  'X-WH-END': stop,
                  'X-WH-REG-IDS': ids,
                  }
        adress=(api_adress,header)
        r=self.displayTest(adress)
        return r


if __name__ == '__main__':
    webHMI=Api(device_adress1,apikey1)
    locTime=webHMI.getLocTime()
    print(locTime)

<<<<<<< HEAD
webHMI2 = Device(device_adress2, apikey2)

regLog = webHMI1.getRegLog('123', '456', '1,2,3,4,5,6')
print(webHMI1.displayTest(regLog))
curVal = webHMI1.getCurValue('1,2,3,4')
print(webHMI1.displayTest(curVal))
regLog = webHMI1.getRegLog('333', '444', '1,2,3,4,5,6,7,8,9,10')
print(webHMI1.displayTest(regLog))
trendlist = webHMI1.trendList()
print(webHMI1.displayTest(trendlist))

regLog = webHMI2.getRegLog('123', '456', '1,2,3,4,5,6')
for i in webHMI2.displayTest(regLog):
    print(i)

conectionList=webHMI1.connectionList()
print (webHMI1.displayReaquest(conectionList))
#webHMI1.displayReaquest(conectionList)


=======
>>>>>>> 00905471baa3e9eb1cfc46e2a7d1e30816dc0dbc
