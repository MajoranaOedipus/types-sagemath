from sage.categories.basic import QuotientFields as QuotientFields, Rings as Rings
from sage.categories.map import Section as Section
from sage.misc.cachefunc import cached_method as cached_method
from sage.rings import fraction_field_element as fraction_field_element, ring as ring
from sage.rings.integer_ring import ZZ as ZZ
from sage.structure.coerce import py_scalar_to_element as py_scalar_to_element
from sage.structure.coerce_maps import CallableConvertMap as CallableConvertMap, DefaultConvertMap_unique as DefaultConvertMap_unique
from sage.structure.element import parent as parent
from sage.structure.parent import Parent as Parent
from sage.structure.richcmp import richcmp as richcmp

def FractionField(R, names=None):
    """
    Create the fraction field of the integral domain ``R``.

    INPUT:

    - ``R`` -- an integral domain

    - ``names`` -- ignored

    EXAMPLES:

    We create some example fraction fields::

        sage: FractionField(IntegerRing())
        Rational Field
        sage: FractionField(PolynomialRing(RationalField(),'x'))
        Fraction Field of Univariate Polynomial Ring in x over Rational Field
        sage: FractionField(PolynomialRing(IntegerRing(),'x'))
        Fraction Field of Univariate Polynomial Ring in x over Integer Ring
        sage: FractionField(PolynomialRing(RationalField(),2,'x'))
        Fraction Field of Multivariate Polynomial Ring in x0, x1 over Rational Field

    Dividing elements often implicitly creates elements of the fraction
    field::

        sage: x = PolynomialRing(RationalField(), 'x').gen()
        sage: f = x/(x+1)
        sage: g = x**3/(x+1)
        sage: f/g
        1/x^2
        sage: g/f
        x^2

    The input must be an integral domain::

        sage: Frac(Integers(4))
        Traceback (most recent call last):
        ...
        TypeError: R must be an integral domain
    """
def is_FractionField(x) -> bool:
    """
    Test whether or not ``x`` inherits from :class:`FractionField_generic`.

    EXAMPLES::

        sage: from sage.rings.fraction_field import is_FractionField
        sage: is_FractionField(Frac(ZZ['x']))
        doctest:warning...
        DeprecationWarning: The function is_FractionField is deprecated;
        use 'isinstance(..., FractionField_generic)' instead.
        See https://github.com/sagemath/sage/issues/38128 for details.
        True
        sage: is_FractionField(QQ)
        False
    """

class FractionField_generic(ring.Field):
    """
    The fraction field of an integral domain.
    """
    def __init__(self, R, element_class=..., category=...) -> None:
        """
        Create the fraction field of the integral domain ``R``.

        INPUT:

        - ``R`` -- an integral domain

        EXAMPLES::

            sage: Frac(QQ['x'])
            Fraction Field of Univariate Polynomial Ring in x over Rational Field
            sage: Frac(QQ['x,y']).variable_names()
            ('x', 'y')
            sage: category(Frac(QQ['x']))
            Category of infinite quotient fields

        TESTS::

            sage: F = FractionField(QQ['x'])
            sage: F.cardinality()
            +Infinity
        """
    def __reduce__(self):
        """
        For pickling.

        TESTS::

            sage: K = Frac(QQ['x'])
            sage: loads(dumps(K)) is K
            True
        """
    def is_field(self, proof: bool = True):
        """
        Return ``True``, since the fraction field is a field.

        EXAMPLES::

            sage: Frac(ZZ).is_field()
            True
        """
    def is_finite(self):
        """
        Tells whether this fraction field is finite.

        .. NOTE::

            A fraction field is finite if and only if the associated
            integral domain is finite.

        EXAMPLES::

            sage: Frac(QQ['a','b','c']).is_finite()
            False
        """
    def base_ring(self):
        """
        Return the base ring of ``self``.

        This is the base ring of the ring
        which this fraction field is the fraction field of.

        EXAMPLES::

            sage: R = Frac(ZZ['t'])
            sage: R.base_ring()
            Integer Ring
        """
    def characteristic(self):
        """
        Return the characteristic of this fraction field.

        EXAMPLES::

            sage: R = Frac(ZZ['t'])
            sage: R.base_ring()
            Integer Ring
            sage: R = Frac(ZZ['t']); R.characteristic()
            0
            sage: R = Frac(GF(5)['w']); R.characteristic()
            5
        """
    def ring(self):
        """
        Return the ring that this is the fraction field of.

        EXAMPLES::

            sage: R = Frac(QQ['x,y'])
            sage: R
            Fraction Field of Multivariate Polynomial Ring in x, y over Rational Field
            sage: R.ring()
            Multivariate Polynomial Ring in x, y over Rational Field
        """
    @cached_method
    def is_exact(self):
        """
        Return if ``self`` is exact which is if the underlying ring is exact.

        EXAMPLES::

            sage: Frac(ZZ['x']).is_exact()
            True
            sage: Frac(CDF['x']).is_exact()                                             # needs sage.rings.complex_double
            False
        """
    def construction(self):
        """
        EXAMPLES::

            sage: Frac(ZZ['x']).construction()
            (FractionField, Univariate Polynomial Ring in x over Integer Ring)
            sage: K = Frac(GF(3)['t'])
            sage: f, R = K.construction()
            sage: f(R)
            Fraction Field of Univariate Polynomial Ring in t
             over Finite Field of size 3
            sage: f(R) == K
            True
        """
    def __eq__(self, other):
        """
        Check whether ``self`` is equal to ``other``.

        EXAMPLES::

            sage: Frac(ZZ['x']) == Frac(ZZ['x'])
            True
            sage: Frac(ZZ['x']) == Frac(QQ['x'])
            False
            sage: Frac(ZZ['x']) == Frac(ZZ['y'])
            False
            sage: Frac(ZZ['x']) == QQ['x']
            False
        """
    def __ne__(self, other):
        """
        Check whether ``self`` is not equal to ``other``.

        EXAMPLES::

            sage: Frac(ZZ['x']) != Frac(ZZ['x'])
            False
            sage: Frac(ZZ['x']) != Frac(QQ['x'])
            True
            sage: Frac(ZZ['x']) != Frac(ZZ['y'])
            True
            sage: Frac(ZZ['x']) != QQ['x']
            True
        """
    def __hash__(self):
        """
        Compute the hash of ``self``.

        EXAMPLES::

            sage: h0 = hash(Frac(ZZ['x']))
            sage: h1 = hash(Frac(ZZ['x']))
            sage: h2 = hash(Frac(QQ['x']))
            sage: h3 = hash(ZZ['x'])
            sage: h0 == h1 and h1 != h2 and h1 != h3
            True
        """
    def ngens(self):
        """
        This is the same as for the parent object.

        EXAMPLES::

            sage: R = Frac(PolynomialRing(QQ,'z',10)); R
            Fraction Field of Multivariate Polynomial Ring
             in z0, z1, z2, z3, z4, z5, z6, z7, z8, z9 over Rational Field
            sage: R.ngens()
            10
        """
    def gen(self, i: int = 0):
        """
        Return the ``i``-th generator of ``self``.

        EXAMPLES::

            sage: R = Frac(PolynomialRing(QQ,'z',10)); R
            Fraction Field of Multivariate Polynomial Ring
             in z0, z1, z2, z3, z4, z5, z6, z7, z8, z9 over Rational Field
            sage: R.0
            z0
            sage: R.gen(3)
            z3
            sage: R.3
            z3
        """
    def random_element(self, *args, **kwds):
        """
        Return a random element in this fraction field.

        The arguments are passed to the random generator of the underlying ring.

        EXAMPLES::

            sage: F = ZZ['x'].fraction_field()
            sage: F.random_element()  # random
            (2*x - 8)/(-x^2 + x)

        ::

            sage: f = F.random_element(degree=5)
            sage: f.numerator().degree() == f.denominator().degree()
            True
            sage: f.denominator().degree() <= 5
            True
            sage: while f.numerator().degree() != 5:
            ....:      f = F.random_element(degree=5)
        """
    def some_elements(self):
        """
        Return some elements in this field.

        EXAMPLES::

            sage: R.<x> = QQ[]
            sage: R.fraction_field().some_elements()
            [0,
             1,
             x,
             2*x,
             x/(x^2 + 2*x + 1),
             1/x^2,
             ...
             (2*x^2 + 2)/(x^2 + 2*x + 1),
             (2*x^2 + 2)/x^3,
             (2*x^2 + 2)/(x^2 - 1),
             2]
        """

class FractionField_1poly_field(FractionField_generic):
    """
    The fraction field of a univariate polynomial ring over a field.

    Many of the functions here are included for coherence with number fields.
    """
    def __init__(self, R, element_class=...) -> None:
        """
        Just change the default for ``element_class``.

        EXAMPLES::

            sage: R.<t> = QQ[]; K = R.fraction_field()
            sage: K._element_class
            <class 'sage.rings.fraction_field_element.FractionFieldElement_1poly_field'>
        """
    def ring_of_integers(self):
        """
        Return the ring of integers in this fraction field.

        EXAMPLES::

            sage: K = FractionField(GF(5)['t'])
            sage: K.ring_of_integers()
            Univariate Polynomial Ring in t over Finite Field of size 5
        """
    def maximal_order(self):
        """
        Return the maximal order in this fraction field.

        EXAMPLES::

            sage: K = FractionField(GF(5)['t'])
            sage: K.maximal_order()
            Univariate Polynomial Ring in t over Finite Field of size 5
        """
    def class_number(self):
        """
        Here for compatibility with number fields and function fields.

        EXAMPLES::

            sage: R.<t> = GF(5)[]; K = R.fraction_field()
            sage: K.class_number()
            1
        """
    def function_field(self):
        """
        Return the isomorphic function field.

        EXAMPLES::

            sage: R.<t> = GF(5)[]
            sage: K = R.fraction_field()
            sage: K.function_field()
            Rational function field in t over Finite Field of size 5

        .. SEEALSO::

            :meth:`sage.rings.function_field.RationalFunctionField.field`
        """

class FractionFieldEmbedding(DefaultConvertMap_unique):
    """
    The embedding of an integral domain into its field of fractions.

    EXAMPLES::

        sage: R.<x> = QQ[]
        sage: f = R.fraction_field().coerce_map_from(R); f
        Coercion map:
          From: Univariate Polynomial Ring in x over Rational Field
          To:   Fraction Field of Univariate Polynomial Ring in x over Rational Field

    TESTS::

        sage: from sage.rings.fraction_field import FractionFieldEmbedding
        sage: isinstance(f, FractionFieldEmbedding)
        True
        sage: TestSuite(f).run()

    Check that :issue:`23185` has been resolved::

        sage: R.<x> = QQ[]
        sage: K.<x> = FunctionField(QQ)
        sage: R.is_subring(K)
        True
        sage: R.is_subring(R.fraction_field())
        True
    """
    def is_surjective(self):
        """
        Return whether this map is surjective.

        EXAMPLES::

            sage: R.<x> = QQ[]
            sage: R.fraction_field().coerce_map_from(R).is_surjective()
            False
        """
    def is_injective(self):
        """
        Return whether this map is injective.

        EXAMPLES:

        The map from an integral domain to its fraction field is always
        injective::

            sage: R.<x> = QQ[]
            sage: R.fraction_field().coerce_map_from(R).is_injective()
            True
        """
    def section(self):
        """
        Return a section of this map.

        EXAMPLES::

            sage: R.<x> = QQ[]
            sage: R.fraction_field().coerce_map_from(R).section()
            Section map:
              From: Fraction Field of Univariate Polynomial Ring in x over Rational Field
              To:   Univariate Polynomial Ring in x over Rational Field
        """
    def __hash__(self):
        """
        Return a hash value for this embedding.

        EXAMPLES::

            sage: R.<x> = QQ[]
            sage: hash(R.fraction_field().coerce_map_from(R)) == hash(R.fraction_field().coerce_map_from(R))
            True
        """

class FractionFieldEmbeddingSection(Section):
    """
    The section of the embedding of an integral domain into its field of
    fractions.

    EXAMPLES::

        sage: R.<x> = QQ[]
        sage: f = R.fraction_field().coerce_map_from(R).section(); f
        Section map:
          From: Fraction Field of Univariate Polynomial Ring in x over Rational Field
          To:   Univariate Polynomial Ring in x over Rational Field

    TESTS::

        sage: from sage.rings.fraction_field import FractionFieldEmbeddingSection
        sage: isinstance(f, FractionFieldEmbeddingSection)
        True
        sage: TestSuite(f).run()
    """
    def __hash__(self):
        """
        Return a hash value for this section.

        EXAMPLES::

            sage: R.<x> = QQ[]
            sage: hash(R.fraction_field().coerce_map_from(R).section()) == hash(R.fraction_field().coerce_map_from(R).section())
            True
        """
