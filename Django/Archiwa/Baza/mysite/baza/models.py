from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


'''

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

'''



class Database(models.Model):
    STATUS_CHOICES = (('dodany', 'Dodany'),('realizowany', 'Realizowany'),('zakończony', 'Zakończony'),)
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


    class Meta:
        ordering = ('-data_dodania',)

    def __str__(self):
        return self.inwestor

    def get_absolute_url(self):
        return '/baza/{}'.format(self.nr_umowy)