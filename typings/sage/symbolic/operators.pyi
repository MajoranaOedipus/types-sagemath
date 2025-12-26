import operator

from sage.structure.element import Expression as Expression

def add_vararg(first, *rest):
    """
    Return the sum of all the arguments.

    INPUT:

    - ``first``, ``*rest`` -- arguments to add

    OUTPUT: sum of the arguments

    EXAMPLES::

        sage: from sage.symbolic.operators import add_vararg
        sage: add_vararg(1, 2, 3, 4, 5, 6, 7)
        28
        sage: x = SR.var('x')
        sage: s = 1 + x + x^2  # symbolic sum
        sage: bool(s.operator()(*s.operands()) == s)
        True
    """
def mul_vararg(first, *rest):
    """
    Return the product of all the arguments.

    INPUT:

    - ``first``, ``*rest`` -- arguments to multiply

    OUTPUT: product of the arguments

    EXAMPLES::

        sage: from sage.symbolic.operators import mul_vararg
        sage: mul_vararg(9, 8, 7, 6, 5, 4)
        60480
        sage: x = SR.var('x')
        sage: p = x * cos(x) * sin(x)  # symbolic product
        sage: bool(p.operator()(*p.operands()) == p)
        True
    """

arithmetic_operators = {add_vararg: '+',
                        mul_vararg: '*',
                        operator.add: '+',
                        operator.sub: '-',
                        operator.mul: '*',
                        operator.truediv: '/',
                        operator.floordiv: '//',
                        operator.pow: '^'}
relation_operators = {operator.eq: '==',
                      operator.lt: '<',
                      operator.gt: '>',
                      operator.ne: '!=',
                      operator.le: '<=',
                      operator.ge: '>='}

class FDerivativeOperator:
    """
    Function derivative operators.

    A function derivative operator represents a partial derivative
    of a function with respect to some variables.

    The underlying data are the function, and the parameter set,
    a list recording the indices of the variables with respect
    to which the partial derivative is taken.
    """
    def __init__(self, function, parameter_set) -> None:
        """
        Initialize this function derivative operator.

        EXAMPLES::

            sage: from sage.symbolic.operators import FDerivativeOperator
            sage: f = function('foo')
            sage: op = FDerivativeOperator(f, [0, 1])
            sage: loads(dumps(op))
            D[0, 1](foo)
        """
    def __call__(self, *args):
        """
        Call this function derivative operator on these arguments.

        EXAMPLES::

            sage: from sage.symbolic.operators import FDerivativeOperator
            sage: x, y = SR.var('x, y')
            sage: f = function('foo')
            sage: op = FDerivativeOperator(f, [0, 1])
            sage: op(x, y)
            diff(foo(x, y), x, y)
            sage: op(x, x^2)
            D[0, 1](foo)(x, x^2)

        TESTS:

        We should be able to operate on functions evaluated at a
        point, not just a symbolic variable, :issue:`12796`::

           sage: from sage.symbolic.operators import FDerivativeOperator
           sage: f = function('f')
           sage: op = FDerivativeOperator(f, [0])
           sage: op(1)
           D[0](f)(1)
        """
    def function(self):
        """
        Return the function associated to this function derivative operator.

        EXAMPLES::

            sage: from sage.symbolic.operators import FDerivativeOperator
            sage: f = function('foo')
            sage: op = FDerivativeOperator(f, [0, 1])
            sage: op.function()
            foo
        """
    def change_function(self, new):
        """
        Return a new function derivative operator with the same
        parameter set but for a new function.

        EXAMPLES::

            sage: from sage.symbolic.operators import FDerivativeOperator
            sage: f = function('foo')
            sage: b = function('bar')
            sage: op = FDerivativeOperator(f, [0, 1])
            sage: op.change_function(bar)
            D[0, 1](bar)
        """
    def parameter_set(self):
        """
        Return the parameter set of this function derivative operator.

        This is the list of indices of variables with respect to which
        the derivative is taken.

        EXAMPLES::

            sage: from sage.symbolic.operators import FDerivativeOperator
            sage: f = function('foo')
            sage: op = FDerivativeOperator(f, [0, 1])
            sage: op.parameter_set()
            [0, 1]
        """

class DerivativeOperator:
    """
    Derivative operator.

    Acting with this operator onto a function gives a new operator (of
    type :class:`FDerivativeOperator`) representing the function
    differentiated with respect to one or multiple of its arguments.

    This operator takes a list of indices specifying the position of
    the arguments to differentiate. For example, D[0, 0, 1] is an
    operator that differentiates a function twice with respect to its
    first argument and once with respect to its second argument.

    EXAMPLES::

        sage: x, y = var('x,y'); f = function('f')
        sage: D[0](f)(x)
        diff(f(x), x)
        sage: D[0](f)(x, y)
        diff(f(x, y), x)
        sage: D[0, 1](f)(x, y)
        diff(f(x, y), x, y)
        sage: D[0, 1](f)(x, x^2)
        D[0, 1](f)(x, x^2)
    """
    class DerivativeOperatorWithParameters:
        def __init__(self, parameter_set) -> None: ...
        def __call__(self, function): ...
    def __getitem__(self, args):
        """
        TESTS:

        The order in which the indices are given should not matter::

            sage: x, y = var('x,y'); f = function('f')
            sage: bool(D[0, 1, 0](f)(x, y) == D[0, 0, 1](f)(x, y))
            True
            sage: bool(D[1, 0, 0](f)(x, y) == D[0, 0, 1](f)(x, y))
            True
        """

D: DerivativeOperator
