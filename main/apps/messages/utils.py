from django.contrib.contenttypes.models import ContentType
from main.apps.messages.models import MessageThread
from main.apps.projects.utils import get_users_for_project


def can_write_to_thread(content_object, user) -> bool:
    if user.is_staff:
        return True

    # predpokladam, ze content object je Project
    if user in get_users_for_project(content_object):
        return True

    return False


def create_thread_for_project(project):
    ct = ContentType.objects.get_for_model(project)
    thread, created = MessageThread.objects.get_or_create(content_type=ct, object_id=project.id)
