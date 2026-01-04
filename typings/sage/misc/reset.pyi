"""
Interpreter reset
"""

EXCLUDE: set[str]
def reset(vars: str | None = None, attached=False) -> None:
    """
    Delete all user-defined variables, reset all global variables
    back to their default states, and reset all interfaces to other
    computer algebra systems.

    If vars is specified, just restore the value of vars and leave
    all other variables alone (i.e., call restore).

    Note that the variables in the set :obj:`sage.misc.reset.EXCLUDE` are
    excluded from being reset.

    INPUT:

    - ``vars`` -- list or space or comma separated string (default:
      ``None``); variables to restore

    - ``attached`` -- boolean (default: ``False``); if ``vars`` is not ``None``,
      whether to detach all attached files

    EXAMPLES::

        sage: x = 5
        sage: reset()
        sage: x                                                                         # needs sage.symbolic
        x

        sage: fn = tmp_filename(ext='.py')
        sage: sage.misc.reset.EXCLUDE.add('fn')
        sage: with open(fn, 'w') as f:
        ....:     _ = f.write('a = 111')
        sage: attach(fn)
        sage: af = attached_files(); len(af)
        1
        sage: af == [fn]
        True
        sage: reset()
        sage: af = attached_files(); len(af)
        1
        sage: reset(attached=True)
        sage: af = attached_files(); len(af)
        0
        sage: sage.misc.reset.EXCLUDE.remove('fn')

    TESTS:

    Confirm that assumptions do not survive a reset (:issue:`10855`)::

        sage: # needs sage.symbolic
        sage: assume(x > 3)
        sage: assumptions()
        [x > 3]
        sage: bool(x > 3)
        True
        sage: reset()
        sage: assumptions()
        []
        sage: bool(x > 3)
        False
    """
def reset_interfaces() -> None:
    ...
def restore(vars: str | None = None) -> None:
    """
    Restore predefined global variables to their default values.

    INPUT:

    - ``vars`` -- string or list (default: ``None``); if not ``None``, restores
      just the given variables to the default value

    EXAMPLES::

        sage: x = 10; y = 15/3; QQ='red'
        sage: QQ
        'red'
        sage: restore('QQ')
        sage: QQ
        Rational Field
        sage: x
        10
        sage: y = var('y')                                                              # needs sage.symbolic
        sage: restore('x y')
        sage: x                                                                         # needs sage.symbolic
        x
        sage: y
        Traceback (most recent call last):
        ...
        NameError: name 'y' is not defined
        sage: x = 10; y = 15/3; QQ='red'
        sage: ww = 15
        sage: restore()
        sage: x, QQ, ww                                                                 # needs sage.symbolic
        (x, Rational Field, 15)
        sage: restore('ww')
        sage: ww
        Traceback (most recent call last):
        ...
        NameError: name 'ww' is not defined
    """
