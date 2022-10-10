from tabnanny import verbose
from django.db import models
from django.utils.html import format_html

class Estado(models.Model):
    name = models.CharField(max_length=150, verbose_name='Nombre')
    description = models.TextField(verbose_name='Descripcion')
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Estado'
        verbose_name_plural ='Estados'
        db_table = 'Estados'
        ordering = ['id']

class Category(models.Model):
    name = models.CharField(max_length=150, verbose_name='Nombre')
    description = models.TextField(verbose_name='Descripcion')
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural ='Categorias'
        db_table = 'categoria'
        ordering = ['id']

class Product(models.Model):
    name = models.CharField(max_length=150, verbose_name='Nombre')
    description = models.TextField(verbose_name='Descripcion')
    price = models.IntegerField(verbose_name='Precio')
    image = models.ImageField(upload_to='media', null=False, blank=False)
    Category = models.ForeignKey(Category, on_delete=models.CASCADE)
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural ='Productos'
        db_table = 'producto'
        ordering = ['id']

    def show_image(self):
        return format_html('<img src={} width="100" /> ', self.image.url)

class Tipopqrs(models.Model):
    name = models.CharField(max_length=150, verbose_name='Tipo')
    description = models.TextField(verbose_name='Descripcion')
    
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Tipo'
        verbose_name_plural ='Tipos'
        db_table = 'tipo'
        ordering = ['id']



class PQRS(models.Model):
    name = models.CharField(max_length=150, verbose_name='Nombre')
    surname = models.CharField(max_length=150, verbose_name='Apellido')
    tel = models.IntegerField(verbose_name='telefono')
    description = models.TextField(verbose_name='Comentario')
    email = models.EmailField(verbose_name='correo')
    Tipopqrs = models.ForeignKey(Tipopqrs, on_delete=models.CASCADE)
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'PQRS'
        verbose_name_plural ='PQRS'
        db_table = 'pqrs'
        ordering = ['id']


class Proveedor(models.Model):
    name = models.CharField(max_length=150, verbose_name='Nombre')
    description = models.TextField(verbose_name='Descripcion')
    surname = models.CharField(max_length=150, verbose_name='Apellido')
    motivo_social = models.CharField (max_length=20, verbose_name='Razon social')
    document = models.BigIntegerField(verbose_name='Documento')
    email = models.EmailField(verbose_name='Correo')
    addres = models.CharField(max_length=150, verbose_name='Direccion')
    estado = models.ForeignKey(Estado, on_delete=models.CASCADE)
    #category models.manytomanyfield(category)
    
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Proveedor'
        verbose_name_plural ='Proveedores'
        db_table = 'proveedor'
        ordering = ['id']

class Pedido(models.Model):
    date = models.DateField(verbose_name='Fecha')
    description = models.TextField(verbose_name='Descripcion')
    value = models.IntegerField(verbose_name='Precio')
    #category models.manytomanyfield(category)
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Pedido'
        verbose_name_plural ='Pedidos'
        db_table = 'pedido'
        ordering = ['id']


class Usuario(models.Model):
    name = models.CharField(max_length=150, verbose_name='Nombre')
    document = models.BigIntegerField(verbose_name='Documento')
    email = models.EmailField(verbose_name='Correo')
    addres = models.CharField(max_length=150, verbose_name='Direccion')
    #category models.manytomanyfield(category)
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural ='Usuarios'
        db_table = 'usuario'
        ordering = ['id']
        
class RegistrarPedidos(models.Model):
    date = models.DateField(verbose_name='Fecha')
    proveedor = models.OneToOneField(Proveedor, verbose_name='Proveedor', on_delete=models.CASCADE)
    description = models.TextField(verbose_name='Descripcion')
    precio = models.IntegerField(verbose_name='Precio')
    soporte_factura = models.FileField(verbose_name='Soporte Factura')