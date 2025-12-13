import sage.structure.element
import sage.structure.parent
import sage.structure.unique_representation
from sage.structure.element import have_same_parent as have_same_parent, parent as parent
from sage.structure.unique_representation import UniqueRepresentation as UniqueRepresentation
from typing import Any, ClassVar

class DummyParent(sage.structure.unique_representation.UniqueRepresentation, sage.structure.parent.Parent):
    """File: /build/sagemath/src/sage/src/sage/structure/element_wrapper.pyx (starting at line 427)

        A class for creating dummy parents for testing :class:`ElementWrapper`
    """
    def __init__(self, name) -> Any:
        '''DummyParent.__init__(self, name)

        File: /build/sagemath/src/sage/src/sage/structure/element_wrapper.pyx (starting at line 431)

        EXAMPLES::

            sage: from sage.structure.element_wrapper import DummyParent
            sage: parent = DummyParent("A Parent")
            sage: skipped = ["_test_an_element", "_test_category",
            ....:            "_test_elements", "_test_elements_eq_reflexive",
            ....:            "_test_elements_eq_symmetric",
            ....:            "_test_elements_eq_transitive",
            ....:            "_test_elements_neq", "_test_some_elements"]
            sage: TestSuite(parent).run(skip=skipped)'''

class ElementWrapper(sage.structure.element.Element):
    '''ElementWrapper(parent, value)

    File: /build/sagemath/src/sage/src/sage/structure/element_wrapper.pyx (starting at line 32)

    A class for wrapping Sage or Python objects as Sage elements.

    EXAMPLES::

        sage: from sage.structure.element_wrapper import DummyParent
        sage: parent = DummyParent("A parent")
        sage: o = ElementWrapper(parent, "bla"); o
        \'bla\'
        sage: isinstance(o, sage.structure.element.Element)
        True
        sage: o.parent()
        A parent
        sage: o.value
        \'bla\'

    Note that ``o`` is not *an instance of* ``str``, but rather
    *contains a* ``str``. Therefore, ``o`` does not inherit the string
    methods. On the other hand, it is provided with reasonable default
    implementations for equality testing, hashing, etc.

    The typical use case of ``ElementWrapper`` is for trivially
    constructing new element classes from pre-existing Sage or Python
    classes, with a containment relation. Here we construct the
    tropical monoid of integers endowed with ``min`` as
    multiplication. There, it is desirable *not* to inherit the
    ``factor`` method from ``Integer``::

        sage: class MinMonoid(Parent):
        ....:     def _repr_(self):
        ....:         return "The min monoid"
        ....:
        sage: M = MinMonoid()
        sage: class MinMonoidElement(ElementWrapper):
        ....:     wrapped_class = Integer
        ....:
        ....:     def __mul__(self, other):
        ....:         return MinMonoidElement(self.parent(), min(self.value, other.value))
        sage: x = MinMonoidElement(M, 5); x
        5
        sage: x.parent()
        The min monoid
        sage: x.value
        5
        sage: y = MinMonoidElement(M, 3)
        sage: x * y
        3

    This example was voluntarily kept to a bare minimum. See the
    examples in the categories (e.g. ``Semigroups().example()``) for
    several full featured applications.

    .. WARNING::

        Versions before :issue:`14519` had parent as the second argument and
        the value as the first.'''
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    value: value
    def __init__(self, parent, value) -> Any:
        '''File: /build/sagemath/src/sage/src/sage/structure/element_wrapper.pyx (starting at line 90)

                EXAMPLES::

                    sage: from sage.structure.element_wrapper import DummyParent
                    sage: a = ElementWrapper(DummyParent("A parent"), 1)

                TESTS::

                    sage: TestSuite(a).run(skip = "_test_category")

                .. NOTE::

                    :class:`ElementWrapper` is not intended to be used directly,
                    hence the failing category test.
        '''
    def __copy__(self) -> Any:
        '''ElementWrapper.__copy__(self)

        File: /build/sagemath/src/sage/src/sage/structure/element_wrapper.pyx (starting at line 393)

        Copy ``self`` and in particular its ``value`` attribute.

        EXAMPLES::

            sage: from sage.structure.element_wrapper import DummyParent
            sage: parent = DummyParent("A parent")
            sage: o1 = ElementWrapper(parent, [1]); o1
            [1]
            sage: o2 = copy(o1); o2
            [1]
            sage: o1 is o2, o1.value is o2.value
            (False, False)
            sage: o2.value[0] = 3; o2
            [3]
            sage: o1
            [1]
            sage: class bla(ElementWrapper): pass
            sage: o3 = bla(parent, [1])
            sage: o4 = copy(o3)
            sage: o3.value[0] = 3; o4
            [1]
            sage: o3.__class__
            <class \'__main__.bla\'>
            sage: o4.__class__
            <class \'__main__.bla\'>'''
    def __eq__(self, other: object) -> bool:
        """Return self==value."""
    def __ge__(self, other: object) -> bool:
        """Return self>=value."""
    def __gt__(self, other: object) -> bool:
        """Return self>value."""
    def __hash__(self) -> Any:
        '''ElementWrapper.__hash__(self)

        File: /build/sagemath/src/sage/src/sage/structure/element_wrapper.pyx (starting at line 237)

        Return the same hash as for the wrapped element.

        EXAMPLES::

            sage: from sage.structure.element_wrapper import DummyParent
            sage: parent1 = DummyParent("A parent")
            sage: parent2 = DummyParent("Another parent")
            sage: hash(ElementWrapper(parent1, 1))
            1
            sage: hash(ElementWrapper(parent2, 1))
            1

        .. TODO::

            Should this take the parent and/or the class into account?'''
    def __le__(self, other: object) -> bool:
        """Return self<=value."""
    def __lt__(self, other: object) -> bool:
        """Return self<value."""
    def __ne__(self, other: object) -> bool:
        """Return self!=value."""

class ElementWrapperCheckWrappedClass(ElementWrapper):
    """File: /build/sagemath/src/sage/src/sage/structure/element_wrapper.pyx (starting at line 517)

        An :class:`element wrapper <ElementWrapper>` such that comparison
        operations are done against subclasses of ``wrapped_class``.
    """
    wrapped_class: ClassVar[type[object]] = ...
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    @classmethod
    def __init__(cls, *args, **kwargs) -> None:
        """Create and return a new object.  See help(type) for accurate signature."""
    def __eq__(self, other: object) -> bool:
        """Return self==value."""
    def __ge__(self, other: object) -> bool:
        """Return self>=value."""
    def __gt__(self, other: object) -> bool:
        """Return self>value."""
    def __hash__(self) -> Any:
        """ElementWrapperCheckWrappedClass.__hash__(self)

        File: /build/sagemath/src/sage/src/sage/structure/element_wrapper.pyx (starting at line 524)

        Return the same hash as for the wrapped element.

        EXAMPLES::

            sage: A = cartesian_product([ZZ, ZZ])
            sage: e1 = A((6,9))
            sage: e2 = A((3,8))
            sage: e3 = A((6,9))
            sage: hash(e1) == hash(e2)
            False
            sage: hash(e1) == hash(e3)
            True"""
    def __le__(self, other: object) -> bool:
        """Return self<=value."""
    def __lt__(self, other: object) -> bool:
        """Return self<value."""
    def __ne__(self, other: object) -> bool:
        """Return self!=value."""

class ElementWrapperTester(ElementWrapper):
    """File: /build/sagemath/src/sage/src/sage/structure/element_wrapper.pyx (starting at line 457)

        Test class for the default :meth:`.__copy` method of subclasses of
        :class:`ElementWrapper`.

        TESTS::

            sage: from sage.structure.element_wrapper import ElementWrapperTester
            sage: x = ElementWrapperTester()
            sage: x.append(2); y = copy(x); y.append(42)
            sage: type(y)
            <class 'sage.structure.element_wrapper.ElementWrapperTester'>
            sage: x, y
            ([n=1, value=[2]], [n=2, value=[2, 42]])
            sage: x.append(21); x.append(7)
            sage: x, y
            ([n=3, value=[2, 21, 7]], [n=2, value=[2, 42]])
            sage: x.value, y.value
            ([2, 21, 7], [2, 42])
            sage: x.__dict__, y.__dict__
            ({'n': 3}, {'n': 2})
    """
    def __init__(self) -> Any:
        """ElementWrapperTester.__init__(self)

        File: /build/sagemath/src/sage/src/sage/structure/element_wrapper.pyx (starting at line 479)

        TESTS::

            sage: from sage.structure.element_wrapper import ElementWrapperTester
            sage: x = ElementWrapperTester(); x
            [n=0, value=[]]"""
    def append(self, x) -> Any:
        """ElementWrapperTester.append(self, x)

        File: /build/sagemath/src/sage/src/sage/structure/element_wrapper.pyx (starting at line 491)

        TESTS::

            sage: from sage.structure.element_wrapper import ElementWrapperTester
            sage: x = ElementWrapperTester()
            sage: x.append(2); x
            [n=1, value=[2]]"""
