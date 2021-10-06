from django.utils import timezone

from django.db import models


class ProjectQuerySet(models.QuerySet):

    def owner(self, user):
        """ Vrátí Projekty ve kterých je daný user vlastníkem. """
        return self.filter(owner=user)

    def has_view_perm(self, user):
        """ Vrátí Projekty na které má uživatel permission alespoň vidět. """
        return self.filter(models.Q(owner=user) | models.Q(consultant=user.company) | models.Q(supplier=user.company))

    def for_notification(self):
        dt = timezone.now() - timezone.timedelta(days=3)
        return self.filter(data__notification_sent_on__isnull=True, created_at__gte=dt)

    def mark_as_notified(self):
        return self.update(data={'notification_sent_on': str(timezone.now())})
