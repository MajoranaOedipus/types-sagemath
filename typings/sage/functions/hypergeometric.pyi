from _typeshed import Incomplete
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

def rational_param_as_tuple(x):
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

hypergeometric: Incomplete

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

hypergeometric_M: Incomplete

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

hypergeometric_U: Incomplete
