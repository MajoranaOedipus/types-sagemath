from .misc import WithLocals as WithLocals
from _typeshed import Incomplete
from sage.misc.superseded import experimental as experimental
from sage.rings.big_oh import O as O
from sage.structure.element import MultiplicativeGroupElement as MultiplicativeGroupElement
from sage.structure.factory import UniqueFactory as UniqueFactory
from sage.structure.parent import Parent as Parent
from sage.structure.richcmp import richcmp_by_eq_and_lt as richcmp_by_eq_and_lt
from sage.structure.unique_representation import UniqueRepresentation as UniqueRepresentation

class ZeroCoefficientError(ValueError): ...

def absorption(left, right):
    """
    Let one of the two passed terms absorb the other.

    Helper function used by
    :class:`~sage.rings.asymptotic.asymptotic_ring.AsymptoticExpansion`.

    .. NOTE::

        If neither of the terms can absorb the other, an
        :python:`ArithmeticError<library/exceptions.html#exceptions.ArithmeticError>`
        is raised.

        See the :ref:`module description <term_absorption>` for a
        detailed explanation of absorption.

    INPUT:

    - ``left`` -- an asymptotic term

    - ``right`` -- an asymptotic term

    OUTPUT: an asymptotic term or ``None``

    EXAMPLES::

        sage: from sage.rings.asymptotic.growth_group import GrowthGroup
        sage: from sage.rings.asymptotic.term_monoid import DefaultTermMonoidFactory as TermMonoid
        sage: from sage.rings.asymptotic.term_monoid import absorption
        sage: T = TermMonoid('O', GrowthGroup('x^ZZ'), ZZ)
        sage: absorption(T(x^2), T(x^3))
        O(x^3)
        sage: absorption(T(x^3), T(x^2))
        O(x^3)

    ::

        sage: T = TermMonoid('exact', GrowthGroup('x^ZZ'), ZZ)
        sage: absorption(T(x^2), T(x^3))
        Traceback (most recent call last):
        ...
        ArithmeticError: Absorption between x^2 and x^3 is not possible.
    """
def can_absorb(left, right):
    """
    Return whether one of the two input terms is able to absorb the
    other.

    Helper function used by
    :class:`~sage.rings.asymptotic.asymptotic_ring.AsymptoticExpansion`.

    INPUT:

    - ``left`` -- an asymptotic term

    - ``right`` -- an asymptotic term

    OUTPUT: boolean

    .. NOTE::

        See the :ref:`module description <term_absorption>` for a
        detailed explanation of absorption.

    EXAMPLES::

        sage: from sage.rings.asymptotic.growth_group import GrowthGroup
        sage: from sage.rings.asymptotic.term_monoid import DefaultTermMonoidFactory as TermMonoid
        sage: from sage.rings.asymptotic.term_monoid import can_absorb
        sage: T = TermMonoid('O', GrowthGroup('x^ZZ'), ZZ)
        sage: can_absorb(T(x^2), T(x^3))
        True
        sage: can_absorb(T(x^3), T(x^2))
        True
    """

class GenericTerm(MultiplicativeGroupElement):
    """
    Base class for asymptotic terms. Mainly the structure and
    several properties of asymptotic terms are handled here.

    INPUT:

    - ``parent`` -- the parent of the asymptotic term

    - ``growth`` -- an asymptotic growth element

    EXAMPLES::

        sage: from sage.rings.asymptotic.growth_group import GrowthGroup
        sage: from sage.rings.asymptotic.term_monoid import GenericTermMonoid
        sage: from sage.rings.asymptotic.term_monoid import DefaultTermMonoidFactory as TermMonoid

        sage: G = GrowthGroup('x^ZZ'); x = G.gen()
        sage: T = GenericTermMonoid(TermMonoid, G, QQ)
        sage: t1 = T(x); t2 = T(x^2); (t1, t2)
        (Generic Term with growth x, Generic Term with growth x^2)
        sage: t1 * t2
        Generic Term with growth x^3
        sage: t1.can_absorb(t2)
        False
        sage: t1.absorb(t2)
        Traceback (most recent call last):
        ...
        ArithmeticError: Generic Term with growth x cannot absorb Generic Term with growth x^2
        sage: t1.can_absorb(t1)
        False
    """
    growth: Incomplete
    def __init__(self, parent, growth) -> None:
        """
        See :class:`GenericTerm` for more information.

        TESTS::

            sage: from sage.rings.asymptotic.growth_group import GrowthGroup
            sage: from sage.rings.asymptotic.term_monoid import GenericTermMonoid
            sage: from sage.rings.asymptotic.term_monoid import DefaultTermMonoidFactory as TermMonoid

            sage: G = GrowthGroup('x^ZZ'); x = G.gen()
            sage: T = GenericTermMonoid(TermMonoid, G, ZZ)
            sage: T(x^2)
            Generic Term with growth x^2

        ::

            sage: from sage.rings.asymptotic.term_monoid import GenericTerm
            sage: GenericTerm(parent=None, growth=x)
            Traceback (most recent call last):
            ...
            ValueError: The parent must be provided
            sage: GenericTerm(T, GrowthGroup('y^ZZ').gen())
            Traceback (most recent call last):
            ...
            ValueError: y is not in Growth Group x^ZZ.
        """
    def construction(self):
        """
        Return a construction of this term.

        OUTPUT:

        A pair ``(cls, kwds)`` such that ``cls(**kwds)`` equals this term.

        EXAMPLES::

            sage: from sage.rings.asymptotic.growth_group import GrowthGroup
            sage: from sage.rings.asymptotic.term_monoid import DefaultTermMonoidFactory as TermMonoid

            sage: T = TermMonoid('O', GrowthGroup('x^ZZ'), QQ)
            sage: a = T.an_element(); a
            O(x)
            sage: cls, kwds = a.construction(); cls, kwds
            (<class 'sage.rings.asymptotic.term_monoid.OTermMonoid_with_category.element_class'>,
            {'growth': x,
             'parent': O-Term Monoid x^ZZ with implicit coefficients in Rational Field})
            sage: cls(**kwds) == a
            True

        .. SEEALSO::

            :meth:`TermWithCoefficient.construction`,
            :meth:`GenericTermMonoid.from_construction`
        """
    def __invert__(self) -> None:
        """
        Invert this term.

        OUTPUT: a :class:`GenericTerm`

        TESTS::

            sage: from sage.rings.asymptotic.growth_group import GrowthGroup
            sage: from sage.rings.asymptotic.term_monoid import GenericTermMonoid
            sage: from sage.rings.asymptotic.term_monoid import DefaultTermMonoidFactory as TermMonoid

            sage: G = GrowthGroup('x^ZZ'); x = G.gen()
            sage: T = GenericTermMonoid(TermMonoid, G, QQ)
            sage: ~T(x) # indirect doctest
            Traceback (most recent call last):
            ...
            NotImplementedError: Inversion of Generic Term with growth x
            not implemented (in this abstract method).

        ::

            sage: t1 = T(x); t2 = T(x^2)
            sage: t1 / t2
            Traceback (most recent call last):
            ...
            NotImplementedError: Inversion of Generic Term with growth x^2
            not implemented (in this abstract method).
        """
    def __pow__(self, exponent) -> None:
        """
        Calculate the power of this element to the given ``exponent``.

        INPUT:

        - ``exponent`` -- an element

        OUTPUT:

        Raise a :python:`NotImplementedError<library/exceptions.html#exceptions.NotImplementedError>`
        since it is an abstract base class.

        TESTS::

            sage: from sage.rings.asymptotic.term_monoid import GenericTermMonoid
            sage: from sage.rings.asymptotic.growth_group import GrowthGroup
            sage: from sage.rings.asymptotic.term_monoid import DefaultTermMonoidFactory as TermMonoid

            sage: G = GrowthGroup('z^ZZ')
            sage: t = GenericTermMonoid(TermMonoid, G, ZZ).an_element(); t
            Generic Term with growth z
            sage: t^3  # indirect doctest
            Traceback (most recent call last):
            ...
            NotImplementedError: Taking powers of Generic Term with growth z
            not implemented (in this abstract method).
        """
    def can_absorb(self, other):
        """
        Check whether this asymptotic term is able to absorb
        the asymptotic term ``other``.

        INPUT:

        - ``other`` -- an asymptotic term

        OUTPUT: boolean

        .. NOTE::

            A :class:`GenericTerm` cannot absorb any other term.

            See the :ref:`module description <term_absorption>` for a
            detailed explanation of absorption.

        EXAMPLES::

            sage: from sage.rings.asymptotic.growth_group import GenericGrowthGroup
            sage: from sage.rings.asymptotic.term_monoid import GenericTermMonoid
            sage: from sage.rings.asymptotic.term_monoid import DefaultTermMonoidFactory as TermMonoid

            sage: G = GenericGrowthGroup(ZZ)
            sage: T = GenericTermMonoid(TermMonoid, G, QQ)
            sage: g1 = G(raw_element=21); g2 = G(raw_element=42)
            sage: t1 = T(g1); t2 = T(g2)
            sage: t1.can_absorb(t2)  # indirect doctest
            False
            sage: t2.can_absorb(t1)  # indirect doctest
            False
        """
    def absorb(self, other, check: bool = True):
        """
        Absorb the asymptotic term ``other`` and return the resulting
        asymptotic term.

        INPUT:

        - ``other`` -- an asymptotic term

        - ``check`` -- boolean; if ``True`` (default), then ``can_absorb``
          is called before absorption

        OUTPUT:

        An asymptotic term or ``None`` if a cancellation occurs. If no
        absorption can be performed, an :python:`ArithmeticError<library/exceptions.html#exceptions.ArithmeticError>`
        is raised.

        .. NOTE::

            Setting ``check`` to ``False`` is meant to be used in
            cases where the respective comparison is done externally
            (in order to avoid duplicate checking).

            For a more detailed explanation of the *absorption* of
            asymptotic terms see
            the :ref:`module description <term_absorption>`.

        EXAMPLES:

        We want to demonstrate in which cases an asymptotic term
        is able to absorb another term, as well as explain the output
        of this operation. We start by defining some parents and
        elements::

            sage: from sage.rings.asymptotic.growth_group import GrowthGroup
            sage: from sage.rings.asymptotic.term_monoid import DefaultTermMonoidFactory as TermMonoid
            sage: G_QQ = GrowthGroup('x^QQ'); x = G_QQ.gen()
            sage: OT = TermMonoid('O', G_QQ, coefficient_ring=QQ)
            sage: ET = TermMonoid('exact', G_QQ, coefficient_ring=QQ)
            sage: ot1 = OT(x); ot2 = OT(x^2)
            sage: et1 = ET(x, coefficient=100); et2 = ET(x^2, coefficient=2)
            sage: et3 = ET(x^2, coefficient=1); et4 = ET(x^2, coefficient=-2)

        `O`-Terms are able to absorb other `O`-terms and exact terms
        with weaker or equal growth. ::

            sage: ot1.absorb(ot1)
            O(x)
            sage: ot1.absorb(et1)
            O(x)
            sage: ot1.absorb(et1) is ot1
            True

        :class:`ExactTerm` is able to absorb another
        :class:`ExactTerm` if the terms have the same growth. In this
        case, *absorption* is nothing else than an addition of the
        respective coefficients::

            sage: et2.absorb(et3)
            3*x^2
            sage: et3.absorb(et2)
            3*x^2
            sage: et3.absorb(et4)
            -x^2

        Note that, for technical reasons, the coefficient `0` is not
        allowed, and thus ``None`` is returned if two exact terms
        cancel each other out::

            sage: et2.absorb(et4)
            sage: et4.absorb(et2) is None
            True

        TESTS:

        When disabling the ``check`` flag, absorb might produce
        wrong results::

            sage: et1.absorb(ot2, check=False)
            O(x)
        """
    def log_term(self, base=None, locals=None) -> None:
        """
        Determine the logarithm of this term.

        INPUT:

        - ``base`` -- the base of the logarithm. If ``None``
          (default value) is used, the natural logarithm is taken.

        - ``locals`` -- dictionary which may contain the following keys and values:

          - ``'log'`` -- value: a function. If not used, then the usual
            :class:`log <sage.functions.log.Function_log>` is taken.

        OUTPUT: a tuple of terms

        .. NOTE::

            This abstract method raises a
            :python:`NotImplementedError<library/exceptions.html#exceptions.NotImplementedError>`.
            See :class:`ExactTerm` and :class:`OTerm` for a concrete
            implementation.

        EXAMPLES::

            sage: from sage.rings.asymptotic.growth_group import GrowthGroup
            sage: from sage.rings.asymptotic.term_monoid import GenericTermMonoid
            sage: from sage.rings.asymptotic.term_monoid import DefaultTermMonoidFactory as TermMonoid

            sage: T = GenericTermMonoid(TermMonoid, GrowthGroup('x^ZZ'), QQ)
            sage: T.an_element().log_term()
            Traceback (most recent call last):
            ...
            NotImplementedError: This method is not implemented in
            this abstract base class.

        ::

            sage: from sage.rings.asymptotic.term_monoid import TermWithCoefficientMonoid
            sage: T = TermWithCoefficientMonoid(TermMonoid, GrowthGroup('x^ZZ'), QQ)
            sage: T.an_element().log_term()
            Traceback (most recent call last):
            ...
            NotImplementedError: This method is not implemented in
            this abstract base class.

        .. SEEALSO::

            :meth:`ExactTerm.log_term`,
            :meth:`OTerm.log_term`.
        """
    def is_constant(self):
        """
        Return whether this term is an (exact) constant.

        OUTPUT: boolean

        .. NOTE::

            Only :class:`ExactTerm` with constant growth (`1`) are
            constant.

        EXAMPLES::

            sage: from sage.rings.asymptotic.growth_group import GrowthGroup
            sage: from sage.rings.asymptotic.term_monoid import GenericTermMonoid
            sage: from sage.rings.asymptotic.term_monoid import DefaultTermMonoidFactory as TermMonoid
            sage: T = GenericTermMonoid(TermMonoid, GrowthGroup('x^ZZ * log(x)^ZZ'), QQ)
            sage: t = T.an_element(); t
            Generic Term with growth x*log(x)
            sage: t.is_constant()
            False

        ::

            sage: T = TermMonoid('O', GrowthGroup('x^ZZ'), QQ)
            sage: T('x').is_constant()
            False
            sage: T(1).is_constant()
            False
        """
    def is_exact(self):
        """
        Return whether this term is an exact term.

        OUTPUT: boolean

        EXAMPLES::

            sage: from sage.rings.asymptotic.growth_group import GrowthGroup
            sage: from sage.rings.asymptotic.term_monoid import GenericTermMonoid
            sage: from sage.rings.asymptotic.term_monoid import DefaultTermMonoidFactory as TermMonoid
            sage: T = GenericTermMonoid(TermMonoid, GrowthGroup('x^ZZ * log(x)^ZZ'), QQ)
            sage: T.an_element().is_exact()
            False
        """
    def is_little_o_of_one(self) -> None:
        """
        Return whether this generic term is of order `o(1)`.

        OUTPUT: boolean

        EXAMPLES::

            sage: from sage.rings.asymptotic.growth_group import GrowthGroup
            sage: from sage.rings.asymptotic.term_monoid import (GenericTermMonoid,
            ....:                                                TermWithCoefficientMonoid)
            sage: from sage.rings.asymptotic.term_monoid import DefaultTermMonoidFactory as TermMonoid

            sage: T = GenericTermMonoid(TermMonoid, GrowthGroup('x^ZZ'), QQ)
            sage: T.an_element().is_little_o_of_one()
            Traceback (most recent call last):
            ...
            NotImplementedError: Cannot check whether Generic Term with growth x is o(1)
            in the abstract base class
            GenericTerm Monoid x^ZZ with (implicit) coefficients in Rational Field.
            sage: T = TermWithCoefficientMonoid(TermMonoid, GrowthGroup('x^ZZ'), QQ)
            sage: T.an_element().is_little_o_of_one()
            Traceback (most recent call last):
            ...
            NotImplementedError: Cannot check whether Term with coefficient 1/2 and growth x
            is o(1) in the abstract base class
            TermWithCoefficient Monoid x^ZZ with coefficients in Rational Field.
        """
    def rpow(self, base) -> None:
        """
        Return the power of ``base`` to this generic term.

        INPUT:

        - ``base`` -- an element or ``'e'``

        OUTPUT: a term

        EXAMPLES::

            sage: from sage.rings.asymptotic.growth_group import GrowthGroup
            sage: from sage.rings.asymptotic.term_monoid import GenericTermMonoid
            sage: from sage.rings.asymptotic.term_monoid import DefaultTermMonoidFactory as TermMonoid

            sage: T = GenericTermMonoid(TermMonoid, GrowthGroup('x^ZZ * log(x)^ZZ'), QQ)
            sage: T.an_element().rpow('e')
            Traceback (most recent call last):
            ...
            NotImplementedError: Cannot take e to the exponent
            Generic Term with growth x*log(x) in the abstract base class
            GenericTerm Monoid x^ZZ * log(x)^ZZ with (implicit) coefficients in Rational Field.
        """
    def variable_names(self):
        """
        Return the names of the variables of this term.

        OUTPUT: a tuple of strings

        EXAMPLES::

            sage: from sage.rings.asymptotic.term_monoid import DefaultTermMonoidFactory as TermMonoid
            sage: T = TermMonoid('exact', 'QQ^m * m^QQ * log(n)^ZZ', QQ)
            sage: T('4 * 2^m * m^4 * log(n)').variable_names()
            ('m', 'n')
            sage: T('4 * 2^m * m^4').variable_names()
            ('m',)
            sage: T('4 * log(n)').variable_names()
            ('n',)
            sage: T('4 * m^3').variable_names()
            ('m',)
            sage: T('4 * m^0').variable_names()
            ()
        """

class GenericTermMonoid(UniqueRepresentation, Parent, WithLocals):
    """
    Parent for generic asymptotic terms.

    INPUT:

    - ``growth_group`` -- a growth group (i.e. an instance of
      :class:`~sage.rings.asymptotic.growth_group.GenericGrowthGroup`)

    - ``coefficient_ring`` -- a ring which contains the (maybe implicit)
      coefficients of the elements

    - ``category`` -- the category of the parent can be specified
      in order to broaden the base structure. It has to be a subcategory
      of ``Join of Category of Monoids and Category of posets``. This
      is also the default category if ``None`` is specified.

    In this class the base
    structure for asymptotic term monoids will be handled. These
    monoids are the parents of asymptotic terms (for example, see
    :class:`GenericTerm` or :class:`OTerm`). Basically, asymptotic
    terms consist of a ``growth`` (which is an asymptotic growth
    group element, for example
    :class:`~sage.rings.asymptotic.growth_group.MonomialGrowthElement`);
    additional structure and properties are added by the classes inherited
    from :class:`GenericTermMonoid`.

    EXAMPLES::

        sage: from sage.rings.asymptotic.growth_group import GrowthGroup
        sage: from sage.rings.asymptotic.term_monoid import GenericTermMonoid
        sage: from sage.rings.asymptotic.term_monoid import DefaultTermMonoidFactory as TermMonoid

        sage: G_x = GrowthGroup('x^ZZ'); x = G_x.gen()
        sage: G_y = GrowthGroup('y^QQ'); y = G_y.gen()
        sage: T_x_ZZ = GenericTermMonoid(TermMonoid, G_x, QQ)
        sage: T_y_QQ = GenericTermMonoid(TermMonoid, G_y, QQ)
        sage: T_x_ZZ
        GenericTerm Monoid x^ZZ with (implicit) coefficients in Rational Field
        sage: T_y_QQ
        GenericTerm Monoid y^QQ with (implicit) coefficients in Rational Field
    """
    Element = GenericTerm
    @staticmethod
    def __classcall__(cls, term_monoid_factory, growth_group, coefficient_ring, category=None):
        """
        Normalize the input in order to ensure a unique
        representation of the parent.

        TESTS::

            sage: from sage.rings.asymptotic.term_monoid import GenericTermMonoid
            sage: from sage.rings.asymptotic.growth_group import GrowthGroup
            sage: from sage.rings.asymptotic.term_monoid import DefaultTermMonoidFactory as TermMonoid

            sage: G = GrowthGroup('x^ZZ')
            sage: T = GenericTermMonoid(TermMonoid, G, QQ)
            sage: T._underlying_class()(TermMonoid, G, QQ) is T
            True

        ::

            sage: GenericTermMonoid(TermMonoid, None, ZZ)  # indirect doctest
            Traceback (most recent call last):
            ...
            ValueError: No growth group specified.
            sage: GenericTermMonoid(TermMonoid, int, ZZ)  # indirect doctest
            Traceback (most recent call last):
            ...
            TypeError: <... 'int'> is not a valid growth group.
            sage: GenericTermMonoid(TermMonoid, G, None)  # indirect doctest
            Traceback (most recent call last):
            ...
            ValueError: No coefficient ring specified.
            sage: GenericTermMonoid(TermMonoid, G, int)  # indirect doctest
            Traceback (most recent call last):
            ...
            TypeError: <... 'int'> is not a valid coefficient ring.
        """
    def __init__(self, term_monoid_factory, growth_group, coefficient_ring, category) -> None:
        """
        See :class:`GenericTermMonoid` for more information.

        EXAMPLES::

            sage: from sage.rings.asymptotic.term_monoid import GenericTermMonoid, TermWithCoefficientMonoid
            sage: from sage.rings.asymptotic.growth_group import GrowthGroup
            sage: from sage.rings.asymptotic.term_monoid import DefaultTermMonoidFactory as TermMonoid

            sage: G_x = GrowthGroup('x^ZZ')
            sage: T_x = GenericTermMonoid(TermMonoid, G_x, QQ); T_x
            GenericTerm Monoid x^ZZ with (implicit) coefficients in Rational Field
            sage: T_x.growth_group
            Growth Group x^ZZ
            sage: G_y = GrowthGroup('y^QQ')
            sage: T_y = GenericTermMonoid(TermMonoid, G_y, QQ); T_y
            GenericTerm Monoid y^QQ with (implicit) coefficients in Rational Field
            sage: T_x is T_y
            False

        ::

            sage: GenericTermMonoid(TermMonoid, None, None)
            Traceback (most recent call last):
            ...
            ValueError: No growth group specified.

        ::

            sage: G = GrowthGroup('x^ZZ')
            sage: T_ZZ = TermWithCoefficientMonoid(TermMonoid, G, ZZ); T_ZZ
            TermWithCoefficient Monoid x^ZZ with coefficients in Integer Ring
            sage: T_QQ = TermWithCoefficientMonoid(TermMonoid, G, QQ); T_QQ
            TermWithCoefficient Monoid x^ZZ with coefficients in Rational Field
            sage: T_QQ.category()
            Join of Category of monoids and Category of posets
        """
    @property
    def term_monoid_factory(self):
        """
        The term monoid factory capable of creating this term monoid.

        EXAMPLES::

            sage: from sage.rings.asymptotic.growth_group import GrowthGroup

            sage: from sage.rings.asymptotic.term_monoid import DefaultTermMonoidFactory
            sage: DefaultTermMonoidFactory('exact', GrowthGroup('x^ZZ'), ZZ).term_monoid_factory
            Term Monoid Factory 'sage.rings.asymptotic.term_monoid.DefaultTermMonoidFactory'

            sage: from sage.rings.asymptotic.term_monoid import TermMonoidFactory
            sage: TermMonoid = TermMonoidFactory('__main__.TermMonoid')

            sage: TermMonoid('exact', GrowthGroup('x^ZZ'), ZZ).term_monoid_factory
            Term Monoid Factory '__main__.TermMonoid'
        """
    def term_monoid(self, type):
        """
        Return the term monoid of specified ``type``.

        INPUT:

        - ``type`` -- 'O' or 'exact', or an instance of an existing term monoid.
          See :class:`~sage.rings.asymptotic.term_monoid.TermMonoidFactory` for
          more details.

        OUTPUT:

        A term monoid object derived from
        :class:`~sage.rings.asymptotic.term_monoid.GenericTermMonoid`.

        EXAMPLES::

            sage: from sage.rings.asymptotic.growth_group import GrowthGroup
            sage: from sage.rings.asymptotic.term_monoid import DefaultTermMonoidFactory as TermMonoid
            sage: E = TermMonoid('exact', GrowthGroup('x^ZZ'), ZZ); E
            Exact Term Monoid x^ZZ with coefficients in Integer Ring
            sage: E.term_monoid('O')
            O-Term Monoid x^ZZ with implicit coefficients in Integer Ring

        TESTS::

            sage: E.term_monoid('exact') is E
            True
        """
    @property
    def growth_group(self):
        """
        The growth group underlying this term monoid.

        EXAMPLES::

            sage: from sage.rings.asymptotic.growth_group import GrowthGroup
            sage: from sage.rings.asymptotic.term_monoid import DefaultTermMonoidFactory as TermMonoid
            sage: TermMonoid('exact', GrowthGroup('x^ZZ'), ZZ).growth_group
            Growth Group x^ZZ
        """
    @property
    def coefficient_ring(self):
        """
        The coefficient ring of this term monoid, i.e. the ring where
        the coefficients are from.

        EXAMPLES::

            sage: from sage.rings.asymptotic.growth_group import GrowthGroup
            sage: from sage.rings.asymptotic.term_monoid import GenericTermMonoid
            sage: from sage.rings.asymptotic.term_monoid import DefaultTermMonoidFactory as TermMonoid

            sage: GenericTermMonoid(TermMonoid, GrowthGroup('x^ZZ'), ZZ).coefficient_ring
            Integer Ring
        """
    def change_parameter(self, growth_group=None, coefficient_ring=None):
        """
        Return a term monoid with a change in one or more of the
        given parameters.

        INPUT:

        - ``growth_group`` -- (default: ``None``) the new growth group

        - ``coefficient_ring`` -- (default: ``None``) the new coefficient ring

        OUTPUT: a term monoid

        EXAMPLES::

            sage: from sage.rings.asymptotic.growth_group import GrowthGroup
            sage: from sage.rings.asymptotic.term_monoid import DefaultTermMonoidFactory as TermMonoid
            sage: E = TermMonoid('exact', GrowthGroup('n^ZZ'), ZZ)
            sage: E.change_parameter(coefficient_ring=QQ)
            Exact Term Monoid n^ZZ with coefficients in Rational Field
            sage: E.change_parameter(growth_group=GrowthGroup('n^QQ'))
            Exact Term Monoid n^QQ with coefficients in Integer Ring

        TESTS::

            sage: E.change_parameter() is E
            True
            sage: E.change_parameter(growth_group=None) is E
            True
            sage: E.change_parameter(coefficient_ring=None) is E
            True
            sage: E.change_parameter(growth_group=None, coefficient_ring=None) is E
            True
        """
    def from_construction(self, construction, **kwds_overrides):
        """
        Create a term from the construction of another term.

        INPUT:

        - ``construction`` -- a pair ``(cls, kwds_construction)``

        - ``kwds_overrides`` -- dictionary

        OUTPUT: a term

        EXAMPLES::

            sage: from sage.rings.asymptotic.growth_group import GrowthGroup
            sage: from sage.rings.asymptotic.term_monoid import DefaultTermMonoidFactory as TermMonoid
            sage: G = GrowthGroup('x^ZZ')
            sage: x = G.gen()
            sage: T = TermMonoid('O', G, QQ)
            sage: o = T.an_element()

        We use a construction directly as input::

            sage: T.from_construction(o.construction())
            O(x)

        We can override the given data::

            sage: T.from_construction(o.construction(), growth=x^2)
            O(x^2)

        A minimalistic example::

            sage: T.from_construction((None, {'growth': x}))
            O(x)

        .. SEEALSO::

            :meth:`GenericTerm.construction`,
            :meth:`TermWithCoefficient.construction`

        TESTS::

            sage: from sage.rings.asymptotic.term_monoid import GenericTermMonoid
            sage: T = GenericTermMonoid(TermMonoid, G, QQ)
            sage: T(G.gen())  # indirect doctest
            Generic Term with growth x

            sage: T = TermMonoid('O', G, QQ)
            sage: T(G.gen())  # indirect doctest
            O(x)
            sage: T(G.gen(), SR.var('y'))  # indirect doctest
            Traceback (most recent call last):
            ...
            ValueError: Cannot create OTerm(x) since given coefficient y
            is not valid in O-Term Monoid x^ZZ with implicit coefficients in
            Rational Field.
            > *previous* TypeError: unable to convert y to a rational
        """
    def some_elements(self):
        """
        Return some elements of this term monoid.

        See :class:`TestSuite` for a typical use case.

        OUTPUT: an iterator

        EXAMPLES::

            sage: from sage.rings.asymptotic.growth_group import GrowthGroup
            sage: from sage.rings.asymptotic.term_monoid import DefaultTermMonoidFactory as TermMonoid
            sage: G = GrowthGroup('x^ZZ')
            sage: tuple(TermMonoid('O', G, QQ).some_elements())
            (O(1), O(x), O(x^(-1)), O(x^2), O(x^(-2)), O(x^3), ...)
        """
    def le(self, left, right):
        """
        Return whether the term ``left`` is at most (less than or equal
        to) the term ``right``.

        INPUT:

        - ``left`` -- an element

        - ``right`` -- an element

        OUTPUT: boolean

        EXAMPLES::

            sage: from sage.rings.asymptotic.growth_group import GrowthGroup
            sage: from sage.rings.asymptotic.term_monoid import GenericTermMonoid
            sage: from sage.rings.asymptotic.term_monoid import DefaultTermMonoidFactory as TermMonoid

            sage: G = GrowthGroup('x^ZZ'); x = G.gen()
            sage: T = GenericTermMonoid(TermMonoid, G, QQ)
            sage: t1 = T(x); t2 = T(x^2)
            sage: T.le(t1, t2)
            True
        """

class OTerm(GenericTerm):
    """
    Class for an asymptotic term representing an `O`-term with
    specified growth. For the mathematical properties of `O`-terms
    see :wikipedia:`Big_O_Notation`.

    `O`-terms can *absorb* terms of weaker or equal growth.

    INPUT:

    - ``parent`` -- the parent of the asymptotic term

    - ``growth`` -- a growth element

    EXAMPLES::

        sage: from sage.rings.asymptotic.growth_group import GrowthGroup
        sage: from sage.rings.asymptotic.term_monoid import OTermMonoid
        sage: from sage.rings.asymptotic.term_monoid import DefaultTermMonoidFactory as TermMonoid

        sage: G = GrowthGroup('x^ZZ'); x = G.gen()
        sage: OT = OTermMonoid(TermMonoid, G, QQ)
        sage: t1 = OT(x^-7); t2 = OT(x^5); t3 = OT(x^42)
        sage: t1, t2, t3
        (O(x^(-7)), O(x^5), O(x^42))
        sage: t1.can_absorb(t2)
        False
        sage: t2.can_absorb(t1)
        True
        sage: t2.absorb(t1)
        O(x^5)
        sage: t1 <= t2 and t2 <= t3
        True
        sage: t3 <= t1
        False

    The conversion of growth elements also works for the creation
    of `O`-terms::

        sage: x = SR('x'); x.parent()
        Symbolic Ring
        sage: OT(x^17)
        O(x^17)
    """
    def __invert__(self) -> None:
        """
        Invert this term.

        OUTPUT:

        A :exc:`ZeroDivisionError` since `O`-terms cannot be inverted.

        TESTS::

            sage: from sage.rings.asymptotic.growth_group import GrowthGroup
            sage: from sage.rings.asymptotic.term_monoid import DefaultTermMonoidFactory as TermMonoid
            sage: G = GrowthGroup('x^ZZ'); x = G.gen()
            sage: T = TermMonoid('O', G, QQ)
            sage: ~T(x) # indirect doctest
            Traceback (most recent call last):
            ...
            ZeroDivisionError: Cannot invert O(x).
        """
    def __pow__(self, exponent):
        """
        Calculate the power of this :class:`OTerm` to the given ``exponent``.

        INPUT:

        - ``exponent`` -- an element

        OUTPUT: an :class:`OTerm`

        TESTS::

            sage: from sage.rings.asymptotic.term_monoid import DefaultTermMonoidFactory as TermMonoid
            sage: from sage.rings.asymptotic.growth_group import GrowthGroup
            sage: G = GrowthGroup('z^ZZ')
            sage: t = TermMonoid('O', G, ZZ).an_element(); t
            O(z)
            sage: t^3  # indirect doctest
            O(z^3)
            sage: t^(1/2)  # indirect doctest
            O(z^(1/2))
            sage: t^(-1)  # indirect doctest
            Traceback (most recent call last):
            ...
            ZeroDivisionError: Cannot take O(z) to exponent -1.
            > *previous* ZeroDivisionError: rational division by zero
        """
    def can_absorb(self, other):
        """
        Check whether this `O`-term can absorb ``other``.

        INPUT:

        - ``other`` -- an asymptotic term

        OUTPUT: boolean

        .. NOTE::

            An :class:`OTerm` can absorb any other asymptotic term
            with weaker or equal growth.

            See the :ref:`module description <term_absorption>` for a
            detailed explanation of absorption.

        EXAMPLES::

            sage: from sage.rings.asymptotic.growth_group import GrowthGroup
            sage: from sage.rings.asymptotic.term_monoid import DefaultTermMonoidFactory as TermMonoid
            sage: OT = TermMonoid('O', GrowthGroup('x^ZZ'), QQ)
            sage: t1 = OT(x^21); t2 = OT(x^42)
            sage: t1.can_absorb(t2)
            False
            sage: t2.can_absorb(t1)
            True
        """
    def log_term(self, base=None, locals=None):
        """
        Determine the logarithm of this O-term.

        INPUT:

        - ``base`` -- the base of the logarithm. If ``None``
          (default value) is used, the natural logarithm is taken.

        - ``locals`` -- dictionary which may contain the following keys and values:

          - ``'log'`` -- value: a function. If not used, then the usual
            :class:`log <sage.functions.log.Function_log>` is taken.

        OUTPUT: a tuple of terms

        .. NOTE::

            This method returns a tuple with the summands that come from
            applying the rule `\\log(x\\cdot y) = \\log(x) + \\log(y)`.

        EXAMPLES::

            sage: from sage.rings.asymptotic.growth_group import GrowthGroup
            sage: from sage.rings.asymptotic.term_monoid import DefaultTermMonoidFactory as TermMonoid
            sage: T = TermMonoid('O', GrowthGroup('x^ZZ * log(x)^ZZ'), QQ)
            sage: T(x^2).log_term()
            (O(log(x)),)
            sage: T(x^1234).log_term()
            (O(log(x)),)

        ::

            sage: from sage.rings.asymptotic.term_monoid import TermWithCoefficientMonoid
            sage: T = TermMonoid('O', GrowthGroup('x^ZZ * log(x)^ZZ * y^ZZ * log(y)^ZZ'), QQ)
            sage: T('x * y').log_term()
            (O(log(x)), O(log(y)))

        .. SEEALSO::

            :meth:`ExactTerm.log_term`.
        """
    def is_little_o_of_one(self):
        """
        Return whether this O-term is of order `o(1)`.

        OUTPUT: boolean

        EXAMPLES::

            sage: from sage.rings.asymptotic.growth_group import GrowthGroup
            sage: from sage.rings.asymptotic.term_monoid import DefaultTermMonoidFactory as TermMonoid
            sage: T = TermMonoid('O', GrowthGroup('x^ZZ'), QQ)
            sage: T(x).is_little_o_of_one()
            False
            sage: T(1).is_little_o_of_one()
            False
            sage: T(x^(-1)).is_little_o_of_one()
            True

        ::

            sage: T = TermMonoid('O', GrowthGroup('x^ZZ * y^ZZ'), QQ)
            sage: T('x * y^(-1)').is_little_o_of_one()
            False
            sage: T('x^(-1) * y').is_little_o_of_one()
            False
            sage: T('x^(-2) * y^(-3)').is_little_o_of_one()
            True

        ::

            sage: T = TermMonoid('O', GrowthGroup('x^QQ * log(x)^QQ'), QQ)
            sage: T('x * log(x)^2').is_little_o_of_one()
            False
            sage: T('x^2 * log(x)^(-1234)').is_little_o_of_one()
            False
            sage: T('x^(-1) * log(x)^4242').is_little_o_of_one()
            True
            sage: T('x^(-1/100) * log(x)^(1000/7)').is_little_o_of_one()
            True
        """
    def rpow(self, base):
        """
        Return the power of ``base`` to this O-term.

        INPUT:

        - ``base`` -- an element or ``'e'``

        OUTPUT: a term

        .. NOTE::

            For :class:`OTerm`, the powers can only be
            constructed for exponents `O(1)` or if ``base`` is `1`.

        EXAMPLES::

            sage: from sage.rings.asymptotic.growth_group import GrowthGroup
            sage: from sage.rings.asymptotic.term_monoid import DefaultTermMonoidFactory as TermMonoid
            sage: T = TermMonoid('O', GrowthGroup('x^ZZ * log(x)^ZZ'), QQ)
            sage: T(1).rpow('e')
            O(1)
            sage: T(1).rpow(2)
            O(1)

        ::

            sage: T.an_element().rpow(1)
            1
            sage: T('x^2').rpow(1)
            1

        ::

            sage: T.an_element().rpow('e')
            Traceback (most recent call last):
            ...
            ValueError: Cannot take e to the exponent O(x*log(x)) in
            O-Term Monoid x^ZZ * log(x)^ZZ with implicit coefficients in Rational Field
            sage: T('log(x)').rpow('e')
            Traceback (most recent call last):
            ...
            ValueError: Cannot take e to the exponent O(log(x)) in
            O-Term Monoid x^ZZ * log(x)^ZZ with implicit coefficients in Rational Field
        """

class OTermMonoid(GenericTermMonoid):
    """
    Parent for asymptotic big `O`-terms.

    INPUT:

    - ``growth_group`` -- a growth group

    - ``category`` -- the category of the parent can be specified
      in order to broaden the base structure. It has to be a subcategory
      of ``Join of Category of monoids and Category of posets``. This
      is also the default category if ``None`` is specified.

    EXAMPLES::

        sage: from sage.rings.asymptotic.growth_group import GrowthGroup
        sage: from sage.rings.asymptotic.term_monoid import OTermMonoid
        sage: from sage.rings.asymptotic.term_monoid import DefaultTermMonoidFactory as TermMonoid
        sage: G_x_ZZ = GrowthGroup('x^ZZ')
        sage: G_y_QQ = GrowthGroup('y^QQ')
        sage: OT_x_ZZ = OTermMonoid(TermMonoid, G_x_ZZ, QQ); OT_x_ZZ
        O-Term Monoid x^ZZ with implicit coefficients in Rational Field
        sage: OT_y_QQ = OTermMonoid(TermMonoid, G_y_QQ, QQ); OT_y_QQ
        O-Term Monoid y^QQ with implicit coefficients in Rational Field

    `O`-term monoids can also be created by using the
    :class:`term factory <TermMonoidFactory>`::

        sage: TermMonoid('O', G_x_ZZ, QQ) is OT_x_ZZ
        True
        sage: TermMonoid('O', GrowthGroup('x^QQ'), QQ)
        O-Term Monoid x^QQ with implicit coefficients in Rational Field
    """
    Element = OTerm

class TermWithCoefficient(GenericTerm):
    """
    Base class for asymptotic terms possessing a coefficient. For
    example, :class:`ExactTerm` directly inherits from this class.

    INPUT:

    - ``parent`` -- the parent of the asymptotic term

    - ``growth`` -- an asymptotic growth element of the parent's growth group

    - ``coefficient`` -- an element of the parent's coefficient ring

    EXAMPLES::

        sage: from sage.rings.asymptotic.growth_group import GrowthGroup
        sage: from sage.rings.asymptotic.term_monoid import TermWithCoefficientMonoid
        sage: from sage.rings.asymptotic.term_monoid import DefaultTermMonoidFactory as TermMonoid

        sage: G = GrowthGroup('x^ZZ'); x = G.gen()
        sage: CT_ZZ = TermWithCoefficientMonoid(TermMonoid, G, ZZ)
        sage: CT_QQ = TermWithCoefficientMonoid(TermMonoid, G, QQ)
        sage: CT_ZZ(x^2, coefficient=5)
        Term with coefficient 5 and growth x^2
        sage: CT_QQ(x^3, coefficient=3/8)
        Term with coefficient 3/8 and growth x^3
    """
    coefficient: Incomplete
    def __init__(self, parent, growth, coefficient) -> None:
        """
        See :class:`TermWithCoefficient` for more information.

        EXAMPLES:

        First, we define some monoids::

            sage: from sage.rings.asymptotic.growth_group import GrowthGroup
            sage: from sage.rings.asymptotic.term_monoid import TermWithCoefficientMonoid
            sage: from sage.rings.asymptotic.term_monoid import DefaultTermMonoidFactory as TermMonoid

            sage: G = GrowthGroup('x^ZZ'); x = G.gen()
            sage: CT_ZZ = TermWithCoefficientMonoid(TermMonoid, G, ZZ)
            sage: CT_QQ = TermWithCoefficientMonoid(TermMonoid, G, QQ)

        The coefficients have to be from the given coefficient ring::

            sage: CT_ZZ(x, 1/2)
            Traceback (most recent call last):
            ...
            ValueError: Cannot create TermWithCoefficient(x)
            since given coefficient 1/2 is not valid in
            TermWithCoefficient Monoid x^ZZ with coefficients in Integer Ring.
            > *previous* TypeError: no conversion of this rational to integer
            sage: CT_QQ(x, coefficient=1/2)
            Term with coefficient 1/2 and growth x

        For technical reasons, the coefficient 0 is not allowed::

            sage: CT_ZZ(x^42, 0)
            Traceback (most recent call last):
            ...
            ZeroCoefficientError:  Zero coefficient 0 is not allowed in
            TermWithCoefficient Monoid x^ZZ with coefficients in Integer Ring.

        The conversion of growth elements also works for the creation
        of terms with coefficient::

            sage: x = SR('x'); x.parent()
            Symbolic Ring
            sage: CT_ZZ(x^42, coefficient=42)
            Term with coefficient 42 and growth x^42
        """
    def construction(self):
        """
        Return a construction of this term.

        OUTPUT:

        A pair ``(cls, kwds)`` such that ``cls(**kwds)`` equals this term.

        EXAMPLES::

            sage: from sage.rings.asymptotic.growth_group import GrowthGroup
            sage: from sage.rings.asymptotic.term_monoid import DefaultTermMonoidFactory as TermMonoid

            sage: T = TermMonoid('exact', GrowthGroup('x^ZZ'), QQ)
            sage: a = T.an_element(); a
            1/2*x
            sage: cls, kwds = a.construction(); cls, kwds
            (<class 'sage.rings.asymptotic.term_monoid.ExactTermMonoid_with_category.element_class'>,
             {'coefficient': 1/2,
              'growth': x,
              'parent': Exact Term Monoid x^ZZ with coefficients in Rational Field})
            sage: cls(**kwds) == a
            True

        .. SEEALSO::

            :meth:`GenericTerm.construction`,
            :meth:`GenericTermMonoid.from_construction`
        """

class TermWithCoefficientMonoid(GenericTermMonoid):
    """
    This class implements the base structure for parents of
    asymptotic terms possessing a coefficient from some coefficient
    ring. In particular, this is also the parent for
    :class:`TermWithCoefficient`.

    INPUT:

    - ``growth_group`` -- a growth group

    - ``category`` -- the category of the parent can be specified
      in order to broaden the base structure. It has to be a subcategory
      of ``Join of Category of monoids and Category of posets``. This
      is also the default category if ``None`` is specified.

    - ``coefficient_ring`` -- the ring which contains the
      coefficients of the elements

    EXAMPLES::

        sage: from sage.rings.asymptotic.growth_group import GrowthGroup
        sage: from sage.rings.asymptotic.term_monoid import TermWithCoefficientMonoid
        sage: from sage.rings.asymptotic.term_monoid import DefaultTermMonoidFactory as TermMonoid

        sage: G_ZZ = GrowthGroup('x^ZZ'); x_ZZ = G_ZZ.gen()
        sage: G_QQ = GrowthGroup('x^QQ'); x_QQ = G_QQ.gen()
        sage: TC_ZZ = TermWithCoefficientMonoid(TermMonoid, G_ZZ, QQ); TC_ZZ
        TermWithCoefficient Monoid x^ZZ with coefficients in Rational Field
        sage: TC_QQ = TermWithCoefficientMonoid(TermMonoid, G_QQ, QQ); TC_QQ
        TermWithCoefficient Monoid x^QQ with coefficients in Rational Field
        sage: TC_ZZ == TC_QQ or TC_ZZ is TC_QQ
        False
        sage: TC_QQ.coerce_map_from(TC_ZZ)
        Coercion map:
          From: TermWithCoefficient Monoid x^ZZ with coefficients in Rational Field
          To:   TermWithCoefficient Monoid x^QQ with coefficients in Rational Field
    """
    Element = TermWithCoefficient
    def some_elements(self):
        """
        Return some elements of this term with coefficient monoid.

        See :class:`TestSuite` for a typical use case.

        OUTPUT: an iterator

        EXAMPLES::

            sage: from itertools import islice
            sage: from sage.rings.asymptotic.term_monoid import DefaultTermMonoidFactory as TermMonoid
            sage: from sage.rings.asymptotic.growth_group import GrowthGroup
            sage: G = GrowthGroup('z^QQ')
            sage: T = TermMonoid('exact', G, ZZ)
            sage: tuple(islice(T.some_elements(), int(10)))
            (z^(1/2), z^(-1/2), -z^(1/2), z^2, -z^(-1/2), 2*z^(1/2),
             z^(-2), -z^2, 2*z^(-1/2), -2*z^(1/2))
        """

class ExactTerm(TermWithCoefficient):
    """
    Class for asymptotic exact terms. These terms primarily consist of
    an asymptotic growth element as well as a coefficient.

    INPUT:

    - ``parent`` -- the parent of the asymptotic term

    - ``growth`` -- an asymptotic growth element from ``parent.growth_group``

    - ``coefficient`` -- an element from ``parent.coefficient_ring``

    EXAMPLES::

        sage: from sage.rings.asymptotic.growth_group import GrowthGroup
        sage: from sage.rings.asymptotic.term_monoid import DefaultTermMonoidFactory as TermMonoid
        sage: from sage.rings.asymptotic.term_monoid import ExactTermMonoid
        sage: G = GrowthGroup('x^ZZ'); x = G.gen()
        sage: ET = ExactTermMonoid(TermMonoid, G, QQ)

    Asymptotic exact terms may be multiplied (with the usual rules
    applying)::

        sage: ET(x^2, coefficient=3) * ET(x, coefficient=-1)
        -3*x^3
        sage: ET(x^0, coefficient=4) * ET(x^5, coefficient=2)
        8*x^5

    They may also be multiplied with `O`-terms::

        sage: OT = TermMonoid('O', G, QQ)
        sage: ET(x^2, coefficient=42) * OT(x)
        O(x^3)

    Absorption for asymptotic exact terms relates to addition::

        sage: ET(x^2, coefficient=5).can_absorb(ET(x^5, coefficient=12))
        False
        sage: ET(x^2, coefficient=5).can_absorb(ET(x^2, coefficient=1))
        True
        sage: ET(x^2, coefficient=5).absorb(ET(x^2, coefficient=1))
        6*x^2

    Note that, as for technical reasons, `0` is not allowed as a
    coefficient for an asymptotic term with coefficient. Instead ``None``
    is returned if two asymptotic exact terms cancel out each other
    during absorption::

        sage: ET(x^2, coefficient=42).can_absorb(ET(x^2, coefficient=-42))
        True
        sage: ET(x^2, coefficient=42).absorb(ET(x^2, coefficient=-42)) is None
        True

    Exact terms can also be created by converting monomials with
    coefficient from the symbolic ring, or a suitable polynomial
    or power series ring::

        sage: x = var('x'); x.parent()
        Symbolic Ring
        sage: ET(5*x^2)
        5*x^2
    """
    def __invert__(self):
        """
        Invert this term.

        OUTPUT: a term

        TESTS::

            sage: from sage.rings.asymptotic.growth_group import GrowthGroup
            sage: from sage.rings.asymptotic.term_monoid import DefaultTermMonoidFactory as TermMonoid
            sage: G = GrowthGroup('x^ZZ'); x = G.gen()
            sage: T = TermMonoid('exact', G, ZZ)
            sage: ~T(x, coefficient=2)  # indirect doctest
            1/2*x^(-1)
            sage: (~T(x, coefficient=2)).parent()
            Exact Term Monoid x^ZZ with coefficients in Rational Field
        """
    def __pow__(self, exponent):
        """
        Calculate the power of this :class:`ExactTerm` to the given ``exponent``.

        INPUT:

        - ``exponent`` -- an element

        OUTPUT: an :class:`ExactTerm`

        TESTS::

            sage: from sage.rings.asymptotic.term_monoid import DefaultTermMonoidFactory as TermMonoid
            sage: from sage.rings.asymptotic.growth_group import GrowthGroup
            sage: G = GrowthGroup('z^ZZ')
            sage: T = TermMonoid('exact', G, ZZ)
            sage: t = T('2*z'); t
            2*z
            sage: t^3  # indirect doctest
            8*z^3
            sage: t^(1/2)  # indirect doctest
            sqrt(2)*z^(1/2)
        """
    def can_absorb(self, other):
        """
        Check whether this exact term can absorb ``other``.

        INPUT:

        - ``other`` -- an asymptotic term

        OUTPUT: boolean

        .. NOTE::

            For :class:`ExactTerm`, absorption corresponds to
            addition. This means that an exact term can absorb
            only other exact terms with the same growth.

            See the :ref:`module description <term_absorption>` for a
            detailed explanation of absorption.

        EXAMPLES::

            sage: from sage.rings.asymptotic.growth_group import GrowthGroup
            sage: from sage.rings.asymptotic.term_monoid import DefaultTermMonoidFactory as TermMonoid
            sage: ET = TermMonoid('exact', GrowthGroup('x^ZZ'), ZZ)
            sage: t1 = ET(x^21, coefficient=1); t2 = ET(x^21, coefficient=2); t3 = ET(x^42, coefficient=1)
            sage: t1.can_absorb(t2)
            True
            sage: t2.can_absorb(t1)
            True
            sage: t1.can_absorb(t3) or t3.can_absorb(t1)
            False
        """
    def log_term(self, base=None, locals=None):
        """
        Determine the logarithm of this exact term.

        INPUT:

        - ``base`` -- the base of the logarithm. If ``None``
          (default value) is used, the natural logarithm is taken.


        - ``locals`` -- dictionary which may contain the following keys and values:

          - ``'log'`` -- value: a function. If not used, then the usual
            :class:`log <sage.functions.log.Function_log>` is taken.

        OUTPUT: a tuple of terms

        .. NOTE::

            This method returns a tuple with the summands that come from
            applying the rule `\\log(x\\cdot y) = \\log(x) + \\log(y)`.

        EXAMPLES::

            sage: from sage.rings.asymptotic.growth_group import GrowthGroup
            sage: from sage.rings.asymptotic.term_monoid import DefaultTermMonoidFactory as TermMonoid
            sage: T = TermMonoid('exact', GrowthGroup('x^ZZ * log(x)^ZZ'), SR)
            sage: T(3*x^2).log_term()
            (log(3), 2*log(x))
            sage: T(x^1234).log_term()
            (1234*log(x),)
            sage: T(49*x^7).log_term(base=7)
            (2, 7/log(7)*log(x))

        ::

            sage: T = TermMonoid('exact', GrowthGroup('x^ZZ * log(x)^ZZ * y^ZZ * log(y)^ZZ'), SR)
            sage: T('x * y').log_term()
            (log(x), log(y))
            sage: T('4 * x * y').log_term(base=2)
            (2, 1/log(2)*log(x), 1/log(2)*log(y))

        .. SEEALSO::

            :meth:`OTerm.log_term`.
        """
    def is_constant(self):
        """
        Return whether this term is an (exact) constant.

        OUTPUT: boolean

        .. NOTE::

            Only :class:`ExactTerm` with constant growth (`1`) are
            constant.

        EXAMPLES::

            sage: from sage.rings.asymptotic.growth_group import GrowthGroup
            sage: from sage.rings.asymptotic.term_monoid import DefaultTermMonoidFactory as TermMonoid
            sage: T = TermMonoid('exact', GrowthGroup('x^ZZ * log(x)^ZZ'), QQ)
            sage: T('x * log(x)').is_constant()
            False
            sage: T('3*x').is_constant()
            False
            sage: T(1/2).is_constant()
            True
            sage: T(42).is_constant()
            True
        """
    def is_little_o_of_one(self):
        """
        Return whether this exact term is of order `o(1)`.

        OUTPUT: boolean

        EXAMPLES::

            sage: from sage.rings.asymptotic.growth_group import GrowthGroup
            sage: from sage.rings.asymptotic.term_monoid import DefaultTermMonoidFactory as TermMonoid
            sage: T = TermMonoid('exact', GrowthGroup('x^ZZ'), QQ)
            sage: T(x).is_little_o_of_one()
            False
            sage: T(1).is_little_o_of_one()
            False
            sage: T(x^(-1)).is_little_o_of_one()
            True

        ::

            sage: T = TermMonoid('exact', GrowthGroup('x^ZZ * y^ZZ'), QQ)
            sage: T('x * y^(-1)').is_little_o_of_one()
            False
            sage: T('x^(-1) * y').is_little_o_of_one()
            False
            sage: T('x^(-2) * y^(-3)').is_little_o_of_one()
            True

        ::

            sage: T = TermMonoid('exact', GrowthGroup('x^QQ * log(x)^QQ'), QQ)
            sage: T('x * log(x)^2').is_little_o_of_one()
            False
            sage: T('x^2 * log(x)^(-1234)').is_little_o_of_one()
            False
            sage: T('x^(-1) * log(x)^4242').is_little_o_of_one()
            True
            sage: T('x^(-1/100) * log(x)^(1000/7)').is_little_o_of_one()
            True
        """
    def is_exact(self):
        """
        Return whether this term is an exact term.

        OUTPUT: boolean

        EXAMPLES::

            sage: from sage.rings.asymptotic.growth_group import GrowthGroup
            sage: from sage.rings.asymptotic.term_monoid import DefaultTermMonoidFactory as TermMonoid
            sage: T = TermMonoid('exact', GrowthGroup('x^ZZ * log(x)^ZZ'), QQ)
            sage: T('x * log(x)').is_exact()
            True
            sage: T('3 * x^2').is_exact()
            True

        TESTS::

            sage: T = TermMonoid('O', GrowthGroup('x^ZZ'), QQ)
            sage: T('x').is_exact()
            False
        """
    def rpow(self, base):
        """
        Return the power of ``base`` to this exact term.

        INPUT:

        - ``base`` -- an element or ``'e'``

        OUTPUT: a term

        EXAMPLES::

            sage: from sage.rings.asymptotic.growth_group import GrowthGroup
            sage: from sage.rings.asymptotic.term_monoid import DefaultTermMonoidFactory as TermMonoid
            sage: T = TermMonoid('exact', GrowthGroup('QQ^x * x^ZZ * log(x)^ZZ'), QQ)
            sage: T('x').rpow(2)
            2^x
            sage: T('log(x)').rpow('e')
            x
            sage: T('42*log(x)').rpow('e')
            x^42
            sage: T('3*x').rpow(2)
            8^x

        ::

            sage: T('3*x^2').rpow(2)
            Traceback (most recent call last):
            ...
            ArithmeticError: Cannot construct 2^(x^2) in
            Growth Group QQ^x * x^ZZ * log(x)^ZZ * Signs^x
            > *previous* TypeError: unsupported operand parent(s) for *:
            'Growth Group QQ^x * x^ZZ * log(x)^ZZ * Signs^x' and
            'Growth Group ZZ^(x^2)'

        ::

            sage: T = TermMonoid('exact', GrowthGroup('(QQ_+)^n * n^QQ'), SR)
            sage: n = T('n')
            sage: n.rpow(2)
            2^n
            sage: _.parent()
            Exact Term Monoid QQ^n * n^QQ with coefficients in Symbolic Ring
        """

class ExactTermMonoid(TermWithCoefficientMonoid):
    """
    Parent for asymptotic exact terms, implemented in
    :class:`ExactTerm`.

    INPUT:

    - ``growth_group`` -- a growth group

    - ``category`` -- the category of the parent can be specified
      in order to broaden the base structure. It has to be a subcategory
      of ``Join of Category of monoids and Category of posets``. This
      is also the default category if ``None`` is specified.

    - ``coefficient_ring`` -- the ring which contains the coefficients of
      the elements

    EXAMPLES::

        sage: from sage.rings.asymptotic.growth_group import GrowthGroup
        sage: from sage.rings.asymptotic.term_monoid import ExactTermMonoid
        sage: from sage.rings.asymptotic.term_monoid import DefaultTermMonoidFactory as TermMonoid

        sage: G_ZZ = GrowthGroup('x^ZZ'); x_ZZ = G_ZZ.gen()
        sage: G_QQ = GrowthGroup('x^QQ'); x_QQ = G_QQ.gen()
        sage: ET_ZZ = ExactTermMonoid(TermMonoid, G_ZZ, ZZ); ET_ZZ
        Exact Term Monoid x^ZZ with coefficients in Integer Ring
        sage: ET_QQ = ExactTermMonoid(TermMonoid, G_QQ, QQ); ET_QQ
        Exact Term Monoid x^QQ with coefficients in Rational Field
        sage: ET_QQ.coerce_map_from(ET_ZZ)
        Coercion map:
          From: Exact Term Monoid x^ZZ with coefficients in Integer Ring
          To:   Exact Term Monoid x^QQ with coefficients in Rational Field

    Exact term monoids can also be created using the
    :class:`term factory <TermMonoidFactory>`::

        sage: TermMonoid('exact', G_ZZ, ZZ) is ET_ZZ
        True
        sage: TermMonoid('exact', GrowthGroup('x^ZZ'), QQ)
        Exact Term Monoid x^ZZ with coefficients in Rational Field
    """
    Element = ExactTerm

class BTerm(TermWithCoefficient):
    """
    Class for asymptotic B-terms.

    A B-term represents all functions which (in absolute value) are bounded
    by the given ``growth`` and ``coefficient`` for the parameters
    given by ``valid_from``.
    For example, we have terms that represent functions

    - bounded by `5|x|^2` for `|x| \\ge 3`,

    - bounded by `42|x|^3` for `|x| \\ge 15` and `|y| \\ge 15`, or

    - bounded by `42 |x|^3 |y|^2` for `|x| \\ge 10` and `|y| \\ge 20` (see below for the actual examples).

    INPUT:

    - ``parent`` -- the parent of the asymptotic term

    - ``growth`` -- an asymptotic growth element of
      the parent's growth group

    - ``coefficient`` -- an element of the parent's coefficient ring

    - ``valid_from`` -- dictionary mapping variable names to lower bounds
      for the corresponding variable. The bound implied by this term is valid when
      all variables are at least their corresponding lower bound. If a number
      is passed to ``valid_from``, then the lower bounds for all variables of
      the asymptotic expansion are set to this number

    EXAMPLES:

    We revisit the examples from the introduction::

        sage: from sage.rings.asymptotic.term_monoid import DefaultTermMonoidFactory as TermMonoid
        sage: from sage.rings.asymptotic.growth_group import GrowthGroup
        sage: G = GrowthGroup('x^ZZ * y^ZZ')
        sage: T = TermMonoid('B', growth_group=G, coefficient_ring=ZZ)
        sage: x, y = G('x'), G('y')

    This is a term bounded by `5|x|^2` for `|x| \\ge 3`::

        sage: T(x^2, coefficient=5, valid_from={'x': 3})
        B(5*x^2, x >= 3)

    This is a term bounded by `42|x|^3` for `|x| \\ge 15` and `|y| \\ge 15`::

        sage: T(x^3, coefficient=42, valid_from={'x': 15, 'y': 15})
        B(42*x^3, x >= 15, y >= 15)

    This is a term bounded by `42 |x|^3 |y|^2` for `|x| \\ge 10` and `|y| \\ge 20`::

        sage: T(x^3*y^2, coefficient=42, valid_from={'x': 10, 'y': 20})
        B(42*x^3*y^2, x >= 10, y >= 20)
    """
    coefficient: Incomplete
    valid_from: Incomplete
    def __init__(self, parent, growth, valid_from, **kwds) -> None:
        """
        See :class:`BTerm` for more information.

        TESTS::

            sage: from sage.rings.asymptotic.growth_group import MonomialGrowthGroup
            sage: from sage.rings.asymptotic.growth_group import GrowthGroup
            sage: from sage.rings.asymptotic.term_monoid import DefaultTermMonoidFactory as TermMonoid

            sage: G = MonomialGrowthGroup(ZZ, 'x');
            sage: BT_QQ = TermMonoid('B', G, QQ)
            sage: BT_QQ(x^3, coefficient=3, valid_from={'m': 20})
            Traceback (most recent call last):
            ...
            ValueError: B-Term has valid_from variables defined which do
            not occur in the term.
            sage: BT_QQ(x^3, coefficient=0, valid_from={'x': 20})
            Traceback (most recent call last):
            ...
            ZeroCoefficientError: Zero coefficient 0 is not allowed in
            B-Term Monoid x^ZZ with coefficients in Rational Field.

            sage: BT_ZZ = TermMonoid('B', G, ZZ)
            sage: BT_ZZ(x, coefficient=1/2, valid_from={'x': 20})
            Traceback (most recent call last):
            ...
            ValueError: Cannot create BTerm(x)
            since given coefficient 1/2 is not valid in
            B-Term Monoid x^ZZ with coefficients in Integer Ring.
            > *previous* TypeError: no conversion of this rational to integer
            sage: B = GrowthGroup('x^ZZ * y^ZZ');
            sage: x, y = B('x'), B('y')
            sage: BT_ZZ = TermMonoid('B', B, ZZ)
            sage: BT_ZZ(x^3, coefficient=42, valid_from={'x': 10})
            B(42*x^3, x >= 10)
            sage: BT_ZZ(x^3, coefficient=42, valid_from={'x': 10, 'y': 20})
            B(42*x^3, x >= 10, y >= 20)
            sage: BT_ZZ(x^3*y^2, coefficient=42, valid_from={'x': 10})
            Traceback (most recent call last):
            ValueError: B-Term has not defined all variables which occur in the term in valid_from.
            sage: BT_ZZ(x^3, coefficient=42, valid_from={'x': 10, 'z': 20})
            Traceback (most recent call last):
            ...
            ValueError: B-Term has valid_from variables defined which do not occur in the term.
        """
    def construction(self):
        """
        Return a construction of this term.

        OUTPUT:

        A pair ``(cls, kwds)`` such that ``cls(**kwds)`` equals this term.

        EXAMPLES::

            sage: from sage.rings.asymptotic.growth_group import GrowthGroup
            sage: from sage.rings.asymptotic.term_monoid import TermMonoidFactory
            sage: TermMonoid = TermMonoidFactory('__main__.TermMonoid')

            sage: T = TermMonoid('B', GrowthGroup('x^ZZ'), QQ)
            sage: a = T.an_element(); a
            B(1/2*x, x >= 42)
            sage: cls, kwds = a.construction(); cls, kwds
            (<class 'sage.rings.asymptotic.term_monoid.BTermMonoid_with_category.element_class'>,
             {'coefficient': 1/2,
              'growth': x,
              'parent': B-Term Monoid x^ZZ with coefficients in Rational Field,
              'valid_from': {'x': 42}})
            sage: cls(**kwds) == a
            True

        .. SEEALSO::

            :meth:`GenericTerm.construction`,
            :meth:`TermWithCoefficient.construction`,
            :meth:`GenericTermMonoid.from_construction`
        """
    def can_absorb(self, other):
        """
        Check whether this B-term can absorb ``other``.

        INPUT:

        - ``other`` -- an asymptotic term

        OUTPUT: boolean

        .. NOTE::

            A :class:`BTerm` can absorb another :class:`BTerm`
            with weaker or equal growth.

            See the :ref:`module description <term_absorption>` for a
            detailed explanation of absorption.

        EXAMPLES::

            sage: from sage.rings.asymptotic.growth_group import GrowthGroup
            sage: from sage.rings.asymptotic.term_monoid import DefaultTermMonoidFactory as TermMonoid
            sage: BT = TermMonoid('B', GrowthGroup('x^ZZ'), QQ)
            sage: t1 = BT(x^3, coefficient=3, valid_from={'x': 20})
            sage: t2 = BT(x^2, coefficient=1, valid_from={'x': 10})
            sage: t3 = BT(x^3, coefficient=10, valid_from={'x': 10})
            sage: t1.can_absorb(t2)
            True
            sage: t2.can_absorb(t1)
            False
            sage: t1.can_absorb(t3)
            True
            sage: t3.can_absorb(t1)
            True
            sage: ET = TermMonoid('exact', GrowthGroup('x^ZZ'), QQ)
            sage: t4 = ET(x^3, coefficient=5)
            sage: t1.can_absorb(t4)
            True

        TESTS::

            sage: from sage.rings.asymptotic.growth_group import MonomialGrowthGroup
            sage: from sage.rings.asymptotic.term_monoid import DefaultTermMonoidFactory as TermMonoid

            sage: G = MonomialGrowthGroup(ZZ, 'x')
            sage: BT = TermMonoid('B', G, QQ)
            sage: t1 = BT(x, coefficient=3, valid_from={'x': 20})
            sage: t2 = BT(x^3, coefficient=5, valid_from={'x': 5})
            sage: t3 = BT(x^3, coefficient=10, valid_from={'x': 10})
            sage: t2.absorb(t1)
            B(2003/400*x^3, x >= 20)
            sage: t2.absorb(t3)
            B(15*x^3, x >= 10)
            sage: t3.absorb(t2)
            B(15*x^3, x >= 10)
        """

class BTermMonoid(TermWithCoefficientMonoid):
    """
    Parent for asymptotic B-terms.

    INPUT:

    - ``growth_group`` -- a growth group

    - ``coefficient_ring`` -- the ring which contains the
      coefficients of the elements

    - ``category`` -- the category of the parent can be specified
      in order to broaden the base structure. It has to be a subcategory
      of ``Join of Category of monoids and Category of posets``. This
      is also the default category if ``None`` is specified.

    EXAMPLES::

        sage: from sage.rings.asymptotic.growth_group import MonomialGrowthGroup
        sage: from sage.rings.asymptotic.term_monoid import BTermMonoid
        sage: from sage.rings.asymptotic.term_monoid import DefaultTermMonoidFactory as TermMonoid

        sage: G = MonomialGrowthGroup(ZZ, 'x')
        sage: BT = TermMonoid('B', G, QQ)
        sage: BT
        B-Term Monoid x^ZZ with coefficients in Rational Field
        sage: BT is BTermMonoid(TermMonoid, G, QQ)
        True
    """
    __init__: Incomplete
    Element = BTerm
    def some_elements(self):
        """
        Return some elements of this B-term monoid.

        See :class:`TestSuite` for a typical use case.

        OUTPUT: an iterator

        EXAMPLES::

            sage: from itertools import islice
            sage: from sage.rings.asymptotic.term_monoid import TermMonoidFactory
            sage: TermMonoid = TermMonoidFactory('__main__.TermMonoid')
            sage: from sage.rings.asymptotic.growth_group import GrowthGroup
            sage: G = GrowthGroup('z^QQ')
            sage: T = TermMonoid('B', G, ZZ)
            sage: tuple(islice(T.some_elements(), int(10)))
            (B(z^(1/2), z >= 0),
             B(z^(-1/2), z >= 1),
             B(z^(1/2), z >= 3),
             B(z^2, z >= 42),
             B(z^(-1/2), z >= 0),
             B(2*z^(1/2), z >= 1),
             B(z^(-2), z >= 3),
             B(z^2, z >= 42),
             B(2*z^(-1/2), z >= 0),
             B(2*z^(1/2), z >= 1))
        """

class TermMonoidFactory(UniqueRepresentation, UniqueFactory):
    """
    Factory for asymptotic term monoids. It can generate the following
    term monoids:

    - :class:`OTermMonoid`,

    - :class:`ExactTermMonoid`,

    - :class:`BTermMonoid`.

    .. NOTE::

        An instance of this factory is available as ``DefaultTermMonoidFactory``.

    INPUT:

    - ``term_monoid`` -- the kind of terms held in the new term monoid
      Either a string ``'exact'``, ``'O'`` (capital letter ``O``) or
      ``'B'`` or an existing instance of a term
      monoid.

    - ``growth_group`` -- a growth group or a string describing a growth group

    - ``coefficient_ring`` -- a ring

    - ``asymptotic_ring`` -- if specified, then ``growth_group`` and
      ``coefficient_ring`` are taken from this asymptotic ring

    OUTPUT: an asymptotic term monoid

    EXAMPLES::

        sage: from sage.rings.asymptotic.growth_group import GrowthGroup
        sage: from sage.rings.asymptotic.term_monoid import DefaultTermMonoidFactory as TermMonoid
        sage: G = GrowthGroup('x^ZZ')
        sage: TermMonoid('O', G, QQ)
        O-Term Monoid x^ZZ with implicit coefficients in Rational Field
        sage: TermMonoid('exact', G, ZZ)
        Exact Term Monoid x^ZZ with coefficients in Integer Ring

    ::

        sage: R = AsymptoticRing(growth_group=G, coefficient_ring=QQ)
        sage: TermMonoid('exact', asymptotic_ring=R)
        Exact Term Monoid x^ZZ with coefficients in Rational Field
        sage: TermMonoid('O', asymptotic_ring=R)
        O-Term Monoid x^ZZ with implicit coefficients in Rational Field

        sage: TermMonoid('exact', 'QQ^m * m^QQ * log(n)^ZZ', ZZ)
        Exact Term Monoid QQ^m * m^QQ * Signs^m * log(n)^ZZ
        with coefficients in Integer Ring

    TESTS::

        sage: TermMonoid(TermMonoid('O', G, ZZ), asymptotic_ring=R)
        O-Term Monoid x^ZZ with implicit coefficients in Rational Field
        sage: TermMonoid(TermMonoid('exact', G, ZZ), asymptotic_ring=R)
        Exact Term Monoid x^ZZ with coefficients in Rational Field
        sage: from sage.rings.asymptotic.term_monoid import GenericTermMonoid
        sage: TermMonoid(GenericTermMonoid(TermMonoid, G, ZZ), asymptotic_ring=R)
        GenericTerm Monoid x^ZZ with (implicit) coefficients in Rational Field

    ::

        sage: TestSuite(TermMonoid('exact', GrowthGroup('x^ZZ'), QQ)).run(verbose=True)  # long time
        running ._test_an_element() . . . pass
        running ._test_associativity() . . . pass
        running ._test_cardinality() . . . pass
        running ._test_category() . . . pass
        running ._test_construction() . . . pass
        running ._test_elements() . . .
          Running the test suite of self.an_element()
          running ._test_category() . . . pass
          running ._test_eq() . . . pass
          running ._test_new() . . . pass
          running ._test_not_implemented_methods() . . . pass
          running ._test_pickling() . . . pass
          pass
        running ._test_elements_eq_reflexive() . . . pass
        running ._test_elements_eq_symmetric() . . . pass
        running ._test_elements_eq_transitive() . . . pass
        running ._test_elements_neq() . . . pass
        running ._test_eq() . . . pass
        running ._test_new() . . . pass
        running ._test_not_implemented_methods() . . . pass
        running ._test_one() . . . pass
        running ._test_pickling() . . . pass
        running ._test_prod() . . . pass
        running ._test_some_elements() . . . pass

    ::

        sage: TestSuite(TermMonoid('O', GrowthGroup('x^QQ'), ZZ)).run(verbose=True)  # long time
        running ._test_an_element() . . . pass
        running ._test_associativity() . . . pass
        running ._test_cardinality() . . . pass
        running ._test_category() . . . pass
        running ._test_construction() . . . pass
        running ._test_elements() . . .
          Running the test suite of self.an_element()
          running ._test_category() . . . pass
          running ._test_eq() . . . pass
          running ._test_new() . . . pass
          running ._test_not_implemented_methods() . . . pass
          running ._test_pickling() . . . pass
          pass
        running ._test_elements_eq_reflexive() . . . pass
        running ._test_elements_eq_symmetric() . . . pass
        running ._test_elements_eq_transitive() . . . pass
        running ._test_elements_neq() . . . pass
        running ._test_eq() . . . pass
        running ._test_new() . . . pass
        running ._test_not_implemented_methods() . . . pass
        running ._test_one() . . . pass
        running ._test_pickling() . . . pass
        running ._test_prod() . . . pass
        running ._test_some_elements() . . . pass
    """
    ExactTermMonoid: Incomplete
    OTermMonoid: Incomplete
    BTermMonoid: Incomplete
    def __init__(self, name, exact_term_monoid_class=None, O_term_monoid_class=None, B_term_monoid_class=None) -> None:
        """
        See :class:`TermMonoidFactory` for more information.

        TESTS::


            sage: from sage.rings.asymptotic.growth_group import GrowthGroup
            sage: from sage.rings.asymptotic.term_monoid import ExactTermMonoid, OTermMonoid, BTermMonoid
            sage: from sage.rings.asymptotic.term_monoid import TermMonoidFactory

            sage: class MyExactTermMonoid(ExactTermMonoid):
            ....:     pass
            sage: class MyOTermMonoid(OTermMonoid):
            ....:     pass
            sage: class MyBTermMonoid(BTermMonoid):
            ....:     pass
            sage: MyTermMonoid = TermMonoidFactory('MyTermMonoid',
            ....:                                  exact_term_monoid_class=MyExactTermMonoid,
            ....:                                  O_term_monoid_class=MyOTermMonoid,
            ....:                                  B_term_monoid_class=MyBTermMonoid)
            sage: G = GrowthGroup('x^ZZ')
            sage: type(MyTermMonoid('exact', G, QQ))
            <class '__main__.MyExactTermMonoid_with_category'>
            sage: type(MyTermMonoid('O', G, QQ))
            <class '__main__.MyOTermMonoid_with_category'>
            sage: type(MyTermMonoid('B', G, QQ))
            <class '__main__.MyBTermMonoid_with_category'>
        """
    def create_key_and_extra_args(self, term_monoid, growth_group=None, coefficient_ring=None, asymptotic_ring=None, **kwds):
        """
        Given the arguments and keyword, create a key that uniquely
        determines this object.

        EXAMPLES::

            sage: from sage.rings.asymptotic.growth_group import GrowthGroup
            sage: from sage.rings.asymptotic.term_monoid import DefaultTermMonoidFactory as TermMonoid
            sage: G = GrowthGroup('x^ZZ')
            sage: TermMonoid.create_key_and_extra_args('O', G, QQ)
            ((<class 'sage.rings.asymptotic.term_monoid.OTermMonoid'>,
              Growth Group x^ZZ, Rational Field), {})
            sage: TermMonoid.create_key_and_extra_args('exact', G, ZZ)
            ((<class 'sage.rings.asymptotic.term_monoid.ExactTermMonoid'>,
              Growth Group x^ZZ, Integer Ring), {})
            sage: TermMonoid.create_key_and_extra_args('exact', G)
            Traceback (most recent call last):
            ...
            ValueError: A coefficient ring has to be specified
            to create a term monoid of type 'exact'

        TESTS::

            sage: TermMonoid.create_key_and_extra_args('icecream', G)
            Traceback (most recent call last):
            ...
            ValueError: Term specification 'icecream' has to be either
            'exact', 'O', 'B' or an instance of an existing term.
            sage: TermMonoid.create_key_and_extra_args('O', ZZ)
            Traceback (most recent call last):
            ...
            ValueError: Integer Ring has to be an asymptotic growth group
        """
    def create_object(self, version, key, **kwds):
        """
        Create a object from the given arguments.

        EXAMPLES::

            sage: from sage.rings.asymptotic.growth_group import GrowthGroup
            sage: from sage.rings.asymptotic.term_monoid import DefaultTermMonoidFactory as TermMonoid
            sage: G = GrowthGroup('x^ZZ')
            sage: TermMonoid('O', G, QQ)  # indirect doctest
            O-Term Monoid x^ZZ with implicit coefficients in Rational Field
            sage: TermMonoid('exact', G, ZZ)  # indirect doctest
            Exact Term Monoid x^ZZ with coefficients in Integer Ring
        """
    def __hash__(self):
        """
        Return a hash of this object.

        TESTS::

            sage: from sage.rings.asymptotic.term_monoid import DefaultTermMonoidFactory as TermMonoid
            sage: hash(TermMonoid)  # random
            42
        """

DefaultTermMonoidFactory: Incomplete
