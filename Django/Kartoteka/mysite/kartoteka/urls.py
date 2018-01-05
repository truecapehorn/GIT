from django.conf.urls import url
from . import views

#app_name = 'kartoteka'
urlpatterns = [
    url(r'^$', views.RowsView.as_view(), name='row_list'),
    url(r'^sorted/$', views.SortView.as_view(), name='sort_list'),
    url(r'^search/$', views.row_search, name='row_search'),
    url(r'^row/(?P<pk>[0-9]+)/$', views.row_detail, name='row_detail'),
    url(r'^row/new/$', views.row_new, name='row_new'),
    url(r'^row/(?P<pk>[0-9]+)/edit/$', views.row_edit, name='row_edit'),
    url(r'^row/(?P<pk>[0-9]+)/delete/$', views.row_delete, name='row_delete'),
]
