from unicodedata import name
from urllib.parse import urlparse
from django.urls import path
from . import views

app_name = 'products'

urlpatterns = [
    path('search', views.ProductSearchListView.as_view(), name='search'),
    path('<slug:slug>', views.ProductDetailview.as_view(), name='detalles'),
]