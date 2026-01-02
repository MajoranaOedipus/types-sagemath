r"""
Hypergeometric functions

This module implements manipulation of infinite hypergeometric series
represented in standard parametric form (as `\,_pF_q` functions).

AUTHORS:

- Fredrik Johansson (2010): initial version

- Eviatar Bach (2013): major changes

EXAMPLES:

Examples from :issue:`9908`::

    sage: # needs sage.symbolic
    sage: maxima('integrate(bessel_j(2, x), x)').sage()
    1/24*x^3*hypergeometric((3/2,), (5/2, 3), -1/4*x^2)
    sage: sum(((2*I)^x/(x^3 + 1)*(1/4)^x), x, 0, oo)
    hypergeometric((1, 1, -1/2*I*sqrt(3) - 1/2, 1/2*I*sqrt(3) - 1/2),...
    (2, -1/2*I*sqrt(3) + 1/2, 1/2*I*sqrt(3) + 1/2), 1/2*I)
    sage: res = sum((-1)^x/((2*x + 1)*factorial(2*x + 1)), x, 0, oo)
    sage: res                                   # not tested (depends on maxima version)
    hypergeometric((1/2,), (3/2, 3/2), -1/4)
    sage: res in [hypergeometric((1/2,), (3/2, 3/2), -1/4), sin_integral(1)]
    True

Simplification (note that ``simplify_full`` does not yet call
``simplify_hypergeometric``)::

    sage: # needs sage.symbolic
    sage: hypergeometric([-2], [], x).simplify_hypergeometric()
    x^2 - 2*x + 1
    sage: hypergeometric([], [], x).simplify_hypergeometric()
    e^x
    sage: a = hypergeometric((hypergeometric((), (), x),), (),
    ....:                    hypergeometric((), (), x))
    sage: a.simplify_hypergeometric()
    1/((-e^x + 1)^e^x)
    sage: a.simplify_hypergeometric(algorithm='sage')
    1/((-e^x + 1)^e^x)

Equality testing::

    sage: bool(hypergeometric([], [], x).derivative(x) ==                               # needs sage.symbolic
    ....:      hypergeometric([], [], x))  # diff(e^x, x) == e^x
    True
    sage: bool(hypergeometric([], [], x) == hypergeometric([], [1], x))                 # needs sage.symbolic
    False

Computing terms and series::

    sage: # needs sage.symbolic
    sage: var('z')
    z
    sage: hypergeometric([], [], z).series(z, 0)
    Order(1)
    sage: hypergeometric([], [], z).series(z, 1)
    1 + Order(z)
    sage: hypergeometric([], [], z).series(z, 2)
    1 + 1*z + Order(z^2)
    sage: hypergeometric([], [], z).series(z, 3)
    1 + 1*z + 1/2*z^2 + Order(z^3)

    sage: # needs sage.symbolic
    sage: hypergeometric([-2], [], z).series(z, 3)
    1 + (-2)*z + 1*z^2
    sage: hypergeometric([-2], [], z).series(z, 6)
    1 + (-2)*z + 1*z^2
    sage: hypergeometric([-2], [], z).series(z, 6).is_terminating_series()
    True
    sage: hypergeometric([-2], [], z).series(z, 2)
    1 + (-2)*z + Order(z^2)
    sage: hypergeometric([-2], [], z).series(z, 2).is_terminating_series()
    False

    sage: hypergeometric([1], [], z).series(z, 6)                                       # needs sage.symbolic
    1 + 1*z + 1*z^2 + 1*z^3 + 1*z^4 + 1*z^5 + Order(z^6)
    sage: hypergeometric([], [1/2], -z^2/4).series(z, 11)                               # needs sage.symbolic
    1 + (-1/2)*z^2 + 1/24*z^4 + (-1/720)*z^6 + 1/40320*z^8 +...
    (-1/3628800)*z^10 + Order(z^11)

    sage: hypergeometric([1], [5], x).series(x, 5)                                      # needs sage.symbolic
    1 + 1/5*x + 1/30*x^2 + 1/210*x^3 + 1/1680*x^4 + Order(x^5)

    sage: sum(hypergeometric([1, 2], [3], 1/3).terms(6)).n()                            # needs sage.symbolic
    1.29788359788360
    sage: hypergeometric([1, 2], [3], 1/3).n()                                          # needs sage.symbolic
    1.29837194594696
    sage: hypergeometric([], [], x).series(x, 20)(x=1).n() == e.n()                     # needs sage.symbolic
    True

Plotting::

    sage: # needs sage.symbolic
    sage: f(x) = hypergeometric([1, 1], [3, 3, 3], x)
    sage: plot(f, x, -30, 30)                                                           # needs sage.plot
    Graphics object consisting of 1 graphics primitive
    sage: g(x) = hypergeometric([x], [], 2)
    sage: complex_plot(g, (-1, 1), (-1, 1))                                             # needs sage.plot
    Graphics object consisting of 1 graphics primitive

Numeric evaluation::

    sage: # needs sage.symbolic
    sage: hypergeometric([1], [], 1/10).n()  # geometric series
    1.11111111111111
    sage: hypergeometric([], [], 1).n()  # e
    2.71828182845905
    sage: hypergeometric([], [], 3., hold=True)
    hypergeometric((), (), 3.00000000000000)
    sage: hypergeometric([1, 2, 3], [4, 5, 6], 1/2).n()
    1.02573619590134
    sage: hypergeometric([1, 2, 3], [4, 5, 6], 1/2).n(digits=30)
    1.02573619590133865036584139535
    sage: hypergeometric([5 - 3*I], [3/2, 2 + I, sqrt(2)], 4 + I).n()
    5.52605111678803 - 7.86331357527540*I
    sage: hypergeometric((10, 10), (50,), 2.)
    -1705.75733163554 - 356.749986056024*I

Conversions::

    sage: maxima(hypergeometric([1, 1, 1], [3, 3, 3], x))                               # needs sage.symbolic
    hypergeometric([1,1,1],[3,3,3],_SAGE_VAR_x)
    sage: hypergeometric((5,), (4,), 3)._sympy_()                                   # needs sympy sage.symbolic
    hyper((5,), (4,), 3)
    sage: hypergeometric((5, 4), (4, 4), 3)._mathematica_init_()                        # needs sage.symbolic
    'HypergeometricPFQ[{5,4},{4,4},3]'

Arbitrary level of nesting for conversions::

    sage: maxima(nest(lambda y: hypergeometric([y], [], x), 3, 1))                      # needs sage.symbolic
    1/(1-_SAGE_VAR_x)^(1/(1-_SAGE_VAR_x)^(1/(1-_SAGE_VAR_x)))
    sage: maxima(nest(lambda y: hypergeometric([y], [3], x), 3, 1))._sage_()            # needs sage.symbolic
    hypergeometric((hypergeometric((hypergeometric((1,), (3,), x),), (3,),...
    x),), (3,), x)
    sage: nest(lambda y: hypergeometric([y], [], x), 3, 1)._mathematica_init_()         # needs sage.symbolic
    'HypergeometricPFQ[{HypergeometricPFQ[{HypergeometricPFQ[{1},{},x]},...

The confluent hypergeometric functions can arise as solutions to second-order
differential equations (example from `here <http://ask.sagemath.org/question/
1168/how-can-one-use-maxima-kummer-confluent-functions>`_)::

    sage: var('m')                                                                      # needs sage.symbolic
    m
    sage: y = function('y')(x)                                                          # needs sage.symbolic
    sage: desolve(diff(y, x, 2) + 2*x*diff(y, x) - 4*m*y, y,                            # needs sage.symbolic
    ....:         contrib_ode=true, ivar=x)
    [y(x) == _K1*hypergeometric_M(-m, 1/2, -x^2) +...
     _K2*hypergeometric_U(-m, 1/2, -x^2)]

Series expansions of confluent hypergeometric functions::

    sage: hypergeometric_M(2, 2, x).series(x, 3)                                        # needs sage.symbolic
    1 + 1*x + 1/2*x^2 + Order(x^3)
    sage: hypergeometric_U(2, 2, x).series(x == 3, 100).subs(x=1).n()                   # needs sage.symbolic
    0.403652637676806
    sage: hypergeometric_U(2, 2, 1).n()                                                 # needs mpmath sage.symbolic
    0.403652637676806
"""

from collections.abc import Generator
from sage.arith.misc import binomial as binomial, factorial as factorial, rising_factorial as rising_factorial
from sage.calculus.functional import derivative as derivative
from sage.functions.error import erf as erf
from sage.functions.gamma import gamma as gamma
from sage.functions.hyperbolic import cosh as cosh, sinh as sinh
from sage.functions.log import exp as exp, log as log
from sage.functions.other import real_part as real_part, sqrt as sqrt
from sage.misc.lazy_import import lazy_import as lazy_import
from sage.misc.misc_c import prod as prod
from sage.rings.infinity import Infinity as Infinity
from sage.rings.integer import Integer as Integer
from sage.rings.integer_ring import ZZ as ZZ
from sage.rings.rational_field import QQ as QQ
from sage.structure.element import Expression as Expression, get_coercion_model as get_coercion_model
from sage.symbolic.function import BuiltinFunction as BuiltinFunction

def rational_param_as_tuple(x) -> tuple[int, int]:
    """
    Utility function for converting rational `\\,_pF_q` parameters to
    tuples (which mpmath handles more efficiently).

    EXAMPLES::

        sage: from sage.functions.hypergeometric import rational_param_as_tuple
        sage: rational_param_as_tuple(1/2)
        (1, 2)
        sage: rational_param_as_tuple(3)
        3
        sage: rational_param_as_tuple(pi)                                               # needs sage.symbolic
        pi
    """

class Hypergeometric(BuiltinFunction):
    """
    Represent a (formal) generalized infinite hypergeometric series.

    It is defined as

    .. MATH::

        \\,_pF_q(a_1, \\ldots, a_p; b_1, \\ldots, b_q; z)
        = \\sum_{n=0}^{\\infty} \\frac{(a_1)_n \\cdots (a_p)_n}{(b_1)_n
        \\cdots(b_q)_n} \\, \\frac{z^n}{n!},

    where `(x)_n` is the rising factorial.
    """
    def __init__(self) -> None:
        """
        Initialize class.

        EXAMPLES::

            sage: maxima(hypergeometric)                                                # needs sage.symbolic
            hypergeometric

        TESTS::

            sage: F = hypergeometric([-4,2],[1],1)  # optional - maple
            sage: G = maple(F); G                   # optional - maple
            hypergeom([-4, 2],[1],1)
            sage: G.simplify()                      # optional - maple
            0
        """
    def __call__(self, a, b, z, **kwargs):
        """
        Return symbolic hypergeometric function expression.

        INPUT:

        - ``a`` -- list or tuple of parameters
        - ``b`` -- list or tuple of parameters
        - ``z`` -- number or symbolic expression

        EXAMPLES::

            sage: # needs sage.symbolic
            sage: hypergeometric([], [], 1)
            hypergeometric((), (), 1)
            sage: hypergeometric([], [1], 1)
            hypergeometric((), (1,), 1)
            sage: hypergeometric([2, 3], [1], 1)
            hypergeometric((2, 3), (1,), 1)
            sage: hypergeometric([], [], x)
            hypergeometric((), (), x)
            sage: hypergeometric([x], [], x^2)
            hypergeometric((x,), (), x^2)

        The only simplification that is done automatically is returning 1
        if ``z`` is 0. For other simplifications use the
        ``simplify_hypergeometric`` method.

        TESTS::

            sage: hypergeometric([2, 3, 4], [4, 1], 1)
            hypergeometric((2, 3, 4), (4, 1), 1)
        """
    class EvaluationMethods:
        def sorted_parameters(self, a, b, z):
            """
            Return with parameters sorted in a canonical order.

            EXAMPLES::

                sage: hypergeometric([2, 1, 3], [5, 4],                                 # needs sage.symbolic
                ....:                1/2).sorted_parameters()
                hypergeometric((1, 2, 3), (4, 5), 1/2)
            """
        def eliminate_parameters(self, a, b, z):
            """
            Eliminate repeated parameters by pairwise cancellation of identical
            terms in ``a`` and ``b``.

            EXAMPLES::

                sage: hypergeometric([1, 1, 2, 5], [5, 1, 4],                           # needs sage.symbolic
                ....:                1/2).eliminate_parameters()
                hypergeometric((1, 2), (4,), 1/2)
                sage: hypergeometric([x], [x], x).eliminate_parameters()                # needs sage.symbolic
                hypergeometric((), (), x)
                sage: hypergeometric((5, 4), (4, 4), 3).eliminate_parameters()          # needs sage.symbolic
                hypergeometric((5,), (4,), 3)
            """
        def is_termwise_finite(self, a, b, z) -> bool:
            """
            Determine whether all terms of ``self`` are finite.

            Any infinite terms or ambiguous terms beyond the first
            zero, if one exists, are ignored.

            Ambiguous cases (where a term is the product of both zero
            and an infinity) are not considered finite.

            EXAMPLES::

                sage: # needs sage.symbolic
                sage: hypergeometric([2], [3, 4], 5).is_termwise_finite()
                True
                sage: hypergeometric([2], [-3, 4], 5).is_termwise_finite()
                False
                sage: hypergeometric([-2], [-3, 4], 5).is_termwise_finite()
                True
                sage: hypergeometric([-3], [-3, 4],
                ....:                5).is_termwise_finite()  # ambiguous
                False

                sage: # needs sage.symbolic
                sage: hypergeometric([0], [-1], 5).is_termwise_finite()
                True
                sage: hypergeometric([0], [0],
                ....:                5).is_termwise_finite()  # ambiguous
                False
                sage: hypergeometric([1], [2], Infinity).is_termwise_finite()
                False
                sage: (hypergeometric([0], [0], Infinity)
                ....:  .is_termwise_finite())  # ambiguous
                False
                sage: (hypergeometric([0], [], Infinity)
                ....:  .is_termwise_finite())  # ambiguous
                False
            """
        def is_terminating(self, a, b, z):
            """
            Determine whether the series represented by ``self`` terminates
            after a finite number of terms.

            This happens if any of the
            numerator parameters are nonnegative integers (with no
            preceding nonnegative denominator parameters), or `z = 0`.

            If terminating, the series represents a polynomial of `z`.

            EXAMPLES::

                sage: hypergeometric([1, 2], [3, 4], x).is_terminating()                # needs sage.symbolic
                False
                sage: hypergeometric([1, -2], [3, 4], x).is_terminating()               # needs sage.symbolic
                True
                sage: hypergeometric([1, -2], [], x).is_terminating()                   # needs sage.symbolic
                True
            """
        def is_absolutely_convergent(self, a, b, z):
            """
            Determine whether ``self`` converges absolutely as an infinite
            series. ``False`` is returned if not all terms are finite.

            EXAMPLES:

            Degree giving infinite radius of convergence::

                sage: hypergeometric([2, 3], [4, 5],                                    # needs sage.symbolic
                ....:                6).is_absolutely_convergent()
                True
                sage: hypergeometric([2, 3], [-4, 5],                                   # needs sage.symbolic
                ....:                6).is_absolutely_convergent()  # undefined
                False
                sage: (hypergeometric([2, 3], [-4, 5], Infinity)                        # needs sage.symbolic
                ....:  .is_absolutely_convergent())  # undefined
                False

            Ordinary geometric series (unit radius of convergence)::

                sage: # needs sage.symbolic
                sage: hypergeometric([1], [], 1/2).is_absolutely_convergent()
                True
                sage: hypergeometric([1], [], 2).is_absolutely_convergent()
                False
                sage: hypergeometric([1], [], 1).is_absolutely_convergent()
                False
                sage: hypergeometric([1], [], -1).is_absolutely_convergent()
                False
                sage: hypergeometric([1], [], -1).n()  # Sum still exists
                0.500000000000000

            Degree `p = q+1` (unit radius of convergence)::

                sage: # needs sage.symbolic
                sage: hypergeometric([2, 3], [4], 6).is_absolutely_convergent()
                False
                sage: hypergeometric([2, 3], [4], 1).is_absolutely_convergent()
                False
                sage: hypergeometric([2, 3], [5], 1).is_absolutely_convergent()
                False
                sage: hypergeometric([2, 3], [6], 1).is_absolutely_convergent()
                True
                sage: hypergeometric([-2, 3], [4],
                ....:                5).is_absolutely_convergent()
                True
                sage: hypergeometric([2, -3], [4],
                ....:                5).is_absolutely_convergent()
                True
                sage: hypergeometric([2, -3], [-4],
                ....:                5).is_absolutely_convergent()
                True
                sage: hypergeometric([2, -3], [-1],
                ....:                5).is_absolutely_convergent()
                False

            Degree giving zero radius of convergence::

                sage: hypergeometric([1, 2, 3], [4],                                    # needs sage.symbolic
                ....:                2).is_absolutely_convergent()
                False
                sage: hypergeometric([1, 2, 3], [4],                                    # needs sage.symbolic
                ....:                1/2).is_absolutely_convergent()
                False
                sage: (hypergeometric([1, 2, -3], [4], 1/2)                             # needs sage.symbolic
                ....:  .is_absolutely_convergent())  # polynomial
                True
            """
        def terms(self, a, b, z, n=None) -> Generator[Incomplete]:
            """
            Generate the terms of ``self`` (optionally only ``n`` terms).

            EXAMPLES::

                sage: list(hypergeometric([-2, 1], [3, 4], x).terms())                  # needs sage.symbolic
                [1, -1/6*x, 1/120*x^2]
                sage: list(hypergeometric([-2, 1], [3, 4], x).terms(2))                 # needs sage.symbolic
                [1, -1/6*x]
                sage: list(hypergeometric([-2, 1], [3, 4], x).terms(0))                 # needs sage.symbolic
                []
            """
        def deflated(self, a, b, z):
            """
            Rewrite as a linear combination of functions of strictly lower
            degree by eliminating all parameters ``a[i]`` and ``b[j]`` such
            that ``a[i]`` = ``b[i]`` + ``m`` for nonnegative integer ``m``.

            EXAMPLES::

                sage: # needs sage.symbolic
                sage: x = hypergeometric([6, 1], [3, 4, 5], 10)
                sage: y = x.deflated(); y
                1/252*hypergeometric((4,), (7, 8), 10)
                 + 1/12*hypergeometric((3,), (6, 7), 10)
                 + 1/2*hypergeometric((2,), (5, 6), 10)
                 + hypergeometric((1,), (4, 5), 10)
                sage: x.n(); y.n()
                2.87893612686782
                2.87893612686782

                sage: # needs sage.symbolic
                sage: x = hypergeometric([6, 7], [3, 4, 5], 10)
                sage: y = x.deflated(); y
                25/27216*hypergeometric((), (11,), 10)
                 + 25/648*hypergeometric((), (10,), 10)
                 + 265/504*hypergeometric((), (9,), 10)
                 + 181/63*hypergeometric((), (8,), 10)
                 + 19/3*hypergeometric((), (7,), 10)
                 + 5*hypergeometric((), (6,), 10)
                 + hypergeometric((), (5,), 10)
                sage: x.n(); y.n()
                63.0734110716969
                63.0734110716969
            """

hypergeometric: Hypergeometric

def closed_form(hyp):
    """
    Try to evaluate ``hyp`` in closed form using elementary
    (and other simple) functions.

    It may be necessary to call :meth:`Hypergeometric.deflated` first to
    find some closed forms.

    EXAMPLES::

        sage: # needs sage.symbolic
        sage: from sage.functions.hypergeometric import closed_form
        sage: var('a b c z')
        (a, b, c, z)
        sage: closed_form(hypergeometric([1], [], 1 + z))
        -1/z
        sage: closed_form(hypergeometric([], [], 1 + z))
        e^(z + 1)
        sage: closed_form(hypergeometric([], [1/2], 4))
        cosh(4)
        sage: closed_form(hypergeometric([], [3/2], 4))
        1/4*sinh(4)
        sage: closed_form(hypergeometric([], [5/2], 4))
        3/16*cosh(4) - 3/64*sinh(4)
        sage: closed_form(hypergeometric([], [-3/2], 4))
        19/3*cosh(4) - 4*sinh(4)
        sage: closed_form(hypergeometric([-3, 1], [var('a')], z))
        -3*z/a + 6*z^2/((a + 1)*a) - 6*z^3/((a + 2)*(a + 1)*a) + 1
        sage: closed_form(hypergeometric([-3, 1/3], [-4], z))
        7/162*z^3 + 1/9*z^2 + 1/4*z + 1
        sage: closed_form(hypergeometric([], [], z))
        e^z
        sage: closed_form(hypergeometric([a], [], z))
        1/((-z + 1)^a)
        sage: closed_form(hypergeometric([1, 1, 2], [1, 1], z))
        (z - 1)^(-2)
        sage: closed_form(hypergeometric([2, 3], [1], x))
        -1/(x - 1)^3 + 3*x/(x - 1)^4
        sage: closed_form(hypergeometric([1/2], [3/2], -5))
        1/10*sqrt(5)*sqrt(pi)*erf(sqrt(5))
        sage: closed_form(hypergeometric([2], [5], 3))
        4
        sage: closed_form(hypergeometric([2], [5], 5))
        48/625*e^5 + 612/625
        sage: closed_form(hypergeometric([1/2, 7/2], [3/2], z))
        1/5*z^2/(-z + 1)^(5/2) + 2/3*z/(-z + 1)^(3/2) + 1/sqrt(-z + 1)
        sage: closed_form(hypergeometric([1/2, 1], [2], z))
        -2*(sqrt(-z + 1) - 1)/z
        sage: closed_form(hypergeometric([1, 1], [2], z))
        -log(-z + 1)/z
        sage: closed_form(hypergeometric([1, 1], [3], z))
        -2*((z - 1)*log(-z + 1)/z - 1)/z
        sage: closed_form(hypergeometric([1, 1, 1], [2, 2], x))
        hypergeometric((1, 1, 1), (2, 2), x)
    """

class Hypergeometric_M(BuiltinFunction):
    '''
    The confluent hypergeometric function of the first kind,
    `y = M(a,b,z)`, is defined to be the solution to Kummer\'s differential
    equation

    .. MATH::

        zy\'\' + (b-z)y\' - ay = 0.

    This is not the same as Kummer\'s `U`-hypergeometric function, though it
    satisfies the same DE that `M` does.

    .. warning::

        In the literature, both are called "Kummer confluent
        hypergeometric" functions.

    EXAMPLES::


        sage: hypergeometric_M(1, 1, 1.)                                                # needs mpmath
        2.71828182845905

        sage: # needs sage.symbolic
        sage: hypergeometric_M(1, 1, 1)
        hypergeometric_M(1, 1, 1)
        sage: hypergeometric_M(1, 1, 1).n(70)                                           # needs mpmath
        2.7182818284590452354
        sage: hypergeometric_M(1, 1, 1).simplify_hypergeometric()
        e
        sage: hypergeometric_M(1, 3/2, 1).simplify_hypergeometric()
        1/2*sqrt(pi)*erf(1)*e
        sage: hypergeometric_M(1, 1/2, x).simplify_hypergeometric()
        (-I*sqrt(pi)*x*erf(I*sqrt(-x))*e^x + sqrt(-x))/sqrt(-x)
    '''
    def __init__(self) -> None:
        """
        TESTS::

            sage: maxima(hypergeometric_M(1,1,x))                                       # needs sage.symbolic
            kummer_m(1,1,_SAGE_VAR_x)
            sage: latex(hypergeometric_M(1,1,x))                                        # needs sage.symbolic
            M\\left(1, 1, x\\right)
        """
    class EvaluationMethods:
        def generalized(self, a, b, z):
            """
            Return as a generalized hypergeometric function.

            EXAMPLES::

                sage: var('a b z')                                                      # needs sage.symbolic
                (a, b, z)
                sage: hypergeometric_M(a, b, z).generalized()                           # needs sage.symbolic
                hypergeometric((a,), (b,), z)
            """

hypergeometric_M: Hypergeometric_M

class Hypergeometric_U(BuiltinFunction):
    '''
    The confluent hypergeometric function of the second kind,
    `y = U(a,b,z)`, is defined to be the solution to Kummer\'s differential
    equation

    .. MATH::

             zy\'\' + (b-z)y\' - ay = 0.

    This satisfies `U(a,b,z) \\sim z^{-a}`, as
    `z\\rightarrow \\infty`, and is sometimes denoted
    `z^{-a}{}_2F_0(a,1+a-b;;-1/z)`. This is not the same as Kummer\'s
    `M`-hypergeometric function, denoted sometimes as
    `_1F_1(\\alpha,\\beta,z)`, though it satisfies the same DE that
    `U` does.

    .. warning::

       In the literature, both are called "Kummer confluent
       hypergeometric" functions.

    EXAMPLES::

        sage: # needs mpmath
        sage: hypergeometric_U(1, 1, 1)
        hypergeometric_U(1, 1, 1)
        sage: hypergeometric_U(1, 1, 1.)
        0.596347362323194

        sage: # needs sage.symbolic
        sage: hypergeometric_U(1, 1, 1).n(70)                                           # needs mpmath
        0.59634736232319407434
        sage: hypergeometric_U(10^4, 1/3, 1).n()                                        # needs sage.libs.pari
        6.60377008885811e-35745
        sage: hypergeometric_U(1, 2, 2).simplify_hypergeometric()
        1/2

        sage: hypergeometric_U(2 + I, 2, 1).n()                                         # needs sage.symbolic
        0.183481989942099 - 0.458685959185190*I
        sage: hypergeometric_U(1, 3, x).simplify_hypergeometric()                       # needs sage.symbolic
        (x + 1)/x^2
    '''
    def __init__(self) -> None:
        """
        TESTS::

            sage: maxima(hypergeometric_U(1, 1, x))                                     # needs sage.symbolic
            kummer_u(1,1,_SAGE_VAR_x)
            sage: latex(hypergeometric_U(1, 1, x))                                      # needs sage.symbolic
            U\\left(1, 1, x\\right)
        """
    class EvaluationMethods:
        def generalized(self, a, b, z):
            """
            Return in terms of the generalized hypergeometric function.

            EXAMPLES::

                sage: # needs sage.symbolic
                sage: var('a b z')
                (a, b, z)
                sage: hypergeometric_U(a, b, z).generalized()
                hypergeometric((a, a - b + 1), (), -1/z)/z^a
                sage: hypergeometric_U(1, 3, 1/2).generalized()
                2*hypergeometric((1, -1), (), -2)
                sage: hypergeometric_U(3, I, 2).generalized()
                1/8*hypergeometric((3, -I + 4), (), -1/2)
            """

hypergeometric_U: Hypergeometric_U
