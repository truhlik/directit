import logging

from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.utils.functional import cached_property

from main.libraries.models import BaseModel


logger = logging.getLogger(__name__)


class MessageThread(BaseModel):
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

    class Meta:
        verbose_name = 'vlákno zpráv'
        verbose_name_plural = 'vlákna zpráv'

    def __str__(self):
        return str(self.id)


class Message(BaseModel):
    thread = models.ForeignKey('MessageThread', on_delete=models.CASCADE, related_name='messages')
    owner = models.ForeignKey('users.User', blank=True, null=True, on_delete=models.CASCADE, related_name='messages')
    text = models.TextField()
    parent = models.ForeignKey('self', blank=True, null=True, on_delete=models.CASCADE, related_name='children')

    class Meta:
        verbose_name = 'zpráva'
        verbose_name_plural = "zprávy"

    def __str__(self):
        return self.text[:64]

    @cached_property
    def replies(self):
        if hasattr(self, '_replies'):
            return self._replies
        return self.children.all().count()
