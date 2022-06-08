import json
from datetime import datetime
from enum import Enum
from typing import Optional

from django.db import models
from django.utils.translation import gettext_lazy as _
from wagtail.admin.edit_handlers import (
    HelpPanel,
    FieldPanel,
    MultiFieldPanel,
    StreamFieldPanel,
)
from wagtail.contrib.settings.models import BaseSetting, register_setting
from wagtail.core.fields import StreamField
from wagtail.core.models import Page
from wagtail.images import get_image_model_string
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.images.models import AbstractImage

from wagtailseo import settings, schema, utils
from wagtailseo.blocks import OpenHoursBlock, StructuredDataActionBlock


class SeoType(Enum):
    ARTICLE = "article"
    WEBSITE = "website"


class TwitterCard(Enum):
    APP = "app"
    LARGE = "summary_large_image"
    PLAYER = "player"
    SUMMARY = "summary"


class SeoMixin(Page):
    """
    Contains fields for SEO-related attributes on a Page model.
    """

    class Meta:
        abstract = True

    canonical_url = models.URLField(
        blank=True,
        max_length=255,
        verbose_name=_("Canonical URL"),
        help_text=_("Leave blank to use the page's URL."),
    )
    og_image = models.ForeignKey(
        get_image_model_string(),
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
        verbose_name=_("Preview image"),
        help_text=_("Shown when linking to this page on social media."),
    )
    struct_org_type = models.CharField(
        default="",
        blank=True,
        max_length=255,
        choices=schema.SCHEMA_ORG_CHOICES,
        verbose_name=_("Organization type"),
        help_text=_("If blank, no structured data will be used on this page."),
    )
    struct_org_name = models.CharField(
        default="",
        blank=True,
        max_length=255,
        verbose_name=_("Organization name"),
        help_text=_("Leave blank to use the site name in Settings > Sites"),
    )
    struct_org_logo = models.ForeignKey(
        get_image_model_string(),
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
        verbose_name=_("Organization logo"),
        help_text=_("Leave blank to use the logo in Settings > Layout > Logo"),
    )
    struct_org_image = models.ForeignKey(
        get_image_model_string(),
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
        verbose_name=_("Photo of Organization"),
        help_text=_(
            "A photo of the facility. This photo will be cropped to 1:1, 4:3, "
            "and 16:9 aspect ratios automatically."
        ),
    )
    struct_org_phone = models.CharField(
        blank=True,
        max_length=255,
        verbose_name=_("Telephone number"),
        help_text=_(
            "Include country code for best results. For example: +1-216-555-8000"
        ),
    )
    struct_org_address_street = models.CharField(
        blank=True,
        max_length=255,
        verbose_name=_("Street address"),
        help_text=_(
            "House number and street. For example, 55 Public Square Suite 1710"
        ),
    )
    struct_org_address_locality = models.CharField(
        blank=True,
        max_length=255,
        verbose_name=_("City"),
        help_text=_("City or locality. For example, Cleveland"),
    )
    struct_org_address_region = models.CharField(
        blank=True,
        max_length=255,
        verbose_name=_("State"),
        help_text=_("State, province, county, or region. For example, OH"),
    )
    struct_org_address_postal = models.CharField(
        blank=True,
        max_length=255,
        verbose_name=_("Postal code"),
        help_text=_("Zip or postal code. For example, 44113"),
    )
    struct_org_address_country = models.CharField(
        blank=True,
        max_length=255,
        verbose_name=_("Country"),
        help_text=_(
            "For example, USA. Two-letter ISO 3166-1 alpha-2 country code is "
            "also acceptable https://en.wikipedia.org/wiki/ISO_3166-1"
        ),
    )
    struct_org_geo_lat = models.DecimalField(
        blank=True,
        null=True,
        max_digits=11,
        decimal_places=8,
        verbose_name=_("Geographic latitude"),
    )
    struct_org_geo_lng = models.DecimalField(
        blank=True,
        null=True,
        max_digits=11,
        decimal_places=8,
        verbose_name=_("Geographic longitude"),
    )
    struct_org_hours = StreamField(
        [("hours", OpenHoursBlock())],
        blank=True,
        verbose_name=_("Hours of operation"),
    )
    struct_org_actions = StreamField(
        [("actions", StructuredDataActionBlock())],
        blank=True,
        verbose_name=_("Actions"),
    )
    struct_org_extra_json = models.TextField(
        blank=True,
        verbose_name=_("Additional Organization markup"),
        help_text=_(
            "Additional JSON-LD inserted into the Organization dictionary. "
            "Must be properties of https://schema.org/Organization or the "
            "selected organization type."
        ),
    )

    # The content type of this page, for search engines.
    seo_content_type = SeoType.WEBSITE

    # List of text attribute names on this model, in order of preference,
    # for use as the SEO description.
    seo_description_sources = [
        "search_description",  # Comes from wagtail.Page
    ]

    # List of text attribute names on tthis model, in order of
    # preference, for use as Canonial URL.
    canonical_url_sources = [
        "canonical_url",
    ]

    # List of Image object attribute names on this model, in order of
    # preference, for use as the preferred Open Graph / SEO image.
    seo_image_sources = [
        "og_image",
    ]

    # List of text attribute names on this model, in order of preference,
    # for use as the SEO title.
    seo_pagetitle_sources = [
        "seo_title",  # Comes from wagtail.Page
    ]

    # The style of Twitter card to show.
    seo_twitter_card = TwitterCard.SUMMARY

    @property
    def seo_author(self) -> str:
        """
        Gets the name of the author of this page.
        Override in your Page model as necessary.
        """
        if self.owner:
            return self.owner.get_full_name()
        return ""

    @property
    def seo_canonical_url(self) -> str:
        """
        Gets the full/absolute/canonical URL preferred for meta tags and search engines.
        Override in your Page model as necessary.
        """
        for attr in self.canonical_url_sources:
            if hasattr(self, attr):
                url = getattr(self, attr)
                if url:
                    return url
        return self.get_full_url()

    @property
    def seo_description(self) -> str:
        """
        Gets the correct search engine and Open Graph description of this page.
        Override in your Page model as necessary.
        """
        for attr in self.seo_description_sources:
            if hasattr(self, attr):
                text = getattr(self, attr)
                if text:
                    return text
        return ""

    @property
    def seo_image(self) -> Optional[AbstractImage]:
        """
        Gets the primary Open Graph image of this page.
        """
        for attr in self.seo_image_sources:
            if hasattr(self, attr):
                image = getattr(self, attr)
                if isinstance(image, AbstractImage):
                    return image
        return None

    @property
    def seo_image_url(self) -> str:
        """
        Gets the absolute URL for the primary Open Graph image of this page.
        """
        if self.seo_image:
            url = self.seo_image.get_rendition("original").url
            base_url = utils.get_absolute_media_url(self.get_site())
            return utils.ensure_absolute_url(url, base_url)
        return ""

    @property
    def seo_logo(self) -> Optional[AbstractImage]:
        """
        Gets the primary logo of the organization.
        """
        if self.struct_org_logo:
            return self.struct_org_logo
        return None

    @property
    def seo_logo_url(self) -> str:
        """
        Gets the absolute URL for the organization logo.
        """
        if self.seo_logo:
            url = self.seo_logo.get_rendition("original").url
            base_url = utils.get_absolute_media_url(self.get_site())
            return utils.ensure_absolute_url(url, base_url)
        return ""

    @property
    def seo_og_type(self) -> str:
        """
        Gets the correct Open Graph type for this page.
        Override in your Page model as necessary.
        """
        return self.seo_content_type.value

    @property
    def seo_sitename(self) -> str:
        """
        Gets the site name.
        Override in your Page model as necessary.
        """
        return self.get_site().site_name

    @property
    def seo_pagetitle(self) -> str:
        """
        Gets the correct search engine and Open Graph title of this page.
        Override in your Page model as necessary.
        """
        for attr in self.seo_pagetitle_sources:
            if hasattr(self, attr):
                text = getattr(self, attr)
                if text:
                    return text

        # Fallback to wagtail.Page.title plus site name.
        return "{0} {1} {2}".format(
            self.title, settings.get("WAGTAILSEO_SEP"), self.seo_sitename
        )

    @property
    def seo_published_at(self) -> datetime:
        """
        Gets the date this page was first published.
        Override in your Page model as necessary.
        """
        return self.first_published_at

    @property
    def seo_twitter_card_content(self) -> str:
        """
        Gets the correct style of twitter card for this page.
        Override in your Page model as necessary.
        """
        return self.seo_twitter_card.value

    @property
    def seo_struct_org_name(self) -> str:
        """
        Gets org name for sturctured data using a fallback.
        """
        if self.struct_org_name:
            return self.struct_org_name
        return self.seo_sitename

    @property
    def seo_struct_org_base_dict(self) -> dict:
        """
        Gets generic "Organization" data for use as a subset of other
        structured data types (for example, as publisher of an Article).

        See: https://developers.google.com/search/docs/data-types/article
        """

        # Base info.
        sd_dict: dict = {
            "@context": "http://schema.org",
            "@type": "Organization",
            "url": self.seo_canonical_url,
            "name": self.seo_struct_org_name,
        }

        # Logo.
        if self.seo_logo:
            sd_dict.update(
                {
                    "logo": {
                        "@type": "ImageObject",
                        "url": self.seo_logo_url,
                    },
                }
            )

        # Image.
        if self.struct_org_image:
            images = utils.get_struct_data_images(
                self.get_site(), self.struct_org_image
            )
            sd_dict.update({"image": images})

        # Telephone.
        if self.struct_org_phone:
            sd_dict.update({"telephone": self.struct_org_phone})

        # Address.
        if self.struct_org_address_street:
            sd_dict.update(
                {
                    "address": {
                        "@type": "PostalAddress",
                        "streetAddress": self.struct_org_address_street,
                        "addressLocality": self.struct_org_address_locality,
                        "addressRegion": self.struct_org_address_region,
                        "postalCode": self.struct_org_address_postal,
                        "addressCountry": self.struct_org_address_country,
                    },
                }
            )

        return sd_dict

    @property
    def seo_struct_org_base_json(self) -> str:
        return json.dumps(self.seo_struct_org_base_dict, cls=utils.StructDataEncoder)

    @property
    def seo_struct_org_dict(self) -> dict:
        """
        Gets full "Organization" structured data on top of base organization data.

        See: https://developers.google.com/search/docs/data-types/local-business
        """

        # Base info.
        sd_dict = self.seo_struct_org_base_dict

        # Override org type to use specific type.
        if self.struct_org_type:
            sd_dict.update({"@type": self.struct_org_type})

        # Geo coordinates.
        if self.struct_org_geo_lat and self.struct_org_geo_lng:
            sd_dict.update(
                {
                    "geo": {
                        "@type": "GeoCoordinates",
                        "latitude": float(self.struct_org_geo_lat),
                        "longitude": float(self.struct_org_geo_lng),
                    },
                }
            )

        # Hours of operation.
        if self.struct_org_hours:
            hours = []
            for spec in self.struct_org_hours:
                hours.append(spec.value.struct_dict)
            sd_dict.update({"openingHoursSpecification": hours})

        # Actions.
        if self.struct_org_actions:
            actions = []
            for action in self.struct_org_actions:
                actions.append(action.value.struct_dict)
            sd_dict.update({"potentialAction": actions})

        # Extra JSON.
        if self.struct_org_extra_json:
            sd_dict.update(json.loads(self.struct_org_extra_json))

        return sd_dict

    @property
    def seo_struct_org_json(self) -> str:
        return json.dumps(self.seo_struct_org_dict, cls=utils.StructDataEncoder)

    @property
    def seo_struct_publisher_dict(self) -> Optional[dict]:
        """
        Gets the base organization info from either this page, or the root page.
        """
        if self.struct_org_type:
            return self.seo_struct_org_base_dict
        else:
            root_page = self.get_site().root_page.specific
            if hasattr(root_page, "seo_struct_org_base_dict"):
                return root_page.seo_struct_org_base_dict
        return None

    @property
    def seo_struct_article_dict(self) -> dict:
        sd_dict = {
            "@context": "http://schema.org",
            "@type": "Article",
            "mainEntityOfPage": {
                "@type": "WebPage",
                "@id": self.seo_canonical_url,
            },
            "headline": self.title,
            "description": self.seo_description,
            "datePublished": self.seo_published_at,
            "dateModified": self.last_published_at,
            "author": {
                "@type": "Person",
                "name": self.seo_author,
            },
        }

        # Image, if available.
        if self.seo_image:
            sd_dict.update(
                {"image": utils.get_struct_data_images(self.get_site(), self.seo_image)}
            )

        # Publisher, if available.
        if self.seo_struct_publisher_dict:
            sd_dict.update({"publisher": self.seo_struct_publisher_dict})

        return sd_dict

    @property
    def seo_struct_article_json(self) -> str:
        return json.dumps(self.seo_struct_article_dict, cls=utils.StructDataEncoder)

    seo_meta_panels = [
        MultiFieldPanel(
            [
                FieldPanel("slug"),
                FieldPanel("seo_title"),
                FieldPanel("search_description"),
                FieldPanel("canonical_url"),
                ImageChooserPanel("og_image"),
            ],
            _("Search and Social Previews"),
        ),
    ]

    seo_menu_panels = [
        MultiFieldPanel(
            [
                FieldPanel("show_in_menus"),
            ],
            _("Navigation"),
        ),
    ]

    seo_struct_panels = [
        MultiFieldPanel(
            [
                HelpPanel(
                    heading=_("About Organization Structured Data"),
                    content=_(schema.SCHEMA_HELP),
                ),
                FieldPanel("struct_org_type"),
                FieldPanel("struct_org_name"),
                ImageChooserPanel("struct_org_logo"),
                ImageChooserPanel("struct_org_image"),
                FieldPanel("struct_org_phone"),
                FieldPanel("struct_org_address_street"),
                FieldPanel("struct_org_address_locality"),
                FieldPanel("struct_org_address_region"),
                FieldPanel("struct_org_address_postal"),
                FieldPanel("struct_org_address_country"),
                FieldPanel("struct_org_geo_lat"),
                FieldPanel("struct_org_geo_lng"),
                StreamFieldPanel("struct_org_hours"),
                StreamFieldPanel("struct_org_actions"),
                FieldPanel("struct_org_extra_json"),
            ],
            _("Structured Data - Organization"),
        ),
    ]

    seo_panels = seo_meta_panels + seo_menu_panels + seo_struct_panels


@register_setting(icon="wagtailseo-line-chart")
class SeoSettings(BaseSetting):
    """
    Toggle Search engine optimization features and meta tags.
    """

    class Meta:
        verbose_name = _("SEO")

    og_meta = models.BooleanField(
        default=True,
        verbose_name=_("Use Open Graph Markup"),
        help_text=_(
            "Show an optimized preview when linking to this site on social media. "
            "See https://ogp.me/"
        ),
    )
    twitter_meta = models.BooleanField(
        default=True,
        verbose_name=_("Use Twitter Markup"),
        help_text=_(
            "Shows content as a card when linking to this site on Twitter. "
            "See https://developer.twitter.com/en/docs/twitter-for-websites/cards"
        ),
    )
    twitter_site = models.CharField(
        max_length=16,
        blank=True,
        verbose_name=_("Twitter Account"),
        help_text=_("The @username of the website owner’s Twitter handle."),
    )
    struct_meta = models.BooleanField(
        default=True,
        verbose_name=_("Use Structured Data"),
        help_text=_(
            "Optimizes information about your organization for search engines. "
            "See https://schema.org/"
        ),
    )

    @property
    def at_twitter_site(self):
        """
        The Twitter site handle, prepended with "@".
        """
        handle = self.twitter_site.lstrip("@")
        return "@{0}".format(handle)

    panels = [
        MultiFieldPanel(
            [
                FieldPanel("og_meta"),
                FieldPanel("struct_meta"),
                FieldPanel("twitter_meta"),
                FieldPanel("twitter_site"),
            ],
            heading=_("Search Engine Optimization"),
        )
    ]
