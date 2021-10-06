from django.db import models


class ReferenceQuerySet(models.QuerySet):

    def full_text_search(self, term):
        """ Vrátí všechny reference, které odpovídají danému query. """
        return self.filter(title__unaccent__icontains=term)
