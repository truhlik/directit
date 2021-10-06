from django.db import models
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _
from django.contrib.postgres.fields import JSONField
from phonenumber_field.modelfields import PhoneNumberField

from main.libraries.functions import get_absolute_url
from main.libraries.models import BaseModel

from .managers import CallBackRequestQuerySet
from . import constants


# class CallBackType(models.Model):
#     name = models.CharField(_('typ callbacku'), max_length=255, unique=True)
#     email = models.EmailField(_('notifikační email'), blank=True, null=True)
#
#     class Meta:
#         verbose_name = _('typ callbacku')
#         verbose_name_plural = _('typy callbacků')
#
#     def __str__(self):
#         return self.name
#
#     @staticmethod
#     def seed():
#         for name in ['průzkum trhu', 'nezávislá reference']:
#             CallBackType.objects.create(name=name)


class CallBackRequest(BaseModel):
    objects = CallBackRequestQuerySet.as_manager()

    # callback_type = models.ForeignKey('CallBackType', null=True, on_delete=models.SET_NULL)
    callback_type = models.CharField('typ', choices=constants.CALLBACK_TYPE_CHOICES, max_length=128, blank=True, null=True)  # noqa
    user = models.ForeignKey('users.User', blank=True, null=True, on_delete=models.CASCADE)
    name = models.CharField(_('jméno'), max_length=255, null=True)
    phone = PhoneNumberField(_('telefon'), max_length=255, null=True)
    time = models.TimeField(_('Vhodný čas pro hovor'), null=True)
    note = models.TextField(_('Poznámka'), blank=True, null=True)
    data = JSONField(default=dict, blank=True)
    tags = models.ManyToManyField('tags.Tag', blank=True)
    categories = models.ManyToManyField('categories.Category', blank=True)

    @property
    def admin_url(self):
        return get_absolute_url(reverse('admin:callbacks_callbackrequest_change', args=(self.id, )))
