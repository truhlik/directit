from django.db import models

from . import constatnts


class Service(models.Model):
    name = models.CharField('název služby', max_length=255)
    icon_name = models.CharField(blank=True, max_length=32, help_text='https://vue.architectui.com/architectui-vue-pro/#/elements/icons')
    time_duration = models.CharField('časová náročnost', max_length=255, blank=True)
    price = models.CharField(blank=True, null=True, max_length=64)
    description = models.TextField()
    milestone = models.IntegerField(choices=constatnts.MILESTONE_CHOICES)
    category = models.CharField('typ služby', max_length=32, choices=constatnts.SERVICE_CHOICES)
    order = models.PositiveSmallIntegerField(default=0)

    class Meta:
        verbose_name = "služba"
        verbose_name_plural = "služby"
        ordering = ['order']

    def __str__(self):
        return self.name
