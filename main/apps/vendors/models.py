from django.db import models


class Vendor(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        verbose_name = 'vendor'
        verbose_name_plural = 'vendors'

    def __str__(self):
        return self.name
