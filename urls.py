from django.conf import settings
from django.conf.urls import url
from django.contrib import admin
from django.conf.urls.static import static

from . import views

app_name = 'tryYoutubeDl'

urlpatterns = [
	url(r'^$', views.index, name='index' ),
	url(r'^download_from_url/$', views.download_from_url, name='download_from_url' ),
	url(r'^download_from_file/$', views.download_from_file, name='download_from_file' ),
]

if settings.DEBUG :
    urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
