from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


class Database(models.Model):
    data_dodania = models.DateTimeField(auto_now_add=True)
    uaktualniony = models.DateTimeField(auto_now=True)
    data_realizacji = models.DateField(blank=True,null=True)
    author = models.ForeignKey(User, related_name='baza_rekord', on_delete=models.CASCADE)
    inwestor = models.CharField(max_length=30,blank=True)
    nr_umowy = models.DecimalField(max_digits=5, decimal_places=0,blank=True)
    kod = models.CharField(max_length=10,blank=True)
    kierownik = models.CharField(max_length=30,blank=True)
    fv = models.CharField(max_length=200,blank=True)
    montaz = models.CharField(max_length=200,blank=True)
    uwagi = models.TextField(blank=True)
    kraj = models.CharField(max_length=20,blank=True)
    STATUS_CHOICES = (('dodany', 'Dodany'),('realizowany', 'Realizowany'),('zakończony', 'Zakończony'),)
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='Dodany',
    )

    class Meta:
        ordering = ('-data_dodania',)

    def __str__(self):
        return self.inwestor

    def get_absolute_url(self):
        return '/baza/{}'.format(self.nr_umowy)
