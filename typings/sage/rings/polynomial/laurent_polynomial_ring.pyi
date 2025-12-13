from _typeshed import Incomplete
from sage.misc.lazy_import import LazyImport as LazyImport
from sage.rings.polynomial.laurent_polynomial import LaurentPolynomial as LaurentPolynomial, LaurentPolynomial_univariate as LaurentPolynomial_univariate
from sage.rings.polynomial.laurent_polynomial_ring_base import LaurentPolynomialRing_generic as LaurentPolynomialRing_generic
from sage.rings.polynomial.polynomial_ring_constructor import PolynomialRing as PolynomialRing
from sage.structure.element import parent as parent

def is_LaurentPolynomialRing(R):
    """
    Return ``True`` if and only if R is a Laurent polynomial ring.

    EXAMPLES::

        sage: from sage.rings.polynomial.laurent_polynomial_ring import is_LaurentPolynomialRing
        sage: P = PolynomialRing(QQ, 2, 'x')
        sage: is_LaurentPolynomialRing(P)
        doctest:warning...
        DeprecationWarning: is_LaurentPolynomialRing is deprecated; use isinstance(...,
        sage.rings.polynomial.laurent_polynomial_ring_base.LaurentPolynomialRing_generic) instead
        See https://github.com/sagemath/sage/issues/35229 for details.
        False

        sage: R = LaurentPolynomialRing(QQ,3,'x')                                       # needs sage.modules
        sage: is_LaurentPolynomialRing(R)                                               # needs sage.modules
        True
    """
def LaurentPolynomialRing(base_ring, *args, **kwds):
    """
    Return the globally unique univariate or multivariate Laurent polynomial
    ring with given properties and variable name or names.

    There are four ways to call the Laurent polynomial ring constructor:

    1. ``LaurentPolynomialRing(base_ring, name,    sparse=False)``
    2. ``LaurentPolynomialRing(base_ring, names,   order='degrevlex')``
    3. ``LaurentPolynomialRing(base_ring, name, n, order='degrevlex')``
    4. ``LaurentPolynomialRing(base_ring, n, name, order='degrevlex')``

    The optional arguments ``sparse`` and ``order`` *must* be explicitly
    named, and the other arguments must be given positionally.

    INPUT:

    - ``base_ring`` -- a commutative ring
    - ``name`` -- string
    - ``names`` -- list or tuple of names, or a comma separated string
    - ``n`` -- positive integer
    - ``sparse`` -- boolean (default: ``False``); whether or not elements are sparse
    - ``order`` -- string or
      :class:`~sage.rings.polynomial.term_order.TermOrder`, e.g.,

      - ``'degrevlex'`` -- default; degree reverse lexicographic
      - ``'lex'`` -- lexicographic
      - ``'deglex'`` -- degree lexicographic
      - ``TermOrder('deglex',3) + TermOrder('deglex',3)`` -- block ordering

    OUTPUT:

    ``LaurentPolynomialRing(base_ring, name, sparse=False)`` returns a
    univariate Laurent polynomial ring; all other input formats return a
    multivariate Laurent polynomial ring.

    UNIQUENESS and IMMUTABILITY: In Sage there is exactly one
    single-variate Laurent polynomial ring over each base ring in each choice
    of variable and sparseness.  There is also exactly one multivariate
    Laurent polynomial ring over each base ring for each choice of names of
    variables and term order.

    ::

        sage: R.<x,y> = LaurentPolynomialRing(QQ, 2); R                                 # needs sage.modules
        Multivariate Laurent Polynomial Ring in x, y over Rational Field
        sage: f = x^2 - 2*y^-2                                                          # needs sage.modules

    You can't just globally change the names of those variables.
    This is because objects all over Sage could have pointers to
    that polynomial ring.

    ::

        sage: R._assign_names(['z','w'])                                                # needs sage.modules
        Traceback (most recent call last):
        ...
        ValueError: variable names cannot be changed after object creation.

    EXAMPLES:

    1. ``LaurentPolynomialRing(base_ring, name, sparse=False)``

       ::

           sage: LaurentPolynomialRing(QQ, 'w')
           Univariate Laurent Polynomial Ring in w over Rational Field

       Use the diamond brackets notation to make the variable
       ready for use after you define the ring::

           sage: R.<w> = LaurentPolynomialRing(QQ)
           sage: (1 + w)^3
           1 + 3*w + 3*w^2 + w^3

       You must specify a name::

           sage: LaurentPolynomialRing(QQ)
           Traceback (most recent call last):
           ...
           TypeError: you must specify the names of the variables

           sage: R.<abc> = LaurentPolynomialRing(QQ, sparse=True); R
           Univariate Laurent Polynomial Ring in abc over Rational Field

           sage: R.<w> = LaurentPolynomialRing(PolynomialRing(GF(7),'k')); R
           Univariate Laurent Polynomial Ring in w over
            Univariate Polynomial Ring in k over Finite Field of size 7

       Rings with different variables are different::

           sage: LaurentPolynomialRing(QQ, 'x') == LaurentPolynomialRing(QQ, 'y')
           False

    2. ``LaurentPolynomialRing(base_ring, names,   order='degrevlex')``

       ::

           sage: R = LaurentPolynomialRing(QQ, 'a,b,c'); R                              # needs sage.modules
           Multivariate Laurent Polynomial Ring in a, b, c over Rational Field

           sage: S = LaurentPolynomialRing(QQ, ['a','b','c']); S                        # needs sage.modules
           Multivariate Laurent Polynomial Ring in a, b, c over Rational Field

           sage: T = LaurentPolynomialRing(QQ, ('a','b','c')); T                        # needs sage.modules
           Multivariate Laurent Polynomial Ring in a, b, c over Rational Field

       All three rings are identical.

       ::

           sage: (R is S) and  (S is T)                                                 # needs sage.modules
           True

       There is a unique Laurent polynomial ring with each term order::

           sage: # needs sage.modules
           sage: R = LaurentPolynomialRing(QQ, 'x,y,z', order='degrevlex'); R
           Multivariate Laurent Polynomial Ring in x, y, z over Rational Field
           sage: S = LaurentPolynomialRing(QQ, 'x,y,z', order='invlex'); S
           Multivariate Laurent Polynomial Ring in x, y, z over Rational Field
           sage: S is LaurentPolynomialRing(QQ, 'x,y,z', order='invlex')
           True
           sage: R == S
           False


    3. ``LaurentPolynomialRing(base_ring, name, n, order='degrevlex')``

       If you specify a single name as a string and a number of
       variables, then variables labeled with numbers are created.

       ::

           sage: LaurentPolynomialRing(QQ, 'x', 10)                                     # needs sage.modules
           Multivariate Laurent Polynomial Ring in x0, x1, x2, x3, x4, x5, x6, x7, x8, x9
            over Rational Field

           sage: LaurentPolynomialRing(GF(7), 'y', 5)                                   # needs sage.modules
           Multivariate Laurent Polynomial Ring in y0, y1, y2, y3, y4
            over Finite Field of size 7

           sage: LaurentPolynomialRing(QQ, 'y', 3, sparse=True)                         # needs sage.modules
           Multivariate Laurent Polynomial Ring in y0, y1, y2 over Rational Field

       By calling the
       :meth:`~sage.structure.category_object.CategoryObject.inject_variables`
       method, all those variable names are available for interactive use::

           sage: R = LaurentPolynomialRing(GF(7), 15, 'w'); R                           # needs sage.modules
           Multivariate Laurent Polynomial Ring in w0, w1, w2, w3, w4, w5, w6, w7,
            w8, w9, w10, w11, w12, w13, w14 over Finite Field of size 7
           sage: R.inject_variables()                                                   # needs sage.modules
           Defining w0, w1, w2, w3, w4, w5, w6, w7, w8, w9, w10, w11, w12, w13, w14
           sage: (w0 + 2*w8 + w13)^2                                                    # needs sage.modules
           w0^2 + 4*w0*w8 + 4*w8^2 + 2*w0*w13 + 4*w8*w13 + w13^2
    """
def from_fraction_field(L, x):
    """
    Helper function to construct a Laurent polynomial from an element of its
    parent's fraction field.

    INPUT:

    - ``L`` -- an instance of :class:`LaurentPolynomialRing_generic`
    - ``x`` -- an element of the fraction field of ``L``

    OUTPUT:

    An instance of the element class of ``L``. If the denominator fails to be
    a unit in ``L`` an error is raised.

    EXAMPLES::

        sage: # needs sage.modules
        sage: from sage.rings.polynomial.laurent_polynomial_ring import from_fraction_field
        sage: L.<x, y> = LaurentPolynomialRing(ZZ)
        sage: F = L.fraction_field()
        sage: xi = F(~x)
        sage: from_fraction_field(L, xi) == ~x
        True
    """

class LaurentPolynomialRing_univariate(LaurentPolynomialRing_generic):
    def __init__(self, R) -> None:
        """
        EXAMPLES::

            sage: L = LaurentPolynomialRing(QQ,'x')
            sage: type(L)
            <class 'sage.rings.polynomial.laurent_polynomial_ring.LaurentPolynomialRing_univariate_with_category'>
            sage: TestSuite(L).run()

        TESTS::

            sage: TestSuite(LaurentPolynomialRing(Zmod(2), 'y')).run()
            sage: TestSuite(LaurentPolynomialRing(Zmod(4), 'y')).run()
            sage: TestSuite(LaurentPolynomialRing(ZZ, 'u')).run()
            sage: TestSuite(LaurentPolynomialRing(Zmod(2)['T'], 'u')).run()
            sage: TestSuite(LaurentPolynomialRing(Zmod(4)['T'], 'u')).run()
        """
    Element = LaurentPolynomial_univariate
    def monomial(self, arg):
        """
        Return the monomial with the given exponent.
        """
    def __reduce__(self):
        """
        Used in pickling.

        EXAMPLES::

            sage: L = LaurentPolynomialRing(QQ, 'x')
            sage: loads(dumps(L)) == L
            True
        """

class LaurentPolynomialRing_mpair(LaurentPolynomialRing_generic):
    def __init__(self, R) -> None:
        """
        EXAMPLES::

            sage: L = LaurentPolynomialRing(QQ,2,'x')                                   # needs sage.modules
            sage: type(L)                                                               # needs sage.modules
            <class
            'sage.rings.polynomial.laurent_polynomial_ring.LaurentPolynomialRing_mpair_with_category'>
            sage: L == loads(dumps(L))                                                  # needs sage.modules
            True
        """
    Element: Incomplete
    def monomial(self, *exponents):
        """
        Return the monomial whose exponents are given in argument.

        EXAMPLES::

            sage: # needs sage.modules
            sage: L = LaurentPolynomialRing(QQ, 'x', 2)
            sage: L.monomial(-3, 5)
            x0^-3*x1^5
            sage: L.monomial(1, 1)
            x0*x1
            sage: L.monomial(0, 0)
            1
            sage: L.monomial(-2, -3)
            x0^-2*x1^-3

            sage: x0, x1 = L.gens()                                                     # needs sage.modules
            sage: L.monomial(-1, 2) == x0^-1 * x1^2                                     # needs sage.modules
            True

            sage: L.monomial(1, 2, 3)                                                   # needs sage.modules
            Traceback (most recent call last):
            ...
            TypeError: tuple key (1, 2, 3) must have same length as ngens (= 2)

        We also allow to specify the exponents in a single tuple::

            sage: L.monomial((-1, 2))                                                   # needs sage.modules
            x0^-1*x1^2

            sage: L.monomial((-1, 2, 3))                                                # needs sage.modules
            Traceback (most recent call last):
            ...
            TypeError: tuple key (-1, 2, 3) must have same length as ngens (= 2)
        """
    def __reduce__(self):
        """
        Used in pickling.

        EXAMPLES::

            sage: L = LaurentPolynomialRing(QQ, 2, 'x')                                 # needs sage.modules
            sage: loads(dumps(L)) == L                                                  # needs sage.modules
            True
        """
