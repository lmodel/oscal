"""oscal.

OSCAL: Open Security Controls Assessment Language: LinkML Schema
"""

try:
    from oscal._version import __version__, __version_tuple__
except ImportError:  # pragma: no cover
    __version__ = "0.0.0"
    __version_tuple__ = (0, 0, 0)
