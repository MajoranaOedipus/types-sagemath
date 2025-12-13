from sage.env import SAGE_LOCAL as SAGE_LOCAL

def find_library(name):
    '''
    Return the shared library filename for a given library.

    The library name is given without any prefixes or suffixes--(e.g.
    just "Singular", not "libSingular", as shared library naming is
    platform-specific.

    This does \'\'not\'\' currently return the absolute path of the file on most
    platforms; see https://bugs.python.org/issue21042

    EXAMPLES::

        sage: from sage.misc.compat import find_library
        sage: find_library(\'giac\')                                                      # needs sage.libs.giac
        \'...giac...\'
    '''
