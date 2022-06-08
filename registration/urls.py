from django.urls import path
from registration import views

# TEMPLATE URLS

app_name = 'registration'

urlpatterns = [
    path('register', views.register, name='register'),
    path('login', views.user_login, name='login'),
]