Release Notes
=============

3.0.0
-----

**This release contains breaking changes!**

* Move Organization fields from individual pages (``SeoMixin``) to Site settings (``SeoSettings``).

* Organization fields (``struct_org_*``) and metadata fields (e.g. ``og_image``) have been split out into mixins: ``SeoOrgFields`` and ``SeoMetaFields``. This enables more customized use on models, snippets, pages, settings, etc.

See :doc:`/getting-started/migration-3`.

2.5.0
-----

* Add support for Wagtail 6.

2.4.1
-----

* Fix bug with slug generation in Wagtail 5.


2.4.0
-----

* Support Wagtail 5.


2.3.0
-----

* Support Wagtail 4.


2.2.0
-----

* Fix Wagtail and Django deprecation warnings.

* Specify ``use_json_field=True`` in StreamFields. This will require making a
  migration in your project:

  .. code-block:: text

     python manage.py makemigrations
     python manage.py migrate


2.1.0
-----

* Add Twitter card description meta tag.

* Fix warnings related to Wagtail 3 import paths and edit handlers.


2.0.1
-----

* Only render SEO meta tags if a page object is present in the template context.

* Check for empty site when getting site name.

* Support serializing ``datetime.date`` objects in structured data.


2.0.0
-----

* There are no functional changes in this release.

* Includes new SVG icon in settings panel. Previously this icon was either the
  cog, or the line chart if ``wagtailfontawesome`` was installed.

* Supports Wagtail 3 and only Wagtail 3. Wagtail 2 support will be maintained in
  the 1.x series as needed.


1.0.2
-----

* Fix broken 1.0.1 wheel caused by build cache issue.


1.0.1
-----

* Only render SEO meta tags if a page object is present in the template context.

* Check for empty site when getting site name.

* Support serializing ``datetime.date`` objects in structured data.


1.0.0
-----

* Set ``default_auto_field`` in ``wagtailseo`` app.

* Designate 1.0.0 version as stable.


0.0.4
-----

* Fix for longitude and latitude with longer digits. Now allowing longitude
  with 3 digits before the decimal point (e.g. +/- 100.12345).

* Replace ``wagtailseo.blocks.MultiSelectBlock`` with Wagtail's built-in
  ``wagtail.core.blocks.MultipleChoiceBlock``.

  .. note::

     You may need to make a corresponding find/replace update in your old
     migrations in order for them to continue working.

* Requires Wagtail>=2.9

* Remove settings and references to AMP pages.

* You may need to make migrations in your project after updating

  .. code-block:: shell

    python manage.py makemigrations
    python manage.py migrate


0.0.3
-----

* Added ``canonical_url`` field to ``SeoMixin``. Uses this as the page's
  canonical URL if it is non-blank, otherwise uses the page's normal URL.

* Fix image URLs when media is hosted on external CDN.

* Return blank author if page owner is null/None.

* Documentation and minor code cleanup.
