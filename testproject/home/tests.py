import json
from decimal import Decimal

from django.contrib.contenttypes.models import ContentType
from django.test import TestCase, override_settings
from django.urls import reverse
from django.utils import timezone
from django.utils.text import capfirst
from django.contrib.auth.models import User
from wagtail.core.models import Page
from wagtail.images.tests.utils import Image, get_test_image_file
from wagtail.tests.utils import WagtailTestUtils
from wagtailseo import schema
from wagtailseo import utils
from wagtailseo.blocks import MultiSelectBlock
from wagtailseo.models import SeoSettings

from home.models import ArticlePage, SeoPage, WagtailPage


class SeoTest(TestCase):
    @classmethod
    def get_content_type(cls, modelname: str):
        ctype, _ = ContentType.objects.get_or_create(model=modelname, app_label="home")
        return ctype

    @classmethod
    def setUpClass(cls):

        # Create an admin user.
        cls.user = User.objects.create(
            username="admin",
            first_name="Philadelphia",
            last_name="Collins",
            is_superuser=True,
        )

        # Stock Wagtail page.
        cls.page_wagtail = WagtailPage(
            title="Wagtail Page",
            slug="wagtail",
            content_type=cls.get_content_type("wagtailpage"),
        )

        # Create a page with no special SEO attributes set.
        cls.page_lowseo = SeoPage(
            title="Low Seo Page",
            slug="lowseo",
            content_type=cls.get_content_type("seopage"),
        )

        # Create a page with all SEO attributes set.
        cls.page_fullseo = SeoPage(
            title="Full Seo Page",
            slug="fullseo",
            seo_title="Custom Title",
            search_description="Custom Description",
            breadcrumbs_are_active=True,
            og_image=Image.objects.create(
                title="OG Image",
                file=get_test_image_file(),
            ),
            struct_org_type=schema.SCHEMA_ORG_CHOICES[1][0],
            struct_org_name="Custom Org Name",
            struct_org_logo=Image.objects.create(
                title="Struct Org Logo",
                file=get_test_image_file(),
            ),
            struct_org_image=Image.objects.create(
                title="Struct Org Image",
                file=get_test_image_file(),
            ),
            struct_org_phone="+1-555-867-5309",
            struct_org_address_street="55 Public Square, Suite 1710",
            struct_org_address_locality="Cleveland",
            struct_org_address_region="OH",
            struct_org_address_postal="44113",
            struct_org_address_country="US",
            struct_org_geo_lat=Decimal("1.1"),
            struct_org_geo_lng=Decimal("2.2"),
            struct_org_hours=r'[{"type": "hours", "value": {"days": ["Monday", "Tuesday", "Wednesday"], "start_time": "09:00:00", "end_time": "17:00:00"}, "id": "d6ff4389-5c26-4b78-87cc-5e108bcb692d"}]',  # noqa
            struct_org_actions=r'[{"type": "actions", "value": {"action_type": "OrderAction", "target": "https://www.example.com/", "language": "en-US", "result_type": "FoodEstablishmentReservation", "result_name": "Custom Result", "extra_json": ""}, "id": "4ef5ddc2-a25f-4263-8516-8262340e9a7f"}]',  # noqa
            struct_org_extra_json=r'{"json": true, "array": ["thing1", "thing2"]}',
            content_type=cls.get_content_type("seopage"),
        )

        # Create an article page.
        cls.page_article = ArticlePage(
            title="Article Page",
            slug="article",
            owner=cls.user,
            first_published_at=timezone.now(),
            last_published_at=timezone.now(),
            seo_title="Custom Article Title",
            search_description="Custom Article Description",
            og_image=Image.objects.create(
                title="Article OG Image",
                file=get_test_image_file(),
            ),
            content_type=cls.get_content_type("articlepage"),
        )

        # Add to home page.
        cls.page_home = Page.objects.get(slug="home")
        cls.page_home.add_child(instance=cls.page_wagtail)
        cls.page_home.add_child(instance=cls.page_lowseo)
        cls.page_home.add_child(instance=cls.page_fullseo)
        cls.page_home.add_child(instance=cls.page_article)

        # Set site name
        site = cls.page_home.get_site()
        site.site_name = "creedthoughts"
        site.save()

        # Turn on all SEO settings.
        seo_set: SeoSettings = SeoSettings.for_site(cls.page_home.get_site())
        seo_set.amp_pages = True
        seo_set.og_meta = True
        seo_set.twitter_meta = True
        seo_set.struct_meta = True
        seo_set.twitter_site = "@coderedcorp"
        seo_set.save()

    @classmethod
    def tearDownClass(cls):
        # Delete pages.
        cls.page_lowseo.delete()
        cls.page_fullseo.delete()
        # Delete user.
        cls.user.delete()

    def test_wagtail_page(self):
        """
        The normal Wagtail Page should not break when rendered with the
        wagtailseo HTML templates.
        """
        response = self.client.get(self.page_home.get_url())
        self.assertEqual(response.status_code, 200)

    def test_meta(self):
        """
        A page with SeoMixin should render with the correct meta attributes.
        """
        for page in [self.page_lowseo, self.page_fullseo]:
            seo_set = SeoSettings.for_site(page.get_site())
            response = self.client.get(page.get_url())
            self.assertEqual(response.status_code, 200)
            self.maxDiff = None
            print(response.content.decode("utf8"))
            self.assertInHTML(
                f"""
                <head>
                <title>{ page.seo_pagetitle }</title>
                <link rel="canonical" href="{ page.seo_canonical_url }">
                <meta name="description" content="{ page.seo_description }" />
                <meta property="og:title" content="{ page.seo_pagetitle }" />
                <meta property="og:description" content="{ page.seo_description }" />
                <meta property="og:image" content="{ page.seo_image_url }" />
                <meta property="og:site_name" content="{ page.seo_sitename }" />
                <meta property="og:url" content="{ page.seo_canonical_url }" />
                <meta property="og:type" content="{ page.seo_og_type }" />
                <meta name="twitter:card" content="{ page.seo_twitter_card_content }" />
                <meta name="twitter:title" content="{ page.seo_pagetitle }">
                <meta name="twitter:image" content="{ page.seo_image_url }">
                <meta name="twitter:site" content="{ seo_set.at_twitter_site }" />
                <link rel="amphtml" href="{ page.seo_amp_url }">
                </head>
                """,
                response.content.decode("utf8"),
            )

    def test_meta_article(self):
        """
        A page with SeoMixin set to article type should render correct meta.
        """
        page = self.page_article
        seo_set = SeoSettings.for_site(page.get_site())
        response = self.client.get(page.get_url())
        self.assertEqual(response.status_code, 200)
        self.maxDiff = None
        print(response.content.decode("utf8"))
        self.assertInHTML(
            f"""
            <head>
            <title>{ page.seo_pagetitle }</title>
            <link rel="canonical" href="{ page.seo_canonical_url }">
            <meta name="description" content="{ page.seo_description }" />
            <meta name="author" content="{ page.seo_author }" />
            <meta property="og:title" content="{ page.seo_pagetitle }" />
            <meta property="og:description" content="{ page.seo_description }" />
            <meta property="og:image" content="{ page.seo_image_url }" />
            <meta property="og:site_name" content="{ page.seo_sitename }" />
            <meta property="og:url" content="{ page.seo_canonical_url }" />
            <meta property="og:type" content="{ page.seo_og_type }" />
            <meta property="article:author" content="{ page.seo_author }" />
            <meta property="article:published_time" content="{ utils.serialize_date(page.seo_published_at) }" />
            <meta property="article:modified_time" content="{ utils.serialize_date(page.last_published_at) }" />
            <meta name="twitter:card" content="{ page.seo_twitter_card_content }" />
            <meta name="twitter:title" content="{ page.seo_pagetitle }">
            <meta name="twitter:image" content="{ page.seo_image_url }">
            <meta name="twitter:site" content="{ seo_set.at_twitter_site }" />
            <link rel="amphtml" href="{ page.seo_amp_url }">
            </head>
            """,  # noqa
            response.content.decode("utf8"),
        )

    def test_struct_org(self):
        """
        A page with SeoMixin should render correct structured data.
        """
        page = self.page_fullseo

        # Manually render the JSON and match against page HTML.
        # Get images to compare against rendered content.
        base_url = utils.get_absolute_media_url(page.get_site())
        img1x1 = base_url + page.struct_org_image.get_rendition("fill-10000x10000").url
        img4x3 = base_url + page.struct_org_image.get_rendition("fill-40000x30000").url
        img16x9 = base_url + page.struct_org_image.get_rendition("fill-16000x9000").url
        org_hours = []
        for spec in page.struct_org_hours:
            org_hours.append(spec.value.struct_dict)
        potential_action = []
        for action in page.struct_org_actions:
            potential_action.append(action.value.struct_dict)

        expected_dict = {
            "@context": "http://schema.org",
            "@graph": [
                {
                    "@type": page.struct_org_type,
                    "url": page.seo_canonical_url,
                    "name": page.seo_struct_org_name,
                    "logo": {
                        "@type": "ImageObject",
                        "url": page.seo_logo_url,
                    },
                    "image": [img1x1, img4x3, img16x9],
                    "telephone": page.struct_org_phone,
                    "address": {
                        "@type": "PostalAddress",
                        "streetAddress": page.struct_org_address_street,
                        "addressLocality": page.struct_org_address_locality,
                        "addressRegion": page.struct_org_address_region,
                        "postalCode": page.struct_org_address_postal,
                        "addressCountry": page.struct_org_address_country,
                    },
                    "geo": {
                        "@type": "GeoCoordinates",
                        "latitude": "1.10000000",
                        "longitude": "2.20000000",
                    },
                    "openingHoursSpecification": org_hours,
                    "potentialAction": potential_action,
                },
                {
                    "@type": "BreadcrumbList",
                    "@id": "http://localhost/fullseo/#breadcrumb",
                    "itemListElement": [
                        {
                            "@type": "ListItem",
                            "position": 1,
                            "item": {
                                "@type": "WebPage",
                                "@id": "http://localhost/",
                                "url": "http://localhost/",
                                "name": "Welcome to your new Wagtail site!",
                            },
                        },
                        {
                            "@type": "ListItem",
                            "position": 2,
                            "item": {
                                "@type": "Type",
                                "@id": "http://localhost/fullseo/",
                                "url": "http://localhost/fullseo/",
                                "name": "Full Seo Page",
                            },
                        },
                    ],
                },
                json.loads(page.struct_org_extra_json),
            ],
        }

        expected_json = json.dumps(expected_dict, cls=utils.StructDataEncoder)

        # GET the page and check its JSON against expected JSON.
        response = self.client.get(page.get_url())
        self.assertEqual(response.status_code, 200)
        self.maxDiff = None
        print(response.content.decode("utf8"))
        self.assertInHTML(
            f"""
            <script type="application/ld+json">
            { expected_json }
            </script>
            """,  # noqa
            response.content.decode("utf8"),
        )

    def test_struct_article(self):
        """
        A page with SeoMixin set to article type should render correct
        structured data.
        """
        page = self.page_article

        # Manually render the JSON and match against page HTML.
        # Get images to compare against rendered content.
        base_url = utils.get_absolute_media_url(page.get_site())
        img1x1 = base_url + page.seo_image.get_rendition("fill-10000x10000").url
        img4x3 = base_url + page.seo_image.get_rendition("fill-40000x30000").url
        img16x9 = base_url + page.seo_image.get_rendition("fill-16000x9000").url
        expected_dict = {
            "@context": "http://schema.org",
            "@type": "Article",
            "mainEntityOfPage": {
                "@type": "WebPage",
                "@id": page.seo_canonical_url,
            },
            "headline": page.title,
            "description": page.seo_description,
            "datePublished": page.seo_published_at,
            "dateModified": page.last_published_at,
            "author": {
                "@type": "Person",
                "name": page.seo_author,
            },
            "image": [img1x1, img4x3, img16x9],
        }
        expected_json = json.dumps(expected_dict, cls=utils.StructDataEncoder)

        # GET the page and check its JSON against expected JSON.
        response = self.client.get(page.get_url())
        self.assertEqual(response.status_code, 200)
        self.maxDiff = None
        print(response.content.decode("utf8"))
        self.assertInHTML(
            f"""
            <script type="application/ld+json">
            { expected_json }
            </script>
            """,  # noqa
            response.content.decode("utf8"),
        )

    @override_settings(WAGTAILSEO_SEP="|")
    def test_custom_sep(self):
        page = self.page_lowseo
        response = self.client.get(page.get_url())
        print(response.content.decode("utf8"))
        self.assertInHTML(
            f"<title>{page.title} | {page.seo_sitename}</title>",
            response.content.decode("utf8"),
        )


class TestSettingMenu(WagtailTestUtils, TestCase):
    """
    Test that the SeoSettings show up in the Wagtail Admin.
    """

    def test_menu_item_in_admin(self):
        self.login()
        response = self.client.get(reverse("wagtailadmin_home"))
        self.assertContains(response, capfirst(SeoSettings._meta.verbose_name))
        self.assertContains(
            response,
            reverse("wagtailsettings:edit", args=("wagtailseo", "seosettings")),
        )


class TestMultiSelectBlock(TestCase):
    def test_render_single_choice(self):
        block = MultiSelectBlock(
            choices=[("tea", "Tea"), ("coffee", "Coffee"), ("water", "Water")]
        )
        html = block.render_form(["tea"])
        self.assertInHTML('<option value="tea" selected>Tea</option>', html)
        self.assertTrue(html.count("selected"), 1)

    def test_render_multi_choice(self):
        block = MultiSelectBlock(
            choices=[("tea", "Tea"), ("coffee", "Coffee"), ("water", "Water")]
        )
        html = block.render_form(["coffee", "tea"])
        self.assertInHTML('<option value="tea" selected>Tea</option>', html)
        self.assertInHTML('<option value="coffee" selected>Coffee</option>', html)
        self.assertTrue(html.count("selected"), 2)
