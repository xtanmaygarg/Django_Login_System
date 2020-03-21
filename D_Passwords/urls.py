from django.contrib import admin
from django.urls import path, include
from D_Passwords import views

# Template URLS........
app_name = 'D_Passwords'

urlpatterns = [
    path('register/', views.register, name = 'register'),
    path('user_login/', views.user_login, name = 'user_login'),
]
