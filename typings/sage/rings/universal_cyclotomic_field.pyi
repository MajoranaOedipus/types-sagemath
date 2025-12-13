import sage.rings.abc
from _typeshed import Incomplete
from sage.categories.morphism import Morphism as Morphism
from sage.misc.cachefunc import cached_method as cached_method
from sage.rings.infinity import Infinity as Infinity
from sage.rings.integer import Integer as Integer
from sage.rings.integer_ring import ZZ as ZZ
from sage.rings.number_field.number_field_element_base import NumberFieldElement_base as NumberFieldElement_base
from sage.rings.qqbar import AA as AA, QQbar as QQbar
from sage.rings.rational import Rational as Rational
from sage.rings.rational_field import QQ as QQ
from sage.structure.coerce import py_scalar_to_element as py_scalar_to_element
from sage.structure.element import FieldElement as FieldElement, parent as parent
from sage.structure.parent import Parent as Parent
from sage.structure.richcmp import rich_to_bool as rich_to_bool
from sage.structure.unique_representation import UniqueRepresentation as UniqueRepresentation

libgap: Incomplete
GapElement_Integer: Incomplete
GapElement_Rational: Incomplete
GapElement_Cyclotomic: Incomplete
gap: Incomplete
gap3: Incomplete

def late_import() -> None:
    """
    This function avoids importing libgap on startup. It is called once through
    the constructor of :class:`UniversalCyclotomicField`.

    EXAMPLES::

        sage: import sage.rings.universal_cyclotomic_field as ucf
        sage: _ = UniversalCyclotomicField()   # indirect doctest
        sage: ucf.libgap is None               # indirect doctest
        False
    """
def UCF_sqrt_int(N, UCF):
    """
    Return the square root of the integer ``N``.

    EXAMPLES::

        sage: from sage.rings.universal_cyclotomic_field import UCF_sqrt_int
        sage: UCF = UniversalCyclotomicField()
        sage: UCF_sqrt_int(0, UCF)
        0
        sage: UCF_sqrt_int(1, UCF)
        1
        sage: UCF_sqrt_int(-1, UCF)
        E(4)
        sage: UCF_sqrt_int(2, UCF)
        E(8) - E(8)^3
        sage: UCF_sqrt_int(-2, UCF)
        E(8) + E(8)^3

    TESTS::

        sage: from sage.rings.universal_cyclotomic_field import UCF_sqrt_int
        sage: all(UCF_sqrt_int(ZZ(n), UCF)**2 == n for n in range(-10, 10))
        True
    """

class UCFtoQQbar(Morphism):
    """
    Conversion to ``QQbar``.

    EXAMPLES::

        sage: UCF = UniversalCyclotomicField()
        sage: QQbar(UCF.gen(3))
        -0.500000000000000? + 0.866025403784439?*I

        sage: CC(UCF.gen(7,2) + UCF.gen(7,6))
        0.400968867902419 + 0.193096429713793*I

        sage: complex(E(7)+E(7,2))
        (0.40096886790241915+1.7567593946498534j)
        sage: complex(UCF.one()/2)
        (0.5+0j)
    """
    def __init__(self, UCF) -> None:
        """
        INPUT:

        - ``UCF`` -- a universal cyclotomic field

        TESTS::

            sage: UCF = UniversalCyclotomicField()
            sage: UCF.coerce_embedding()
            Generic morphism:
              From: Universal Cyclotomic Field
              To:   Algebraic Field
        """

class UniversalCyclotomicFieldElement(FieldElement):
    def __init__(self, parent, obj) -> None:
        """
        INPUT:

        - ``parent`` -- a universal cyclotomic field

        - ``obj`` -- a libgap element (either an integer, a rational or a
          cyclotomic)

        TESTS::

            sage: UCF = UniversalCyclotomicField()
            sage: a = UCF.an_element()
            sage: TestSuite(a).run()
        """
    def __bool__(self) -> bool:
        """
        TESTS::

            sage: UCF = UniversalCyclotomicField()
            sage: list(map(bool, [UCF.zero(), UCF.one(), UCF.gen(3), UCF.gen(5) + UCF.gen(5,3)]))
            [False, True, True, True]
        """
    def __reduce__(self):
        """
        TESTS::

            sage: UCF = UniversalCyclotomicField()
            sage: a = UCF.zero()
            sage: loads(dumps(a))
            0
            sage: parent(_)
            Universal Cyclotomic Field

            sage: b = UCF.gen(5,1) - 3*UCF.gen(5,4)
            sage: c = loads(dumps(b))
            sage: c
            E(5) - 3*E(5)^4
            sage: c == b
            True
            sage: parent(c)
            Universal Cyclotomic Field
        """
    def __eq__(self, other) -> bool:
        """
        Equality test.

        EXAMPLES::

            sage: UCF = UniversalCyclotomicField()
            sage: UCF.one() == 1
            True
            sage: 1 == UCF.one()
            True

            sage: UCF(2/3) == 2/3
            True
            sage: 2/3 == UCF(2/3)
            True

            sage: UCF.gen(3) == UCF.gen(5)
            False
            sage: UCF.gen(5) + UCF.gen(3) == UCF.gen(3) + UCF.gen(5)
            True

            sage: UCF.zero() == None
            False

            sage: QQbar.zeta(5) == UCF.gen(5)
            True
            sage: UCF.gen(5) == QQbar.zeta(5)
            True
            sage: QQbar.zeta(5) == UCF.gen(5,2)
            False
            sage: UCF.gen(5,2) == QQbar.zeta(5)
            False
        """
    def __ne__(self, other) -> bool:
        """
        Difference test.

        EXAMPLES::

            sage: UCF = UniversalCyclotomicField()
            sage: UCF.one() != 1
            False
            sage: 1 != UCF.one()
            False

            sage: UCF(2/3) != 3/2
            True
            sage: 3/2 != UCF(2/3)
            True

            sage: UCF.gen(3) != UCF.gen(5)
            True
            sage: UCF.gen(3) + UCF.gen(5) != UCF.gen(5) + UCF.gen(3)
            False

            sage: UCF.gen(7) != QQbar.zeta(7)
            False
            sage: UCF.gen(7,2) != QQbar.zeta(7)
            True
        """
    def real(self):
        """
        Return the real part of this element.

        EXAMPLES::

            sage: E(3).real()
            -1/2
            sage: E(5).real()
            1/2*E(5) + 1/2*E(5)^4

            sage: a = E(5) - 2*E(3)
            sage: AA(a.real()) == QQbar(a).real()
            True
        """
    real_part = real
    def imag(self):
        """
        Return the imaginary part of this element.

        EXAMPLES::

            sage: E(3).imag()
            -1/2*E(12)^7 + 1/2*E(12)^11
            sage: E(5).imag()
            1/2*E(20) - 1/2*E(20)^9

            sage: a = E(5) - 2*E(3)
            sage: AA(a.imag()) == QQbar(a).imag()
            True
        """
    imag_part = imag
    def is_real(self) -> bool:
        """
        Test whether this element is real.

        EXAMPLES::

            sage: E(3).is_real()
            False
            sage: (E(3) + E(3,2)).is_real()
            True

            sage: a = E(3) - 2*E(7)
            sage: a.real_part().is_real()
            True
            sage: a.imag_part().is_real()
            True
        """
    def is_integral(self) -> bool:
        """
        Return whether ``self`` is an algebraic integer.

        This just wraps ``IsIntegralCyclotomic`` from GAP.

        .. SEEALSO:: :meth:`denominator`

        EXAMPLES::

            sage: E(6).is_integral()
            True
            sage: (E(4)/2).is_integral()
            False
        """
    def conductor(self):
        """
        Return the conductor of ``self``.

        EXAMPLES::

            sage: E(3).conductor()
            3
            sage: (E(5) + E(3)).conductor()
            15
        """
    def to_cyclotomic_field(self, R=None):
        """
        Return this element as an element of a cyclotomic field.

        EXAMPLES::

            sage: UCF = UniversalCyclotomicField()

            sage: UCF.gen(3).to_cyclotomic_field()
            zeta3
            sage: UCF.gen(3,2).to_cyclotomic_field()
            -zeta3 - 1

            sage: CF = CyclotomicField(5)
            sage: CF(E(5)) # indirect doctest
            zeta5

            sage: CF = CyclotomicField(7)
            sage: CF(E(5)) # indirect doctest
            Traceback (most recent call last):
            ...
            TypeError: cannot coerce zeta5 into Cyclotomic Field of order 7 and
            degree 6

            sage: CF = CyclotomicField(10)
            sage: CF(E(5)) # indirect doctest
            zeta10^2

        Matrices are correctly dealt with::

            sage: M = Matrix(UCF,2,[E(3),E(4),E(5),E(6)]); M
            [   E(3)    E(4)]
            [   E(5) -E(3)^2]

            sage: Matrix(CyclotomicField(60),M)  # indirect doctest
            [zeta60^10 - 1     zeta60^15]
            [    zeta60^12     zeta60^10]

        Using a non-standard embedding::

            sage: # needs sage.symbolic
            sage: CF = CyclotomicField(5, embedding=CC(exp(4*pi*i/5)))
            sage: x = E(5)
            sage: CC(x)
            0.309016994374947 + 0.951056516295154*I
            sage: CC(CF(x))
            0.309016994374947 + 0.951056516295154*I

        Test that the bug reported in :issue:`19912` has been fixed::

            sage: a = 1+E(4); a
            1 + E(4)
            sage: a.to_cyclotomic_field()
            zeta4 + 1
        """
    def __hash__(self):
        """
        EXAMPLES::

            sage: UCF = UniversalCyclotomicField()
            sage: hash(UCF.zero())  # indirect doctest
            0
            sage: hash(UCF.gen(3,2)) == hash((3,0,0,1))
            True

        TESTS:

        See :issue:`19514`::

            sage: hash(UCF.one())
            1
        """
    def __float__(self) -> float:
        """
        TESTS::

            sage: float(E(7) + E(7,6))
            1.246979603717467
        """
    def __complex__(self) -> complex:
        """
        TESTS::

            sage: complex(E(3))
            (-0.5+0.8660254037844386j)
        """
    def denominator(self):
        """
        Return the denominator of this element.

        .. SEEALSO:: :meth:`is_integral`

        EXAMPLES::

            sage: a = E(5) + 1/2*E(5,2) + 1/3*E(5,3)
            sage: a
            E(5) + 1/2*E(5)^2 + 1/3*E(5)^3
            sage: a.denominator()
            6
            sage: parent(_)
            Integer Ring
        """
    def multiplicative_order(self):
        """
        Return the multiplicative order.

        EXAMPLES::

            sage: E(5).multiplicative_order()
            5
            sage: (E(5) + E(12)).multiplicative_order()
            +Infinity
            sage: UniversalCyclotomicField().zero().multiplicative_order()
            Traceback (most recent call last):
            ...
            GAPError: Error, argument must be nonzero
        """
    def additive_order(self):
        """
        Return the additive order.

        EXAMPLES::

            sage: UCF = UniversalCyclotomicField()
            sage: UCF.zero().additive_order()
            0
            sage: UCF.one().additive_order()
            +Infinity
            sage: UCF.gen(3).additive_order()
            +Infinity
        """
    def is_rational(self) -> bool:
        """
        Test whether this element is a rational number.

        EXAMPLES::

            sage: E(3).is_rational()
            False
            sage: (E(3) + E(3,2)).is_rational()
            True

        TESTS::

            sage: type(E(3).is_rational())
            <... 'bool'>
        """
    def __neg__(self):
        """
        Return the inverse of ``self``.

        TESTS::

            sage: -E(5)
            -E(5)
        """
    def __invert__(self):
        """
        TESTS::

            sage: UCF = UniversalCyclotomicField()
            sage: ~(UCF.one())
            1
            sage: ~UCF.gen(4)
            -E(4)
        """
    inverse = __invert__
    def is_square(self) -> bool:
        """
        EXAMPLES::

            sage: UCF = UniversalCyclotomicField()
            sage: UCF(5/2).is_square()
            True

            sage: UCF.zeta(7,3).is_square()
            True

            sage: (2 + UCF.zeta(3)).is_square()
            Traceback (most recent call last):
            ...
            NotImplementedError: is_square() not fully implemented for elements of Universal Cyclotomic Field
        """
    def sqrt(self, extend: bool = True, all: bool = False):
        """
        Return a square root of ``self``.

        With default options, the output is an element of the universal
        cyclotomic field when this element is expressed via a single root
        of unity (including rational numbers). Otherwise, return an algebraic
        number.

        INPUT:

        - ``extend`` -- boolean (default: ``True``); if ``True``, might return
          a square root in the algebraic closure of the rationals. If
          ``False``, return a square root in the universal cyclotomic field or
          raises an error.

        - ``all`` -- boolean (default: ``False``); if ``True``, return a
          list of all square roots

        EXAMPLES::

            sage: UCF = UniversalCyclotomicField()
            sage: UCF(3).sqrt()
            E(12)^7 - E(12)^11
            sage: (UCF(3).sqrt())**2
            3

            sage: r = UCF(-1400 / 143).sqrt()
            sage: r**2
            -1400/143

            sage: E(33).sqrt()
            -E(33)^17
            sage: E(33).sqrt() ** 2
            E(33)

            sage: (3 * E(5)).sqrt()
            -E(60)^11 + E(60)^31
            sage: (3 * E(5)).sqrt() ** 2
            3*E(5)

        Setting ``all=True`` you obtain the two square roots in a list::

            sage: UCF(3).sqrt(all=True)
            [E(12)^7 - E(12)^11, -E(12)^7 + E(12)^11]
            sage: (1 + UCF.zeta(5)).sqrt(all=True)
            [1.209762576525833? + 0.3930756888787117?*I,
             -1.209762576525833? - 0.3930756888787117?*I]

        In the following situation, Sage is not (yet) able to compute a
        square root within the universal cyclotomic field::

            sage: (E(5) + E(5, 2)).sqrt()
            0.7476743906106103? + 1.029085513635746?*I
            sage: (E(5) + E(5, 2)).sqrt(extend=False)
            Traceback (most recent call last):
            ...
            NotImplementedError: sqrt() not fully implemented for elements of Universal Cyclotomic Field
        """
    def conjugate(self):
        """
        Return the complex conjugate.

        EXAMPLES::

            sage: (E(7) + 3*E(7,2) - 5 * E(7,3)).conjugate()
            -5*E(7)^4 + 3*E(7)^5 + E(7)^6
        """
    def galois_conjugates(self, n=None) -> list:
        """
        Return the Galois conjugates of ``self``.

        INPUT:

        - ``n`` -- an optional integer. If provided, return the orbit of the
          Galois group of the ``n``-th cyclotomic field over `\\QQ`. Note that
          ``n`` must be such that this element belongs to the ``n``-th
          cyclotomic field (in other words, it must be a multiple of the
          conductor).

        EXAMPLES::

            sage: E(6).galois_conjugates()
            [-E(3)^2, -E(3)]

            sage: E(6).galois_conjugates()
            [-E(3)^2, -E(3)]

            sage: (E(9,2) - E(9,4)).galois_conjugates()
            [E(9)^2 - E(9)^4,
             E(9)^2 + E(9)^4 + E(9)^5,
             -E(9)^2 - E(9)^5 - E(9)^7,
             -E(9)^2 - E(9)^4 - E(9)^7,
             E(9)^4 + E(9)^5 + E(9)^7,
             -E(9)^5 + E(9)^7]

            sage: zeta = E(5)
            sage: zeta.galois_conjugates(5)
            [E(5), E(5)^2, E(5)^3, E(5)^4]
            sage: zeta.galois_conjugates(10)
            [E(5), E(5)^3, E(5)^2, E(5)^4]
            sage: zeta.galois_conjugates(15)
            [E(5), E(5)^2, E(5)^4, E(5)^2, E(5)^3, E(5), E(5)^3, E(5)^4]

            sage: zeta.galois_conjugates(17)
            Traceback (most recent call last):
            ...
            ValueError: n = 17 must be a multiple of the conductor (5)
        """
    def __abs__(self):
        """
        Return the absolute value (or complex modulus) of ``self``.

        The absolute value is returned as an algebraic real number.

        EXAMPLES::

            sage: f = 5/2*E(3)+E(5)/7
            sage: f.abs()
            2.597760303873084?
            sage: abs(f)
            2.597760303873084?
            sage: a = E(8)
            sage: abs(a)
            1
            sage: v, w = vector([a]), vector([a, a])
            sage: v.norm(), w.norm()
            (1, 1.414213562373095?)
            sage: v.norm().parent()
            Algebraic Real Field

        TESTS::

            sage: [abs(E(n)) for n in range(1, 11)]
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
            sage: UniversalCyclotomicField().zero().abs()
            0
        """
    abs = __abs__
    def norm_of_galois_extension(self):
        """
        Return the norm as a Galois extension of `\\QQ`, which is
        given by the product of all galois_conjugates.

        EXAMPLES::

            sage: E(3).norm_of_galois_extension()
            1
            sage: E(6).norm_of_galois_extension()
            1
            sage: (E(2) + E(3)).norm_of_galois_extension()
            3
            sage: parent(_)
            Integer Ring
        """
    def minpoly(self, var: str = 'x'):
        """
        The minimal polynomial of ``self`` element over `\\QQ`.

        INPUT:

        - ``var`` -- (default: ``'x'``) the name of the variable to use

        EXAMPLES::

            sage: UCF.<E> = UniversalCyclotomicField()

            sage: UCF(4).minpoly()
            x - 4

            sage: UCF(4).minpoly(var='y')
            y - 4

            sage: E(3).minpoly()
            x^2 + x + 1

            sage: E(3).minpoly(var='y')
            y^2 + y + 1

        TESTS::

            sage: for elt in UCF.some_elements():
            ....:     assert elt.minpoly() == elt.to_cyclotomic_field().minpoly()
            ....:     assert elt.minpoly(var='y') == elt.to_cyclotomic_field().minpoly(var='y')

        .. TODO::

            Polynomials with libgap currently does not implement a ``.sage()`` method
            (see :issue:`18266`). It would be faster/safer to not use string to
            construct the polynomial.
        """

class UniversalCyclotomicField(UniqueRepresentation, sage.rings.abc.UniversalCyclotomicField):
    """
    The universal cyclotomic field.

    The universal cyclotomic field is the infinite algebraic extension of `\\QQ`
    generated by the roots of unity. It is also the maximal Abelian extension of
    `\\QQ` in the sense that any Abelian Galois extension of `\\QQ` is also a
    subfield of the universal cyclotomic field.
    """
    Element = UniversalCyclotomicFieldElement
    @staticmethod
    def __classcall__(cls, names=None):
        """
        Just ignoring the argument ``names``.

        TESTS::

            sage: UCF.<E> = UniversalCyclotomicField()
            sage: E(3,1)
            E(3)
            sage: E(3,2)
            E(3)^2
        """
    def __init__(self, names=None) -> None:
        """
        TESTS::

            sage: UCF = UniversalCyclotomicField()
            sage: TestSuite(UCF).run()

            sage: UniversalCyclotomicField().is_finite()
            False
        """
    def an_element(self):
        """
        Return an element.

        EXAMPLES::

            sage: UniversalCyclotomicField().an_element()
            E(5) - 3*E(5)^2
        """
    def some_elements(self) -> tuple:
        """
        Return a tuple of some elements in the universal cyclotomic field.

        EXAMPLES::

            sage: UniversalCyclotomicField().some_elements()
            (0, 1, -1, E(3), E(7) - 2/3*E(7)^2)
            sage: all(parent(x) is UniversalCyclotomicField() for x in _)
            True
        """
    def is_exact(self) -> bool:
        """
        Return ``True`` as this is an exact ring (i.e. not numerical).

        EXAMPLES::

            sage: UniversalCyclotomicField().is_exact()
            True
        """
    @cached_method
    def zero(self):
        """
        Return zero.

        EXAMPLES::

            sage: UCF = UniversalCyclotomicField()
            sage: UCF.zero()
            0
            sage: parent(_)
            Universal Cyclotomic Field
        """
    @cached_method
    def one(self):
        """
        Return one.

        EXAMPLES::

            sage: UCF = UniversalCyclotomicField()
            sage: UCF.one()
            1
            sage: parent(_)
            Universal Cyclotomic Field
        """
    def characteristic(self):
        """
        Return the characteristic.

        EXAMPLES::

            sage: UniversalCyclotomicField().characteristic()
            0
            sage: parent(_)
            Integer Ring
        """
    def gen(self, n, k: int = 1):
        """
        Return the standard primitive ``n``-th root of unity.

        If ``k`` is not ``None``, return the ``k``-th power of it.

        EXAMPLES::

            sage: UCF = UniversalCyclotomicField()
            sage: UCF.gen(15)
            E(15)
            sage: UCF.gen(7,3)
            E(7)^3
            sage: UCF.gen(4,2)
            -1

        There is an alias ``zeta`` also available::

            sage: UCF.zeta(6)
            -E(3)^2
        """
    zeta = gen
    def degree(self):
        """
        Return the *degree* of ``self`` as a field extension over the Rationals.

        EXAMPLES::

            sage: UCF = UniversalCyclotomicField()
            sage: UCF.degree()
            +Infinity
        """
    def algebraic_closure(self):
        """
        The algebraic closure.

        EXAMPLES::

            sage: UniversalCyclotomicField().algebraic_closure()
            Algebraic Field
        """

def E(n, k: int = 1):
    """
    Return the ``n``-th root of unity as an element of the universal cyclotomic
    field.

    EXAMPLES::

        sage: E(3)
        E(3)
        sage: E(3) + E(5)
        -E(15)^2 - 2*E(15)^8 - E(15)^11 - E(15)^13 - E(15)^14
    """
