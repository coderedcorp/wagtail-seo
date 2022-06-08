Contributing Guide
==================

The goal of Wagtail SEO is to become the most complete, go-to package for doing
SEO on Wagtail. This means it will not only provide the features, but will
continually stay up to date with evolving SEO practices and data standards (and
Google's whims).

That being said we heartily welcome contributions!

Bugs, feature requests, and ideas should be opened first as a `GitHub issue
<https://github.com/coderedcorp/wagtail-seo/issues>`_. Pull requests will be
accepted provided they meet the project's quality standards, and can be
demonstrated to align with a published SEO or data standard.

Development Environment
-----------------------

To set up your development environment:

#. Create a new environment (in a ``.venv`` folder)

   .. code-block:: shell

       python -m venv .venv

       # Mac and Linux
       source ./.venv/bin/activate

       # Windows (PowerShell)
       ./.venv/Scripts/Activate.ps1

#. Enter the source code directory and install the package locally with
   additional development tools

   .. code-block:: shell

       pip install -r requirements-dev.txt

#. Write some code.

#. Next, run the static analysis tools

   .. code-block:: shell

       black .
       codespell .
       flake8 .
       mypy ./wagtailseo/

#. Next, run the units tests. A simple Wagtail project using Wagtail SEO is
   in the ``testproject/`` directory. The tests will also generate a code
   coverage report at ``htmlcov/index.html``, which you can open in your browser

   .. code-block:: shell

       pytest ./testproject/


Documentation
-------------

To build the documentation, run the following, which will output to the
``docs/_build/html/`` directory

.. code-block:: shell

    sphinx-build -M html ./docs/ ./docs/_build/ -W


Publishing
----------

To create a python package, run the following, which will output the package to
the ``dist/`` directory

.. code-block:: shell

   python setup.py sdist bdist_wheel
