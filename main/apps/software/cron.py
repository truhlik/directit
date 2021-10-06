from django_cron import CronJobBase, Schedule
from main.libraries.decorators import sentry_exceptions
from main.apps.notifications.email import send_expiration_notifications


class ExpirationNotification(CronJobBase):
    """
    Cron job updating files defined in static_files_dict from url.
    """
    RUN_AT_TIMES = ['3:00']

    schedule = Schedule(run_at_times=RUN_AT_TIMES)
    code = 'main.apps.software.cron'

    @sentry_exceptions
    def do(self):
        send_expiration_notifications()
