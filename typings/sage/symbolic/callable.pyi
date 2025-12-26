"""
Callable Symbolic Expressions

EXAMPLES:

When you do arithmetic with::

    sage: f(x, y, z) = sin(x+y+z)
    sage: g(x, y) = y + 2*x
    sage: f + g
    (x, y, z) |--> 2*x + y + sin(x + y + z)

::

    sage: f(x, y, z) = sin(x+y+z)
    sage: g(w, t) = cos(w - t)
    sage: f + g
    (t, w, x, y, z) |--> cos(-t + w) + sin(x + y + z)

::

    sage: f(x, y, t) = y*(x^2-t)
    sage: g(x, y, w) = x + y - cos(w)
    sage: f*g
    (x, y, t, w) |--> (x^2 - t)*(x + y - cos(w))*y

::

    sage: f(x,y, t) = x+y
    sage: g(x, y, w) = w + t
    sage: f + g
    (x, y, t, w) |--> t + w + x + y

TESTS:

The arguments in the definition must be symbolic variables (:issue:`10747`)::

    sage: f(1)=2
    Traceback (most recent call last):
    ...
    SyntaxError: can...t assign to function call...

    sage: f(x,1)=2
    Traceback (most recent call last):
    ...
    SyntaxError: can...t assign to function call...

    sage: f(1,2)=3
    Traceback (most recent call last):
    ...
    SyntaxError: can...t assign to function call...

    sage: f(1,2)=x
    Traceback (most recent call last):
    ...
    SyntaxError: can...t assign to function call...

    sage: f(x,2)=x
    Traceback (most recent call last):
    ...
    SyntaxError: can...t assign to function call...
"""
import sage.rings.abc
from sage.categories.pushout import ConstructionFunctor as ConstructionFunctor
from sage.structure.factory import UniqueFactory as UniqueFactory
from sage.symbolic.ring import SR as SR, SymbolicRing as SymbolicRing

class CallableSymbolicExpressionFunctor(ConstructionFunctor):
    rank: int
    def __init__(self, arguments) -> None:
        """
        A functor which produces a CallableSymbolicExpressionRing from
        the SymbolicRing.

        EXAMPLES::

            sage: from sage.symbolic.callable import CallableSymbolicExpressionFunctor
            sage: x,y = var('x,y')
            sage: f = CallableSymbolicExpressionFunctor((x,y)); f
            CallableSymbolicExpressionFunctor(x, y)
            sage: f(SR)
            Callable function ring with arguments (x, y)

            sage: loads(dumps(f))
            CallableSymbolicExpressionFunctor(x, y)
        """
    def merge(self, other):
        """
        EXAMPLES::

            sage: from sage.symbolic.callable import CallableSymbolicExpressionFunctor
            sage: x,y = var('x,y')
            sage: a = CallableSymbolicExpressionFunctor((x,))
            sage: b = CallableSymbolicExpressionFunctor((y,))
            sage: a.merge(b)
            CallableSymbolicExpressionFunctor(x, y)
        """
    def __call__(self, R):
        """
        EXAMPLES::

            sage: from sage.symbolic.callable import CallableSymbolicExpressionFunctor
            sage: x,y = var('x,y')
            sage: a = CallableSymbolicExpressionFunctor((x,y))
            sage: a(SR)
            Callable function ring with arguments (x, y)
        """
    def arguments(self):
        """
        EXAMPLES::

            sage: from sage.symbolic.callable import CallableSymbolicExpressionFunctor
            sage: x,y = var('x,y')
            sage: a = CallableSymbolicExpressionFunctor((x,y))
            sage: a.arguments()
            (x, y)
        """
    def unify_arguments(self, x):
        """
        Take the variable list from another ``CallableSymbolicExpression``
        object and compare it with the current ``CallableSymbolicExpression``
        object's variable list, combining them according to the following rules:

        Let ``a`` be ``self``'s variable list, let ``b`` be ``y``'s
        variable list.

        #. If ``a == b``, then the variable lists are
           identical, so return that variable list.

        #. If ``a`` `\\neq` ``b``, then check if the first `n` items in
           ``a`` are the first `n` items in ``b``, or vice versa. If
           so, return a list with these `n` items, followed by the
           remaining items in ``a`` and ``b`` sorted together in
           alphabetical order.


        .. NOTE::

           When used for arithmetic between
           ``CallableSymbolicExpression``'s, these rules ensure that
           the set of ``CallableSymbolicExpression``'s will have
           certain properties. In particular, it ensures that the set
           is a *commutative* ring, i.e., the order of the input
           variables is the same no matter in which order arithmetic
           is done.

        INPUT:

        - ``x`` -- a ``CallableSymbolicExpression``

        OUTPUT: a tuple of variables

        EXAMPLES::

            sage: from sage.symbolic.callable import CallableSymbolicExpressionFunctor
            sage: x,y = var('x,y')
            sage: a = CallableSymbolicExpressionFunctor((x,))
            sage: b = CallableSymbolicExpressionFunctor((y,))
            sage: a.unify_arguments(b)
            (x, y)

        AUTHORS:

        - Bobby Moretti: thanks to William Stein for the rules
        """

class CallableSymbolicExpressionRing_class(SymbolicRing, sage.rings.abc.CallableSymbolicExpressionRing):
    symbols: dict
    def __init__(self, arguments) -> None:
        """
        EXAMPLES:

        We verify that coercion works in the case where ``x`` is not an
        instance of SymbolicExpression, but its parent is still the
        SymbolicRing::

            sage: f(x) = 1
            sage: f*e
            x |--> e

        TESTS::

            sage: TestSuite(f.parent()).run(skip=['_test_divides'])
        """
    def construction(self):
        """
        EXAMPLES::

            sage: f(x,y) = x^2 + y
            sage: f.parent().construction()
            (CallableSymbolicExpressionFunctor(x, y), Symbolic Ring)
        """
    def arguments(self):
        """
        Return the arguments of ``self``.

        The order that the variables appear in ``self.arguments()`` is
        the order that is used in evaluating the elements of ``self``.

        EXAMPLES::

            sage: x,y = var('x,y')
            sage: f(x,y) = 2*x+y
            sage: f.parent().arguments()
            (x, y)
            sage: f(y,x) = 2*x+y
            sage: f.parent().arguments()
            (y, x)
        """
    args = arguments
    __reduce__: Incomplete

class CallableSymbolicExpressionRingFactory(UniqueFactory):
    def create_key(self, args, check: bool = True):
        """
        EXAMPLES::

            sage: x,y = var('x,y')
            sage: CallableSymbolicExpressionRing.create_key((x,y))
            (x, y)
        """
    def create_object(self, version, key, **extra_args):
        """
        Return a CallableSymbolicExpressionRing given a version and a key.

        EXAMPLES::

            sage: x,y = var('x,y')
            sage: CallableSymbolicExpressionRing.create_object(0, (x, y))
            Callable function ring with arguments (x, y)
        """

CallableSymbolicExpressionRing: CallableSymbolicExpressionRingFactory
