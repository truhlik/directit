from django.db import models

from .managers import ReferenceQuerySet
from ..companies.utils import first_letter_name
from ..sectors.constants import BUSSINES_SECTOR_CHOICES


class Reference(models.Model):
    objects = ReferenceQuerySet.as_manager()
    owner = models.ForeignKey('users.User', related_name='references', on_delete=models.SET_NULL, blank=True, null=True)
    solver = models.ForeignKey('companies.Company', related_name='solver_references', on_delete=models.SET_NULL, blank=True, null=True)

    category = models.ForeignKey('categories.Category', related_name='+', on_delete=models.SET_NULL, blank=True, null=True)
    products = models.ManyToManyField('products.Product', related_name='+', blank=True)
    sector = models.PositiveSmallIntegerField(choices=BUSSINES_SECTOR_CHOICES)

    title = models.CharField('title', max_length=255)
    client_name = models.CharField('jméno klienta', max_length=255, blank=True, null=True)
    contact_name = models.CharField('jméno', max_length=255, blank=True, null=True)
    contact_email = models.EmailField('email', max_length=255, blank=True, null=True)

    problem_text = models.TextField(blank=True, null=True)
    solution_text = models.TextField(blank=True, null=True)
    benefits_text = models.TextField(blank=True, null=True)

    files = models.ManyToManyField('files.File', blank=True, related_name='references')

    class Meta:
        verbose_name = 'reference'
        verbose_name_plural = 'references'

    def __str__(self):
        return self.title

    def public_contact_name(self) -> str:
        return first_letter_name(self.contact_name)

    def public_contact_email(self) -> str:
        return first_letter_name(self.contact_email)
