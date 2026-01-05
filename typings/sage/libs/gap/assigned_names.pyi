"""nodoctest
List of assigned names in GAP

EXAMPLES::

    sage: from sage.libs.gap.assigned_names import KEYWORDS, GLOBALS, FUNCTIONS
    sage: 'fi' in KEYWORDS
    True
    sage: 'ZassenhausIntersection' in GLOBALS
    True
    sage: 'SubdirectProduct' in FUNCTIONS
    True
"""

from _typeshed import Incomplete
from sage.libs.gap.libgap import libgap as libgap
from sage.libs.gap.saved_workspace import workspace as workspace

NamesGVars: Incomplete
Filtered: Incomplete
ValueGlobal: Incomplete
IsBoundGlobal: Incomplete
IsFunction: Incomplete
IsDocumentedWord: Incomplete

def load_or_compute(name, function):
    """
    Helper to load a cached value or compute it.

    INPUT:

    - ``name`` -- string; part of the cache filename

    - ``function`` -- function; to compute the value if not cached

    OUTPUT: the value of ``function``, possibly cached

    EXAMPLES::

        sage: from sage.libs.gap.assigned_names import GLOBALS
        sage: len(GLOBALS) > 1000    # indirect doctest
        True
        sage: from sage.libs.gap.saved_workspace import workspace
        sage: workspace(name='globals')
        ('...', True)
    """
def list_keywords():
    """
    Return the GAP reserved keywords.

    OUTPUT: tuple of strings

    EXAMPLES::

        sage: from sage.libs.gap.assigned_names import KEYWORDS
        sage: 'fi' in KEYWORDS   # indirect doctest
        True
    """

KEYWORDS: Incomplete

def list_globals():
    """
    Return the GAP reserved keywords.

    OUTPUT: tuple of strings

    EXAMPLES::

        sage: from sage.libs.gap.assigned_names import GLOBALS
        sage: 'ZassenhausIntersection' in GLOBALS   # indirect doctest
        True
    """

GLOBALS: Incomplete

def list_functions():
    """
    Return the GAP documented global functions.

    OUTPUT: tuple of strings

    EXAMPLES::

        sage: from sage.libs.gap.assigned_names import FUNCTIONS
        sage: 'IsBound' in FUNCTIONS    # is a keyword
        False
        sage: 'SubdirectProduct' in FUNCTIONS    # indirect doctest
        True
    """

FUNCTIONS: Incomplete
