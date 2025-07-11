Customizing Metadata & Fallbacks
================================

Most likely, the page models on your site will have many custom fields that
you would prefer to use as fallbacks for bits of SEO metadata, such as the
image used for Open Graph. Wagtail SEO is fully customizable and "override-able"
via various properties available on the page model.

Fallback sources
----------------

Descriptions, titles, and Open Graph images pull from a list of attributes to
determine fallback order.

* ``seo_content_type`` --- Enum of ``SeoType`` indicating the content type of
  this page, for search engines.

* ``seo_description_sources`` --- List of attribute names on this model, in
  order of preference, for use as the SEO description.

* ``seo_image_sources`` --- List of Image object attribute names on this model,
  in order of preference, for use as the preferred Open Graph / SEO image.

* ``seo_pagetitle_sources`` --- List of attribute names on this model, in
  order of preference, for use as the SEO title.

* ``seo_twitter_card`` --- Enum of ``TwitterCard`` indicating the type of
  Twitter card to show

For example, if your page has a ``caption`` field, you might want that as a
fallback if the ``search_description`` field is not provided. Likewise, you
can specify a blog image as the fallback for the Open Graph image.

.. code-block:: python

    class MyPage(SeoMixin, Page):

        caption = models.CharField(
            ...
        )
        blog_image = models.ForeignKey(
            "wagtailimages.Image",
            ...
        )

        # Provide caption as a fallback if search_description is empty.
        seo_description_sources = [
            "search_description",
            "caption",
        ]

        # Provide blog_image as a fallback if og_image is empty.
        seo_image_sources = [
            "og_image",
            "blog_image",
        ]


SEO Properties
--------------

Aside from these special fallbacks, every metadata value is accessed via a
"getter" property which can be overridden on the model.

.. code-block:: python

    @property
    def seo_author(self) -> str:
        """
        Gets the name of the author of this page.
        Override in your Page model as necessary.
        """
        ...

    @property
    def seo_canonical_url(self) -> str:
        """
        Gets the full/absolute/canonical URL preferred for meta tags and search
        engines. Override in your Page model as necessary.
        """
        ...

    @property
    def seo_description(self) -> str:
        """
        Gets the correct search engine and Open Graph description of this page.
        Override in your Page model as necessary.
        """
        ...

    @property
    def seo_image(self) -> Optional[AbstractImage]:
        """
        Gets the primary Open Graph image of this page.
        """
        ...

    @property
    def seo_logo(self) -> Optional[AbstractImage]:
        """
        Gets the primary logo of the organization.
        """
        ...

    @property
    def seo_sitename(self) -> str:
        """
        Gets the site name.
        Override in your Page model as necessary.
        """
        ...

    @property
    def seo_pagetitle(self) -> str:
        """
        Gets the correct search engine and Open Graph title of this page.
        Override in your Page model as necessary.
        """
        ...

    @property
    def seo_published_at(self) -> datetime:
        """
        Gets the date this page was first published.
        Override in your Page model as necessary.
        """
        ...


Customize Organization and Article Data
---------------------------------------

Structured data is generated as dictionaries, and serialized as JSON-LD.
Likewise, there are a few properties on the model which can be extended or
overridden to customize the structured data.

The two types provided by Wagtail SEO are "Organization" and "Article" as these
are most common across all websites.

For example, to manually add an additional field on to the Organization
structured data that is not provided by Wagtail SEO:

.. code-block:: python

    class MyPage(SeoMixin, Page):

        @property
        def seo_struct_org_dict(self) -> dict:
            # Call wagtailseo.
            sd_dict = super().seo_struct_org_dict

            # Add custom "sameAs" field (which is a list of social media URLs).
            sd_dict.update({
                "sameAs": ["https://www.linkedin.com/MegaCorp/"]
            })

            return sd_dict


Add New Types of Structured Data
--------------------------------

You can easily add your own custom types of structured data by following the
pattern and utilities provided by Wagtail SEO. For example, to add a Recipe
(`as defined by Google <https://developers.google.com/search/docs/data-types/recipe>`_)
first make a property on the page model:

.. code-block:: python

    from wagtailseo.models import SeoMixin
    from wagtailseo.utils import get_struct_data_images, StructDataEncoder


    class RecipePage(SeoMixin, Page):

        recipe_photo = models.ForeignKey(
            "wagtailimages.Image",
            ...
        )

        @property
        def my_struct_recipe_dict(self) -> dict:
            sd_dict = {
                "@context": "https://schema.org/",
                "@type": "Recipe",
                "name": self.seo_pagetitle,

                # Google requires multiple different aspect ratios for certain
                # structured data image fields. This will render the image in
                # 1:1, 4:3, and 16:9 aspect ratios with very high resolution
                # and return a list of URLs.
                "image": get_struct_data_images(self.get_site(), self.recipe_photo),

                "author": {
                    "@type": "Person",
                    "name": self.seo_author,
                },
                "datePublished": self.seo_published_at,
                "description": self.seo_description,
                "prepTime": "PT20M",
                "cookTime": "PT30M",
                "totalTime": "PT50M",
                ...
            }

            # Add the publisher (your organization) using the base organization
            # details (a lighter version of the full organization for including
            # in other forms of structured data such as this recipe).
            if self.seo_struct_publisher_dict:
                sd_dict.update({"publisher": self.seo_struct_publisher_dict})

            return sd_dict

        @property
        def my_struct_recipe_json(self) -> str:
            return json.dumps(self.my_struct_recipe_dict, cls=StructDataEncoder)

Now, update your HTML template to include the structured data at the end of the
body:

.. code-block:: html

    <body>
      ...
      <script type="application/ld+json">
        {{ self.my_struct_recipe_json }}
      </script>
    </body>
