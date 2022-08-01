import json

from django import forms
from django.utils.translation import gettext_lazy as _
from wagtail import blocks

from wagtailseo import schema


class OpenHoursValue(blocks.StructValue):
    """
    Renders OpenHours in Structured Data format.
    """

    @property
    def struct_dict(self) -> dict:
        """
        Returns a dictionary in structured data format.
        """
        return {
            "@type": "OpeningHoursSpecification",
            "dayOfWeek": self["days"],
            "opens": self["start_time"],  # |date:'H:i'
            "closes": self["end_time"],  # |date:'H:i'
        }


class OpenHoursBlock(blocks.StructBlock):
    """
    Holds day and time combination for business open hours.
    """

    class Meta:
        label = _("Open Hours")
        value_class = OpenHoursValue

    days = blocks.MultipleChoiceBlock(
        required=True,
        verbose_name=_("Days"),
        help_text=_(
            "For late night hours past 23:59, define each day in a separate block."
        ),
        widget=forms.CheckboxSelectMultiple,
        choices=[
            ("Monday", _("Monday")),
            ("Tuesday", _("Tuesday")),
            ("Wednesday", _("Wednesday")),
            ("Thursday", _("Thursday")),
            ("Friday", _("Friday")),
            ("Saturday", _("Saturday")),
            ("Sunday", _("Sunday")),
        ],
    )
    start_time = blocks.TimeBlock(
        verbose_name=_("Opening time"),
    )
    end_time = blocks.TimeBlock(
        verbose_name=_("Closing time"),
    )


class StructuredDataActionValue(blocks.StructValue):
    """
    Renders Action in Structured Data format.
    """

    @property
    def struct_dict(self) -> dict:
        sd_dict = {
            "@type": self["action_type"],
            "target": {
                "@type": "EntryPoint",
                "urlTemplate": self["target"],
                "inLanguage": self["language"],
                "actionPlatform": [
                    "http://schema.org/DesktopWebPlatform",
                    "http://schema.org/IOSPlatform",
                    "http://schema.org/AndroidPlatform",
                ],
            },
        }
        if self["result_type"]:
            sd_dict.update(
                {
                    "result": {
                        "@type": self["result_type"],
                        "name": self["result_name"],
                    }
                }
            )
        if self["extra_json"]:
            sd_dict.update(
                json.loads(self["extra_json"]),
            )
        return sd_dict


class StructuredDataActionBlock(blocks.StructBlock):
    """
    Action object from schema.org
    """

    class Meta:
        label = _("Action")
        value_class = StructuredDataActionValue

    action_type = blocks.ChoiceBlock(
        verbose_name=_("Action Type"),
        required=True,
        choices=schema.SCHEMA_ACTION_CHOICES,
    )
    target = blocks.URLBlock(
        verbose_name=_("Target URL"),
    )
    language = blocks.CharBlock(
        verbose_name=_("Language"),
        help_text=_(
            "If the action is offered in multiple languages, create separate "
            "actions for each language."
        ),
        default="en-US",
    )
    result_type = blocks.ChoiceBlock(
        required=False,
        verbose_name=_("Result Type"),
        help_text=_("Leave blank for OrderAction"),
        choices=schema.SCHEMA_RESULT_CHOICES,
    )
    result_name = blocks.CharBlock(
        required=False,
        verbose_name=_("Result Name"),
        help_text=_('Example: "Reserve a table", "Book an appointment", etc.'),
    )
    extra_json = blocks.RawHTMLBlock(
        required=False,
        verbose_name=_("Additional action markup"),
        classname="monospace",
        help_text=_(
            "Additional JSON-LD inserted into the Action dictionary. "
            "Must be properties of https://schema.org/Action."
        ),
    )
