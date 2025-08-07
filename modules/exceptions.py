"""
Custom exceptions
"""

class ProductFileEmptyError(Exception):
    """Empty file with products."""
    pass

class ProductFileMissingError(Exception):
    """The product file was not found."""
    pass