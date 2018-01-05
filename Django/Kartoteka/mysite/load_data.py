from kartoteka.models import Row
from django.contrib.auth.models import User
from django.utils import timezone

'''

Exportuje dane do bazy danych:

    STATUS_CHOICES = (('dodany', 'Dodany'), ('realizowany', 'Realizowany'), ('zakończony', 'Zakończony'),)
    state = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Dodany', )
    entry_date = models.DateTimeField(default=timezone.now)
    num = models.IntegerField(blank=True,null=True)
    entry_code = models.CharField(max_length=30, blank=True)
    author = models.ForeignKey(User, related_name='entries', blank=True, on_delete=models.CASCADE)
    last_modified = models.DateTimeField(auto_now=True)
    investor = models.CharField(max_length=30, blank=True)
    contract_number = models.CharField(max_length=30, blank=True)
    zip_code = models.CharField(max_length=30, blank=True)
    manager = models.CharField(max_length=30, blank=True)
    invoice = models.CharField(max_length=200, blank=True)
    design = models.CharField(max_length=200, blank=True)
    rcd_date = models.DateField(blank=True, null=True)
    implementation_date = models.DateField(blank=True, null=True)
    doer = models.CharField(max_length=30, blank=True)  # wykonawca
    comments = models.TextField(blank=True)
    coutry = models.CharField(max_length=30, blank=True)


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
