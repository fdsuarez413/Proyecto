from django.db import models
from users.models import User
from enum import Enum
# Create your models here.

class ShippingAddres(models.Model): #Nombre erroneo
    user = models.ForeignKey(User, null=False, blank=False, on_delete=models.CASCADE)
    linea1 = models.CharField(max_length=200, verbose_name='Direccion 1')
    linea2 = models.CharField(max_length=200, blank=True, verbose_name='Direccion 2')
    city = models.CharField(max_length=100, verbose_name='Ciudad', default="Bogotá")
    state = models.CharField(max_length=100, verbose_name='Barrio')
    country = models.CharField(max_length=50, verbose_name='Pais', default="Colombia")
    reference = models.CharField(max_length=300, verbose_name='Anotacion')
    postal_code = models.CharField(max_length=10, null=False, blank=False, verbose_name='Codigo Postal')
    default = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.postal_code
    
    def has_orders(self):
        return self.order_set.count() >=1
    
    def update_default(self, default=False):
        self.default = default
        self.save()
    
    @property #Si hay error eliminar
    def address(self):
        return '{} - {} - {}'.format(self.country, self.city, self.state)