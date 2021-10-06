from django.db import models
from django.utils.translation import ugettext_lazy as _

from mptt.fields import TreeForeignKey
from mptt.models import MPTTModel

from . import managers


class Category(MPTTModel):
    objects = managers.CategoryQuerySet.as_manager()

    name = models.CharField(_('název'), max_length=512, db_index=True)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')

    class MPTTMeta:
        order_insertion_by = ['name']

    class Meta:
        verbose_name = 'kategorie'
        verbose_name_plural = 'kategorie'
        ordering = ['name']

    def __str__(self):
        return self.name
