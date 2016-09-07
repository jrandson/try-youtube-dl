from django.conf import settings
from django.conf.urls import url
from django.contrib import admin
from django.conf.urls.static import static

from . import views

app_name = 'tryYoutubeDl'

urlpatterns = [
	url(r'^$', views.index, name='index' ),
]

if settings.DEBUG :
    urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
