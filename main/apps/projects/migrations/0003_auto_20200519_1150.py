# Generated by Django 3.0 on 2020-05-19 11:50

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_auto_20200128_1608'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='data',
            field=django.contrib.postgres.fields.jsonb.JSONField(blank=True, default=dict),
        ),
        migrations.AlterField(
            model_name='project',
            name='step1',
            field=models.BooleanField(verbose_name='Definice projektu'),
        ),
        migrations.AlterField(
            model_name='project',
            name='step2',
            field=models.BooleanField(verbose_name='Základní návrh řešení'),
        ),
        migrations.AlterField(
            model_name='project',
            name='step3',
            field=models.BooleanField(verbose_name='Studie trhu'),
        ),
        migrations.AlterField(
            model_name='project',
            name='step4',
            field=models.BooleanField(verbose_name='Oslovení dodavatelů'),
        ),
        migrations.AlterField(
            model_name='project',
            name='step5',
            field=models.BooleanField(verbose_name='Testování a Finální Selekce'),
        ),
        migrations.AlterField(
            model_name='project',
            name='step6',
            field=models.BooleanField(verbose_name='Implementace'),
        ),
    ]
