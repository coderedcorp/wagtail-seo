"""
Use a shiny fontawesome icon if available.
"""
from django.apps import apps


if apps.is_installed("wagtailfontawesome"):
    SEO_ICON = "fa-line-chart"
else:
    SEO_ICON = "cog"
