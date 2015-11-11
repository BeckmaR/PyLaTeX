
"""
This module implements Error base classes.

..  :copyright: (c) 2015 by Rene Beckmann.
    :license: MIT, see License for more details.
"""


class PyLaTeXError(Exception):
    """A Base class for all PyLaTeX Exceptions."""


class TableError(PyLaTeXError):
    """A Base class for all errors concerning tables."""
