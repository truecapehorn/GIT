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
    1   ZLECENIODAWCA
    2	ROK
    3	MIESIAC(NAZWA)
    4	MIESIAC(LICZBA)
    5   SUFIX
    6   NR W MIESIACU
    7	Inwestor
    8    LINK
    9	Nr. Umowy
    10	UWAGI
    11	Status
    12	Kierownik
    13	FV
    14	PROJEKTANT
    15	Data różnicówki
    16	Data montażu
    17	Instalacje wykona
    18  KRAJ
    19	AFD


ex: 2011-09-01T13:20:30

Nalezy przygotowac plik exel tak aby moożliwe był export do bazy danych. Po odpowiednim przygotowaniu pliku
nalezy uruchomic testy które trzeba bedzie jescze dodac :)))

'''


def base(lista):
    User.objects.all()
    me = User.objects.get(username='admin')
    for i in lista:
        dataDodania = '{0}-{1}-{2}T13:20:30'.format(int(i[2]), int(i[4]), 1)

        Row.objects.create(entry_date=dataDodania, author=me, investor=i[7],
                           contract_number=i[9],manager=i[12], invoice=i[13],
                           design=i[14], comments=i[10], coutry=i[18],
                           num=int(i[0]),entry_code=i[5],customer=i[1],link=i[8],afd=i[19])
