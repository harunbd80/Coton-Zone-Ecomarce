# Generated by Django 5.0.4 on 2024-04-28 17:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0005_feature'),
    ]

    operations = [
        migrations.CreateModel(
            name='banner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('women', models.ImageField(blank=True, null=True, upload_to=None, verbose_name='Women Bennar Change')),
                ('man', models.ImageField(blank=True, null=True, upload_to=None, verbose_name='Man Bennar Change')),
                ('kid', models.ImageField(blank=True, null=True, upload_to=None, verbose_name='Kid’s fashion Benner Change')),
                ('cos', models.ImageField(blank=True, null=True, upload_to=None, verbose_name='Cosmetics Benner Change')),
                ('acc', models.ImageField(blank=True, null=True, upload_to=None, verbose_name='Accessories Benner Change')),
                ('name', models.CharField(max_length=50, verbose_name='Product Cetagory Name')),
            ],
        ),
    ]
