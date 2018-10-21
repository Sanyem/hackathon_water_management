from django.conf.urls import url

from . import views

from django.contrib.auth import views as v
app_name = 'sensors'

urlpatterns = [
	
    url(r'^logdata/$', views.sensor_data.as_view(), name = 'sensor_data'),
    url(r'^data/logout/$', v.logout , {'next_page': '/'}, name='logout'),
    url(r'^data/$', views.show_list, name = 'data'),
    url(r'^setreservoir/$', views.setreservoir, name = 'setreservoir'),
    url(r'^dataupdate/$', views.data_update, name = 'dataupdate'),
    url(r'^(?P<pid>[0-9]+)/$',views.DetailView,name='detail'),
    url(r'^api/drinking/$', views.drinking, name='drinking'),
]
