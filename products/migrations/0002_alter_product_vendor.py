# Generated by Django 4.1.2 on 2022-11-06 03:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vendors', '0002_remove_vendor_id_alter_vendor_name'),
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='vendor',
            field=models.ForeignKey(db_column='vendor_name', on_delete=django.db.models.deletion.CASCADE, related_name='products', to='vendors.vendor'),
        ),
    ]
