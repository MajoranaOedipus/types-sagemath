from typing import Any, overload

class restore_atexit:
    '''restore_atexit(run=False, *, clear=None)

    File: /build/sagemath/src/sage/src/sage/cpython/atexit.pyx (starting at line 21)

    Context manager that restores the state of the atexit module to its
    previous state when exiting the context.

    INPUT:

    - ``run`` -- boolean (default: ``False``); if ``True``, when exiting the
      context (but before restoring the old exit functions), run all
      atexit functions which were added inside the context

    - ``clear`` -- boolean (default: equal to ``run``); if ``True``, clear
      already registered atexit handlers upon entering the context

    .. WARNING::

        The combination ``run=True`` and ``clear=False`` will cause
        already-registered exit functions to be run twice: once when
        exiting the context and again when exiting Python.

    EXAMPLES:

    For this example we will wrap the entire example with
    ``restore_atexit(clear=True)`` so as to start with a fresh atexit
    module state for the sake of the example.

    Note that the function ``atexit._run_exitfuncs()`` runs all registered
    handlers, and then clears the list of handlers, so we can use it to test
    manipulation of the ``atexit`` state::

        sage: import atexit
        sage: from sage.cpython.atexit import restore_atexit
        sage: def handler(*args, **kwargs):
        ....:     import sys
        ....:     # see https://github.com/sagemath/sage/issues/25270#comment:56
        ....:     sys.stdout.write(str((args, kwargs)))
        ....:     sys.stdout.write(\'\\n\')
        sage: atexit.register(handler, 1, 2, c=3)
        <function handler at 0x...>
        sage: atexit.register(handler, 4, 5, d=6)
        <function handler at 0x...>
        sage: with restore_atexit(clear=True):
        ....:     atexit._run_exitfuncs()  # Should be none registered
        ....:     atexit.register(handler, 1, 2, c=3)
        ....:     with restore_atexit():
        ....:         atexit._run_exitfuncs()  # Run just registered handler
        ....:     atexit._run_exitfuncs()  # Handler should be run again
        <function handler at 0x...>
        ((1, 2), {\'c\': 3})
        ((1, 2), {\'c\': 3})

    We test the ``run`` option::

        sage: with restore_atexit(run=True):
        ....:     # this handler is run when exiting the context
        ....:     _ = atexit.register(handler, 7, 8, e=9)
        ((7, 8), {\'e\': 9})
        sage: with restore_atexit(clear=False, run=True):
        ....:     # original handlers are run when exiting the context
        ....:     pass
        ((4, 5), {\'d\': 6})
        ((1, 2), {\'c\': 3})

    The original handlers are still in place::

        sage: atexit._run_exitfuncs()
        ((4, 5), {\'d\': 6})
        ((1, 2), {\'c\': 3})

    TESTS::

        sage: from sage.cpython.atexit import (_get_exithandlers,
        ....:                                  _clear_exithandlers)
        sage: atexit.register(handler, 1, 2, c=3)
        <function handler at 0x...>
        sage: atexit.register(handler, 4, 5, d=6)
        <function handler at 0x...>
        sage: print("Initial exit handlers:\\n{}".format(_get_exithandlers()))
        Initial exit handlers:
        [(<function handler at 0x...>, (1, 2), {\'c\': 3}),
         (<function handler at 0x...>, (4, 5), {\'d\': 6})]

        sage: with restore_atexit():
        ....:     pass
        sage: print("After restore_atexit:\\n{}".format(_get_exithandlers()))
        After restore_atexit:
        [(<function handler at 0x...>, (1, 2), {\'c\': 3}),
         (<function handler at 0x...>, (4, 5), {\'d\': 6})]

        sage: with restore_atexit(clear=True):
        ....:     print("Exit handlers in context manager: {}".format(
        ....:           _get_exithandlers()))
        Exit handlers in context manager: []

        sage: print("After restore_atexit with clear=True:\\n{}".format(
        ....:       _get_exithandlers()))
        After restore_atexit with clear=True:
        [(<function handler at 0x...>, (1, 2), {\'c\': 3}),
         (<function handler at 0x...>, (4, 5), {\'d\': 6})]
        sage: _clear_exithandlers()
        sage: _get_exithandlers()
        []'''
    @overload
    def __init__(self, run=..., clear=...) -> Any:
        """File: /build/sagemath/src/sage/src/sage/cpython/atexit.pyx (starting at line 128)"""
    @overload
    def __init__(self, clear=...) -> Any:
        """File: /build/sagemath/src/sage/src/sage/cpython/atexit.pyx (starting at line 128)"""
    def __enter__(self) -> Any:
        """restore_atexit.__enter__(self)

        File: /build/sagemath/src/sage/src/sage/cpython/atexit.pyx (starting at line 134)"""
    def __exit__(self, *exc) -> Any:
        """restore_atexit.__exit__(self, *exc)

        File: /build/sagemath/src/sage/src/sage/cpython/atexit.pyx (starting at line 141)"""
