from _typeshed import Incomplete

user_globals: Incomplete

def get_globals():
    '''
    Return the dictionary of all user globals.

    EXAMPLES::

        sage: from sage.repl.user_globals import get_globals, initialize_globals
        sage: initialize_globals(sage.all)
        sage: get_globals()["Matrix"]
        <cyfunction matrix at ...>
    '''
def set_globals(g: dict) -> None:
    """
    Set the dictionary of all user globals to ``g``.

    INPUT:

    - ``g`` -- dictionary; typically, this will be some dictionary
      given by the user interface or just ``globals()``

    EXAMPLES::

        sage: from sage.repl.user_globals import get_globals, set_globals
        sage: my_dict = dict()
        sage: set_globals(my_dict)
        sage: my_dict is get_globals()
        True
    """
def initialize_globals(all, g=None) -> None:
    '''
    Set the user globals dictionary to ``g`` and assign everything
    which was imported in module ``all`` as global.

    INPUT:

    - ``all`` -- a module whose globals will be injected

    - ``g`` -- dictionary; see :func:`set_globals`. If this is
      ``None``, keep the current globals dictionary.

    EXAMPLES::

        sage: my_globs = {"foo": "bar"}
        sage: from sage.repl.user_globals import initialize_globals
        sage: initialize_globals(sage.all, my_globs)
        sage: my_globs["foo"]
        \'bar\'
        sage: my_globs["Matrix"]
        <cyfunction matrix at ...>

    Remove ``Matrix`` from the globals and initialize again without
    changing the dictionary::

        sage: del my_globs["Matrix"]
        sage: initialize_globals(sage.all)
        sage: my_globs["Matrix"]
        <cyfunction matrix at ...>
    '''
def get_global(name):
    '''
    Return the value of global variable ``name``.

    Raise :exc:`NameError` if there is no such global variable.

    INPUT:

    - ``name`` -- string representing a variable name

    OUTPUT: the value of variable ``name``

    EXAMPLES::

        sage: from sage.repl.user_globals import get_global
        sage: the_answer = 42
        sage: get_global("the_answer")
        42
        sage: get_global("the_question")
        Traceback (most recent call last):
        ...
        NameError: name \'the_question\' is not defined
    '''
def set_global(name, value) -> None:
    '''
    Assign ``value`` to global variable ``name``. This is equivalent
    to executing ``name = value`` in the global namespace.

    INPUT:

    - ``name`` -- string representing a variable name

    - ``value`` -- a value to assign to the variable

    EXAMPLES::

        sage: from sage.repl.user_globals import set_global
        sage: set_global("the_answer", 42)
        sage: the_answer
        42
    '''
