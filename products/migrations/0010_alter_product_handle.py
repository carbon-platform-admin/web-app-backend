# Generated by Django 4.1.2 on 2022-11-07 22:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0009_alter_product_handle'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='handle',
            field=models.CharField(max_length=100),
        ),
    ]
