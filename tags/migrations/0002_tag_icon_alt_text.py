# Generated by Django 4.1.2 on 2022-11-18 00:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tags', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tag',
            name='icon_alt_text',
            field=models.TextField(blank=True),
        ),
    ]
