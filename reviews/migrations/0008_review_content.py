# Generated by Django 4.1.2 on 2022-11-11 12:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0007_remove_review_logo'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='content',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
    ]
