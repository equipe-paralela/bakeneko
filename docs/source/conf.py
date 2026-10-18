# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Bakeneko'
copyright = '2026, Equipe Paralela'
author = 'Guilherme Nunes Trofino'
release = 'v1.8.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx.ext.duration',
    "sphinx.ext.intersphinx",
    'sphinx_design',
    'sphinx_simplepdf',
    'sphinxcontrib.mermaid',
]

templates_path = ['_templates']
exclude_patterns = []

intersphinx_mapping = {
    "sumo-firmware": ("https://sumo-firmware.readthedocs.io/en/latest/", None),
    "sumo-hardware": ("https://sumo-hardware.readthedocs.io/en/latest/", None),
}



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
