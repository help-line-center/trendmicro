# Configuration file for the Sphinx documentation builder.

import os
import sys

# -- Path setup --------------------------------------------------------------

# Add any paths to sys.path if your modules are outside the root
# sys.path.insert(0, os.path.abspath('../src'))

# -- Project information -----------------------------------------------------

project = 'Trend Micro Activation Guide'
copyright = '2025, Trend Micro'
author = 'Trend Micro Support Team'

# The full version, including alpha/beta/rc tags
release = '1.0.0'

# -- General configuration ---------------------------------------------------

# Sphinx extensions (leave blank or add as needed)
extensions = []

# Allow reStructuredText raw HTML
raw_enabled = True

# Templates and patterns to ignore
templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# -- Options for HTML output -------------------------------------------------

# Theme (optional)
# html_theme = 'sphinx_rtd_theme'

# Page titles
html_title = "How to Activate Trend Micro – Complete Setup Guide"
html_short_title = "Trend Micro Activation"
html_favicon = 'favicon.ico'  # Place the icon in _static or root

# Hide "view source"
html_show_sourcelink = False

# Allow raw HTML inside .rst files
html_allow_unsafe = True

# Theme settings
html_theme_options = {
    'show_powered_by': False,
}

# Static files (uncomment if needed)
# html_static_path = ['_static']
