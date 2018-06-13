from kartoteka.models import Row
from django.contrib.auth.models import User
from django.utils import timezone

'''

Exportuje dane do bazy danych:




    status = models.CharField(max_length=20,choices=STATUS_CHOICES,default='Dodany',)
    data_dodania = models.DateTimeField(auto_now_add=False, default=timezone.now())
    uaktualniony = models.DateTimeField(auto_now=True)
    lp=models.IntegerField()
    sufix=models.CharField(max_length=30,blank=True)
    author = models.ForeignKey(User, related_name='baza_rekord', on_delete=models.CASCADE)
    inwestor = models.CharField(max_length=30,blank=True)
    nr_umowy = models.CharField(max_length=30,blank=True)
    kod = models.CharField(max_length=30,blank=True)
    kierownik = models.CharField(max_length=30,blank=True)
    fv = models.CharField(max_length=200,blank=True)
    projekt = models.CharField(max_length=200,blank=True)
    data_roznicowki = models.DateField(blank=True,null=True)
    data_realizacji = models.DateField(blank=True, null=True)
    wykonawca = models.CharField(max_length=30,blank=True)
    uwagi = models.TextField(blank=True)
    kraj = models.CharField(max_length=30,blank=True)



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
        Row.objects.create(data_dodania='{0}-{1}-{2}T13:20:30'.format(int(i[4]),int(i[3]),int(i[2])),author=me, inwestor=i[5], nr_umowy=i[6], kod=i[7], kierownik=i[9], fv=i[10], projekt=i[11],
                                uwagi=i[15], kraj=i[16],lp=int(i[0]),sufix=i[1])
