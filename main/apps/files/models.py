from django.conf import settings
from django.db import models

from main.libraries.models import BaseModel
from .utils import uuid_gen_path
from .managers import FileQuerySet


class File(BaseModel):
    objects = FileQuerySet.as_manager()

    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='+', on_delete=models.SET_NULL, blank=True, null=True)
    file = models.FileField(upload_to=uuid_gen_path)
    title = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name = 'soubor'
        verbose_name_plural = 'soubory'
        ordering = ('created_at', )

    def __str__(self):
        return self.title if self.title else str(self.file)
