# Generated by Django 3.0 on 2021-05-21 09:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_product_image'),
        ('files', '0002_auto_20200721_1209'),
        ('orders', '0003_auto_20200204_0803'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='tags',
        ),
        migrations.AddField(
            model_name='order',
            name='files',
            field=models.ManyToManyField(blank=True, related_name='orders', to='files.File'),
        ),
        migrations.AddField(
            model_name='order',
            name='products',
            field=models.ManyToManyField(blank=True, to='products.Product', verbose_name='products'),
        ),
    ]
