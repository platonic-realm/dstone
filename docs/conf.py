import os
import sys
sys.path.insert(0, os.path.abspath('../src'))

project = 'Deepstone'
author = 'Arash Fatehi'

extensions = [
    'sphinx.ext.autodoc',
]

html_theme = 'alabaster'
