# Generated by Django 3.0 on 2020-01-24 10:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tags', '0001_initial'),
        ('callbacks', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='callbackrequest',
            name='tags',
            field=models.ManyToManyField(blank=True, to='tags.Tag'),
        ),
    ]