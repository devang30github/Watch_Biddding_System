#urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('home/',views.home,name='home'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('add_watch/', views.add_watch, name='add_watch'),
    path('watches/', views.list_watches, name='list_watches'),
    path('bid/<int:watch_id>/', views.place_bid, name='place_bid'),
    path('profile/', views.user_profile, name='user_profile'),
    
]