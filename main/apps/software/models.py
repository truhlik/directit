from django.contrib.postgres.fields import JSONField
from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _

from main.libraries.models import BaseModel
from .managers import SoftwareQuerySet
from . import constants


class Software(BaseModel):
    objects = SoftwareQuerySet.as_manager()

    owner = models.ForeignKey('users.User', verbose_name=_('kategorie'),
                              on_delete=models.CASCADE, related_name='software')
    categories = models.ManyToManyField('categories.Category', related_name='+', verbose_name=_('kategorie'))
    name = models.CharField(_('název'), max_length=255, null=True)
    service_contact = models.CharField(_('servisní kontakt'), blank=True, null=True, max_length=255)

    licence_type = models.CharField(_('typ licence'), choices=constants.LICENCE_TYPE_CHOICES, blank=True, null=True, max_length=32)
    licence_unit = models.CharField(_('metrika licence'), choices=constants.LICENCE_METRIC_CHOICES, blank=True, null=True, max_length=32)  # noqa
    licence_count = models.PositiveIntegerField(_('počet licencí'), blank=True, null=True)
    licence_till = models.DateField(_('licence platná do'), blank=True, null=True)

    find_alternative = models.BooleanField(_('najít alternativy'))
    watch_expiration = models.BooleanField(_('hlídat expiraci'))
    need_extension = models.BooleanField(_('potřeba rozšíření'))
    need_customization = models.BooleanField(_('potřeba cusomizace'))
    need_upgrade = models.BooleanField(_('potřeba ugprade'))

    note = models.TextField(_('poznámka'), blank=True, null=True)
    data = JSONField(default=dict, blank=True)

    class Meta:
        verbose_name = 'software'
        verbose_name_plural = 'software'

    def __str__(self):
        return self.name

    def mark_as_notified(self):
        self.data['notification_sent_on'] = str(timezone.now())
