# Generated by Django 2.0.3 on 2018-05-01 10:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ticket', '0008_auto_20180421_2147'),
    ]

    operations = [
        migrations.AddField(
            model_name='passanger',
            name='vehicle',
            field=models.CharField(choices=[('bus', 'bus'), ('truck', 'truck'), ('car', 'car')], default='car', max_length=10),
        ),
    ]