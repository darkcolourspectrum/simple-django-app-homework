"""
URL configuration for calculator_project project.
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('calculator/', include('calculator.urls')),
    path('', include('calculator.urls')),  # Главная страница тоже будет калькулятор
]