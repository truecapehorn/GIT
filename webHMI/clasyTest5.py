import requests

device_adress1 = 'http://192.168.0.229'
apikey1 = '1D0DC2F189E5D96EB16AAD59A9A9C2C3C6FE3C0F'

device_adress2 = 'http://192.168.0.22'
apikey2 = '833FFE648B82D17655636E19085FB3CFE9554BFCF'


class Device():
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
        #print(r.json())
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
        return api_adress, header

    def registerList(self):
        '''Zczytanie listy rejestrow webHMI'''
        api_adress = '/api/registers'
        header = {}
        return api_adress, header

    def trendList(self):
        '''Zczytanie listy trendow webHMI'''
        api_adress = '/api/trends'
        header = {}
        return api_adress, header

    def graphList(self):
        '''Zczytanie listy grafow webHMI'''
        api_adress = '/api/graphs'
        header = {}
        return api_adress, header

    def getCurValue(self, conns):
        '''Zczytanie wartosci z rejestru
        r jest identyfikatorem rejestru. Na przykład 10
        v jest wartością rejestru w bieżącym czasie lub '-1', jeśli wartość nie powiodła się.
        s to stan rejestru, który dopasował go w określonym czasie. Unknown = u, Disabled = d, Normal = n, Ostrzeżenie = w, Alert = a, Niepoprawnie = i.
        '''
        api_adress = '/api/register-values'
        header = {'X-WH-CONNS': conns}
        return api_adress, header

    def getLocTime(self):
        '''Zczytanie daty w formacie unix'''
        api_adress = '/api/timeinfo'
        header = {}
        return api_adress, header

    def getRegLog(self, start, stop, ids):
        '''
        Zczytanie wartosci logow
        r jest identyfikatorem rejestru. Na przykład 10
        v jest wartością rejestru w określonym punkcie czasowym lub pustym łańcuchem, jeśli obecnie nie ma danych dla tego rejestru.
        s to stan rejestru, który dopasował go w określonym czasie. Nieznany = -1, Disabled = 0, Normal = 1, Ostrzeżenie = 2, Alert = 3 lub pusty ciąg znaków, jeśli wartości rejestru nie są.
        '''
        api_adress = '/api/register-log'
        header = {'X-WH-START': start,  # stop unix format
                  'X-WH-END': stop,  # koniec unix format
                  'X-WH-REG-IDS': ids,  # indentyfikator rejstru
                  }
        return api_adress, header


webHMI1 = Device(device_adress1, apikey1)

conectionList = webHMI1.connectionList()
registerList = webHMI1.registerList()
getCurVal = webHMI1.getCurValue('1')
getLocTime = webHMI1.getLocTime()
regLog = webHMI1.getRegLog('1528880160', '1528882760', '1,2,3,4,5,6,7,8,9')

print(webHMI1.displayReaquest(conectionList))
print(webHMI1.displayReaquest(registerList))
print(webHMI1.displayReaquest(getCurVal))
print('\n')
for i in webHMI1.displayReaquest(regLog):
    print(i)
