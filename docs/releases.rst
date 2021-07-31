Release Notes
=============

0.0.4
-----

*  Fix for longitude and latitude with longer digits. Now allowing longitude with 3 digits before the decimal point (e.g. +/- 100.12345)

0.0.3
-----

* Added ``canonical_url`` field to ``SeoMixin``. Uses this as the page's
  canonical URL if it is non-blank, otherwises uses the page's normal URL.

* Fix image URLs when media is hosted on external CDN.

* Return blank author if page owner is null/None.

* Documentation and minor code cleanup.
