from django.utils.translation import ugettext_lazy as _

CALLBACK_TYPE_SURVEY = 'SURVEY'
CALLBACK_TYPE_REFERENCE = 'REFERENCE'
CALLBACK_TYPE_OTHER = 'OTHER'
CALLBACK_TYPE_CONSULTATION = 'CONSULTATION'
CALLBACK_TYPE_EXPERTIZE = 'EXPERTIZE'

CALLBACK_TYPE_CHOICES = (
    (CALLBACK_TYPE_SURVEY, _('průzkum trhu')),
    (CALLBACK_TYPE_REFERENCE, _('nezávislá reference')),
    (CALLBACK_TYPE_CONSULTATION, _('konzultace k vybranému projektu ')),
    (CALLBACK_TYPE_EXPERTIZE, _('expertní názor')),
    (CALLBACK_TYPE_OTHER, _('ostatní')),
)
