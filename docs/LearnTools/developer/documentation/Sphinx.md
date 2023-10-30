# Sphinx: Python Documentation Generator

https://www.sphinx-doc.org/en/master/

Sphinx can parse your docstring in python code and generate beautiful documentation web pages.
User can also write docuementation in rst or markdown format and generate web pages.

Many Python packages are using Sphinx to build their docuemntation.
For example, PyTorch builds its documentation with Sphinx. See0 https://github.com/pytorch/pytorch#building-the-documentation with [sphinx-rtd-theme](https://sphinx-rtd-theme.readthedocs.io/en/stable/). rtd means Read the Docs.

## Separate Source and Build

```bash
pip install -U Sphinx
pip install sphinx_rtd_theme
sphinx-quickstart build-docs
mkdir build-docs/source/docstring
sphinx-apidoc -o ./build-docs/source/docstring ./project
# add modules to index.rst
sphinx-build -b html ./build-docs/source ./docs
```

## Don't Separate Source and Build

```bash
sphinx-quickstart project # choose not to separate source and build
```

Replace `html_theme = 'alabaster'` with `html_theme = "sphinx_rtd_theme"`

Add extensions

```py
extensions = [
    'myst_parser',
    'sphinx.ext.autodoc'
]
```
