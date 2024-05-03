# Generated by Django 5.0.4 on 2024-05-03 15:32

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0025_alter_subscribe_email'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
                ('add', models.CharField(max_length=50, verbose_name='Add By Blog ')),
                ('img', models.ImageField(upload_to='Blog')),
                ('date', models.DateField()),
                ('cetagory', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Main.cetagory')),
            ],
            options={
                'verbose_name': 'Add To Blog Page',
            },
        ),
    ]