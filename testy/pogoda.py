import requests
import json


def pogoda():

    r = requests.get('http://api.openweathermap.org/data/2.5/find?q=Bialystok&type=like&appid=3d039646360b064fa3d418287bd8009c')

    text=r.text
    jsones=r.json()

    #print(jsones)

    data = json.loads(jsones.decode()) if not isinstance(jsones, dict) else jsones
    cities = ["{} ({})".format(d['name'], d['sys']['country']) for d in data['list']]
    temp =  ['{}'.format(d['main']['temp']) for d in data['list']]
    wind=['{}'.format(d['wind']['speed']) for d in data['list']]
    pressure=['{}'.format(d['main']['pressure']) for d in data['list']]
    icon=['{}'.format(d['weather'][0]['icon']) for d in data['list']]



    temp_float=float(temp[0])-272.15
    wiatr_float=float(wind[0])
    cisnienie_float=float(pressure[0])
    icona=icon[0]

    temperatura=round(temp_float,2)
    temperatura_int=int(temp_float*100)
    wiatr_int=int(wiatr_float*100)
    cisnienie_int=int(cisnienie_float)


    ic={'01d':1,'02d':2,'03d':3,'04d':4,'09d':5,'10d':6,'11d':7,'13d':8,'50d':9,
        '01n':10,'02n':11,'03n':12,'04n':13,'09n':14,'10n':15,'11n':16,'13n':17,'50n':18}



    #print(ic[icona])

    return temperatura_int, wiatr_int, cisnienie_int, ic[icona]
