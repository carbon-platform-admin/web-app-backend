# Generated by Django 4.1.2 on 2023-01-20 22:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0039_alter_product_handle_alter_product_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image_src',
            field=models.URLField(max_length=500, null=True),
        ),
    ]
