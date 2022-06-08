"""
Registers wagtail-seo icon in the admin dashboard.
"""
from wagtail import hooks


@hooks.register("register_icons")
def register_icons(icons):
    """
    Add custom SVG icons to the Wagtail admin.
    """
    # These SVG files should be in the django templates folder, and follow exact
    # specifications to work with Wagtail:
    # https://github.com/wagtail/wagtail/pull/6028
    icons.append("wagtailseo/wagtailseo-line-chart.svg")
    return icons
