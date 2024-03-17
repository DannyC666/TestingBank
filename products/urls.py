
from django.contrib import admin
from django.urls import path
from .import views
urlpatterns = [
    path('',views.select_client,name='select_client'),
    path('client_product/<int:pk>/',views.client_product),
  
]
