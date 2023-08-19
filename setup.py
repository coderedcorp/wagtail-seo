from setuptools import setup
from wagtailseo import __version__

with open("README.md", encoding="utf8") as readme_file:
    readme = readme_file.read()

setup(
    name="cjkcms-seo",
    version=__version__,
    author="Grzegorz Krol",
    author_email="info@cjkcms.com",
    url="https://github.com/cjkpl/cjkcms-seo.git",
    description="Search engine and social media optimization for Wagtail.",
    long_description=readme,
    long_description_content_type="text/markdown",
    license="BSD license",
    include_package_data=True,
    packages=["wagtailseo"],
    python_requires=">=3.8",
    install_requires=["wagtail>=4.0,<=6.0"],
    classifiers=[
        "Framework :: Django",
        "Framework :: Wagtail",
        "Framework :: Wagtail :: 4",
        "Framework :: Wagtail :: 5",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3 :: Only",
        "Topic :: Internet :: WWW/HTTP :: Site Management",
    ],
)
