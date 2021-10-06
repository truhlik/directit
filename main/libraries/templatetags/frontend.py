from django import template
from django.template.defaultfilters import stringfilter
from ..utils import decode_url as utils_decode_url

register = template.Library()


@register.filter(is_safe=True)
@stringfilter
def decode_url(url: str):
    return utils_decode_url(url)
