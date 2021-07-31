Release Notes
=============

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

* You may need to make migrations in your project after updating::

    python manage.py makemigrations
    python manage.py migrate


0.0.3
-----

* Added ``canonical_url`` field to ``SeoMixin``. Uses this as the page's
  canonical URL if it is non-blank, otherwise uses the page's normal URL.

* Fix image URLs when media is hosted on external CDN.

* Return blank author if page owner is null/None.

* Documentation and minor code cleanup.
