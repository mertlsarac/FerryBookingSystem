# Generated by Django 2.0.3 on 2018-04-18 18:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('departure_city', models.CharField(choices=[('AMBARLI', 'Ambarlı'), ('ARMUTLU', 'Armutlu'), ('ARMUTLU_TATIL_KOYU', 'Armutlu Tatil Köyü'), ('AVCILAR', 'Avcılar'), ('AVSA_ADASI', 'Avşa Adası'), ('BANDIRMA', 'Bandırma'), ('BESIKTAS', 'Beşiktaş'), ('BOSTANCI', 'Bostancı'), ('BURSA_GUZEL_YALI', 'Bursa Güzel Yalı'), ('CINARCIK', 'Çınarcık'), ('ESENKOY', 'Esenköy'), ('KADIKOY', 'Kadıköy'), ('KARTAL', 'Kartal'), ('KUMLA', 'Kumla'), ('MARMARA_ADASI', 'Marmara Adası'), ('PENDIK', 'Pendik'), ('TOPCULAR', 'Topçular'), ('TUZLA', 'Tuzla'), ('YALOVA', 'Yalova'), ('YALOVA_DO', 'Yalova Do'), ('YENIKAPI', 'Yenikapı')], default='AMBARLI', max_length=20)),
                ('destination_city', models.CharField(choices=[('AMBARLI', 'Ambarlı'), ('ARMUTLU', 'Armutlu'), ('ARMUTLU_TATIL_KOYU', 'Armutlu Tatil Köyü'), ('AVCILAR', 'Avcılar'), ('AVSA_ADASI', 'Avşa Adası'), ('BANDIRMA', 'Bandırma'), ('BESIKTAS', 'Beşiktaş'), ('BOSTANCI', 'Bostancı'), ('BURSA_GUZEL_YALI', 'Bursa Güzel Yalı'), ('CINARCIK', 'Çınarcık'), ('ESENKOY', 'Esenköy'), ('KADIKOY', 'Kadıköy'), ('KARTAL', 'Kartal'), ('KUMLA', 'Kumla'), ('MARMARA_ADASI', 'Marmara Adası'), ('PENDIK', 'Pendik'), ('TOPCULAR', 'Topçular'), ('TUZLA', 'Tuzla'), ('YALOVA', 'Yalova'), ('YALOVA_DO', 'Yalova Do'), ('YENIKAPI', 'Yenikapı')], default='AMBARLI', max_length=20)),
                ('journey_date', models.DateTimeField(verbose_name='journey date')),
                ('with_a_car', models.BooleanField(default=False)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ticket.Company')),
            ],
        ),
    ]