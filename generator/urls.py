from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('generate/', views.generate_password, name='generate_password'),
    path('history/', views.password_history, name='password_history'),
]
