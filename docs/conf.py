# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information
import os
import sys
import tomllib
from datetime import date

# Load pyproject.toml
with open('../pyproject.toml', 'rb') as f:
	pyproject = tomllib.load(f)

# Add parent directory to path so sphinx can find the modules
sys.path.insert(0, os.path.abspath('..'))

project = pyproject['project']['name']
copyright = f'2024-{date.today().year}, {pyproject["project"]["maintainers"][0]["name"]}'
author = pyproject['project']['maintainers'][0]['name']
version = pyproject['project']['version']

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
	'sphinx.ext.autodoc',
	'sphinx.ext.viewcode',
	'sphinx.ext.napoleon',
]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
html_css_files = [
	'css/dark.css',
]

# Napoleon settings
napoleon_google_docstring = True
napoleon_numpy_docstring = False
napoleon_include_init_with_doc = False
napoleon_include_private_with_doc = False
napoleon_include_special_with_doc = False
napoleon_use_admonition_for_examples = False
napoleon_use_admonition_for_notes = False
napoleon_use_admonition_for_references = False
napoleon_use_ivar = False
napoleon_use_param = True
napoleon_use_rtype = True
napoleon_attr_annotations = True

# Autodoc settings
autodoc_default_options = {
	'members': True,
	'member-order': 'bysource',
	'special-members': '__init__',
	'undoc-members': True,
	'exclude-members': '__weakref__',
}

# Document inherited members for classes
autodoc_inherit_docstrings = True

# Show module/class where member is inherited from
# This helps understand which methods come from which modules
autodoc_show_inheritance = True
