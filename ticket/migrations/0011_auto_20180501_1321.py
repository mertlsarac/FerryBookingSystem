# Generated by Django 2.0.3 on 2018-05-01 13:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ticket', '0010_auto_20180501_1021'),
    ]

    operations = [
        migrations.AlterField(
            model_name='passanger',
            name='email',
            field=models.CharField(blank=True, max_length=70),
        ),
    ]
