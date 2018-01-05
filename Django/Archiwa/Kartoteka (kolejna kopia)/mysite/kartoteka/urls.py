from django.conf.urls import url
from . import views

#app_name = 'kartoteka'
urlpatterns = [
    url(r'^$', views.RowsView.as_view(), name='row_list'),
    url(r'^row/(?P<pk>[0-9]+)/$', views.row_detail, name='row_detail'),
]
