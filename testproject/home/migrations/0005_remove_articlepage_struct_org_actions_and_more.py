# Generated by Django 5.0.6 on 2024-06-14 09:24

from django.db import migrations

STRUCT_ORG_FIELDS = [
    "struct_org_type",
    "struct_org_name",
    "struct_org_logo_id",
    "struct_org_image_id",
    "struct_org_phone",
    "struct_org_address_street",
    "struct_org_address_locality",
    "struct_org_address_region",
    "struct_org_address_postal",
    "struct_org_address_country",
    "struct_org_geo_lat",
    "struct_org_geo_lng",
    "struct_org_hours",
    "struct_org_actions",
    "struct_org_extra_json", ]
# put here every model names of yours that could have been filled with structured seo data;
# order will matter when searching for pages data
SEO_MODELS = ["SeoPage", "ArticlePage"]


def fill_settings_from_pages_struct_org(apps, schema_editor):
    """
    Search for pages where seo struct info was filled and use that to
    fill new settings struct data
    """

    SeoSettings = apps.get_model("wagtailseo", "SeoSettings")
    Site = apps.get_model("wagtailcore", "Site")

    for site in Site.objects.all().select_related("root_page"):
        for model_name in SEO_MODELS:
            model = apps.get_model("home", model_name)
            page = model.objects.filter(
                path__startswith=site.root_page.path,
                depth__gte=site.root_page.depth
            ).order_by(
                'path'
            ).exclude(struct_org_name__exact="").first()
            # if you are sure that only root pages were used to fill structured data,
            # you can directly use:
            # page = site.root_page.specific if site.root_page.specific._meta.model_name in SEO_MODELS else None
            if page is not None:
                seo_settings, _ = SeoSettings.objects.get_or_create(site=site)
                for field in STRUCT_ORG_FIELDS:
                    setattr(seo_settings, field, getattr(page, field))
                seo_settings.save()
                break


def fill_pages_from_settings_struct_org(apps, schema_editor):
    """
    For every site, find the most top-level page inheriting from SeoMixin
    and fill its struct information using the site's settings
    """
    SeoSettings = apps.get_model("wagtailseo", "SeoSettings")
    for seo_settings in SeoSettings.objects.all().select_related("site", "site__root_page"):
        for model_name in SEO_MODELS:
            model = apps.get_model("home", model_name)
            page = model.objects.filter(
                path__startswith=seo_settings.site.root_page.path,
                depth__gte=seo_settings.site.root_page.depth
            ).order_by('path').first()
            if page is not None:
                for field in STRUCT_ORG_FIELDS:
                    setattr(page, field, getattr(seo_settings, field))
                page.save()
                break


class Migration(migrations.Migration):
    dependencies = [
        ("home", "0004_alter_articlepage_struct_org_logo_and_more"),
        ("wagtailseo", "0003_seosettings_struct_org_fields"),
    ]

    operations = [
        migrations.RunPython(
            fill_settings_from_pages_struct_org, fill_pages_from_settings_struct_org
        ),
        migrations.RemoveField(
            model_name="articlepage",
            name="struct_org_actions",
        ),
        migrations.RemoveField(
            model_name="articlepage",
            name="struct_org_address_country",
        ),
        migrations.RemoveField(
            model_name="articlepage",
            name="struct_org_address_locality",
        ),
        migrations.RemoveField(
            model_name="articlepage",
            name="struct_org_address_postal",
        ),
        migrations.RemoveField(
            model_name="articlepage",
            name="struct_org_address_region",
        ),
        migrations.RemoveField(
            model_name="articlepage",
            name="struct_org_address_street",
        ),
        migrations.RemoveField(
            model_name="articlepage",
            name="struct_org_extra_json",
        ),
        migrations.RemoveField(
            model_name="articlepage",
            name="struct_org_geo_lat",
        ),
        migrations.RemoveField(
            model_name="articlepage",
            name="struct_org_geo_lng",
        ),
        migrations.RemoveField(
            model_name="articlepage",
            name="struct_org_hours",
        ),
        migrations.RemoveField(
            model_name="articlepage",
            name="struct_org_image",
        ),
        migrations.RemoveField(
            model_name="articlepage",
            name="struct_org_logo",
        ),
        migrations.RemoveField(
            model_name="articlepage",
            name="struct_org_name",
        ),
        migrations.RemoveField(
            model_name="articlepage",
            name="struct_org_phone",
        ),
        migrations.RemoveField(
            model_name="articlepage",
            name="struct_org_type",
        ),
        migrations.RemoveField(
            model_name="seopage",
            name="struct_org_actions",
        ),
        migrations.RemoveField(
            model_name="seopage",
            name="struct_org_address_country",
        ),
        migrations.RemoveField(
            model_name="seopage",
            name="struct_org_address_locality",
        ),
        migrations.RemoveField(
            model_name="seopage",
            name="struct_org_address_postal",
        ),
        migrations.RemoveField(
            model_name="seopage",
            name="struct_org_address_region",
        ),
        migrations.RemoveField(
            model_name="seopage",
            name="struct_org_address_street",
        ),
        migrations.RemoveField(
            model_name="seopage",
            name="struct_org_extra_json",
        ),
        migrations.RemoveField(
            model_name="seopage",
            name="struct_org_geo_lat",
        ),
        migrations.RemoveField(
            model_name="seopage",
            name="struct_org_geo_lng",
        ),
        migrations.RemoveField(
            model_name="seopage",
            name="struct_org_hours",
        ),
        migrations.RemoveField(
            model_name="seopage",
            name="struct_org_image",
        ),
        migrations.RemoveField(
            model_name="seopage",
            name="struct_org_logo",
        ),
        migrations.RemoveField(
            model_name="seopage",
            name="struct_org_name",
        ),
        migrations.RemoveField(
            model_name="seopage",
            name="struct_org_phone",
        ),
        migrations.RemoveField(
            model_name="seopage",
            name="struct_org_type",
        ),
    ]
