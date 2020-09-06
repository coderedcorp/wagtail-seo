import re

from django.conf import settings
from wagtail.core.models import Site


# Matches a protocol, such as https://
PROTOCOL_RE = re.compile(r"^(\w[\w\.\-\+]*:)*//")
MEDIA_IS_ABSOLUTE = PROTOCOL_RE.match(settings.MEDIA_URL)


def get_absolute_media_url(site: Site) -> str:
    """
    Returns an absolute base URL for media files.

    This will normally be the site's root URL, except for when MEDIA_URL already
    looks like a full URL.
    """
    if MEDIA_IS_ABSOLUTE:
        return ""

    return site.root_url
