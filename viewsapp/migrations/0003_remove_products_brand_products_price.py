# Generated by Django 4.2.17 on 2025-01-16 07:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('viewsapp', '0002_remove_products_milage_products_mielage_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='products',
            name='brand',
        ),
        migrations.AddField(
            model_name='products',
            name='price',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
