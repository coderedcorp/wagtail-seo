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
copyright = f"2020–{str(datetime.datetime.now().year)}, {author}"


# -- Setup Django ------------------------------------------------------------

# To render autodoc, a Django project must be configure to import wagtailseo.
sys.path.append(os.path.join(PROJECT_PATH, "testproject"))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "testproject.settings")
django.setup()


# -- General configuration ---------------------------------------------------

extensions = [
    "sphinx.ext.autodoc",
    "sphinx_wagtail_theme",
]

source_suffix = ".rst"

master_doc = "index"

language = "en"

exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]


# -- Options for HTML output -------------------------------------------------

html_show_sourcelink = False

html_theme = "sphinx_wagtail_theme"

html_sidebars = {"**": ["searchbox.html", "globaltoc.html", "sponsor.html"]}

html_theme_options = {
    "project_name": "wagtail-seo",
    "github_url": "https://github.com/coderedcorp/wagtail-seo/blob/main/docs/",
    "footer_links": (
        "GitHub|https://github.com/coderedcorp/wagtail-seo,"
        "Wagtail Hosting by CodeRed|https://www.codered.cloud/,"
        "About CodeRed|https://www.coderedcorp.com/"
    ),
}

html_last_updated_fmt = ""
