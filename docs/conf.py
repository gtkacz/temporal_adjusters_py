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

# Import version from pyproject.toml
with open('../pyproject.toml', 'rb') as f:
	pyproject = tomllib.load(f)

version = pyproject['project']['version']

# Add parent directory to path so sphinx can find the modules
sys.path.insert(0, os.path.abspath('..'))

project = 'Temporal Adjuster'
copyright = f'{date.today().year}, Gabriel Mitelman Tkacz'
author = 'Gabriel Mitelman Tkacz'
version = version

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
	'sphinx.ext.autodoc',
	'sphinx.ext.autosummary',
	'sphinx.ext.viewcode',
	'sphinx.ext.napoleon',
]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# Set the autodoc member ordering to match the source code
autodoc_member_order = 'bysource'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'alabaster'
html_static_path = ['_static']

# -- Add autodoc settings to properly handle type hints ----------------------
autodoc_typehints = 'description'
python_use_unqualified_type_names = True
