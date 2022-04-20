from django.shortcuts import render
from django.http import HttpResponse
from .models import *

# Create your views here.
def home(request):
	iteams= Iteam.objects.all()
	return render(request, 'shelf/home.html', {'iteams':iteams})

def info(request):
	return render(request, 'shelf/info.html')

def Iteam(request):

def update(request):
	return render(request, 'shelf/update.html')

