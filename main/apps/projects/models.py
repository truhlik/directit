from django.contrib.postgres.fields import JSONField
from django.db import models
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _

from main.libraries.models import BaseModel
from .managers import ProjectQuerySet
from . import constants
from ...libraries.functions import get_absolute_url


class Project(BaseModel):
    objects = ProjectQuerySet.as_manager()

    owner = models.ForeignKey('users.User', verbose_name=_('vlastník'),
                              on_delete=models.CASCADE, related_name='projects')
    categories = models.ManyToManyField('categories.Category', related_name='+', verbose_name=_('kategorie'))
    name = models.CharField(_('název'), max_length=255, null=True)
    description = models.TextField(_('popis projektu'), null=True)
    due_date = models.DateField(_('realizace do'), null=True)
    status = models.PositiveSmallIntegerField('status projektu', choices=constants.PROJECT_STATUS_CHOICES,
                                              default=constants.PROJECT_STATUS_NEW)

    step1int = models.PositiveSmallIntegerField('Definice projektu', choices=constants.PROJECT_STEP_CHOICES,
                                                default=constants.PROJECT_STEP_NOT_DEMAND)
    step2int = models.PositiveSmallIntegerField('Základní návrh řešení', choices=constants.PROJECT_STEP_CHOICES,
                                                default=constants.PROJECT_STEP_NOT_DEMAND)
    step3int = models.PositiveSmallIntegerField('Studie trhu', choices=constants.PROJECT_STEP_CHOICES,
                                                default=constants.PROJECT_STEP_NOT_DEMAND)
    step4int = models.PositiveSmallIntegerField('Oslovení dodavatelů', choices=constants.PROJECT_STEP_CHOICES,
                                                default=constants.PROJECT_STEP_NOT_DEMAND)
    step5int = models.PositiveSmallIntegerField('Testování a Finální Selekce', choices=constants.PROJECT_STEP_CHOICES,
                                                default=constants.PROJECT_STEP_NOT_DEMAND)
    step6int = models.PositiveSmallIntegerField('Implementace', choices=constants.PROJECT_STEP_CHOICES,
                                                default=constants.PROJECT_STEP_NOT_DEMAND)
    consultant = models.ForeignKey('companies.Company', blank=True, null=True, on_delete=models.SET_NULL,
                                   related_name='projects')
    supplier = models.ForeignKey('companies.Company', blank=True, null=True, on_delete=models.SET_NULL,
                                 related_name='supplier_projects')
    files = models.ManyToManyField('files.File', blank=True, related_name='projects')

    data = JSONField(default=dict, blank=True)

    class Meta:
        verbose_name = 'projekt'
        verbose_name_plural = 'projekty'

    def __str__(self):
        return self.name

    def __getattr__(self, item):
        if item.startswith('step'):
            return self.get_step(item)
        return super(Project, self).__getattr__(item)

    def get_step(self, item):
        return self.data.get(item, None) if self.data is not None else None

    @property
    def admin_url(self):
        return get_absolute_url(reverse('admin:callbacks_callbackrequest_change', args=(self.id, )))
