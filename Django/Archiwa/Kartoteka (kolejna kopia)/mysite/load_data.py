from kartoteka.models import Row
from django.contrib.auth.models import User
from django.utils import timezone

'''

Exportuje dane do bazy danych:



Polecenia w shell:

from import_data import data
from load_data import base
lista=data()
base(lista)


lista= []
0	LP
1	SUFIX
2	DZIEN
3	MIESIAC
4	ROK
5	Inwestor
6	Nr. Umowy
7	Kod
8	Status
9	Kierownik
10	FV
11	elektro
12	Data różnicówki
13	Data montażu
14	Instalacje wykona
15	uwagi
16	Kraj

ex: 2011-09-01T13:20:30

'''


def base(lista):
    User.objects.all()
    me = User.objects.get(username='admin')
    for i in lista:
        dataDodania = '{0}-{1}-{2}T13:20:30'.format(int(i[4]), int(i[3]), int(i[2]))
        Row.objects.create(entry_date=dataDodania, author=me, investor=i[5], contract_number=i[6], zip_code=i[7],
                           manager=i[9], invoice=i[10], design=i[11], comments=i[15], coutry=i[16], num=int(i[0]),
                           entry_code=i[1])
