r"""
Loading and saving sessions and listing all variables

EXAMPLES:

We reset the current session, then define a rational number ``2/3``, and
verify that it is listed as a newly defined variable::

    sage: reset()
    sage: w = 2/3; w
    2/3
    sage: show_identifiers()
    ['w']

We next save this session. We are using a temporary directory to hold
the session file but we do this *for testing only.* Please do not do
this if you want to save your session permanently. Also note that
the ``tempfile`` module weasels its way into the session::

::

    sage: from tempfile import TemporaryDirectory
    sage: d = TemporaryDirectory()
    sage: save_session(os.path.join(d.name, 'session'))

This saves a dictionary with ``w`` as one of the keys::

    sage: z = load(os.path.join(d.name, 'session'))
    sage: list(z)
    ['w', 'd']
    sage: z['w']
    2/3

Next we reset all variables in the session except for the temporary
directory name. We verify that the session is reset, and then load
it back.::

    sage: sage.misc.reset.EXCLUDE.add('d')
    sage: reset()
    sage: show_identifiers()
    ['d']
    sage: load_session(os.path.join(d.name, 'session'))

Indeed ``w`` is now defined again.::

    sage: show_identifiers()
    ['d', 'w']
    sage: w
    2/3

Finally, we clean up the temporary directory::

    sage: d.cleanup()

AUTHOR:

- William Stein
"""

from sage.misc.persist import dumps as dumps, load as load, loads as loads, save as save

def init(state: dict|None=None):
    """
    Initialize some dictionaries needed by the :func:`show_identifiers`,
    :func:`save_session`, and :func:`load_session` functions.

    INPUT:

    - ``state`` -- dictionary or ``None``; if ``None`` the :func:`locals()`
      of the caller is used

    EXAMPLES::

        sage: reset()
        sage: w = 10
        sage: show_identifiers()
        ['w']

    When we call :func:`init()` below it reinitializes the internal table, so
    the ``w`` we just defined doesn't count as a new identifier::

        sage: sage.misc.session.init()
        sage: show_identifiers()
        []
    """
def load_session(name='sage_session', verbose=False):
    r"""
    Load a saved session.

    This merges in all variables from a previously saved session.  It
    does not clear out the variables in the current sessions, unless
    they are overwritten.  You can thus merge multiple sessions, and
    don't necessarily loose all your current work when you use this
    command.

    .. NOTE::

        In the Sage notebook the session name is searched for both
        in the current working cell and the ``DATA`` directory.

    EXAMPLES::

        sage: a = 5
        sage: f = lambda x: x^2

    For testing, we use a temporary file, that will be removed as soon
    as Sage is left. Of course, for permanently saving your session,
    you should choose a permanent file.

    ::

        sage: tmp_f = tmp_filename()
        sage: save_session(tmp_f)
        sage: del a; del f
        sage: load_session(tmp_f)
        sage: print(a)
        5

    Note that ``f`` does not come back, since it is a function, hence
    couldn't be saved::

        sage: print(f)
        Traceback (most recent call last):
        ...
        NameError: name 'f' is not defined
    """
def save_session(name='sage_session', verbose=False) -> None:
    r"""
    Save all variables that can be saved to the given filename.  The
    variables will be saved to a dictionary, which can be loaded using
    ``load(name)`` or :func:`load_session`.

    .. NOTE::

        1. Function and anything else that can't be pickled is not
           saved. This failure is silent unless you set
           ``verbose=True``.

        2. One can still make sessions that can't be reloaded.  E.g., define
           a class with::

               class Foo: pass

          and make an instance with::

               f = Foo()

          Then :func:`save_session` followed by ``quit`` and
          :func:`load_session` fails. I doubt there is any good way to
          deal with this. Fortunately, one can simply re-evaluate the
          code to define ``Foo``, and suddenly :func:`load_session`
          works fine.

    INPUT:

        - ``name`` -- string (default: ``'sage_session'``); name of ``sobj``
          to save the session to

        - ``verbose`` -- boolean (default: ``False``); if ``True``, print
          info about why certain variables can't be saved

    OUTPUT: creates a file and returns silently

    EXAMPLES:

    For testing, we use a temporary file that will be removed as soon
    as Sage is left. Of course, for permanently saving your session,
    you should choose a permanent file.

    ::

        sage: a = 5
        sage: tmp_f = tmp_filename()
        sage: save_session(tmp_f)
        sage: del a
        sage: load_session(tmp_f)
        sage: print(a)
        5

    We illustrate what happens when one of the variables is a function::

        sage: f = lambda x : x^2
        sage: save_session(tmp_f)
        sage: save_session(tmp_f, verbose=True)
        ...
        Not saving f: f is a function or method

    Something similar happens for cython-defined functions::

        sage: g = cython_lambda('double x', 'x*x + 1.5')
        sage: save_session(tmp_f, verbose=True)
        ...
        Not saving g: g is a cython function or method

    And the same for a lazy import::

        sage: from sage.misc.lazy_import import LazyImport
        sage: lazy_ZZ = LazyImport('sage.rings.integer_ring', 'ZZ')
        sage: save_session(tmp_f, verbose=True)
        ...
        Not saving lazy_ZZ: lazy_ZZ is a lazy import
    """
def show_identifiers(hidden=False) -> list[str]:
    r"""
    Return a list of all variable names that have been defined during
    this session.  By default, this returns only those identifiers
    that don't start with an underscore.

    INPUT:

    - ``hidden`` -- boolean (default: ``False``); if ``True``, also return
      identifiers that start with an underscore

    OUTPUT: list of variable names

    EXAMPLES:

    We reset the state of all variables, and see that none are defined::

        sage: reset()
        sage: show_identifiers()
        []

    We then define two variables, one which overwrites the default factor
    function; both are shown by :func:`show_identifiers()`::

        sage: a = 10
        sage: factor = 20
        sage: show_identifiers()
        ['factor', 'a']

    To get the actual value of a variable from the list, use the
    :func:`globals()` function.::

        sage: globals()['factor']
        20

    By default :func:`show_identifiers()` only returns variables that
    don't start with an underscore.  There is an option hidden that
    allows one to list those as well::

        sage: _hello = 10
        sage: show_identifiers()
        ['factor', 'a']
        sage: '_hello' in show_identifiers(hidden=True)
        True

    Many of the hidden variables are part of the IPython command history, at
    least in command line mode.::

        sage: show_identifiers(hidden=True)        # random output
        ['__builtin__', '_ih', '_oh', '_dh', 'exit', 'quit', '_', '__', '___',
        '_i', '_ii', '_iii', '_i1', 'factor', '_i2', '_2', '_i3', 'a', '_i4',
        '_i5', '_5', '_i6', '_6', '_i7', '_hello', '_i8', '_8', '_i9', '_9',
        '_i10']
    """
state_at_init: dict|None
