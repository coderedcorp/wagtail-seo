from django import template
from django.utils.html import mark_safe
from wagtail.core.rich_text import RichText
from wagtail.core.templatetags.wagtailcore_tags import richtext

from wagtailseo import amp


register = template.Library()


@register.filter
def convert_to_amp(value):
    """
    Converts HTML to AMP.
    """
    if isinstance(value, RichText):
        value = richtext(value.source)
    return mark_safe(amp.convert_to_amp(value))
