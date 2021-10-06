from django.db import models
from django.utils.translation import ugettext_lazy as _

from .managers import TestimonialQuerySet
from main.libraries.models import BaseModel


class Testimonial(BaseModel):
    objects = TestimonialQuerySet.as_manager()

    owner = models.ForeignKey('users.User', verbose_name=_('od uživatele'),
                              on_delete=models.CASCADE, related_name='testimonials')
    company = models.ForeignKey('companies.Company', verbose_name=_('jaké společnosti'),
                                on_delete=models.CASCADE, related_name='testimonials')
    rating = models.PositiveSmallIntegerField(_('hodnocení'), null=True)
    text = models.TextField(_('slovní hodnocení'), blank=True, null=True)
    authorized = models.BooleanField(_('autorizováno'), default=False)

    class Meta:
        verbose_name = _('reference')
        verbose_name_plural = _('reference')

    def __str__(self):
        return '{} - {}'.format(self._meta.verbose_name, self.rating)
