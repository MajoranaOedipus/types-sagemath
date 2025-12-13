from _typeshed import Incomplete
from sage.arith.misc import rising_factorial as rising_factorial
from sage.misc.lazy_import import lazy_import as lazy_import
from sage.misc.superseded import deprecated_function_alias as deprecated_function_alias
from sage.rings.integer_ring import ZZ as ZZ
from sage.rings.rational_field import QQ as QQ
from sage.structure.element import Expression as Expression, parent as parent
from sage.symbolic.function import BuiltinFunction as BuiltinFunction, GinacFunction as GinacFunction

class OrthogonalFunction(BuiltinFunction):
    """
    Base class for orthogonal polynomials.

    This class is an abstract base class for all orthogonal polynomials since
    they share similar properties. The evaluation as a polynomial
    is either done via maxima, or with pynac.

    Convention: The first argument is always the order of the polynomial,
    the others are other values or parameters where the polynomial is
    evaluated.
    """
    def __init__(self, name, nargs: int = 2, latex_name=None, conversions=None) -> None:
        """
        :class:`OrthogonalFunction` class needs the same input parameter as
        its parent class.

        EXAMPLES::

            sage: from sage.functions.orthogonal_polys import OrthogonalFunction
            sage: new = OrthogonalFunction('testo_P')
            sage: new
            testo_P
        """
    def eval_formula(self, *args) -> None:
        """
        Evaluate this polynomial using an explicit formula.

        EXAMPLES::

            sage: from sage.functions.orthogonal_polys import OrthogonalFunction
            sage: P = OrthogonalFunction('testo_P')
            sage: P.eval_formula(1, 2.0)
            Traceback (most recent call last):
            ...
            NotImplementedError: no explicit calculation of values implemented
        """
    def __call__(self, *args, **kwds):
        """
        This overrides the call method from SageObject to avoid
        problems with coercions, since the _eval_ method is able to
        handle more data types than symbolic functions would normally
        allow.

        Thus we have the distinction between algebraic objects (if n is an integer),
        and else as symbolic function.

        EXAMPLES::

            sage: # needs sage.symbolic
            sage: chebyshev_T(5, x)
            16*x^5 - 20*x^3 + 5*x
            sage: chebyshev_T(5, x, algorithm='pari')                                   # needs sage.libs.pari
            16*x^5 - 20*x^3 + 5*x
            sage: chebyshev_T(5, x, algorithm='maxima')
            16*x^5 - 20*x^3 + 5*x
            sage: chebyshev_T(5, x, algorithm='recursive')
            16*x^5 - 20*x^3 + 5*x
        """

class ChebyshevFunction(OrthogonalFunction):
    """
    Abstract base class for Chebyshev polynomials of the first and second kind.

    EXAMPLES::

        sage: chebyshev_T(3, x)                                                         # needs sage.symbolic
        4*x^3 - 3*x
    """
    def __call__(self, n, *args, **kwds):
        """
        This overrides the call method from :class:`SageObject` to
        avoid problems with coercions, since the ``_eval_`` method is
        able to handle more data types than symbolic functions would
        normally allow.

        Thus we have the distinction between algebraic objects (if n is an integer),
        and else as symbolic function.

        EXAMPLES::

            sage: x = polygen(QQ, 'x')
            sage: K.<a> = NumberField(x^3 - x - 1)                                      # needs sage.rings.number_field
            sage: chebyshev_T(5, a)                                                     # needs sage.rings.number_field
            16*a^2 + a - 4
            sage: chebyshev_T(5, MatrixSpace(ZZ, 2)([1, 2, -4, 7]))                     # needs sage.modules
            [-40799  44162]
            [-88324  91687]
            sage: R.<x> = QQ[]
            sage: parent(chebyshev_T(5, x))
            Univariate Polynomial Ring in x over Rational Field
            sage: chebyshev_T(5, 2, hold=True)                                          # needs sage.symbolic
            chebyshev_T(5, 2)
            sage: chebyshev_T(1, 2, 3)
            Traceback (most recent call last):
            ...
            TypeError: Symbolic function chebyshev_T takes exactly 2 arguments (3 given)
        """

class Func_chebyshev_T(ChebyshevFunction):
    """
    Chebyshev polynomials of the first kind.

    REFERENCE:

    - [AS1964]_ 22.5.31 page 778 and 6.1.22 page 256.

    EXAMPLES::

       sage: chebyshev_T(5, x)                                                          # needs sage.symbolic
       16*x^5 - 20*x^3 + 5*x
       sage: var('k')                                                                   # needs sage.symbolic
       k
       sage: test = chebyshev_T(k, x); test                                             # needs sage.symbolic
       chebyshev_T(k, x)
    """
    def __init__(self) -> None:
        """
        Init method for the chebyshev polynomials of the first kind.

        EXAMPLES::

            sage: # needs sage.symbolic
            sage: var('n, x')
            (n, x)
            sage: from sage.functions.orthogonal_polys import Func_chebyshev_T
            sage: chebyshev_T2 = Func_chebyshev_T()
            sage: chebyshev_T2(1, x)
            x
            sage: chebyshev_T(x, x)._sympy_()                                           # needs sympy
            chebyshevt(x, x)
            sage: maxima(chebyshev_T(1, x, hold=True))
            _SAGE_VAR_x
            sage: maxima(chebyshev_T(n, chebyshev_T(n, x)))
            chebyshev_t(_SAGE_VAR_n,chebyshev_t(_SAGE_VAR_n,_SAGE_VAR_x))
        """
    def eval_formula(self, n, x):
        """
        Evaluate ``chebyshev_T`` using an explicit formula.
        See [AS1964]_ 227 (p. 782) for details for the recursions.
        See also [Koe1999]_ for fast evaluation techniques.

        INPUT:

        - ``n`` -- integer

        - ``x`` -- a value to evaluate the polynomial at (this can be
          any ring element)

        EXAMPLES::

            sage: # needs sage.symbolic
            sage: chebyshev_T.eval_formula(-1, x)
            x
            sage: chebyshev_T.eval_formula(0, x)
            1
            sage: chebyshev_T.eval_formula(1, x)
            x
            sage: chebyshev_T.eval_formula(10, x)
            512*x^10 - 1280*x^8 + 1120*x^6 - 400*x^4 + 50*x^2 - 1
            sage: chebyshev_T.eval_algebraic(10, x).expand()
            512*x^10 - 1280*x^8 + 1120*x^6 - 400*x^4 + 50*x^2 - 1

            sage: chebyshev_T.eval_formula(2, 0.1) == chebyshev_T._evalf_(2, 0.1)       # needs sage.rings.complex_double
            True
        """
    def eval_algebraic(self, n, x):
        """
        Evaluate :class:`chebyshev_T` as polynomial, using a recursive
        formula.

        INPUT:

        - ``n`` -- integer

        - ``x`` -- a value to evaluate the polynomial at (this can be
          any ring element)

        EXAMPLES::

            sage: chebyshev_T.eval_algebraic(5, x)                                      # needs sage.symbolic
            2*(2*(2*x^2 - 1)*x - x)*(2*x^2 - 1) - x
            sage: chebyshev_T(-7, x) - chebyshev_T(7, x)                                # needs sage.symbolic
            0
            sage: R.<t> = ZZ[]
            sage: chebyshev_T.eval_algebraic(-1, t)
            t
            sage: chebyshev_T.eval_algebraic(0, t)
            1
            sage: chebyshev_T.eval_algebraic(1, t)
            t
            sage: chebyshev_T(7^100, 1/2)
            1/2
            sage: chebyshev_T(7^100, Mod(2,3))
            2
            sage: n = 97; x = RIF(pi/2/n)                                               # needs sage.symbolic
            sage: chebyshev_T(n, cos(x)).contains_zero()                                # needs sage.symbolic
            True

            sage: # needs sage.rings.padics
            sage: R.<t> = Zp(2, 8, 'capped-abs')[]
            sage: chebyshev_T(10^6 + 1, t)
            (2^7 + O(2^8))*t^5 + O(2^8)*t^4 + (2^6 + O(2^8))*t^3 + O(2^8)*t^2
             + (1 + 2^6 + O(2^8))*t + O(2^8)
        """

chebyshev_T: Incomplete

class Func_chebyshev_U(ChebyshevFunction):
    """
    Class for the Chebyshev polynomial of the second kind.

    REFERENCE:

    - [AS1964]_ 22.8.3 page 783 and 6.1.22 page 256.

    EXAMPLES::

        sage: R.<t> = QQ[]
        sage: chebyshev_U(2, t)
        4*t^2 - 1
        sage: chebyshev_U(3, t)
        8*t^3 - 4*t
    """
    def __init__(self) -> None:
        """
        Init method for the chebyshev polynomials of the second kind.

        EXAMPLES::

            sage: # needs sage.symbolic
            sage: var('n, x')
            (n, x)
            sage: from sage.functions.orthogonal_polys import Func_chebyshev_U
            sage: chebyshev_U2 = Func_chebyshev_U()
            sage: chebyshev_U2(1, x)
            2*x
            sage: chebyshev_U(x, x)._sympy_()                                           # needs sympy
            chebyshevu(x, x)
            sage: maxima(chebyshev_U(2,x, hold=True))
            3*(...-...(8*(1-_SAGE_VAR_x))/3)+(4*(1-_SAGE_VAR_x)^2)/3+1)
            sage: maxima(chebyshev_U(n,x, hold=True))
            chebyshev_u(_SAGE_VAR_n,_SAGE_VAR_x)
        """
    def eval_formula(self, n, x):
        """
        Evaluate ``chebyshev_U`` using an explicit formula.

        See [AS1964]_ 227 (p. 782) for details on the recursions.
        See also [Koe1999]_ for the recursion formulas.

        INPUT:

        - ``n`` -- integer

        - ``x`` -- a value to evaluate the polynomial at (this can be
          any ring element)

        EXAMPLES::

            sage: # needs sage.symbolic
            sage: chebyshev_U.eval_formula(10, x)
            1024*x^10 - 2304*x^8 + 1792*x^6 - 560*x^4 + 60*x^2 - 1
            sage: chebyshev_U.eval_formula(-2, x)
            -1
            sage: chebyshev_U.eval_formula(-1, x)
            0
            sage: chebyshev_U.eval_formula(0, x)
            1
            sage: chebyshev_U.eval_formula(1, x)
            2*x
            sage: chebyshev_U.eval_formula(2, 0.1) == chebyshev_U._evalf_(2, 0.1)
            True
        """
    def eval_algebraic(self, n, x):
        """
        Evaluate :class:`chebyshev_U` as polynomial, using a recursive
        formula.

        INPUT:

        - ``n`` -- integer

        - ``x`` -- a value to evaluate the polynomial at (this can be
          any ring element)

        EXAMPLES::

            sage: chebyshev_U.eval_algebraic(5, x)                                      # needs sage.symbolic
            -2*((2*x + 1)*(2*x - 1)*x - 4*(2*x^2 - 1)*x)*(2*x + 1)*(2*x - 1)
            sage: parent(chebyshev_U(3, Mod(8,9)))
            Ring of integers modulo 9
            sage: parent(chebyshev_U(3, Mod(1,9)))
            Ring of integers modulo 9
            sage: chebyshev_U(-3, x) + chebyshev_U(1, x)                                # needs sage.symbolic
            0
            sage: chebyshev_U(-1, Mod(5,8))
            0
            sage: parent(chebyshev_U(-1, Mod(5,8)))
            Ring of integers modulo 8
            sage: R.<t> = ZZ[]
            sage: chebyshev_U.eval_algebraic(-2, t)
            -1
            sage: chebyshev_U.eval_algebraic(-1, t)
            0
            sage: chebyshev_U.eval_algebraic(0, t)
            1
            sage: chebyshev_U.eval_algebraic(1, t)
            2*t
            sage: n = 97; x = RIF(pi/n)                                                 # needs sage.symbolic
            sage: chebyshev_U(n - 1, cos(x)).contains_zero()                            # needs sage.symbolic
            True

            sage: # needs sage.rings.padics
            sage: R.<t> = Zp(2, 6, 'capped-abs')[]
            sage: chebyshev_U(10^6 + 1, t)
            (2 + O(2^6))*t + O(2^6)
        """

chebyshev_U: Incomplete

class Func_legendre_P(GinacFunction):
    '''
    EXAMPLES::

        sage: # needs sage.symbolic
        sage: legendre_P(4, 2.0)
        55.3750000000000
        sage: legendre_P(1, x)
        x
        sage: legendre_P(4, x + 1)
        35/8*(x + 1)^4 - 15/4*(x + 1)^2 + 3/8
        sage: legendre_P(1/2, I+1.)
        1.05338240025858 + 0.359890322109665*I
        sage: legendre_P(0, SR(1)).parent()
        Symbolic Ring

        sage: legendre_P(0, 0)                                                          # needs sage.symbolic
        1
        sage: legendre_P(1, x)                                                          # needs sage.symbolic
        x

        sage: # needs sage.symbolic
        sage: legendre_P(4, 2.)
        55.3750000000000
        sage: legendre_P(5.5, 1.00001)
        1.00017875754114
        sage: legendre_P(1/2, I + 1).n()
        1.05338240025858 + 0.359890322109665*I
        sage: legendre_P(1/2, I + 1).n(59)
        1.0533824002585801 + 0.35989032210966539*I
        sage: legendre_P(42, RR(12345678))
        2.66314881466753e309
        sage: legendre_P(42, Reals(20)(12345678))
        2.6632e309
        sage: legendre_P(201/2, 0).n()
        0.0561386178630179
        sage: legendre_P(201/2, 0).n(100)
        0.056138617863017877699963095883

        sage: # needs sage.symbolic
        sage: R.<x> = QQ[]
        sage: legendre_P(4, x)
        35/8*x^4 - 15/4*x^2 + 3/8
        sage: legendre_P(10000, x).coefficient(x, 1)
        0
        sage: var(\'t,x\')
        (t, x)
        sage: legendre_P(-5, t)
        35/8*t^4 - 15/4*t^2 + 3/8
        sage: legendre_P(4, x + 1)
        35/8*(x + 1)^4 - 15/4*(x + 1)^2 + 3/8
        sage: legendre_P(4, sqrt(2))
        83/8
        sage: legendre_P(4, I*e)
        35/8*e^4 + 15/4*e^2 + 3/8

        sage: # needs sage.symbolic
        sage: n = var(\'n\')
        sage: derivative(legendre_P(n,x), x)
        (n*x*legendre_P(n, x) - n*legendre_P(n - 1, x))/(x^2 - 1)
        sage: derivative(legendre_P(3,x), x)
        15/2*x^2 - 3/2
        sage: derivative(legendre_P(n,x), n)
        Traceback (most recent call last):
        ...
        RuntimeError: derivative w.r.t. to the index is not supported yet

    TESTS:

    Verify that :issue:`33962` is fixed::

        sage: [legendre_P(n, 0) for n in range(-10, 10)]                                # needs sage.symbolic
        [0, 35/128, 0, -5/16, 0, 3/8, 0, -1/2, 0, 1,
         1, 0, -1/2, 0, 3/8, 0, -5/16, 0, 35/128, 0]

    Verify that :issue:`33963` is fixed::

        sage: # needs sage.symbolic
        sage: n = var("n")
        sage: assume(n, "integer")
        sage: assume(n, "even")
        sage: legendre_P(n, 0)
        2^(-n + 2)*(-1)^(1/2*n)*gamma(n)/(n*gamma(1/2*n)^2)
        sage: forget()
    '''
    def __init__(self) -> None:
        """
        Init method for the Legendre polynomials of the first kind.

        EXAMPLES::

            sage: loads(dumps(legendre_P))
            legendre_P
        """

legendre_P: Incomplete

class Func_legendre_Q(BuiltinFunction):
    def __init__(self) -> None:
        """
        EXAMPLES::

            sage: loads(dumps(legendre_Q))
            legendre_Q
            sage: maxima(legendre_Q(20, x, hold=True))._sage_().coefficient(x, 10)      # needs sage.symbolic
            -29113619535/131072*log(-(x + 1)/(x - 1))
        """
    def eval_recursive(self, n, arg, **kwds):
        """
        Return expanded Legendre Q(n, arg) function expression.

        EXAMPLES::

            sage: legendre_Q.eval_recursive(2, x)                                       # needs sage.symbolic
            3/4*x^2*(log(x + 1) - log(-x + 1)) - 3/2*x - 1/4*log(x + 1) + 1/4*log(-x + 1)
            sage: legendre_Q.eval_recursive(20, x).expand().coefficient(x, 10)          # needs sage.symbolic
            -29113619535/131072*log(x + 1) + 29113619535/131072*log(-x + 1)
        """
    def eval_formula(self, n, arg, **kwds):
        """
        Return expanded Legendre ``Q(n, arg)`` function expression.

        REFERENCE:

        - T. M. Dunster, Legendre and Related Functions, https://dlmf.nist.gov/14.7#E2

        EXAMPLES::

            sage: # needs sage.symbolic
            sage: legendre_Q.eval_formula(1, x)
            1/2*x*(log(x + 1) - log(-x + 1)) - 1
            sage: legendre_Q.eval_formula(2, x).expand().collect(log(1+x)).collect(log(1-x))
            1/4*(3*x^2 - 1)*log(x + 1) - 1/4*(3*x^2 - 1)*log(-x + 1) - 3/2*x
            sage: legendre_Q.eval_formula(20, x).coefficient(x, 10)
            -29113619535/131072*log(x + 1) + 29113619535/131072*log(-x + 1)
            sage: legendre_Q(0, 2)
            -1/2*I*pi + 1/2*log(3)

            sage: legendre_Q(0, 2.)                                                     # needs mpmath
            0.549306144334055 - 1.57079632679490*I
        """

legendre_Q: Incomplete

class Func_assoc_legendre_P(BuiltinFunction):
    '''
    Return the Ferrers function `\\mathtt{P}_n^m(x)` of first kind for
    `x \\in (-1,1)` with general order `m` and general degree `n`.

    Ferrers functions of first kind are one of two linearly independent
    solutions of the associated Legendre differential equation

    .. MATH::

        (1-x^2) \\frac{\\mathrm{d}^2 w}{\\mathrm{d}x^2} -
            2x \\frac{\\mathrm{d} w}{\\mathrm{d}x} +
            \\left(n(n+1) - \\frac{m^2}{1-x^2}\\right) w = 0

    on the interval `x \\in (-1, 1)` and are usually denoted by
    `\\mathtt{P}_n^m(x)`.

    .. SEEALSO ::

        The other linearly independent solution is called *Ferrers function of
        second kind* and denoted by `\\mathtt{Q}_n^m(x)`,
        see :class:`Func_assoc_legendre_Q`.

    .. WARNING::

        Ferrers functions must be carefully distinguished from associated
        Legendre functions which are defined on `\\CC \\setminus (- \\infty, 1]`
        and have not yet been implemented.

    EXAMPLES:

    We give the first Ferrers functions for nonnegative integers
    `n` and `m` in the interval `-1<x<1`::

        sage: for n in range(4):                                                        # needs sage.symbolic
        ....:     for m in range(n+1):
        ....:         print(f"P_{n}^{m}({x}) = {gen_legendre_P(n, m, x)}")
        P_0^0(x) = 1
        P_1^0(x) = x
        P_1^1(x) = -sqrt(-x^2 + 1)
        P_2^0(x) = 3/2*x^2 - 1/2
        P_2^1(x) = -3*sqrt(-x^2 + 1)*x
        P_2^2(x) = -3*x^2 + 3
        P_3^0(x) = 5/2*x^3 - 3/2*x
        P_3^1(x) = -3/2*(5*x^2 - 1)*sqrt(-x^2 + 1)
        P_3^2(x) = -15*(x^2 - 1)*x
        P_3^3(x) = -15*(-x^2 + 1)^(3/2)

    These expressions for nonnegative integers are computed by the
    Rodrigues-type given in :meth:`eval_gen_poly`. Negative values for `n` are
    obtained by the following identity:

    .. MATH::

        P^{m}_{-n}(x) = P^{m}_{n-1}(x).

    For `n` being a nonnegative integer, negative values for `m` are
    obtained by

    .. MATH::

        P^{-|m|}_n(x) = (-1)^{|m|} \\frac{(n-|m|)!}{(n+|m|)!} P_n^{|m|}(x),

    where `|m| \\leq n`.

    Here are some specific values with negative integers::

        sage: # needs sage.symbolic
        sage: gen_legendre_P(-2, -1, x)
        1/2*sqrt(-x^2 + 1)
        sage: gen_legendre_P(2, -2, x)
        -1/8*x^2 + 1/8
        sage: gen_legendre_P(3, -2, x)
        -1/8*(x^2 - 1)*x
        sage: gen_legendre_P(1, -2, x)
        0

    Here are some other random values with floating numbers::

        sage: # needs sage.symbolic
        sage: m = var(\'m\'); assume(m, \'integer\')
        sage: gen_legendre_P(m, m, .2)
        0.960000000000000^(1/2*m)*(-1)^m*factorial(2*m)/(2^m*factorial(m))
        sage: gen_legendre_P(.2, m, 0)
        sqrt(pi)*2^m/(gamma(-1/2*m + 1.10000000000000)*gamma(-1/2*m + 0.400000000000000))
        sage: gen_legendre_P(.2, .2, .2)
        0.757714892929573

    TESTS:

    Some consistency checks::

        sage: gen_legendre_P(1, 1, x)                                                   # needs sage.symbolic
        -sqrt(-x^2 + 1)
        sage: gen_legendre_P.eval_gen_poly(1, 1, x)                                     # needs sage.symbolic
        -sqrt(-x^2 + 1)
        sage: gen_legendre_P(1, 1, 0.5)  # abs tol 1e-14                                # needs mpmath
        -0.866025403784439
        sage: gen_legendre_P.eval_gen_poly(1, 1, 0.5)  # abs tol 1e-14                  # needs sage.rings.real_mpfr
        -0.866025403784439
        sage: gen_legendre_P._evalf_(1, 1, 0.5)  # abs tol 1e-14                        # needs mpmath
        -0.866025403784439
        sage: gen_legendre_P(2/3, 1, 0.)  # abs tol 1e-14                               # needs mpmath
        -0.773063511309286
        sage: gen_legendre_P._eval_special_values_(2/3, 1, 0.).n()  # abs tol 1e-14     # needs sage.symbolic
        -0.773063511309286

    REFERENCES:

    - [DLMF-Legendre]_
    '''
    def __init__(self) -> None:
        """
        EXAMPLES::

            sage: loads(dumps(gen_legendre_P))
            gen_legendre_P
            sage: maxima(gen_legendre_P(20, 6, x, hold=True))._sage_().expand().coefficient(x,10)   # needs sage.symbolic
            2508866163428625/128

        TESTS::

            sage: fricas(gen_legendre_P(2, 1/2, x))                             # optional - fricas, needs sage.symbolic
                        1
            legendreP(2,-,x)
                        2

            sage: gen_legendre_P(3, 0, x)                                               # needs sage.symbolic
            5/2*x^3 - 3/2*x
            sage: fricas.legendreP(3, x)                                        # optional - fricas, needs sage.symbolic
            5  3   3
            - x  - - x
            2      2
        """
    def eval_gen_poly(self, n, m, arg, **kwds):
        """
        Return the Ferrers function of first kind `\\mathtt{P}_n^m(x)` for
        integers `n > -1, m > -1` given by the following Rodrigues-type
        formula:

        .. MATH::

            \\mathtt{P}_n^m(x) = (-1)^{m+n} \\frac{(1-x^2)^{m/2}}{2^n n!}
                \\frac{\\mathrm{d}^{m+n}}{\\mathrm{d}x^{m+n}} (1-x^2)^n.

        INPUT:

        - ``n`` -- integer degree
        - ``m`` -- integer order
        - ``x`` -- either an integer or a non-numerical symbolic expression

        EXAMPLES::

            sage: gen_legendre_P(7, 4, x)                                               # needs sage.symbolic
            3465/2*(13*x^3 - 3*x)*(x^2 - 1)^2
            sage: gen_legendre_P(3, 1, sqrt(x))                                         # needs sage.symbolic
            -3/2*(5*x - 1)*sqrt(-x + 1)

        REFERENCE:

        - [DLMF-Legendre]_, Section 14.7 eq. 10 (https://dlmf.nist.gov/14.7#E10)
        """
    eval_poly: Incomplete

gen_legendre_P: Incomplete

class Func_assoc_legendre_Q(BuiltinFunction):
    def __init__(self) -> None:
        """
        EXAMPLES::

            sage: loads(dumps(gen_legendre_Q))
            gen_legendre_Q
            sage: maxima(gen_legendre_Q(2, 1, 3, hold=True))._sage_().simplify_full()   # needs sage.symbolic
            1/4*sqrt(2)*(36*pi - 36*I*log(2) + 25*I)
        """
    def eval_recursive(self, n, m, x, **kwds):
        """
        Return the associated Legendre Q(n, m, arg) function for integers `n > -1, m > -1`.

        EXAMPLES::

            sage: # needs sage.symbolic
            sage: gen_legendre_Q(3, 4, x)
            48/(x^2 - 1)^2
            sage: gen_legendre_Q(4, 5, x)
            -384/((x^2 - 1)^2*sqrt(-x^2 + 1))
            sage: gen_legendre_Q(0, 1, x)
            -1/sqrt(-x^2 + 1)
            sage: gen_legendre_Q(0, 2, x)
            -1/2*((x + 1)^2 - (x - 1)^2)/(x^2 - 1)
            sage: gen_legendre_Q(2, 2, x).subs(x=2).expand()
            9/2*I*pi - 9/2*log(3) + 14/3
        """

gen_legendre_Q: Incomplete

class Func_hermite(GinacFunction):
    """
    Return the Hermite polynomial for integers `n > -1`.

    REFERENCE:

    - [AS1964]_ 22.5.40 and 22.5.41, page 779.

    EXAMPLES::

        sage: # needs sage.symbolic
        sage: x = PolynomialRing(QQ, 'x').gen()
        sage: hermite(2, x)
        4*x^2 - 2
        sage: hermite(3, x)
        8*x^3 - 12*x
        sage: hermite(3, 2)
        40
        sage: S.<y> = PolynomialRing(RR)
        sage: hermite(3, y)
        8.00000000000000*y^3 - 12.0000000000000*y
        sage: R.<x,y> = QQ[]
        sage: hermite(3, y^2)
        8*y^6 - 12*y^2
        sage: w = var('w')
        sage: hermite(3, 2*w)
        64*w^3 - 24*w
        sage: hermite(5, 3.1416)
        5208.69733891963
        sage: hermite(5, RealField(100)(pi))
        5208.6167627118104649470287166

    Check that :issue:`17192` is fixed::

        sage: # needs sage.symbolic
        sage: x = PolynomialRing(QQ, 'x').gen()
        sage: hermite(0, x)
        1
        sage: hermite(-1, x)
        Traceback (most recent call last):
        ...
        RuntimeError: hermite_eval: The index n must be a nonnegative integer
        sage: hermite(-7, x)
        Traceback (most recent call last):
        ...
        RuntimeError: hermite_eval: The index n must be a nonnegative integer
        sage: m, x = SR.var('m,x')
        sage: hermite(m, x).diff(m)
        Traceback (most recent call last):
        ...
        RuntimeError: derivative w.r.t. to the index is not supported yet
    """
    def __init__(self) -> None:
        """
        Init method for the Hermite polynomials.

        EXAMPLES::

            sage: loads(dumps(hermite))
            hermite
            sage: hermite(x, x)._sympy_()                                               # needs sympy sage.symbolic
            hermite(x, x)

        TESTS::

            sage: fricas(hermite(x, 5))         # optional - fricas                     # needs sage.symbolic
            hermiteH(x,5)

            sage: hermite(5, x)                                                         # needs sage.symbolic
            32*x^5 - 160*x^3 + 120*x
            sage: fricas.hermiteH(5, x)         # optional - fricas                     # needs sage.symbolic
                5        3
            32 x  - 160 x  + 120 x
        """

hermite: Incomplete

class Func_jacobi_P(OrthogonalFunction):
    """
    Return the Jacobi polynomial `P_n^{(a,b)}(x)` for integers
    `n > -1` and a and b symbolic or `a > -1` and `b > -1`.

    The Jacobi polynomials are actually defined for all `a` and `b`.
    However, the Jacobi polynomial weight `(1-x)^a(1+x)^b` is not
    integrable for `a \\leq -1` or `b \\leq -1`.

    REFERENCE:

    - Table on page 789 in [AS1964]_.

    EXAMPLES::

        sage: x = PolynomialRing(QQ, 'x').gen()
        sage: jacobi_P(2, 0, 0, x)                                                      # needs sage.libs.flint sage.symbolic
        3/2*x^2 - 1/2
        sage: jacobi_P(2, 1, 2, 1.2)                                                    # needs sage.libs.flint
        5.01000000000000
    """
    def __init__(self) -> None:
        """
        Init method for the Jacobi polynomials.

        EXAMPLES::

            sage: n, a, b, x = SR.var('n,a,b,x')                                        # needs sage.symbolic
            sage: loads(dumps(jacobi_P))
            jacobi_P
            sage: jacobi_P(n, a, b, x, hold=True)._sympy_()                             # needs sympy sage.symbolic
            jacobi(n, a, b, x)

        TESTS::

            sage: fricas(jacobi_P(1/2, 4, 1/3, x))                              # optional - fricas, needs sage.symbolic
                    1   1
            jacobiP(-,4,-,x)
                    2   3

            sage: jacobi_P(1, 2, 3, x)                                                  # needs sage.symbolic
            7/2*x - 1/2
            sage: fricas.jacobiP(1, 2, 3, x)                                    # optional - fricas, needs sage.symbolic
            7 x - 1
            -------
               2
        """

jacobi_P: Incomplete

class Func_ultraspherical(GinacFunction):
    '''
    Return the ultraspherical (or Gegenbauer) polynomial ``gegenbauer(n,a,x)``,

    .. MATH::

        C_n^{a}(x) = \\sum_{k=0}^{\\lfloor n/2\\rfloor} (-1)^k
        \\frac{\\Gamma(n-k+a)}{\\Gamma(a)k!(n-2k)!} (2x)^{n-2k}.

    When `n` is a nonnegative integer, this formula gives a
    polynomial in `z` of degree `n`, but all parameters are
    permitted to be complex numbers. When `a = 1/2`, the
    Gegenbauer polynomial reduces to a Legendre polynomial.

    Computed using Pynac.

    For numerical evaluation, consider using the `mpmath library
    <http://mpmath.org/doc/current/functions/orthogonal.html#gegenbauer-polynomials>`_,
    as it also allows complex numbers (and negative `n` as well);
    see the examples below.

    REFERENCE:

    - [AS1964]_ 22.5.27

    EXAMPLES::

        sage: # needs sage.symbolic
        sage: ultraspherical(8, 101/11, x)
        795972057547264/214358881*x^8 - 62604543852032/19487171*x^6...
        sage: x = PolynomialRing(QQ, \'x\').gen()
        sage: ultraspherical(2, 3/2, x)
        15/2*x^2 - 3/2
        sage: ultraspherical(1, 1, x)
        2*x
        sage: t = PolynomialRing(RationalField(), "t").gen()
        sage: gegenbauer(3, 2, t)
        32*t^3 - 12*t
        sage: x = SR.var(\'x\')
        sage: n = ZZ.random_element(5, 5001)
        sage: a = QQ.random_element().abs() + 5
        sage: s = (  (n + 1)*ultraspherical(n + 1, a, x)
        ....:      - 2*x*(n + a)*ultraspherical(n, a, x)
        ....:      + (n + 2*a - 1)*ultraspherical(n - 1, a, x) )
        sage: s.expand().is_zero()
        True
        sage: ultraspherical(5, 9/10, 3.1416)
        6949.55439044240
        sage: ultraspherical(5, 9/10, RealField(100)(pi))                               # needs sage.rings.real_mpfr
        6949.4695419382702451843080687

        sage: # needs sage.symbolic
        sage: a, n = SR.var(\'a,n\')
        sage: gegenbauer(2, a, x)
        2*(a + 1)*a*x^2 - a
        sage: gegenbauer(3, a, x)
        4/3*(a + 2)*(a + 1)*a*x^3 - 2*(a + 1)*a*x
        sage: gegenbauer(3, a, x).expand()
        4/3*a^3*x^3 + 4*a^2*x^3 + 8/3*a*x^3 - 2*a^2*x - 2*a*x
        sage: gegenbauer(10, a, x).expand().coefficient(x, 2)
        1/12*a^6 + 5/4*a^5 + 85/12*a^4 + 75/4*a^3 + 137/6*a^2 + 10*a
        sage: ex = gegenbauer(100, a, x)
        sage: (ex.subs(a==55/98) - gegenbauer(100, 55/98, x)).is_trivial_zero()
        True

        sage: # needs sage.symbolic
        sage: gegenbauer(2, -3, x)
        12*x^2 + 3
        sage: gegenbauer(120, -99/2, 3)
        1654502372608570682112687530178328494861923493372493824
        sage: gegenbauer(5, 9/2, x)
        21879/8*x^5 - 6435/4*x^3 + 1287/8*x
        sage: gegenbauer(15, 3/2, 5)
        3903412392243800

        sage: derivative(gegenbauer(n, a, x), x)                                        # needs sage.symbolic
        2*a*gegenbauer(n - 1, a + 1, x)
        sage: derivative(gegenbauer(3, a, x), x)                                        # needs sage.symbolic
        4*(a + 2)*(a + 1)*a*x^2 - 2*(a + 1)*a
        sage: derivative(gegenbauer(n, a, x), a)                                        # needs sage.symbolic
        Traceback (most recent call last):
        ...
        RuntimeError: derivative w.r.t. to the second index is not supported yet

    Numerical evaluation with the mpmath library::

        sage: # needs mpmath
        sage: from mpmath import gegenbauer as gegenbauer_mp
        sage: from mpmath import mp
        sage: print(gegenbauer_mp(-7,0.5,0.3))
        0.1291811875
        sage: with mp.workdps(25):
        ....:     print(gegenbauer_mp(2+3j, -0.75, -1000j))
        (-5038991.358609026523401901 + 9414549.285447104177860806j)

    TESTS:

    Check that :issue:`17192` is fixed::

        sage: x = PolynomialRing(QQ, \'x\').gen()
        sage: ultraspherical(0, 1, x)                                                   # needs sage.symbolic
        1

        sage: ultraspherical(-1, 1, x)                                                  # needs sage.symbolic
        Traceback (most recent call last):
        ...
        RuntimeError: gegenb_eval: The index n must be a nonnegative integer

        sage: ultraspherical(-7, 1, x)                                                  # needs sage.symbolic
        Traceback (most recent call last):
        ...
        RuntimeError: gegenb_eval: The index n must be a nonnegative integer
    '''
    def __init__(self) -> None:
        """
        Init method for the ultraspherical polynomials.

        EXAMPLES::

            sage: loads(dumps(ultraspherical))
            gegenbauer
            sage: ultraspherical(x, x, x)._sympy_()                                     # needs sympy sage.symbolic
            gegenbauer(x, x, x)
        """

ultraspherical: Incomplete
gegenbauer: Incomplete

class Func_laguerre(OrthogonalFunction):
    """
    REFERENCE:

    - [AS1964]_ 22.5.16, page 778 and page 789.
    """
    def __init__(self) -> None:
        """
        Init method for the Laguerre polynomials.

        EXAMPLES::

            sage: # needs sage.symbolic
            sage: n, x = var('n,x')
            sage: laguerre(x, x)._sympy_()                                              # needs sympy
            laguerre(x, x)
            sage: maxima(laguerre(1, x, hold=True))
            1-_SAGE_VAR_x
            sage: maxima(laguerre(n, laguerre(n, x)))
            laguerre(_SAGE_VAR_n,laguerre(_SAGE_VAR_n,_SAGE_VAR_x))

        TESTS::

            sage: loads(dumps(laguerre))
            laguerre
        """

laguerre: Incomplete

class Func_gen_laguerre(OrthogonalFunction):
    """
    REFERENCE:

    - [AS1964]_ 22.5.16, page 778 and page 789.
    """
    def __init__(self) -> None:
        """
        Init method for the Laguerre polynomials.

        EXAMPLES::

            sage: # needs sage.symbolic
            sage: a, n, x = var('a, n, x')
            sage: gen_laguerre(x, x, x)._sympy_()                                       # needs sympy
            assoc_laguerre(x, x, x)
            sage: maxima(gen_laguerre(1, 2, x, hold=True))
            3*(1-_SAGE_VAR_x/3)
            sage: maxima(gen_laguerre(n, a, gen_laguerre(n, a, x)))
            gen_laguerre(_SAGE_VAR_n,_SAGE_VAR_a, gen_laguerre(_SAGE_VAR_n,_SAGE_VAR_a,_SAGE_VAR_x))

        TESTS::

            sage: loads(dumps(gen_laguerre))
            gen_laguerre
        """

gen_laguerre: Incomplete

class Func_krawtchouk(OrthogonalFunction):
    """
    Krawtchouk polynomials `K_j(x; n, p)`.

    INPUT:

    - ``j`` -- the degree
    - ``x`` -- the independent variable `x`
    - ``n`` -- the number of discrete points
    - ``p`` -- the parameter `p`

    .. SEEALSO::

        :func:`sage.coding.delsarte_bounds.krawtchouk`
        `\\bar{K}^{n,q}_l(x)`, which are related by

        .. MATH::

            (-q)^j \\bar{K}^{n,q^{-1}}_j(x) = K_j(x; n, 1-q).

    EXAMPLES:

    We verify the orthogonality for `n = 4`::

        sage: n = 4
        sage: p = SR.var('p')                                                           # needs sage.symbolic
        sage: matrix([[sum(binomial(n,m) * p**m * (1-p)**(n-m)                          # needs sage.symbolic
        ....:              * krawtchouk(i,m,n,p) * krawtchouk(j,m,n,p)
        ....:              for m in range(n+1)).expand().factor()
        ....:          for i in range(n+1)] for j in range(n+1)])
        [               1                0                0                0                0]
        [               0     -4*(p - 1)*p                0                0                0]
        [               0                0  6*(p - 1)^2*p^2                0                0]
        [               0                0                0 -4*(p - 1)^3*p^3                0]
        [               0                0                0                0    (p - 1)^4*p^4]

    We verify the relationship between the Krawtchouk implementations::

        sage: q = SR.var('q')                                                           # needs sage.symbolic
        sage: all(codes.bounds.krawtchouk(n, 1/q, j, x)*(-q)^j                          # needs sage.symbolic
        ....:     == krawtchouk(j, x, n, 1-q) for j in range(n+1))
        True
    """
    def __init__(self) -> None:
        """
        Initialize ``self``.

        EXAMPLES::

            sage: k, x, n, p = var('k,x,n,p')                                           # needs sage.symbolic
            sage: TestSuite(krawtchouk).run()
            sage: TestSuite(krawtchouk(k, x, n, p)).run()                               # needs sage.symbolic
            sage: TestSuite(krawtchouk(3, x, n, p)).run()                               # needs sage.symbolic
        """
    def eval_formula(self, k, x, n, p):
        """
        Evaluate ``self`` using an explicit formula.

        EXAMPLES::

            sage: x, n, p = var('x,n,p')                                                # needs sage.symbolic
            sage: krawtchouk.eval_formula(3, x, n, p).expand().collect(x)               # needs sage.symbolic
            -1/6*n^3*p^3 + 1/2*n^2*p^3 - 1/3*n*p^3 - 1/2*(n*p - 2*p + 1)*x^2
             + 1/6*x^3 + 1/6*(3*n^2*p^2 - 9*n*p^2 + 3*n*p + 6*p^2 - 6*p + 2)*x
        """
    def eval_recursive(self, j, x, n, p, *args, **kwds):
        """
        Return the Krawtchouk polynomial `K_j(x; n, p)` using the
        recursive formula.

        EXAMPLES::

            sage: # needs sage.symbolic
            sage: x, n, p = var('x,n,p')
            sage: krawtchouk.eval_recursive(0, x, n, p)
            1
            sage: krawtchouk.eval_recursive(1, x, n, p)
            -n*p + x
            sage: krawtchouk.eval_recursive(2, x, n, p).collect(x)
            1/2*n^2*p^2 + 1/2*n*(p - 1)*p - n*p^2 + 1/2*n*p
             - 1/2*(2*n*p - 2*p + 1)*x + 1/2*x^2
            sage: bool(krawtchouk.eval_recursive(2, x, n, p) == krawtchouk(2, x, n, p))
            True
            sage: bool(krawtchouk.eval_recursive(3, x, n, p) == krawtchouk(3, x, n, p))
            True
            sage: bool(krawtchouk.eval_recursive(4, x, n, p) == krawtchouk(4, x, n, p))
            True

            sage: M = matrix([[-1/2, -1], [1, 0]])                                      # needs sage.modules
            sage: krawtchouk.eval_recursive(2, M, 3, 1/2)                               # needs sage.modules
            [ 9/8  7/4]
            [-7/4  1/4]
        """

krawtchouk: Incomplete

class Func_meixner(OrthogonalFunction):
    """
    Meixner polynomials `M_n(x; b, c)`.

    INPUT:

    - ``n`` -- the degree
    - ``x`` -- the independent variable `x`
    - ``b``, ``c`` -- the parameters `b`, `c`
    """
    def __init__(self) -> None:
        """
        Initialize ``self``.

        EXAMPLES::

            sage: n, x, b, c = var('n,x,b,c')                                           # needs sage.symbolic
            sage: TestSuite(meixner).run()
            sage: TestSuite(meixner(3, x, b, c)).run()                                  # needs sage.symbolic
            sage: TestSuite(meixner(n, x, b, c)).run()                                  # needs sage.symbolic
        """
    def eval_formula(self, n, x, b, c):
        """
        Evaluate ``self`` using an explicit formula.

        EXAMPLES::

            sage: x, b, c = var('x,b,c')                                                # needs sage.symbolic
            sage: meixner.eval_formula(3, x, b, c).expand().collect(x)                  # needs sage.symbolic
            -x^3*(3/c - 3/c^2 + 1/c^3 - 1) + b^3
             + 3*(b - 2*b/c + b/c^2 - 1/c - 1/c^2 + 1/c^3 + 1)*x^2 + 3*b^2
             + (3*b^2 + 6*b - 3*b^2/c - 3*b/c - 3*b/c^2 - 2/c^3 + 2)*x + 2*b
        """
    def eval_recursive(self, n, x, b, c, *args, **kwds):
        """
        Return the Meixner polynomial `M_n(x; b, c)` using the
        recursive formula.

        EXAMPLES::

            sage: # needs sage.symbolic
            sage: x, b, c = var('x,b,c')
            sage: meixner.eval_recursive(0, x, b, c)
            1
            sage: meixner.eval_recursive(1, x, b, c)
            -x*(1/c - 1) + b
            sage: meixner.eval_recursive(2, x, b, c).simplify_full().collect(x)
            -x^2*(2/c - 1/c^2 - 1) + b^2 + (2*b - 2*b/c - 1/c^2 + 1)*x + b
            sage: bool(meixner(2, x, b, c) == meixner.eval_recursive(2, x, b, c))
            True
            sage: bool(meixner(3, x, b, c) == meixner.eval_recursive(3, x, b, c))
            True
            sage: bool(meixner(4, x, b, c) == meixner.eval_recursive(4, x, b, c))
            True
            sage: M = matrix([[-1/2, -1], [1, 0]])
            sage: ret = meixner.eval_recursive(2, M, b, c).simplify_full().factor()
            sage: for i in range(2):  # make the output polynomials in 1/c
            ....:     for j in range(2):
            ....:         ret[i, j] = ret[i, j].collect(c)
            sage: ret
            [b^2 + 1/2*(2*b + 3)/c - 1/4/c^2 - 5/4    -2*b + (2*b - 1)/c + 3/2/c^2 - 1/2]
            [    2*b - (2*b - 1)/c - 3/2/c^2 + 1/2             b^2 + b + 2/c - 1/c^2 - 1]
        """

meixner: Incomplete

class Func_hahn(OrthogonalFunction):
    """
    Hahn polynomials `Q_k(x; a, b, n)`.

    INPUT:

    - ``k`` -- the degree
    - ``x`` -- the independent variable `x`
    - ``a``, ``b`` -- the parameters `a`, `b`
    - ``n`` -- the number of discrete points

    EXAMPLES:

    We verify the orthogonality for `n = 3`::

        sage: # needs sage.symbolic
        sage: n = 2
        sage: a, b = SR.var('a,b')
        sage: def rho(k, a, b, n):
        ....:     return binomial(a + k, k) * binomial(b + n - k, n - k)
        sage: M = matrix([[sum(rho(k, a, b, n)
        ....:                  * hahn(i, k, a, b, n) * hahn(j, k, a, b, n)
        ....:                  for k in range(n + 1)).expand().factor()
        ....:              for i in range(n+1)] for j in range(n+1)])
        sage: M = M.factor()
        sage: P = rising_factorial
        sage: def diag(i, a, b, n):
        ....:    return ((-1)^i * factorial(i) * P(b + 1, i) * P(i + a + b + 1, n + 1)
        ....:            / (factorial(n) * (2*i + a + b + 1) * P(-n, i) * P(a + 1, i)))
        sage: all(M[i,i] == diag(i, a, b, n) for i in range(3))
        True
        sage: all(M[i,j] == 0 for i in range(3) for j in range(3) if i != j)
        True
    """
    def __init__(self) -> None:
        """
        Initialize ``self``.

        EXAMPLES::

            sage: k, x, a, b, n = var('k,x,a,b,n')                                      # needs sage.symbolic
            sage: TestSuite(hahn).run()
            sage: TestSuite(hahn(3, x, a, b, n)).run()                                  # needs sage.symbolic
            sage: TestSuite(hahn(k, x, a, b, n)).run(skip='_test_category')             # needs sage.symbolic
        """
    def eval_formula(self, k, x, a, b, n):
        """
        Evaluate ``self`` using an explicit formula.

        EXAMPLES::

            sage: # needs sage.symbolic
            sage: k, x, a, b, n = var('k,x,a,b,n')
            sage: Q2 = hahn.eval_formula(2, x, a, b, n).simplify_full()
            sage: Q2.coefficient(x^2).factor()
            (a + b + 4)*(a + b + 3)/((a + 2)*(a + 1)*(n - 1)*n)
            sage: Q2.coefficient(x).factor()
            -(2*a*n - a + b + 4*n)*(a + b + 3)/((a + 2)*(a + 1)*(n - 1)*n)
            sage: Q2(x=0)
            1
        """
    def eval_recursive(self, k, x, a, b, n, *args, **kwds):
        """
        Return the Hahn polynomial `Q_k(x; a, b, n)` using the
        recursive formula.

        EXAMPLES::

            sage: # needs sage.symbolic
            sage: x, a, b, n = var('x,a,b,n')
            sage: hahn.eval_recursive(0, x, a, b, n)
            1
            sage: hahn.eval_recursive(1, x, a, b, n)
            -(a + b + 2)*x/((a + 1)*n) + 1
            sage: bool(hahn(2, x, a, b, n) == hahn.eval_recursive(2, x, a, b, n))
            True
            sage: bool(hahn(3, x, a, b, n) == hahn.eval_recursive(3, x, a, b, n))
            True
            sage: bool(hahn(4, x, a, b, n) == hahn.eval_recursive(4, x, a, b, n))
            True
            sage: M = matrix([[-1/2, -1], [1, 0]])                                      # needs sage.modules
            sage: ret = hahn.eval_recursive(2, M, 1, 2, n).simplify_full().factor()     # needs sage.modules
            sage: ret                                                                   # needs sage.modules
            [1/4*(4*n^2 + 8*n - 19)/((n - 1)*n)          3/2*(4*n + 3)/((n - 1)*n)]
            [        -3/2*(4*n + 3)/((n - 1)*n)          (n^2 - n - 7)/((n - 1)*n)]
        """

hahn: Incomplete
