import urllib

from django.conf import settings
from django.template.loader import render_to_string
from django.urls import reverse
from django.utils.translation import activate

from .functions import get_absolute_url
from .tasks import send_email


class EmailBase:
    subject = None
    template_name = None

    def __init__(self, *args, **kwargs):
        pass

    def get_context(self):
        return {
            'title': self.get_subject(),
            'site_url': get_absolute_url(),
        }

    def get_subject(self):
        return self.subject

    def get_html_content(self, context):
        return render_to_string(self.template_name, context)

    def send_html_email(self, email_to, context=None, attachments=None, fail_silently=False):
        """
        Send marketing emails to user based on given email_type.
        :param email_to: email of the reciever
        :param context: dict, context to use in email template
        :param attachments: EmailAttachment object or list of them,
        :param fail_silently: Boolean defining if error should be raised in case of fail
        :return: Boolean if sending was successful
        """

        # aktivujeme jazyk pro překlady
        activate('cs')

        # naplníme context
        if not context:
            context = {}
        context.update(self.get_context())

        # vyrenderujeme HTML
        html_content = self.get_html_content(context)

        # odešleme email
        return send_email.delay(
            subject=self.get_subject(),
            email_from=settings.DEFAULT_FROM_EMAIL,
            email_to=email_to,
            attachments=attachments,
            html_content=html_content,
            fail_silently=fail_silently
        )


class EmailCallback(EmailBase):
    subject = 'nová žádost o callback'
    template_name = 'emails/email_callback.html'

    def __init__(self, qs, *args, **kwargs):
        self.qs = qs
        super(EmailCallback, self).__init__(*args, **kwargs)

    def get_context(self):
        ctx = super(EmailCallback, self).get_context()
        ctx.update({
            'qs': self.qs,
        })
        return ctx


class EmailExpiration(EmailBase):
    subject = 'expirace licence'
    template_name = 'emails/email_software_expiration.html'

    def __init__(self, obj, *args, **kwargs):
        self.obj = obj
        super(EmailExpiration, self).__init__(*args, **kwargs)

    def get_context(self):
        ctx = super(EmailExpiration, self).get_context()
        ctx.update({
            'obj': self.obj,
            'BASE_URL': settings.BASE_URL,
        })
        return ctx


class EmailProject(EmailBase):
    subject = 'nový projekt'
    template_name = 'emails/email_project.html'

    def __init__(self, qs, *args, **kwargs):
        self.qs = qs
        super(EmailProject, self).__init__(*args, **kwargs)

    def get_context(self):
        ctx = super(EmailProject, self).get_context()
        ctx.update({
            'qs': self.qs,
        })
        return ctx


class CustomerEmailProject(EmailBase):
    subject = 'Děkujeme za zadání nového projektu'
    template_name = 'emails/email_project_customer.html'

    def __init__(self, obj, *args, **kwargs):
        self.obj = obj
        super(CustomerEmailProject, self).__init__(*args, **kwargs)

    def get_context(self):
        ctx = super(CustomerEmailProject, self).get_context()

        ctx.update({
            'project_url': get_absolute_url(urllib.parse.unquote(reverse('frontend_project_detail', args=(self.obj.id, ))))
        })
        return ctx


class EmailOrder(EmailBase):
    subject = 'nová objednávka'
    template_name = 'emails/email_order.html'

    def __init__(self, qs, *args, **kwargs):
        self.qs = qs
        super(EmailOrder, self).__init__(*args, **kwargs)

    def get_context(self):
        ctx = super(EmailOrder, self).get_context()

        ctx.update({
            'qs': self.qs,
        })
        return ctx
