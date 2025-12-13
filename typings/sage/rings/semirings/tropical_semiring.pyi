import sage.categories.map
import sage.structure.element
import sage.structure.parent
import sage.structure.unique_representation
from sage.categories.category import ZZ as ZZ
from sage.categories.semirings import Semirings as Semirings
from sage.misc.cachefunc import cached_method as cached_method
from sage.structure.element import have_same_parent as have_same_parent, parent as parent
from sage.structure.parent import Parent as Parent
from sage.structure.richcmp import revop as revop, rich_to_bool as rich_to_bool, rich_to_bool_sgn as rich_to_bool_sgn, richcmp as richcmp, richcmp_not_equal as richcmp_not_equal
from sage.structure.unique_representation import UniqueRepresentation as UniqueRepresentation
from typing import Any, ClassVar, overload

class TropicalSemiring(sage.structure.parent.Parent, sage.structure.unique_representation.UniqueRepresentation):
    '''File: /build/sagemath/src/sage/src/sage/rings/semirings/tropical_semiring.pyx (starting at line 422)

        The tropical semiring.

        Given an ordered additive semigroup `R`, we define the tropical
        semiring `T = R \\cup \\{+\\infty\\}` by defining tropical addition
        and multiplication as follows:

        .. MATH::

            a \\oplus b = \\min(a, b), \\quad \\quad a \\odot b = a + b.

        In particular, note that there are no (tropical) additive inverses
        (except for `\\infty`), and every element in `R` has a (tropical)
        multiplicative inverse.

        There is an alternative definition where we define `T = R \\cup \\{-\\infty\\}`
        and alter tropical addition to be defined by

        .. MATH::

            a \\oplus b = \\max(a, b).

        To use the `\\max` definition, set the argument ``use_min = False``.

        .. WARNING::

            :meth:`zero` and :meth:`one` refer to the tropical additive
            and multiplicative identities respectively. These are **not** the
            same as calling ``T(0)`` and ``T(1)`` respectively as these are **not**
            the tropical additive and multiplicative identities respectively.

            Specifically do not use ``sum(...)`` as this converts `0` to `0` as
            a tropical element, which is not the same as :meth:`zero`. Instead
            use the ``sum`` method of the tropical semiring::

                sage: T = TropicalSemiring(QQ)

                sage: sum([T(1), T(2)]) # This is wrong
                0
                sage: T.sum([T(1), T(2)]) # This is correct
                1

            Be careful about using code that has not been checked for tropical
            safety.

        INPUT:

        - ``base`` -- the base ordered additive semigroup `R`
        - ``use_min`` -- boolean (default: ``True``); if ``True``, then the semiring uses
          `a \\oplus b = \\min(a, b)`. Otherwise uses `a \\oplus b = \\max(a, b)`.

        EXAMPLES::

            sage: T = TropicalSemiring(QQ)
            sage: elt = T(2); elt
            2

        Recall that tropical addition is the minimum of two elements::

            sage: T(3) + T(5)
            3

        Tropical multiplication is the addition of two elements::

            sage: T(2) * T(3)
            5
            sage: T(0) * T(-2)
            -2

        We can also do tropical division and arbitrary tropical exponentiation::

            sage: T(2) / T(1)
            1
            sage: T(2)^(-3/7)
            -6/7

        Note that "zero" and "one" are the additive and multiplicative
        identities of the tropical semiring. In general, they are **not**
        the elements `0` and `1` of `R`, respectively, even if such elements
        exist (e.g., for `R = \\ZZ`), but instead the (tropical) additive and
        multiplicative identities `+\\infty` and `0` respectively::

            sage: T.zero() + T(3) == T(3)
            True
            sage: T.one() * T(3) == T(3)
            True
            sage: T.zero() == T(0)
            False
            sage: T.one() == T(1)
            False
    '''

    class Element(sage.structure.element.Element):
        """TropicalSemiringElement(parent, ModuleElement val=None)

        File: /build/sagemath/src/sage/src/sage/rings/semirings/tropical_semiring.pyx (starting at line 33)

        An element in the tropical semiring over an ordered additive semigroup
        `R`. Either in `R` or `\\infty`. The operators `+, \\cdot` are defined as
        the tropical operators `\\oplus, \\odot` respectively."""
        __pyx_vtable__: ClassVar[PyCapsule] = ...
        def __init__(self, *args, **kwargs) -> None:
            """File: /build/sagemath/src/sage/src/sage/rings/semirings/tropical_semiring.pyx (starting at line 51)

                    Initialize ``self``.

                    EXAMPLES::

                        sage: T = TropicalSemiring(QQ)
                        sage: elt = T(2)
                        sage: TestSuite(elt).run()
        """
        @overload
        def lift(self) -> ModuleElement:
            """TropicalSemiringElement.lift(self) -> ModuleElement

            File: /build/sagemath/src/sage/src/sage/rings/semirings/tropical_semiring.pyx (starting at line 401)

            Return the value of ``self`` lifted to the base.

            EXAMPLES::

                sage: T = TropicalSemiring(QQ)
                sage: elt = T(2)
                sage: elt.lift()
                2
                sage: elt.lift().parent() is QQ
                True
                sage: T.additive_identity().lift().parent()
                The Infinity Ring"""
        @overload
        def lift(self) -> Any:
            """TropicalSemiringElement.lift(self) -> ModuleElement

            File: /build/sagemath/src/sage/src/sage/rings/semirings/tropical_semiring.pyx (starting at line 401)

            Return the value of ``self`` lifted to the base.

            EXAMPLES::

                sage: T = TropicalSemiring(QQ)
                sage: elt = T(2)
                sage: elt.lift()
                2
                sage: elt.lift().parent() is QQ
                True
                sage: T.additive_identity().lift().parent()
                The Infinity Ring"""
        @overload
        def lift(self) -> Any:
            """TropicalSemiringElement.lift(self) -> ModuleElement

            File: /build/sagemath/src/sage/src/sage/rings/semirings/tropical_semiring.pyx (starting at line 401)

            Return the value of ``self`` lifted to the base.

            EXAMPLES::

                sage: T = TropicalSemiring(QQ)
                sage: elt = T(2)
                sage: elt.lift()
                2
                sage: elt.lift().parent() is QQ
                True
                sage: T.additive_identity().lift().parent()
                The Infinity Ring"""
        @overload
        def lift(self) -> Any:
            """TropicalSemiringElement.lift(self) -> ModuleElement

            File: /build/sagemath/src/sage/src/sage/rings/semirings/tropical_semiring.pyx (starting at line 401)

            Return the value of ``self`` lifted to the base.

            EXAMPLES::

                sage: T = TropicalSemiring(QQ)
                sage: elt = T(2)
                sage: elt.lift()
                2
                sage: elt.lift().parent() is QQ
                True
                sage: T.additive_identity().lift().parent()
                The Infinity Ring"""
        @overload
        def multiplicative_order(self) -> Any:
            """TropicalSemiringElement.multiplicative_order(self)

            File: /build/sagemath/src/sage/src/sage/rings/semirings/tropical_semiring.pyx (starting at line 384)

            Return the multiplicative order of ``self``.

            EXAMPLES::

                sage: T = TropicalSemiring(QQ)
                sage: T.multiplicative_identity().multiplicative_order()
                1
                sage: T.additive_identity().multiplicative_order()
                +Infinity"""
        @overload
        def multiplicative_order(self) -> Any:
            """TropicalSemiringElement.multiplicative_order(self)

            File: /build/sagemath/src/sage/src/sage/rings/semirings/tropical_semiring.pyx (starting at line 384)

            Return the multiplicative order of ``self``.

            EXAMPLES::

                sage: T = TropicalSemiring(QQ)
                sage: T.multiplicative_identity().multiplicative_order()
                1
                sage: T.additive_identity().multiplicative_order()
                +Infinity"""
        @overload
        def multiplicative_order(self) -> Any:
            """TropicalSemiringElement.multiplicative_order(self)

            File: /build/sagemath/src/sage/src/sage/rings/semirings/tropical_semiring.pyx (starting at line 384)

            Return the multiplicative order of ``self``.

            EXAMPLES::

                sage: T = TropicalSemiring(QQ)
                sage: T.multiplicative_identity().multiplicative_order()
                1
                sage: T.additive_identity().multiplicative_order()
                +Infinity"""
        def __hash__(self) -> Any:
            """TropicalSemiringElement.__hash__(self)

            File: /build/sagemath/src/sage/src/sage/rings/semirings/tropical_semiring.pyx (starting at line 120)

            Return the hash of ``self``.

            EXAMPLES::

                sage: T = TropicalSemiring(QQ)
                sage: hash(T(2)) == hash(T(2))
                True
                sage: hash(T.infinity()) == hash(T.infinity())
                True"""
        def __invert__(self) -> Any:
            """TropicalSemiringElement.__invert__(self)

            File: /build/sagemath/src/sage/src/sage/rings/semirings/tropical_semiring.pyx (starting at line 328)

            Return the multiplicative inverse of ``self``.

            EXAMPLES::

                sage: T = TropicalSemiring(QQ)
                sage: ~T(2)
                -2"""
        def __neg__(self) -> Any:
            """TropicalSemiringElement.__neg__(self)

            File: /build/sagemath/src/sage/src/sage/rings/semirings/tropical_semiring.pyx (starting at line 259)

            Return the additive inverse, which only exists for `\\infty`.

            EXAMPLES::

                sage: T = TropicalSemiring(QQ)
                sage: -T.infinity()
                +infinity
                sage: -T(2)
                Traceback (most recent call last):
                ...
                ArithmeticError: cannot negate any non-infinite element"""
        def __pow__(self, base, exp, dummy) -> Any:
            """TropicalSemiringElement.__pow__(base, exp, dummy)

            File: /build/sagemath/src/sage/src/sage/rings/semirings/tropical_semiring.pyx (starting at line 347)

            Return ``self`` to ``exp``.

            EXAMPLES::

                sage: T = TropicalSemiring(QQ)
                sage: elt = T(2)
                sage: elt**3
                6
                sage: elt**-2
                -4
                sage: elt**(3/7)
                6/7
                sage: elt**0
                0

                sage: elt = T.infinity()
                sage: elt**0
                0
                sage: elt**(1/2)
                +infinity
                sage: elt*33
                +infinity"""
        @overload
        def __reduce__(self) -> Any:
            """TropicalSemiringElement.__reduce__(self)

            File: /build/sagemath/src/sage/src/sage/rings/semirings/tropical_semiring.pyx (starting at line 64)

            Used in pickling tropical semiring elements.

            EXAMPLES::

                sage: T = TropicalSemiring(QQ)
                sage: elt = T(2)
                sage: elt.__reduce__()
                (<class 'sage.rings.semirings.tropical_semiring.TropicalSemiringElement'>,
                 (Tropical semiring over Rational Field, 2))"""
        @overload
        def __reduce__(self) -> Any:
            """TropicalSemiringElement.__reduce__(self)

            File: /build/sagemath/src/sage/src/sage/rings/semirings/tropical_semiring.pyx (starting at line 64)

            Used in pickling tropical semiring elements.

            EXAMPLES::

                sage: T = TropicalSemiring(QQ)
                sage: elt = T(2)
                sage: elt.__reduce__()
                (<class 'sage.rings.semirings.tropical_semiring.TropicalSemiringElement'>,
                 (Tropical semiring over Rational Field, 2))"""
        def __rpow__(self, other):
            """Return pow(value, self, mod)."""
    def __init__(self, base, use_min=...) -> Any:
        """TropicalSemiring.__init__(self, base, use_min=True)

        File: /build/sagemath/src/sage/src/sage/rings/semirings/tropical_semiring.pyx (starting at line 514)

        Initialize ``self``.

        TESTS::

            sage: T = TropicalSemiring(QQ); T
            Tropical semiring over Rational Field
            sage: TestSuite(T).run()"""
    def additive_identity(self, *args, **kwargs):
        """TropicalSemiring.zero(self)

        File: /build/sagemath/src/sage/src/sage/rings/semirings/tropical_semiring.pyx (starting at line 612)

        Return the (tropical) additive identity element `+\\infty`.

        EXAMPLES::

            sage: T = TropicalSemiring(QQ)
            sage: T.zero()
            +infinity"""
    @overload
    def gens(self) -> tuple:
        """TropicalSemiring.gens(self) -> tuple

        File: /build/sagemath/src/sage/src/sage/rings/semirings/tropical_semiring.pyx (starting at line 643)

        Return the generators of ``self``.

        EXAMPLES::

            sage: T = TropicalSemiring(QQ)
            sage: T.gens()
            (1, +infinity)"""
    @overload
    def gens(self) -> Any:
        """TropicalSemiring.gens(self) -> tuple

        File: /build/sagemath/src/sage/src/sage/rings/semirings/tropical_semiring.pyx (starting at line 643)

        Return the generators of ``self``.

        EXAMPLES::

            sage: T = TropicalSemiring(QQ)
            sage: T.gens()
            (1, +infinity)"""
    def infinity(self, *args, **kwargs):
        """TropicalSemiring.zero(self)

        File: /build/sagemath/src/sage/src/sage/rings/semirings/tropical_semiring.pyx (starting at line 612)

        Return the (tropical) additive identity element `+\\infty`.

        EXAMPLES::

            sage: T = TropicalSemiring(QQ)
            sage: T.zero()
            +infinity"""
    def multiplicative_identity(self, *args, **kwargs):
        """TropicalSemiring.one(self)

        File: /build/sagemath/src/sage/src/sage/rings/semirings/tropical_semiring.pyx (starting at line 628)

        Return the (tropical) multiplicative identity element `0`.

        EXAMPLES::

            sage: T = TropicalSemiring(QQ)
            sage: T.one()
            0"""
    @overload
    def one(self) -> Any:
        """TropicalSemiring.one(self)

        File: /build/sagemath/src/sage/src/sage/rings/semirings/tropical_semiring.pyx (starting at line 628)

        Return the (tropical) multiplicative identity element `0`.

        EXAMPLES::

            sage: T = TropicalSemiring(QQ)
            sage: T.one()
            0"""
    @overload
    def one(self) -> Any:
        """TropicalSemiring.one(self)

        File: /build/sagemath/src/sage/src/sage/rings/semirings/tropical_semiring.pyx (starting at line 628)

        Return the (tropical) multiplicative identity element `0`.

        EXAMPLES::

            sage: T = TropicalSemiring(QQ)
            sage: T.one()
            0"""
    def zero(self) -> Any:
        """TropicalSemiring.zero(self)

        File: /build/sagemath/src/sage/src/sage/rings/semirings/tropical_semiring.pyx (starting at line 612)

        Return the (tropical) additive identity element `+\\infty`.

        EXAMPLES::

            sage: T = TropicalSemiring(QQ)
            sage: T.zero()
            +infinity"""

class TropicalSemiringElement(sage.structure.element.Element):
    """TropicalSemiringElement(parent, ModuleElement val=None)

    File: /build/sagemath/src/sage/src/sage/rings/semirings/tropical_semiring.pyx (starting at line 33)

    An element in the tropical semiring over an ordered additive semigroup
    `R`. Either in `R` or `\\infty`. The operators `+, \\cdot` are defined as
    the tropical operators `\\oplus, \\odot` respectively."""
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    def __init__(self, parent, ModuleElementval=...) -> Any:
        """File: /build/sagemath/src/sage/src/sage/rings/semirings/tropical_semiring.pyx (starting at line 51)

                Initialize ``self``.

                EXAMPLES::

                    sage: T = TropicalSemiring(QQ)
                    sage: elt = T(2)
                    sage: TestSuite(elt).run()
        """
    @overload
    def lift(self) -> ModuleElement:
        """TropicalSemiringElement.lift(self) -> ModuleElement

        File: /build/sagemath/src/sage/src/sage/rings/semirings/tropical_semiring.pyx (starting at line 401)

        Return the value of ``self`` lifted to the base.

        EXAMPLES::

            sage: T = TropicalSemiring(QQ)
            sage: elt = T(2)
            sage: elt.lift()
            2
            sage: elt.lift().parent() is QQ
            True
            sage: T.additive_identity().lift().parent()
            The Infinity Ring"""
    @overload
    def lift(self) -> Any:
        """TropicalSemiringElement.lift(self) -> ModuleElement

        File: /build/sagemath/src/sage/src/sage/rings/semirings/tropical_semiring.pyx (starting at line 401)

        Return the value of ``self`` lifted to the base.

        EXAMPLES::

            sage: T = TropicalSemiring(QQ)
            sage: elt = T(2)
            sage: elt.lift()
            2
            sage: elt.lift().parent() is QQ
            True
            sage: T.additive_identity().lift().parent()
            The Infinity Ring"""
    @overload
    def lift(self) -> Any:
        """TropicalSemiringElement.lift(self) -> ModuleElement

        File: /build/sagemath/src/sage/src/sage/rings/semirings/tropical_semiring.pyx (starting at line 401)

        Return the value of ``self`` lifted to the base.

        EXAMPLES::

            sage: T = TropicalSemiring(QQ)
            sage: elt = T(2)
            sage: elt.lift()
            2
            sage: elt.lift().parent() is QQ
            True
            sage: T.additive_identity().lift().parent()
            The Infinity Ring"""
    @overload
    def lift(self) -> Any:
        """TropicalSemiringElement.lift(self) -> ModuleElement

        File: /build/sagemath/src/sage/src/sage/rings/semirings/tropical_semiring.pyx (starting at line 401)

        Return the value of ``self`` lifted to the base.

        EXAMPLES::

            sage: T = TropicalSemiring(QQ)
            sage: elt = T(2)
            sage: elt.lift()
            2
            sage: elt.lift().parent() is QQ
            True
            sage: T.additive_identity().lift().parent()
            The Infinity Ring"""
    @overload
    def multiplicative_order(self) -> Any:
        """TropicalSemiringElement.multiplicative_order(self)

        File: /build/sagemath/src/sage/src/sage/rings/semirings/tropical_semiring.pyx (starting at line 384)

        Return the multiplicative order of ``self``.

        EXAMPLES::

            sage: T = TropicalSemiring(QQ)
            sage: T.multiplicative_identity().multiplicative_order()
            1
            sage: T.additive_identity().multiplicative_order()
            +Infinity"""
    @overload
    def multiplicative_order(self) -> Any:
        """TropicalSemiringElement.multiplicative_order(self)

        File: /build/sagemath/src/sage/src/sage/rings/semirings/tropical_semiring.pyx (starting at line 384)

        Return the multiplicative order of ``self``.

        EXAMPLES::

            sage: T = TropicalSemiring(QQ)
            sage: T.multiplicative_identity().multiplicative_order()
            1
            sage: T.additive_identity().multiplicative_order()
            +Infinity"""
    @overload
    def multiplicative_order(self) -> Any:
        """TropicalSemiringElement.multiplicative_order(self)

        File: /build/sagemath/src/sage/src/sage/rings/semirings/tropical_semiring.pyx (starting at line 384)

        Return the multiplicative order of ``self``.

        EXAMPLES::

            sage: T = TropicalSemiring(QQ)
            sage: T.multiplicative_identity().multiplicative_order()
            1
            sage: T.additive_identity().multiplicative_order()
            +Infinity"""
    def __hash__(self) -> Any:
        """TropicalSemiringElement.__hash__(self)

        File: /build/sagemath/src/sage/src/sage/rings/semirings/tropical_semiring.pyx (starting at line 120)

        Return the hash of ``self``.

        EXAMPLES::

            sage: T = TropicalSemiring(QQ)
            sage: hash(T(2)) == hash(T(2))
            True
            sage: hash(T.infinity()) == hash(T.infinity())
            True"""
    def __invert__(self) -> Any:
        """TropicalSemiringElement.__invert__(self)

        File: /build/sagemath/src/sage/src/sage/rings/semirings/tropical_semiring.pyx (starting at line 328)

        Return the multiplicative inverse of ``self``.

        EXAMPLES::

            sage: T = TropicalSemiring(QQ)
            sage: ~T(2)
            -2"""
    def __neg__(self) -> Any:
        """TropicalSemiringElement.__neg__(self)

        File: /build/sagemath/src/sage/src/sage/rings/semirings/tropical_semiring.pyx (starting at line 259)

        Return the additive inverse, which only exists for `\\infty`.

        EXAMPLES::

            sage: T = TropicalSemiring(QQ)
            sage: -T.infinity()
            +infinity
            sage: -T(2)
            Traceback (most recent call last):
            ...
            ArithmeticError: cannot negate any non-infinite element"""
    def __pow__(self, base, exp, dummy) -> Any:
        """TropicalSemiringElement.__pow__(base, exp, dummy)

        File: /build/sagemath/src/sage/src/sage/rings/semirings/tropical_semiring.pyx (starting at line 347)

        Return ``self`` to ``exp``.

        EXAMPLES::

            sage: T = TropicalSemiring(QQ)
            sage: elt = T(2)
            sage: elt**3
            6
            sage: elt**-2
            -4
            sage: elt**(3/7)
            6/7
            sage: elt**0
            0

            sage: elt = T.infinity()
            sage: elt**0
            0
            sage: elt**(1/2)
            +infinity
            sage: elt*33
            +infinity"""
    @overload
    def __reduce__(self) -> Any:
        """TropicalSemiringElement.__reduce__(self)

        File: /build/sagemath/src/sage/src/sage/rings/semirings/tropical_semiring.pyx (starting at line 64)

        Used in pickling tropical semiring elements.

        EXAMPLES::

            sage: T = TropicalSemiring(QQ)
            sage: elt = T(2)
            sage: elt.__reduce__()
            (<class 'sage.rings.semirings.tropical_semiring.TropicalSemiringElement'>,
             (Tropical semiring over Rational Field, 2))"""
    @overload
    def __reduce__(self) -> Any:
        """TropicalSemiringElement.__reduce__(self)

        File: /build/sagemath/src/sage/src/sage/rings/semirings/tropical_semiring.pyx (starting at line 64)

        Used in pickling tropical semiring elements.

        EXAMPLES::

            sage: T = TropicalSemiring(QQ)
            sage: elt = T(2)
            sage: elt.__reduce__()
            (<class 'sage.rings.semirings.tropical_semiring.TropicalSemiringElement'>,
             (Tropical semiring over Rational Field, 2))"""
    def __rpow__(self, other):
        """Return pow(value, self, mod)."""

class TropicalToTropical(sage.categories.map.Map):
    """File: /build/sagemath/src/sage/src/sage/rings/semirings/tropical_semiring.pyx (starting at line 656)

        Map from the tropical semiring to itself (possibly with different bases).
        Used in coercion.
    """
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    @classmethod
    def __init__(cls, *args, **kwargs) -> None:
        """Create and return a new object.  See help(type) for accurate signature."""
