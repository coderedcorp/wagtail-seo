Use on Snippet models
=====================

If you use your own custom models which do not inherit from Page (aka `Snippet`
in Wagtail), you can inherit from `SeoMixinBase`.

You'll have to override some properties and method to match your own seo
fields or fallbacks:

.. code-block:: python

    class MySnippet(SeoMixinBase, models.Model):
        promote_panels = SeoMixinBase.seo_panels

        def __str__(self):
            return f"my snippet {self.pk or 0}"

        def get_full_url(self) -> str:
            """
            Return the full URL (including protocol / domain) to this snippet
            """
            path = reverse("my_snippet_detail", kwargs={"pk": self.pk})
            return f"{self.get_site().root_url}/{path}"

        @property
        def seo_author(self) -> str:
            """
            Gets the name of the author of this page.
            """
            return "Tux"

        @property
        def seo_published_at(self) -> datetime:
            """
            Gets the date this snippet was first published.
            """
            return datetime(1122, 1, 1)

        @property
        def seo_modified_at(self) -> datetime:
            """
            Gets the date this snippet was first published.
            """
            return datetime(1204, 3, 31)

        def get_site(self):
            """
            Return the Site object that this snippet belongs to.
            """
            return Site.objects.first()

Do not forget to add your instance accessible via a `self` into context data
of your template:


.. code-block:: python

    class MySnippetDetailView(DetailView):
        model = MySnippet
        template_name = "my_snippet.html"

        def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            context["self"] = context["object"]
            return context

Now, ensure your template includes meta and struct_data into the head and body:

.. code-block:: html

    <!-- my_snippet.html -->
    <html>
        <head>
            {% include "wagtailseo/meta.html" %}
        </head>
        <body>
            {% include "wagtailseo/struct_data.html" %}
            <h1>My Snippet {{ self.pk }}</h1>
        </body>
    </html>
