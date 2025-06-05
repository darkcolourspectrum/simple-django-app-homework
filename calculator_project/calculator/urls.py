"""
URL configuration for calculator app.
"""
from django.urls import path
from . import views

app_name = 'calculator'

urlpatterns = [
    path('', views.index, name='index'),
    path('calculate/', views.calculate_result, name='calculate'),
]