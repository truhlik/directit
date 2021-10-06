from django.db import models

from main.apps.products.managers import ProductQuerySet
from main.apps.products.utils import product_dir_path


class Product(models.Model):
    objects = ProductQuerySet.as_manager()
    name = models.CharField(max_length=255)
    image = models.ImageField('logo', upload_to=product_dir_path, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    vendor = models.ForeignKey('vendors.Vendor', null=True, related_name='products', on_delete=models.CASCADE)
    suppliers = models.ManyToManyField('companies.Company', blank=True, related_name='products')
    categories = models.ManyToManyField('categories.Category', blank=True, related_name='products')
    tags = models.ManyToManyField('tags.Tag', blank=True, related_name='products')

    class Meta:
        verbose_name = 'produkt'
        verbose_name_plural = 'produkty'

    def __str__(self):
        return self.name
