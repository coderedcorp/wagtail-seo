import re
from datetime import date
from datetime import datetime
from datetime import time
from json import JSONEncoder
from typing import List
from typing import Union

from django.conf import settings
from wagtail.images.models import AbstractImage
from wagtail.models import Site


# Matches a protocol, such as https://
PROTOCOL_RE = re.compile(r"^(\w[\w\.\-\+]*:)*//")
MEDIA_IS_ABSOLUTE = PROTOCOL_RE.match(settings.MEDIA_URL)


def serialize_date(date: Union[date, datetime, time]) -> str:
    """
    Serializes a datetime or time into ISO 8601 format required for Open Graph
    and Structured Data.

    :param Union[date, datetime, time] date: The date object to serialize.
    :rtype: str
    :returns: String-ified date.
    """
    return date.isoformat()


def get_absolute_media_url(site: Site) -> str:
    """
    Returns an absolute base URL for media files.

    This will normally be the site's root URL, except for when MEDIA_URL already
    looks like a full URL (e.g. if media is stored and served from S3, a CDN,
    etc.). The return value can always be safely prefixed to an image URL.

    :param Site site: The site object from which the media is served.
    :rtype: str
    :returns: The absolute base URL for media files of this site.
    """
    if MEDIA_IS_ABSOLUTE:
        return ""

    return site.root_url


def ensure_absolute_url(url: str, base_url: str) -> str:
    if not PROTOCOL_RE.match(url):
        url = base_url + url
    return url


def get_struct_data_images(site: Site, image: AbstractImage) -> List[str]:
    """
    Google requires multiple different aspect ratios for certain structured
    data image fields. This will render the image in 1:1, 4:3, and 16:9 aspect
    ratios with very high resolution and return a list of URLs.

    :param Site site: The Wagtail Site this image belongs to.
    :param Image image: An image descending from Wagtail AbstractImage model.
    :rtype: List[str]
    :return: A list of absolute image URLs.
    """

    base_url = get_absolute_media_url(site)

    # Use huge numbers because Wagtail will not upscale, but will max out at the
    # image's original resolution using the specified aspect ratio.
    # Google wants them high resolution.
    img1x1 = ensure_absolute_url(
        image.get_rendition("fill-10000x10000").url, base_url
    )
    img4x3 = ensure_absolute_url(
        image.get_rendition("fill-40000x30000").url, base_url
    )
    img16x9 = ensure_absolute_url(
        image.get_rendition("fill-16000x9000").url, base_url
    )

    return [img1x1, img4x3, img16x9]


class StructDataEncoder(JSONEncoder):
    """
    Serializes data into LD+JSON format required for Structured Data.
    """

    def default(self, obj):
        # Serialize dates to ISO 8601 format.
        if isinstance(obj, date):
            return serialize_date(obj)

        # Serialize datetimes to ISO 8601 format.
        if isinstance(obj, datetime):
            return serialize_date(obj)

        # Serialize times to ISO 8601 format.
        if isinstance(obj, time):
            return serialize_date(obj)

        # Fallback to default encoding.
        return super().default(obj)
