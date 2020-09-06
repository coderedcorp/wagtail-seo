from decimal import Decimal

from django.contrib.contenttypes.models import ContentType
from django.test import TestCase, override_settings
from django.urls import reverse
from django.utils.text import capfirst
from django.contrib.auth.models import User
from wagtail.images.tests.utils import Image, get_test_image_file
from wagtail.tests.utils import WagtailTestUtils
from wagtailseo import schema
from wagtailseo.blocks import MultiSelectBlock
from wagtailseo.models import SeoSettings

from home.models import SeoPage, WagtailPage


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
            is_superuser=True,
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
            # struct_org_hours=object,
            # struct_org_actions=object,
            struct_org_extra_json=r'{"json": true, "array": ["thing1", "thing2"]}',
            content_type=cls.get_content_type("seopage"),
        )

        # Add to home page.
        cls.page_wagtail = WagtailPage.objects.get(slug="home")
        cls.page_wagtail.add_child(instance=cls.page_lowseo)
        cls.page_wagtail.add_child(instance=cls.page_fullseo)

        # Turn on all SEO settings.
        seo_set: SeoSettings = SeoSettings.for_site(cls.page_wagtail.get_site())
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

    # ---- TEST PAGES ----------------------------------------------------------

    def test_wagtail_page(self):
        """
        The normal Wagtail Page should not break when rendered with the
        wagtailseo meta html include.
        """
        response = self.client.get(self.page_wagtail.get_url())
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
            self.assertHTMLEqual(
                response.content.decode("utf8"),
                f"""
                <html>
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
                <meta name="twitter:card" content="{ page.seo_twitter_card }" />
                <meta name="twitter:title" content="{ page.seo_pagetitle }">
                <meta name="twitter:image" content="{ page.seo_image_url }">
                <meta name="twitter:site" content="{ seo_set.at_twitter_site }" />
                <link rel="amphtml" href="{ page.seo_amp_url }">
                </head>
                <body></body>
                </html>
                """,
            )

    # ---- ALTERNATE SETTINGS --------------------------------------------------

    @override_settings(WAGTAILSEO_SEP="|")
    def test_custom_sep(self):
        pass
        # response = self.client.get(self.page_lowseo.get_url())
        # self.assertIsNotNone(response.get(self.header_name, None))


class TestSettingMenu(WagtailTestUtils, TestCase):
    def test_menu_item_in_admin(self):
        self.login()
        response = self.client.get(reverse("wagtailadmin_home"))
        self.assertContains(response, capfirst(SeoSettings._meta.verbose_name))
        self.assertContains(
            response,
            reverse("wagtailsettings:edit", args=("wagtailseo", "seosettings")),
        )


class TestMultiSelectBlock(WagtailTestUtils, TestCase):
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
