from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    url(r'^rango/', include('rango.urls')),
    url(r'^admin/', admin.site.urls),
]
if settings.DEBUG is True:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)