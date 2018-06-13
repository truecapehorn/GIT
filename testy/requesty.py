import requests
import json

r = requests.get('http://api.openweathermap.org/data/2.5/find?q=Bialystok&type=like&appid=3d039646360b064fa3d418287bd8009c')

text=r.text
jsones=r.json()

print(jsones)

data = json.loads(jsones.decode()) if not isinstance(jsones, dict) else jsones
cities = ["{} ({})".format(d['name'], d['sys']['country']) for d in data['list']]
temp =  ['Temperatura {}'.format(d['main']['temp']) for d in data['list']]
wind=['Wiatr {}'.format(d['wind']['speed']) for d in data['list']]



print(cities)
print(temp)
