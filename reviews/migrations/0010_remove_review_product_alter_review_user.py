# Generated by Django 4.1.2 on 2022-12-03 04:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0009_review_rating'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='product',
        ),
        migrations.AlterField(
            model_name='review',
            name='user',
            field=models.URLField(blank=True, null=True),
        ),
    ]
