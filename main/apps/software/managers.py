from django.db import models
from django.utils import timezone


class SoftwareQuerySet(models.QuerySet):

    def owner(self, user):
        """ Vrátí company ve kterých je daný user vlastníkem. """
        return self.filter(owner=user)

    def for_notification(self):
        today = timezone.now().today().date()
        dt = timezone.now() + timezone.timedelta(days=30)
        return self.filter(data__notification_sent_on__isnull=True,
                           licence_till__lte=dt,
                           licence_till__gte=today,
                           watch_expiration=True)
