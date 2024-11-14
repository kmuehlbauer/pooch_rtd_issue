# Configuration file for the Sphinx documentation builder.

# -- Project information

import requests
import subprocess 

project = 'Lumache'
copyright = '2021, Graziella'
author = 'Graziella'

release = '0.1'
version = '0.1.0'

# -- General configuration

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
]

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

# -- Options for HTML output

html_theme = 'sphinx_rtd_theme'

# -- Options for EPUB output
epub_show_urls = 'footnote'

output_file = open("output_file.nc", "w+b")
url = "https://github.com/readthedocs/readthedocs.org/raw/refs/heads/main/docs/dev/code-of-conduct.rst"
print("downloading: ", url)
try:
    response = requests.get(url, timeout=30, allow_redirects=True)
    response.raise_for_status()
    output_file.write(response.content)
finally:
    output_file.close()


subprocess.run(["ls", "-l"])
