from setuptools import setup, find_packages
from wagtailseo import __version__

with open("README.md", encoding="utf8") as readme_file:
    readme = readme_file.read()

setup(
    name="wagtail-seo",
    version=__version__,
    author="CodeRed LLC",
    author_email="info@coderedcorp.com",
    url="https://github.com/coderedcorp/wagtail-seo",
    description="Search engine and social media optimization for Wagtail.",
    long_description=readme,
    long_description_content_type="text/markdown",
    license="BSD license",
    include_package_data=True,
    packages=["wagtailseo"],
    install_requires=[
        "wagtail>=2.0"
    ],
    classifiers=[
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3 :: Only",
        "Framework :: Django",
        "Framework :: Django :: 2.0",
        "Framework :: Django :: 2.1",
        "Framework :: Django :: 2.2",
        "Framework :: Django :: 3.0",
        "Framework :: Wagtail",
        "Framework :: Wagtail :: 2",
    ],
)
