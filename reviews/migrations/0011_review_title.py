# Generated by Django 4.1.2 on 2022-12-03 04:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0010_remove_review_product_alter_review_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='title',
            field=models.CharField(default='', max_length=40),
            preserve_default=False,
        ),
    ]