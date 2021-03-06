# Generated by Django 3.0 on 2020-01-28 14:49

from django.conf import settings
import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('categories', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Vytvořeno')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Upraveno')),
                ('name', models.CharField(max_length=255, null=True, verbose_name='název')),
                ('description', models.TextField(null=True, verbose_name='popis projektu')),
                ('due_date', models.DateField(null=True, verbose_name='realizace do')),
                ('data', django.contrib.postgres.fields.jsonb.JSONField(blank=True, default=dict, null=True, verbose_name='data')),
                ('categories', models.ManyToManyField(related_name='_project_categories_+', to='categories.Category', verbose_name='kategorie')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='projects', to=settings.AUTH_USER_MODEL, verbose_name='vlastník')),
            ],
            options={
                'verbose_name': 'projekt',
                'verbose_name_plural': 'projekty',
            },
        ),
    ]
