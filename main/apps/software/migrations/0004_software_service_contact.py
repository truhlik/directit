# Generated by Django 3.0 on 2020-09-22 11:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('software', '0003_software_data'),
    ]

    operations = [
        migrations.AddField(
            model_name='software',
            name='service_contact',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='servisní kontakt'),
        ),
    ]