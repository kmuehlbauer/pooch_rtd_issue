# Configuration file for the Sphinx documentation builder.

# -- Project information

import pooch
import requests

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
kwargs = {}
#kwargs.setdefault("stream", True)
kwargs["allow_redirects"] = True
url = "https://github.com/openradar/open-radar-data/raw/main/data/cfrad.20080604_002217_000_SPOL_v36_SUR.nc"
try:
    response = requests.get(url, timeout=30, **kwargs)
    response.raise_for_status()
    content = response.iter_content(chunk_size=1024)
    total = int(response.headers.get("content-length", 0))
    output_file.write(content)
    for chunk in content:
        if chunk:
            output_file.write(chunk)
            output_file.flush()
finally:
    output_file.close()
fname = pooch.retrieve("https://github.com/openradar/open-radar-data/raw/main/data/cfrad.20080604_002217_000_SPOL_v36_SUR.nc", "67821b6c2bb0f27b5de49dee636f36e6e5bbad95f1ee168cb2d1af48e98992fe")
