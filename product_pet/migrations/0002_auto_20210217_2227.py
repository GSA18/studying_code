# Generated by Django 3.1.6 on 2021-02-18 01:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product_pet', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productpet',
            name='weight',
            field=models.DecimalField(decimal_places=3, max_digits=9),
        ),
    ]
