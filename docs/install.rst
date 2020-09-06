Install Wagtail SEO
===================

Install from pip:

.. code-block:: console

    $ pip install wagtail-seo

Next, add to your INSTALLED_APPS in the Django settings file.
Wagtail SEO also requires the Wagtail Site Settings app and context processor.

.. code-block:: python

    # settings.py

    INSTALLED_APPS = [
        ...
        "wagtailseo",
        "wagtail.sites",
        ...
    ]

    TEMPLATES = [
        {
            ...
            "OPTIONS": {
                "context_processors": [
                    ...
                    "wagtail.contrib.settings.context_processors.settings",
                ]
            }
        }
    ]

Add the ``SeoMixin`` to your ``Page`` model. In order for the new fields to
show up in the Wagtail admin, you may also want to override the promote panel.

.. code-block:: python

    # models.py

    class MyPage(SeoMixin, Page):
        ...

        promote_panel = SeoMixin.seo_panel
