from django.db import models
from django.contrib.auth.models import User


	

class Student(models.Model):
	user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
	id=models.IntegerField(primary_key=True)
	name = models.CharField(max_length=200, null=True)
	email = models.CharField(max_length=200, null=True)
	def __str__(self):
		return self.name

class Item(models.Model):
	name = models.CharField(max_length=200, null=True)
	img = models.ImageField(null=True, blank=True)
	Stock = models.IntegerField(null=True)
	TAG = (
			('Perishable', 'Perishable'),
			('Non-perishable', 'Non-perishable'),
			('Health', 'Health'),
			) 
	tags = models.CharField(max_length=200, null=True, choices=TAG)

	def __str__(self):
		return self.name

class Request(models.Model):
	name = models.CharField(max_length=200, null=True)
	TAG = (
			('Perishable', 'Perishable'),
			('Non-perishable', 'Non-perishable'),
			('Health', 'Health'),
			) 
	tags = models.CharField(max_length=200, null=True, choices=TAG)
	
	def __str__(self):
		return self.name
class Contact(models.Model):
	
	name = models.CharField(max_length=200, null=True)
	email = models.CharField(max_length=200, null=True)
	message = models.CharField(max_length=200, null=True)
	
	def __str__(self):
		return self.name

class Update(models.Model):
	
	message = models.CharField(max_length=200, null=True)
	date_created = models.DateTimeField(auto_now_add=True, null=True)
	


class Live(models.Model):
	
	img = models.ImageField(null=True, blank=True)
	date_created = models.DateTimeField(auto_now_add=True, null=True)
	




# Create your models here.
