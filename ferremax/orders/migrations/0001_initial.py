# Generated by Django 4.1 on 2022-09-23 02:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import orders.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cart', '0002_cart_products'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_created=True)),
                ('status', models.CharField(choices=[(orders.models.OrderStatus['CREATED'], 'CREATED'), (orders.models.OrderStatus['PAYED'], 'PAYED'), (orders.models.OrderStatus['COMPLETED'], 'COMPLETED'), (orders.models.OrderStatus['CANCELED'], 'CANCELED')], default=orders.models.OrderStatus['CREATED'], max_length=50)),
                ('shipping_total', models.DecimalField(decimal_places=0, default=0, max_digits=8)),
                ('total', models.DecimalField(decimal_places=2, default=0, max_digits=8)),
                ('cart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cart.cart')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
