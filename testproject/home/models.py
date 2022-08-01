from wagtail.models import Page
from wagtailseo.models import SeoMixin, SeoType, TwitterCard


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

    promote_panels = SeoMixin.seo_panels


class ArticlePage(SeoMixin, Page):
    """
    Display as article type which enables corresponding Open Graph, Structured
    Data, and AMP content.
    """

    template = "home/page.html"

    seo_content_type = SeoType.ARTICLE
    seo_twitter_card = TwitterCard.LARGE

    promote_panels = SeoMixin.seo_panels
