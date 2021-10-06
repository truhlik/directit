from django.db import models


class TestimonialQuerySet(models.QuerySet):

    def authorized(self):
        """ Vrátí všechny autorizované Testimonialy. """
        return self.filter(authorized=True)

    def owner(self, user):
        """ Vrátí Testimonialy ve kterých je daný user vlastníkem. """
        return self.filter(owner=user)

