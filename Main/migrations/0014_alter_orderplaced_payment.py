# Generated by Django 5.0.4 on 2024-04-30 16:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0013_alter_cupon_options_orderplaced'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderplaced',
            name='payment',
            field=models.CharField(blank=True, choices=[('Cash On Delivary', 'Cash On Dalivary'), ('Bikash', 'Bikash')], max_length=50, null=True),
        ),
    ]
