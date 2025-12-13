TIMEOUT: float

def sage_inputhook(context) -> None: ...
def install() -> None:
    """
    Install the Sage input hook.

    EXAMPLES:

    Make sure ipython is running so we really test this function::

        sage: from sage.repl.interpreter import get_test_shell
        sage: get_test_shell()
        <sage.repl.interpreter.SageTestShell object at ...>

    Run the function twice, to check it is idempotent (see :issue:`35235`)::

        sage: from sage.repl.inputhook import install
        sage: install()
        sage: install()
    """
def uninstall() -> None:
    """
    Uninstall the Sage input hook.

    EXAMPLES::

        sage: from sage.repl.inputhook import uninstall
        sage: uninstall()
    """
