from datetime import datetime

from django.db import models
from django.urls import reverse
from wagtail.models import Page, Site

from wagtailseo.models import SeoMixin, SeoMixinBase, SeoType, TwitterCard


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


class BadWolf(SeoMixinBase, models.Model):
    pass


class MySnippet(SeoMixinBase, models.Model):
    template = "home/page.html"

    seo_content_type = SeoType.ARTICLE
    seo_twitter_card = TwitterCard.LARGE

    promote_panels = SeoMixinBase.seo_panels

    def __str__(self):
        return f"my snippet {self.pk or 0}"

    def get_full_url(self) -> str:
        path = reverse("my_snippet_detail", kwargs={"pk": self.pk})
        return f"{self.get_site().root_url}/{path}"

    @property
    def seo_author(self) -> str:
        return "Tux"

    @property
    def seo_published_at(self) -> datetime:
        return datetime(1122, 1, 1)

    @property
    def seo_modified_at(self) -> datetime:
        return datetime(1204, 3, 31)

    def get_site(self):
        return Site.objects.first()
