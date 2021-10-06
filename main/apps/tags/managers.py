from django.db import models


class TagQuerySet(models.QuerySet):

    def full_text_search(self, term):
        """ Vrátí všechny tagy, které obsahují daný term. """
        return self.filter(name__unaccent__icontains=term)
