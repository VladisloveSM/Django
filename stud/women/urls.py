from django.contrib import admin
from django.urls import path
from women import views

urlpatterns = [
    path('', views.index),
    path('cat/<int:cat_id>/', views.categories),
    path('cat/<slug:cat_slug>/', views.categories_by_slug),
]
