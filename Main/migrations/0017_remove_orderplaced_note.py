# Generated by Django 5.0.4 on 2024-04-30 16:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0016_alter_orderplaced_note'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderplaced',
            name='note',
        ),
    ]
