# Generated by Django 3.0 on 2021-06-11 10:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reference', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reference',
            name='client',
        ),
        migrations.AddField(
            model_name='reference',
            name='client_name',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='jméno klienta'),
        ),
    ]
