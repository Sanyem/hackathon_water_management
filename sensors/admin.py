from django.contrib import admin
from .models import weathersensors, plantsensors, reservoir, reservoirdata

admin.site.register(weathersensors)
admin.site.register(plantsensors)
admin.site.register(reservoir)
admin.site.register(reservoirdata)