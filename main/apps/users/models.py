import uuid

from django.db import models
from django.core.cache import cache
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from .managers import CustomUserManager, CustomUserQuerySet
from django.utils.translation import ugettext_lazy as _


class User(AbstractBaseUser, PermissionsMixin):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    first_name = models.CharField(_('jméno'), max_length=64)
    last_name = models.CharField(_('příjmení'), max_length=64)
    phone = models.CharField(_('telefon'), max_length=32, blank=True, null=True)
    email = models.EmailField(_('email'), unique=True, max_length=128)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False, help_text=_('určuje možnost přístupu do administrace'))
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
    job = models.CharField(blank=True, null=True, max_length=255)

    objects = CustomUserManager.from_queryset(CustomUserQuerySet)()
    USERNAME_FIELD = 'email'

    class Meta:
        verbose_name = _('uživatel')
        verbose_name_plural = _('uživatelé')
        ordering = ['last_name', 'first_name']

    def __str__(self):
        if self.first_name or self.last_name:
            return str(self.first_name + ' ' + self.last_name)
        else:
            return self.email

    @property
    def company(self):
        company = cache.get('user-company-{}'.format(self.id))
        if company is None:
            company = self.companies.first()
            cache.set('user-company', company)
        return company

    @property
    def full_name(self):
        return str(self)

    def has_paid_plan(self) -> bool:
        return self.company.has_paid_plan() if self.company is not None else False

    def is_client(self) -> bool:
        return self.company.is_client() if self.company is not None else False

    def is_consultant(self) -> bool:
        return self.company.is_consultant() if self.company is not None else False

    def is_supplier(self) -> bool:
        return self.company.is_supplier() if self.company is not None else False

    @property
    def role(self) -> str:
        return self.company.role if self.company else ""

    @property
    def plan(self) -> str:
        return self.company.plan if self.company else ""

