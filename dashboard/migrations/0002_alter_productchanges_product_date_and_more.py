# Generated by Django 4.2.17 on 2025-01-05 16:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productchanges',
            name='product_date',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='products',
            name='product_date',
            field=models.DateTimeField(),
        ),
    ]
