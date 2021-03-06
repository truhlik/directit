# Generated by Django 3.0 on 2019-12-23 09:53

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='gps_lat',
            field=models.CharField(blank=True, max_length=16, null=True, verbose_name='GPS lat'),
        ),
        migrations.AddField(
            model_name='company',
            name='gps_lng',
            field=models.CharField(blank=True, max_length=16, null=True, verbose_name='GPS lng'),
        ),
        migrations.AlterField(
            model_name='company',
            name='city',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='město'),
        ),
        migrations.AlterField(
            model_name='company',
            name='data',
            field=django.contrib.postgres.fields.jsonb.JSONField(blank=True, default=dict, null=True, verbose_name='data'),
        ),
        migrations.AlterField(
            model_name='company',
            name='street_number',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='čp'),
        ),
        migrations.AlterField(
            model_name='company',
            name='zip',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='PSČ'),
        ),
    ]
