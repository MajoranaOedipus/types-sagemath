from sage.env import DOT_SAGE as DOT_SAGE, SAGE_LIB as SAGE_LIB

def get_cache_file():
    """
    Return the canonical filename for caching names of lazily imported
    modules.

    EXAMPLES::

        sage: from sage.misc.lazy_import_cache import get_cache_file
        sage: get_cache_file()
        '...-lazy_import_cache.pickle'
        sage: get_cache_file().startswith(DOT_SAGE)
        True
        sage: 'cache' in get_cache_file()
        True

    It should not matter whether DOT_SAGE ends with a slash::

        sage: OLD = DOT_SAGE
        sage: sage.misc.lazy_import_cache.DOT_SAGE = '/tmp'
        sage: get_cache_file().startswith('/tmp/')
        True
        sage: sage.misc.lazy_import_cache.DOT_SAGE = OLD
    """
