# Generated by Django 2.0.3 on 2018-05-01 10:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ticket', '0009_passanger_vehicle'),
    ]

    operations = [
        migrations.AlterField(
            model_name='passanger',
            name='vehicle',
            field=models.CharField(choices=[('Without vehicle', 'Without vehicle'), ('Bus', 'Bus'), ('Truck', 'Truck'), ('Car', 'Car')], default='car', max_length=10),
        ),
    ]
