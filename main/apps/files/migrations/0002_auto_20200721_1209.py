# Generated by Django 3.0 on 2020-07-21 12:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('files', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='file',
            options={'ordering': ('created_at',), 'verbose_name': 'soubor', 'verbose_name_plural': 'soubory'},
        ),
    ]
