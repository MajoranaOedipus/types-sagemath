from _typeshed import Incomplete
from sage.structure.element import MultiplicativeGroupElement as MultiplicativeGroupElement
from sage.structure.factory import UniqueFactory as UniqueFactory
from sage.structure.parent import Parent as Parent
from sage.structure.richcmp import richcmp_by_eq_and_lt as richcmp_by_eq_and_lt
from sage.structure.unique_representation import UniqueRepresentation as UniqueRepresentation

class AbstractArgument(MultiplicativeGroupElement):
    """
    An element of :class:`AbstractArgumentGroup`. This abstract class
    encapsulates an element of the parent's base, i.e. it can be seen
    as a wrapper class.

    INPUT:

    - ``parent`` -- a SageMath parent

    - ``element`` -- an element of parent's base

    - ``normalize`` -- boolean (default: ``True``)
    """
    def __init__(self, parent, element, normalize: bool = True) -> None:
        """
        See :class:`AbstractArgument` for more information.

        TESTS::

            sage: from sage.groups.misc_gps.argument_groups import UnitCircleGroup, RootsOfUnityGroup
            sage: C = UnitCircleGroup(RR)
            sage: C(exponent=1/2)  # indirect doctest
            e^(2*pi*0.500000000000000)
            sage: C(exponent=3/2)
            e^(2*pi*0.500000000000000)

            sage: U = RootsOfUnityGroup()
            sage: U(exponent=0)
            1
            sage: U(exponent=1)
            1
            sage: U(exponent=2/3) == U(exponent=5/3)
            True
        """
    def __hash__(self):
        """
        Return a hash value of this argument.

        TESTS::

            sage: from sage.groups.misc_gps.argument_groups import UnitCircleGroup
            sage: C = UnitCircleGroup(RR)
            sage: hash(C(exponent=1/3))  # indirect doctest, random
            42
        """
    def __abs__(self):
        """
        Return the absolute value of this argument which equals `1`.

        TESTS::

            sage: from sage.groups.misc_gps.argument_groups import RootsOfUnityGroup
            sage: U = RootsOfUnityGroup()
            sage: abs(U(exponent=1/4))  # indirect doctest
            1
            sage: _.parent()
            Integer Ring
        """

class AbstractArgumentGroup(UniqueRepresentation, Parent):
    """
    A group whose elements represent (complex) arguments.

    INPUT:

    - ``base`` -- a SageMath parent

    - ``category`` -- a category
    """
    Element = AbstractArgument
    @staticmethod
    def __classcall__(cls, base, category=None):
        """
        See :class:`AbstractArgumentGroup` for more information.

        TESTS:

            sage: from sage.groups.misc_gps.argument_groups import UnitCircleGroup
            sage: UnitCircleGroup(RR).category()  # indirect doctest
            Category of commutative groups
        """
    def __init__(self, base, category) -> None:
        """
        See :class:`AbstractArgumentGroup` for more information.

        TESTS:

            sage: from sage.groups.misc_gps.argument_groups import UnitCircleGroup
            sage: UnitCircleGroup(RR).base()  # indirect doctest
            Real Field with 53 bits of precision
        """
    def __hash__(self):
        """
        Return a hash value of this argument group.

        TESTS::

            sage: from sage.groups.misc_gps.argument_groups import UnitCircleGroup
            sage: hash(UnitCircleGroup(RR))  # indirect doctest, random
            42
        """

class UnitCirclePoint(AbstractArgument):
    """
    An element of :class:`UnitCircleGroup`
    which is `e^{2\\pi\\cdot\\mathit{exponent}}`.

    INPUT:

    - ``parent`` -- a SageMath parent

    - ``exponent`` -- a number (of a subset of the reals)

    - ``normalize`` -- boolean (default: ``True``)
    """
    @property
    def exponent(self):
        """
        The exponent of this point on the unit circle.

        EXAMPLES::

            sage: from sage.groups.misc_gps.argument_groups import UnitCircleGroup
            sage: C = UnitCircleGroup(RR)
            sage: C(exponent=4/3).exponent
            0.333333333333333
        """
    def __pow__(self, exponent):
        """
        Return the power of this point on the unit circle
        to the given ``exponent``.

        TESTS::

            sage: from sage.groups.misc_gps.argument_groups import UnitCircleGroup, RootsOfUnityGroup

            sage: C = UnitCircleGroup(RR)
            sage: C(exponent=0.1)^2
            e^(2*pi*0.200000000000000)
            sage: _.parent()
            Unit Circle Group with Exponents in
            Real Field with 53 bits of precision modulo ZZ
            sage: C(exponent=0.1)^QQ(2/1)
            e^(2*pi*0.200000000000000)
            sage: _.parent()
            Unit Circle Group with Exponents in
            Real Field with 53 bits of precision modulo ZZ

            sage: U = RootsOfUnityGroup()
            sage: a = U(exponent=1/7); a
            zeta7
            sage: a^(7/3)
            zeta3
            sage: _.parent()
            Group of Roots of Unity

            sage: U(exponent=1/3)^(0.25)
            e^(2*pi*0.0833333333333333)
            sage: _.parent()
            Unit Circle Group with Exponents in
            Real Field with 53 bits of precision modulo ZZ

            sage: U(exponent=1/3)^x
            (1/2*I*sqrt(3) - 1/2)^x
            sage: U(exponent=1/2)^x
            (-1)^x
            sage: U(exponent=1/4)^x
            I^x
            sage: U(exponent=1/4)^SR(8)
            1
        """
    def __invert__(self):
        """
        Return the inverse of this point on the unit circle.

        TESTS::

            sage: from sage.groups.misc_gps.argument_groups import UnitCircleGroup
            sage: C = UnitCircleGroup(RR)
            sage: ~C(exponent=0.4)
            e^(2*pi*0.600000000000000)
            sage: C(1) / C(exponent=0.4)
            e^(2*pi*0.600000000000000)
            sage: C(exponent=0) / C(exponent=0.42)
            e^(2*pi*0.580000000000000)
        """
    def is_one(self):
        """
        Return whether this point on the unit circle is `1`.

        EXAMPLES::

            sage: from sage.groups.misc_gps.argument_groups import UnitCircleGroup
            sage: C = UnitCircleGroup(QQ)
            sage: C(exponent=0).is_one()
            True
            sage: C(exponent=1/2).is_one()
            False
            sage: C(exponent=2/3).is_one()
            False
            sage: C(exponent=42).is_one()
            True
        """
    def is_minus_one(self):
        """
        Return whether this point on the unit circle is `-1`.

        EXAMPLES::

            sage: from sage.groups.misc_gps.argument_groups import UnitCircleGroup
            sage: C = UnitCircleGroup(QQ)
            sage: C(exponent=0).is_minus_one()
            False
            sage: C(exponent=1/2).is_minus_one()
            True
            sage: C(exponent=2/3).is_minus_one()
            False
        """

class UnitCircleGroup(AbstractArgumentGroup):
    """
    A group of points on the unit circle. These points are
    represented by `e^{2\\pi\\cdot\\mathit{exponent}}`.

    INPUT:

    - ``base`` -- a SageMath parent representing a subset of the reals

    - ``category`` -- a category

    EXAMPLES::

        sage: from sage.groups.misc_gps.argument_groups import UnitCircleGroup

        sage: R = UnitCircleGroup(RR); R
        Unit Circle Group with Exponents in Real Field with 53 bits of precision modulo ZZ
        sage: R(exponent=2.42)
        e^(2*pi*0.420000000000000)

        sage: Q = UnitCircleGroup(QQ); Q
        Unit Circle Group with Exponents in Rational Field modulo ZZ
        sage: Q(exponent=6/5)
        e^(2*pi*1/5)
    """
    Element = UnitCirclePoint

class RootOfUnity(UnitCirclePoint):
    """
    A root of unity (i.e. an element of :class:`RootsOfUnityGroup`)
    which is `e^{2\\pi\\cdot\\mathit{exponent}}` for a rational ``exponent``.
    """
    def exponent_numerator(self):
        """
        Return the numerator of the rational quotient in `[0,1)`
        representing the exponent of this root of unity.

        EXAMPLES::

            sage: from sage.groups.misc_gps.argument_groups import RootsOfUnityGroup
            sage: U = RootsOfUnityGroup()
            sage: a = U(exponent=2/3); a
            zeta3^2
            sage: a.exponent_numerator()
            2
        """
    def exponent_denominator(self):
        """
        Return the denominator of the rational quotient in `[0,1)`
        representing the exponent of this root of unity.

        EXAMPLES::

            sage: from sage.groups.misc_gps.argument_groups import RootsOfUnityGroup
            sage: U = RootsOfUnityGroup()
            sage: a = U(exponent=2/3); a
            zeta3^2
            sage: a.exponent_denominator()
            3
        """

class RootsOfUnityGroup(UnitCircleGroup):
    """
    The group of all roots of unity.

    INPUT:

    - ``category`` -- a category

    This is a specialized :class:`UnitCircleGroup` with base `\\QQ`.

    EXAMPLES::

        sage: from sage.groups.misc_gps.argument_groups import RootsOfUnityGroup
        sage: U = RootsOfUnityGroup(); U
        Group of Roots of Unity
        sage: U(exponent=1/4)
        I
    """
    Element = RootOfUnity
    @staticmethod
    def __classcall__(cls, category=None):
        """
        See :class:`RootsOfUnityGroup` for more information.

        TESTS:

            sage: from sage.groups.misc_gps.argument_groups import RootsOfUnityGroup
            sage: RootsOfUnityGroup().category()  # indirect doctest
            Category of commutative groups
        """
    def __init__(self, category) -> None:
        """
        See :class:`RootsOfUnityGroup` for more information.

        TESTS:

            sage: from sage.groups.misc_gps.argument_groups import RootsOfUnityGroup
            sage: RootsOfUnityGroup().base()  # indirect doctest
            Rational Field
        """

class ArgumentByElement(AbstractArgument):
    """
    An element of :class:`ArgumentByElementGroup`.

    INPUT:

    - ``parent`` -- a SageMath parent

    - ``element`` -- a nonzero element of the parent's base

    - ``normalize`` -- boolean (default: ``True``)
    """
    def __init__(self, parent, element, normalize: bool = True) -> None:
        """
        See :class:`ArgumentByElement` for more information.

        TESTS::

            sage: from sage.groups.misc_gps.argument_groups import ArgumentByElementGroup
            sage: C = ArgumentByElementGroup(CC)
            sage: C(1+2*I)  # indirect doctest                                          # needs sage.symbolic
            e^(I*arg(1.00000000000000 + 2.00000000000000*I))
        """
    def __pow__(self, exponent):
        """
        Return the power of this argument by element
        to the given ``exponent``.

        TESTS::

            sage: from sage.groups.misc_gps.argument_groups import ArgumentByElementGroup
            sage: C = ArgumentByElementGroup(CC)
            sage: C(I)^5  # indirect doctest                                            # needs sage.symbolic
            e^(I*arg(1.00000000000000*I))
            sage: _.parent()
            Unit Circle Group with Argument of Elements in
            Complex Field with 53 bits of precision
            sage: C(1+I)^3  # indirect doctest                                          # needs sage.symbolic
            e^(I*arg(-2.00000000000000 + 2.00000000000000*I))
            sage: _.parent()
            Unit Circle Group with Argument of Elements in
            Complex Field with 53 bits of precision

            sage: C = ArgumentByElementGroup(RR)
            sage: C(0.42)^CC(2.4)
            e^(I*arg(0.124680431591996))
            sage: _.parent()
            Unit Circle Group with Argument of Elements in
            Complex Field with 53 bits of precision

            sage: C = ArgumentByElementGroup(QQ)
            sage: a = C(-20)^x; a
            (-1)^x
            sage: a.parent()
            Symbolic Ring
        """
    def __invert__(self):
        """
        Return the inverse of this argument by element.

        TESTS::

            sage: from sage.groups.misc_gps.argument_groups import ArgumentByElementGroup
            sage: C = ArgumentByElementGroup(CC)
            sage: ~C(I)  # indirect doctest                                             # needs sage.symbolic
            e^(I*arg(-1.00000000000000*I))
        """

class ArgumentByElementGroup(AbstractArgumentGroup):
    """
    A group of (complex) arguments. The arguments are represented
    by a the formal argument of an element, i.e.,
    by `\\mathrm{arg}(\\mathit{element})`.

    INPUT:

    - ``base`` -- a SageMath parent representing a subset of the complex plane

    - ``category`` -- a category

    EXAMPLES::

        sage: from sage.groups.misc_gps.argument_groups import ArgumentByElementGroup
        sage: C = ArgumentByElementGroup(CC); C
        Unit Circle Group with Argument of Elements in
        Complex Field with 53 bits of precision
        sage: C(1 + 2*I)                                                                # needs sage.symbolic
        e^(I*arg(1.00000000000000 + 2.00000000000000*I))
    """
    Element = ArgumentByElement

class Sign(AbstractArgument):
    """
    An element of :class:`SignGroup`.

    INPUT:

    - ``parent`` -- a SageMath parent

    - ``element`` -- a nonzero element of the parent's base

    - ``normalize`` -- boolean (default: ``True``)
    """
    def __init__(self, parent, element, normalize: bool = True) -> None:
        """
        See :class:`Sign` for more information.

        TESTS::

            sage: from sage.groups.misc_gps.argument_groups import SignGroup
            sage: S = SignGroup()
            sage: S.an_element()  # indirect doctest
            -1
        """
    def __pow__(self, exponent):
        """
        Return the power of this sign to the given ``exponent``.

        TESTS::

            sage: from sage.groups.misc_gps.argument_groups import SignGroup
            sage: S = SignGroup()
            sage: S(-1)^4  # indirect doctest
            1
            sage: S(-1)^3  # indirect doctest
            -1

        Check that the results may live in other parents too::

            sage: x = SR.var('x')
            sage: elem = S(-1)^x; elem  # indirect doctest
            (-1)^x
            sage: elem.parent()
            Symbolic Ring

        """
    def __invert__(self):
        """
        Return the inverse of this sign.

        TESTS::

            sage: from sage.groups.misc_gps.argument_groups import SignGroup
            sage: S = SignGroup()
            sage: ~S(-1)  # indirect doctest
            -1
            sage: _.parent()
            Sign Group
        """
    def is_one(self):
        """
        Return whether this sign is `1`.

        EXAMPLES::

            sage: from sage.groups.misc_gps.argument_groups import SignGroup
            sage: S = SignGroup()
            sage: S(-1).is_one()
            False
            sage: S(1).is_one()
            True
        """
    def is_minus_one(self):
        """
        Return whether this sign is `-1`.

        EXAMPLES::

            sage: from sage.groups.misc_gps.argument_groups import SignGroup
            sage: S = SignGroup()
            sage: S(1).is_minus_one()
            False
            sage: S(-1).is_minus_one()
            True
        """

class SignGroup(AbstractArgumentGroup):
    """
    A group of the signs `-1` and `1`.

    INPUT:

    - ``category`` -- a category

    EXAMPLES::

        sage: from sage.groups.misc_gps.argument_groups import SignGroup
        sage: S = SignGroup(); S
        Sign Group
        sage: S(-1)
        -1
    """
    Element = Sign
    @staticmethod
    def __classcall__(cls, category=None):
        """
        See :class:`SignGroup` for more information.

        TESTS:

            sage: from sage.groups.misc_gps.argument_groups import SignGroup
            sage: S = SignGroup()
            sage: S.category()  # indirect doctest
            Category of finite commutative groups
        """
    def __init__(self, category) -> None:
        """
        See :class:`SignGroup` for more information.

        TESTS:

            sage: from sage.groups.misc_gps.argument_groups import SignGroup
            sage: S = SignGroup()
            sage: S.base()  # indirect doctest
            <class 'int'>
        """

class ArgumentGroupFactory(UniqueFactory):
    """
    A factory for creating argument groups.

    INPUT:

    - ``data`` -- an object

      The factory will analyze ``data`` and interpret it as
      ``specification`` or ``domain``.

    - ``specification`` -- string

      The following is possible:

      - ``'Signs'`` give the :class:`SignGroup`

      - ``'UU'`` give the :class:`RootsOfUnityGroup`

      - ``'UU_P'``, where ``'P'`` is
        a string representing a SageMath parent which is interpreted as
        ``exponents``

      - ``'Arg_P'``, where ``'P'`` is
        a string representing a SageMath parent which is interpreted as
        ``domain``

    - ``domain`` -- a SageMath parent representing a subset of the complex plane;
      an instance of :class:`ArgumentByElementGroup` will be created with the given
      ``domain``

    - ``exponents`` -- a SageMath parent representing a subset of the reals;
      an instance of :class`UnitCircleGroup` will be created with the given
      ``exponents``

    Exactly one of ``data``, ``specification``, ``exponents`` has to be provided.

    Further keyword parameters will be carried on to the initialization of
    the group.

    EXAMPLES::

        sage: from sage.groups.misc_gps.argument_groups import ArgumentGroup

        sage: ArgumentGroup('UU')                                                       # needs sage.rings.number_field
        Group of Roots of Unity

        sage: # needs sage.rings.number_field
        sage: ArgumentGroup(ZZ)
        Sign Group
        sage: ArgumentGroup(QQ)
        Sign Group
        sage: ArgumentGroup('UU_QQ')
        Group of Roots of Unity
        sage: ArgumentGroup(AA)
        Sign Group

        sage: ArgumentGroup(RR)                                                         # needs sage.rings.number_field
        Sign Group
        sage: ArgumentGroup('Arg_RR')                                                   # needs sage.rings.number_field
        Sign Group
        sage: ArgumentGroup(RIF)                                                        # needs sage.rings.real_interval_field
        Sign Group
        sage: ArgumentGroup(RBF)
        Sign Group

        sage: ArgumentGroup(CC)                                                         # needs sage.rings.number_field
        Unit Circle Group with Exponents in
        Real Field with 53 bits of precision modulo ZZ
        sage: ArgumentGroup('Arg_CC')                                                   # needs sage.rings.number_field
        Unit Circle Group with Exponents in
        Real Field with 53 bits of precision modulo ZZ
        sage: ArgumentGroup(CIF)
        Unit Circle Group with Exponents in
        Real Interval Field with 53 bits of precision modulo ZZ
        sage: ArgumentGroup(CBF)
        Unit Circle Group with Exponents in
        Real ball field with 53 bits of precision modulo ZZ

        sage: ArgumentGroup(CyclotomicField(3))                                         # needs sage.rings.number_field
        Unit Circle Group with Argument of Elements in
        Cyclotomic Field of order 3 and degree 2
    """
    def create_key_and_extra_args(self, data=None, specification=None, domain=None, exponents=None, **kwds):
        """
        Normalize the input.

        See :class:`ArgumentGroupFactory` for a description and examples.

        TESTS::

            sage: from sage.groups.misc_gps.argument_groups import ArgumentGroup

            sage: # needs sage.rings.number_field
            sage: ArgumentGroup(specification='UU')
            Group of Roots of Unity
            sage: ArgumentGroup('UU') is ArgumentGroup(exponents=QQ)  # indirect doctest
            True
            sage: ArgumentGroup('Arg_CC') is ArgumentGroup(exponents=RR)  # indirect doctest
            True
            sage: ArgumentGroup('Arg_CC') is ArgumentGroup(domain=CC)  # indirect doctest
            True
        """
    def create_object(self, version, key, **kwds):
        """
        Create an object from the given arguments.

        TESTS::

            sage: from sage.groups.misc_gps.argument_groups import ArgumentGroup
            sage: ArgumentGroup('UU')  # indirect doctest                               # needs sage.rings.number_field
            Group of Roots of Unity
        """

ArgumentGroup: Incomplete
