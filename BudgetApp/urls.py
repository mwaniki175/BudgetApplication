
from django.contrib import admin
from django.urls import path
from BudgetApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home),
    path('about/', views.about),
    path('form/', views.form),
]
