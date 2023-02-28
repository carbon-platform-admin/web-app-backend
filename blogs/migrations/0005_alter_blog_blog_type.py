# Generated by Django 4.1.2 on 2023-02-24 22:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0004_blog_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='blog_type',
            field=models.CharField(choices=[('V', 'Vlog'), ('B', 'Blog'), ('A', 'Article')], max_length=20),
        ),
    ]