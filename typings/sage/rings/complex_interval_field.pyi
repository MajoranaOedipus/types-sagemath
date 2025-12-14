import sage.rings.abc
from _typeshed import Incomplete
from sage.misc.cachefunc import cached_method as cached_method
from sage.rings import complex_interval as complex_interval, integer as integer
from sage.rings.complex_mpfr import ComplexField as ComplexField
from sage.rings.integer_ring import ZZ as ZZ
from sage.rings.rational_field import QQ as QQ
from sage.rings.real_mpfi import RealIntervalField as RealIntervalField, RealIntervalField_class as RealIntervalField_class
from sage.rings.ring import Field as Field
from sage.structure.parent import Parent as Parent

cache: Incomplete

def ComplexIntervalField(prec: int = 53, names=None):
    """
    Return the complex interval field with real and imaginary parts having
    ``prec`` *bits* of precision.

    EXAMPLES::

        sage: ComplexIntervalField()
        Complex Interval Field with 53 bits of precision
        sage: ComplexIntervalField(100)
        Complex Interval Field with 100 bits of precision
        sage: ComplexIntervalField(100).base_ring()
        Real Interval Field with 100 bits of precision
        sage: i = ComplexIntervalField(200).gen()
        sage: i^2
        -1
        sage: i^i
        0.207879576350761908546955619834978770033877841631769608075136?
    """

class ComplexIntervalField_class(sage.rings.abc.ComplexIntervalField):
    """
    The field of complex (interval) numbers.

    EXAMPLES::

        sage: C = ComplexIntervalField(); C
        Complex Interval Field with 53 bits of precision
        sage: Q = RationalField()
        sage: C(1/3)
        0.3333333333333334?
        sage: C(1/3, 2)
        0.3333333333333334? + 2*I

    We can also coerce rational numbers and integers into ``C``, but
    coercing a polynomial will raise an exception::

        sage: Q = RationalField()
        sage: C(1/3)
        0.3333333333333334?
        sage: S.<x> = PolynomialRing(Q)
        sage: C(x)
        Traceback (most recent call last):
        ...
        TypeError: cannot convert nonconstant polynomial

    This illustrates precision::

        sage: CIF = ComplexIntervalField(10); CIF(1/3, 2/3)
        0.334? + 0.667?*I
        sage: CIF
        Complex Interval Field with 10 bits of precision
        sage: CIF = ComplexIntervalField(100); CIF
        Complex Interval Field with 100 bits of precision
        sage: z = CIF(1/3, 2/3); z
        0.333333333333333333333333333334? + 0.666666666666666666666666666667?*I

    We can load and save complex numbers and the complex interval field::

        sage: saved_z = loads(z.dumps())
        sage: saved_z.endpoints() == z.endpoints()
        True
        sage: loads(CIF.dumps()) == CIF
        True
        sage: k = ComplexIntervalField(100)
        sage: loads(dumps(k)) == k
        True

    This illustrates basic properties of a complex (interval) field::

        sage: CIF = ComplexIntervalField(200)
        sage: CIF.is_field()
        True
        sage: CIF.characteristic()
        0
        sage: CIF.precision()
        200
        sage: CIF.variable_name()
        'I'
        sage: CIF == ComplexIntervalField(200)
        True
        sage: CIF == ComplexIntervalField(53)
        False
        sage: CIF == 1.1
        False
        sage: CIF = ComplexIntervalField(53)

        sage: CIF.category()
        Category of infinite fields
        sage: TestSuite(CIF).run(skip='_test_gcd_vs_xgcd')

    TESTS:

    This checks that :issue:`15355` is fixed::

        sage: x + CIF(RIF(-2,2), 0)
        x + 0.?e1
        sage: x + CIF(RIF(-2,2), RIF(-2,2))
        x + 0.?e1 + 0.?e1*I
        sage: x + RIF(-2,2)
        x + 0.?e1
        sage: x + CIF(RIF(3.14,3.15), RIF(3.14, 3.15))
        x + 3.15? + 3.15?*I
        sage: CIF(RIF(-2,2), RIF(-2,2))
        0.?e1 + 0.?e1*I
        sage: x + CIF(RIF(3.14,3.15), 0)
        x + 3.15?

    Methods inherited from categories::

        sage: CIF.is_finite()
        False

    .. SEEALSO::

        - :mod:`sage.rings.real_mpfi`
        - :class:`sage.rings.complex_arb.ComplexBallField` (alternative
          implementation of complex intervals, with more features)
    """
    Element: Incomplete
    def __init__(self, prec: int = 53) -> None:
        """
        Initialize ``self``.

        EXAMPLES::

            sage: ComplexIntervalField()
            Complex Interval Field with 53 bits of precision
            sage: ComplexIntervalField(200)
            Complex Interval Field with 200 bits of precision
        """
    def __reduce__(self):
        """
        Used for pickling.

        TESTS::

            sage: loads(dumps(CIF)) == CIF
            True
        """
    def construction(self):
        """
        Return the functorial construction of this complex interval field,
        namely as the algebraic closure of the real interval field with
        the same precision.

        EXAMPLES::

            sage: c, S = CIF.construction(); c, S
            (AlgebraicClosureFunctor,
             Real Interval Field with 53 bits of precision)
            sage: CIF == c(S)
            True

        TESTS:

        Test that :issue:`19922` is fixed::

            sage: c = ComplexIntervalField(128).an_element()
            sage: r = RealIntervalField(64).an_element()
            sage: c + r
            1 + 1*I
            sage: r + c
            1 + 1*I
            sage: parent(c+r)
            Complex Interval Field with 64 bits of precision
            sage: R = ComplexIntervalField(128)['x']
            sage: (R.gen() * RIF.one()).parent()
            Univariate Polynomial Ring in x over Complex Interval Field with 53 bits of precision
        """
    def is_exact(self):
        """
        The complex interval field is not exact.

        EXAMPLES::

            sage: CIF.is_exact()
            False
        """
    def prec(self):
        """
        Return the precision of ``self`` (in bits).

        EXAMPLES::

            sage: CIF.prec()
            53
            sage: ComplexIntervalField(200).prec()
            200
        """
    def to_prec(self, prec):
        """
        Return a complex interval field with the given precision.

        EXAMPLES::

            sage: CIF.to_prec(150)
            Complex Interval Field with 150 bits of precision
            sage: CIF.to_prec(15)
            Complex Interval Field with 15 bits of precision
            sage: CIF.to_prec(53) is CIF
            True
        """
    precision = prec
    @cached_method
    def real_field(self):
        """
        Return the underlying :class:`RealIntervalField`.

        EXAMPLES::

            sage: R = CIF.real_field(); R
            Real Interval Field with 53 bits of precision
            sage: ComplexIntervalField(200).real_field()
            Real Interval Field with 200 bits of precision
            sage: CIF.real_field() is R
            True
        """
    @cached_method
    def middle_field(self):
        """
        Return the corresponding :class:`ComplexField` with the same precision
        as ``self``.

        EXAMPLES::

            sage: CIF.middle_field()
            Complex Field with 53 bits of precision
            sage: ComplexIntervalField(200).middle_field()
            Complex Field with 200 bits of precision
        """
    def __eq__(self, other):
        """
        Test whether ``self`` is equal to ``other``.

        If ``other`` is not a :class:`ComplexIntervalField_class`,
        return ``False``.  Otherwise, return ``True`` if ``self`` and
        ``other`` have the same precision.

        EXAMPLES::

            sage: CIF == ComplexIntervalField(200)
            False
            sage: CIF == CC
            False
            sage: CIF == CIF
            True
        """
    def __hash__(self):
        """
        Return the hash.

        EXAMPLES::

            sage: C = ComplexIntervalField(200)
            sage: from sage.rings.complex_interval_field import ComplexIntervalField_class
            sage: D = ComplexIntervalField_class(200)
            sage: hash(C) == hash(D)
            True
        """
    def __ne__(self, other):
        """
        Test whether ``self`` is not equal to ``other``.

        EXAMPLES::

            sage: CIF != ComplexIntervalField(200)
            True
            sage: CIF != CC
            True
            sage: CIF != CIF
            False
        """
    def __call__(self, x=None, im=None, **kwds):
        """
        Construct an element.

        EXAMPLES::

            sage: CIF(2) # indirect doctest
            2
            sage: CIF(CIF.0)
            1*I
            sage: CIF('1+I')
            Traceback (most recent call last):
            ...
            TypeError: unable to convert '1+I' to real interval
            sage: CIF(2,3)
            2 + 3*I
            sage: CIF(pi, e)                                                            # needs sage.symbolic
            3.141592653589794? + 2.718281828459046?*I
            sage: ComplexIntervalField(100)(CIF(RIF(2,3)))
            3.?

            sage: QQi.<i> = QuadraticField(-1)
            sage: CIF(i)
            1*I
            sage: QQi.<i> = QuadraticField(-1, embedding=CC(0,-1))
            sage: CIF(i)
            -1*I
            sage: QQi.<i> = QuadraticField(-1, embedding=None)
            sage: CIF(i)
            1*I

        ::

            sage: R.<x> = CIF[]
            sage: a = R(CIF(0,1)); a
            I
            sage: CIF(a)
            1*I
        """
    def characteristic(self):
        """
        Return the characteristic of the complex (interval) field, which is 0.

        EXAMPLES::

            sage: CIF.characteristic()
            0
        """
    def gen(self, n: int = 0):
        """
        Return the generator of the complex (interval) field.

        EXAMPLES::

            sage: CIF.0
            1*I
            sage: CIF.gen(0)
            1*I
        """
    def random_element(self, *args, **kwds):
        """
        Create a random element of ``self``.

        This simply chooses the real and imaginary part randomly, passing
        arguments and keywords to the underlying real interval field.

        EXAMPLES::

            sage: CIF.random_element().parent() is CIF
            True
            sage: re, im = CIF.random_element(10, 20)
            sage: 10 <= re <= 20
            True
            sage: 10 <= im <= 20
            True

        Passes extra positional or keyword arguments through::

            sage: re, im = CIF.random_element(max=0, min=-5)
            sage: -5 <= re <= 0
            True
            sage: -5 <= im <= 0
            True
        """
    def is_field(self, proof: bool = True):
        """
        Return ``True``, since the complex numbers are a field.

        EXAMPLES::

            sage: CIF.is_field()
            True
        """
    def pi(self):
        """
        Return `\\pi` as an element in the complex (interval) field.

        EXAMPLES::

            sage: ComplexIntervalField(100).pi()
            3.14159265358979323846264338328?
        """
    def ngens(self):
        """
        The number of generators of this complex (interval) field as an
        `\\RR`-algebra.

        There is one generator, namely ``sqrt(-1)``.

        EXAMPLES::

            sage: CIF.ngens()
            1
        """
    def zeta(self, n: int = 2):
        """
        Return a primitive `n`-th root of unity.

        .. TODO::

            Implement :class:`ComplexIntervalFieldElement` multiplicative order
            and set this output to have multiplicative order ``n``.

        INPUT:

        - ``n`` -- integer (default: 2)

        OUTPUT: a complex `n`-th root of unity

        EXAMPLES::

            sage: CIF.zeta(2)
            -1
            sage: CIF.zeta(5)
            0.309016994374948? + 0.9510565162951536?*I
        """
    def scientific_notation(self, status=None):
        """
        Set or return the scientific notation printing flag.

        If this flag is ``True`` then complex numbers with this space as parent
        print using scientific notation.

        EXAMPLES::

            sage: CIF((0.025, 2))
            0.025000000000000002? + 2*I
            sage: CIF.scientific_notation(True)
            sage: CIF((0.025, 2))
            2.5000000000000002?e-2 + 2*I
            sage: CIF.scientific_notation(False)
            sage: CIF((0.025, 2))
            0.025000000000000002? + 2*I
        """


from sage.categories.category import JoinCategory
class ComplexIntervalField_class_with_category(
    ComplexIntervalField_class, 
    JoinCategory.parent_class
):
    ... #TODO: check mro of CIF to decides exactly which classes to inherit from

CIF = ComplexIntervalField_class_with_category(53)