from __future__ import unicode_literals
from django.db import models
from django import forms
from django.core.urlresolvers import reverse


class Users(models.Model):
	name = models.CharField(max_length=50)
	password = models.CharField(max_length=70)
	phone = models.CharField(max_length = 15, unique=True)
	address = models.CharField(max_length=150)
	currentplant = models.CharField(max_length = 50, null = True)
	currentreservoir = models.IntegerField(default = 0)
	plantcount = models.IntegerField(default = 0)
	vehicleCount = models.IntegerField(default = 0)
	membercount = models.IntegerField(default = 0)
	reservoircount = models.IntegerField(default = 0)

	def get_absolute_url(self):
		return reverse('users:login')

	def __str__(self):
		return self.name

class Plants(models.Model):
	userid = models.ForeignKey(Users, on_delete=models.CASCADE)
	plantName = models.CharField(max_length = 50)

	def __str__(self):
		return self.plantName

class Members(models.Model):
	userid = models.ForeignKey(Users, on_delete = models.CASCADE)
	memberName = models.CharField(max_length = 50)

	def __str__(self):
		return self.memberName

class Vehicles(models.Model):
	userid = models.ForeignKey(Users, on_delete = models.CASCADE)
	vehicle = models.CharField(max_length = 50)

	def __str__(self):
		return self.vehicle