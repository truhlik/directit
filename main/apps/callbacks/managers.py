from django.db import models
from django.utils import timezone


class CallBackRequestQuerySet(models.QuerySet):

    def owner(self, user):
        """ Vrátí company ve kterých je daný user vlastníkem. """
        return self.filter(user=user)

    def for_notification(self):
        dt = timezone.now() - timezone.timedelta(days=3)
        return self.filter(data__notification_sent_on__isnull=True, created_at__gte=dt)

    def mark_as_notified(self):
        return self.update(data={'notification_sent_on': str(timezone.now())})

    def consierge(self):
        return self.filter(callback_type__isnull=False)

    def callback(self):
        return self.filter(callback_type__isnull=True)
