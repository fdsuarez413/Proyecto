from django.contrib import admin
from.models import RegistrarPedidos, Tipopqrs, PQRS, Proveedor, Estado


admin.site.register(Tipopqrs)
admin.site.register(PQRS)
admin.site.register(Proveedor)
admin.site.register(Estado)
admin.site.register(RegistrarPedidos)