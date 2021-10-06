from django.apps import AppConfig


class MessagesConfig(AppConfig):
    name = 'main.apps.messages'
    label = 'custom_messages'

    def ready(self):
        import main.apps.messages.signals  # noqa