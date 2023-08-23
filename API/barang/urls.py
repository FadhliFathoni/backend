from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.allBarang),
    path('add',views.index),
    path('<int:id_barang>',views.oneBarang),
    path('<int:id_barang>/delete',views.deleteBarang), 
    path('<int:id_barang>/update',views.updateBarang),
]
