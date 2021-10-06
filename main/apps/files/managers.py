from django.db import models


class FileQuerySet(models.QuerySet):

    def owner(self, user):
        return self.filter(user=user)
