from _typeshed import Incomplete
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

TateAlgebra: Incomplete

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
