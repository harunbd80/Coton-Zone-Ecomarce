# Generated by Django 5.0.4 on 2024-04-30 16:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0015_alter_orderplaced_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderplaced',
            name='note',
            field=models.CharField(max_length=50),
        ),
    ]
