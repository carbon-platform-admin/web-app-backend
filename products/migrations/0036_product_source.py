# Generated by Django 4.1.2 on 2023-01-04 02:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0035_alter_product_carbon_footprint'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='source',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
    ]