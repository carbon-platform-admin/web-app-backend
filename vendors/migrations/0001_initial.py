# Generated by Django 4.1.2 on 2022-11-06 03:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Vendor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=35)),
                ('logo', models.URLField()),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
