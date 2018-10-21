from __future__ import unicode_literals
from django.contrib import admin
from .models import Users, Plants, Members, Vehicles

admin.site.register(Users)
admin.site.register(Plants)
admin.site.register(Members)
admin.site.register(Vehicles)