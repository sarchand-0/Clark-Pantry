from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import RequestForm, CreateUserForm, ContactForm
from .filters import ItemFilter
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
# Create your views here.


def home(request):
	items = Item.objects.all()
	live=Live.objects.all()
	myFilter = ItemFilter(request.GET, queryset=items)
	items=myFilter.qs
	
	context= {'items':items,'myFilter':myFilter, 'live':live,}
	return render(request, 'shelf/home.html', context)
def items(request):
	items = Item.objects.all()
	
	myFilter = ItemFilter(request.GET, queryset=items)
	items=myFilter.qs
	
	context= {'items':items,'myFilter':myFilter}
	return render(request, 'shelf/items.html', context)


def info(request):
	form=ContactForm()
	if request.method=="POST":
		form = ContactForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('home')
		else:
			print("invalide")

	context={'form':form}
	return render(request, 'shelf/info.html',context)

def update(request):
	updates= Update.objects.all()
	context={'updates':updates}
	return render(request, 'shelf/update.html', context)

def perishable(request):
	perishable_items = Item.objects.filter(tags = "Perishable")
	context= {"perishable_items":perishable_items}
	return render(request,'shelf/perishable.html', context)

def non_perishable(request):
	non_perishable_items = Item.objects.filter(tags = "Non-perishable")
	context= {"non_perishable_items":non_perishable_items}
	return render(request,'shelf/non_perishable.html', context)

def health(request):
	health_item = Item.objects.filter(tags = "Health")
	context= {"health_item":health_item}
	return render(request,'shelf/health.html', context)


login_required(login_url='login')
def request(request):
	form = RequestForm()
	if request.method == 'POST':
		form = RequestForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('/')
	context={'form':form}
	return render(request,'shelf/request.html',context )

def registerPage(request):
	if request.user.is_authenticated:
		return redirect('home')
	else:
		form=CreateUserForm()
		if request.method=="POST":
			form=CreateUserForm(request.POST)
			if  form.is_valid():
				form.save()
				user= form.cleaned_data.get('username')
				messages.success(request, "Account was created for" + user)
				return redirect('login')
		context={'form':form}
		return render(request, 'shelf/register.html',context)

def loginPage(request):
	if request.user.is_authenticated:
		return redirect('home')
	else:
		if request.method == "POST":
			username=request.POST.get('username')
			password=request.POST.get('password')
			user=authenticate(request, username=username, password=password)
			if user is not None:
				login(request, user)
				return redirect('home')
			else:
				messages.info(request, "Incorrect Username or Password ")

		context={}
		return render(request, 'shelf/login.html',context)

def logoutUser(request):
	logout(request)
	return redirect('login')

login_required(login_url='login')

login_required(login_url='login')
def donate(request):
	return render(request,'shelf/donate.html' )