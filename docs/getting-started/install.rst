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

Add the ``SeoMixin`` to your ``Page`` model(s). In order for the new fields to
show up in the page editor, you may also want to override the promote panels.

.. code-block:: python

    # models.py
    from wagtailseo.models import SeoMixin


    class MyPage(SeoMixin, Page):
        ...

        promote_panels = SeoMixin.seo_panels

Wagtail SEO also supports special types for article-style pages (news, blog
posts, etc.), and controls for Twitter card previews. Article-style pages should
be indicated as such:

.. code-block:: python

    # models.py
    from wagtailseo.models import SeoMixin, SeoType, TwitterCard

    class ArticlePage(SeoMixin, Page):
        ...

        # Indicate this is article-style content.
        seo_content_type = SeoType.ARTICLE

        # Change the Twitter card style.
        seo_twitter_card = TwitterCard.LARGE

        promote_panels = SeoMixin.seo_panels

The ``SeoMixin`` adds many new fields to the page. So now make and apply a
migration:

.. code-block:: console

    $ python manage.py makemigrations
    $ python manage.py migrate

Finally, in your HTML template, add the metadata to the ``head`` tag and
structured data at the bottom of the ``body`` tag. The metadata template includes
*everything* such as title, canonical URL, Open Graph tags, various meta tags,
and a link to an AMP version of the page (if applicable).

.. code-block:: html

    <head>
      {% include "wagtailseo/meta.html" %}
    </head>

    <body>
      ...
      {% include "wagtailseo/struct_data.html" %}
    </body>

All done. Your page will now render with just about every form of metadata a
search engine or social media site could ask for!

Next we will look at :doc:`editing SEO metadata →<edit-meta>`
