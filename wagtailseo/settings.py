"""
Provide default Django settings.
"""

from django.conf import settings


# Title sitename separator. Default is em-dash.
DEFAULTS = {"WAGTAILSEO_SEP": "—"}


def get(name: str):
    return getattr(settings, name, DEFAULTS[name])
