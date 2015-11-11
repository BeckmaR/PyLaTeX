"""
This module implements Error classes.

..  :copyright: (c) 2015 by Rene Beckmann.
    :license: MIT, see License for more details.
"""

from .base_classes import TableError


class TableRowSizeError(TableError):
    """Error for wrong table row size."""
