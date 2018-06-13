import requests

device_adress1 = 'http://192.168.0.229'
apikey1 = '72D4E648B82D17655636E19085FB3CFE9554BFCF'

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

