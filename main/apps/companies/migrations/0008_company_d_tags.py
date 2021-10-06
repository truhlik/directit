# Generated by Django 3.0 on 2020-11-27 10:01

from django.db import migrations, models


def denormalize_tags(apps, schema):
    Company = apps.get_model('companies.Company')
    for c in Company.objects.all():
        c.d_tags = ",".join(c.tags.all().values_list('name', flat=True))
        c.d_categories = ",".join(c.categories.all().values_list('name', flat=True))
        c.save()


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0007_company_plan'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='d_tags',
            field=models.CharField(blank=True, max_length=2048, null=True),
        ),
        migrations.AddField(
            model_name='company',
            name='d_categories',
            field=models.CharField(blank=True, max_length=2048, null=True),
        ),
        migrations.RunPython(denormalize_tags)
    ]
