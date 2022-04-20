from django.forms import ModelForm
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
class RequestForm(ModelForm):
	class Meta:
		model =Request
		fields ='__all__'
class CreateUserForm(UserCreationForm):
	class Meta:
		model = User
		fields= ['username','email','password1','password2']
class ContactForm(ModelForm):
	message = forms.CharField(widget=forms.Textarea)
	class Meta:
		model=Contact
		fields=['name','email','message']


