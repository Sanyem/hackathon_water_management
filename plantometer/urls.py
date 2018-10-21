from django.conf.urls import url, include
from django.contrib import admin
from django.shortcuts import redirect
from django.views.generic.base import RedirectView
from . import views
from django.contrib.auth import views as v

urlpatterns = [
	#url(r'^$', RedirectView.as_view(url='/users/')),
	url(r'^$', views.homepage, name='homepage'),
    url(r'^admin/', admin.site.urls),
    url(r'^users/', include('users.urls', namespace='users')),
    
    url(r'^sensors/', include('sensors.urls', namespace='sensors')),
    url(r'^logout/$', v.logout , {'next_page': '/'}),
    
]
