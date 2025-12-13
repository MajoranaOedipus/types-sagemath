from _typeshed import Incomplete
from sage.categories.rings import Rings as Rings
from sage.categories.semirings import Semirings as Semirings
from sage.misc.fast_methods import Singleton as Singleton
from sage.misc.lazy_import import lazy_import as lazy_import
from sage.rings.ring import CommutativeRing as CommutativeRing
from sage.structure.element import InfinityElement as InfinityElement, RingElement as RingElement
from sage.structure.parent import Parent as Parent
from sage.structure.richcmp import rich_to_bool as rich_to_bool, richcmp as richcmp

class _uniq:
    def __new__(cls, *args):
        """
        This ensures uniqueness of these objects.

        EXAMPLES::

            sage: sage.rings.infinity.UnsignedInfinityRing_class() is sage.rings.infinity.UnsignedInfinityRing_class()
            True
        """

class AnInfinity:
    """
    TESTS::

        sage: oo == oo
        True
        sage: oo < oo
        False
        sage: -oo < oo
        True
        sage: -oo < 3 < oo
        True

        sage: unsigned_infinity == 3
        False
        sage: unsigned_infinity == unsigned_infinity
        True
        sage: unsigned_infinity == oo
        True
    """
    def __pari__(self):
        """
        Convert ``self`` to a Pari object.

        EXAMPLES::

            sage: pari(-oo)                                                             # needs sage.libs.pari
            -oo
            sage: pari(oo)                                                              # needs sage.libs.pari
            +oo
        """
    def __abs__(self):
        """
        EXAMPLES::

            sage: [abs(x) for x in [UnsignedInfinityRing.gen(), oo, -oo]]
            [Infinity, +Infinity, +Infinity]
        """
    def __float__(self) -> float:
        """
        Generate a floating-point infinity.

        The printing of floating-point infinity varies across platforms.

        EXAMPLES::

            sage: RDF(infinity)
            +infinity
            sage: float(infinity) # random
            +infinity
            sage: CDF(infinity)                                                         # needs sage.rings.complex_double
            +infinity
            sage: infinity.__float__() # random
            +infinity

            sage: RDF(-infinity)
            -infinity
            sage: float(-infinity) # random
            -inf
            sage: CDF(-infinity)                                                        # needs sage.rings.complex_double
            -infinity
            sage: (-infinity).__float__() # random
            -inf
            sage: float(unsigned_infinity)
            Traceback (most recent call last):
            ...
            ValueError: unsigned infinity cannot be represented in a float
        """
    def lcm(self, x):
        """
        Return the least common multiple of ``oo`` and ``x``, which
        is by definition oo unless ``x`` is 0.

        EXAMPLES::

            sage: oo.lcm(0)
            0
            sage: oo.lcm(oo)
            +Infinity
            sage: oo.lcm(-oo)
            +Infinity
            sage: oo.lcm(10)
            +Infinity
            sage: (-oo).lcm(10)
            +Infinity
        """

class UnsignedInfinityRing_class(Singleton, Parent):
    def __init__(self) -> None:
        """
        Initialize ``self``.

        TESTS::

            sage: sage.rings.infinity.UnsignedInfinityRing_class() is sage.rings.infinity.UnsignedInfinityRing_class() is UnsignedInfinityRing
            True

        Sage can understand SymPy's complex infinity (:issue:`17493`)::

            sage: import sympy                                                          # needs sympy
            sage: SR(sympy.zoo)                                                         # needs sympy
            Infinity

        Some equality checks::

            sage: infinity == UnsignedInfinityRing.gen()
            True
            sage: UnsignedInfinityRing(3) == UnsignedInfinityRing(-19.5)
            True
        """
    def ngens(self) -> int:
        '''
        The unsigned infinity ring has one "generator."

        EXAMPLES::

            sage: UnsignedInfinityRing.ngens()
            1
            sage: len(UnsignedInfinityRing.gens())
            1
        '''
    def gen(self, n: int = 0):
        '''
        The "generator" of ``self`` is the infinity object.

        EXAMPLES::

            sage: UnsignedInfinityRing.gen()
            Infinity
            sage: UnsignedInfinityRing.gen(1)
            Traceback (most recent call last):
            ...
            IndexError: UnsignedInfinityRing only has one generator
        '''
    def gens(self) -> tuple:
        '''
        The "generator" of ``self`` is the infinity object.

        EXAMPLES::

            sage: UnsignedInfinityRing.gens()
            (Infinity,)
        '''
    def less_than_infinity(self):
        """
        This is the element that represents a finite value.

        EXAMPLES::

            sage: UnsignedInfinityRing.less_than_infinity()
            A number less than infinity
            sage: UnsignedInfinityRing(5) is UnsignedInfinityRing.less_than_infinity()
            True
        """

UnsignedInfinityRing: Incomplete

class LessThanInfinity(_uniq, RingElement):
    def __init__(self, parent=...) -> None:
        """
        Initialize ``self``.

        EXAMPLES::

            sage: sage.rings.infinity.LessThanInfinity() is UnsignedInfinityRing(5)
            True
        """
    def sign(self) -> None:
        """
        Raise an error because the sign of ``self`` is not well defined.

        EXAMPLES::

            sage: sign(UnsignedInfinityRing(2))
            Traceback (most recent call last):
            ...
            NotImplementedError: sign of number < oo is not well defined
            sage: sign(UnsignedInfinityRing(0))
            Traceback (most recent call last):
            ...
            NotImplementedError: sign of number < oo is not well defined
            sage: sign(UnsignedInfinityRing(-2))
            Traceback (most recent call last):
            ...
            NotImplementedError: sign of number < oo is not well defined
        """

class UnsignedInfinity(_uniq, AnInfinity, InfinityElement):
    def __init__(self) -> None:
        """
        Initialize ``self``.

        TESTS::

            sage: sage.rings.infinity.UnsignedInfinity() is sage.rings.infinity.UnsignedInfinity() is unsigned_infinity
            True
        """
    def __hash__(self):
        """
        TESTS::

            sage: hash(unsigned_infinity)
            9223372036854775806 # 64-bit
            2147483646          # 32-bit
        """

unsigned_infinity: Incomplete
less_than_infinity: Incomplete

def is_Infinite(x) -> bool:
    """
    This is a type check for infinity elements.

    EXAMPLES::

        sage: sage.rings.infinity.is_Infinite(oo)
        doctest:warning...
        DeprecationWarning: The function is_Infinite is deprecated;
        use 'isinstance(..., InfinityElement)' instead.
        See https://github.com/sagemath/sage/issues/38022 for details.
        True
        sage: sage.rings.infinity.is_Infinite(-oo)
        True
        sage: sage.rings.infinity.is_Infinite(unsigned_infinity)
        True
        sage: sage.rings.infinity.is_Infinite(3)
        False
        sage: sage.rings.infinity.is_Infinite(RR(infinity))
        False
        sage: sage.rings.infinity.is_Infinite(ZZ)
        False
    """

class SignError(ArithmeticError):
    """
    Sign error exception.
    """

class InfinityRing_class(Singleton, CommutativeRing):
    def __init__(self) -> None:
        """
        Initialize ``self``.

        TESTS::

            sage: sage.rings.infinity.InfinityRing_class() is sage.rings.infinity.InfinityRing_class() is InfinityRing
            True

        Comparison tests::

            sage: InfinityRing == InfinityRing
            True
            sage: InfinityRing == UnsignedInfinityRing
            False
        """
    def fraction_field(self) -> None:
        """
        This isn't really a ring, let alone an integral domain.

        TESTS::

            sage: InfinityRing.fraction_field()
            Traceback (most recent call last):
            ...
            TypeError: infinity 'ring' has no fraction field
        """
    def ngens(self) -> int:
        """
        The two generators are plus and minus infinity.

        EXAMPLES::

            sage: InfinityRing.ngens()
            2
            sage: len(InfinityRing.gens())
            2
        """
    def gen(self, n: int = 0):
        """
        The two generators are plus and minus infinity.

        EXAMPLES::

            sage: InfinityRing.gen(0)
            +Infinity
            sage: InfinityRing.gen(1)
            -Infinity
            sage: InfinityRing.gen(2)
            Traceback (most recent call last):
            ...
            IndexError: n must be 0 or 1
        """
    def gens(self) -> tuple:
        """
        The two generators are plus and minus infinity.

        EXAMPLES::

            sage: InfinityRing.gens()
            (+Infinity, -Infinity)
        """
    def is_zero(self) -> bool:
        """
        The Infinity Ring is not zero

        EXAMPLES::

           sage: InfinityRing.is_zero()
           False
        """
    def is_commutative(self) -> bool:
        """
        The Infinity Ring is commutative

        EXAMPLES::

            sage: InfinityRing.is_commutative()
            True
        """

class FiniteNumber(RingElement):
    value: Incomplete
    def __init__(self, parent, x) -> None:
        """
        Initialize ``self``.

        TESTS::

            sage: sage.rings.infinity.FiniteNumber(InfinityRing, 1)
            A positive finite number
            sage: sage.rings.infinity.FiniteNumber(InfinityRing, -1)
            A negative finite number
            sage: sage.rings.infinity.FiniteNumber(InfinityRing, 0)
            Zero
        """
    def __invert__(self):
        """
        EXAMPLES::

            sage: P = InfinityRing
            sage: ~P(2)
            A positive finite number
            sage: ~P(-7)
            A negative finite number
            sage: ~P(0)
            Traceback (most recent call last):
            ...
            ZeroDivisionError: Cannot divide by zero
        """
    def __abs__(self):
        """
        EXAMPLES::

            sage: abs(InfinityRing(-3))
            A positive finite number
            sage: abs(InfinityRing(3))
            A positive finite number
            sage: abs(InfinityRing(0))
            Zero
        """
    def sign(self):
        """
        Return the sign of ``self``.

        EXAMPLES::

            sage: sign(InfinityRing(2))
            1
            sage: sign(InfinityRing(0))
            0
            sage: sign(InfinityRing(-2))
            -1

        TESTS::

            sage: sgn(InfinityRing(7))
            1
            sage: sgn(InfinityRing(0))
            0
            sage: sgn(InfinityRing(-7))
            -1
        """
    def sqrt(self):
        """
        EXAMPLES::

            sage: InfinityRing(7).sqrt()
            A positive finite number
            sage: InfinityRing(0).sqrt()
            Zero
            sage: InfinityRing(-.001).sqrt()
            Traceback (most recent call last):
            ...
            SignError: cannot take square root of a negative number
        """

class MinusInfinity(_uniq, AnInfinity, InfinityElement):
    def __init__(self) -> None:
        """
        Initialize ``self``.

        TESTS::

            sage: sage.rings.infinity.MinusInfinity() is sage.rings.infinity.MinusInfinity() is -oo
            True
        """
    def __hash__(self):
        """
        TESTS::

            sage: hash(-infinity)
            -9223372036854775808 # 64-bit
            -2147483648          # 32-bit
        """
    def sqrt(self) -> None:
        """
        EXAMPLES::

            sage: (-oo).sqrt()
            Traceback (most recent call last):
            ...
            SignError: cannot take square root of negative infinity
        """

class PlusInfinity(_uniq, AnInfinity, InfinityElement):
    def __init__(self) -> None:
        """
        Initialize ``self``.

        TESTS::

            sage: sage.rings.infinity.PlusInfinity() is sage.rings.infinity.PlusInfinity() is oo
            True
        """
    def __hash__(self):
        """
        TESTS::

            sage: hash(+infinity)
            9223372036854775807 # 64-bit
            2147483647          # 32-bit
        """
    def sqrt(self):
        """
        The square root of ``self``.

        The square root of infinity is infinity.

        EXAMPLES::

            sage: oo.sqrt()
            +Infinity
        """

InfinityRing: Incomplete
infinity: Incomplete
Infinity = infinity
minus_infinity: Incomplete

def check_comparison(ring) -> None:
    """
    Check comparison with infinity.

    INPUT:

    - ``ring`` -- a sub-ring of the real numbers

    OUTPUT:

    Various attempts are made to generate elements of ``ring``. An
    assertion is triggered if one of these elements does not compare
    correctly with plus/minus infinity.

    EXAMPLES::

        sage: from sage.rings.infinity import check_comparison
        sage: rings = [ZZ, QQ, RDF]
        sage: rings += [RR, RealField(200)]                                             # needs sage.rings.real_mpfr
        sage: rings += [RLF, RIF]                                                       # needs sage.rings.real_interval_field
        sage: for R in rings:
        ....:     print('testing {}'.format(R))
        ....:     check_comparison(R)
        testing Integer Ring
        testing Rational Field
        testing Real Double Field...
        sage: check_comparison(AA)                                                       # needs sage.rings.number_field

    Comparison with number fields does not work::

        sage: x = polygen(ZZ, 'x')
        sage: K.<sqrt3> = NumberField(x^2 - 3)                                          # needs sage.rings.number_field
        sage: (-oo < 1 + sqrt3) and (1 + sqrt3 < oo)    # known bug                     # needs sage.rings.number_field
        False

    The symbolic ring handles its own infinities, but answers
    ``False`` (meaning: cannot decide) already for some very
    elementary comparisons::

        sage: check_comparison(SR)               # known bug                             # needs sage.symbolic
        Traceback (most recent call last):
        ...
        AssertionError: testing -1000.0 in Symbolic Ring: id = ...
    """
def check_signed_infinity(pos_inf) -> None:
    """
    Test consistency of infinity representations.

    There are different possible representations of infinity in
    Sage. These are all consistent with the infinity ring, that is,
    compare with infinity in the expected way. See also :issue:`14045`

    INPUT:

    - ``pos_inf`` -- a representation of positive infinity

    OUTPUT:

    An assertion error is raised if the representation is not
    consistent with the infinity ring.

    Check that :issue:`14045` is fixed::

        sage: InfinityRing(float('+inf'))
        +Infinity
        sage: InfinityRing(float('-inf'))
        -Infinity
        sage: oo > float('+inf')
        False
        sage: oo == float('+inf')
        True

    EXAMPLES::

        sage: from sage.rings.infinity import check_signed_infinity
        sage: check_signed_infinity(oo)
        sage: check_signed_infinity(float('+inf'))
        sage: check_signed_infinity(RLF(oo))                                             # needs sage.rings.real_interval_field
        sage: check_signed_infinity(RIF(oo))                                             # needs sage.rings.real_interval_field
        sage: check_signed_infinity(SR(oo))                                              # needs sage.symbolic
    """
