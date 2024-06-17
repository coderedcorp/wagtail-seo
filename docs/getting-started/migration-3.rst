Migrating to version 3.0 of Wagtail SEO
===========================================

If you are in a version < 3 and would like to upgrade, you will need
to take care of some change to the underlying data models.

In version 3, you will need to change the base class of every page that
could have been filled with organization structured data (typically only
the root pages); make them inheriting from ``SeoOrgMixin`` instead of ``SeoMixin``.

Switch from:

.. code-block:: python

  # models.py
  class HomePage(SeoMixin):
    pass

to:

.. code-block:: python

  # models.py
  class HomePage(SeoOrgMixin):
    pass


.. note::
    After updating, run ``makemigrations`` and check that there no db change for any
    of your page models that could contains org data.
