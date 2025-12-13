from _typeshed import Incomplete

LEVEL: int
verbose_files: Incomplete

def verbose(mesg: str = '', t: int = 0, level: int = 1, caller_name=None):
    '''
    Print a message if the current verbosity is at least level.

    INPUT:

    - ``mesg`` -- string; a message to print

    - ``t`` -- integer (optional); if included, will also print ``cputime(t)``,
      which is the time since time ``t``. Thus ``t`` should have been obtained
      with ``t=cputime()``

    - ``level`` -- integer (default: 1); the verbosity level of
      what we are printing

    - ``caller_name`` -- string (default: ``None``); the name
      of the calling function. In most cases Python can deduce this, so
      it need not be provided.

    OUTPUT: possibly prints a message to stdout; also returns ``cputime()``

    EXAMPLES::

        sage: set_verbose(1)
        sage: t = cputime()
        sage: t = verbose("This is Sage.", t, level=1, caller_name="william")       # not tested
        VERBOSE1 (william): This is Sage. (time = 0.0)
        sage: set_verbose(0)
    '''
def set_verbose(level, files: str = 'all') -> None:
    '''
    Set the global Sage verbosity level.

    INPUT:

    - ``level`` -- integer between 0 and 2, inclusive

    - ``files`` -- (default: ``\'all\'``) list of files to make verbose, or
      \'all\' to make ALL files verbose (the default)

    OUTPUT: changes the state of the verbosity flag and possibly
    appends to the list of files that are verbose

    EXAMPLES::

        sage: set_verbose(2)
        sage: verbose("This is Sage.", level=1)  # not tested
        VERBOSE1 (?): This is Sage.
        sage: verbose("This is Sage.", level=2)  # not tested
        VERBOSE2 (?): This is Sage.
        sage: verbose("This is Sage.", level=3)  # not tested
        [no output]
        sage: set_verbose(0)
    '''
def set_verbose_files(file_name) -> None: ...
def get_verbose_files(): ...
def unset_verbose_files(file_name) -> None: ...
def get_verbose():
    """
    Return the global Sage verbosity level.

    EXAMPLES::

        sage: get_verbose()
        0
        sage: set_verbose(2)
        sage: get_verbose()
        2
        sage: set_verbose(0)
    """
