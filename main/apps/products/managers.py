from django.db import models


class ProductQuerySet(models.QuerySet):

    def full_text_search(self, term):
        """ Vrátí všechny company, které odpovídají danému query. """
        return self.filter(name__unaccent__icontains=term)
