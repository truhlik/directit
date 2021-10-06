from django.conf import settings

from main.apps.callbacks.models import CallBackRequest
from main.apps.orders.models import Order
from main.apps.projects.models import Project
from main.apps.software.models import Software
from main.libraries.emails import EmailCallback, EmailExpiration, EmailProject, EmailOrder


def send_callback_notifications():
    c_qs = CallBackRequest.objects.for_notification()
    if len(c_qs) == 0:
        return

    email_cls = EmailCallback(c_qs)
    sent = email_cls.send_html_email(settings.DEFAULT_NOTIFICATION_EMAIL, fail_silently=True)

    if sent:
        c_qs.mark_as_notified()


def send_expiration_notifications():
    s_qs = Software.objects.for_notification()
    if len(s_qs) == 0:
        return

    for soft in s_qs:
        email_cls = EmailExpiration(soft)
        sent = email_cls.send_html_email(settings.DEFAULT_NOTIFICATION_EMAIL, fail_silently=False)

        if sent:
            soft.mark_as_notified()
            soft.save()


def send_project_notifications():
    p_qs = Project.objects.for_notification()
    if len(p_qs) == 0:
        return

    email_cls = EmailProject(p_qs)
    sent = email_cls.send_html_email(settings.DEFAULT_NOTIFICATION_EMAIL, fail_silently=True)

    if sent:
        p_qs.mark_as_notified()


def send_order_notifications():
    o_qs = Order.objects.for_notification()
    if len(o_qs) == 0:
        return

    email_cls = EmailOrder(o_qs)
    sent = email_cls.send_html_email(settings.DEFAULT_NOTIFICATION_EMAIL, fail_silently=True)

    if sent:
        o_qs.mark_as_notified()
