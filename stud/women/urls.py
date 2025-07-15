from django.contrib import admin
from django.urls import path
from women import views

urlpatterns = [
    path('', views.index),
    path('cat/<int:cat_id>/', views.categories),
]
