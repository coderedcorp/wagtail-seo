#!/usr/bin/env bash
black .
codespell .
flake8 .
mypy ./wagtailseo/
pytest ./testproject/
sphinx-build -M html ./docs/ ./docs/_build/ -W
