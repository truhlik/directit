# Generated by Django 3.0 on 2021-06-18 10:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0002_service_icon_name'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='service',
            options={'ordering': ['order'], 'verbose_name': 'služba', 'verbose_name_plural': 'služby'},
        ),
        migrations.AddField(
            model_name='service',
            name='order',
            field=models.PositiveSmallIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='service',
            name='price',
            field=models.CharField(blank=True, max_length=64, null=True),
        ),
    ]
