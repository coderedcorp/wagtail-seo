from bs4 import BeautifulSoup


def convert_to_amp(value: str, pretty=True) -> str:
    """
    Converts standard HTML to valid AMP-HTML.

    :param value str: A string containing HTML.
    :param pretty bool: Indent and pretty-print the outputted AMP HTML.
    """
    soup = BeautifulSoup(value, "html.parser")

    # Replace ``<img>`` tags with ``<amp-img>``.
    try:
        img_tags = soup.find_all("img")
        for img_tag in img_tags:
            # Force the tag to be non-self-closing
            # i.e. <img.../> becomes <amp-img...></amp-img>
            img_tag.can_be_empty_element = False
            # Change tag name from "img" to "amp-img"
            img_tag.name = "amp-img"
    except AttributeError:
        pass

    # Replace iframe tags with amp-iframe
    try:
        iframe_tags = soup.find_all("iframe")
        for iframe_tag in iframe_tags:
            # Change tag name from "iframe" to "amp-iframe"
            iframe_tag.name = "amp-iframe"
            # Add layout=repsonsive attribute.
            iframe_tag["layout"] = "responsive"
    except AttributeError:
        pass

    if pretty:
        return soup.prettify()

    return str(soup)
