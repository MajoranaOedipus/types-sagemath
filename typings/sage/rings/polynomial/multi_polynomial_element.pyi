from . import polydict as polydict
from .multi_polynomial import MPolynomial as MPolynomial, is_MPolynomial as is_MPolynomial
from _typeshed import Incomplete
from collections.abc import Generator
from sage.misc.lazy_attribute import lazy_attribute as lazy_attribute
from sage.misc.misc_c import prod as prod
from sage.misc.superseded import deprecated_function_alias as deprecated_function_alias
from sage.rings.fraction_field import FractionField as FractionField
from sage.rings.integer import Integer as Integer
from sage.rings.polynomial.polynomial_singular_interface import Polynomial_singular_repr as Polynomial_singular_repr
from sage.rings.qqbar_decorators import handle_AA_and_QQbar as handle_AA_and_QQbar
from sage.rings.rational_field import QQ as QQ
from sage.structure.element import CommutativeRingElement as CommutativeRingElement, coerce_binop as coerce_binop, get_coercion_model as get_coercion_model, parent as parent
from sage.structure.factorization import Factorization as Factorization
from sage.structure.sequence import Sequence as Sequence

class MPolynomial_element(MPolynomial):
    """
    Generic multivariate polynomial.

    This implementation is based on the :class:`~sage.rings.polynomial.polydict.PolyDict`.

    .. TODO::

        As mentioned in their docstring,
        :class:`~sage.rings.polynomial.polydict.PolyDict` objects never clear
        zeros. In all arithmetic operations on :class:`MPolynomial_element`
        there is an additional call to the method ``remove_zeros`` to clear
        them. This is not ideal because of the presence of inexact zeros, see
        :issue:`35174`.
    """
    def __init__(self, parent, x) -> None:
        """
        EXAMPLES::

            sage: # needs sage.rings.number_field
            sage: x = polygen(ZZ, 'x')
            sage: K.<cuberoot2> = NumberField(x^3 - 2)
            sage: L.<cuberoot3> = K.extension(x^3 - 3)
            sage: S.<sqrt2> = L.extension(x^2 - 2)
            sage: S
            Number Field in sqrt2 with defining polynomial x^2 - 2 over its base field
            sage: P.<x,y,z> = PolynomialRing(S) # indirect doctest
        """
    def __call__(self, *x, **kwds):
        """
        Evaluate this multi-variate polynomial at `x`, where
        `x` is either the tuple of values to substitute in, or one
        can use functional notation `f(a_0,a_1,a_2, \\ldots)` to
        evaluate `f` with the `i`-th variable replaced by `a_i`.

        EXAMPLES::

            sage: # needs sage.rings.real_mpfr
            sage: R.<x,y> = CC[]
            sage: f = x^2 + y^2
            sage: f(1,2)
            5.00000000000000
            sage: f((1,2))
            5.00000000000000

        ::

            sage: # needs sage.rings.real_mpfr
            sage: x = PolynomialRing(CC, 3, 'x').gens()
            sage: f = x[0] + x[1] - 2*x[1]*x[2]; f
            (-2.00000000000000)*x1*x2 + x0 + x1
            sage: f(1,2,0)
            3.00000000000000
            sage: f(1,2,5)
            -17.0000000000000

        TESTS:

        Check :issue:`27446`::

            sage: P = PolynomialRing(QQ, 't', 0)
            sage: a = P(1)
            sage: a(()).parent()
            Rational Field

        AUTHORS:

        - David Kohel (2005-09-27)
        """
    def number_of_terms(self):
        """
        Return the number of nonzero coefficients of this polynomial.

        This is also called weight, :meth:`hamming_weight` or sparsity.

        EXAMPLES::

            sage: # needs sage.rings.real_mpfr
            sage: R.<x, y> = CC[]
            sage: f = x^3 - y
            sage: f.number_of_terms()
            2
            sage: R(0).number_of_terms()
            0
            sage: f = (x+y)^100
            sage: f.number_of_terms()
            101

        The method :meth:`hamming_weight` is an alias::

            sage: f.hamming_weight()                                                    # needs sage.rings.real_mpfr
            101
        """
    hamming_weight = number_of_terms
    def __neg__(self):
        """
        Return the negative of ``self``.

        EXAMPLES::

            sage: R.<x,y> = QQbar[]                                                     # needs sage.rings.number_field
            sage: -x                                                                    # needs sage.rings.number_field
            -x
            sage: -(y-1)                                                                # needs sage.rings.number_field
            -y + 1
        """
    def __rpow__(self, n): ...
    def element(self): ...

class MPolynomial_polydict(Polynomial_singular_repr, MPolynomial_element):
    """
    Multivariate polynomials implemented in pure python using
    polydicts.
    """
    def __init__(self, parent, x) -> None:
        """
        EXAMPLES::

            sage: R, x = PolynomialRing(QQbar, 10, 'x').objgens()                       # needs sage.rings.number_field
            sage: x                                                                     # needs sage.rings.number_field
            (x0, x1, x2, x3, x4, x5, x6, x7, x8, x9)
            sage: loads(dumps(x)) == x                                                  # needs sage.rings.number_field
            True
        """
    def degrees(self):
        """
        Return a tuple (precisely - an ``ETuple``) with the
        degree of each variable in this polynomial. The list of degrees is,
        of course, ordered by the order of the generators.

        EXAMPLES::

            sage: # needs sage.rings.number_field
            sage: R.<x,y,z> = PolynomialRing(QQbar)
            sage: f = 3*x^2 - 2*y + 7*x^2*y^2 + 5
            sage: f.degrees()
            (2, 2, 0)
            sage: f = x^2 + z^2
            sage: f.degrees()
            (2, 0, 2)
            sage: f.total_degree()  # this simply illustrates that total degree is not the sum of the degrees
            2
            sage: R.<x,y,z,u> = PolynomialRing(QQbar)
            sage: f = (1-x) * (1+y+z+x^3)^5
            sage: f.degrees()
            (16, 5, 5, 0)
            sage: R(0).degrees()
            (0, 0, 0, 0)
        """
    def degree(self, x=None, std_grading: bool = False):
        """
        Return the degree of ``self`` in ``x``, where ``x`` must be one of the
        generators for the parent of ``self``.

        INPUT:

        - ``x`` -- multivariate polynomial (a generator of the parent
          of ``self``). If ``x`` is not specified (or is None), return
          the total degree, which is the maximum degree of any
          monomial. Note that a weighted term ordering alters the
          grading of the generators of the ring; see the tests below.
          To avoid this behavior, set the optional argument ``std_grading=True``.

        OUTPUT: integer

        EXAMPLES::

            sage: R.<x,y> = RR[]
            sage: f = y^2 - x^9 - x
            sage: f.degree(x)
            9
            sage: f.degree(y)
            2
            sage: (y^10*x - 7*x^2*y^5 + 5*x^3).degree(x)
            3
            sage: (y^10*x - 7*x^2*y^5 + 5*x^3).degree(y)
            10

        Note that total degree takes into account if we are working in a polynomial
        ring with a weighted term order.

        ::

            sage: R = PolynomialRing(QQ, 'x,y', order=TermOrder('wdeglex',(2,3)))
            sage: x,y = R.gens()
            sage: x.degree()
            2
            sage: y.degree()
            3
            sage: x.degree(y), x.degree(x), y.degree(x), y.degree(y)
            (0, 1, 0, 1)
            sage: f = x^2*y + x*y^2
            sage: f.degree(x)
            2
            sage: f.degree(y)
            2
            sage: f.degree()
            8
            sage: f.degree(std_grading=True)
            3

        Note that if ``x`` is not a generator of the parent of ``self``,
        for example if it is a generator of a polynomial algebra which
        maps naturally to this one, then it is converted to an element
        of this algebra. (This fixes the problem reported in
        :issue:`17366`.)

        ::

            sage: x, y = ZZ['x','y'].gens()
            sage: GF(3037000453)['x','y'].gen(0).degree(x)                              # needs sage.rings.finite_rings
            1

            sage: x0, y0 = QQ['x','y'].gens()
            sage: GF(3037000453)['x','y'].gen(0).degree(x0)                             # needs sage.rings.finite_rings
            Traceback (most recent call last):
            ...
            TypeError: argument is not coercible to the parent

            sage: GF(3037000453)['x','y'].gen(0).degree(x^2)                            # needs sage.rings.finite_rings
            Traceback (most recent call last):
            ...
            TypeError: argument is not a generator

        TESTS::

            sage: R = PolynomialRing(GF(2)['t'], 'x,y',
            ....:                    order=TermOrder('wdeglex', (2,3)))
            sage: x, y = R.gens()
            sage: x.degree()
            2
            sage: y.degree()
            3
            sage: x.degree(y), x.degree(x), y.degree(x), y.degree(y)
            (0, 1, 0, 1)
            sage: f = (x^2*y + x*y^2)
            sage: f.degree(x)
            2
            sage: f.degree(y)
            2
            sage: f.degree()
            8
            sage: f.degree(std_grading=True)
            3
            sage: R(0).degree()
            -1

        Degree of zero polynomial for other implementation :issue:`20048` ::

            sage: R.<x,y> = GF(3037000453)[]                                            # needs sage.rings.finite_rings
            sage: R.zero().degree(x)
            -1

        Ensure that :issue:`37603` is fixed::

            sage: R.<x,y,z> = PolynomialRing(QQbar)
            sage: f = 3*x^2 - 2*y + 7*x^2*y^2 + 5
            sage: type(f.degree())
            <class 'sage.rings.integer.Integer'>
            sage: type(f.degree(x))
            <class 'sage.rings.integer.Integer'>
            sage: type(f.degree(x)) == type(f.degree(y)) == type(f.degree(z))
            True
        """
    def total_degree(self):
        """
        Return the total degree of ``self``, which is the maximum degree of any
        monomial in ``self``.

        EXAMPLES::

            sage: # needs sage.rings.number_field
            sage: R.<x,y,z> = QQbar[]
            sage: f = 2*x*y^3*z^2
            sage: f.total_degree()
            6
            sage: f = 4*x^2*y^2*z^3
            sage: f.total_degree()
            7
            sage: f = 99*x^6*y^3*z^9
            sage: f.total_degree()
            18
            sage: f = x*y^3*z^6 + 3*x^2
            sage: f.total_degree()
            10
            sage: f = z^3 + 8*x^4*y^5*z
            sage: f.total_degree()
            10
            sage: f = z^9 + 10*x^4 + y^8*x^2
            sage: f.total_degree()
            10

        TESTS:

        Ensure that :issue:`37603` is fixed::
             sage: R.<x,y,z> = QQbar[]
             sage: f = 2*x*y^3*z^2
             sage: f.total_degree()
             6
             sage: type(f.total_degree())
             <class 'sage.rings.integer.Integer'>
        """
    def monomial_coefficient(self, mon):
        """
        Return the coefficient in the base ring of the monomial ``mon`` in
        ``self``, where ``mon`` must have the same parent as ``self``.

        This function contrasts with the function
        ``coefficient`` which returns the coefficient of a
        monomial viewing this polynomial in a polynomial ring over a base
        ring having fewer variables.

        INPUT:

        - ``mon`` -- a monomial

        OUTPUT: coefficient in base ring

        .. SEEALSO::

           For coefficients in a base ring of fewer variables, look
           at :meth:`coefficient`.

        EXAMPLES:

        ::

            sage: # needs sage.rings.number_field
            sage: R.<x,y> = QQbar[]
            sage: f = 2 * x * y
            sage: c = f.monomial_coefficient(x*y); c
            2
            sage: c.parent()
            Algebraic Field

        ::

            sage: # needs sage.rings.number_field
            sage: f = y^2 + y^2*x - x^9 - 7*x + 5*x*y
            sage: f.monomial_coefficient(y^2)
            1
            sage: f.monomial_coefficient(x*y)
            5
            sage: f.monomial_coefficient(x^9)
            -1
            sage: f.monomial_coefficient(x^10)
            0

        ::

            sage: # needs sage.rings.number_field
            sage: a = polygen(ZZ, 'a')
            sage: K.<a> = NumberField(a^2 + a + 1)
            sage: P.<x,y> = K[]
            sage: f = (a*x - 1) * ((a+1)*y - 1); f
            -x*y + (-a)*x + (-a - 1)*y + 1
            sage: f.monomial_coefficient(x)
            -a
        """
    def monomial_coefficients(self, copy=None):
        """
        Return underlying dictionary with keys the exponents and values
        the coefficients of this polynomial.

        EXAMPLES::

            sage: # needs sage.rings.number_field
            sage: R.<x,y,z> = PolynomialRing(QQbar, order='lex')
            sage: f = (x^1*y^5*z^2 + x^2*z + x^4*y^1*z^3)
            sage: f.monomial_coefficients()
            {(1, 5, 2): 1, (2, 0, 1): 1, (4, 1, 3): 1}

        ``dict`` is an alias::

            sage: f.dict()                                                              # needs sage.rings.number_field
            {(1, 5, 2): 1, (2, 0, 1): 1, (4, 1, 3): 1}
        """
    dict = monomial_coefficients
    def __iter__(self):
        """
        Iterate over ``self`` respecting the term order.

        EXAMPLES::

            sage: R.<x,y,z> = PolynomialRing(QQbar, order='lex')                        # needs sage.rings.number_field
            sage: f = (x^1*y^5*z^2 + x^2*z + x^4*y^1*z^3)                               # needs sage.rings.number_field
            sage: list(f)                                                               # needs sage.rings.number_field
            [(1, x^4*y*z^3), (1, x^2*z), (1, x*y^5*z^2)]

        ::

            sage: R.<x,y,z> = PolynomialRing(QQbar, order='deglex')                     # needs sage.rings.number_field
            sage: f = (x^1*y^5*z^2 + x^2*z + x^4*y^1*z^3)                               # needs sage.rings.number_field
            sage: list(f)                                                               # needs sage.rings.number_field
            [(1, x^4*y*z^3), (1, x*y^5*z^2), (1, x^2*z)]

        ::

            sage: R.<x,y,z> = PolynomialRing(QQbar, order='degrevlex')                  # needs sage.rings.number_field
            sage: f = (x^1*y^5*z^2 + x^2*z + x^4*y^1*z^3)                               # needs sage.rings.number_field
            sage: list(f)                                                               # needs sage.rings.number_field
            [(1, x*y^5*z^2), (1, x^4*y*z^3), (1, x^2*z)]

        ::

            sage: R = ZZ['t']
            sage: P.<x,y,z> = PolynomialRing(R,3)
            sage: f = 3*x^3*y + 16*x + 7
            sage: [(c,m) for c,m in f]
            [(3, x^3*y), (16, x), (7, 1)]
            sage: f = P.random_element(10,10)
            sage: sum(c*m for c,m in f) == f
            True
        """
    def __getitem__(self, x):
        """
        Return the coefficient corresponding to ``x``.

        INPUT:

        - ``x`` -- tuple or, in case of a single-variable
          MPolynomial ring, ``x`` can also be an integer

        EXAMPLES::

            sage: # needs sage.rings.number_field
            sage: R.<x, y> = PolynomialRing(QQbar, 2)
            sage: f = -10*x^3*y + 17*x*y
            sage: f[3,1]
            -10
            sage: f[1,1]
            17
            sage: f[0,1]
            0

        ::

            sage: R.<x> = PolynomialRing(QQbar, 1); R                                   # needs sage.rings.number_field
            Multivariate Polynomial Ring in x over Algebraic Field
            sage: f = 5*x^2 + 3; f                                                      # needs sage.rings.number_field
            5*x^2 + 3
            sage: f[2]                                                                  # needs sage.rings.number_field
            5
        """
    def iterator_exp_coeff(self, as_ETuples: bool = True) -> Generator[Incomplete]:
        """
        Iterate over ``self`` as pairs of ((E)Tuple, coefficient).

        INPUT:

        - ``as_ETuples`` -- boolean (default: ``True``); if ``True`` iterate
          over pairs whose first element is an ETuple, otherwise as a tuples

        EXAMPLES::

            sage: R.<x,y,z> = PolynomialRing(QQbar, order='lex')                        # needs sage.rings.number_field
            sage: f = (x^1*y^5*z^2 + x^2*z + x^4*y^1*z^3)                               # needs sage.rings.number_field
            sage: list(f.iterator_exp_coeff())                                          # needs sage.rings.number_field
            [((4, 1, 3), 1), ((2, 0, 1), 1), ((1, 5, 2), 1)]

            sage: R.<x,y,z> = PolynomialRing(QQbar, order='deglex')                     # needs sage.rings.number_field
            sage: f = (x^1*y^5*z^2 + x^2*z + x^4*y^1*z^3)                               # needs sage.rings.number_field
            sage: list(f.iterator_exp_coeff(as_ETuples=False))                          # needs sage.rings.number_field
            [((4, 1, 3), 1), ((1, 5, 2), 1), ((2, 0, 1), 1)]
        """
    def coefficient(self, degrees):
        """
        Return the coefficient of the variables with the degrees specified
        in the python dictionary ``degrees``. Mathematically,
        this is the coefficient in the base ring adjoined by the variables
        of this ring not listed in ``degrees``. However, the
        result has the same parent as this polynomial.

        This function contrasts with the function
        ``monomial_coefficient`` which returns the coefficient
        in the base ring of a monomial.

        INPUT:

        - ``degrees`` -- can be any of:

          - a dictionary of degree restrictions

          - a list of degree restrictions (with ``None`` in
            the unrestricted variables)

          - a monomial (very fast, but not as flexible)

        OUTPUT: element of the parent of ``self``

        .. SEEALSO::

           For coefficients of specific monomials, look at
           :meth:`monomial_coefficient`.

        EXAMPLES::

            sage: # needs sage.rings.number_field
            sage: R.<x, y> = QQbar[]
            sage: f = 2 * x * y
            sage: c = f.coefficient({x: 1, y: 1}); c
            2
            sage: c.parent()
            Multivariate Polynomial Ring in x, y over Algebraic Field
            sage: c in PolynomialRing(QQbar, 2, names=['x', 'y'])
            True
            sage: f = y^2 - x^9 - 7*x + 5*x*y
            sage: f.coefficient({y: 1})
            5*x
            sage: f.coefficient({y: 0})
            -x^9 + (-7)*x
            sage: f.coefficient({x: 0, y: 0})
            0
            sage: f = (1+y+y^2) * (1+x+x^2)
            sage: f.coefficient({x: 0})
            y^2 + y + 1
            sage: f.coefficient([0, None])
            y^2 + y + 1
            sage: f.coefficient(x)
            y^2 + y + 1
            sage: # Be aware that this may not be what you think!
            sage: # The physical appearance of the variable x is deceiving -- particularly if the exponent would be a variable.
            sage: f.coefficient(x^0) # outputs the full polynomial
            x^2*y^2 + x^2*y + x*y^2 + x^2 + x*y + y^2 + x + y + 1

        ::

            sage: # needs sage.rings.real_mpfr
            sage: R.<x,y> = RR[]
            sage: f = x*y + 5
            sage: c = f.coefficient({x: 0, y: 0}); c
            5.00000000000000
            sage: parent(c)
            Multivariate Polynomial Ring in x, y over Real Field with 53 bits of precision

        AUTHORS:

        - Joel B. Mohler (2007-10-31)
        """
    def global_height(self, prec=None):
        """
        Return the (projective) global height of the polynomial.

        This returns the absolute logarithmic height of the coefficients
        thought of as a projective point.

        INPUT:

        - ``prec`` -- desired floating point precision (default:
          default :class:`RealField` precision)

        OUTPUT: a real number

        EXAMPLES::

            sage: R.<x,y> = PolynomialRing(QQbar, 2)                                    # needs sage.rings.number_field
            sage: f = QQbar(i)*x^2 + 3*x*y                                              # needs sage.rings.number_field
            sage: f.global_height()                                                     # needs sage.rings.number_field
            1.09861228866811

        Scaling should not change the result::

            sage: # needs sage.rings.number_field sage.symbolic
            sage: R.<x, y> = PolynomialRing(QQbar, 2)
            sage: f = 1/25*x^2 + 25/3*x + 1 + QQbar(sqrt(2))*y^2
            sage: f.global_height()
            6.43775164973640
            sage: g = 100 * f
            sage: g.global_height()
            6.43775164973640

        ::

            sage: # needs sage.rings.number_field
            sage: R.<x> = QQ[]
            sage: K.<k> = NumberField(x^2 + 1)
            sage: Q.<q,r> = PolynomialRing(K, implementation='generic')
            sage: f = 12 * q
            sage: f.global_height()
            0.000000000000000

        ::

            sage: R.<x,y> = PolynomialRing(QQ, implementation='generic')
            sage: f = 1/123*x*y + 12
            sage: f.global_height(prec=2)                                               # needs sage.symbolic
            8.0

        ::

            sage: R.<x,y> = PolynomialRing(QQ, implementation='generic')
            sage: f = 0*x*y
            sage: f.global_height()                                                     # needs sage.rings.real_mpfr
            0.000000000000000
        """
    def local_height(self, v, prec=None):
        """
        Return the maximum of the local height of the coefficients of
        this polynomial.

        INPUT:

        - ``v`` -- a prime or prime ideal of the base ring

        - ``prec`` -- desired floating point precision (default:
          default RealField precision)

        OUTPUT: a real number

        EXAMPLES::

            sage: R.<x,y> = PolynomialRing(QQ, implementation='generic')
            sage: f = 1/1331*x^2 + 1/4000*y
            sage: f.local_height(1331)                                                  # needs sage.rings.real_mpfr
            7.19368581839511

        ::

            sage: # needs sage.rings.number_field
            sage: R.<x> = QQ[]
            sage: K.<k> = NumberField(x^2 - 5)
            sage: T.<t,w> = PolynomialRing(K, implementation='generic')
            sage: I = K.ideal(3)
            sage: f = 1/3*t*w + 3
            sage: f.local_height(I)                                                     # needs sage.symbolic
            1.09861228866811

        ::

            sage: R.<x,y> = PolynomialRing(QQ, implementation='generic')
            sage: f = 1/2*x*y + 2
            sage: f.local_height(2, prec=2)                                             # needs sage.rings.real_mpfr
            0.75
        """
    def local_height_arch(self, i, prec=None):
        """
        Return the maximum of the local height at the ``i``-th infinite place
        of the coefficients of this polynomial.

        INPUT:

        - ``i`` -- integer

        - ``prec`` -- desired floating point precision (default:
          default :class:`RealField` precision)

        OUTPUT: a real number

        EXAMPLES::

            sage: R.<x,y> = PolynomialRing(QQ, implementation='generic')
            sage: f = 210*x*y
            sage: f.local_height_arch(0)                                                # needs sage.rings.real_mpfr
            5.34710753071747

        ::

            sage: # needs sage.rings.number_field
            sage: R.<x> = QQ[]
            sage: K.<k> = NumberField(x^2 - 5)
            sage: T.<t,w> = PolynomialRing(K, implementation='generic')
            sage: f = 1/2*t*w + 3
            sage: f.local_height_arch(1, prec=52)
            1.09861228866811

        ::

            sage: R.<x,y> = PolynomialRing(QQ, implementation='generic')
            sage: f = 1/2*x*y + 3
            sage: f.local_height_arch(0, prec=2)                                        # needs sage.rings.real_mpfr
            1.0
        """
    def exponents(self, as_ETuples: bool = True):
        """
        Return the exponents of the monomials appearing in ``self``.

        INPUT:

        - ``as_ETuples`` -- (default: ``True``) return the list of
          exponents as a list of ETuples

        OUTPUT: the list of exponents as a list of ETuples or tuples

        EXAMPLES::

            sage: R.<a,b,c> = PolynomialRing(QQbar, 3)                                  # needs sage.rings.number_field
            sage: f = a^3 + b + 2*b^2                                                   # needs sage.rings.number_field
            sage: f.exponents()                                                         # needs sage.rings.number_field
            [(3, 0, 0), (0, 2, 0), (0, 1, 0)]

        By default the list of exponents is a list of ETuples::

            sage: type(f.exponents()[0])                                                # needs sage.rings.number_field
            <class 'sage.rings.polynomial.polydict.ETuple'>
            sage: type(f.exponents(as_ETuples=False)[0])                                # needs sage.rings.number_field
            <... 'tuple'>

        TESTS:

        Check that we can mutate the list and not change the result::

            sage: # needs sage.rings.number_field
            sage: R.<a,b,c> = PolynomialRing(QQbar, 3)
            sage: f = a^3 + b + 2*b^2
            sage: E = f.exponents(); E
            [(3, 0, 0), (0, 2, 0), (0, 1, 0)]
            sage: E.pop()
            (0, 1, 0)
            sage: E != f.exponents()
            True
        """
    def inverse_of_unit(self):
        """
        Return the inverse of a unit in a ring.

        TESTS::

            sage: R.<c> = QQ[]
            sage: l = R(2)
            sage: l.inverse_of_unit().parent()
            Univariate Polynomial Ring in c over Rational Field
        """
    def is_homogeneous(self):
        '''
        Return ``True`` if ``self`` is a homogeneous polynomial.

        EXAMPLES::

            sage: # needs sage.rings.number_field
            sage: R.<x,y> = QQbar[]
            sage: (x + y).is_homogeneous()
            True
            sage: (x.parent()(0)).is_homogeneous()
            True
            sage: (x + y^2).is_homogeneous()
            False
            sage: (x^2 + y^2).is_homogeneous()
            True
            sage: (x^2 + y^2*x).is_homogeneous()
            False
            sage: (x^2*y + y^2*x).is_homogeneous()
            True

        The weight of the parent ring is respected::

            sage: term_order = TermOrder("wdegrevlex", [1, 3])
            sage: R.<x, y> = PolynomialRing(Qp(5), order=term_order)
            sage: (x + y).is_homogeneous()
            False
            sage: (x^3 + y).is_homogeneous()
            True
        '''
    def is_gen(self) -> bool:
        """
        Return ``True`` if ``self`` is a generator of its parent.

        EXAMPLES::

            sage: # needs sage.rings.number_field
            sage: R.<x,y> = QQbar[]
            sage: x.is_gen()
            True
            sage: (x + y - y).is_gen()
            True
            sage: (x*y).is_gen()
            False

        TESTS::

            sage: # needs sage.rings.number_field
            sage: R.<x,y> = QQbar[]
            sage: x.is_generator()
            doctest:warning...:
            DeprecationWarning: is_generator is deprecated. Please use is_gen instead.
            See https://github.com/sagemath/sage/issues/38942 for details.
            True
        """
    is_generator: Incomplete
    def is_monomial(self):
        """
        Return ``True`` if ``self`` is a monomial, which we define to be a
        product of generators with coefficient 1.

        Use :meth:`is_term` to allow the coefficient to not be 1.

        EXAMPLES::

            sage: # needs sage.rings.number_field
            sage: R.<x,y> = QQbar[]
            sage: x.is_monomial()
            True
            sage: (x + 2*y).is_monomial()
            False
            sage: (2*x).is_monomial()
            False
            sage: (x*y).is_monomial()
            True

        To allow a non-1 leading coefficient, use :meth:`is_term`::

            sage: (2*x*y).is_term()                                                     # needs sage.rings.number_field
            True
            sage: (2*x*y).is_monomial()                                                 # needs sage.rings.number_field
            False
        """
    def is_term(self):
        """
        Return ``True`` if ``self`` is a term, which we define to be a
        product of generators times some coefficient, which need
        not be 1.

        Use :meth:`is_monomial` to require that the coefficient be 1.

        EXAMPLES::

            sage: # needs sage.rings.number_field
            sage: R.<x,y> = QQbar[]
            sage: x.is_term()
            True
            sage: (x + 2*y).is_term()
            False
            sage: (2*x).is_term()
            True
            sage: (7*x^5*y).is_term()
            True

        To require leading coefficient 1, use :meth:`is_monomial`::

            sage: (2*x*y).is_monomial()                                                 # needs sage.rings.number_field
            False
            sage: (2*x*y).is_term()                                                     # needs sage.rings.number_field
            True
        """
    def subs(self, fixed=None, **kwds):
        """
        Fix some given variables in a given multivariate polynomial and
        return the changed multivariate polynomials. The polynomial itself
        is not affected. The variable, value pairs for fixing are to be
        provided as a dictionary of the form ``{variable: value}``.

        This is a special case of evaluating the polynomial with some of
        the variables constants and the others the original variables.

        INPUT:

        - ``fixed`` -- (optional) dictionary of inputs

        - ``**kwds`` -- named parameters

        OUTPUT: new :class:`MPolynomial`

        EXAMPLES::

            sage: # needs sage.rings.number_field
            sage: R.<x,y> = QQbar[]
            sage: f = x^2 + y + x^2*y^2 + 5
            sage: f((5, y))
            25*y^2 + y + 30
            sage: f.subs({x: 5})
            25*y^2 + y + 30
        """
    def monomials(self):
        """
        Return the list of monomials in ``self``. The returned list is
        decreasingly ordered by the term ordering of ``self.parent()``.

        OUTPUT: list of :class:`MPolynomial` instances, representing monomials

        EXAMPLES::

            sage: R.<x,y> = QQbar[]                                                     # needs sage.rings.number_field
            sage: f = 3*x^2 - 2*y + 7*x^2*y^2 + 5                                       # needs sage.rings.number_field
            sage: f.monomials()                                                         # needs sage.rings.number_field
            [x^2*y^2, x^2, y, 1]

        ::

            sage: # needs sage.rings.number_field
            sage: R.<fx,fy,gx,gy> = QQbar[]
            sage: F = (fx*gy - fy*gx)^3; F
            -fy^3*gx^3 + 3*fx*fy^2*gx^2*gy + (-3)*fx^2*fy*gx*gy^2 + fx^3*gy^3
            sage: F.monomials()
            [fy^3*gx^3, fx*fy^2*gx^2*gy, fx^2*fy*gx*gy^2, fx^3*gy^3]
            sage: F.coefficients()
            [-1, 3, -3, 1]
            sage: sum(map(mul, zip(F.coefficients(), F.monomials()))) == F
            True
        """
    def constant_coefficient(self):
        """
        Return the constant coefficient of this multivariate polynomial.

        EXAMPLES::

            sage: # needs sage.rings.number_field
            sage: R.<x,y> = QQbar[]
            sage: f = 3*x^2 - 2*y + 7*x^2*y^2 + 5
            sage: f.constant_coefficient()
            5
            sage: f = 3*x^2
            sage: f.constant_coefficient()
            0
        """
    def is_univariate(self):
        """
        Return ``True`` if this multivariate polynomial is univariate and
        ``False`` otherwise.

        EXAMPLES::

            sage: # needs sage.rings.number_field
            sage: R.<x,y> = QQbar[]
            sage: f = 3*x^2 - 2*y + 7*x^2*y^2 + 5
            sage: f.is_univariate()
            False
            sage: g = f.subs({x: 10}); g
            700*y^2 + (-2)*y + 305
            sage: g.is_univariate()
            True
            sage: f = x^0
            sage: f.is_univariate()
            True
        """
    def univariate_polynomial(self, R=None):
        """
        Return a univariate polynomial associated to this multivariate
        polynomial.

        INPUT:

        - ``R`` -- (default: ``None``) :class:`PolynomialRing`


        If this polynomial is not in at most one variable, then a
        :exc:`ValueError` exception is raised. This is checked using the
        method :meth:`is_univariate`. The new :class:`Polynomial` is over the same base
        ring as the given :class:`MPolynomial`.

        EXAMPLES::

            sage: # needs sage.rings.number_field
            sage: R.<x,y> = QQbar[]
            sage: f = 3*x^2 - 2*y + 7*x^2*y^2 + 5
            sage: f.univariate_polynomial()
            Traceback (most recent call last):
            ...
            TypeError: polynomial must involve at most one variable
            sage: g = f.subs({x: 10}); g
            700*y^2 + (-2)*y + 305
            sage: g.univariate_polynomial()
            700*y^2 - 2*y + 305
            sage: g.univariate_polynomial(PolynomialRing(QQ, 'z'))
            700*z^2 - 2*z + 305

        TESTS::

            sage: P = PolynomialRing(QQ, 0, '')
            sage: P(5).univariate_polynomial()
            5
        """
    def variables(self):
        """
        Return the tuple of variables occurring in this polynomial.

        EXAMPLES::

            sage: # needs sage.rings.number_field
            sage: R.<x,y> = QQbar[]
            sage: f = 3*x^2 - 2*y + 7*x^2*y^2 + 5
            sage: f.variables()
            (x, y)
            sage: g = f.subs({x: 10}); g
            700*y^2 + (-2)*y + 305
            sage: g.variables()
            (y,)

        TESTS:

        This shows that the issue at :issue:`7077` is fixed::

            sage: x,y,z=polygens(QQ,'x,y,z')
            sage: (x^2).variables()
            (x,)
        """
    def variable(self, i):
        """
        Return the `i`-th variable occurring in this polynomial.

        EXAMPLES::

            sage: # needs sage.rings.number_field
            sage: R.<x,y> = QQbar[]
            sage: f = 3*x^2 - 2*y + 7*x^2*y^2 + 5
            sage: f.variable(0)
            x
            sage: f.variable(1)
            y
        """
    def nvariables(self):
        """
        Return the number of variables in this polynomial.

        EXAMPLES::

            sage: # needs sage.rings.number_field
            sage: R.<x,y> = QQbar[]
            sage: f = 3*x^2 - 2*y + 7*x^2*y^2 + 5
            sage: f.nvariables()
            2
            sage: g = f.subs({x: 10}); g
            700*y^2 + (-2)*y + 305
            sage: g.nvariables()
            1
        """
    def is_constant(self):
        """
        Return ``True`` if ``self`` is a constant and ``False`` otherwise.

        EXAMPLES::

            sage: # needs sage.rings.number_field
            sage: R.<x,y> = QQbar[]
            sage: f = 3*x^2 - 2*y + 7*x^2*y^2 + 5
            sage: f.is_constant()
            False
            sage: g = 10*x^0
            sage: g.is_constant()
            True
        """
    def lm(self):
        """
        Return the lead monomial of ``self`` with respect to the term order of
        ``self.parent()``.

        EXAMPLES::

            sage: R.<x,y,z> = PolynomialRing(GF(7), 3, order='lex')
            sage: (x^1*y^2 + y^3*z^4).lm()
            x*y^2
            sage: (x^3*y^2*z^4 + x^3*y^2*z^1).lm()
            x^3*y^2*z^4

        ::

            sage: # needs sage.rings.real_mpfr
            sage: R.<x,y,z> = PolynomialRing(CC, 3, order='deglex')
            sage: (x^1*y^2*z^3 + x^3*y^2*z^0).lm()
            x*y^2*z^3
            sage: (x^1*y^2*z^4 + x^1*y^1*z^5).lm()
            x*y^2*z^4

        ::

            sage: # needs sage.rings.number_field
            sage: R.<x,y,z> = PolynomialRing(QQbar, 3, order='degrevlex')
            sage: (x^1*y^5*z^2 + x^4*y^1*z^3).lm()
            x*y^5*z^2
            sage: (x^4*y^7*z^1 + x^4*y^2*z^3).lm()
            x^4*y^7*z

        TESTS::

            sage: from sage.rings.polynomial.multi_polynomial_ring import MPolynomialRing_polydict
            sage: R.<x,y> = MPolynomialRing_polydict(GF(2), 2, order='lex')
            sage: f = x + y
            sage: f.lm()
            x
        """
    def lc(self):
        """
        Return the leading coefficient of ``self``, i.e.,
        ``self.coefficient(self.lm())``.

        EXAMPLES::

            sage: R.<x,y,z> = QQbar[]                                                   # needs sage.rings.number_field
            sage: f = 3*x^2 - y^2 - x*y                                                 # needs sage.rings.number_field
            sage: f.lc()                                                                # needs sage.rings.number_field
            3
        """
    def lt(self):
        '''
        Return the leading term of ``self`` i.e., ``self.lc()*self.lm()``. The
        notion of "leading term" depends on the ordering defined in the
        parent ring.

        EXAMPLES::

            sage: # needs sage.rings.number_field
            sage: R.<x,y,z> = PolynomialRing(QQbar)
            sage: f = 3*x^2 - y^2 - x*y
            sage: f.lt()
            3*x^2
            sage: R.<x,y,z> = PolynomialRing(QQbar, order=\'invlex\')
            sage: f = 3*x^2 - y^2 - x*y
            sage: f.lt()
            -y^2

        TESTS::

            sage: from sage.rings.polynomial.multi_polynomial_ring import MPolynomialRing_polydict
            sage: R.<x,y> = MPolynomialRing_polydict(GF(2), 2, order=\'lex\')
            sage: f = x + y
            sage: f.lt()
            x
        '''
    def __eq__(self, right): ...
    def __ne__(self, right): ...
    __hash__: Incomplete
    def __bool__(self) -> bool:
        """
        Return ``True`` if ``self != 0``.

        .. NOTE::

           This is much faster than actually writing ``self == 0``.
        """
    def integral(self, var=None):
        """
        Integrate ``self`` with respect to variable ``var``.

        .. NOTE::

            The integral is always chosen so the constant term is 0.

        If ``var`` is not one of the generators of this ring, ``integral(var)``
        is called recursively on each coefficient of this polynomial.

        EXAMPLES:

        On polynomials with rational coefficients::

            sage: x, y = PolynomialRing(QQ, 'x, y').gens()
            sage: ex = x*y + x - y
            sage: it = ex.integral(x); it
            1/2*x^2*y + 1/2*x^2 - x*y
            sage: it.parent() == x.parent()
            True

            sage: R = ZZ['x']['y, z']
            sage: y, z = R.gens()
            sage: R.an_element().integral(y).parent()
            Multivariate Polynomial Ring in y, z
             over Univariate Polynomial Ring in x over Rational Field

        On polynomials with coefficients in power series::

            sage: # needs sage.rings.number_field
            sage: R.<t> = PowerSeriesRing(QQbar)
            sage: S.<x, y> = PolynomialRing(R)
            sage: f = (t^2 + O(t^3))*x^2*y^3 + (37*t^4 + O(t^5))*x^3
            sage: f.parent()
            Multivariate Polynomial Ring in x, y
             over Power Series Ring in t over Algebraic Field
            sage: f.integral(x)   # with respect to x
            (1/3*t^2 + O(t^3))*x^3*y^3 + (37/4*t^4 + O(t^5))*x^4
            sage: f.integral(x).parent()
            Multivariate Polynomial Ring in x, y
             over Power Series Ring in t over Algebraic Field
            sage: f.integral(y)   # with respect to y
            (1/4*t^2 + O(t^3))*x^2*y^4 + (37*t^4 + O(t^5))*x^3*y
            sage: f.integral(t)   # with respect to t (recurses into base ring)
            (1/3*t^3 + O(t^4))*x^2*y^3 + (37/5*t^5 + O(t^6))*x^3

        TESTS::

            sage: f.integral()    # can't figure out the variable                       # needs sage.rings.number_field
            Traceback (most recent call last):
            ...
            ValueError: must specify which variable to integrate with respect to

        :issue:`34000`::

            sage: R = ZZ['x']['y,z']
            sage: y, z = R.gens()
            sage: parent(y.integral(y))
            Multivariate Polynomial Ring in y, z over Univariate Polynomial Ring in x over Rational Field
        """
    def factor(self, proof=None):
        '''
        Compute the irreducible factorization of this polynomial.

        INPUT:

        - ``proof`` -- insist on provably correct results (default: ``True``
          unless explicitly disabled for the ``\'polynomial\'`` subsystem with
          :class:`sage.structure.proof.proof.WithProof`.)

        TESTS:

        Check if we can handle polynomials with no variables, see :issue:`7950`::

            sage: P = PolynomialRing(ZZ,0,\'\')
            sage: res = P(10).factor(); res
            2 * 5
            sage: res[0][0].parent()
            Multivariate Polynomial Ring in no variables over Integer Ring
            sage: R = PolynomialRing(QQ,0,\'\')
            sage: res = R(10).factor(); res
            10
            sage: res.unit().parent()
            Rational Field
            sage: P(0).factor()
            Traceback (most recent call last):
            ...
            ArithmeticError: factorization of 0 is not defined

        Check if we can factor a constant polynomial, see :issue:`8207`::

            sage: R.<x,y> = CC[]                                                        # needs sage.rings.real_mpfr
            sage: R(1).factor()                                                         # needs sage.rings.real_mpfr
            1.00000000000000

        Check that we prohibit too large moduli, :issue:`11829`::

            sage: R.<x,y> = GF(previous_prime(2^31))[]                                  # needs sage.rings.finite_rings
            sage: factor(x + y + 1)                                                     # needs sage.rings.finite_rings
            Traceback (most recent call last):
            ...
            NotImplementedError: Factorization of multivariate polynomials
            over prime fields with characteristic > 2^29 is not implemented.

        Check that we can factor over the algebraic field (:issue:`25390`)::

            sage: # needs sage.libs.singular sage.rings.number_field
            sage: R.<x,y> = PolynomialRing(QQbar)
            sage: factor(x^2 + y^2)
            (x + (-1*I)*y) * (x + 1*I*y)

        Check that the global proof flag for polynomials is honored::

            sage: R.<x,y> = PolynomialRing(QQ[\'z\'])
            sage: f = x^2 + y^2
            sage: with proof.WithProof(\'polynomial\', True):
            ....:     f.factor()
            Traceback (most recent call last):
            ...
            NotImplementedError: Provably correct factorization not implemented.
            Disable this error by wrapping your code in a
            `with proof.WithProof(\'polynomial\', False):` block.
            sage: with proof.WithProof(\'polynomial\', False):
            ....:     f.factor()
            Traceback (most recent call last):
            ...
            TypeError: no conversion of this ring to a Singular ring defined

        We check that the original issue in :issue:`7554` is fixed::

            sage: K.<a> = PolynomialRing(QQ)
            sage: R.<x,y> = PolynomialRing(FractionField(K))
            sage: factor(x)                                                             # needs sage.libs.pari
            x

        In the example below, we set the special method
        ``_factor_multivariate_polynomial()`` in the base ring which is called to
        factor multivariate polynomials.  This facility can be used to easily
        extend polynomial factorization to work over new rings you introduce::

             sage: R.<x, y> = PolynomialRing(QQ[\'z\'])
             sage: (x*y).factor()
             Traceback (most recent call last):
             ...
             NotImplementedError: ...
             sage: R.base_ring()._factor_multivariate_polynomial = lambda f, **kwargs: f.change_ring(QQ).factor()
             sage: (x*y).factor()                                                       # needs sage.libs.pari
             y * x
             sage: del R.base_ring()._factor_multivariate_polynomial # clean up

        Check that a "multivariate" polynomial in one variable is factored
        correctly::

            sage: R.<z> = PolynomialRing(CC,1)                                          # needs sage.rings.real_mpfr
            sage: f = z^4 - 6*z + 3                                                     # needs sage.rings.real_mpfr
            sage: f.factor()                                                            # needs sage.libs.pari sage.rings.real_mpfr
            (z - 1.60443920904349) * (z - 0.511399619393097)
             * (z + 1.05791941421830 - 1.59281852704435*I)
             * (z + 1.05791941421830 + 1.59281852704435*I)

        We check a case that failed with an exception at some point::

            sage: # needs sage.rings.finite_rings
            sage: k.<u> = GF(4)
            sage: R.<v> = k[]
            sage: l.<v> = R.quo(v^3 + v + 1)
            sage: R.<x,y> = l[]
            sage: f = y^3 + x^3 + (u + 1)*x
            sage: f.factor()
            x^3 + y^3 + (u + 1)*x
        '''
    @handle_AA_and_QQbar
    def lift(self, I):
        """
        Given an ideal `I = (f_1,...,f_r)` and some `g` (= ``self``) in `I`, find
        `s_1,...,s_r` such that `g = s_1 f_1 + ... + s_r f_r`.

        ALGORITHM: Use Singular.

        EXAMPLES::

            sage: # needs sage.rings.real_mpfr
            sage: A.<x,y> = PolynomialRing(CC, 2, order='degrevlex')
            sage: I = A.ideal([x^10 + x^9*y^2, y^8 - x^2*y^7])
            sage: f = x*y^13 + y^12
            sage: M = f.lift(I); M                                                      # needs sage.libs.singular
            [y^7, x^7*y^2 + x^8 + x^5*y^3 + x^6*y + x^3*y^4 + x^4*y^2 + x*y^5 + x^2*y^3 + y^4]
            sage: sum(map(mul, zip(M, I.gens()))) == f                                  # needs sage.libs.singular
            True

        TESTS:

        Check that this method works over ``QQbar`` (:issue:`25351`)::

            sage: # needs sage.rings.number_field
            sage: A.<x,y> = QQbar[]
            sage: I = A.ideal([x^2 + y^2 - 1, x^2 - y^2])
            sage: f = 2*x^2 - 1
            sage: M = f.lift(I)                                                         # needs sage.libs.singular
            sage: sum(map(mul, zip(M, I.gens()))) == f                                  # needs sage.libs.singular
            True
        """
    @coerce_binop
    @handle_AA_and_QQbar
    def quo_rem(self, right):
        """
        Return quotient and remainder of ``self`` and ``right``.

        EXAMPLES::

            sage: R.<x,y> = CC[]                                                        # needs sage.rings.real_mpfr
            sage: f = y*x^2 + x + 1                                                     # needs sage.rings.real_mpfr
            sage: f.quo_rem(x)                                                          # needs sage.libs.singular sage.rings.real_mpfr
            (x*y + 1.00000000000000, 1.00000000000000)

            sage: R = QQ['a','b']['x','y','z']
            sage: p1 = R('a + (1+2*b)*x*y + (3-a^2)*z')
            sage: p2 = R('x-1')
            sage: p1.quo_rem(p2)                                                        # needs sage.libs.singular
            ((2*b + 1)*y, (2*b + 1)*y + (-a^2 + 3)*z + a)

            sage: R.<x,y> = Qp(5)[]                                                     # needs sage.rings.padics
            sage: x.quo_rem(y)                                                          # needs sage.libs.singular sage.rings.padics
            Traceback (most recent call last):
            ...
            TypeError: no conversion of this ring to a Singular ring defined

        ALGORITHM: Use Singular.

        TESTS:

        Check that this method works over ``QQbar`` (:issue:`25351`)::

            sage: R.<x,y> = QQbar[]                                                     # needs sage.rings.number_field
            sage: f = y*x^2 + x + 1                                                     # needs sage.rings.number_field
            sage: f.quo_rem(x)                                                          # needs sage.libs.singular sage.rings.number_field
            (x*y + 1, 1)
        """
    @handle_AA_and_QQbar
    def resultant(self, other, variable=None):
        """
        Compute the resultant of ``self`` and ``other`` with respect
        to ``variable``.

        If a second argument is not provided, the first variable of
        ``self.parent()`` is chosen.

        For inexact rings or rings not available in Singular,
        this computes the determinant of the Sylvester matrix.

        INPUT:

        - ``other`` -- polynomial in ``self.parent()``

        - ``variable`` -- (optional) variable (of type polynomial) in
          ``self.parent()``

        EXAMPLES::

            sage: P.<x,y> = PolynomialRing(QQ, 2)
            sage: a = x + y
            sage: b = x^3 - y^3
            sage: a.resultant(b)                                                        # needs sage.libs.singular
            -2*y^3
            sage: a.resultant(b, y)                                                     # needs sage.libs.singular
            2*x^3

        TESTS::

            sage: from sage.rings.polynomial.multi_polynomial_ring import MPolynomialRing_polydict_domain
            sage: P.<x,y> = MPolynomialRing_polydict_domain(QQ, 2, order='degrevlex')
            sage: a = x + y
            sage: b = x^3 - y^3
            sage: a.resultant(b)                                                        # needs sage.libs.singular
            -2*y^3
            sage: a.resultant(b, y)                                                     # needs sage.libs.singular
            2*x^3

        Check that :issue:`15061` is fixed::

            sage: R.<x, y> = AA[]                                                       # needs sage.rings.number_field
            sage: (x^2 + 1).resultant(x^2 - y)                                          # needs sage.libs.singular sage.rings.number_field
            y^2 + 2*y + 1

        Test for :issue:`2693`::

            sage: R.<x,y> = RR[]
            sage: p = x + y
            sage: q = x*y
            sage: p.resultant(q)                                                        # needs sage.libs.singular sage.modules
            -y^2

        Check that this method works over QQbar (:issue:`25351`)::

            sage: # needs sage.rings.number_field
            sage: P.<x,y> = QQbar[]
            sage: a = x + y
            sage: b = x^3 - y^3
            sage: a.resultant(b)                                                        # needs sage.libs.singular sage.modules
            (-2)*y^3
            sage: a.resultant(b, y)                                                     # needs sage.libs.singular sage.modules
            2*x^3
        """
    @coerce_binop
    @handle_AA_and_QQbar
    def subresultants(self, other, variable=None):
        """
        Return the nonzero subresultant polynomials of ``self`` and ``other``.

        INPUT:

        - ``other`` -- a polynomial

        OUTPUT: list of polynomials in the same ring as ``self``

        EXAMPLES::

            sage: # needs sage.libs.singular sage.rings.number_field
            sage: R.<x,y> = QQbar[]
            sage: p = (y^2 + 6)*(x - 1) - y*(x^2 + 1)
            sage: q = (x^2 + 6)*(y - 1) - x*(y^2 + 1)
            sage: p.subresultants(q, y)
            [2*x^6 + (-22)*x^5 + 102*x^4 + (-274)*x^3 + 488*x^2 + (-552)*x + 288,
             -x^3 - x^2*y + 6*x^2 + 5*x*y + (-11)*x + (-6)*y + 6]
            sage: p.subresultants(q, x)
            [2*y^6 + (-22)*y^5 + 102*y^4 + (-274)*y^3 + 488*y^2 + (-552)*y + 288,
             x*y^2 + y^3 + (-5)*x*y + (-6)*y^2 + 6*x + 11*y - 6]
        """
    def reduce(self, I):
        """
        Reduce this polynomial by the polynomials in `I`.

        INPUT:

        - ``I`` -- list of polynomials or an ideal

        EXAMPLES::

            sage: # needs sage.rings.number_field
            sage: P.<x,y,z> = QQbar[]
            sage: f1 = -2 * x^2 + x^3
            sage: f2 = -2 * y + x * y
            sage: f3 = -x^2 + y^2
            sage: F = Ideal([f1, f2, f3])
            sage: g = x*y - 3*x*y^2
            sage: g.reduce(F)                                                           # needs sage.libs.singular
            (-6)*y^2 + 2*y
            sage: g.reduce(F.gens())                                                    # needs sage.libs.singular
            (-6)*y^2 + 2*y

        ::

            sage: f = 3*x                                                               # needs sage.rings.number_field
            sage: f.reduce([2*x, y])                                                    # needs sage.rings.number_field
            0

        ::

            sage: # needs sage.rings.number_field
            sage: k.<w> = CyclotomicField(3)
            sage: A.<y9,y12,y13,y15> = PolynomialRing(k)
            sage: J = [y9 + y12]
            sage: f = y9 - y12; f.reduce(J)
            -2*y12
            sage: f = y13*y15; f.reduce(J)
            y13*y15
            sage: f = y13*y15 + y9 - y12; f.reduce(J)
            y13*y15 - 2*y12

        Make sure the remainder returns the correct type, fixing :issue:`13903`::

            sage: R.<y1,y2> = PolynomialRing(Qp(5), 2, order='lex')                     # needs sage.rings.padics
            sage: G = [y1^2 + y2^2, y1*y2 + y2^2, y2^3]                                 # needs sage.rings.padics
            sage: type((y2^3).reduce(G))                                                # needs sage.rings.padics
            <class 'sage.rings.polynomial.multi_polynomial_element.MPolynomial_polydict'>

        TESTS:

        Verify that :issue:`34105` is fixed::

            sage: R.<x,y> = AA[]                                                        # needs sage.rings.number_field
            sage: x.reduce(R.zero_ideal())                                              # needs sage.rings.number_field
            x
        """

def degree_lowest_rational_function(r, x):
    '''
    Return the difference of valuations of ``r`` with respect to variable ``x``.

    INPUT:

    - ``r`` -- a multivariate rational function

    - ``x`` -- a multivariate polynomial ring generator

    OUTPUT: integer; the difference `val_x(p) - val_x(q)` where `r = p/q`

    .. NOTE::

        This function should be made a method of the
        :class:`FractionFieldElement` class.

    EXAMPLES::

        sage: R1 = PolynomialRing(FiniteField(5), 3, names=["a", "b", "c"])
        sage: F = FractionField(R1)
        sage: a,b,c = R1.gens()
        sage: f = 3*a*b^2*c^3 + 4*a*b*c
        sage: g = a^2*b*c^2 + 2*a^2*b^4*c^7

    Consider the quotient
    `f/g = \\frac{4 + 3 bc^{2}}{ac + 2 ab^{3}c^{6}}` (note the
    cancellation).

    ::

        sage: # needs sage.rings.finite_rings
        sage: r = f/g; r
        (-2*b*c^2 - 1)/(2*a*b^3*c^6 + a*c)
        sage: degree_lowest_rational_function(r, a)
        -1
        sage: degree_lowest_rational_function(r, b)
        0
        sage: degree_lowest_rational_function(r, c)
        -1
    '''
