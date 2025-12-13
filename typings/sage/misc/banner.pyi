from sage.env import SAGE_BANNER as SAGE_BANNER, SAGE_VERSION as SAGE_VERSION

def version():
    """
    Return the version of Sage.

    OUTPUT: string

    EXAMPLES::

       sage: version()
       doctest:warning
       ...
       DeprecationWarning: Use sage.version instead.
       ...
       'SageMath version ..., Release Date: ...'
    """
def banner_text(full: bool = True):
    """
    Text for the Sage banner.

    INPUT:

    - ``full`` -- boolean (default: ``True``)

    OUTPUT:

    A string containing the banner message.

    If option full is ``False``, a simplified plain ASCII banner is
    displayed; if ``True`` the full banner with box art is displayed.

    EXAMPLES::

        sage: print(sage.misc.banner.banner_text(full=True))
        ┌────────────────────────────────────────────────────────────────────┐
        │ SageMath version ...
        sage: print(sage.misc.banner.banner_text(full=False))
        SageMath version ..., Release Date: ...
    """
def banner() -> None:
    '''
    Print the Sage banner.

    OUTPUT: none

    If the environment variable ``SAGE_BANNER`` is set to ``no``, no
    banner is displayed. If ``SAGE_BANNER`` is set to ``bare``, a
    simplified plain ASCII banner is displayed. Otherwise, the full
    banner with box art is displayed.

    EXAMPLES::

        sage: import sage.misc.banner; sage.misc.banner.SAGE_BANNER = \'\'
        sage: sage.misc.banner.banner()
        ┌────────────────────────────────────────────────────────────────────┐
        │ SageMath version ..., Release Date: ...                            │
        │ Using Python .... Type "help()" for help.                          │
        ...
    '''
def version_dict():
    '''
    A dictionary describing the version of Sage.

    OUTPUT: dictionary with keys \'major\', \'minor\', \'tiny\', \'prerelease\'

    This process the Sage version string and produces a dictionary.
    It expects the Sage version to be in one of these forms::

       N.N
       N.N.N
       N.N.N.N
       N.N.str
       N.N.N.str
       N.N.N.N.str

    where \'N\' stands for an integer and \'str\' stands for a string.
    The first integer is stored under the \'major\' key and the second
    integer under \'minor\'.  If there is one more integer, it is stored
    under \'tiny\'; if there are two more integers, then they are stored
    together as a float N.N under \'tiny\'.  If there is a string, then
    the key \'prerelease\' returns True.

    For example, if the Sage version is \'3.2.1\', then the dictionary
    is {\'major\': 3, \'minor\': 2, \'tiny\': 1, \'prerelease\': False}.
    If the Sage version is \'3.2.1.2\', then the dictionary is
    {\'major\': 3, \'minor\': 2, \'tiny\': 1.200..., \'prerelease\': False}.
    If the Sage version is \'3.2.alpha0\', then the dictionary is
    {\'major\': 3, \'minor\': 2, \'tiny\': 0, \'prerelease\': True}.

    EXAMPLES::

        sage: from sage.misc.banner import version_dict
        sage: print("SageMath major version is %s" % version_dict()[\'major\'])
        SageMath major version is ...
        sage: version_dict()[\'major\'] == int(sage.version.version.split(\'.\')[0])
        True
    '''
def require_version(major, minor: int = 0, tiny: int = 0, prerelease: bool = False, print_message: bool = False):
    """
    Return ``True`` if Sage version is at least ``major.minor.tiny``.

    INPUT:

    - ``major`` -- integer
    - ``minor`` -- integer (default: 0)
    - ``tiny`` -- float (default: 0)
    - ``prerelease`` -- boolean (default: ``False``)
    - ``print_message`` -- boolean (default: ``False``)

    OUTPUT: ``True`` if ``major.minor.tiny`` is <= version of Sage, ``False``
    otherwise

    For example, if the Sage version number is 3.1.2, then
    require_version(3, 1, 3) will return False, while
    require_version(3, 1, 2) will return True.
    If the Sage version is 3.1.2.alpha0, then
    require_version(3, 1, 1) will return True, while, by default,
    require_version(3, 1, 2) will return False.  Note, though, that
    require_version(3, 1, 2, prerelease=True) will return True:
    if the optional argument prerelease is True, then a prerelease
    version of Sage counts as if it were the released version.

    If optional argument print_message is ``True`` and this function
    is returning False, print a warning message.

    EXAMPLES::

        sage: from sage.misc.banner import require_version
        sage: require_version(2, 1, 3)
        True
        sage: require_version(821, 4)
        False
        sage: require_version(821, 4, print_message=True)
        This code requires at least version 821.4 of SageMath to run correctly.
        You are running version ...
        False
    """
