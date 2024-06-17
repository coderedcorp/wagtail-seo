Customizing the Editor Interface
================================

Wagtail SEO provides various editor panels for use in the Wagtail page editor.

The simplest way to enable them is to override the built-in promote tab on your
page model:

.. code-block:: python

    class MyPage(SeoMixin, Page):

        promote_panels = SeoMixin.seo_panels

This is identical to combining all of the individual editor panels provided
by Wagtail SEO. You may mix and match as necessary.

.. code-block:: python

    class MyPage(SeoMixin, Page):

        # Each is a list of panels.
        promote_panels = (
            seo_meta_panels +
            seo_menu_panels
        )

Going further, it is possible to totally override all of Wagtail's tabs to
define your own. For example, you could add the SEO panels in their own tab.

This is accomplished by overriding Wagtail's ``get_edit_handler()`` method.

.. code-block:: python

    class MyPage(SeoMixin, Page):

        @cached_classmethod
        def get_edit_handler(cls):
            panels = [

                # Normal Wagtail panels.
                ObjectList(cls.content_panels, heading="Content"),
                ObjectList(cls.promote_panels, heading="Promote",),
                ObjectList(cls.settings_panels, heading="Settings", classname="settings"),

                # Add custom SEO panels in new tab.
                ObjectList(SeoMixin.seo_panels, heading="SEO", classname="seo"),
            ]
            return TabbedInterface(panels).bind_to(model=cls)
