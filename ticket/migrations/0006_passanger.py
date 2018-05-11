# Generated by Django 2.0.3 on 2018-04-21 21:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ticket', '0005_auto_20180419_1950'),
    ]

    operations = [
        migrations.CreateModel(
            name='Passanger',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('surname', models.CharField(max_length=20)),
                ('email', models.EmailField(blank=True, max_length=70)),
                ('telephone', models.CharField(max_length=11)),
                ('journey', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ticket.Journey')),
            ],
        ),
    ]
