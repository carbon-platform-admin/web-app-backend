# Generated by Django 4.1.2 on 2022-11-08 00:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0018_alter_product_vendor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='gift_card',
            field=models.BooleanField(default=False, null=True),
        ),
    ]
