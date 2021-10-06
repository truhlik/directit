from django_cron import CronJobBase, Schedule
from main.libraries.decorators import sentry_exceptions
from main.apps.notifications.email import send_callback_notifications


class CallBackNotification(CronJobBase):
    """
    Cron job updating files defined in static_files_dict from url.
    """
    RUN_EVERY_MIN = 30

    schedule = Schedule(run_every_mins=RUN_EVERY_MIN)
    code = 'main.apps.callbacks.cron'

    @sentry_exceptions
    def do(self):
        send_callback_notifications()
