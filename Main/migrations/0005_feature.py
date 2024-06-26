# Generated by Django 5.0.4 on 2024-04-27 11:16

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0004_best_sels_hottrend'),
    ]

    operations = [
        migrations.CreateModel(
            name='feature',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Main.product', verbose_name='Add To Feature Product')),
            ],
            options={
                'verbose_name_plural': 'Product Feature',
            },
        ),
    ]
