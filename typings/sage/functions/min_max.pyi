from _typeshed import Incomplete
from sage.misc.lazy_import import lazy_import as lazy_import
from sage.structure.element import Expression as Expression
from sage.symbolic.function import BuiltinFunction as BuiltinFunction

class MinMax_base(BuiltinFunction):
    def eval_helper(self, this_f, builtin_f, initial_val, args):
        """
        EXAMPLES::

            sage: # needs sage.symbolic
            sage: max_symbolic(3, 5, x)  # indirect doctest
            max(x, 5)
            sage: max_symbolic([5.0r])   # indirect doctest
            5.0
            sage: min_symbolic(3, 5, x)
            min(x, 3)
            sage: min_symbolic([5.0r])   # indirect doctest
            5.0
        """
    def __call__(self, *args, **kwds):
        """
        EXAMPLES::

            sage: max_symbolic(3, 5, x)                                                 # needs sage.symbolic
            max(x, 5)
            sage: max_symbolic(3, 5, x, hold=True)                                      # needs sage.symbolic
            max(3, 5, x)
            sage: max_symbolic([3, 5, x])                                               # needs sage.symbolic
            max(x, 5)

        ::

            sage: min_symbolic(3, 5, x)                                                 # needs sage.symbolic
            min(x, 3)
            sage: min_symbolic(3, 5, x, hold=True)                                      # needs sage.symbolic
            min(3, 5, x)
            sage: min_symbolic([3, 5, x])                                               # needs sage.symbolic
            min(x, 3)

        TESTS:

        We get an exception if no arguments are given::

            sage: max_symbolic()
            Traceback (most recent call last):
            ...
            ValueError: number of arguments must be > 0

        Check if a single argument which is not iterable works::

            sage: # needs sage.symbolic
            sage: max_symbolic(None)
            Traceback (most recent call last):
            ...
            TypeError: 'NoneType' object is not iterable
            sage: max_symbolic(5)
            Traceback (most recent call last):
            ...
            TypeError: 'sage.rings.integer.Integer' object is not iterable
            sage: max_symbolic(x)
            Traceback (most recent call last):
            ...
            TypeError: 'sage.symbolic.expression.Expression' object is not iterable
            sage: min_symbolic(5)
            Traceback (most recent call last):
            ...
            TypeError: 'sage.rings.integer.Integer' object is not iterable
            sage: min_symbolic(x)
            Traceback (most recent call last):
            ...
            TypeError: 'sage.symbolic.expression.Expression' object is not iterable
        """

class MaxSymbolic(MinMax_base):
    def __init__(self) -> None:
        """
        Symbolic `\\max` function.

        The Python builtin :func:`max` function does not work as expected when symbolic
        expressions are given as arguments. This function delays evaluation
        until all symbolic arguments are substituted with values.

        EXAMPLES::

            sage: # needs sage.symbolic
            sage: max_symbolic(3, x)
            max(3, x)
            sage: max_symbolic(3, x).subs(x=5)
            5
            sage: max_symbolic(3, 5, x)
            max(x, 5)
            sage: max_symbolic([3, 5, x])
            max(x, 5)

        TESTS::

            sage: loads(dumps(max_symbolic(x, 5)))                                      # needs sage.symbolic
            max(x, 5)
            sage: latex(max_symbolic(x, 5))                                             # needs sage.symbolic
            \\max\\left(x, 5\\right)
            sage: max_symbolic(x, 5)._sympy_()                                          # needs sympy sage.symbolic
            Max(5, x)
        """

max_symbolic: Incomplete

class MinSymbolic(MinMax_base):
    def __init__(self) -> None:
        """
        Symbolic `\\min` function.

        The Python builtin :func:`min` function does not work as expected when symbolic
        expressions are given as arguments. This function delays evaluation
        until all symbolic arguments are substituted with values.

        EXAMPLES::

            sage: # needs sage.symbolic
            sage: min_symbolic(3, x)
            min(3, x)
            sage: min_symbolic(3, x).subs(x=5)
            3
            sage: min_symbolic(3, 5, x)
            min(x, 3)
            sage: min_symbolic([3, 5, x])
            min(x, 3)

        TESTS::

            sage: loads(dumps(min_symbolic(x, 5)))                                      # needs sage.symbolic
            min(x, 5)
            sage: latex(min_symbolic(x, 5))                                             # needs sage.symbolic
            \\min\\left(x, 5\\right)
            sage: min_symbolic(x, 5)._sympy_()                                          # needs sympy sage.symbolic
            Min(5, x)
        """

min_symbolic: Incomplete
