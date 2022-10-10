"""ferremax URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views 

from django.conf import settings
from django.conf.urls.static import static

from django.urls import include

from products.views import ProductListView

urlpatterns = [
    path('admin/', admin.site.urls,),
    path('', views.index, name='index'),
    path('contacto/', views.contacto, name='contacto'),
    path('catalogo/', views.catalogo, name='catalogo'),
    path('ofertas/', views.ofertas, name='ofertas'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register, name='register'),
    path('carrito/', include('cart.urls')),
    path('productos/', ProductListView.as_view(), name='productos'),
    path('detalles/', include('products.urls')),
    path('orden/', include('orders.urls')),
    path('direcciones/', include('shipping_addresses.urls')),
    path('codigos/', include('promo_codes.urls')),
    path('pagos', include('billing_profiles.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)