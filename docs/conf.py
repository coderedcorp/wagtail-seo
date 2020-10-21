# Configuration file for the Sphinx documentation builder.
#
# This file does only contain a selection of the most common options. For a
# full list see the documentation:
# http://www.sphinx-doc.org/en/master/config

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))

import datetime
import os
import sys

import django


DOCS_PATH = os.path.dirname(os.path.abspath(__file__))
PROJECT_PATH = os.path.dirname(DOCS_PATH)


# -- Project information -----------------------------------------------------

project = "wagtail-seo"
author = "CodeRed LLC"
copyright = f"{str(datetime.datetime.now().year)}, {author}"


# -- Setup Django ------------------------------------------------------------

# To render autodoc, a Django project must be configure to import wagtailseo.
sys.path.append(os.path.join(PROJECT_PATH, "testproject"))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "testproject.settings")
django.setup()


# -- General configuration ---------------------------------------------------

extensions = ["sphinx.ext.autodoc"]

source_suffix = ".rst"

master_doc = "index"

language = "en"

exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]


# -- Options for HTML output -------------------------------------------------

html_show_sourcelink = False

html_theme = "library"

html_sidebars = {
    "**": [
        "about.html",  # Project name, description, etc.
        "searchbox.html",  # Search.
        "globaltoc.html",  # Global table of contents.
        "readingmodes.html",  # Light/sepia/dark color schemes.
        "sponsors.html",  # Fancy sponsor links.
    ]
}

html_theme_options = {
    "description": "Search engine and social media optimization for Wagtail.",
    # "sponsors_heading": "Official CodeRed Project",
    "sponsors": [
        {
            "href": "https://github.com/coderedcorp/wagtail-seo",
            "image": "https://docs.coderedcorp.com/logo-square-red-128.png",
            "note": "This project is comercially supported by CodeRed.",
        }
    ],
}

html_last_updated_fmt = ""
