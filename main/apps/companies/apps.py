from django.apps import AppConfig


class CompaniesConfig(AppConfig):
    name = 'main.apps.companies'

    def ready(self):
        import main.apps.companies.signals  # noqa
