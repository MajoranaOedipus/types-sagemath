from sage.misc.misc import run_once as run_once

class UndefSageHelper:
    """
    Helper class to convert sympy function objects to sage functions

    EXAMPLES::

        sage: from sympy import Function
        sage: f = function('f')
        sage: F = Function('f')
        sage: assert f._sympy_() == F
        sage: assert f == F._sage_()
    """
    def __get__(self, ins, typ): ...

@run_once
def sympy_init() -> None:
    """
    Add ``_sage_()`` methods to SymPy objects where needed.

    This gets called with every call to ``Expression._sympy_()``
    so there is only need to call it if you bypass ``_sympy_()`` to
    create SymPy objects. Note that SymPy objects have ``_sage_()``
    methods hard installed but having them inside Sage as
    one file makes them easier to maintain for Sage developers.

    EXAMPLES::

        sage: from sage.interfaces.sympy import sympy_init
        sage: from sympy import Symbol, Abs
        sage: sympy_init()
        sage: assert abs(x) == Abs(Symbol('x'))._sage_()
    """
def check_expression(expr, var_symbols, only_from_sympy: bool = False) -> None:
    '''
    Do ``eval(expr)`` both in Sage and SymPy and other checks.

    EXAMPLES::

        sage: from sage.interfaces.sympy import check_expression
        sage: check_expression("1.123*x", "x")
    '''
def check_all() -> None:
    """
    Call some tests that were originally in SymPy.

    EXAMPLES::

        sage: from sage.interfaces.sympy import check_all
        sage: check_all()
    """
def sympy_set_to_list(set, vars):
    """
    Convert all set objects that can be returned by SymPy's solvers.
    """
