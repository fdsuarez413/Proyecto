# Generated by Django 4.1 on 2022-10-04 21:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shipping_addresses', '0002_alter_shippingaddres_city_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shippingaddres',
            name='postal_code',
            field=models.CharField(max_length=10, verbose_name='Codigo Postal'),
        ),
    ]