from wagtail.core.models import Page
from wagtailseo.models import SeoMixin


class WagtailPage(Page):
    """
    A normal Wagtail page without the SEO mixin.
    """

    template = "home/page.html"


class SeoPage(SeoMixin, Page):
    """
    Represents a normal use-case.
    """

    template = "home/page.html"

    # To override the contents of the promote tab.
    promote_panels = SeoMixin.seo_panels

    # To override the tabs themselves.
    # @cached_classmethod
    # def get_edit_handler(cls):
    #     panels = [
    #         ObjectList(cls.content_panels heading=_('Content')),
    #         ObjectList(cls.promote_panels, heading=_('SEO'), classname="seo"),
    #         ObjectList(cls.settings_panels, heading=_('Settings'), classname="settings"),
    #     ]
    #     return TabbedInterface(panels).bind_to(model=cls)
