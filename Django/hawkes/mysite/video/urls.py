from django.conf.urls import url
from . import views

app_name = 'video'
urlpatterns = [
    url(r'^$', views.video, name='video'),
    #url(r'^(?P<video_id>\d+)/$', views.video, name='video'),

]
