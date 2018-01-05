from django.conf.urls import url
from . import views

app_name='baza'
urlpatterns = [
    #url(r'^$', views.baza, name='baza'),
    #url(r'^(?P<nr_umowy>\d+)/$', views.baza, name='baza'),
    url(r'^$', views.BazaView.as_view(), name='baza'),
]
