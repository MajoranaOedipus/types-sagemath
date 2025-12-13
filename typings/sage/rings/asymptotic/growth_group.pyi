from .misc import WithLocals as WithLocals
from _typeshed import Incomplete
from sage.categories.additive_magmas import AdditiveMagmas as AdditiveMagmas
from sage.categories.division_rings import DivisionRings as DivisionRings
from sage.categories.groups import Groups as Groups
from sage.categories.magmas import Magmas as Magmas
from sage.categories.posets import Posets as Posets
from sage.categories.pushout import ConstructionFunctor as ConstructionFunctor
from sage.categories.sets_cat import Sets as Sets
from sage.misc.lazy_import import lazy_import as lazy_import
from sage.structure.element import MultiplicativeGroupElement as MultiplicativeGroupElement
from sage.structure.factory import UniqueFactory as UniqueFactory
from sage.structure.parent import Parent as Parent
from sage.structure.richcmp import richcmp_by_eq_and_lt as richcmp_by_eq_and_lt
from sage.structure.sage_object import SageObject as SageObject
from sage.structure.unique_representation import CachedRepresentation as CachedRepresentation, UniqueRepresentation as UniqueRepresentation
from typing import NamedTuple

class Variable(CachedRepresentation, SageObject):
    """
    A class managing the variable of a growth group.

    INPUT:

    - ``var`` -- an object whose representation string is used as the
      variable. It has to be a valid Python identifier. ``var`` can
      also be a tuple (or other iterable) of such objects.

    - ``repr`` -- (default: ``None``) if specified, then this string
      will be displayed instead of ``var``. Use this to get
      e.g. ``log(x)^ZZ``: ``var`` is then used to specify the variable `x`.

    - ``latex_name`` -- (default: ``None``) if specified, then this string
      will be used as LaTeX-representation of ``var``

    - ``ignore`` -- (default: ``None``) a tuple (or other iterable)
      of strings which are not variables

    TESTS::

        sage: from sage.rings.asymptotic.growth_group import Variable
        sage: v = Variable('x'); repr(v), v.variable_names()
        ('x', ('x',))
        sage: v = Variable('x1'); repr(v), v.variable_names()
        ('x1', ('x1',))
        sage: v = Variable('x_42'); repr(v), v.variable_names()
        ('x_42', ('x_42',))
        sage: v = Variable(' x'); repr(v), v.variable_names()
        ('x', ('x',))
        sage: v = Variable('x '); repr(v), v.variable_names()
        ('x', ('x',))
        sage: v = Variable(''); repr(v), v.variable_names()
        ('', ())

    ::

        sage: v = Variable(('x', 'y')); repr(v), v.variable_names()
        ('x, y', ('x', 'y'))
        sage: v = Variable(('x', 'log(y)')); repr(v), v.variable_names()
        ('x, log(y)', ('x', 'y'))
        sage: v = Variable(('x', 'log(x)')); repr(v), v.variable_names()
        Traceback (most recent call last):
        ...
        ValueError: Variable names ('x', 'x') are not pairwise distinct.

    ::

        sage: v = Variable('log(x)'); repr(v), v.variable_names()
        ('log(x)', ('x',))
        sage: v = Variable('log(log(x))'); repr(v), v.variable_names()
        ('log(log(x))', ('x',))

    ::

        sage: v = Variable('x', repr='log(x)'); repr(v), v.variable_names()
        ('log(x)', ('x',))

    ::

        sage: v = Variable('e^x', ignore=('e',)); repr(v), v.variable_names()
        ('e^x', ('x',))

    ::

        sage: v = Variable('(e^n)', ignore=('e',)); repr(v), v.variable_names()
        ('e^n', ('n',))
        sage: v = Variable('(e^(n*log(n)))', ignore=('e',)); repr(v), v.variable_names()
        ('e^(n*log(n))', ('n',))
    """
    var_bases: Incomplete
    var_repr: Incomplete
    latex_name: Incomplete
    def __init__(self, var, repr=None, latex_name=None, ignore=None) -> None:
        """
        See :class:`Variable` for details.

        TESTS::

            sage: from sage.rings.asymptotic.growth_group import Variable
            sage: Variable('blub')
            blub
            sage: Variable('blub') is Variable('blub')
            True

        ::

            sage: Variable('(:-)')
            Traceback (most recent call last):
            ...
            TypeError: Malformed expression: : !!! -
            sage: Variable('(:-)', repr='icecream')
            Traceback (most recent call last):
            ...
            ValueError: ':-' is not a valid name for a variable.

        Check :issue:`26452`::

            sage: Variable(('w',),
            ....:          repr='w^(Number Field in i with defining polynomial x^2 + 1) * log(w)^ZZ')
            w^(Number Field in i with defining polynomial x^2 + 1) * log(w)^ZZ
        """
    def __hash__(self):
        """
        Return the hash of this variable.

        TESTS::

            sage: from sage.rings.asymptotic.growth_group import Variable
            sage: hash(Variable('blub'))  # random
            -123456789
        """
    def __eq__(self, other):
        """
        Compare whether this variable equals ``other``.

        INPUT:

        - ``other`` -- another variable

        OUTPUT: boolean

        TESTS::

            sage: from sage.rings.asymptotic.growth_group import Variable
            sage: Variable('x') == Variable('x')
            True
            sage: Variable('x') == Variable('y')
            False
        """
    def __ne__(self, other):
        """
        Return whether this variable does not equal ``other``.

        INPUT:

        - ``other`` -- another variable

        OUTPUT: boolean

        TESTS::

            sage: from sage.rings.asymptotic.growth_group import Variable
            sage: Variable('x') != Variable('x')
            False
            sage: Variable('x') != Variable('y')
            True
        """
    def variable_names(self):
        """
        Return the names of the variables.

        OUTPUT: a tuple of strings

        EXAMPLES::

            sage: from sage.rings.asymptotic.growth_group import Variable
            sage: Variable('x').variable_names()
            ('x',)
            sage: Variable('log(x)').variable_names()
            ('x',)
        """
    def is_monomial(self):
        """
        Return whether this is a monomial variable.

        OUTPUT: boolean

        EXAMPLES::

            sage: from sage.rings.asymptotic.growth_group import Variable
            sage: Variable('x').is_monomial()
            True
            sage: Variable('log(x)').is_monomial()
            False
        """
    @staticmethod
    def extract_variable_names(s):
        """
        Determine the name of the variable for the given string.

        INPUT:

        - ``s`` -- string

        OUTPUT: a tuple of strings

        EXAMPLES::

            sage: from sage.rings.asymptotic.growth_group import Variable
            sage: Variable.extract_variable_names('')
            ()
            sage: Variable.extract_variable_names('x')
            ('x',)
            sage: Variable.extract_variable_names('exp(x)')
            ('x',)
            sage: Variable.extract_variable_names('sin(cos(ln(x)))')
            ('x',)

        ::

            sage: Variable.extract_variable_names('log(77w)')
            ('w',)
            sage: Variable.extract_variable_names('log(x')
            Traceback (most recent call last):
            ...
            TypeError: Bad function call: log(x !!!
            sage: Variable.extract_variable_names('x)')
            Traceback (most recent call last):
            ...
            TypeError: Malformed expression: x) !!!
            sage: Variable.extract_variable_names('log)x(')
            Traceback (most recent call last):
            ...
            TypeError: Malformed expression: log) !!! x(
            sage: Variable.extract_variable_names('log(x)+y')
            ('x', 'y')
            sage: Variable.extract_variable_names('icecream(summer)')
            ('summer',)

        ::

            sage: Variable.extract_variable_names('a + b')
            ('a', 'b')
            sage: Variable.extract_variable_names('a+b')
            ('a', 'b')
            sage: Variable.extract_variable_names('a +b')
            ('a', 'b')
            sage: Variable.extract_variable_names('+a')
            ('a',)
            sage: Variable.extract_variable_names('a+')
            Traceback (most recent call last):
            ...
            TypeError: Malformed expression: a+ !!!
            sage: Variable.extract_variable_names('b!')
            ('b',)
            sage: Variable.extract_variable_names('-a')
            ('a',)
            sage: Variable.extract_variable_names('a*b')
            ('a', 'b')
            sage: Variable.extract_variable_names('2^q')
            ('q',)
            sage: Variable.extract_variable_names('77')
            ()

        ::

            sage: Variable.extract_variable_names('a + (b + c) + d')
            ('a', 'b', 'c', 'd')
        """

class PartialConversionValueError(ValueError):
    """
    A special :python:`ValueError<library/exceptions.html#exceptions.ValueError>`
    which is raised when (partial) conversion fails.

    INPUT:

    - ``element`` -- a :class:`PartialConversionElement`

    The remaining argument passed on to
    :python:`ValueError<library/exceptions.html#exceptions.ValueError>`.
    """
    element: Incomplete
    def __init__(self, element, *args, **kwds) -> None:
        """
        See :exc:`PartialConversionValueError` for more information.

        TESTS::

            sage: from sage.rings.asymptotic.growth_group import PartialConversionValueError, PartialConversionElement, GrowthGroup
            sage: raise PartialConversionValueError(
            ....:     PartialConversionElement(GrowthGroup('QQ^n'), -2), 'wrong value')
            Traceback (most recent call last):
            ...
            PartialConversionValueError: wrong value
        """

class PartialConversionElement(SageObject):
    """
    A not converted element of a growth group.

    INPUT:

    - ``growth_group`` -- a group group

    - ``raw_element`` -- an object

    A :class:`PartialConversionElement` is an element ``growth_group(raw_element)``
    which usually appears in conjunction with :exc:`PartialConversionValueError`.
    In this case, it was to possible to create that element, although
    the conversion went partially well in the sense that a ``raw_element``
    (e.g. an exponent for :class:`MonomialGrowthElement` or a base for
    :class:`ExponentialGrowthElement`) could be extracted.

    Its main purpose is to carry data used during the creation of
    elements of
    :mod:`cartesian products of growth groups <sage.rings.asymptotic.growth_group_cartesian>`.
    """
    growth_group: Incomplete
    raw_element: Incomplete
    def __init__(self, growth_group, raw_element) -> None:
        """
        See :class:`PartialConversionElement` for more information.

        TESTS::

            sage: from sage.rings.asymptotic.growth_group import PartialConversionElement, GrowthGroup
            sage: PartialConversionElement(GrowthGroup('(QQ_+)^n'), -2)
            element with parameter -2 (Integer Ring) in Growth Group QQ^n
        """
    def split(self):
        """
        Split the contained ``raw_element`` according to the growth group's
        :meth:`GrowthGroup._split_raw_element_`.

        EXAMPLES::

            sage: from sage.rings.asymptotic.growth_group import ExponentialGrowthGroup, PartialConversionValueError
            sage: E = ExponentialGrowthGroup(ZZ, 'x')
            sage: try:
            ....:     E((-2)^x)
            ....: except PartialConversionValueError as e:
            ....:     e.element.split()
            (2^x, element with parameter -1 (<class 'int'>) in Growth Group ZZ^x)

        TESTS::

            sage: try:
            ....:     E((2/3)^x)
            ....: except PartialConversionValueError as e:
            ....:     e.element.split()
            Traceback (most recent call last):
            ...
            ValueError: cannot split element with parameter 2/3 (Symbolic Ring) in Growth Group ZZ^x
            > *previous* PartialConversionValueError: 2/3 (Rational Field) is not in Integer Ring
            >> *previous* TypeError: no conversion of this rational to integer
        """
    def is_compatible(self, other):
        """
        Wrapper to :meth:`GenericGrowthGroup.is_compatible`.

        TESTS::

            sage: from sage.rings.asymptotic.growth_group import ExponentialGrowthGroup, ExponentialNonGrowthGroup, PartialConversionElement
            sage: from sage.groups.misc_gps.argument_groups import RootsOfUnityGroup
            sage: Q = ExponentialGrowthGroup(QQ, 'n')
            sage: UU = ExponentialNonGrowthGroup(RootsOfUnityGroup(), 'n')
            sage: PartialConversionElement(Q, -42/5).is_compatible(UU)
            True
        """

class GenericGrowthElement(MultiplicativeGroupElement):
    """
    A basic implementation of a generic growth element.

    Growth elements form a group by multiplication, and (some of) the
    elements can be compared to each other, i.e., all elements form a
    poset.

    INPUT:

    - ``parent`` -- a :class:`GenericGrowthGroup`

    - ``raw_element`` -- an element from the base of the parent

    EXAMPLES::

        sage: from sage.rings.asymptotic.growth_group import (GenericGrowthGroup,
        ....:                                                 GenericGrowthElement)
        sage: G = GenericGrowthGroup(ZZ)
        sage: g = GenericGrowthElement(G, 42); g
        GenericGrowthElement(42)
        sage: g.parent()
        Growth Group Generic(ZZ)
        sage: G(raw_element=42) == g
        True
    """
    def __init__(self, parent, raw_element) -> None:
        """
        See :class:`GenericGrowthElement` for more information.

        EXAMPLES::

            sage: from sage.rings.asymptotic.growth_group import GenericGrowthGroup
            sage: G = GenericGrowthGroup(ZZ)
            sage: G(raw_element=42)
            GenericGrowthElement(42)

        TESTS::

            sage: G(raw_element=42).category()
            Category of elements of Growth Group Generic(ZZ)

        ::

            sage: G = GenericGrowthGroup(ZZ)
            sage: G(raw_element=42).category()
            Category of elements of Growth Group Generic(ZZ)

        ::

            sage: from sage.rings.asymptotic.growth_group import GenericGrowthElement
            sage: GenericGrowthElement(None, 0)
            Traceback (most recent call last):
            ...
            ValueError: The parent must be provided
        """
    def __hash__(self):
        """
        Return the hash of this element.

        OUTPUT: integer

        EXAMPLES::

            sage: from sage.rings.asymptotic.growth_group import GenericGrowthGroup
            sage: G = GenericGrowthGroup(ZZ)
            sage: hash(G(raw_element=42))  # random
            5656565656565656
        """
    def __invert__(self) -> None:
        """
        Return the inverse of this growth element.

        OUTPUT: an instance of :class:`GenericGrowthElement`

        TESTS::

            sage: from sage.rings.asymptotic.growth_group import GrowthGroup
            sage: from sage.rings.asymptotic.growth_group import GenericGrowthGroup
            sage: G = GenericGrowthGroup(ZZ)
            sage: ~G.an_element()
            Traceback (most recent call last):
            ...
            NotImplementedError: Inversion of GenericGrowthElement(1) not implemented
            (in this abstract method).
            sage: G.an_element()^7
            Traceback (most recent call last):
            ...
            NotImplementedError: Only implemented in concrete realizations.
            sage: P = GrowthGroup('x^ZZ')
            sage: ~P.an_element()
            x^(-1)
        """
    log: Incomplete
    log_factor: Incomplete
    rpow: Incomplete
    def factors(self):
        """
        Return the atomic factors of this growth element. An atomic factor
        cannot be split further.

        OUTPUT: a tuple of growth elements

        EXAMPLES::

            sage: from sage.rings.asymptotic.growth_group import GrowthGroup
            sage: G = GrowthGroup('x^ZZ')
            sage: G.an_element().factors()
            (x,)
        """
    is_lt_one: Incomplete
    def variable_names(self):
        """
        Return the names of the variables of this growth element.

        OUTPUT: a tuple of strings

        EXAMPLES::

            sage: from sage.rings.asymptotic.growth_group import GrowthGroup
            sage: G = GrowthGroup('m^QQ')
            sage: G('m^2').variable_names()
            ('m',)
            sage: G('m^0').variable_names()
            ()

        ::

            sage: G = GrowthGroup('QQ^m')
            sage: G('2^m').variable_names()
            ('m',)
            sage: G('1^m').variable_names()
            ()

        TESTS::

            sage: from sage.rings.asymptotic.growth_group import GenericGrowthGroup
            sage: G = GenericGrowthGroup(QQ)
            sage: G(raw_element=2).variable_names()
            Traceback (most recent call last):
            ...
            AttributeError: 'GenericGrowthGroup_with_category.element_class' object
            has no attribute 'is_one'...
        """

class GenericGrowthGroup(UniqueRepresentation, Parent, WithLocals):
    """
    A basic implementation for growth groups.

    INPUT:

    - ``base`` -- one of SageMath's parents, out of which the elements
      get their data (``raw_element``)

    - ``category`` -- (default: ``None``) the category of the newly
      created growth group. It has to be a subcategory of ``Join of
      Category of groups and Category of posets``. This is also the
      default category if ``None`` is specified.

    - ``ignore_variables`` -- (default: ``None``) a tuple (or other
      iterable) of strings. The specified names are not considered as
      variables.

    .. NOTE::

        This class should be derived for concrete implementations.

    EXAMPLES::

        sage: from sage.rings.asymptotic.growth_group import GenericGrowthGroup
        sage: G = GenericGrowthGroup(ZZ); G
        Growth Group Generic(ZZ)

    .. SEEALSO::

        :class:`MonomialGrowthGroup`,
        :class:`ExponentialGrowthGroup`
    """
    Element = GenericGrowthElement
    @staticmethod
    def __classcall__(cls, base, var=None, category=None, ignore_variables=None):
        """
        Normalize the input in order to ensure a unique
        representation.

        For more information see :class:`GenericGrowthGroup`.

        TESTS::

            sage: from sage.rings.asymptotic.growth_group import MonomialGrowthGroup
            sage: P1 = MonomialGrowthGroup(ZZ, 'x')
            sage: P2 = MonomialGrowthGroup(ZZ, ZZ['x'].gen())
            sage: P3 = MonomialGrowthGroup(ZZ, SR.var('x'))
            sage: P1 is P2 and P2 is P3
            True
            sage: P5 = MonomialGrowthGroup(ZZ, 'x ')
            sage: P1 is P5
            True

        ::

            sage: L1 = MonomialGrowthGroup(QQ, log(x))
            sage: L2 = MonomialGrowthGroup(QQ, 'log(x)')
            sage: L1 is L2
            True

        Test determining of the category (:class:`GenericGrowthGroup`)::

            sage: from sage.rings.asymptotic.growth_group import GenericGrowthGroup
            sage: GenericGrowthGroup(ZZ, 'x').category()  # indirect doctest
            Category of posets
            sage: GenericGrowthGroup(ZZ, 'x', category=Groups()).category()  # indirect doctest
            Category of groups

        Test determining of the category (:class:`MonomialGrowthGroup`)::

            sage: from sage.rings.asymptotic.growth_group import MonomialGrowthGroup
            sage: MonomialGrowthGroup(ZZ, 'x').category()  # indirect doctest
            Join of Category of commutative groups and Category of posets
            sage: MonomialGrowthGroup(ZZ, 'x', category=Monoids()).category()  # indirect doctest
            Category of monoids
            sage: W = Words([0, 1])
            sage: W.category()
            Category of sets
            sage: MonomialGrowthGroup(W, 'x').category()  # indirect doctest
            Category of sets

        Test determining of the category (:class:`ExponentialGrowthGroup`)::

            sage: from sage.rings.asymptotic.growth_group import ExponentialGrowthGroup
            sage: ExponentialGrowthGroup(ZZ, 'x').category()  # indirect doctest
            Join of Category of commutative monoids and Category of posets
            sage: ExponentialGrowthGroup(QQ, 'x').category()  # indirect doctest
            Join of Category of commutative groups and Category of posets
            sage: ExponentialGrowthGroup(ZZ, 'x', category=Groups()).category()  # indirect doctest
            Category of groups
            sage: ExponentialGrowthGroup(QQ, 'x', category=Monoids()).category()  # indirect doctest
            Category of monoids

        ::

            sage: MonomialGrowthGroup(AsymptoticRing('z^ZZ', QQ), 'x')
            Traceback (most recent call last):
            ...
            TypeError: Asymptotic Ring <z^ZZ> over Rational Field is not a valid base.
        """
    def __init__(self, base, var, category) -> None:
        """
        See :class:`GenericGrowthGroup` for more information.

        EXAMPLES::

            sage: from sage.rings.asymptotic.growth_group import GenericGrowthGroup
            sage: GenericGrowthGroup(ZZ).category()
            Category of posets

        ::

            sage: from sage.rings.asymptotic.growth_group import MonomialGrowthGroup
            sage: MonomialGrowthGroup(ZZ, 'x')
            Growth Group x^ZZ
            sage: MonomialGrowthGroup(QQ, SR.var('n'))
            Growth Group n^QQ
            sage: MonomialGrowthGroup(ZZ, ZZ['y'].gen())
            Growth Group y^ZZ
            sage: MonomialGrowthGroup(QQ, 'log(x)')
            Growth Group log(x)^QQ

        ::

            sage: from sage.rings.asymptotic.growth_group import ExponentialGrowthGroup
            sage: ExponentialGrowthGroup(QQ, 'x')
            Growth Group QQ^x
            sage: assume(SR.an_element() > 0)
            sage: ExponentialGrowthGroup(SR, ZZ['y'].gen())
            Growth Group SR^y
            sage: forget()

        TESTS::

            sage: G = GenericGrowthGroup(ZZ)
            sage: G.is_parent_of(G(raw_element=42))
            True
            sage: G2 = GenericGrowthGroup(ZZ, category=FiniteGroups() & Posets())
            sage: G2.category()
            Join of Category of finite groups and Category of finite posets

        ::

            sage: G = GenericGrowthGroup('42')
            Traceback (most recent call last):
            ...
            TypeError: 42 is not a valid base.

        ::

            sage: MonomialGrowthGroup('x', ZZ)
            Traceback (most recent call last):
            ...
            TypeError: x is not a valid base.
            sage: MonomialGrowthGroup('x', 'y')
            Traceback (most recent call last):
            ...
            TypeError: x is not a valid base.

        ::

            sage: ExponentialGrowthGroup('x', ZZ)
            Traceback (most recent call last):
            ...
            TypeError: x is not a valid base.
            sage: ExponentialGrowthGroup('x', 'y')
            Traceback (most recent call last):
            ...
            TypeError: x is not a valid base.
        """
    def __hash__(self):
        """
        Return the hash of this group.

        OUTPUT: integer

        EXAMPLES::

            sage: from sage.rings.asymptotic.growth_group import (GenericGrowthGroup,
            ....:                                                 GrowthGroup)
            sage: hash(GenericGrowthGroup(ZZ))  # random
            4242424242424242

        ::

            sage: P = GrowthGroup('x^ZZ')
            sage: hash(P)  # random
            -1234567890123456789

        ::

            sage: P = GrowthGroup('QQ^x')
            sage: hash(P)  # random
            -1234567890123456789
        """
    def some_elements(self):
        """
        Return some elements of this growth group.

        See :class:`TestSuite` for a typical use case.

        OUTPUT: an iterator

        EXAMPLES::

            sage: from sage.rings.asymptotic.growth_group import GrowthGroup
            sage: tuple(GrowthGroup('z^ZZ').some_elements())
            (1, z, z^(-1), z^2, z^(-2), z^3, z^(-3),
             z^4, z^(-4), z^5, z^(-5), ...)
            sage: tuple(GrowthGroup('z^QQ').some_elements())
            (z^(1/2), z^(-1/2), z^2, z^(-2),
             1, z, z^(-1), z^42,
             z^(2/3), z^(-2/3), z^(3/2), z^(-3/2),
             z^(4/5), z^(-4/5), z^(5/4), z^(-5/4), ...)
        """
    def le(self, left, right):
        """
        Return whether the growth of ``left`` is at most (less than or
        equal to) the growth of ``right``.

        INPUT:

        - ``left`` -- an element

        - ``right`` -- an element

        OUTPUT: boolean

        .. NOTE::

            This function uses the coercion model to find a common
            parent for the two operands.

        EXAMPLES::

            sage: from sage.rings.asymptotic.growth_group import GrowthGroup
            sage: G = GrowthGroup('x^ZZ')
            sage: x = G.gen()
            sage: G.le(x, x^2)
            True
            sage: G.le(x^2, x)
            False
            sage: G.le(x^0, 1)
            True
        """
    def is_compatible(self, other):
        """
        Return whether this growth group is compatible with ``other`` meaning
        that both are of the same type and have the same variables, but
        maybe a different base.

        INPUT:

        - ``other`` -- a growth group

        EXAMPLES::

            sage: from sage.rings.asymptotic.growth_group import ExponentialGrowthGroup, ExponentialNonGrowthGroup
            sage: from sage.groups.misc_gps.argument_groups import RootsOfUnityGroup
            sage: EQ = ExponentialGrowthGroup(QQ, 'n')
            sage: EZ = ExponentialGrowthGroup(ZZ, 'n')
            sage: UU = ExponentialNonGrowthGroup(RootsOfUnityGroup(), 'n')
            sage: for a in (EQ, EZ, UU):
            ....:     for b in (EQ, EZ, UU):
            ....:         print('{} is {}compatible with {}'.format(
            ....:             a, '' if a.is_compatible(b) else 'not ', b))
            Growth Group QQ^n is compatible with Growth Group QQ^n
            Growth Group QQ^n is compatible with Growth Group ZZ^n
            Growth Group QQ^n is compatible with Growth Group UU^n
            Growth Group ZZ^n is compatible with Growth Group QQ^n
            Growth Group ZZ^n is compatible with Growth Group ZZ^n
            Growth Group ZZ^n is compatible with Growth Group UU^n
            Growth Group UU^n is not compatible with Growth Group QQ^n
            Growth Group UU^n is not compatible with Growth Group ZZ^n
            Growth Group UU^n is compatible with Growth Group UU^n
        """
    def gens_monomial(self) -> tuple:
        """
        Return a tuple containing monomial generators of this growth
        group.

        OUTPUT: an empty tuple

        .. NOTE::

            A generator is called monomial generator if the variable
            of the underlying growth group is a valid identifier. For
            example, ``x^ZZ`` has ``x`` as a monomial generator,
            while ``log(x)^ZZ`` or ``icecream(x)^ZZ`` do not have
            monomial generators.

        TESTS::

            sage: from sage.rings.asymptotic.growth_group import GenericGrowthGroup
            sage: GenericGrowthGroup(ZZ).gens_monomial()
            ()

        ::

            sage: from sage.rings.asymptotic.growth_group import GrowthGroup
            sage: GrowthGroup('x^QQ').gens_monomial()
            (x,)
            sage: GrowthGroup('QQ^x').gens_monomial()
            ()
        """
    def gens(self) -> tuple:
        """
        Return a tuple of all generators of this growth group.

        OUTPUT: a tuple whose entries are growth elements

        EXAMPLES::

            sage: from sage.rings.asymptotic.growth_group import GrowthGroup
            sage: P = GrowthGroup('x^ZZ')
            sage: P.gens()
            (x,)
            sage: GrowthGroup('log(x)^ZZ').gens()
            (log(x),)
        """
    def gen(self, n: int = 0):
        """
        Return the `n`-th generator (as a group) of this growth group.

        INPUT:

        - ``n`` -- (default: `0`)

        OUTPUT: a :class:`MonomialGrowthElement`

        EXAMPLES::

            sage: from sage.rings.asymptotic.growth_group import GrowthGroup
            sage: P = GrowthGroup('x^ZZ')
            sage: P.gen()
            x

        ::

            sage: P = GrowthGroup('(QQ_+)^x')
            sage: P.gen()
            Traceback (most recent call last):
            ...
            IndexError: tuple index out of range
        """
    def ngens(self):
        """
        Return the number of generators (as a group) of this growth group.

        OUTPUT: a Python integer

        EXAMPLES::

            sage: from sage.rings.asymptotic.growth_group import GrowthGroup
            sage: P = GrowthGroup('x^ZZ')
            sage: P.ngens()
            1
            sage: GrowthGroup('log(x)^ZZ').ngens()
            1

        ::

            sage: P = GrowthGroup('(QQ_+)^x')
            sage: P.ngens()
            0
        """
    def variable_names(self):
        """
        Return the names of the variables of this growth group.

        OUTPUT: a tuple of strings

        EXAMPLES::

            sage: from sage.rings.asymptotic.growth_group import GenericGrowthGroup
            sage: GenericGrowthGroup(ZZ).variable_names()
            ()

        ::

            sage: from sage.rings.asymptotic.growth_group import GrowthGroup
            sage: GrowthGroup('x^ZZ').variable_names()
            ('x',)
            sage: GrowthGroup('log(x)^ZZ').variable_names()
            ('x',)

        ::

            sage: GrowthGroup('(QQ_+)^x').variable_names()
            ('x',)
            sage: GrowthGroup('(QQ_+)^(x*log(x))').variable_names()
            ('x',)
        """
    CartesianProduct = CartesianProductGrowthGroups
    def extended_by_non_growth_group(self):
        """
        Extend to a cartesian product of this growth group
        and a suitable non growth group.

        OUTPUT: a group group

        EXAMPLES::

            sage: from sage.rings.asymptotic.growth_group import GrowthGroup
            sage: GrowthGroup('(QQ_+)^x').extended_by_non_growth_group()
            Growth Group QQ^x * Signs^x
            sage: GrowthGroup('(RR_+)^x').extended_by_non_growth_group()
            Growth Group RR^x * Signs^x
            sage: GrowthGroup('(RIF_+)^x').extended_by_non_growth_group()
            Growth Group RIF^x * Signs^x
            sage: GrowthGroup('(RBF_+)^x').extended_by_non_growth_group()
            Growth Group RBF^x * Signs^x
            sage: GrowthGroup('(CC_+)^x').extended_by_non_growth_group()
            Growth Group CC^x * UU_RR^x
            sage: GrowthGroup('(CIF_+)^x').extended_by_non_growth_group()
            Growth Group CIF^x * UU_RIF^x
            sage: GrowthGroup('(CBF_+)^x').extended_by_non_growth_group()
            Growth Group CBF^x * UU_RBF^x
        """
    def non_growth_group(self) -> None:
        """
        Return a non-growth group compatible with this growth group.

        OUTPUT: a group group

        EXAMPLES::

            sage: from sage.rings.asymptotic.growth_group import GenericGrowthGroup
            sage: GenericGrowthGroup(ZZ, 'n').non_growth_group()
            Traceback (most recent call last):
            ...
            NotImplementedError: only implemented in concrete realizations
        """

class AbstractGrowthGroupFunctor(ConstructionFunctor):
    """
    A base class for the functors constructing growth groups.

    INPUT:

    - ``var`` -- string or list of strings (or anything else :class:`Variable`
      accepts)

    - ``domain`` -- a category

    EXAMPLES::

        sage: from sage.rings.asymptotic.growth_group import GrowthGroup
        sage: GrowthGroup('z^QQ').construction()[0]  # indirect doctest
        MonomialGrowthGroup[z]

    .. SEEALSO::

        :doc:`asymptotic_ring`,
        :class:`ExponentialGrowthGroupFunctor`,
        :class:`MonomialGrowthGroupFunctor`,
        :class:`sage.rings.asymptotic.asymptotic_ring.AsymptoticRingFunctor`,
        :class:`sage.categories.pushout.ConstructionFunctor`.
    """
    rank: int
    var: Incomplete
    def __init__(self, var, domain) -> None:
        """
        See :class:`AbstractGrowthGroupFunctor` for details.

        TESTS::

            sage: from sage.rings.asymptotic.growth_group import AbstractGrowthGroupFunctor
            sage: AbstractGrowthGroupFunctor('x', Groups())
            AbstractGrowthGroup[x]
        """
    def merge(self, other):
        """
        Merge this functor with ``other`` of possible.

        INPUT:

        - ``other`` -- a functor

        OUTPUT: a functor or ``None``

        EXAMPLES::

            sage: from sage.rings.asymptotic.growth_group import GrowthGroup
            sage: F = GrowthGroup('(QQ_+)^t').construction()[0]
            sage: G = GrowthGroup('t^QQ').construction()[0]
            sage: F.merge(F)
            ExponentialGrowthGroup[t]
            sage: F.merge(G) is None
            True
        """
    def __eq__(self, other):
        """
        Return whether this functor is equal to ``other``.

        INPUT:

        - ``other`` -- a functor

        OUTPUT: boolean

        EXAMPLES::

            sage: from sage.rings.asymptotic.growth_group import GrowthGroup
            sage: F = GrowthGroup('QQ^t').construction()[0]
            sage: G = GrowthGroup('t^QQ').construction()[0]
            sage: F == F
            True
            sage: F == G
            False
        """
    def __ne__(self, other):
        """
        Return whether this functor is not equal to ``other``.

        INPUT:

        - ``other`` -- a functor

        OUTPUT: boolean

        EXAMPLES::

            sage: from sage.rings.asymptotic.growth_group import GrowthGroup
            sage: F = GrowthGroup('QQ^t').construction()[0]
            sage: G = GrowthGroup('t^QQ').construction()[0]
            sage: F != F
            False
            sage: F != G
            True
        """

class DecreasingGrowthElementError(ValueError):
    """
    A special :python:`ValueError<library/exceptions.html#exceptions.ValueError>`
    which is raised when a growth element is less than one.

    INPUT:

    - ``element`` -- a :class:`GenericGrowthElement`

    The remaining arguments are passed on to
    :python:`ValueError<library/exceptions.html#exceptions.ValueError>`.
    """
    element: Incomplete
    def __init__(self, element, *args, **kwds) -> None:
        """
        See :exc:`DecreasingGrowthElementError` for more information.

        TESTS::

            sage: from sage.rings.asymptotic.growth_group import DecreasingGrowthElementError, GenericGrowthElement, MonomialGrowthGroup
            sage: raise DecreasingGrowthElementError(
            ....:     GenericGrowthElement(MonomialGrowthGroup(QQ, 'x'), 1/2), 'wrong value')
            Traceback (most recent call last):
            ...
            DecreasingGrowthElementError: wrong value
        """

class MonomialGrowthElement(GenericGrowthElement):
    """
    An implementation of monomial growth elements.

    INPUT:

    - ``parent`` -- a :class:`MonomialGrowthGroup`

    - ``raw_element`` -- an element from the base ring of the parent

      This ``raw_element`` is the exponent of the created monomial
      growth element.

    A monomial growth element represents a term of the type
    `\\operatorname{variable}^{\\operatorname{exponent}}`. The multiplication
    corresponds to the addition of the exponents.

    EXAMPLES::

        sage: from sage.rings.asymptotic.growth_group import MonomialGrowthGroup
        sage: P = MonomialGrowthGroup(ZZ, 'x')
        sage: e1 = P(1); e1
        1
        sage: e2 = P(raw_element=2); e2
        x^2
        sage: e1 == e2
        False
        sage: P.le(e1, e2)
        True
        sage: P.le(e1, P.gen()) and P.le(P.gen(), e2)
        True
    """
    @property
    def exponent(self):
        """
        The exponent of this growth element.

        EXAMPLES::

            sage: from sage.rings.asymptotic.growth_group import GrowthGroup
            sage: P = GrowthGroup('x^ZZ')
            sage: P(x^42).exponent
            42
        """
    def __invert__(self):
        """
        Return the multiplicative inverse of this monomial growth element.

        OUTPUT: the multiplicative inverse as a :class:`MonomialGrowthElement`

        EXAMPLES::

            sage: from sage.rings.asymptotic.growth_group import GrowthGroup
            sage: P = GrowthGroup('x^ZZ')
            sage: e1 = P(raw_element=2)
            sage: e2 = e1.__invert__(); e2
            x^(-2)
            sage: e2 == ~e1
            True
            sage: Q = GrowthGroup('x^NN'); Q
            Growth Group x^(Non negative integer semiring)
            sage: e3 = ~Q('x'); e3
            x^(-1)
            sage: e3.parent()
            Growth Group x^ZZ
        """
    def __pow__(self, exponent):
        """
        Calculate the power of this growth element to the given ``exponent``.

        INPUT:

        - ``exponent`` -- a number. This can be anything that is a
          valid right hand side of ``*`` with elements of the
          parent's base.

        OUTPUT: the result of this exponentiation, a :class:`MonomialGrowthElement`

        EXAMPLES::

            sage: from sage.rings.asymptotic.growth_group import GrowthGroup
            sage: P = GrowthGroup('x^ZZ')
            sage: x = P.gen()
            sage: a = x^7; a
            x^7
            sage: a^(1/2)
            x^(7/2)
            sage: (a^(1/2)).parent()
            Growth Group x^QQ
            sage: a^(1/7)
            x
            sage: (a^(1/7)).parent()
            Growth Group x^QQ
            sage: P = GrowthGroup('x^QQ')
            sage: b = P.gen()^(7/2); b
            x^(7/2)
            sage: b^12
            x^42
        """

class MonomialGrowthGroup(GenericGrowthGroup):
    """
    A growth group dealing with powers of a fixed object/symbol.

    The elements :class:`MonomialGrowthElement` of this group represent powers
    of a fixed base; the group law is the multiplication, which corresponds
    to the addition of the exponents of the monomials.

    INPUT:

    - ``base`` -- one of SageMath's parents, out of which the elements
      get their data (``raw_element``)

      As monomials are represented by this group, the elements in
      ``base`` are the exponents of these monomials.

    - ``var`` -- an object

      The string representation of ``var`` acts as a base of the
      monomials represented by this group.

    - ``category`` -- (default: ``None``) the category of the newly
      created growth group. It has to be a subcategory of ``Join of
      Category of groups and Category of posets``. This is also the
      default category if ``None`` is specified.

    EXAMPLES::

        sage: from sage.rings.asymptotic.growth_group import MonomialGrowthGroup
        sage: P = MonomialGrowthGroup(ZZ, 'x'); P
        Growth Group x^ZZ
        sage: MonomialGrowthGroup(ZZ, log(SR.var('y')))
        Growth Group log(y)^ZZ

    .. SEEALSO::

        :class:`GenericGrowthGroup`

    TESTS::

        sage: L1 = MonomialGrowthGroup(QQ, log(x))
        sage: L2 = MonomialGrowthGroup(QQ, 'log(x)')
        sage: L1 is L2
        True
    """
    Element = MonomialGrowthElement
    def gens_monomial(self) -> tuple:
        """
        Return a tuple containing monomial generators of this growth
        group.

        OUTPUT: a tuple containing elements of this growth group

        .. NOTE::

            A generator is called monomial generator if the variable
            of the underlying growth group is a valid identifier. For
            example, ``x^ZZ`` has ``x`` as a monomial generator,
            while ``log(x)^ZZ`` or ``icecream(x)^ZZ`` do not have
            monomial generators.

        TESTS::

            sage: from sage.rings.asymptotic.growth_group import GrowthGroup
            sage: GrowthGroup('x^ZZ').gens_monomial()
            (x,)
            sage: GrowthGroup('log(x)^QQ').gens_monomial()
            ()
        """
    def gens_logarithmic(self) -> tuple:
        """
        Return a tuple containing logarithmic generators of this growth
        group.

        OUTPUT: a tuple containing elements of this growth group

        .. NOTE::

            A generator is called logarithmic generator if the variable
            of the underlying growth group is the logarithm of a valid
            identifier. For
            example, ``x^ZZ`` has no logarithmic generator,
            while ``log(x)^ZZ`` has ``log(x)`` as
            logarithmic generator.

        TESTS::

            sage: from sage.rings.asymptotic.growth_group import GrowthGroup
            sage: GrowthGroup('x^ZZ').gens_logarithmic()
            ()
            sage: GrowthGroup('log(x)^QQ').gens_logarithmic()
            (log(x),)
        """
    def construction(self):
        """
        Return the construction of this growth group.

        OUTPUT:

        A pair whose first entry is a
        :class:`monomial construction functor <MonomialGrowthGroupFunctor>`
        and its second entry the base.

        EXAMPLES::

            sage: from sage.rings.asymptotic.growth_group import GrowthGroup
            sage: GrowthGroup('x^ZZ').construction()
            (MonomialGrowthGroup[x], Integer Ring)
        """
    @classmethod
    def factory(cls, base, var, extend_by_non_growth_group: bool = False, return_factors: bool = False, **kwds):
        """
        Create a monomial growth group.

        INPUT:

        - ``base``, ``var``, keywords -- use in the initialization of the
          exponential growth group; see :class:`MonomialGrowthGroup`
          for details.

        - ``extend_by_non_growth_group`` -- boolean (default: ``False``); if
          set, then the growth group consists of two parts, one part dealing
          with the absolute values of the bases and one for their arguments.

        - ``return_factors`` -- boolean (default: ``False``); if set,
          then a tuple of the (cartesian) factors of this growth group
          is returned

        OUTPUT: a growth group or tuple of growth groups

        EXAMPLES::

            sage: from sage.rings.asymptotic.growth_group import MonomialGrowthGroup
            sage: from sage.groups.misc_gps.imaginary_groups import ImaginaryGroup
            sage: MonomialGrowthGroup.factory(ZZ, 'n')
            Growth Group n^ZZ
            sage: MonomialGrowthGroup.factory(ImaginaryGroup(ZZ), 'n')
            Growth Group n^(ZZ*I)

        TESTS::

            sage: MonomialGrowthGroup.factory(ZZ, 'n', return_factors=True)
            (Growth Group n^ZZ,)
            sage: MonomialGrowthGroup.factory(ZZ, 'n', extend_by_non_growth_group=True)
            Growth Group n^ZZ * n^(ZZ*I)
            sage: MonomialGrowthGroup.factory(ZZ, 'n', return_factors=True,
            ....:                             extend_by_non_growth_group=True)
            (Growth Group n^ZZ, Growth Group n^(ZZ*I))
        """
    def non_growth_group(self):
        """
        Return a non-growth group
        (with an imaginary group as base)
        compatible with this monomial growth group.

        OUTPUT: a group group

        EXAMPLES::

            sage: from sage.rings.asymptotic.growth_group import GrowthGroup
            sage: GrowthGroup('n^ZZ').non_growth_group()
            Growth Group n^(ZZ*I)
        """

class MonomialGrowthGroupFunctor(AbstractGrowthGroupFunctor):
    """
    A :class:`construction functor <sage.categories.pushout.ConstructionFunctor>`
    for :class:`monomial growth groups <MonomialGrowthGroup>`.

    INPUT:

    - ``var`` -- string or list of strings (or anything else
      :class:`Variable` accepts)

    EXAMPLES::

        sage: from sage.rings.asymptotic.growth_group import GrowthGroup, MonomialGrowthGroupFunctor
        sage: GrowthGroup('z^QQ').construction()[0]
        MonomialGrowthGroup[z]

    .. SEEALSO::

        :doc:`asymptotic_ring`,
        :class:`AbstractGrowthGroupFunctor`,
        :class:`ExponentialGrowthGroupFunctor`,
        :class:`sage.rings.asymptotic.asymptotic_ring.AsymptoticRingFunctor`,
        :class:`sage.categories.pushout.ConstructionFunctor`.

    TESTS::

        sage: from sage.rings.asymptotic.growth_group import GrowthGroup, MonomialGrowthGroupFunctor
        sage: cm = sage.structure.element.get_coercion_model()
        sage: A = GrowthGroup('x^QQ')
        sage: B = MonomialGrowthGroupFunctor('x')(ZZ['t'])
        sage: cm.common_parent(A, B)
        Growth Group x^QQ[t]
    """
    def __init__(self, var) -> None:
        """
        See :class:`MonomialGrowthGroupFunctor` for details.

        TESTS::

            sage: from sage.rings.asymptotic.growth_group import MonomialGrowthGroupFunctor
            sage: MonomialGrowthGroupFunctor('x')
            MonomialGrowthGroup[x]
        """

class ExponentialGrowthElement(GenericGrowthElement):
    """
    An implementation of exponential growth elements.

    INPUT:

    - ``parent`` -- an :class:`ExponentialGrowthGroup`

    - ``raw_element`` -- an element from the base ring of the parent

      This ``raw_element`` is the base of the created exponential
      growth element.

    An exponential growth element represents a term of the type
    `\\operatorname{base}^{\\operatorname{variable}}`. The multiplication
    corresponds to the multiplication of the bases.

    EXAMPLES::

        sage: from sage.rings.asymptotic.growth_group import GrowthGroup
        sage: P = GrowthGroup('(ZZ_+)^x')
        sage: e1 = P(1); e1
        1
        sage: e2 = P(raw_element=2); e2
        2^x
        sage: e1 == e2
        False
        sage: P.le(e1, e2)
        True
        sage: P.le(e1, P(1)) and P.le(P(1), e2)
        True
    """
    @property
    def base(self):
        """
        The base of this exponential growth element.

        EXAMPLES::

            sage: from sage.rings.asymptotic.growth_group import GrowthGroup
            sage: P = GrowthGroup('(ZZ_+)^x')
            sage: P(42^x).base
            42
        """
    def __invert__(self):
        """
        Return the multiplicative inverse of this exponential growth element.

        OUTPUT: the multiplicative inverse as a :class:`ExponentialGrowthElement`

        EXAMPLES::

            sage: from sage.rings.asymptotic.growth_group import GrowthGroup
            sage: P = GrowthGroup('(ZZ_+)^x')
            sage: e1 = P(raw_element=2)
            sage: e2 = e1.__invert__(); e2
            (1/2)^x
            sage: e2 == ~e1
            True
            sage: e2.parent()
            Growth Group QQ^x

        ::

            sage: (~P(raw_element=1)).parent()
            Growth Group QQ^x

        ::

            sage: UU = GrowthGroup('UU^n')
            sage: zeta = UU.an_element(); zeta
            (-1)^n
            sage: ~zeta
            (-1)^n
        """
    def __pow__(self, exponent):
        """
        Calculate the power of this growth element to the given ``exponent``.

        INPUT:

        - ``exponent`` -- a number. This can be anything that is valid to be
          on the right hand side of ``*`` with an elements of the
          parent's base.

        OUTPUT: the result of this exponentiation as an :class:`ExponentialGrowthElement`

        EXAMPLES::

            sage: from sage.rings.asymptotic.growth_group import GrowthGroup
            sage: P = GrowthGroup('(ZZ_+)^x')
            sage: assume(SR.an_element() > 0)
            sage: a = P(7^x); a
            7^x
            sage: b = a^(1/2); b
            sqrt(7)^x
            sage: b.parent()
            Growth Group SR^x
            sage: b^12
            117649^x
            sage: forget()

        TESTS::

             sage: SCR = SR.subring(no_variables=True)
             sage: G = GrowthGroup('QQ^x * x^ZZ'); G
             Growth Group QQ^x * x^ZZ * Signs^x
             sage: x = G('x')
             sage: x^SCR(1)
             x
             sage: _.parent()
             Growth Group QQ^x * x^ZZ * Signs^x
        """

class ExponentialGrowthGroup(GenericGrowthGroup):
    """
    A growth group dealing with expressions involving a fixed
    variable/symbol as the exponent.

    The elements :class:`ExponentialGrowthElement` of this group
    represent exponential functions with bases from a fixed base
    ring; the group law is the multiplication.

    INPUT:

    - ``base`` -- one of SageMath's parents, out of which the elements
      get their data (``raw_element``)

      As exponential expressions are represented by this group,
      the elements in ``base`` are the bases of these exponentials.

    - ``var`` -- an object

      The string representation of ``var`` acts as an exponent of the
      elements represented by this group.

    - ``category`` -- (default: ``None``) the category of the newly
      created growth group. It has to be a subcategory of ``Join of
      Category of groups and Category of posets``. This is also the
      default category if ``None`` is specified.

    EXAMPLES::

        sage: from sage.rings.asymptotic.growth_group import ExponentialGrowthGroup
        sage: P = ExponentialGrowthGroup(QQ, 'x'); P
        Growth Group QQ^x

    .. SEEALSO::

        :class:`GenericGrowthGroup`
    """
    Element = ExponentialGrowthElement
    def __init__(self, base, *args, **kwds) -> None:
        """
        See :class:`ExponentialGrowthGroup` for more information.

        TESTS::

            sage: from sage.rings.asymptotic.growth_group import ExponentialGrowthGroup
            sage: ExponentialGrowthGroup(SR.subring(no_variables=True), 't')  # indirect doctest
            Growth Group (Symbolic Constants Subring)^t
            sage: ExponentialGrowthGroup(SR, 't')  # indirect doctest
            doctest:warning
            ...
            RuntimeWarning: When using the Exponential Growth Group SR^t,
            make assumptions on the used symbolic elements.
            In particular, use something like 'assume(SR.an_element() > 0)'
            to make coercions work properly.
            Growth Group SR^t
            sage: assume(SR.an_element() > 0)
            sage: ExponentialGrowthGroup(SR, 't')  # indirect doctest
            Growth Group SR^t
            sage: forget()
        """
    def some_elements(self):
        """
        Return some elements of this exponential growth group.

        See :class:`TestSuite` for a typical use case.

        OUTPUT: an iterator

        EXAMPLES::

            sage: from sage.rings.asymptotic.growth_group import GrowthGroup
            sage: tuple(GrowthGroup('(QQ_+)^z').some_elements())
            ((1/2)^z, 2^z, 1, 42^z, (2/3)^z, (3/2)^z, ...)
        """
    def gens(self) -> tuple:
        """
        Return a tuple of all generators of this exponential growth
        group.

        OUTPUT: an empty tuple

        EXAMPLES::

            sage: from sage.rings.asymptotic.growth_group import GrowthGroup
            sage: E = GrowthGroup('(ZZ_+)^x')
            sage: E.gens()
            ()
        """
    def construction(self):
        """
        Return the construction of this growth group.

        OUTPUT:

        A pair whose first entry is an
        :class:`exponential construction functor <ExponentialGrowthGroupFunctor>`
        and its second entry the base.

        EXAMPLES::

            sage: from sage.rings.asymptotic.growth_group import GrowthGroup
            sage: GrowthGroup('(QQ_+)^x').construction()
            (ExponentialGrowthGroup[x], Rational Field)
        """
    @classmethod
    def factory(cls, base, var, extend_by_non_growth_group: bool = True, return_factors: bool = False, **kwds):
        """
        Create an exponential growth group.

        This factory takes care of the splitting of the bases into their
        absolute values and arguments.

        INPUT:

        - ``base``, ``var``, keywords -- use in the initialization of the
          exponential growth group; see :class:`ExponentialGrowthGroup`
          for details.

        - ``extend_by_non_growth_group`` -- boolean (default: ``True``); if
          set, then the growth group consists of two parts, one part dealing
          with the absolute values of the bases and one for their arguments.

        - ``return_factors`` -- boolean (default: ``False``); if set,
          then a tuple of the (cartesian) factors of this growth group
          is returned

        OUTPUT: a growth group or tuple of growth groups

        EXAMPLES::

            sage: from sage.rings.asymptotic.growth_group import ExponentialGrowthGroup
            sage: ExponentialGrowthGroup.factory(QQ, 'n')
            Growth Group QQ^n * Signs^n

        TESTS::

            sage: ExponentialGrowthGroup.factory(QQ, 'n', return_factors=True)
            (Growth Group QQ^n, Growth Group Signs^n)
            sage: ExponentialGrowthGroup.factory(QQ, 'n', extend_by_non_growth_group=False)
            Growth Group QQ^n
            sage: from sage.groups.misc_gps.argument_groups import ArgumentGroup
            sage: UU = ArgumentGroup(exponents=QQ)
            sage: ExponentialGrowthGroup.factory(UU, 'n')
            Growth Group UU^n

            sage: ExponentialGrowthGroup.factory(CC, 'n')
            Growth Group RR^n * UU_RR^n
            sage: ExponentialGrowthGroup.factory(CyclotomicField(3), 'n')
            Growth Group (Algebraic Real Field)^n * (Arg_(Cyclotomic Field of order 3 and degree 2))^n
        """
    def non_growth_group(self):
        """
        Return a non-growth group
        (with an argument group, e.g. roots of unity, as base)
        compatible with this exponential growth group.

        OUTPUT: a group group

        EXAMPLES::

            sage: from sage.rings.asymptotic.growth_group import GrowthGroup
            sage: GrowthGroup('(QQ_+)^x').non_growth_group()
            Growth Group Signs^x
            sage: GrowthGroup('(RR_+)^x').non_growth_group()
            Growth Group Signs^x
            sage: GrowthGroup('(RIF_+)^x').non_growth_group()
            Growth Group Signs^x
            sage: GrowthGroup('(RBF_+)^x').non_growth_group()
            Growth Group Signs^x
            sage: GrowthGroup('(CC_+)^x').non_growth_group()
            Growth Group UU_RR^x
            sage: GrowthGroup('(CIF_+)^x').non_growth_group()
            Growth Group UU_RIF^x
            sage: GrowthGroup('(CBF_+)^x').non_growth_group()
            Growth Group UU_RBF^x
        """

class ExponentialGrowthGroupFunctor(AbstractGrowthGroupFunctor):
    """
    A :class:`construction functor <sage.categories.pushout.ConstructionFunctor>`
    for :class:`exponential growth groups <ExponentialGrowthGroup>`.

    INPUT:

    - ``var`` -- string or list of strings (or anything else
      :class:`Variable` accepts)

    EXAMPLES::

        sage: from sage.rings.asymptotic.growth_group import GrowthGroup, ExponentialGrowthGroupFunctor
        sage: GrowthGroup('(QQ_+)^z').construction()[0]
        ExponentialGrowthGroup[z]

    .. SEEALSO::

        :doc:`asymptotic_ring`,
        :class:`AbstractGrowthGroupFunctor`,
        :class:`MonomialGrowthGroupFunctor`,
        :class:`sage.rings.asymptotic.asymptotic_ring.AsymptoticRingFunctor`,
        :class:`sage.categories.pushout.ConstructionFunctor`.

    TESTS::

        sage: from sage.rings.asymptotic.growth_group import GrowthGroup, ExponentialGrowthGroupFunctor
        sage: cm = sage.structure.element.get_coercion_model()
        sage: A = GrowthGroup('(QQ_+)^x')
        sage: B = ExponentialGrowthGroupFunctor('x')(ZZ['t'])
        sage: cm.common_parent(A, B)
        Growth Group QQ[t]^x
    """
    def __init__(self, var) -> None:
        """
        See :class:`ExponentialGrowthGroupFunctor` for details.

        TESTS::

            sage: from sage.rings.asymptotic.growth_group import ExponentialGrowthGroupFunctor
            sage: ExponentialGrowthGroupFunctor('x')
            ExponentialGrowthGroup[x]
        """

class GenericNonGrowthElement(GenericGrowthElement):
    """
    An element of :class:`GenericNonGrowthGroup`.
    """
class GenericNonGrowthGroup(GenericGrowthGroup):
    """
    A (abstract) growth group whose elements are all of the same growth `1`.

    See :class:`ExponentialNonGrowthGroup` for a concrete
    realization.
    """
class ExponentialNonGrowthElement(GenericNonGrowthElement, ExponentialGrowthElement):
    """
    An element of :class:`ExponentialNonGrowthGroup`.
    """

class ExponentialNonGrowthGroup(GenericNonGrowthGroup, ExponentialGrowthGroup):
    """
    A growth group whose base is an
    :mod:`argument group <sage.groups.misc_gps.argument_groups>`.

    EXAMPLES::

        sage: from sage.groups.misc_gps.argument_groups import RootsOfUnityGroup
        sage: from sage.rings.asymptotic.growth_group import ExponentialNonGrowthGroup
        sage: UU = ExponentialNonGrowthGroup(RootsOfUnityGroup(), 'n')
        sage: UU(raw_element=-1)
        (-1)^n

    TESTS::

        sage: UU(raw_element=int(-1))
        (-1)^n

    ::

        sage: UU.category()
        Join of Category of commutative groups and Category of posets
    """
    Element = ExponentialNonGrowthElement
    def construction(self):
        """
        Return the construction of this growth group.

        OUTPUT:

        A pair whose first entry is an
        :class:`ExponentialNonGrowthGroupFunctor`
        and its second entry the base.

        EXAMPLES::

            sage: from sage.rings.asymptotic.growth_group import GrowthGroup
            sage: GrowthGroup('UU^x').construction()
            (ExponentialNonGrowthGroup[x], Group of Roots of Unity)
        """

class ExponentialNonGrowthGroupFunctor(ExponentialGrowthGroupFunctor):
    """
    A :class:`construction functor <sage.categories.pushout.ConstructionFunctor>`
    for :class:`ExponentialNonGrowthGroup`.
    """
class MonomialNonGrowthElement(GenericNonGrowthElement, MonomialGrowthElement):
    """
    An element of :class:`MonomialNonGrowthGroup`.
    """

class MonomialNonGrowthGroup(GenericNonGrowthGroup, MonomialGrowthGroup):
    """
    A growth group whose base is an
    :mod:`imaginary group <sage.groups.misc_gps.imaginary_groups>`.

    EXAMPLES::

        sage: from sage.groups.misc_gps.imaginary_groups import ImaginaryGroup
        sage: from sage.rings.asymptotic.growth_group import MonomialNonGrowthGroup
        sage: J = MonomialNonGrowthGroup(ImaginaryGroup(ZZ), 'n')
        sage: J.an_element()
        n^I

    TESTS::

        sage: J.category()
        Join of Category of commutative groups and Category of posets
    """
    Element = MonomialNonGrowthElement
    def construction(self):
        """
        Return the construction of this growth group.

        OUTPUT:

        A pair whose first entry is an
        :class:`MonomialNonGrowthGroupFunctor`
        and its second entry the base.

        EXAMPLES::

            sage: from sage.rings.asymptotic.growth_group import GrowthGroup
            sage: GrowthGroup('x^(QQ*I)').construction()
            (MonomialNonGrowthGroup[x], Imaginary Group over Rational Field)
        """

class MonomialNonGrowthGroupFunctor(MonomialGrowthGroupFunctor):
    """
    A :class:`construction functor <sage.categories.pushout.ConstructionFunctor>`
    for :class:`MonomialNonGrowthGroup`.
    """

class GrowthGroupFactor(NamedTuple):
    cls: Incomplete
    base: Incomplete
    var: Incomplete
    extend_by_non_growth_group: Incomplete

class GrowthGroupFactory(UniqueFactory):
    """
    A factory creating asymptotic growth groups.

    INPUT:

    - ``specification`` -- string

    - keyword arguments are passed on to the growth group
      constructor.
      If the keyword ``ignore_variables`` is not specified, then
      ``ignore_variables=('e',)`` (to ignore ``e`` as a variable name)
      is used.

    OUTPUT: an asymptotic growth group

    .. NOTE::

        An instance of this factory is available as ``GrowthGroup``.

    EXAMPLES::

        sage: from sage.rings.asymptotic.growth_group import GrowthGroup
        sage: GrowthGroup('x^ZZ')
        Growth Group x^ZZ
        sage: GrowthGroup('log(x)^QQ')
        Growth Group log(x)^QQ

    This factory can also be used to construct Cartesian products
    of growth groups::

        sage: GrowthGroup('x^ZZ * y^ZZ')
        Growth Group x^ZZ * y^ZZ
        sage: GrowthGroup('x^ZZ * log(x)^ZZ')
        Growth Group x^ZZ * log(x)^ZZ
        sage: GrowthGroup('x^ZZ * log(x)^ZZ * y^QQ')
        Growth Group x^ZZ * log(x)^ZZ * y^QQ
        sage: GrowthGroup('(QQ_+)^x * x^ZZ * y^QQ * (QQ_+)^z')
        Growth Group QQ^x * x^ZZ * y^QQ * QQ^z
        sage: GrowthGroup('QQ^x * x^ZZ * y^QQ * QQ^z')
        Growth Group QQ^x * x^ZZ * Signs^x * y^QQ * QQ^z * Signs^z
        sage: GrowthGroup('exp(x)^ZZ * x^ZZ')
        Growth Group exp(x)^ZZ * x^ZZ
        sage: GrowthGroup('(e^x)^ZZ * x^ZZ')
        Growth Group (e^x)^ZZ * x^ZZ

    ::

        sage: GrowthGroup('QQ^n * n^ZZ')
        Growth Group QQ^n * n^ZZ * Signs^n
        sage: GrowthGroup('(QQ_+)^n * n^ZZ * UU^n')
        Growth Group QQ^n * n^ZZ * UU^n
        sage: GrowthGroup('(QQ_+)^n * n^ZZ')
        Growth Group QQ^n * n^ZZ

    ::

        sage: GrowthGroup('n^(ZZ)')
        Growth Group n^ZZ
        sage: GrowthGroup('n^(ZZ[I])')
        Growth Group n^ZZ * n^(ZZ*I)
        sage: GrowthGroup('n^(I*ZZ)')
        Growth Group n^(ZZ*I)
        sage: GrowthGroup('n^(ZZ*I)')
        Growth Group n^(ZZ*I)

    TESTS::

        sage: G = GrowthGroup('(e^(n*log(n)))^ZZ')
        sage: G, G._var_
        (Growth Group (e^(n*log(n)))^ZZ, e^(n*log(n)))
        sage: G = GrowthGroup('(e^n)^ZZ')
        sage: G, G._var_
        (Growth Group (e^n)^ZZ, e^n)
        sage: G = GrowthGroup('(e^(n*log(n)))^ZZ * (e^n)^ZZ * n^ZZ * log(n)^ZZ')
        sage: G, tuple(F._var_ for F in G.cartesian_factors())
        (Growth Group (e^(n*log(n)))^ZZ * (e^n)^ZZ * n^ZZ * log(n)^ZZ,
         (e^(n*log(n)), e^n, n, log(n)))

    ::

        sage: GrowthGroup('m^(ZZ[I]) * log(m)^(ZZ[I]) * n^(ZZ[I])')
        Growth Group m^ZZ * log(m)^ZZ * m^(ZZ*I) * log(m)^(ZZ*I) * n^ZZ * n^(ZZ*I)

    ::

        sage: TestSuite(GrowthGroup('x^ZZ')).run(verbose=True)  # long time
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
        running ._test_inverse() . . . pass
        running ._test_new() . . . pass
        running ._test_not_implemented_methods() . . . pass
        running ._test_one() . . . pass
        running ._test_pickling() . . . pass
        running ._test_prod() . . . pass
        running ._test_some_elements() . . . pass

    ::

        sage: TestSuite(GrowthGroup('(QQ_+)^y')).run(verbose=True)  # long time
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
        running ._test_inverse() . . . pass
        running ._test_new() . . . pass
        running ._test_not_implemented_methods() . . . pass
        running ._test_one() . . . pass
        running ._test_pickling() . . . pass
        running ._test_prod() . . . pass
        running ._test_some_elements() . . . pass

    ::

        sage: TestSuite(GrowthGroup('x^QQ * log(x)^ZZ')).run(verbose=True)  # long time
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
        running ._test_inverse() . . . pass
        running ._test_new() . . . pass
        running ._test_not_implemented_methods() . . . pass
        running ._test_one() . . . pass
        running ._test_pickling() . . . pass
        running ._test_prod() . . . pass
        running ._test_some_elements() . . . pass
    """
    def create_key_and_extra_args(self, specification, **kwds):
        """
        Given the arguments and keyword, create a key that uniquely
        determines this object.

        TESTS::

            sage: from sage.rings.asymptotic.growth_group import GrowthGroup
            sage: GrowthGroup.create_key_and_extra_args('asdf')
            Traceback (most recent call last):
            ...
            ValueError: 'asdf' is not a valid substring of 'asdf' describing a growth group.
            sage: GrowthGroup('as^df')  # indirect doctest
            Traceback (most recent call last):
            ...
            ValueError: 'as^df' is not a valid substring of as^df
            describing a growth group.
            > *previous* ValueError: Cannot create a parent out of 'as'.
            >> *previous* ValueError: unknown specification as
            >> *and* SyntaxError: ... (<string>, line 1)
            > *and* ValueError: Cannot create a parent out of 'df'.
            >> *previous* ValueError: unknown specification df
            >> *and* NameError: name 'df' is not defined
            sage: GrowthGroup('x^y^z')
            Traceback (most recent call last):
            ...
            ValueError: 'x^y^z' is an ambiguous substring of
            a growth group description of 'x^y^z'.
            Use parentheses to make it unique.
            sage: GrowthGroup('(x^y)^z')
            Traceback (most recent call last):
            ...
            ValueError: '(x^y)^z' is not a valid substring of (x^y)^z
            describing a growth group.
            > *previous* ValueError: Cannot create a parent out of 'x^y'.
            >> *previous* ValueError: unknown specification x^y
            >> *and* NameError: name 'x' is not defined
            > *and* ValueError: Cannot create a parent out of 'z'.
            >> *previous* ValueError: unknown specification z
            >> *and* NameError: name 'z' is not defined
            sage: GrowthGroup('x^(y^z)')
            Traceback (most recent call last):
            ...
            ValueError: 'x^(y^z)' is not a valid substring of x^(y^z)
            describing a growth group.
            > *previous* ValueError: Cannot create a parent out of 'x'.
            >> *previous* ValueError: unknown specification x
            >> *and* NameError: name 'x' is not defined
            > *and* ValueError: Cannot create a parent out of 'y^z'.
            >> *previous* ValueError: unknown specification y^z
            >> *and* NameError: name 'y' is not defined

        ::

            sage: GrowthGroup('n^(I*ZZ)')
            Growth Group n^(ZZ*I)
            sage: GrowthGroup('n^(I  *   ZZ)')
            Growth Group n^(ZZ*I)
        """
    def create_object(self, version, factors, **kwds):
        """
        Create an object from the given arguments.

        TESTS::

            sage: from sage.rings.asymptotic.growth_group import GrowthGroup
            sage: GrowthGroup('QQ^n')  # indirect doctest
            Growth Group QQ^n * Signs^n
        """

GrowthGroup: Incomplete
