# Generated by Django 4.1.2 on 2023-01-02 22:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0029_alter_product_handle'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='title',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
