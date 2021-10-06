from django.test import TestCase
from django.core import mail
from django.utils import timezone

from model_bakery import baker

from ...notifications.email import send_project_notifications


class ProjectsManagerTestCase(TestCase):

    def setUp(self) -> None:
        super(ProjectsManagerTestCase, self).setUp()

    def test_send_notification_new(self):
        with self.settings(CELERY_TASK_ALWAYS_EAGER=True):
            baker.make('projects.Project')
            send_project_notifications()
            self.assertEqual(1, len(mail.outbox))

    def test_send_notification_alredy_sent(self):
        with self.settings(CELERY_TASK_ALWAYS_EAGER=True):
            baker.make('projects.Project', data={'notification_sent_on': str(timezone.now())})
            send_project_notifications()
            self.assertEqual(0, len(mail.outbox))
