from django.contrib import admin
from django.urls import path
from address import views

urlpatterns = [
    path('', views.home),
    path('write', views.write),
    path('insert', views.insert),
    path('detail', views.detail),
    path('update', views.update),
    path('delete', views.delete),
]