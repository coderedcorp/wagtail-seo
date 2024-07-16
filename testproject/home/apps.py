from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class HomeAppConfig(AppConfig):
    name = "home"
    label = "home"
    verbose_name = _("home")
    default_auto_field = "django.db.models.AutoField"
