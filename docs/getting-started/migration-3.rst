Migrating to version 3.0 of Wagtail SEO
===========================================

If you are in a version < 3 and would like to upgrade, you will need to take care of some change to the underlying data models as well as templates. In version 3, you will need to add the following line to the body of the template used by your root page:

.. code-block:: html

   <body>
     ...
     {% include "wagtailseo/struct_data.html" %}
     {% include "wagtailseo/struct_org_data.html" %}
   </body>

Also, in version 3 the structured data has moved from being fields of ``SeoMixin``
(on every page) to the SEO site settings. This means the under the default implementation, each site will have **one** organization.


Separate organization data per page
-----------------------------------

If you were previously using different Organization data on each page (not common), then you will need to re-implement this on your Page models. Most sites should skip this step, unless the site has multiple locations, branches, franchises, etc.

To do this, you'll need to add the Organization fields to your page model, and then override the getter to load from the page rather than the settings:

.. code-block:: python

   # Add ``SeoOrgFields`` before ``SeoMixin``.
   class MyPage(SeoOrgFields, SeoMixin, Page):

       ...

       # Override the getter to return the page, rather than the
       # SeoSettings, when getting the organization data.
       def seo_org_fields(self):
          return self

After doing this, there should not be any migration changes. Double check by making migrations:

.. code-block:: console

   $ python manage.py makemigrations


Migrating organization data to site settings
--------------------------------------------

If you prefer to re-enter the organization data manually, you can skip the steps below. However, we recommend creating a migration to preserve the data.

This migration should manually copy the ``struct_org_*`` fields from your Site's Root Page into the ``SeoSettings``.

For the most common case, the procedure is the following:

#. Create the new migration file(s)

   .. code-block:: console

      $ python manage.py makemigrations

#. For each created file, add the wagtailseo migration as a dependency:

   .. code-block:: python

        # new_migration.py

        class Migration(migrations.Migration):
            dependencies = [
                ...
                ("wagtailseo", "0003_seosettings_struct_org_fields"),
            ]

#. Edit your generated migration files to add a ``RunPython`` operation as your **first** operation. The code should handle populating the settings structured data using existing pages, as well as the reverse operation. Adapt depending on how you filled the structured data for your current site.

   .. code-block:: python

        # new_migration.py

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
        SEO_MODELS = [TODO]


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
            The reverse migration.

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
            ...

            operations = [
                migrations.RunPython(
                    fill_settings_from_pages_struct_org, fill_pages_from_settings_struct_org
                ),


.. note::

    Don't forget to check your migration locally before deploying to production!
