from django.db import models
from django.contrib.auth.models import User


class Tag(models.Model):

	name = models.CharField(max_length=200, null=True)

	def __str__(self):
		return self.name
	

class Student(models.Model):
	user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
	id=models.IntegerField(primary_key=True)
	name = models.CharField(max_length=200, null=True)
	email = models.CharField(max_length=200, null=True)
	def __str__(self):
		return self.name

class Item(models.Model):
	name = models.CharField(max_length=200, null=True)
	id=models.IntegerField(primary_key=True)
	img = models.ImageField(default="product.png", null=True, blank=True)
	Stock = models.IntegerField(null=True)
	tags = models.ManyToManyField(Tag)
	def __str__(self):
		return self.name
	




# Create your models here.
