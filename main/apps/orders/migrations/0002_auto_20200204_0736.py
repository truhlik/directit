# Generated by Django 3.0 on 2020-02-04 07:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tags', '0001_initial'),
        ('categories', '0001_initial'),
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='categories',
            field=models.ManyToManyField(blank=True, to='categories.Category', verbose_name='categories'),
        ),
        migrations.AddField(
            model_name='order',
            name='date_from',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='datum od'),
        ),
        migrations.AddField(
            model_name='order',
            name='duration',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='délka'),
        ),
        migrations.AddField(
            model_name='order',
            name='tags',
            field=models.ManyToManyField(blank=True, to='tags.Tag', verbose_name='tags'),
        ),
    ]