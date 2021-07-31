from setuptools import setup
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
    python_requires=">=3.6",
    install_requires=["wagtail>=2.9"],
    classifiers=[
        "Framework :: Django",
        "Framework :: Django :: 2.2",
        "Framework :: Django :: 3.0",
        "Framework :: Django :: 3.1",
        "Framework :: Django :: 3.2",
        "Framework :: Wagtail",
        "Framework :: Wagtail :: 2",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Topic :: Internet :: WWW/HTTP :: Site Management",
    ],
)
