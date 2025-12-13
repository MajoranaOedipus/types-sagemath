import _cython_3_2_1
import sage.structure.parent
from sage.misc.superseded import deprecation as deprecation
from sage.rings.infinity import infinity as infinity
from typing import Any, ClassVar, overload

is_Group: _cython_3_2_1.cython_function_or_method

class AbelianGroup(Group):
    """File: /build/sagemath/src/sage/src/sage/groups/group.pyx (starting at line 265)

        Generic abelian group.
    """
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    @classmethod
    def __init__(cls, *args, **kwargs) -> None:
        """Create and return a new object.  See help(type) for accurate signature."""
    @overload
    def is_abelian(self) -> Any:
        """AbelianGroup.is_abelian(self)

        File: /build/sagemath/src/sage/src/sage/groups/group.pyx (starting at line 269)

        Return ``True``.

        EXAMPLES::

            sage: from sage.groups.group import AbelianGroup
            sage: G = AbelianGroup()
            sage: G.is_abelian()
            True"""
    @overload
    def is_abelian(self) -> Any:
        """AbelianGroup.is_abelian(self)

        File: /build/sagemath/src/sage/src/sage/groups/group.pyx (starting at line 269)

        Return ``True``.

        EXAMPLES::

            sage: from sage.groups.group import AbelianGroup
            sage: G = AbelianGroup()
            sage: G.is_abelian()
            True"""

class AlgebraicGroup(Group):
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    @classmethod
    def __init__(cls, *args, **kwargs) -> None:
        """Create and return a new object.  See help(type) for accurate signature."""

class FiniteGroup(Group):
    """FiniteGroup(base=None, category=None)

    File: /build/sagemath/src/sage/src/sage/groups/group.pyx (starting at line 282)

    Generic finite group."""
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    def __init__(self, base=..., category=...) -> Any:
        """File: /build/sagemath/src/sage/src/sage/groups/group.pyx (starting at line 287)

                The Python constructor.

                TESTS::

                    sage: from sage.groups.group import FiniteGroup
                    sage: G = FiniteGroup()
                    sage: G.category()
                    Category of finite groups
        """
    @overload
    def is_finite(self) -> Any:
        """FiniteGroup.is_finite(self)

        File: /build/sagemath/src/sage/src/sage/groups/group.pyx (starting at line 308)

        Return ``True``.

        EXAMPLES::

            sage: from sage.groups.group import FiniteGroup
            sage: G = FiniteGroup()
            sage: G.is_finite()
            True"""
    @overload
    def is_finite(self) -> Any:
        """FiniteGroup.is_finite(self)

        File: /build/sagemath/src/sage/src/sage/groups/group.pyx (starting at line 308)

        Return ``True``.

        EXAMPLES::

            sage: from sage.groups.group import FiniteGroup
            sage: G = FiniteGroup()
            sage: G.is_finite()
            True"""

class Group(sage.structure.parent.Parent):
    '''Group(base=None, category=None)

    File: /build/sagemath/src/sage/src/sage/groups/group.pyx (starting at line 49)

    Base class for all groups.

    TESTS::

        sage: from sage.groups.group import Group
        sage: G = Group()
        sage: TestSuite(G).run(skip = ["_test_an_element",        ....:                          "_test_associativity",        ....:                          "_test_elements",        ....:                          "_test_elements_eq_reflexive",        ....:                          "_test_elements_eq_symmetric",        ....:                          "_test_elements_eq_transitive",        ....:                          "_test_elements_neq",        ....:                          "_test_inverse",        ....:                          "_test_one",        ....:                          "_test_pickling",        ....:                          "_test_prod",        ....:                          "_test_some_elements"])

    Generic groups have very little functionality::

        sage: 4 in G
        Traceback (most recent call last):
        ...
        NotImplementedError: cannot construct elements of <sage.groups.group.Group object at ...>'''
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    @overload
    def __init__(self, base=..., category=...) -> Any:
        """File: /build/sagemath/src/sage/src/sage/groups/group.pyx (starting at line 77)

                The Python constructor.

                TESTS::

                    sage: from sage.groups.group import Group
                    sage: G = Group()
                    sage: G.category()
                    Category of groups
                    sage: G = Group(category=Groups()) # todo: do the same test with some subcategory of Groups when there will exist one
                    sage: G.category()
                    Category of groups
                    sage: G = Group(category=CommutativeAdditiveGroups())
                    Traceback (most recent call last):
                    ...
                    ValueError: (Category of commutative additive groups,) is not a subcategory of Category of groups
                    sage: G._repr_option('element_is_atomic')
                    False

                Check for :issue:`8119`::

                    sage: # needs sage.groups
                    sage: G = SymmetricGroup(2)
                    sage: h = hash(G)
                    sage: G.rename('S2')
                    sage: h == hash(G)
                    True
        """
    @overload
    def __init__(self) -> Any:
        """File: /build/sagemath/src/sage/src/sage/groups/group.pyx (starting at line 77)

                The Python constructor.

                TESTS::

                    sage: from sage.groups.group import Group
                    sage: G = Group()
                    sage: G.category()
                    Category of groups
                    sage: G = Group(category=Groups()) # todo: do the same test with some subcategory of Groups when there will exist one
                    sage: G.category()
                    Category of groups
                    sage: G = Group(category=CommutativeAdditiveGroups())
                    Traceback (most recent call last):
                    ...
                    ValueError: (Category of commutative additive groups,) is not a subcategory of Category of groups
                    sage: G._repr_option('element_is_atomic')
                    False

                Check for :issue:`8119`::

                    sage: # needs sage.groups
                    sage: G = SymmetricGroup(2)
                    sage: h = hash(G)
                    sage: G.rename('S2')
                    sage: h == hash(G)
                    True
        """
    @overload
    def is_abelian(self) -> Any:
        """Group.is_abelian(self)

        File: /build/sagemath/src/sage/src/sage/groups/group.pyx (starting at line 116)

        Test whether this group is abelian.

        EXAMPLES::

            sage: from sage.groups.group import Group
            sage: G = Group()
            sage: G.is_abelian()
            Traceback (most recent call last):
            ...
            NotImplementedError"""
    @overload
    def is_abelian(self) -> Any:
        """Group.is_abelian(self)

        File: /build/sagemath/src/sage/src/sage/groups/group.pyx (starting at line 116)

        Test whether this group is abelian.

        EXAMPLES::

            sage: from sage.groups.group import Group
            sage: G = Group()
            sage: G.is_abelian()
            Traceback (most recent call last):
            ...
            NotImplementedError"""
    @overload
    def is_commutative(self) -> Any:
        """Group.is_commutative(self)

        File: /build/sagemath/src/sage/src/sage/groups/group.pyx (starting at line 131)

        Test whether this group is commutative.

        This is an alias for is_abelian, largely to make groups work
        well with the Factorization class.

        (Note for developers: Derived classes should override is_abelian, not
        is_commutative.)

        EXAMPLES::

            sage: SL(2, 7).is_commutative()                                             # needs sage.libs.gap sage.modules sage.rings.finite_rings
            False"""
    @overload
    def is_commutative(self) -> Any:
        """Group.is_commutative(self)

        File: /build/sagemath/src/sage/src/sage/groups/group.pyx (starting at line 131)

        Test whether this group is commutative.

        This is an alias for is_abelian, largely to make groups work
        well with the Factorization class.

        (Note for developers: Derived classes should override is_abelian, not
        is_commutative.)

        EXAMPLES::

            sage: SL(2, 7).is_commutative()                                             # needs sage.libs.gap sage.modules sage.rings.finite_rings
            False"""
    @overload
    def is_finite(self) -> Any:
        """Group.is_finite(self)

        File: /build/sagemath/src/sage/src/sage/groups/group.pyx (starting at line 174)

        Return ``True`` if this group is finite.

        EXAMPLES::

            sage: from sage.groups.group import Group
            sage: G = Group()
            sage: G.is_finite()
            Traceback (most recent call last):
            ...
            NotImplementedError"""
    @overload
    def is_finite(self) -> Any:
        """Group.is_finite(self)

        File: /build/sagemath/src/sage/src/sage/groups/group.pyx (starting at line 174)

        Return ``True`` if this group is finite.

        EXAMPLES::

            sage: from sage.groups.group import Group
            sage: G = Group()
            sage: G.is_finite()
            Traceback (most recent call last):
            ...
            NotImplementedError"""
    @overload
    def is_multiplicative(self) -> Any:
        """Group.is_multiplicative(self)

        File: /build/sagemath/src/sage/src/sage/groups/group.pyx (starting at line 221)

        Return ``True`` if the group operation is given by ``*`` (rather than ``+``).

        Override for additive groups.

        EXAMPLES::

            sage: from sage.groups.group import Group
            sage: G = Group()
            sage: G.is_multiplicative()
            True"""
    @overload
    def is_multiplicative(self) -> Any:
        """Group.is_multiplicative(self)

        File: /build/sagemath/src/sage/src/sage/groups/group.pyx (starting at line 221)

        Return ``True`` if the group operation is given by ``*`` (rather than ``+``).

        Override for additive groups.

        EXAMPLES::

            sage: from sage.groups.group import Group
            sage: G = Group()
            sage: G.is_multiplicative()
            True"""
    @overload
    def is_trivial(self) -> Any:
        """Group.is_trivial(self)

        File: /build/sagemath/src/sage/src/sage/groups/group.pyx (starting at line 189)

        Return ``True`` if this group is the trivial group.

        A group is trivial, if it consists only of the identity
        element.

        .. WARNING::

            It is in principle undecidable whether a group is
            trivial, for example, if the group is given by a finite
            presentation.  Thus, this method may not terminate.

        EXAMPLES::

            sage: groups.presentation.Cyclic(1).is_trivial()
            True

            sage: G.<a,b> = FreeGroup('a, b')
            sage: H = G / (a^2, b^3, a*b*~a*~b)
            sage: H.is_trivial()
            False

        A non-trivial presentation of the trivial group::

            sage: F.<a,b> = FreeGroup()
            sage: J = F / ((~a)*b*a*(~b)^2, (~b)*a*b*(~a)^2)
            sage: J.is_trivial()
            True"""
    @overload
    def is_trivial(self) -> Any:
        """Group.is_trivial(self)

        File: /build/sagemath/src/sage/src/sage/groups/group.pyx (starting at line 189)

        Return ``True`` if this group is the trivial group.

        A group is trivial, if it consists only of the identity
        element.

        .. WARNING::

            It is in principle undecidable whether a group is
            trivial, for example, if the group is given by a finite
            presentation.  Thus, this method may not terminate.

        EXAMPLES::

            sage: groups.presentation.Cyclic(1).is_trivial()
            True

            sage: G.<a,b> = FreeGroup('a, b')
            sage: H = G / (a^2, b^3, a*b*~a*~b)
            sage: H.is_trivial()
            False

        A non-trivial presentation of the trivial group::

            sage: F.<a,b> = FreeGroup()
            sage: J = F / ((~a)*b*a*(~b)^2, (~b)*a*b*(~a)^2)
            sage: J.is_trivial()
            True"""
    @overload
    def is_trivial(self) -> Any:
        """Group.is_trivial(self)

        File: /build/sagemath/src/sage/src/sage/groups/group.pyx (starting at line 189)

        Return ``True`` if this group is the trivial group.

        A group is trivial, if it consists only of the identity
        element.

        .. WARNING::

            It is in principle undecidable whether a group is
            trivial, for example, if the group is given by a finite
            presentation.  Thus, this method may not terminate.

        EXAMPLES::

            sage: groups.presentation.Cyclic(1).is_trivial()
            True

            sage: G.<a,b> = FreeGroup('a, b')
            sage: H = G / (a^2, b^3, a*b*~a*~b)
            sage: H.is_trivial()
            False

        A non-trivial presentation of the trivial group::

            sage: F.<a,b> = FreeGroup()
            sage: J = F / ((~a)*b*a*(~b)^2, (~b)*a*b*(~a)^2)
            sage: J.is_trivial()
            True"""
    @overload
    def is_trivial(self) -> Any:
        """Group.is_trivial(self)

        File: /build/sagemath/src/sage/src/sage/groups/group.pyx (starting at line 189)

        Return ``True`` if this group is the trivial group.

        A group is trivial, if it consists only of the identity
        element.

        .. WARNING::

            It is in principle undecidable whether a group is
            trivial, for example, if the group is given by a finite
            presentation.  Thus, this method may not terminate.

        EXAMPLES::

            sage: groups.presentation.Cyclic(1).is_trivial()
            True

            sage: G.<a,b> = FreeGroup('a, b')
            sage: H = G / (a^2, b^3, a*b*~a*~b)
            sage: H.is_trivial()
            False

        A non-trivial presentation of the trivial group::

            sage: F.<a,b> = FreeGroup()
            sage: J = F / ((~a)*b*a*(~b)^2, (~b)*a*b*(~a)^2)
            sage: J.is_trivial()
            True"""
    @overload
    def order(self) -> Any:
        """Group.order(self)

        File: /build/sagemath/src/sage/src/sage/groups/group.pyx (starting at line 148)

        Return the number of elements of this group.

        This is either a positive integer or infinity.

        EXAMPLES::

            sage: from sage.groups.group import Group
            sage: G = Group()
            sage: G.order()
            Traceback (most recent call last):
            ...
            NotImplementedError

        TESTS::

            sage: H = SL(2, QQ)                                                         # needs sage.modules
            sage: H.order()                                                             # needs sage.modules
            +Infinity"""
    @overload
    def order(self) -> Any:
        """Group.order(self)

        File: /build/sagemath/src/sage/src/sage/groups/group.pyx (starting at line 148)

        Return the number of elements of this group.

        This is either a positive integer or infinity.

        EXAMPLES::

            sage: from sage.groups.group import Group
            sage: G = Group()
            sage: G.order()
            Traceback (most recent call last):
            ...
            NotImplementedError

        TESTS::

            sage: H = SL(2, QQ)                                                         # needs sage.modules
            sage: H.order()                                                             # needs sage.modules
            +Infinity"""
    @overload
    def order(self) -> Any:
        """Group.order(self)

        File: /build/sagemath/src/sage/src/sage/groups/group.pyx (starting at line 148)

        Return the number of elements of this group.

        This is either a positive integer or infinity.

        EXAMPLES::

            sage: from sage.groups.group import Group
            sage: G = Group()
            sage: G.order()
            Traceback (most recent call last):
            ...
            NotImplementedError

        TESTS::

            sage: H = SL(2, QQ)                                                         # needs sage.modules
            sage: H.order()                                                             # needs sage.modules
            +Infinity"""
    @overload
    def quotient(self, H, **kwds) -> Any:
        """Group.quotient(self, H, **kwds)

        File: /build/sagemath/src/sage/src/sage/groups/group.pyx (starting at line 250)

        Return the quotient of this group by the normal subgroup `H`.

        EXAMPLES::

            sage: from sage.groups.group import Group
            sage: G = Group()
            sage: G.quotient(G)
            Traceback (most recent call last):
            ...
            NotImplementedError"""
    @overload
    def quotient(self, G) -> Any:
        """Group.quotient(self, H, **kwds)

        File: /build/sagemath/src/sage/src/sage/groups/group.pyx (starting at line 250)

        Return the quotient of this group by the normal subgroup `H`.

        EXAMPLES::

            sage: from sage.groups.group import Group
            sage: G = Group()
            sage: G.quotient(G)
            Traceback (most recent call last):
            ...
            NotImplementedError"""
