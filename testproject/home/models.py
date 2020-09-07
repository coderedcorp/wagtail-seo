from wagtail.core.models import Page
from wagtailseo.models import OpenGraphType, SeoMixin


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


class ArticlePage(SeoMixin, Page):
    """
    Display as Open Graph article type, AMP content.
    """

    template = "home/page.html"

    seo_og_type = OpenGraphType.ARTICLE.value

    promote_panels = SeoMixin.seo_panels
