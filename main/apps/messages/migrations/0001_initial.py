# Generated by Django 3.0 on 2021-05-07 10:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


def create_message_thread_for_all_projects(apps, schema):
    Project = apps.get_model('projects.Project')
    MessageThread = apps.get_model('custom_messages.MessageThread')
    ContentType = apps.get_model('contenttypes.ContentType')
    for p in Project.objects.all():
        ct = ContentType.objects.get_for_model(Project)
        MessageThread.objects.create(object_id=p.id, content_type=ct)


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('projects', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='MessageThread',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Vytvořeno')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Upraveno')),
                ('object_id', models.PositiveIntegerField()),
                ('content_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contenttypes.ContentType')),
            ],
            options={
                'verbose_name': 'vlákno zpráv',
                'verbose_name_plural': 'vlákna zpráv',
            },
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Vytvořeno')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Upraveno')),
                ('text', models.TextField()),
                ('owner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='messages', to=settings.AUTH_USER_MODEL)),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='custom_messages.Message')),
                ('thread', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='messages', to='custom_messages.MessageThread')),
            ],
            options={
                'verbose_name': 'zpráva',
                'verbose_name_plural': 'zprávy',
            },
        ),
        migrations.RunPython(create_message_thread_for_all_projects)
    ]
