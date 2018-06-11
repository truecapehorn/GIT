import requests


device_adress = 'http://192.168.0.229'
apikey = '72D4E648B82D17655636E19085FB3CFE9554BFCF'

head1='1'
head2='2'



class Device:
    def __init__(self,device_adress,apikey ):
        self.device_adress=device_adress
        self.apikey=apikey

class Api(Device):
    def __init__(self, device_adress, apikey, api_adress, headers):
        super().__init__(device_adress,apikey)
        self.api_adress = api_adress
        self.headres = headers

class Display(Api):

    def displayReaquest(self): # moze tu taj trzeba dodoac headres i moze wpierdolic jako klase
        url = self.device_adress + self.api_adress
        r = requests.get(url, headers=self.headres)
        return r.json()

    def displayTest(self):
        return print(self.device_adress + self.api_adress)



dis1=Display(device_adress,apikey,'api adres',head1)

dis1.displayTest()




