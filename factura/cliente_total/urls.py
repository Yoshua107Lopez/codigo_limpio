# views.py
from django.shortcuts import render
from django.urls import path
from .views import dataView

urlpatterns = [
    path('orden/', dataView.as_view(), name='orden-list'),
    path('orden/<int:id>/', dataView.as_view(), name='orden-detail'),
]
