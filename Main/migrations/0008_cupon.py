# Generated by Django 5.0.4 on 2024-04-29 20:06

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0007_review'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cupon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=50, unique=True)),
                ('valid_from', models.DateField()),
                ('valid_to', models.DateField()),
                ('discaunt', models.FloatField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxLengthValidator(80)])),
                ('active', models.BooleanField(default=False)),
            ],
        ),
    ]
