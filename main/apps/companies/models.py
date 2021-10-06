from django.contrib.postgres.fields import JSONField
from django.db import models
from django.utils.translation import ugettext_lazy as _
from sorl.thumbnail import ImageField  # noqa

from main.libraries.location import get_lat_lng
from main.libraries.models import BaseModel
from main.libraries.utils import get_location_format
from .managers import CompanyQuerySet
from .utils import company_dir_path, first_letter_name, first_letter_in_word
from . import constants


class UserCompany(BaseModel):
    user = models.ForeignKey('users.User', on_delete=models.CASCADE, related_name='user_company')
    company = models.ForeignKey('companies.Company', on_delete=models.CASCADE, related_name='user_company')


class Company(BaseModel):
    objects = CompanyQuerySet.as_manager()

    owners = models.ManyToManyField('users.User',
                                    related_name='companies',
                                    through='companies.UserCompany',
                                    blank=True)

    role = models.CharField(_('typ subjektu'), choices=constants.COMPANY_ROLE_CHOICES, max_length=64)
    plan = models.CharField('Profil', choices=constants.PROFILE_CHOICES, max_length=32, default=constants.PROFILE_FREE)
    name = models.CharField(_('obchodní název'), max_length=512, db_index=True)
    name_public = models.CharField(_('obchodní název publikovatelný'), max_length=512, db_index=True)
    # image = ImageField(_('obrázek'), upload_to=company_dir_path, blank=True, null=True)
    image = models.ImageField(_('obrázek'), upload_to=company_dir_path, blank=True, null=True)
    description = models.TextField(_('popis'), blank=True, null=True)
    data = JSONField(_('data'), default=dict, blank=True, null=True)

    email = models.EmailField(_('email'), blank=True, null=True)
    phone = models.CharField(_('telefon'), max_length=32, blank=True, null=True)
    web = models.URLField(_('web'), blank=True, null=True)

    reg_number = models.CharField(_('IČ'), max_length=32, blank=True, null=True)
    vat_number = models.CharField(_('DIČ'), max_length=32, blank=True, null=True)

    street = models.CharField(_('ulice'), max_length=255, blank=True, null=True)
    street_number = models.CharField(_('čp'), max_length=255, blank=True, null=True)
    city = models.CharField(_('město'), max_length=255, blank=True, null=True)
    zip = models.CharField(_('PSČ'), max_length=255, blank=True, null=True)
    gps_lat = models.CharField(_('GPS lat'), max_length=32, blank=True, null=True)
    gps_lng = models.CharField(_('GPS lng'), max_length=32, blank=True, null=True)

    d_tags = models.CharField(max_length=2048, blank=True, null=True)
    d_categories = models.CharField(max_length=2048, blank=True, null=True)

    tags = models.ManyToManyField('tags.Tag', verbose_name=_('tags'), blank=True)
    categories = models.ManyToManyField('categories.Category', verbose_name=_('categories'), blank=True)

    class Meta:
        verbose_name = 'obchodní subjekt'
        verbose_name_plural = 'obchodní subjekty'
        ordering = ['name']

    def __str__(self):
        return self.name

    @property
    def address(self):
        return get_location_format(self.street_number, self.street, self.zip, self.city)

    def save(self, *args, **kwargs):
        if not self.gps_lat or not self.gps_lng:
            self.gps_lat, self.gps_lng = get_lat_lng(self.address)
        self.name_public = self.get_name_public()
        super(Company, self).save(*args, **kwargs)

    def get_name_public(self):
        if self.role == constants.COMPANY_ROLE_CONSULTANT:
            return first_letter_in_word(self.name)[:512]
        return self.name

    @property
    def email_public(self):
        if self.role == constants.COMPANY_ROLE_CONSULTANT:
            return first_letter_name(self.email)
        return self.email

    @property
    def phone_public(self):
        if self.role == constants.COMPANY_ROLE_CONSULTANT:
            return first_letter_name(self.phone)
        return self.phone

    @property
    def reg_number_public(self):
        if self.role == constants.COMPANY_ROLE_CONSULTANT:
            return first_letter_name(self.reg_number)
        return self.reg_number

    def has_paid_plan(self) -> bool:
        return self.plan in [constants.PROFILE_BASIC, constants.PROFILE_PREMIUM]

    def is_client(self) -> bool:
        return self.role == constants.COMPANY_ROLE_CLIENT

    def is_consultant(self) -> bool:
        return self.role == constants.COMPANY_ROLE_CONSULTANT

    def is_supplier(self) -> bool:
        return self.role == constants.COMPANY_ROLE_SUPPLIER
