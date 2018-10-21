from django.db import models
from users.models import Users

class weathersensors(models.Model):
    userid = models.IntegerField()
    temp = models.FloatField()
    humidity = models.FloatField()
    rain = models.IntegerField()
    time = models.TimeField(null=True)
    date = models.DateField(null=True)

    def __str__(self):
        return str(self.date) + ' - ' + str(self.time) + '(' + str(self.id) + ')'

class plantsensors(models.Model):
    entryid = models.ForeignKey(weathersensors, on_delete = models.CASCADE)
    soilmoisture = models.FloatField()
    def __str__(self):
        return str(self.entryid)


class reservoir(models.Model):
    userid = models.ForeignKey(Users, on_delete = models.CASCADE)
    reservoirname = models.CharField(max_length = 50, null = True)
    volume = models.FloatField(default = 10)
    
    def __str__(self):
        return str(self.reservoirname)

class reservoirdata(models.Model):
    entryid = models.ForeignKey(weathersensors, on_delete = models.CASCADE)
    reservoirid = models.ForeignKey(reservoir, on_delete = models.CASCADE)
    distance = models.FloatField(default = 0)
    actualHieght = models.FloatField(default= 35)
    ph = models.FloatField(default = 0)
    turbidity = models.FloatField(default = 0)
