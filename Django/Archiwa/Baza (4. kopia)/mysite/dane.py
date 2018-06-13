'''

0.Miesiąc
1.Lp.
2.Inwestor
3.Nr.Umowy
4.Kod
5.Status
6.Kierownik
7.FV
8.elektro
9.UWAGI
10.Kraj


Database.objects.create(data_dodania = timezone.now(),uaktualniony = timezone.now(),author =me,inwestor= i[2],nr_umowy = i[3],kod = i[4],kierownik = i[6],fv = i[7],montaz =i[8],uwagi = i[9],kraj =i[10])

from baza.models import Database
from django.contrib.auth.models import User
from django.utils import timezone
from dane import data

User.objects.all()
me = User.objects.get(username='admin')
lista=data()
for i in lista:
    Database.objects.create(author =me,inwestor= i[2],nr_umowy = i[3],kod = i[4],kierownik = i[6],fv = i[7],montaz =i[8],uwagi = i[9],kraj =i[10])

'''

def data():
    F = open('exel.csv', 'r')
    dict1 = {}
    lista = []
    for line in F.readlines():
        parts1=line.strip()
        parts2=parts1.split(';')
        lista.append(parts2)
    return lista
