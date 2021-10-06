from django.db import models
from django.utils.translation import ugettext_lazy as _

from . import managers


class Tag(models.Model):
    objects = managers.TagQuerySet.as_manager()

    name = models.CharField(_('název'), max_length=255, unique=True)
    image = models.ImageField(_('obrázek'), blank=True, null=True)
    categories = models.ManyToManyField('categories.Category', verbose_name=_('kategorie'), blank=True)

    class Meta:
        verbose_name = _('tag')
        verbose_name_plural = _('tagy')
        ordering = ['name']

    def __str__(self):
        return self.name
