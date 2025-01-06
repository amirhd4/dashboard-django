# Generated by Django 4.2.17 on 2025-01-05 16:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Products',
            fields=[
                ('product_id', models.AutoField(primary_key=True, serialize=False)),
                ('product_name', models.CharField(max_length=80)),
                ('product_price', models.CharField(max_length=16)),
                ('product_description', models.TextField()),
                ('product_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='ProductChanges',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('product_price', models.CharField(max_length=16)),
                ('product_date', models.DateField()),
                ('product', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to='dashboard.products')),
            ],
        ),
    ]
