from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('info/', views.info, name='info'),
    path('update/', views.update, name= 'update'),

    path('perishable/', views.perishable, name='perishable'),
    path('non_perishable/', views.non_perishable,name='non_perishable'),
    path('health/', views.health, name='health'),

    path('request/', views.request, name='request'),

    path('register/', views.registerPage, name="register"),
	path('login/', views.loginPage, name="login"),  
	path('logout/', views.logoutUser, name="logout"),
]