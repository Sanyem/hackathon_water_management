from django.conf.urls import url, include
from django.contrib import admin
from . import views

from django.contrib.auth import views as v
from sensors.forms import LoginForm

app_name = 'users'

urlpatterns = [

	url(r'^homepage$', views.homepage, name='homepage'),
	url(r'^loginpage/$', views.signUp, name='loginpage'),
	url(r'^data/$', views.temperature, name='data'),
	url(r'^login/$', views.login, name='login'),
	url(r'^logout/$', v.logout , {'next_page': '/'}, name='logout'), 
	url(r'', include('sensors.urls')),
	url(r'^addplant/$', views.addplant, name='addplant'),
	url(r'^addvehicle/$', views.addVehicle, name='addVehicle'),
	url(r'^addmember/$', views.addMember, name='addMember'),
	url(r'^addReservoir/$', views.addReservoir, name='addReservoir'),
	url(r'^api/login/$', views.mobile_login, name='mobile_login'),
]
