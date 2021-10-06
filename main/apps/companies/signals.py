from django.db.models.signals import m2m_changed
from django.dispatch import receiver

from main.apps.companies.models import Company


@receiver(m2m_changed, sender=Company.tags.through)
def update_tags(sender, instance: Company, action, reverse, model, pk_set, using, **kwargs):
    if action == 'post_add':
        tag_str = ",".join(model.objects.filter(id__in=pk_set).values_list('name', flat=True))
        if instance.d_tags:
            instance.d_tags += ","
        instance.d_tags = (instance.d_tags or "") + tag_str
        instance.save()

    if action == 'post_remove':
        tag_str = ",".join(instance.tags.all().exclude(id__in=pk_set).values_list('name', flat=True))
        instance.d_tags = tag_str
        instance.save()


@receiver(m2m_changed, sender=Company.categories.through)
def update_categories(sender, instance: Company, action, reverse, model, pk_set, using, **kwargs):
    if action == 'post_add':
        categories_str = ",".join(model.objects.filter(id__in=pk_set).values_list('name', flat=True))
        if instance.d_categories:
            instance.d_categories += ","
        instance.d_categories = (instance.d_categories or "") + categories_str
        instance.save()

    if action == 'post_remove':
        categories_str = ",".join(instance.categories.all().exclude(id__in=pk_set).values_list('name', flat=True))
        instance.d_categories = categories_str
        instance.save()
