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


class Row(models.Model):

    customer=models.CharField(max_length=200, blank=True)
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
    link=models.CharField(max_length=200, blank=True)

    class Meta:
        ordering = ('-entry_date',)

    def __str__(self):
        return self.investor
