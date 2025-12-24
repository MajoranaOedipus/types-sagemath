r"""
Tate algebras

Let `K` be a finite extension of `\Bold{Q}_p` for some prime number `p`
and let `(v_1, \dots, v_n)` be a tuple of real numbers.

The associated Tate algebra consists of series of the form

.. MATH::

    \sum_{i_1,\dots,i_n \in \NN} a_{i_1,\dots,i_n} x_1^{i_1} \cdots x_n^{i_n}

for which the quantity

.. MATH::

    \operatorname{val}(a_{i_1,\dots,i_n}) - (v_1 i_1 + \cdots + v_n i_n)

goes to infinity when the multi-index `(i_1,\dots,i_n)` goes to infinity.

These series converge on the closed disc defined by the inequalities
`\operatorname{val}(x_i) \geq -v_i` for all `i \in \{1,\dots,n\}`. The `v_i`'s are
then the logarithms of the radii of convergence of the series in the
above Tate algebra; the will be called the log radii of convergence.

We can create Tate algebras using the constructor
:func:`sage.rings.tate_algebra.TateAlgebra`::

    sage: K = Qp(2, 5, print_mode='digits')
    sage: A.<x,y> = TateAlgebra(K); A
    Tate Algebra in x (val >= 0), y (val >= 0)
     over 2-adic Field with capped relative precision 5

As we observe, the default value for the log radii of convergence
is `0` (the series then converge on the closed unit disc).

We can specify different log radii using the following syntax::

    sage: B.<u,v> = TateAlgebra(K, log_radii=[1,2]); B
    Tate Algebra in u (val >= -1), v (val >= -2)
     over 2-adic Field with capped relative precision 5

Note that if we pass in the ring of integers of `p`-adic field,
the same Tate algebra is returned::

    sage: A1.<x,y> = TateAlgebra(K.integer_ring()); A1
    Tate Algebra in x (val >= 0), y (val >= 0)
     over 2-adic Field with capped relative precision 5
    sage: A is A1
    True

However the method :meth:`integer_ring` constructs the integer ring
of a Tate algebra, that is the subring consisting of series bounded
by `1` on the domain of convergence::

    sage: Ao = A.integer_ring(); Ao
    Integer ring of the Tate Algebra in x (val >= 0), y (val >= 0)
     over 2-adic Field with capped relative precision 5

Now we can build elements::

    sage: f = 5 + 2*x*y^3 + 4*x^2*y^2; f
    ...00101 + ...000010*x*y^3 + ...0000100*x^2*y^2
    sage: g = x^3*y + 2*x*y; g
    ...00001*x^3*y + ...000010*x*y

and perform all usual arithmetic operations on them::

    sage: f + g
    ...00001*x^3*y + ...00101 + ...000010*x*y^3 + ...000010*x*y + ...0000100*x^2*y^2
    sage: f * g
    ...00101*x^3*y + ...000010*x^4*y^4 + ...001010*x*y
     + ...0000100*x^5*y^3 + ...0000100*x^2*y^4 + ...00001000*x^3*y^3

An element in the integer ring is invertible if and only if its
reduction modulo `p` is a nonzero constant. In our example,
`f` is invertible (its reduction modulo `2` is `1`) but `g` is not::

    sage: f.inverse_of_unit()
    ...01101 + ...01110*x*y^3 + ...10100*x^2*y^6 + ... + O(2^5 * <x, y>)
    sage: g.inverse_of_unit()
    Traceback (most recent call last):
    ...
    ValueError: this series in not invertible

The notation `O(2^5)` in the result above hides a series which lies
in `2^5` times the integer ring of `A`, that is a series which is
bounded by `|2^5|` (`2`-adic norm) on the domain of convergence.

We can also evaluate series in a point of the domain of convergence
(in the base field or in an extension)::

    sage: L.<a> = Qq(2^3, 5)
    sage: f(a^2, 2*a)
    1 + 2^2 + a*2^4 + O(2^5)

    sage: u = polygen(ZZ, 'u')
    sage: L.<pi> = K.change(print_mode='series').extension(u^3 - 2)
    sage: g(pi, 2*pi)
    pi^7 + pi^8 + pi^19 + pi^20 + O(pi^21)

Computations with ideals in Tate algebras are also supported::

    sage: f = 7*x^3*y + 2*x*y - x*y^2 - 6*y^5
    sage: g = x*y^4 + 8*x^3 - 3*y^3 + 1
    sage: I = A.ideal([f, g])
    sage: I.groebner_basis()
    [...00001*x^2*y^3 + ...00001*y^4 + ...10001*x^2 + ... + O(2^5 * <x, y>),
     ...00001*x*y^4 + ...11101*y^3 + ...00001 + ... + O(2^5 * <x, y>),
     ...00001*y^5 + ...11111*x*y^3 + ...01001*x^2*y + ... + O(2^5 * <x, y>),
     ...00001*x^3 + ...01001*x*y + ...10110*y^4 + ...01110*x + O(2^5 * <x, y>)]

    sage: (x^2 + 3*y)*f + 1/2*(x^3*y + x*y)*g in I
    True


AUTHORS:

- Xavier Caruso, Thibaut Verron (2018-09)
"""
from sage.categories.algebras import Algebras as Algebras
from sage.categories.pushout import pushout as pushout
from sage.misc.misc_c import prod as prod
from sage.monoids.monoid import Monoid_class as Monoid_class
from sage.rings.integer_ring import ZZ as ZZ
from sage.rings.padics.padic_generic import pAdicGeneric as pAdicGeneric
from sage.rings.polynomial.polydict import ETuple as ETuple
from sage.rings.polynomial.term_order import TermOrder as TermOrder
from sage.rings.tate_algebra_element import TateAlgebraElement as TateAlgebraElement, TateAlgebraTerm as TateAlgebraTerm
from sage.structure.category_object import normalize_names as normalize_names
from sage.structure.factory import UniqueFactory as UniqueFactory
from sage.structure.parent import Parent as Parent
from sage.structure.unique_representation import UniqueRepresentation as UniqueRepresentation

class TateAlgebraFactory(UniqueFactory):
    """
    Construct a Tate algebra over a `p`-adic field.

    Given a `p`-adic field `K`, variables `X_1,\\dots,X_k`
    and convergence log radii `v_1, \\dots, v_n` in `\\RR`, the corresponding
    Tate algebra `K{X_1,\\dots,X_k}` consists of power series with
    coefficients `a_{i_1,\\dots,i_n}` in `K` such that

    .. MATH::

        \\operatorname{val}(a_{i_1,\\dots,i_n}) - (i_1 v_1 + \\cdots + i_n v_n)

    tends to infinity as `i_1,\\dots,i_n` go towards infinity.

    INPUT:

    - ``base`` -- a `p`-adic ring or field; if a ring is given, the
      Tate algebra over its fraction field will be constructed

    - ``prec`` -- integer or ``None`` (default: ``None``); the
      precision cap. It is used if an exact object must be truncated
      in order to do an arithmetic operation.
      If left as ``None``, it will be set to the precision cap of
      the base field.

    - ``log_radii`` -- integer or a list or a tuple of integers
      (default: ``0``); the value(s) `v_i`.
      If an integer is given, this will be the common value for all
      `v_i`.

    - ``names`` -- names of the indeterminates

    - ``order`` -- the monomial ordering (default: ``degrevlex``)
      used to break ties when comparing terms with the same
      coefficient valuation

    EXAMPLES::

        sage: R = Zp(2, 10, print_mode='digits'); R
        2-adic Ring with capped relative precision 10
        sage: A.<x,y> = TateAlgebra(R, order='lex'); A
        Tate Algebra in x (val >= 0), y (val >= 0)
         over 2-adic Field with capped relative precision 10

    We observe that the result is the Tate algebra over the fraction
    field of `R` and not `R` itself::

        sage: A.base_ring()
        2-adic Field with capped relative precision 10
        sage: A.base_ring() is R.fraction_field()
        True

    If we want to construct the ring of integers of the Tate algebra,
    we must use the method :meth:`integer_ring`::

        sage: Ao = A.integer_ring(); Ao
        Integer ring of the Tate Algebra in x (val >= 0), y (val >= 0)
         over 2-adic Field with capped relative precision 10
        sage: Ao.base_ring()
        2-adic Ring with capped relative precision 10
        sage: Ao.base_ring() is R
        True

    The term ordering is used (in particular) to determine how series are
    displayed. Terms are compared first according to the valuation of their
    coefficient, and ties are broken using the monomial ordering::

        sage: A.term_order()
        Lexicographic term order
        sage: f = 2 + y^5 + x^2; f
        ...0000000001*x^2 + ...0000000001*y^5 + ...00000000010
        sage: B.<x,y> = TateAlgebra(R); B
        Tate Algebra in x (val >= 0), y (val >= 0) over 2-adic Field with capped relative precision 10
        sage: B.term_order()
        Degree reverse lexicographic term order
        sage: B(f)
        ...0000000001*y^5 + ...0000000001*x^2 + ...00000000010

    Here are examples of Tate algebra with smaller radii of convergence::

        sage: B.<x,y> = TateAlgebra(R, log_radii=-1); B
        Tate Algebra in x (val >= 1), y (val >= 1) over 2-adic Field with capped relative precision 10
        sage: C.<x,y> = TateAlgebra(R, log_radii=[-1,-2]); C
        Tate Algebra in x (val >= 1), y (val >= 2) over 2-adic Field with capped relative precision 10

    AUTHORS:

    - Xavier Caruso, Thibaut Verron (2018-09)
    """
    def create_key(self, base, prec=None, log_radii=..., names=None, order: str = 'degrevlex'):
        """
        Create a key from the input parameters.

        INPUT:

        - ``base`` -- a `p`-adic ring or field

        - ``prec`` -- integer or ``None`` (default: ``None``)

        - ``log_radii`` -- integer or a list or a tuple of integers
          (default: ``0``)

        - ``names`` -- names of the indeterminates

        - ``order`` -- a monomial ordering (default: ``degrevlex``)

        EXAMPLES::

            sage: TateAlgebra.create_key(Zp(2), names=['x','y'])
            (2-adic Field with capped relative precision 20,
             20,
             (0, 0),
             ('x', 'y'),
             Degree reverse lexicographic term order)

        TESTS::

            sage: TateAlgebra.create_key(Zp(2))
            Traceback (most recent call last):
            ...
            ValueError: you must specify the names of the variables
            sage: TateAlgebra.create_key(ZZ)
            Traceback (most recent call last):
            ...
            TypeError: the base ring must be a p-adic ring or a p-adic field
            sage: TateAlgebra.create_key(Zp(2), names=['x','y'], log_radii=[1])
            Traceback (most recent call last):
            ...
            ValueError: the number of radii does not match the number of variables
            sage: TateAlgebra.create_key(Zp(2), names=['x','y'], log_radii=[0, 1/2])
            Traceback (most recent call last):
            ...
            NotImplementedError: only integral log_radii are implemented
            sage: TateAlgebra.create_key(Zp(2), names=['x','y'], order='myorder')
            Traceback (most recent call last):
            ...
            ValueError: unknown term order 'myorder'
        """
    def create_object(self, version, key):
        """
        Create an object using the given key.

        TESTS::

            sage: key = TateAlgebra.create_key(Zp(2), names=('x','y'))
            sage: TateAlgebra.create_object((8,4,6), key)
            Tate Algebra in x (val >= 0), y (val >= 0) over 2-adic Field with capped relative precision 20
        """

TateAlgebra: TateAlgebraFactory

class TateTermMonoid(Monoid_class, UniqueRepresentation):
    """
    A base class for Tate algebra terms.

    A term in a Tate algebra `K\\{X_1,\\dots,X_n\\}` (resp. in its ring of
    integers) is a monomial in this ring.

    Those terms form a pre-ordered monoid, with term multiplication and the
    term order of the parent Tate algebra.
    """
    Element = TateAlgebraTerm
    def __init__(self, A) -> None:
        """
        Initialize the Tate term monoid.

        INPUT:

        - ``A`` -- a Tate algebra

        EXAMPLES::

            sage: R = pAdicRing(2, 10)
            sage: A.<x,y> = TateAlgebra(R, log_radii=1)
            sage: T = A.monoid_of_terms(); T
            Monoid of terms in x (val >= -1), y (val >= -1) over 2-adic Field with capped relative precision 10

        TESTS::

            sage: A.<x,y> = TateAlgebra(Zp(2), log_radii=1)
            sage: T = A.monoid_of_terms()
            sage: TestSuite(T).run()
        """
    def prime(self):
        """
        Return the prime, that is the characteristic of the residue field.

        EXAMPLES::

            sage: R = Zp(3)
            sage: A.<x,y> = TateAlgebra(R)
            sage: T = A.monoid_of_terms()
            sage: T.prime()
            3
        """
    def algebra_of_series(self):
        """
        Return the Tate algebra corresponding to this Tate term monoid.

        EXAMPLES::

            sage: R = Zp(2, 10)
            sage: A.<x,y> = TateAlgebra(R)
            sage: T = A.monoid_of_terms()
            sage: T.algebra_of_series()
            Tate Algebra in x (val >= 0), y (val >= 0) over 2-adic Field with capped relative precision 10
            sage: T.algebra_of_series() is A
            True
        """
    def base_ring(self):
        """
        Return the base ring of this Tate term monoid.

        EXAMPLES::

            sage: R = Zp(2, 10)
            sage: A.<x,y> = TateAlgebra(R)
            sage: T = A.monoid_of_terms()
            sage: T.base_ring()
            2-adic Field with capped relative precision 10

        We observe that the base field is not ``R`` but its
        fraction field::

            sage: T.base_ring() is R
            False
            sage: T.base_ring() is R.fraction_field()
            True

        If we really want to create an integral Tate algebra,
        we have to invoke the method :meth:`integer_ring`::

            sage: Ao = A.integer_ring(); Ao
            Integer ring of the Tate Algebra in x (val >= 0), y (val >= 0) over 2-adic Field with capped relative precision 10
            sage: Ao.base_ring()
            2-adic Ring with capped relative precision 10
            sage: Ao.base_ring() is R
            True
        """
    def variable_names(self):
        """
        Return the names of the variables of this Tate term monoid.

        EXAMPLES::

            sage: R = Zp(2, 10)
            sage: A.<x,y> = TateAlgebra(R)
            sage: T = A.monoid_of_terms()
            sage: T.variable_names()
            ('x', 'y')
        """
    def log_radii(self):
        """
        Return the log radii of convergence of this Tate term monoid.

        EXAMPLES::

            sage: R = Zp(2, 10)
            sage: A.<x,y> = TateAlgebra(R)
            sage: T = A.monoid_of_terms()
            sage: T.log_radii()
            (0, 0)

            sage: B.<x,y> = TateAlgebra(R, log_radii=[1,2])
            sage: B.monoid_of_terms().log_radii()
            (1, 2)
        """
    def term_order(self):
        """
        Return the term order on this Tate term monoid.

        EXAMPLES::

            sage: R = Zp(2, 10)
            sage: A.<x,y> = TateAlgebra(R)
            sage: T = A.monoid_of_terms()
            sage: T.term_order()  # default term order is grevlex
            Degree reverse lexicographic term order

            sage: A.<x,y> = TateAlgebra(R, order='lex')
            sage: T = A.monoid_of_terms()
            sage: T.term_order()
            Lexicographic term order
        """
    def ngens(self):
        """
        Return the number of variables in the Tate term monoid.

        EXAMPLES::

            sage: R = Zp(2, 10)
            sage: A.<x,y> = TateAlgebra(R)
            sage: T = A.monoid_of_terms()
            sage: T.ngens()
            2
        """
    def gens(self) -> tuple:
        """
        Return the generators of this monoid of terms.

        EXAMPLES::

            sage: R = Zp(2, 10, print_mode='digits')
            sage: A.<x,y> = TateAlgebra(R)
            sage: T = A.monoid_of_terms()
            sage: T.gens()
            (...0000000001*x, ...0000000001*y)
        """
    def gen(self, n: int = 0):
        """
        Return the `n`-th generator of this monoid of terms.

        INPUT:

        - ``n`` -- integer (default: `0`); the index of
          the requested generator

        EXAMPLES::

            sage: R = Zp(2, 10, print_mode='digits')
            sage: A.<x,y> = TateAlgebra(R)
            sage: T = A.monoid_of_terms()
            sage: T.gen()
            ...0000000001*x
            sage: T.gen(0)
            ...0000000001*x
            sage: T.gen(1)
            ...0000000001*y
            sage: T.gen(2)
            Traceback (most recent call last):
            ...
            ValueError: generator not defined
        """
    def some_elements(self):
        """
        Return a list of elements in this monoid of terms.

        EXAMPLES::

            sage: R = Zp(2, 10, print_mode='digits')
            sage: A.<x,y> = TateAlgebra(R)
            sage: T = A.monoid_of_terms()
            sage: T.some_elements()
            [...00000000010, ...0000000001*x, ...0000000001*y, ...00000000010*x*y]
        """

class TateAlgebra_generic(Parent):
    element_class: Incomplete
    def __init__(self, field, prec, log_radii, names, order, integral: bool = False) -> None:
        """
        Initialize the Tate algebra.

        TESTS::

            sage: A.<x,y> = TateAlgebra(Zp(2), log_radii=1)
            sage: TestSuite(A).run()

        We check that univariate Tate algebras work correctly::

            sage: B.<t> = TateAlgebra(Zp(3))
        """
    def prime(self):
        """
        Return the prime, that is the characteristic of the residue field.

        EXAMPLES::

            sage: R = Zp(3)
            sage: A.<x,y> = TateAlgebra(R)
            sage: A.prime()
            3
        """
    def gen(self, n: int = 0):
        """
        Return the `n`-th generator of this Tate algebra.

        INPUT:

        - ``n`` -- integer (default: `0`); the index of
          the requested generator

        EXAMPLES::

            sage: R = Zp(2, 10, print_mode='digits')
            sage: A.<x,y> = TateAlgebra(R)
            sage: A.gen()
            ...0000000001*x
            sage: A.gen(0)
            ...0000000001*x
            sage: A.gen(1)
            ...0000000001*y
            sage: A.gen(2)
            Traceback (most recent call last):
            ...
            ValueError: generator not defined
        """
    def gens(self) -> tuple:
        """
        Return the generators of this Tate algebra.

        EXAMPLES::

            sage: R = Zp(2, 10, print_mode='digits')
            sage: A.<x,y> = TateAlgebra(R)
            sage: A.gens()
            (...0000000001*x, ...0000000001*y)
        """
    def ngens(self):
        """
        Return the number of generators of this algebra.

        EXAMPLES::

            sage: R = Zp(2, 10, print_mode='digits')
            sage: A.<x,y> = TateAlgebra(R)
            sage: A.ngens()
            2
        """
    def some_elements(self):
        """
        Return a list of elements in this Tate algebra.

        EXAMPLES::

            sage: R = Zp(2, 10, print_mode='digits')
            sage: A.<x,y> = TateAlgebra(R)
            sage: A.some_elements()
            [0,
             ...00000000010,
             ...0000000001*x,
             ...0000000001*y,
             ...00000000010*x*y,
             ...00000000100,
             ...0000000001*x + ...00000000010,
             ...0000000001*y + ...00000000010,
             ...00000000010*x*y + ...00000000010,
             ...0000000010*x,
             ...0000000001*x + ...0000000001*y,
             ...0000000001*x + ...00000000010*x*y,
             ...0000000010*y,
             ...0000000001*y + ...00000000010*x*y,
             ...00000000100*x*y]
        """
    def variable_names(self):
        """
        Return the names of the variables of this algebra.

        EXAMPLES::

            sage: R = Zp(2, 10, print_mode='digits')
            sage: A.<x,y> = TateAlgebra(R)
            sage: A.variable_names()
            ('x', 'y')
        """
    def log_radii(self):
        """
        Return the list of the log-radii of convergence radii defining
        this Tate algebra.

        EXAMPLES::

            sage: R = Zp(2, 10)
            sage: A.<x,y> = TateAlgebra(R)
            sage: A.log_radii()
            (0, 0)

            sage: B.<x,y> = TateAlgebra(R, log_radii=1)
            sage: B.log_radii()
            (1, 1)

            sage: C.<x,y> = TateAlgebra(R, log_radii=(1,-1))
            sage: C.log_radii()
            (1, -1)
        """
    def integer_ring(self):
        """
        Return the ring of integers (consisting of series bounded by
        1 in the domain of convergence) of this Tate algebra.

        EXAMPLES::

            sage: R = Zp(2, 10)
            sage: A.<x,y> = TateAlgebra(R)
            sage: Ao = A.integer_ring()
            sage: Ao
            Integer ring of the Tate Algebra in x (val >= 0), y (val >= 0) over 2-adic Field with capped relative precision 10

            sage: x in Ao
            True
            sage: x/2 in Ao
            False
        """
    def monoid_of_terms(self):
        """
        Return the monoid of terms of this Tate algebra.

        EXAMPLES::

            sage: R = Zp(2, 10)
            sage: A.<x,y> = TateAlgebra(R)
            sage: A.monoid_of_terms()
            Monoid of terms in x (val >= 0), y (val >= 0) over 2-adic Field with capped relative precision 10
        """
    def term_order(self):
        """
        Return the monomial order used in this algebra.

        EXAMPLES::

            sage: R = Zp(2, 10)
            sage: A.<x,y> = TateAlgebra(R)
            sage: A.term_order()
            Degree reverse lexicographic term order

            sage: A.<x,y> = TateAlgebra(R, order='lex')
            sage: A.term_order()
            Lexicographic term order
        """
    def precision_cap(self):
        """
        Return the precision cap of this Tate algebra.

        .. NOTE::

            The precision cap is the truncation precision
            used for arithmetic operations computed by
            successive approximations (as inversion).

        EXAMPLES:

        By default the precision cap is the precision cap of the
        field of coefficients::

            sage: R = Zp(2, 10)
            sage: A.<x,y> = TateAlgebra(R)
            sage: A.precision_cap()
            10

        But it could be different (either smaller or larger) if we
        ask to::

            sage: A.<x,y> = TateAlgebra(R, prec=5)
            sage: A.precision_cap()
            5

            sage: A.<x,y> = TateAlgebra(R, prec=20)
            sage: A.precision_cap()
            20
        """
    def absolute_e(self):
        """
        Return the absolute index of ramification of this
        Tate algebra.

        It is equal to the absolute index of ramification
        of the field of coefficients.

        EXAMPLES::

            sage: R = Zp(2)
            sage: A.<u,v> = TateAlgebra(R)
            sage: A.absolute_e()
            1

            sage: R.<a> = Zq(2^3)
            sage: A.<u,v> = TateAlgebra(R)
            sage: A.absolute_e()
            1

            sage: x = polygen(ZZ, 'x')
            sage: S.<a> = R.extension(x^2 - 2)
            sage: A.<u,v> = TateAlgebra(S)
            sage: A.absolute_e()
            2
        """
    def characteristic(self):
        """
        Return the characteristic of this algebra.

        EXAMPLES::

            sage: R = Zp(2, 10, print_mode='digits')
            sage: A.<x,y> = TateAlgebra(R)
            sage: A.characteristic()
            0
        """
    def random_element(self, degree: int = 2, terms: int = 5, integral: bool = False, prec=None):
        """
        Return a random element of this Tate algebra.

        INPUT:

        - ``degree`` -- integer (default: 2); an upper bound on
          the total degree of the result

        - ``terms`` -- integer (default: 5); the maximal number
          of terms of the result

        - ``integral`` -- boolean (default: ``False``); if ``True``
          the result will be in the ring of integers

        - ``prec`` -- (optional) an integer, the precision of the result

        EXAMPLES::

            sage: R = Zp(2, prec=10, print_mode='digits')
            sage: A.<x,y> = TateAlgebra(R)
            sage: A.random_element()  # random
            (...00101000.01)*y + ...1111011111*x^2 + ...0010010001*x*y
              + ...110000011 + ...010100100*y^2

            sage: A.random_element(degree=5, terms=3)  # random
            (...0101100.01)*x^2*y + (...01000011.11)*y^2 + ...00111011*x*y

            sage: A.random_element(integral=True)  # random
            ...0001111101*x + ...1101110101 + ...00010010110*y
             + ...101110001100*x*y + ...000001100100*y^2

        Note that if we are already working on the ring of integers,
        specifying ``integral=False`` has no effect::

            sage: Ao = A.integer_ring()
            sage: f = Ao.random_element(integral=False); f  # random
            ...1100111011*x^2 + ...1110100101*x + ...1100001101*y
             + ...1110110001 + ...01011010110*y^2
            sage: f in Ao
            True

        When the log radii are negative, integral series may have non
        integral coefficients::

            sage: B.<x,y> = TateAlgebra(R, log_radii=[-1,-2])
            sage: B.random_element(integral=True)  # random
            (...1111111.001)*x*y + (...111000101.1)*x + (...11010111.01)*y^2
             + ...0010011011*y + ...0010100011000
        """
    def is_integral_domain(self, proof: bool = True):
        """
        Return ``True`` since any Tate algebra is an integral domain.

        EXAMPLES::

            sage: A.<x,y> = TateAlgebra(Zp(3))
            sage: A.is_integral_domain()
            True

        TESTS:

        Check that :issue:`34372` is fixed::

            sage: A.<x,y> = TateAlgebra(Zp(3))
            sage: R.<a,b> = PolynomialRing(A)
            sage: R.is_integral_domain(proof=True)
            True
        """
