from django_filters.rest_framework import DjangoFilterBackend

from rest_framework.filters import SearchFilter
from django.db.models.constants import LOOKUP_SEP


class UnAccentSearchFilter(SearchFilter):
    lookup_prefixes = {
        '^': 'unaccent__istartswith',
        '=': 'unaccent__iexact',
        '@': 'search',
        '$': 'iregex',
        '!': ''
    }

    def construct_search(self, field_name):
        lookup = self.lookup_prefixes.get(field_name[0])
        if lookup:
            field_name = field_name[1:]
        else:
            lookup = 'unaccent__icontains'
        return LOOKUP_SEP.join([field_name, lookup])

    def get_search_terms(self, request):
        """
        Search terms are set by a ?search=... query parameter,
        and may be comma and/or whitespace delimited.
        """
        params = request.query_params.get(self.search_param, '')
        params = params.replace('\x00', '')  # strip null characters
        return params.split(",")


class CustomDjangoFilterBackend(DjangoFilterBackend):

    def get_coreschema_field(self, field):
        field_cls = super(CustomDjangoFilterBackend, self).get_coreschema_field(field)
        if field_cls.description == None or field_cls.description == '':
            field_cls.description = 'Dummy help text'
        return field_cls
