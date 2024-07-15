# Generated by Django 5.0.7 on 2024-07-12 14:45

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=125, verbose_name='Kompaniya nomi')),
                ('phone', models.CharField(max_length=15, verbose_name='telefon raqami')),
                ('address', models.CharField(max_length=200, verbose_name='location')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=125, verbose_name='Mahsulot nomi')),
                ('price', models.PositiveIntegerField(verbose_name='narxi')),
                ('qty', models.PositiveIntegerField(verbose_name='miqdori')),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='todo.company')),
            ],
        ),
        migrations.CreateModel(
            name='Sale',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_name', models.CharField(max_length=150, verbose_name='xaridor ismi')),
                ('qty', models.PositiveIntegerField(verbose_name='miqdori')),
                ('product_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='todo.product', verbose_name='mahsulot nomi')),
            ],
        ),
    ]