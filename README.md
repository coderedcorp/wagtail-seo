Wagtail SEO
===========

Search engine and social media optimization for Wagtail.

(COMING SOON - Work in progress)

[Source code on GitHub](https://github.com/coderedcorp/wagtail-seo)


Status
------

|                        |                      |
|------------------------|----------------------|
| Python Package         | [![PyPI - Python Version](https://img.shields.io/pypi/pyversions/wagtail-seo)](https://pypi.org/project/wagtail-seo/) [![PyPI - Django Version](https://img.shields.io/pypi/djversions/wagtail-seo)](https://pypi.org/project/wagtail-seo/) [![PyPI - Wheel](https://img.shields.io/pypi/wheel/wagtail-seo)](https://pypi.org/project/wagtail-seo/) [![PyPI - Downloads](https://img.shields.io/pypi/dm/wagtail-seo)](https://pypi.org/project/wagtail-seo/) [![PyPI](https://img.shields.io/pypi/v/wagtail-seo)](https://pypi.org/project/wagtail-seo/) |
| Build                  | [![Build Status](https://dev.azure.com/coderedcorp/cr-github/_apis/build/status/wagtail-seo?branchName=main)](https://dev.azure.com/coderedcorp/wagtail-seo/_build/latest?definitionId=13&branchName=main) [![Azure DevOps tests (branch)](https://img.shields.io/azure-devops/tests/coderedcorp/cr-github/13/main)](https://dev.azure.com/coderedcorp/cr-github/_build/latest?definitionId=13&branchName=main) [![Azure DevOps coverage (branch)](https://img.shields.io/azure-devops/coverage/coderedcorp/cr-github/13/main)](https://dev.azure.com/coderedcorp/cr-github/_build/latest?definitionId=13&branchName=main) |


Contributing
------------

To set up your development environment:

1. Create a new environment:

   ```
   python -m venv ./venv/

   # Mac and Linux
   source ./venv/bin/activate

   # Windows (PowerShell)
   ./venv/Scripts/Activate.ps1
   ```

2. Enter the source code directory and install the package locally with
   additional development tools:

   ```
   pip install -r requirements-dev.txt
   ```

3. Write some code.

4. Next, run the static analysis tools:

   ```
   black .
   flake8 ./wagtailseo/
   mypy ./wagtailseo/
   codespell ./wagtailseo/ ./docs/
   ```

5. Next, run the units tests. A simple Wagtail project using Wagtail SEO is
   in the `testproject/` directory. The tests will generate a visual HTML file
   at `htmlcov/index.html` when finished, which you can open in your browser.

   ```
   pytest ./testproject/
   ```

6. To build the documentation, run the following, which will output to the
   `docs/_build/html/` directory.

   ```
   sphinx-build -M html ./docs/ ./docs/_build/ -W
   ```

7. To create a python package, run the following, which will output the package
   to the `dist/` directory.

   ```
   python setup.py sdist bdist_wheel
   ```
