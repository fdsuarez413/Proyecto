from unicodedata import name
from django.urls import path
from . import views

app_name = 'cart'

urlpatterns = [
     path('', views.cart, name='cart'),
     path('agregar', views.add, name='add'),
     path('eliminar', views.remove, name='remove'),
]