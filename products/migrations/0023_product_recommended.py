# Generated by Django 4.1.2 on 2022-11-11 10:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0022_alter_product_variant_requires_shipping_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='recommended',
            field=models.BooleanField(default=False, null=True),
        ),
    ]