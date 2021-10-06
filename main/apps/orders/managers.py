from django.db import models
from django.utils import timezone


class OrderQuerySet(models.QuerySet):

    def owner(self, user):
        """ Vrátí OrderCompany ve kterých je daný user vlastníkem. """
        return self.filter(owner=user)

    def for_notification(self):
        dt = timezone.now() - timezone.timedelta(days=3)
        return self.filter(data__notification_sent_on__isnull=True, created_at__gte=dt)

    def mark_as_notified(self):
        return self.update(data={'notification_sent_on': str(timezone.now())})
