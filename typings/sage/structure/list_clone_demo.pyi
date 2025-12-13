import sage.structure.list_clone
import sage.structure.parent
import sage.structure.unique_representation
from sage.categories.sets_cat import Sets as Sets
from sage.structure.element import have_same_parent as have_same_parent, parent as parent
from sage.structure.parent import Parent as Parent
from sage.structure.unique_representation import UniqueRepresentation as UniqueRepresentation
from typing import Any, ClassVar, overload

class IncreasingArray(sage.structure.list_clone.ClonableArray):
    """File: /build/sagemath/src/sage/src/sage/structure/list_clone_demo.pyx (starting at line 23)

        A small extension class for testing
        :class:`~sage.structure.list_clone.ClonableArray`.

        TESTS::

            sage: from sage.structure.list_clone_demo import IncreasingArrays
            sage: TestSuite(IncreasingArrays()([1,2,3])).run()
            sage: TestSuite(IncreasingArrays()([])).run()
    """
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    @classmethod
    def __init__(cls, *args, **kwargs) -> None:
        """Create and return a new object.  See help(type) for accurate signature."""
    def check(self) -> Any:
        """IncreasingArray.check(self)

        File: /build/sagemath/src/sage/src/sage/structure/list_clone_demo.pyx (starting at line 35)

        Check that ``self`` is increasing.

        EXAMPLES::

            sage: from sage.structure.list_clone_demo import IncreasingArrays
            sage: IncreasingArrays()([1,2,3]) # indirect doctest
            [1, 2, 3]
            sage: IncreasingArrays()([3,2,1]) # indirect doctest
            Traceback (most recent call last):
            ...
            ValueError: array is not increasing"""

class IncreasingArrays(sage.structure.unique_representation.UniqueRepresentation, sage.structure.parent.Parent):
    """File: /build/sagemath/src/sage/src/sage/structure/list_clone_demo.pyx (starting at line 55)

        A small (incomplete) parent for testing
        :class:`~sage.structure.list_clone.ClonableArray`

        TESTS::

            sage: from sage.structure.list_clone_demo import IncreasingArrays
            sage: IncreasingArrays().element_class
            <... 'sage.structure.list_clone_demo.IncreasingArray'>
    """

    class Element(sage.structure.list_clone.ClonableArray):
        """File: /build/sagemath/src/sage/src/sage/structure/list_clone_demo.pyx (starting at line 23)

            A small extension class for testing
            :class:`~sage.structure.list_clone.ClonableArray`.

            TESTS::

                sage: from sage.structure.list_clone_demo import IncreasingArrays
                sage: TestSuite(IncreasingArrays()([1,2,3])).run()
                sage: TestSuite(IncreasingArrays()([])).run()
    """
        __pyx_vtable__: ClassVar[PyCapsule] = ...
        @classmethod
        def __init__(cls, *args, **kwargs) -> None:
            """Create and return a new object.  See help(type) for accurate signature."""
        def check(self) -> Any:
            """IncreasingArray.check(self)

            File: /build/sagemath/src/sage/src/sage/structure/list_clone_demo.pyx (starting at line 35)

            Check that ``self`` is increasing.

            EXAMPLES::

                sage: from sage.structure.list_clone_demo import IncreasingArrays
                sage: IncreasingArrays()([1,2,3]) # indirect doctest
                [1, 2, 3]
                sage: IncreasingArrays()([3,2,1]) # indirect doctest
                Traceback (most recent call last):
                ...
                ValueError: array is not increasing"""
    def __init__(self) -> Any:
        """IncreasingArrays.__init__(self)

        File: /build/sagemath/src/sage/src/sage/structure/list_clone_demo.pyx (starting at line 67)

        TESTS::

            sage: from sage.structure.list_clone_demo import IncreasingArrays
            sage: IncreasingArrays()
            <sage.structure.list_clone_demo.IncreasingArrays_with_category object at ...>
            sage: IncreasingArrays() == IncreasingArrays()
            True"""

class IncreasingIntArray(sage.structure.list_clone.ClonableIntArray):
    """File: /build/sagemath/src/sage/src/sage/structure/list_clone_demo.pyx (starting at line 138)

        A small extension class for testing
        :class:`~sage.structure.list_clone.ClonableIntArray`.

        TESTS::

            sage: from sage.structure.list_clone_demo import IncreasingIntArrays
            sage: TestSuite(IncreasingIntArrays()([1,2,3])).run()
            sage: TestSuite(IncreasingIntArrays()([])).run()
    """
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    @classmethod
    def __init__(cls, *args, **kwargs) -> None:
        """Create and return a new object.  See help(type) for accurate signature."""
    def check(self) -> Any:
        """IncreasingIntArray.check(self)

        File: /build/sagemath/src/sage/src/sage/structure/list_clone_demo.pyx (starting at line 150)

        Check that ``self`` is increasing.

        EXAMPLES::

            sage: from sage.structure.list_clone_demo import IncreasingIntArrays
            sage: IncreasingIntArrays()([1,2,3]) # indirect doctest
            [1, 2, 3]
            sage: IncreasingIntArrays()([3,2,1]) # indirect doctest
            Traceback (most recent call last):
            ...
            ValueError: array is not increasing"""

class IncreasingIntArrays(IncreasingArrays):
    """File: /build/sagemath/src/sage/src/sage/structure/list_clone_demo.pyx (starting at line 172)

        A small (incomplete) parent for testing
        :class:`~sage.structure.list_clone.ClonableIntArray`

        TESTS::

            sage: from sage.structure.list_clone_demo import IncreasingIntArrays
            sage: IncreasingIntArrays().element_class
            <... 'sage.structure.list_clone_demo.IncreasingIntArray'>
    """

    class Element(sage.structure.list_clone.ClonableIntArray):
        """File: /build/sagemath/src/sage/src/sage/structure/list_clone_demo.pyx (starting at line 138)

            A small extension class for testing
            :class:`~sage.structure.list_clone.ClonableIntArray`.

            TESTS::

                sage: from sage.structure.list_clone_demo import IncreasingIntArrays
                sage: TestSuite(IncreasingIntArrays()([1,2,3])).run()
                sage: TestSuite(IncreasingIntArrays()([])).run()
    """
        __pyx_vtable__: ClassVar[PyCapsule] = ...
        @classmethod
        def __init__(cls, *args, **kwargs) -> None:
            """Create and return a new object.  See help(type) for accurate signature."""
        def check(self) -> Any:
            """IncreasingIntArray.check(self)

            File: /build/sagemath/src/sage/src/sage/structure/list_clone_demo.pyx (starting at line 150)

            Check that ``self`` is increasing.

            EXAMPLES::

                sage: from sage.structure.list_clone_demo import IncreasingIntArrays
                sage: IncreasingIntArrays()([1,2,3]) # indirect doctest
                [1, 2, 3]
                sage: IncreasingIntArrays()([3,2,1]) # indirect doctest
                Traceback (most recent call last):
                ...
                ValueError: array is not increasing"""

class IncreasingList(sage.structure.list_clone.ClonableList):
    """File: /build/sagemath/src/sage/src/sage/structure/list_clone_demo.pyx (starting at line 106)

        A small extension class for testing
        :class:`~sage.structure.list_clone.ClonableList`

        TESTS::

            sage: from sage.structure.list_clone_demo import IncreasingLists
            sage: TestSuite(IncreasingLists()([1,2,3])).run()
            sage: TestSuite(IncreasingLists()([])).run()
    """
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    @classmethod
    def __init__(cls, *args, **kwargs) -> None:
        """Create and return a new object.  See help(type) for accurate signature."""
    def check(self) -> Any:
        """IncreasingList.check(self)

        File: /build/sagemath/src/sage/src/sage/structure/list_clone_demo.pyx (starting at line 118)

        Check that ``self`` is increasing.

        EXAMPLES::

            sage: from sage.structure.list_clone_demo import IncreasingLists
            sage: IncreasingLists()([1,2,3]) # indirect doctest
            [1, 2, 3]
            sage: IncreasingLists()([3,2,1]) # indirect doctest
            Traceback (most recent call last):
            ...
            ValueError: array is not increasing"""

class IncreasingLists(IncreasingArrays):
    """File: /build/sagemath/src/sage/src/sage/structure/list_clone_demo.pyx (starting at line 92)

        A small (incomplete) parent for testing
        :class:`~sage.structure.list_clone.ClonableList`

        TESTS::

            sage: from sage.structure.list_clone_demo import IncreasingLists
            sage: IncreasingLists().element_class
            <... 'sage.structure.list_clone_demo.IncreasingList'>
    """

    class Element(sage.structure.list_clone.ClonableList):
        """File: /build/sagemath/src/sage/src/sage/structure/list_clone_demo.pyx (starting at line 106)

            A small extension class for testing
            :class:`~sage.structure.list_clone.ClonableList`

            TESTS::

                sage: from sage.structure.list_clone_demo import IncreasingLists
                sage: TestSuite(IncreasingLists()([1,2,3])).run()
                sage: TestSuite(IncreasingLists()([])).run()
    """
        __pyx_vtable__: ClassVar[PyCapsule] = ...
        @classmethod
        def __init__(cls, *args, **kwargs) -> None:
            """Create and return a new object.  See help(type) for accurate signature."""
        def check(self) -> Any:
            """IncreasingList.check(self)

            File: /build/sagemath/src/sage/src/sage/structure/list_clone_demo.pyx (starting at line 118)

            Check that ``self`` is increasing.

            EXAMPLES::

                sage: from sage.structure.list_clone_demo import IncreasingLists
                sage: IncreasingLists()([1,2,3]) # indirect doctest
                [1, 2, 3]
                sage: IncreasingLists()([3,2,1]) # indirect doctest
                Traceback (most recent call last):
                ...
                ValueError: array is not increasing"""

class SortedList(sage.structure.list_clone.NormalizedClonableList):
    """File: /build/sagemath/src/sage/src/sage/structure/list_clone_demo.pyx (starting at line 186)

        A small extension class for testing
        :class:`~sage.structure.list_clone.NormalizedClonableList`.

        TESTS::

            sage: from sage.structure.list_clone_demo import IncreasingIntArrays
            sage: TestSuite(IncreasingIntArrays()([1,2,3])).run()
            sage: TestSuite(IncreasingIntArrays()([])).run()
    """
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    @classmethod
    def __init__(cls, *args, **kwargs) -> None:
        """Create and return a new object.  See help(type) for accurate signature."""
    def check(self) -> Any:
        """SortedList.check(self)

        File: /build/sagemath/src/sage/src/sage/structure/list_clone_demo.pyx (starting at line 217)

        Check that ``self`` is strictly increasing.

        EXAMPLES::

            sage: from sage.structure.list_clone_demo import SortedList, SortedLists
            sage: SortedLists()([1,2,3]) # indirect doctest
            [1, 2, 3]
            sage: SortedLists()([3,2,2]) # indirect doctest
            Traceback (most recent call last):
            ...
            ValueError: list is not strictly increasing"""
    @overload
    def normalize(self) -> Any:
        """SortedList.normalize(self)

        File: /build/sagemath/src/sage/src/sage/structure/list_clone_demo.pyx (starting at line 197)

        Normalize ``self``.

        Sort the list stored in ``self``.

        EXAMPLES::

            sage: from sage.structure.list_clone_demo import SortedList, SortedLists
            sage: l = SortedList(SortedLists(), [3,1,2], False, False)
            sage: l         # indirect doctest
            [1, 2, 3]
            sage: l[1] = 5; l
            [1, 5, 3]
            sage: l.normalize(); l
            [1, 3, 5]"""
    @overload
    def normalize(self) -> Any:
        """SortedList.normalize(self)

        File: /build/sagemath/src/sage/src/sage/structure/list_clone_demo.pyx (starting at line 197)

        Normalize ``self``.

        Sort the list stored in ``self``.

        EXAMPLES::

            sage: from sage.structure.list_clone_demo import SortedList, SortedLists
            sage: l = SortedList(SortedLists(), [3,1,2], False, False)
            sage: l         # indirect doctest
            [1, 2, 3]
            sage: l[1] = 5; l
            [1, 5, 3]
            sage: l.normalize(); l
            [1, 3, 5]"""

class SortedLists(IncreasingLists):
    """File: /build/sagemath/src/sage/src/sage/structure/list_clone_demo.pyx (starting at line 236)

        A small (incomplete) parent for testing
        :class:`~sage.structure.list_clone.NormalizedClonableList`

        TESTS::

            sage: from sage.structure.list_clone_demo import SortedList, SortedLists
            sage: SL = SortedLists()
            sage: SL([3,1,2])
            [1, 2, 3]
    """

    class Element(sage.structure.list_clone.NormalizedClonableList):
        """File: /build/sagemath/src/sage/src/sage/structure/list_clone_demo.pyx (starting at line 186)

            A small extension class for testing
            :class:`~sage.structure.list_clone.NormalizedClonableList`.

            TESTS::

                sage: from sage.structure.list_clone_demo import IncreasingIntArrays
                sage: TestSuite(IncreasingIntArrays()([1,2,3])).run()
                sage: TestSuite(IncreasingIntArrays()([])).run()
    """
        __pyx_vtable__: ClassVar[PyCapsule] = ...
        @classmethod
        def __init__(cls, *args, **kwargs) -> None:
            """Create and return a new object.  See help(type) for accurate signature."""
        def check(self) -> Any:
            """SortedList.check(self)

            File: /build/sagemath/src/sage/src/sage/structure/list_clone_demo.pyx (starting at line 217)

            Check that ``self`` is strictly increasing.

            EXAMPLES::

                sage: from sage.structure.list_clone_demo import SortedList, SortedLists
                sage: SortedLists()([1,2,3]) # indirect doctest
                [1, 2, 3]
                sage: SortedLists()([3,2,2]) # indirect doctest
                Traceback (most recent call last):
                ...
                ValueError: list is not strictly increasing"""
        @overload
        def normalize(self) -> Any:
            """SortedList.normalize(self)

            File: /build/sagemath/src/sage/src/sage/structure/list_clone_demo.pyx (starting at line 197)

            Normalize ``self``.

            Sort the list stored in ``self``.

            EXAMPLES::

                sage: from sage.structure.list_clone_demo import SortedList, SortedLists
                sage: l = SortedList(SortedLists(), [3,1,2], False, False)
                sage: l         # indirect doctest
                [1, 2, 3]
                sage: l[1] = 5; l
                [1, 5, 3]
                sage: l.normalize(); l
                [1, 3, 5]"""
        @overload
        def normalize(self) -> Any:
            """SortedList.normalize(self)

            File: /build/sagemath/src/sage/src/sage/structure/list_clone_demo.pyx (starting at line 197)

            Normalize ``self``.

            Sort the list stored in ``self``.

            EXAMPLES::

                sage: from sage.structure.list_clone_demo import SortedList, SortedLists
                sage: l = SortedList(SortedLists(), [3,1,2], False, False)
                sage: l         # indirect doctest
                [1, 2, 3]
                sage: l[1] = 5; l
                [1, 5, 3]
                sage: l.normalize(); l
                [1, 3, 5]"""
