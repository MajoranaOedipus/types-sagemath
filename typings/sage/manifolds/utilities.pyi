from sage.functions.other import abs_symbolic as abs_symbolic
from sage.functions.trig import cos as cos, sin as sin
from sage.misc.functional import sqrt as sqrt
from sage.rings.rational import Rational as Rational
from sage.symbolic.constants import pi as pi
from sage.symbolic.expression import Expression as Expression
from sage.symbolic.expression_conversions import ExpressionTreeWalker as ExpressionTreeWalker
from sage.symbolic.ring import SR as SR

class SimplifySqrtReal(ExpressionTreeWalker):
    """
    Class for simplifying square roots in the real domain, by walking the
    expression tree.

    The end user interface is the function :func:`simplify_sqrt_real`.

    INPUT:

    - ``ex`` -- a symbolic expression

    EXAMPLES:

    Let us consider the square root of an exact square under some assumption::

        sage: assume(x<1)
        sage: a = sqrt(x^2-2*x+1)

    The method :meth:`~sage.symbolic.expression.Expression.simplify_full()`
    is ineffective on such an expression::

        sage: a.simplify_full()
        sqrt(x^2 - 2*x + 1)

    and the more aggressive method :meth:`~sage.symbolic.expression.Expression.canonicalize_radical()`
    yields a wrong result, given that `x<1`::

        sage: a.canonicalize_radical()  # wrong output!
        x - 1

    We construct a :class:`SimplifySqrtReal` object ``s`` from the symbolic
    expression ``a``::

        sage: from sage.manifolds.utilities import SimplifySqrtReal
        sage: s = SimplifySqrtReal(a)

    We use the ``__call__`` method to walk the expression tree and produce a
    correctly simplified expression::

        sage: s()
        -x + 1

    Calling the simplifier ``s`` with an expression actually simplifies this
    expression::

        sage: s(a)  # same as s() since s is built from a
        -x + 1
        sage: s(sqrt(x^2))
        abs(x)
        sage: s(sqrt(1+sqrt(x^2-2*x+1)))  # nested sqrt's
        sqrt(-x + 2)

    Another example where both
    :meth:`~sage.symbolic.expression.Expression.simplify_full()` and
    :meth:`~sage.symbolic.expression.Expression.canonicalize_radical()`
    fail::

        sage: b = sqrt((x-1)/(x-2))*sqrt(1-x)
        sage: b.simplify_full()  # does not simplify
        sqrt(-x + 1)*sqrt((x - 1)/(x - 2))
        sage: b.canonicalize_radical()  # wrong output, given that x<1
        (I*x - I)/sqrt(x - 2)
        sage: SimplifySqrtReal(b)()  # OK, given that x<1
        -(x - 1)/sqrt(-x + 2)

    TESTS:

    We check that the inverse of a square root is well simplified; this is a
    a non-trivial test since ``1/sqrt(x)`` is represented by ``pow(x,-1/2)``
    in the expression tree::

        sage: SimplifySqrtReal(1/sqrt(x^2-4*x+4))()
        -1/(x - 2)
        sage: SimplifySqrtReal(sqrt((x-2)/((x-3)*(x^2-2*x+1))))()
        -sqrt(-x + 2)/((x - 1)*sqrt(-x + 3))
        sage: forget()  # for doctests below

    .. SEEALSO::

        :func:`simplify_sqrt_real` for more examples with
        :class:`SimplifySqrtReal` at work.
    """
    def arithmetic(self, ex, operator):
        """
        This is the only method of the base class
        :class:`~sage.symbolic.expression_conversions.ExpressionTreeWalker`
        that is reimplemented, since square roots are considered as
        arithmetic operations with ``operator`` = ``pow`` and
        ``ex.operands()[1]`` = ``1/2`` or ``-1/2``.

        INPUT:

        - ``ex`` -- a symbolic expression
        - ``operator`` -- an arithmetic operator

        OUTPUT:

        - a symbolic expression, equivalent to ``ex`` with square roots
          simplified

        EXAMPLES::

            sage: from sage.manifolds.utilities import SimplifySqrtReal
            sage: a = sqrt(x^2+2*x+1)
            sage: s = SimplifySqrtReal(a)
            sage: a.operator()
            <built-in function pow>
            sage: s.arithmetic(a, a.operator())
            abs(x + 1)

        ::

            sage: a = x + 1  # no square root
            sage: s.arithmetic(a, a.operator())
            x + 1

        ::

            sage: a = x + 1 + sqrt(function('f')(x)^2)
            sage: s.arithmetic(a, a.operator())
            x + abs(f(x)) + 1
        """

class SimplifyAbsTrig(ExpressionTreeWalker):
    """
    Class for simplifying absolute values of cosines or sines (in the real
    domain), by walking the expression tree.

    The end user interface is the function :func:`simplify_abs_trig`.

    INPUT:

    - ``ex`` -- a symbolic expression

    EXAMPLES:

    Let us consider the following symbolic expression with some assumption
    on the range of the variable `x`::

        sage: assume(pi/2<x, x<pi)
        sage: a = abs(cos(x)) + abs(sin(x))

    The method :meth:`~sage.symbolic.expression.Expression.simplify_full()`
    is ineffective on such an expression::

        sage: a.simplify_full()
        abs(cos(x)) + abs(sin(x))

    We construct a :class:`SimplifyAbsTrig` object ``s`` from the symbolic
    expression ``a``::

        sage: from sage.manifolds.utilities import SimplifyAbsTrig
        sage: s = SimplifyAbsTrig(a)

    We use the ``__call__`` method to walk the expression tree and produce a
    correctly simplified expression, given that `x\\in(\\pi/2, \\pi)`::

        sage: s()
        -cos(x) + sin(x)

    Calling the simplifier ``s`` with an expression actually simplifies this
    expression::

        sage: s(a)  # same as s() since s is built from a
        -cos(x) + sin(x)
        sage: s(abs(cos(x/2)) + abs(sin(x/2)))  #  pi/4 < x/2 < pi/2
        cos(1/2*x) + sin(1/2*x)
        sage: s(abs(cos(2*x)) + abs(sin(2*x)))  #  pi < 2 x < 2*pi
        abs(cos(2*x)) - sin(2*x)
        sage: s(abs(sin(2+abs(cos(x)))))  # nested abs(sin_or_cos(...))
        sin(-cos(x) + 2)

    TESTS::

        sage: forget()  # for doctests below

    .. SEEALSO::

        :func:`simplify_abs_trig` for more examples with
        :class:`SimplifyAbsTrig` at work.
    """
    def composition(self, ex, operator):
        """
        This is the only method of the base class
        :class:`~sage.symbolic.expression_conversions.ExpressionTreeWalker`
        that is reimplemented, since it manages the composition of
        ``abs`` with ``cos`` or ``sin``.

        INPUT:

        - ``ex`` -- a symbolic expression
        - ``operator`` -- an operator

        OUTPUT:

        - a symbolic expression, equivalent to ``ex`` with ``abs(cos(...))``
          and ``abs(sin(...))`` simplified, according to the range of their
          argument.

        EXAMPLES::

            sage: from sage.manifolds.utilities import SimplifyAbsTrig
            sage: assume(-pi/2 < x, x<0)
            sage: a = abs(sin(x))
            sage: s = SimplifyAbsTrig(a)
            sage: a.operator()
            abs
            sage: s.composition(a, a.operator())
            sin(-x)

        ::

            sage: a = exp(function('f')(x))  # no abs(sin_or_cos(...))
            sage: a.operator()
            exp
            sage: s.composition(a, a.operator())
            e^f(x)

        ::

            sage: forget()  # no longer any assumption on x
            sage: a = abs(cos(sin(x)))  # simplifiable since -1 <= sin(x) <= 1
            sage: s.composition(a, a.operator())
            cos(sin(x))
            sage: a = abs(sin(cos(x)))  # not simplifiable
            sage: s.composition(a, a.operator())
            abs(sin(cos(x)))
        """

def simplify_sqrt_real(expr):
    """
    Simplify ``sqrt`` in symbolic expressions in the real domain.

    EXAMPLES:

    Simplifications of basic expressions::

        sage: from sage.manifolds.utilities import simplify_sqrt_real
        sage: simplify_sqrt_real( sqrt(x^2) )
        abs(x)
        sage: assume(x<0)
        sage: simplify_sqrt_real( sqrt(x^2) )
        -x
        sage: simplify_sqrt_real( sqrt(x^2-2*x+1) )
        -x + 1
        sage: simplify_sqrt_real( sqrt(x^2) + sqrt(x^2-2*x+1) )
        -2*x + 1

    This improves over
    :meth:`~sage.symbolic.expression.Expression.canonicalize_radical`,
    which yields incorrect results when ``x < 0``::

        sage: forget()  # removes the assumption x<0
        sage: sqrt(x^2).canonicalize_radical()
        x
        sage: assume(x<0)
        sage: sqrt(x^2).canonicalize_radical()
        -x
        sage: sqrt(x^2-2*x+1).canonicalize_radical() # wrong output
        x - 1
        sage: ( sqrt(x^2) + sqrt(x^2-2*x+1) ).canonicalize_radical() # wrong output
        -1

    Simplification of nested ``sqrt``'s::

        sage: forget()  # removes the assumption x<0
        sage: simplify_sqrt_real( sqrt(1 + sqrt(x^2)) )
        sqrt(abs(x) + 1)
        sage: assume(x<0)
        sage: simplify_sqrt_real( sqrt(1 + sqrt(x^2)) )
        sqrt(-x + 1)
        sage: simplify_sqrt_real( sqrt(x^2 + sqrt(4*x^2) + 1) )
        -x + 1

    Again, :meth:`~sage.symbolic.expression.Expression.canonicalize_radical`
    fails on the last one::

        sage: (sqrt(x^2 + sqrt(4*x^2) + 1)).canonicalize_radical()
        x - 1

    TESTS:

    Simplification of expressions involving some symbolic derivatives::

        sage: f = function('f')
        sage: simplify_sqrt_real( diff(f(x), x)/sqrt(x^2-2*x+1) )  # x<0 => x-1<0
        -diff(f(x), x)/(x - 1)
        sage: g = function('g')
        sage: simplify_sqrt_real( sqrt(x^3*diff(f(g(x)), x)^2) )  # x<0
        (-x)^(3/2)*abs(D[0](f)(g(x)))*abs(diff(g(x), x))
        sage: forget()  # for doctests below
    """
def simplify_abs_trig(expr):
    """
    Simplify ``abs(sin(...))`` and ``abs(cos(...))`` in symbolic expressions.

    EXAMPLES::

        sage: M = Manifold(3, 'M', structure='topological')
        sage: X.<x,y,z> = M.chart(r'x y:(0,pi) z:(-pi/3,0)')
        sage: X.coord_range()
        x: (-oo, +oo); y: (0, pi); z: (-1/3*pi, 0)

    Since `x` spans all `\\RR`, no simplification of ``abs(sin(x))``
    occurs, while ``abs(sin(y))`` and ``abs(sin(3*z))`` are correctly
    simplified, given that `y \\in (0,\\pi)` and `z \\in (-\\pi/3,0)`::

        sage: from sage.manifolds.utilities import simplify_abs_trig
        sage: simplify_abs_trig( abs(sin(x)) + abs(sin(y)) + abs(sin(3*z)) )
        abs(sin(x)) + sin(y) + sin(-3*z)

    Note that neither
    :meth:`~sage.symbolic.expression.Expression.simplify_trig` nor
    :meth:`~sage.symbolic.expression.Expression.simplify_full`
    works in this case::

        sage: s = abs(sin(x)) + abs(sin(y)) + abs(sin(3*z))
        sage: s.simplify_trig()
        abs(4*cos(-z)^2 - 1)*abs(sin(-z)) + abs(sin(x)) + abs(sin(y))
        sage: s.simplify_full()
        abs(4*cos(-z)^2 - 1)*abs(sin(-z)) + abs(sin(x)) + abs(sin(y))

    despite the following assumptions hold::

        sage: assumptions()
        [x is real, y is real, y > 0, y < pi, z is real, z > -1/3*pi, z < 0]

    Additional checks are::

        sage: simplify_abs_trig( abs(sin(y/2)) )  # shall simplify
        sin(1/2*y)
        sage: simplify_abs_trig( abs(sin(2*y)) )  # must not simplify
        abs(sin(2*y))
        sage: simplify_abs_trig( abs(sin(z/2)) )  # shall simplify
        sin(-1/2*z)
        sage: simplify_abs_trig( abs(sin(4*z)) )  # must not simplify
        abs(sin(-4*z))

    Simplification of ``abs(cos(...))``::

        sage: forget()
        sage: M = Manifold(3, 'M', structure='topological')
        sage: X.<x,y,z> = M.chart(r'x y:(0,pi/2) z:(pi/4,3*pi/4)')
        sage: X.coord_range()
        x: (-oo, +oo); y: (0, 1/2*pi); z: (1/4*pi, 3/4*pi)
        sage: simplify_abs_trig( abs(cos(x)) + abs(cos(y)) + abs(cos(2*z)) )
        abs(cos(x)) + cos(y) - cos(2*z)

    Additional tests::

        sage: simplify_abs_trig(abs(cos(y-pi/2)))  # shall simplify
        cos(-1/2*pi + y)
        sage: simplify_abs_trig(abs(cos(y+pi/2)))  # shall simplify
        -cos(1/2*pi + y)
        sage: simplify_abs_trig(abs(cos(y-pi)))  # shall simplify
        -cos(-pi + y)
        sage: simplify_abs_trig(abs(cos(2*y)))  # must not simplify
        abs(cos(2*y))
        sage: simplify_abs_trig(abs(cos(y/2)) * abs(sin(z)))  # shall simplify
        cos(1/2*y)*sin(z)

    TESTS:

    Simplification of expressions involving some symbolic derivatives::

        sage: f = function('f')
        sage: s = abs(cos(x)) + abs(cos(y))*diff(f(x),x) + abs(cos(2*z))
        sage: simplify_abs_trig(s)
        cos(y)*diff(f(x), x) + abs(cos(x)) - cos(2*z)
        sage: s = abs(sin(x))*diff(f(x),x).subs(x=y^2) + abs(cos(y))
        sage: simplify_abs_trig(s)
        abs(sin(x))*D[0](f)(y^2) + cos(y)
        sage: forget()  # for doctests below
    """
def simplify_chain_real(expr):
    """
    Apply a chain of simplifications to a symbolic expression, assuming the
    real domain.

    This is the simplification chain used in calculus involving coordinate
    functions on real manifolds, as implemented in
    :class:`~sage.manifolds.chart_func.ChartFunction`.

    The chain is formed by the following functions, called
    successively:

    #. :meth:`~sage.symbolic.expression.Expression.simplify_factorial`
    #. :meth:`~sage.symbolic.expression.Expression.simplify_trig`
    #. :meth:`~sage.symbolic.expression.Expression.simplify_rational`
    #. :func:`simplify_sqrt_real`
    #. :func:`simplify_abs_trig`
    #. :meth:`~sage.symbolic.expression.Expression.canonicalize_radical`
    #. :meth:`~sage.symbolic.expression.Expression.simplify_log`
    #. :meth:`~sage.symbolic.expression.Expression.simplify_rational`
    #. :meth:`~sage.symbolic.expression.Expression.simplify_trig`

    EXAMPLES:

    We consider variables that are coordinates of a chart on a real manifold::

        sage: M = Manifold(2, 'M', structure='topological')
        sage: X.<x,y> = M.chart('x:(0,1) y')

    The following assumptions then hold::

        sage: assumptions()
        [x is real, x > 0, x < 1, y is real]

    and we have::

        sage: from sage.manifolds.utilities import simplify_chain_real
        sage: s = sqrt(y^2)
        sage: simplify_chain_real(s)
        abs(y)

    The above result is correct since ``y`` is real. It is obtained by
    :meth:`~sage.symbolic.expression.Expression.simplify_real` as well::

        sage: s.simplify_real()
        abs(y)
        sage: s.simplify_full()
        abs(y)

    Furthermore, we have::

        sage: s = sqrt(x^2-2*x+1)
        sage: simplify_chain_real(s)
        -x + 1

    which is correct since `x \\in (0,1)`. On this example, neither
    :meth:`~sage.symbolic.expression.Expression.simplify_real`
    nor :meth:`~sage.symbolic.expression.Expression.simplify_full`,
    nor :meth:`~sage.symbolic.expression.Expression.canonicalize_radical`
    give satisfactory results::

        sage: s.simplify_real()  # unsimplified output
        sqrt(x^2 - 2*x + 1)
        sage: s.simplify_full()  # unsimplified output
        sqrt(x^2 - 2*x + 1)
        sage: s.canonicalize_radical()  # wrong output since x in (0,1)
        x - 1

    Other simplifications::

        sage: s = abs(sin(pi*x))
        sage: simplify_chain_real(s)  # correct output since x in (0,1)
        sin(pi*x)
        sage: s.simplify_real()  # unsimplified output
        abs(sin(pi*x))
        sage: s.simplify_full()  # unsimplified output
        abs(sin(pi*x))

    ::

        sage: s = cos(y)^2 + sin(y)^2
        sage: simplify_chain_real(s)
        1
        sage: s.simplify_real()  # unsimplified output
        cos(y)^2 + sin(y)^2
        sage: s.simplify_full()  # OK
        1

    TESTS::

        sage: forget()  # for doctests below
    """
def simplify_chain_generic(expr):
    """
    Apply a chain of simplifications to a symbolic expression.

    This is the simplification chain used in calculus involving coordinate
    functions on manifolds over fields different from `\\RR`, as implemented in
    :class:`~sage.manifolds.chart_func.ChartFunction`.

    The chain is formed by the following functions, called
    successively:

    #. :meth:`~sage.symbolic.expression.Expression.simplify_factorial`
    #. :meth:`~sage.symbolic.expression.Expression.simplify_rectform`
    #. :meth:`~sage.symbolic.expression.Expression.simplify_trig`
    #. :meth:`~sage.symbolic.expression.Expression.simplify_rational`
    #. :meth:`~sage.symbolic.expression.Expression.expand_sum`

    NB: for the time being, this is identical to
    :meth:`~sage.symbolic.expression.Expression.simplify_full`.

    EXAMPLES:

    We consider variables that are coordinates of a chart on a complex
    manifold::

        sage: M = Manifold(2, 'M', structure='topological', field='complex')
        sage: X.<x,y> = M.chart()

    Then neither ``x`` nor ``y`` is assumed to be real::

        sage: assumptions()
        []

    Accordingly, ``simplify_chain_generic`` does not simplify
    ``sqrt(x^2)`` to ``abs(x)``::

        sage: from sage.manifolds.utilities import simplify_chain_generic
        sage: s = sqrt(x^2)
        sage: simplify_chain_generic(s)
        sqrt(x^2)

    This contrasts with the behavior of
    :func:`~sage.manifolds.utilities.simplify_chain_real`.

    Other simplifications::

        sage: s = (x+y)^2 - x^2 -2*x*y - y^2
        sage: simplify_chain_generic(s)
        0
        sage: s = (x^2 - 2*x + 1) / (x^2 -1)
        sage: simplify_chain_generic(s)
        (x - 1)/(x + 1)
        sage: s = cos(2*x) - 2*cos(x)^2 + 1
        sage: simplify_chain_generic(s)
        0

    TESTS::

        sage: forget()  # for doctests below
    """
def simplify_chain_generic_sympy(expr):
    """
    Apply a chain of simplifications to a sympy expression.

    This is the simplification chain used in calculus involving coordinate
    functions on manifolds over fields different from `\\RR`, as implemented in
    :class:`~sage.manifolds.chart_func.ChartFunction`.

    The chain is formed by the following functions, called
    successively:

    #. :meth:`~sympy.simplify.combsimp`
    #. :meth:`~sympy.simplify.trigsimp`
    #. :meth:`~sympy.core.expand`
    #. :meth:`~sympy.simplify.simplify`

    EXAMPLES:

    We consider variables that are coordinates of a chart on a complex
    manifold::

        sage: forget()  # for doctest only
        sage: M = Manifold(2, 'M', structure='topological', field='complex', calc_method='sympy')
        sage: X.<x,y> = M.chart()

    Then neither ``x`` nor ``y`` is assumed to be real::

        sage: assumptions()
        []

    Accordingly, ``simplify_chain_generic_sympy`` does not simplify
    ``sqrt(x^2)`` to ``abs(x)``::

        sage: from sage.manifolds.utilities import simplify_chain_generic_sympy
        sage: s = (sqrt(x^2))._sympy_()
        sage: simplify_chain_generic_sympy(s)
        sqrt(x**2)

    This contrasts with the behavior of
    :func:`~sage.manifolds.utilities.simplify_chain_real_sympy`.

    Other simplifications::

        sage: s = ((x+y)^2 - x^2 -2*x*y - y^2)._sympy_()
        sage: simplify_chain_generic_sympy(s)
        0
        sage: s = ((x^2 - 2*x + 1) / (x^2 -1))._sympy_()
        sage: simplify_chain_generic_sympy(s)
        (x - 1)/(x + 1)
        sage: s = (cos(2*x) - 2*cos(x)^2 + 1)._sympy_()
        sage: simplify_chain_generic_sympy(s)
        0
    """
def simplify_chain_real_sympy(expr):
    """
    Apply a chain of simplifications to a sympy expression, assuming the
    real domain.

    This is the simplification chain used in calculus involving coordinate
    functions on real manifolds, as implemented in
    :class:`~sage.manifolds.chart_func.ChartFunction`.

    The chain is formed by the following functions, called
    successively:

    #. :meth:`~sympy.simplify.combsimp`
    #. :meth:`~sympy.simplify.trigsimp`
    #. :func:`simplify_sqrt_real`
    #. :func:`simplify_abs_trig`
    #. :meth:`~sympy.core.expand`
    #. :meth:`~sympy.simplify.simplify`

    EXAMPLES:

    We consider variables that are coordinates of a chart on a real manifold::

        sage: forget()  # for doctest only
        sage: M = Manifold(2, 'M', structure='topological',calc_method='sympy')
        sage: X.<x,y> = M.chart('x:(0,1) y')

    The following assumptions then hold::

        sage: assumptions()
        [x is real, x > 0, x < 1, y is real]

    and we have::

        sage: from sage.manifolds.utilities import simplify_chain_real_sympy
        sage: s = (sqrt(y^2))._sympy_()
        sage: simplify_chain_real_sympy(s)
        Abs(y)

    Furthermore, we have::

        sage: s = (sqrt(x^2-2*x+1))._sympy_()
        sage: simplify_chain_real_sympy(s)
        1 - x

    Other simplifications::

        sage: s = (abs(sin(pi*x)))._sympy_()
        sage: simplify_chain_real_sympy(s)  # correct output since x in (0,1)
        sin(pi*x)

    ::

        sage: s = (cos(y)^2 + sin(y)^2)._sympy_()
        sage: simplify_chain_real_sympy(s)
        1
    """

class ExpressionNice(Expression):
    '''
    Subclass of :class:`~sage.symbolic.expression.Expression` for a
    "human-friendly" display of partial derivatives and the possibility to
    shorten the display by skipping the arguments of symbolic functions.

    INPUT:

    - ``ex`` -- symbolic expression

    EXAMPLES:

    An expression formed with callable symbolic expressions::

        sage: var(\'x y z\')
        (x, y, z)
        sage: f = function(\'f\')(x, y)
        sage: g = f.diff(y).diff(x)
        sage: h = function(\'h\')(y, z)
        sage: k = h.diff(z)
        sage: fun = x*g + y*(k-z)^2

    The standard Pynac display of partial derivatives::

        sage: fun
        y*(z - diff(h(y, z), z))^2 + x*diff(f(x, y), x, y)
        sage: latex(fun)
        y {\\left(z - \\frac{\\partial}{\\partial z}h\\left(y, z\\right)\\right)}^{2} + x \\frac{\\partial^{2}}{\\partial x\\partial y}f\\left(x, y\\right)

    With :class:`ExpressionNice`, the Pynac notation ``D[...]`` is replaced
    by textbook-like notation::

        sage: from sage.manifolds.utilities import ExpressionNice
        sage: ExpressionNice(fun)
        y*(z - d(h)/dz)^2 + x*d^2(f)/dxdy
        sage: latex(ExpressionNice(fun))
        y {\\left(z - \\frac{\\partial\\,h}{\\partial z}\\right)}^{2}
         + x \\frac{\\partial^2\\,f}{\\partial x\\partial y}

    An example when function variables are themselves functions::

        sage: f = function(\'f\')(x, y)
        sage: g = function(\'g\')(x, f)  # the second variable is the function f
        sage: fun = (g.diff(x))*x - x^2*f.diff(x,y)
        sage: fun
        -x^2*diff(f(x, y), x, y) + (diff(f(x, y), x)*D[1](g)(x, f(x, y)) + D[0](g)(x, f(x, y)))*x
        sage: ExpressionNice(fun)
        -x^2*d^2(f)/dxdy + (d(f)/dx*d(g)/d(f(x, y)) + d(g)/dx)*x
        sage: latex(ExpressionNice(fun))
        -x^{2} \\frac{\\partial^2\\,f}{\\partial x\\partial y}
         + {\\left(\\frac{\\partial\\,f}{\\partial x}
           \\frac{\\partial\\,g}{\\partial \\left( f\\left(x, y\\right) \\right)}
         + \\frac{\\partial\\,g}{\\partial x}\\right)} x

    Note that ``D[1](g)(x, f(x,y))`` is rendered as ``d(g)/d(f(x, y))``.

    An example with multiple differentiations::

        sage: fun = f.diff(x,x,y,y,x)*x
        sage: fun
        x*diff(f(x, y), x, x, x, y, y)
        sage: ExpressionNice(fun)
        x*d^5(f)/dx^3dy^2
        sage: latex(ExpressionNice(fun))
        x \\frac{\\partial^5\\,f}{\\partial x ^ 3\\partial y ^ 2}

    Parentheses are added around powers of partial derivatives to avoid any
    confusion::

        sage: fun = f.diff(y)^2
        sage: fun
        diff(f(x, y), y)^2
        sage: ExpressionNice(fun)
        (d(f)/dy)^2
        sage: latex(ExpressionNice(fun))
        \\left(\\frac{\\partial\\,f}{\\partial y}\\right)^{2}

    The explicit mention of function arguments can be omitted for the sake of
    brevity::

        sage: fun = fun*f
        sage: ExpressionNice(fun)
        f(x, y)*(d(f)/dy)^2
        sage: Manifold.options.omit_function_arguments=True
        sage: ExpressionNice(fun)
        f*(d(f)/dy)^2
        sage: latex(ExpressionNice(fun))
        f \\left(\\frac{\\partial\\,f}{\\partial y}\\right)^{2}
        sage: Manifold.options._reset()
        sage: ExpressionNice(fun)
        f(x, y)*(d(f)/dy)^2
        sage: latex(ExpressionNice(fun))
        f\\left(x, y\\right) \\left(\\frac{\\partial\\,f}{\\partial y}\\right)^{2}
    '''
    def __init__(self, ex) -> None:
        """
        Initialize ``self``.

        TESTS::

            sage: f = function('f')(x)
            sage: df = f.diff(x)
            sage: df
            diff(f(x), x)
            sage: from sage.manifolds.utilities import ExpressionNice
            sage: df_nice = ExpressionNice(df)
            sage: df_nice
            d(f)/dx
        """

def set_axes_labels(graph, xlabel, ylabel, zlabel, **kwds):
    """
    Set axes labels for a 3D graphics object ``graph``.

    This is a workaround for the lack of axes labels in 3D plots.
    This sets the labels as :func:`~sage.plot.plot3d.shapes2.text3d`
    objects at locations determined from the bounding box of the
    graphic object ``graph``.

    INPUT:

    - ``graph`` -- :class:`~sage.plot.plot3d.base.Graphics3d`;
      a 3D graphic object
    - ``xlabel`` -- string for the x-axis label
    - ``ylabel`` -- string for the y-axis label
    - ``zlabel`` -- string for the z-axis label
    - ``**kwds`` -- options (e.g. color) for text3d

    OUTPUT: the 3D graphic object with text3d labels added

    EXAMPLES::

        sage: # needs sage.plot
        sage: g = sphere()
        sage: g.all
        [Graphics3d Object]
        sage: from sage.manifolds.utilities import set_axes_labels
        sage: ga = set_axes_labels(g, 'X', 'Y', 'Z', color='red')
        sage: ga.all  # the 3D frame has now axes labels
        [Graphics3d Object, Graphics3d Object,
         Graphics3d Object, Graphics3d Object]
    """
def exterior_derivative(form):
    """
    Exterior derivative of a differential form.

    INPUT:

    - ``form`` -- a differential form; this must an instance of either

      * :class:`~sage.manifolds.differentiable.scalarfield.DiffScalarField`
        for a 0-form (scalar field)
      * :class:`~sage.manifolds.differentiable.diff_form.DiffFormParal` for
        a `p`-form (`p\\geq 1`) on a parallelizable manifold
      * :class:`~sage.manifolds.differentiable.diff_form.DiffForm` for a
        a `p`-form (`p\\geq 1`) on a non-parallelizable manifold

    OUTPUT:

    - the `(p+1)`-form that is the exterior derivative of ``form``

    EXAMPLES:

    Exterior derivative of a scalar field (0-form)::

        sage: from sage.manifolds.utilities import exterior_derivative
        sage: M = Manifold(3, 'M')
        sage: X.<x,y,z> = M.chart()
        sage: f = M.scalar_field({X: x+y^2+z^3}, name='f')
        sage: df = exterior_derivative(f); df
        1-form df on the 3-dimensional differentiable manifold M
        sage: df.display()
        df = dx + 2*y dy + 3*z^2 dz

    An alias is ``xder``::

        sage: from sage.manifolds.utilities import xder
        sage: df == xder(f)
        True

    Exterior derivative of a 1-form::

        sage: a = M.one_form(name='a')
        sage: a[:] = [x+y*z, x-y*z, x*y*z]
        sage: da = xder(a); da
        2-form da on the 3-dimensional differentiable manifold M
        sage: da.display()
        da = (-z + 1) dx∧dy + (y*z - y) dx∧dz + (x*z + y) dy∧dz
        sage: dda = xder(da); dda
        3-form dda on the 3-dimensional differentiable manifold M
        sage: dda.display()
        dda = 0

    .. SEEALSO::

        :class:`sage.manifolds.differentiable.diff_form.DiffFormParal.exterior_derivative`
        or :class:`sage.manifolds.differentiable.diff_form.DiffForm.exterior_derivative`
        for more examples.
    """
xder = exterior_derivative
