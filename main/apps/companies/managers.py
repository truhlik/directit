from django.db import models

from . import constants


class CompanyQuerySet(models.QuerySet):

    def prefetch_list(self):
        from main.apps.testimonials.models import Testimonial
        qs = Testimonial.objects.authorized().select_related('owner')

        return self.prefetch_related('tags__categories', 'categories', 'owners',
                                     models.Prefetch('testimonials', queryset=qs))

    def consultants_or_suppliers(self):
        return self.filter(role__in=[constants.COMPANY_ROLE_CONSULTANT, constants.COMPANY_ROLE_SUPPLIER])

    def clients(self):
        """ Vrátí pouze klienty. """
        return self.filter(role=constants.COMPANY_ROLE_CLIENT)

    def consultants(self):
        """ Vrátí pouze konzultanty. """
        return self.filter(role=constants.COMPANY_ROLE_CONSULTANT)

    def owner(self, user):
        """ Vrátí company ve kterých je daný user vlastníkem. """
        return self.filter(owners=user)

    def full_text_search(self, term):
        """ Vrátí všechny company, které odpovídají danému query. """
        return self.filter(name_public__unaccent__icontains=term)

    def suppliers(self):
        """ Vrátí pouze dodavatele. """
        return self.filter(role=constants.COMPANY_ROLE_SUPPLIER)
