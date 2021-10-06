from django.db.models.signals import post_save
from django.dispatch import receiver

from main.apps.messages.utils import create_thread_for_project
from main.apps.projects.models import Project


@receiver(post_save, sender=Project)
def create_thread(sender, instance, raw, created, **kwargs):
    if not created:
        return
    create_thread_for_project(instance)
