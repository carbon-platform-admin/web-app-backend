# Generated by Django 4.1.2 on 2023-01-21 01:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0043_alter_product_variant_sku'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='variant_SKU',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
