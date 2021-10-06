from typing import Tuple, Optional

from django.contrib.postgres.fields import JSONField
from django.db import models
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _

from main.libraries.functions import get_absolute_url
from main.libraries.models import BaseModel
from .managers import OrderQuerySet
from . import constants


class Order(BaseModel):
    objects = OrderQuerySet.as_manager()

    owner = models.ForeignKey('users.User', related_name='+', on_delete=models.CASCADE)
    company = models.ForeignKey('companies.Company', related_name='+', on_delete=models.SET_NULL, null=True)
    note = models.TextField('poznámka', blank=True, null=True)
    data = JSONField(default=dict, blank=True)
    date_from = models.DateField(_('datum od'), blank=True, null=True)
    duration = models.PositiveIntegerField(_('délka'), blank=True, null=True)
    categories = models.ManyToManyField('categories.Category', verbose_name=_('categories'), blank=True)
    products = models.ManyToManyField('products.Product', verbose_name=_('products'), blank=True)
    files = models.ManyToManyField('files.File', blank=True, related_name='orders')

    class Meta:
        verbose_name = 'objednávka'
        verbose_name_plural = 'objednávky'

    def __str__(self):
        return 'objednávka {}'.format(self.id or '')

    @property
    def admin_url(self):
        return get_absolute_url(reverse('admin:orders_order_change', args=(self.id, )))

    @property
    def duration_length(self):
        return self._get_duration()[1]

    @property
    def duration_unit(self):
        return self._get_duration()[0]

    def _get_duration(self) -> Tuple[Optional[str], Optional[int]]:
        if self.duration is None:
            return None, None

        if self.duration // 365 > 0:
            return constants.YEAR, round(self.duration / 365)

        if self.duration // 30 > 0:
            return constants.MONTH, round(self.duration / 30)

        return constants.DAY, self.duration
