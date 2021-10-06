from django.db import models


class CategoryQuerySet(models.QuerySet):

    def full_text_search(self, term):
        """ Vrátí všechny company, které odpovídají danému query. """
        return self.filter(name__unaccent__icontains=term)

    def main_category_with_prefetch_subcategories_and_projects(self):
        from main.apps.categories.models import Category
        return self.filter(parent__isnull=True).prefetch_related(
            models.Prefetch('children', queryset=Category.objects.all().annotate(
                products_count=models.Count('products')
            ))
        )
