# Generated by Django 3.0 on 2020-02-04 08:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_auto_20200204_0736'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='date_from',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='datum od'),
        ),
        migrations.AddField(
            model_name='order',
            name='date_from',
            field=models.DateField(blank=True, null=True, verbose_name='datum od'),
        ),
    ]
