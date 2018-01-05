from django.shortcuts import render
from .models import Database
from django.shortcuts import get_object_or_404
from django.views.generic import ListView


#TODO: Dodac widoki: deail reckord
#TODO: Dodac widoki: filtrownia po rekordach. Post.objects.all().order_by('created_date'),
#TODO: Dodac widoki: przeszukiwania, A gdybyśmy chciały wyświetlić wszystkie wpisy zawierające słowo 'title' w polu tytuł? Post.objects.filter(title__contains = 'tytuł')


class BazaView(ListView):
    queryset = Database.objects.all()
    context_object_name = 'baza'
    paginate_by = 2
    template_name = 'baza/index.html'
