from sage.categories.algebras import Algebras as Algebras
from sage.categories.complete_discrete_valuation import CompleteDiscreteValuationFields as CompleteDiscreteValuationFields
from sage.categories.fields import Fields as Fields
from sage.categories.integral_domains import IntegralDomains as IntegralDomains
from sage.categories.rings import Rings as Rings
from sage.misc.cachefunc import cached_method as cached_method
from sage.misc.lazy_import import lazy_import as lazy_import
from sage.rings.infinity import infinity as infinity
from sage.rings.integer_ring import ZZ as ZZ
from sage.rings.laurent_series_ring_element import LaurentSeries as LaurentSeries
from sage.structure.parent import Parent as Parent
from sage.structure.unique_representation import UniqueRepresentation as UniqueRepresentation

def is_LaurentSeriesRing(x):
    """
    Return ``True`` if this is a *univariate* Laurent series ring.

    This is in keeping with the behavior of ``is_PolynomialRing``
    versus ``is_MPolynomialRing``.

    TESTS::

        sage: from sage.rings.laurent_series_ring import is_LaurentSeriesRing
        sage: K.<q> = LaurentSeriesRing(QQ)
        sage: is_LaurentSeriesRing(K)
        doctest:warning...
        DeprecationWarning: The function is_LaurentSeriesRing is deprecated;
        use 'isinstance(..., (LaurentSeriesRing, LazyLaurentSeriesRing))' instead.
        See https://github.com/sagemath/sage/issues/38290 for details.
        True
        sage: L.<z> = LazyLaurentSeriesRing(QQ)
        sage: is_LaurentSeriesRing(L)
        True
    """

class LaurentSeriesRing(UniqueRepresentation, Parent):
    '''
    Univariate Laurent Series Ring.

    EXAMPLES::

        sage: R = LaurentSeriesRing(QQ, \'x\'); R
        Laurent Series Ring in x over Rational Field
        sage: x = R.0
        sage: g = 1 - x + x^2 - x^4 + O(x^8); g
        1 - x + x^2 - x^4 + O(x^8)
        sage: g = 10*x^(-3) + 2006 - 19*x + x^2 - x^4 +O(x^8); g
        10*x^-3 + 2006 - 19*x + x^2 - x^4 + O(x^8)

    You can also use more mathematical notation when the base is a
    field::

        sage: Frac(QQ[[\'x\']])
        Laurent Series Ring in x over Rational Field
        sage: Frac(GF(5)[\'y\'])
        Fraction Field of Univariate Polynomial Ring in y over Finite Field of size 5

    When the base ring is a domain, the fraction field is the
    Laurent series ring over the fraction field of the base ring::

        sage: Frac(ZZ[[\'t\']])
        Laurent Series Ring in t over Rational Field

    Laurent series rings are determined by their variable and the base
    ring, and are globally unique::

        sage: # needs sage.rings.padics
        sage: K = Qp(5, prec=5)
        sage: L = Qp(5, prec=200)
        sage: R.<x> = LaurentSeriesRing(K)
        sage: S.<y> = LaurentSeriesRing(L)
        sage: R is S
        False
        sage: T.<y> = LaurentSeriesRing(Qp(5, prec=200))
        sage: S is T
        True
        sage: W.<y> = LaurentSeriesRing(Qp(5, prec=199))
        sage: W is T
        False

        sage: K = LaurentSeriesRing(CC, \'q\'); K                                         # needs sage.rings.real_mpfr
        Laurent Series Ring in q over Complex Field with 53 bits of precision
        sage: loads(K.dumps()) == K                                                     # needs sage.rings.real_mpfr
        True
        sage: P = QQ[[\'x\']]
        sage: F = Frac(P)
        sage: TestSuite(F).run()

    When the base ring `k` is a field, the ring `k((x))` is a CDVF, that is
    a field equipped with a discrete valuation for which it is complete.
    The appropriate (sub)category is automatically set in this case::

        sage: k = GF(11)
        sage: R.<x> = k[[]]
        sage: F = Frac(R)
        sage: F.category()
        Join of
         Category of complete discrete valuation fields and
         Category of commutative algebras over (finite enumerated fields and
         subquotients of monoids and quotients of semigroups) and
         Category of infinite sets
        sage: TestSuite(F).run()

    TESTS:

    Check if changing global series precision does it right (and
    that :issue:`17955` is fixed)::

        sage: set_series_precision(3)
        sage: R.<x> = LaurentSeriesRing(ZZ)
        sage: 1/(1 - 2*x)
        1 + 2*x + 4*x^2 + O(x^3)
        sage: set_series_precision(5)
        sage: R.<x> = LaurentSeriesRing(ZZ)
        sage: 1/(1 - 2*x)
        1 + 2*x + 4*x^2 + 8*x^3 + 16*x^4 + O(x^5)
        sage: set_series_precision(20)

    Check categories (:issue:`24420`)::

        sage: LaurentSeriesRing(ZZ, \'x\').category()
        Category of infinite commutative no zero divisors algebras
         over (Dedekind domains and euclidean domains
         and noetherian rings and infinite enumerated sets and metric spaces)
        sage: LaurentSeriesRing(QQ, \'x\').category()
        Join of Category of complete discrete valuation fields and Category of commutative algebras
         over (number fields and quotient fields and metric spaces) and Category of infinite sets
        sage: LaurentSeriesRing(Zmod(4), \'x\').category()
        Category of infinite commutative algebras
         over (finite commutative rings and subquotients of monoids and quotients of semigroups and finite enumerated sets)

    Check coercions (:issue:`24431`)::

        sage: pts = [LaurentSeriesRing,
        ....:        PolynomialRing,
        ....:        PowerSeriesRing,
        ....:        LaurentPolynomialRing]
        sage: LS = LaurentSeriesRing(QQ, \'x\')
        sage: LSx = LS.gen()

        sage: for P in pts:
        ....:     x = P(QQ, \'x\').gen()
        ....:     assert parent(LSx * x) is LS, "wrong parent for {}".format(P)

        sage: for P in pts:
        ....:     y = P(QQ, \'y\').gen()
        ....:     try:
        ....:         LSx * y
        ....:     except TypeError:
        ....:         pass
        ....:     else:
        ....:         print("wrong coercion {}".format(P))
    '''
    Element = LaurentSeries
    @staticmethod
    def __classcall__(cls, *args, **kwds):
        """
        TESTS::

            sage: L = LaurentSeriesRing(QQ, 'q')
            sage: L is LaurentSeriesRing(QQ, name='q')
            True
            sage: loads(dumps(L)) is L
            True

            sage: L.variable_names()
            ('q',)
            sage: L.variable_name()
            'q'
        """
    def __init__(self, power_series) -> None:
        """
        Initialization.

        EXAMPLES::

            sage: K.<q> = LaurentSeriesRing(QQ, default_prec=4); K
            Laurent Series Ring in q over Rational Field
            sage: 1 / (q-q^2)
            q^-1 + 1 + q + q^2 + O(q^3)

            sage: RZZ = LaurentSeriesRing(ZZ, 't')
            sage: RZZ.category()
            Category of infinite commutative no zero divisors algebras
             over (Dedekind domains and euclidean domains
             and noetherian rings and infinite enumerated sets
             and metric spaces)
            sage: TestSuite(RZZ).run()

            sage: R1 = LaurentSeriesRing(Zmod(1), 't')
            sage: R1.category()
            Category of finite commutative algebras
             over (finite commutative rings and subquotients of monoids and quotients of semigroups and finite enumerated sets)
            sage: TestSuite(R1).run()

            sage: R2 = LaurentSeriesRing(Zmod(2), 't')
            sage: R2.category()
            Join of Category of complete discrete valuation fields
                and Category of commutative algebras over (finite enumerated fields and subquotients of monoids and quotients of semigroups)
                and Category of infinite sets
            sage: TestSuite(R2).run()

            sage: R4 = LaurentSeriesRing(Zmod(4), 't')
            sage: R4.category()
            Category of infinite commutative algebras
             over (finite commutative rings and subquotients of monoids and quotients of semigroups and finite enumerated sets)
            sage: TestSuite(R4).run()

            sage: RQQ = LaurentSeriesRing(QQ, 't')
            sage: RQQ.category()
            Join of Category of complete discrete valuation fields
                and Category of commutative algebras over (number fields and quotient fields and metric spaces)
                and Category of infinite sets
            sage: TestSuite(RQQ).run()
        """
    def base_extend(self, R):
        """
        Return the Laurent series ring over R in the same variable as
        ``self``, assuming there is a canonical coerce map from the base ring
        of ``self`` to R.

        EXAMPLES::

            sage: K.<x> = LaurentSeriesRing(QQ, default_prec=4)
            sage: K.base_extend(QQ['t'])
            Laurent Series Ring in x over Univariate Polynomial Ring in t over Rational Field
        """
    def fraction_field(self):
        """
        Return the fraction field of this ring of Laurent series.

        If the base ring is a field, then Laurent series are already a field.
        If the base ring is a domain, then the Laurent series over its fraction
        field is returned. Otherwise, raise a :exc:`ValueError`.

        EXAMPLES::

            sage: R = LaurentSeriesRing(ZZ, 't', 30).fraction_field()
            sage: R
            Laurent Series Ring in t over Rational Field
            sage: R.default_prec()
            30

            sage: LaurentSeriesRing(Zmod(4), 't').fraction_field()
            Traceback (most recent call last):
            ...
            ValueError: must be an integral domain
        """
    def change_ring(self, R):
        """
        EXAMPLES::

            sage: K.<x> = LaurentSeriesRing(QQ, default_prec=4)
            sage: R = K.change_ring(ZZ); R
            Laurent Series Ring in x over Integer Ring
            sage: R.default_prec()
            4
        """
    def is_sparse(self):
        """
        Return if ``self`` is a sparse implementation.

        EXAMPLES::

            sage: K.<x> = LaurentSeriesRing(QQ, sparse=True)
            sage: K.is_sparse()
            True
        """
    def is_field(self, proof: bool = True):
        """
        A Laurent series ring is a field if and only if the base ring
        is a field.

        TESTS::

            sage: LaurentSeriesRing(QQ,'t').is_field()
            True
            sage: LaurentSeriesRing(ZZ,'t').is_field()
            False
        """
    def is_dense(self):
        """
        EXAMPLES::

            sage: K.<x> = LaurentSeriesRing(QQ, sparse=True)
            sage: K.is_dense()
            False
        """
    def random_element(self, algorithm: str = 'default'):
        """
        Return a random element of this Laurent series ring.

        The optional ``algorithm`` parameter decides how elements are generated.
        Algorithms currently implemented:

        - ``'default'``: Choose an integer ``shift`` using the standard
          distribution on the integers.  Then choose a list of coefficients
          using the ``random_element`` function of the base ring, and construct
          a new element based on those coefficients, so that the i-th
          coefficient corresponds to the (i+shift)-th power of the uniformizer.
          The amount of coefficients is determined by the ``default_prec``
          of the ring. Note that this method only creates non-exact elements.

        EXAMPLES::

            sage: S.<s> = LaurentSeriesRing(GF(3))
            sage: S.random_element()  # random
            s^-8 + s^-7 + s^-6 + s^-5 + s^-1 + s + s^3 + s^4
            + s^5 + 2*s^6 + s^7 + s^11 + O(s^12)
        """
    def construction(self):
        """
        Return the functorial construction of this Laurent power series ring.

        The construction is given as the completion of the Laurent polynomials.

        EXAMPLES::

            sage: L.<t> = LaurentSeriesRing(ZZ, default_prec=42)
            sage: phi, arg = L.construction()
            sage: phi
            Completion[t, prec=42]
            sage: arg
            Univariate Laurent Polynomial Ring in t over Integer Ring
            sage: phi(arg) is L
            True

        Because of this construction, pushout is automatically available::

            sage: 1/2 * t
            1/2*t
            sage: parent(1/2 * t)
            Laurent Series Ring in t over Rational Field

            sage: QQbar.gen() * t                                                       # needs sage.rings.number_field
            I*t
            sage: parent(QQbar.gen() * t)                                               # needs sage.rings.number_field
            Laurent Series Ring in t over Algebraic Field
        """
    def characteristic(self):
        """
        EXAMPLES::

            sage: R.<x> = LaurentSeriesRing(GF(17))
            sage: R.characteristic()
            17
        """
    def residue_field(self):
        """
        Return the residue field of this Laurent series field
        if it is a complete discrete valuation field (i.e. if
        the base ring is a field, in which base it is also the
        residue field).

        EXAMPLES::

            sage: R.<x> = LaurentSeriesRing(GF(17))
            sage: R.residue_field()
            Finite Field of size 17

            sage: R.<x> = LaurentSeriesRing(ZZ)
            sage: R.residue_field()
            Traceback (most recent call last):
            ...
            TypeError: the base ring is not a field
        """
    def default_prec(self):
        """
        Get the precision to which exact elements are truncated when
        necessary (most frequently when inverting).

        EXAMPLES::

            sage: R.<x> = LaurentSeriesRing(QQ, default_prec=5)
            sage: R.default_prec()
            5
        """
    def is_exact(self):
        '''
        Laurent series rings are inexact.

        EXAMPLES::

            sage: R = LaurentSeriesRing(QQ, "x")
            sage: R.is_exact()
            False
        '''
    @cached_method
    def gen(self, n: int = 0):
        '''
        EXAMPLES::

            sage: R = LaurentSeriesRing(QQ, "x")
            sage: R.gen()
            x
        '''
    def gens(self) -> tuple:
        '''
        EXAMPLES::

            sage: R = LaurentSeriesRing(QQ, "x")
            sage: R.gens()
            (x,)
        '''
    def uniformizer(self):
        """
        Return a uniformizer of this Laurent series field if it is
        a discrete valuation field (i.e. if the base ring is actually
        a field). Otherwise, an error is raised.

        EXAMPLES::

            sage: R.<t> = LaurentSeriesRing(QQ)
            sage: R.uniformizer()
            t

            sage: R.<t> = LaurentSeriesRing(ZZ)
            sage: R.uniformizer()
            Traceback (most recent call last):
            ...
            TypeError: the base ring is not a field
        """
    def ngens(self):
        '''
        Laurent series rings are univariate.

        EXAMPLES::

            sage: R = LaurentSeriesRing(QQ, "x")
            sage: R.ngens()
            1
        '''
    def polynomial_ring(self):
        '''
        If this is the Laurent series ring `R((t))`, return the
        polynomial ring `R[t]`.

        EXAMPLES::

            sage: R = LaurentSeriesRing(QQ, "x")
            sage: R.polynomial_ring()
            Univariate Polynomial Ring in x over Rational Field
        '''
    def laurent_polynomial_ring(self):
        '''
        If this is the Laurent series ring `R((t))`, return the Laurent
        polynomial ring `R[t,1/t]`.

        EXAMPLES::

            sage: R = LaurentSeriesRing(QQ, "x")
            sage: R.laurent_polynomial_ring()
            Univariate Laurent Polynomial Ring in x over Rational Field
        '''
    def power_series_ring(self):
        '''
        If this is the Laurent series ring `R((t))`, return the
        power series ring `R[[t]]`.

        EXAMPLES::

            sage: R = LaurentSeriesRing(QQ, "x")
            sage: R.power_series_ring()
            Power Series Ring in x over Rational Field
        '''
