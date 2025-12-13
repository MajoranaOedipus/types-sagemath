import sage.structure.element
from sage.structure.element import have_same_parent as have_same_parent, parent as parent
from sage.structure.richcmp import revop as revop, rich_to_bool as rich_to_bool, rich_to_bool_sgn as rich_to_bool_sgn, richcmp as richcmp, richcmp_not_equal as richcmp_not_equal
from typing import Any, ClassVar, overload

class ClonableArray(ClonableElement):
    """ClonableArray(Parent parent, lst, check=True, immutable=True)

    File: /build/sagemath/src/sage/src/sage/structure/list_clone.pyx (starting at line 490)

    Array with clone protocol.

    The class of objects which are
    :class:`Element<sage.structure.element.Element>` behave as arrays
    (i.e. lists of fixed length) and implement the clone protocol. See
    :class:`ClonableElement` for details about clone protocol.

    INPUT:

    - ``parent`` -- a :class:`Parent<sage.structure.parent.Parent>`
    - ``lst`` -- list
    - ``check`` -- boolean specifying if the invariant must be checked
      using method :meth:`check`
    - ``immutable`` -- boolean (default: ``True``); whether the created element
      is immutable

    .. SEEALSO:: :class:`~sage.structure.list_clone_demo.IncreasingArray` for
                 an example of usage.

    EXAMPLES::

        sage: from sage.structure.list_clone_demo import IncreasingArrays
        sage: IA = IncreasingArrays()
        sage: ia1 = IA([1, 4, 6]); ia1
        [1, 4, 6]
        sage: with ia1.clone() as ia2:
        ....:      ia2[1] = 5
        sage: ia2
        [1, 5, 6]
        sage: with ia1.clone() as ia2:
        ....:      ia2[1] = 7
        Traceback (most recent call last):
        ...
        ValueError: array is not increasing"""
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    def __init__(self, Parentparent, lst, check=..., immutable=...) -> Any:
        """File: /build/sagemath/src/sage/src/sage/structure/list_clone.pyx (starting at line 527)

                Initialize ``self``.

                TESTS::

                    sage: from sage.structure.list_clone_demo import IncreasingArrays
                    sage: IncreasingArrays()([1,2,3])
                    [1, 2, 3]

                    sage: el = IncreasingArrays()([3,2,1])
                    Traceback (most recent call last):
                    ...
                    ValueError: array is not increasing

                    sage: IncreasingArrays()(None)
                    Traceback (most recent call last):
                    ...
                    TypeError: 'NoneType' object is not iterable

                You are not supposed to do the following (giving a wrong list and
                desactivating checks)::

                    sage: broken = IncreasingArrays()([3,2,1], False)
        """
    def check(self) -> Any:
        """ClonableArray.check(self)

        File: /build/sagemath/src/sage/src/sage/structure/list_clone.pyx (starting at line 893)

        Check that ``self`` fulfill the invariants.

        This is an abstract method. Subclasses are supposed to overload
        ``check``.

        EXAMPLES::

            sage: from sage.structure.list_clone import ClonableArray
            sage: ClonableArray(Parent(), [1,2,3]) # indirect doctest
            Traceback (most recent call last):
            ...
            NotImplementedError: this should never be called, please overload the check method
            sage: from sage.structure.list_clone_demo import IncreasingArrays
            sage: el = IncreasingArrays()([1,2,4]) # indirect doctest"""
    def count(self, key) -> int:
        """ClonableArray.count(self, key) -> int

        File: /build/sagemath/src/sage/src/sage/structure/list_clone.pyx (starting at line 786)

        Return number of ``i``'s for which ``s[i] == key``

        EXAMPLES::

            sage: from sage.structure.list_clone_demo import IncreasingArrays
            sage: c = IncreasingArrays()([1,2,2,4])
            sage: c.count(1)
            1
            sage: c.count(2)
            2
            sage: c.count(3)
            0"""
    def index(self, x, start=..., stop=...) -> int:
        """ClonableArray.index(self, x, start=None, stop=None) -> int

        File: /build/sagemath/src/sage/src/sage/structure/list_clone.pyx (starting at line 762)

        Return the smallest ``k`` such that ``s[k] == x`` and ``i <= k < j``

        EXAMPLES::

            sage: from sage.structure.list_clone_demo import IncreasingArrays
            sage: c = IncreasingArrays()([1,2,4])
            sage: c.index(1)
            0
            sage: c.index(4)
            2
            sage: c.index(5)
            Traceback (most recent call last):
            ...
            ValueError: 5 is not in list"""
    def __bool__(self) -> bool:
        """True if self else False"""
    def __contains__(self, item) -> Any:
        """ClonableArray.__contains__(self, item)

        File: /build/sagemath/src/sage/src/sage/structure/list_clone.pyx (starting at line 749)

        EXAMPLES::

            sage: from sage.structure.list_clone_demo import IncreasingArrays
            sage: c = IncreasingArrays()([1,2,4])
            sage: 1 in c
            True
            sage: 5 in c
            False"""
    def __copy__(self) -> ClonableArray:
        """ClonableArray.__copy__(self) -> ClonableArray

        File: /build/sagemath/src/sage/src/sage/structure/list_clone.pyx (starting at line 849)

        Return a copy of ``self``.

        TESTS::

            sage: from sage.structure.list_clone_demo import IncreasingArrays
            sage: el = IncreasingArrays()([1,2,4])
            sage: elc = copy(el)
            sage: el[:] == elc[:]
            True
            sage: el is elc
            False

        We check that empty lists are correctly copied::

            sage: el = IncreasingArrays()([])
            sage: elc = copy(el)
            sage: el is elc
            False
            sage: bool(elc)
            False
            sage: elc.is_mutable()
            True

        We check that element with a ``__dict__`` are correctly copied::

            sage: IL = IncreasingArrays()
            sage: class myClass(IL.element_class): pass
            sage: el = myClass(IL, [])
            sage: el.toto = 2
            sage: elc = copy(el)
            sage: elc.toto
            2"""
    def __delitem__(self, other) -> None:
        """Delete self[key]."""
    def __getitem__(self, key) -> Any:
        """ClonableArray.__getitem__(self, key)

        File: /build/sagemath/src/sage/src/sage/structure/list_clone.pyx (starting at line 627)

        Return the ``key``-th element of ``self``.

        It also works with slice returning a python list in this case.

        EXAMPLES::

            sage: from sage.structure.list_clone_demo import IncreasingArrays
            sage: IncreasingArrays()([1,2,3])[1]
            2
            sage: IncreasingArrays()([1,2,3])[7]
            Traceback (most recent call last):
            ...
            IndexError: list index out of range
            sage: IncreasingArrays()([1,2,3])[-1]
            3
            sage: IncreasingArrays()([1,2,3])[-1:]
            [3]
            sage: IncreasingArrays()([1,2,3])[:]
            [1, 2, 3]
            sage: type(IncreasingArrays()([1,2,3])[:])
            <... 'list'>"""
    def __hash__(self) -> Any:
        """ClonableArray.__hash__(self)

        File: /build/sagemath/src/sage/src/sage/structure/list_clone.pyx (starting at line 803)

        Return the hash value of ``self``.

        TESTS::

            sage: from sage.structure.list_clone_demo import IncreasingArrays
            sage: el = IncreasingArrays()([1,2,3])
            sage: hash(el)    # random
            -309690657
            sage: el1 = copy(el); hash(el1)
            Traceback (most recent call last):
            ...
            ValueError: cannot hash a mutable object."""
    def __iter__(self) -> Any:
        """ClonableArray.__iter__(self)

        File: /build/sagemath/src/sage/src/sage/structure/list_clone.pyx (starting at line 725)

        Return an iterator for ``self``::

        EXAMPLES::

            sage: from sage.structure.list_clone_demo import IncreasingArrays
            sage: el = IncreasingArrays()([1,2,4])
            sage: list(iter(el))
            [1, 2, 4]

        As a consequence ``min``, ``max`` behave properly::

            sage: el = IncreasingArrays()([1,4,8])
            sage: min(el), max(el)
            (1, 8)

        TESTS::

            sage: list(iter(IncreasingArrays()([])))
            []"""
    def __len__(self) -> Any:
        """ClonableArray.__len__(self)

        File: /build/sagemath/src/sage/src/sage/structure/list_clone.pyx (starting at line 615)

        Return the ``len`` of ``self``.

        EXAMPLES::

            sage: from sage.structure.list_clone_demo import IncreasingArrays
            sage: len(IncreasingArrays()([1,2,3]))
            3"""
    @overload
    def __reduce__(self) -> Any:
        """ClonableArray.__reduce__(self)

        File: /build/sagemath/src/sage/src/sage/structure/list_clone.pyx (starting at line 927)

        TESTS::

            sage: from sage.structure.list_clone_demo import IncreasingArrays
            sage: el = IncreasingArrays()([1,2,4])
            sage: loads(dumps(el))
            [1, 2, 4]
            sage: t = el.__reduce__(); t
            (<cyfunction _make_array_clone at ...>,
             (<class 'sage.structure.list_clone_demo.IncreasingArray'>,
              <sage.structure.list_clone_demo.IncreasingArrays_with_category object at ...>,
              [1, 2, 4],
              True,
              True,
              None))
            sage: t[0](*t[1])
            [1, 2, 4]"""
    @overload
    def __reduce__(self) -> Any:
        """ClonableArray.__reduce__(self)

        File: /build/sagemath/src/sage/src/sage/structure/list_clone.pyx (starting at line 927)

        TESTS::

            sage: from sage.structure.list_clone_demo import IncreasingArrays
            sage: el = IncreasingArrays()([1,2,4])
            sage: loads(dumps(el))
            [1, 2, 4]
            sage: t = el.__reduce__(); t
            (<cyfunction _make_array_clone at ...>,
             (<class 'sage.structure.list_clone_demo.IncreasingArray'>,
              <sage.structure.list_clone_demo.IncreasingArrays_with_category object at ...>,
              [1, 2, 4],
              True,
              True,
              None))
            sage: t[0](*t[1])
            [1, 2, 4]"""
    def __setitem__(self, intkey, value) -> Any:
        """ClonableArray.__setitem__(self, int key, value)

        File: /build/sagemath/src/sage/src/sage/structure/list_clone.pyx (starting at line 655)

        Set the ``i``-th element of ``self``.

        An exception is raised if ``self`` is immutable.

        EXAMPLES::

            sage: from sage.structure.list_clone_demo import IncreasingArrays
            sage: el = IncreasingArrays()([1,2,4,10])
            sage: elc = copy(el)
            sage: elc[1] = 3; elc
            [1, 3, 4, 10]
            sage: el[1] = 3
            Traceback (most recent call last):
            ...
            ValueError: object is immutable; please change a copy instead.
            sage: elc[5] = 3
            Traceback (most recent call last):
            ...
            IndexError: list assignment index out of range"""

class ClonableElement(sage.structure.element.Element):
    '''File: /build/sagemath/src/sage/src/sage/structure/list_clone.pyx (starting at line 158)

        Abstract class for elements with clone protocol.

        This class is a subclass of :class:`Element<sage.structure.element.Element>`
        and implements the "prototype" design pattern (see [Prototype_pattern]_, [GHJV1994]_). The role
        of this class is:

        - to manage copy and mutability and hashing of elements
        - to ensure that at the end of a piece of code an object is restored in a
          meaningful mathematical state.

        A class ``C`` inheriting from :class:`ClonableElement` must implement
        the following two methods

        - ``obj.__copy__()`` -- returns a fresh copy of obj
        - ``obj.check()`` -- returns nothing, raise an exception if ``obj``
          doesn\'t satisfy the data structure invariants

        and ensure to call ``obj._require_mutable()`` at the beginning of any
        modifying method.

        Additionally, one can also implement

        - ``obj._hash_()`` -- return the hash value of ``obj``

        Then, given an instance ``obj`` of ``C``, the following sequences of
        instructions ensures that the invariants of ``new_obj`` are properly
        restored at the end::

           with obj.clone() as new_obj:
               ...
               # lot of invariant breaking modifications on new_obj
               ...
           # invariants are ensured to be fulfilled

        The following equivalent sequence of instructions can be used if speed is
        needed, in particular in Cython code::

           new_obj = obj.__copy__()
           ...
           # lot of invariant breaking modifications on new_obj
           ...
           new_obj.set_immutable()
           new_obj.check()
           # invariants are ensured to be fulfilled

        Finally, if the class implements the ``_hash_`` method, then
        :class:`ClonableElement` ensures that the hash value can only be
        computed on an immutable object. It furthermore caches it so that
        it is only computed once.

        .. warning:: for the hash caching mechanism to work correctly, the hash
           value cannot be 0.

        EXAMPLES:

        The following code shows a minimal example of usage of
        :class:`ClonableElement`. We implement a class or pairs `(x,y)`
        such that `x < y`::

            sage: from sage.structure.list_clone import ClonableElement
            sage: class IntPair(ClonableElement):
            ....:      def __init__(self, parent, x, y):
            ....:          ClonableElement.__init__(self, parent=parent)
            ....:          self._x = x
            ....:          self._y = y
            ....:          self.set_immutable()
            ....:          self.check()
            ....:      def _repr_(self):
            ....:          return "(x=%s, y=%s)"%(self._x, self._y)
            ....:      def check(self):
            ....:          if self._x >= self._y:
            ....:              raise ValueError("Incorrectly ordered pair")
            ....:      def get_x(self): return self._x
            ....:      def get_y(self): return self._y
            ....:      def set_x(self, v): self._require_mutable(); self._x = v
            ....:      def set_y(self, v): self._require_mutable(); self._y = v

        .. NOTE:: we don\'t need to define ``__copy__`` since it is properly
           inherited from :class:`Element<sage.structure.element.Element>`.

        We now demonstrate the behavior. Let\'s create an ``IntPair``::

            sage: myParent = Parent()
            sage: el = IntPair(myParent, 1, 3); el
            (x=1, y=3)
            sage: el.get_x()
            1

        Modifying it is forbidden::

            sage: el.set_x(4)
            Traceback (most recent call last):
            ...
            ValueError: object is immutable; please change a copy instead.

        However, you can modify a mutable copy::

            sage: with el.clone() as el1:
            ....:      el1.set_x(2)
            sage: [el, el1]
            [(x=1, y=3), (x=2, y=3)]

        We check that the original and the modified copy are in a proper immutable
        state::

            sage: el.is_immutable(), el1.is_immutable()
            (True, True)
            sage: el1.set_x(4)
            Traceback (most recent call last):
            ...
            ValueError: object is immutable; please change a copy instead.

        A modification which doesn\'t restore the invariant `x < y` at the end is
        illegal and raise an exception::

            sage: with el.clone() as elc2:
            ....:      elc2.set_x(5)
            Traceback (most recent call last):
            ...
            ValueError: Incorrectly ordered pair
    '''
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    @classmethod
    def __init__(cls, *args, **kwargs) -> None:
        """Create and return a new object.  See help(type) for accurate signature."""
    @overload
    def clone(self, boolcheck=...) -> ClonableElement:
        """ClonableElement.clone(self, bool check=True) -> ClonableElement

        File: /build/sagemath/src/sage/src/sage/structure/list_clone.pyx (starting at line 419)

        Return a clone that is mutable copy of ``self``.

        INPUT:

        - ``check`` -- boolean indicating if ``self.check()`` must be called
          after modifications

        EXAMPLES::

            sage: from sage.structure.list_clone_demo import IncreasingArrays
            sage: el = IncreasingArrays()([1,2,3])
            sage: with el.clone() as el1:
            ....:      el1[2] = 5
            sage: el1
            [1, 2, 5]"""
    @overload
    def clone(self) -> Any:
        """ClonableElement.clone(self, bool check=True) -> ClonableElement

        File: /build/sagemath/src/sage/src/sage/structure/list_clone.pyx (starting at line 419)

        Return a clone that is mutable copy of ``self``.

        INPUT:

        - ``check`` -- boolean indicating if ``self.check()`` must be called
          after modifications

        EXAMPLES::

            sage: from sage.structure.list_clone_demo import IncreasingArrays
            sage: el = IncreasingArrays()([1,2,3])
            sage: with el.clone() as el1:
            ....:      el1[2] = 5
            sage: el1
            [1, 2, 5]"""
    @overload
    def is_immutable(self) -> bool:
        """ClonableElement.is_immutable(self) -> bool

        File: /build/sagemath/src/sage/src/sage/structure/list_clone.pyx (starting at line 333)

        Return ``True`` if ``self`` is immutable (cannot be changed)
        and ``False`` if it is not.

        To make ``self`` immutable use ``self.set_immutable()``.

        EXAMPLES::

            sage: from sage.structure.list_clone_demo import IncreasingArrays
            sage: el = IncreasingArrays()([1,2,3])
            sage: el.is_immutable()
            True
            sage: copy(el).is_immutable()
            False
            sage: with el.clone() as el1:
            ....:      print([el.is_immutable(), el1.is_immutable()])
            [True, False]"""
    @overload
    def is_immutable(self) -> Any:
        """ClonableElement.is_immutable(self) -> bool

        File: /build/sagemath/src/sage/src/sage/structure/list_clone.pyx (starting at line 333)

        Return ``True`` if ``self`` is immutable (cannot be changed)
        and ``False`` if it is not.

        To make ``self`` immutable use ``self.set_immutable()``.

        EXAMPLES::

            sage: from sage.structure.list_clone_demo import IncreasingArrays
            sage: el = IncreasingArrays()([1,2,3])
            sage: el.is_immutable()
            True
            sage: copy(el).is_immutable()
            False
            sage: with el.clone() as el1:
            ....:      print([el.is_immutable(), el1.is_immutable()])
            [True, False]"""
    @overload
    def is_immutable(self) -> Any:
        """ClonableElement.is_immutable(self) -> bool

        File: /build/sagemath/src/sage/src/sage/structure/list_clone.pyx (starting at line 333)

        Return ``True`` if ``self`` is immutable (cannot be changed)
        and ``False`` if it is not.

        To make ``self`` immutable use ``self.set_immutable()``.

        EXAMPLES::

            sage: from sage.structure.list_clone_demo import IncreasingArrays
            sage: el = IncreasingArrays()([1,2,3])
            sage: el.is_immutable()
            True
            sage: copy(el).is_immutable()
            False
            sage: with el.clone() as el1:
            ....:      print([el.is_immutable(), el1.is_immutable()])
            [True, False]"""
    @overload
    def is_immutable(self) -> Any:
        """ClonableElement.is_immutable(self) -> bool

        File: /build/sagemath/src/sage/src/sage/structure/list_clone.pyx (starting at line 333)

        Return ``True`` if ``self`` is immutable (cannot be changed)
        and ``False`` if it is not.

        To make ``self`` immutable use ``self.set_immutable()``.

        EXAMPLES::

            sage: from sage.structure.list_clone_demo import IncreasingArrays
            sage: el = IncreasingArrays()([1,2,3])
            sage: el.is_immutable()
            True
            sage: copy(el).is_immutable()
            False
            sage: with el.clone() as el1:
            ....:      print([el.is_immutable(), el1.is_immutable()])
            [True, False]"""
    @overload
    def is_mutable(self) -> bool:
        """ClonableElement.is_mutable(self) -> bool

        File: /build/sagemath/src/sage/src/sage/structure/list_clone.pyx (starting at line 312)

        Return ``True`` if ``self`` is mutable (can be changed) and ``False``
        if it is not.

        To make this object immutable use ``self.set_immutable()``.

        EXAMPLES::

            sage: from sage.structure.list_clone_demo import IncreasingArrays
            sage: el = IncreasingArrays()([1,2,3])
            sage: el.is_mutable()
            False
            sage: copy(el).is_mutable()
            True
            sage: with el.clone() as el1:
            ....:      print([el.is_mutable(), el1.is_mutable()])
            [False, True]"""
    @overload
    def is_mutable(self) -> Any:
        """ClonableElement.is_mutable(self) -> bool

        File: /build/sagemath/src/sage/src/sage/structure/list_clone.pyx (starting at line 312)

        Return ``True`` if ``self`` is mutable (can be changed) and ``False``
        if it is not.

        To make this object immutable use ``self.set_immutable()``.

        EXAMPLES::

            sage: from sage.structure.list_clone_demo import IncreasingArrays
            sage: el = IncreasingArrays()([1,2,3])
            sage: el.is_mutable()
            False
            sage: copy(el).is_mutable()
            True
            sage: with el.clone() as el1:
            ....:      print([el.is_mutable(), el1.is_mutable()])
            [False, True]"""
    @overload
    def is_mutable(self) -> Any:
        """ClonableElement.is_mutable(self) -> bool

        File: /build/sagemath/src/sage/src/sage/structure/list_clone.pyx (starting at line 312)

        Return ``True`` if ``self`` is mutable (can be changed) and ``False``
        if it is not.

        To make this object immutable use ``self.set_immutable()``.

        EXAMPLES::

            sage: from sage.structure.list_clone_demo import IncreasingArrays
            sage: el = IncreasingArrays()([1,2,3])
            sage: el.is_mutable()
            False
            sage: copy(el).is_mutable()
            True
            sage: with el.clone() as el1:
            ....:      print([el.is_mutable(), el1.is_mutable()])
            [False, True]"""
    @overload
    def is_mutable(self) -> Any:
        """ClonableElement.is_mutable(self) -> bool

        File: /build/sagemath/src/sage/src/sage/structure/list_clone.pyx (starting at line 312)

        Return ``True`` if ``self`` is mutable (can be changed) and ``False``
        if it is not.

        To make this object immutable use ``self.set_immutable()``.

        EXAMPLES::

            sage: from sage.structure.list_clone_demo import IncreasingArrays
            sage: el = IncreasingArrays()([1,2,3])
            sage: el.is_mutable()
            False
            sage: copy(el).is_mutable()
            True
            sage: with el.clone() as el1:
            ....:      print([el.is_mutable(), el1.is_mutable()])
            [False, True]"""
    @overload
    def set_immutable(self) -> Any:
        """ClonableElement.set_immutable(self)

        File: /build/sagemath/src/sage/src/sage/structure/list_clone.pyx (starting at line 354)

        Makes ``self`` immutable, so it can never again be changed.

        EXAMPLES::

            sage: from sage.structure.list_clone_demo import IncreasingArrays
            sage: el = IncreasingArrays()([1,2,3])
            sage: el1 = copy(el); el1.is_mutable()
            True
            sage: el1.set_immutable();  el1.is_mutable()
            False
            sage: el1[2] = 4
            Traceback (most recent call last):
            ...
            ValueError: object is immutable; please change a copy instead."""
    @overload
    def set_immutable(self) -> Any:
        """ClonableElement.set_immutable(self)

        File: /build/sagemath/src/sage/src/sage/structure/list_clone.pyx (starting at line 354)

        Makes ``self`` immutable, so it can never again be changed.

        EXAMPLES::

            sage: from sage.structure.list_clone_demo import IncreasingArrays
            sage: el = IncreasingArrays()([1,2,3])
            sage: el1 = copy(el); el1.is_mutable()
            True
            sage: el1.set_immutable();  el1.is_mutable()
            False
            sage: el1[2] = 4
            Traceback (most recent call last):
            ...
            ValueError: object is immutable; please change a copy instead."""
    @overload
    def __enter__(self) -> Any:
        """ClonableElement.__enter__(self)

        File: /build/sagemath/src/sage/src/sage/structure/list_clone.pyx (starting at line 442)

        Implement the ``self`` guarding clone protocol.

        TESTS::

            sage: from sage.structure.list_clone_demo import IncreasingArrays
            sage: el = IncreasingArrays()([1,2,3])
            sage: el.clone().__enter__()
            [1, 2, 3]"""
    @overload
    def __enter__(self) -> Any:
        """ClonableElement.__enter__(self)

        File: /build/sagemath/src/sage/src/sage/structure/list_clone.pyx (starting at line 442)

        Implement the ``self`` guarding clone protocol.

        TESTS::

            sage: from sage.structure.list_clone_demo import IncreasingArrays
            sage: el = IncreasingArrays()([1,2,3])
            sage: el.clone().__enter__()
            [1, 2, 3]"""
    def __exit__(self, typ, value, tracback) -> Any:
        """ClonableElement.__exit__(self, typ, value, tracback)

        File: /build/sagemath/src/sage/src/sage/structure/list_clone.pyx (starting at line 456)

        Implement the ``self`` guarding clone protocol.

        .. NOTE:: The input argument are required by the ``with`` protocol but
           are ignored.

        TESTS::

            sage: from sage.structure.list_clone_demo import IncreasingArrays
            sage: el = IncreasingArrays()([1,2,3])
            sage: el1 = el.clone().__enter__()
            sage: el1.__exit__(None, None, None)
            False

        Lets try to make a broken list::

            sage: elc2 = el.clone().__enter__()
            sage: elc2[1] = 7
            sage: elc2.__exit__(None, None, None)
            Traceback (most recent call last):
            ...
            ValueError: array is not increasing"""
    def __hash__(self) -> Any:
        """ClonableElement.__hash__(self)

        File: /build/sagemath/src/sage/src/sage/structure/list_clone.pyx (starting at line 397)

        Return the hash value of ``self``.

        TESTS::

            sage: from sage.structure.list_clone_demo import IncreasingArrays
            sage: el = IncreasingArrays()([1,2,3])
            sage: hash(el)    # random
            -309690657
            sage: el1 = copy(el); hash(el1)
            Traceback (most recent call last):
            ...
            ValueError: cannot hash a mutable object."""

class ClonableIntArray(ClonableElement):
    """ClonableIntArray(Parent parent, lst, check=True, immutable=True)

    File: /build/sagemath/src/sage/src/sage/structure/list_clone.pyx (starting at line 1225)

    Array of integers with clone protocol.

    The class of objects which are
    :class:`Element<sage.structure.element.Element>` behave as list of int and
    implement the clone protocol. See :class:`ClonableElement` for details
    about clone protocol.


    INPUT:

    - ``parent`` -- a :class:`Parent<sage.structure.parent.Parent>`
    - ``lst`` -- list
    - ``check`` -- boolean specifying if the invariant must be checked
      using method :meth:`check`
    - ``immutable`` -- boolean (default: ``True``); whether the created element
      is immutable

    .. SEEALSO:: :class:`~sage.structure.list_clone_demo.IncreasingIntArray`
                 for an example of usage."""
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    def __init__(self, Parentparent, lst, check=..., immutable=...) -> Any:
        """File: /build/sagemath/src/sage/src/sage/structure/list_clone.pyx (starting at line 1251)

                Initialize ``self``.

                TESTS::

                    sage: from sage.structure.list_clone_demo import IncreasingIntArrays
                    sage: IncreasingIntArrays()([1,2,3])
                    [1, 2, 3]
                    sage: IncreasingIntArrays()((1,2,3))
                    [1, 2, 3]

                    sage: IncreasingIntArrays()(None)
                    Traceback (most recent call last):
                    ...
                    TypeError: object of type 'NoneType' has no len()

                    sage: el = IncreasingIntArrays()([3,2,1])
                    Traceback (most recent call last):
                    ...
                    ValueError: array is not increasing

                    sage: el = IncreasingIntArrays()([1,2,4])
                    sage: list(iter(el))
                    [1, 2, 4]
                    sage: list(iter(IncreasingIntArrays()([])))
                    []

                You are not supposed to do the following (giving a wrong list and
                desactivating checks)::

                    sage: broken = IncreasingIntArrays()([3,2,1], False)
        """
    def check(self) -> Any:
        """ClonableIntArray.check(self)

        File: /build/sagemath/src/sage/src/sage/structure/list_clone.pyx (starting at line 1684)

        Check that ``self`` fulfill the invariants.

        This is an abstract method. Subclasses are supposed to overload
        ``check``.

        EXAMPLES::

            sage: from sage.structure.list_clone import ClonableArray
            sage: ClonableArray(Parent(), [1,2,3]) # indirect doctest
            Traceback (most recent call last):
            ...
            NotImplementedError: this should never be called, please overload the check method
            sage: from sage.structure.list_clone_demo import IncreasingIntArrays
            sage: el = IncreasingIntArrays()([1,2,4]) # indirect doctest"""
    @overload
    def index(self, intitem) -> int:
        """ClonableIntArray.index(self, int item) -> int

        File: /build/sagemath/src/sage/src/sage/structure/list_clone.pyx (starting at line 1543)

        EXAMPLES::

            sage: from sage.structure.list_clone_demo import IncreasingIntArrays
            sage: c = IncreasingIntArrays()([1,2,4])
            sage: c.index(1)
            0
            sage: c.index(4)
            2
            sage: c.index(5)
            Traceback (most recent call last):
            ...
            ValueError: list.index(x): x not in list"""
    @overload
    def index(self, x) -> Any:
        """ClonableIntArray.index(self, int item) -> int

        File: /build/sagemath/src/sage/src/sage/structure/list_clone.pyx (starting at line 1543)

        EXAMPLES::

            sage: from sage.structure.list_clone_demo import IncreasingIntArrays
            sage: c = IncreasingIntArrays()([1,2,4])
            sage: c.index(1)
            0
            sage: c.index(4)
            2
            sage: c.index(5)
            Traceback (most recent call last):
            ...
            ValueError: list.index(x): x not in list"""
    def list(self) -> list:
        """ClonableIntArray.list(self) -> list

        File: /build/sagemath/src/sage/src/sage/structure/list_clone.pyx (starting at line 1385)

        Convert ``self`` into a Python list.

        EXAMPLES::

            sage: from sage.structure.list_clone_demo import IncreasingIntArrays
            sage: I = IncreasingIntArrays()(range(5))
            sage: I == list(range(5))
            False
            sage: I.list() == list(range(5))
            True
            sage: I = IncreasingIntArrays()(range(1000))
            sage: I.list() == list(range(1000))
            True"""
    def __bool__(self) -> bool:
        """True if self else False"""
    def __contains__(self, intitem) -> Any:
        """ClonableIntArray.__contains__(self, int item)

        File: /build/sagemath/src/sage/src/sage/structure/list_clone.pyx (starting at line 1526)

        EXAMPLES::

            sage: from sage.structure.list_clone_demo import IncreasingIntArrays
            sage: c = IncreasingIntArrays()([1,2,4])
            sage: 1 in c
            True
            sage: 5 in c
            False"""
    def __copy__(self) -> ClonableIntArray:
        """ClonableIntArray.__copy__(self) -> ClonableIntArray

        File: /build/sagemath/src/sage/src/sage/structure/list_clone.pyx (starting at line 1637)

        Return a copy of ``self``.

        TESTS::

            sage: from sage.structure.list_clone_demo import IncreasingIntArrays
            sage: el = IncreasingIntArrays()([1,2,4])
            sage: elc = copy(el)
            sage: el[:] == elc[:]
            True
            sage: el is elc
            False

        We check that void lists are correctly copied::

            sage: el = IncreasingIntArrays()([])
            sage: elc = copy(el)
            sage: el is elc
            False
            sage: bool(elc)
            True
            sage: elc.is_mutable()
            True

        We check that element with a ``__dict__`` are correctly copied::

            sage: IL = IncreasingIntArrays()
            sage: class myClass(IL.element_class): pass
            sage: el = myClass(IL, [])
            sage: el.toto = 2
            sage: elc = copy(el)
            sage: elc.toto
            2"""
    def __delitem__(self, other) -> None:
        """Delete self[key]."""
    def __getitem__(self, key) -> Any:
        """ClonableIntArray.__getitem__(self, key)

        File: /build/sagemath/src/sage/src/sage/structure/list_clone.pyx (starting at line 1410)

        Return the i-th element of ``self``.

        EXAMPLES::

            sage: from sage.structure.list_clone_demo import IncreasingIntArrays
            sage: el = IncreasingIntArrays()([1,2,3])
            sage: el[1]
            2
            sage: el[1:2]
            [2]
            sage: el[4]
            Traceback (most recent call last):
            ...
            IndexError: list index out of range
            sage: el[-1]
            3
            sage: el[-1:]
            [3]
            sage: el[:]
            [1, 2, 3]
            sage: el[1:3]
            [2, 3]
            sage: type(el[:])
            <... 'list'>
            sage: list(el)
            [1, 2, 3]
            sage: it = iter(el); next(it), next(it)
            (1, 2)"""
    def __hash__(self) -> Any:
        """ClonableIntArray.__hash__(self)

        File: /build/sagemath/src/sage/src/sage/structure/list_clone.pyx (starting at line 1566)

        Return the hash value of ``self``.

        TESTS::

            sage: from sage.structure.list_clone_demo import IncreasingIntArrays
            sage: el = IncreasingIntArrays()([1,2,3])
            sage: hash(el)    # random
            -309690657
            sage: el1 = copy(el); hash(el1)
            Traceback (most recent call last):
            ...
            ValueError: cannot hash a mutable object."""
    def __iter__(self) -> Any:
        """ClonableIntArray.__iter__(self)

        File: /build/sagemath/src/sage/src/sage/structure/list_clone.pyx (starting at line 1370)

        Iterate over the items of ``self``.

        EXAMPLES::

            sage: from sage.structure.list_clone_demo import IncreasingIntArrays
            sage: I = IncreasingIntArrays()(range(5))
            sage: I == list(range(5))
            False
            sage: list(I) == list(range(5))  # indirect doctest
            True"""
    def __len__(self) -> Any:
        """ClonableIntArray.__len__(self)

        File: /build/sagemath/src/sage/src/sage/structure/list_clone.pyx (starting at line 1358)

        Return the len of ``self``.

        EXAMPLES::

            sage: from sage.structure.list_clone_demo import IncreasingIntArrays
            sage: len(IncreasingIntArrays()([1,2,3]))
            3"""
    @overload
    def __reduce__(self) -> Any:
        """ClonableIntArray.__reduce__(self)

        File: /build/sagemath/src/sage/src/sage/structure/list_clone.pyx (starting at line 1723)

        TESTS::

            sage: from sage.structure.list_clone_demo import IncreasingIntArrays
            sage: el = IncreasingIntArrays()([1,2,4])
            sage: loads(dumps(el))
            [1, 2, 4]
            sage: t = el.__reduce__(); t
            (<cyfunction _make_int_array_clone at ...>,
             (<class 'sage.structure.list_clone_demo.IncreasingIntArray'>,
              <sage.structure.list_clone_demo.IncreasingIntArrays_with_category object at ...>,
              [1, 2, 4],
              True,
              True,
              None))
            sage: t[0](*t[1])
            [1, 2, 4]"""
    @overload
    def __reduce__(self) -> Any:
        """ClonableIntArray.__reduce__(self)

        File: /build/sagemath/src/sage/src/sage/structure/list_clone.pyx (starting at line 1723)

        TESTS::

            sage: from sage.structure.list_clone_demo import IncreasingIntArrays
            sage: el = IncreasingIntArrays()([1,2,4])
            sage: loads(dumps(el))
            [1, 2, 4]
            sage: t = el.__reduce__(); t
            (<cyfunction _make_int_array_clone at ...>,
             (<class 'sage.structure.list_clone_demo.IncreasingIntArray'>,
              <sage.structure.list_clone_demo.IncreasingIntArrays_with_category object at ...>,
              [1, 2, 4],
              True,
              True,
              None))
            sage: t[0](*t[1])
            [1, 2, 4]"""
    def __setitem__(self, intkey, value) -> Any:
        """ClonableIntArray.__setitem__(self, int key, value)

        File: /build/sagemath/src/sage/src/sage/structure/list_clone.pyx (starting at line 1459)

        Set the i-th element of ``self``.

        An exception is raised if ``self`` is immutable.

        EXAMPLES::

            sage: from sage.structure.list_clone_demo import IncreasingIntArrays
            sage: el = IncreasingIntArrays()([1,2,4])
            sage: elc = copy(el)
            sage: elc[1] = 3; elc
            [1, 3, 4]
            sage: el[1] = 3
            Traceback (most recent call last):
            ...
            ValueError: object is immutable; please change a copy instead."""

class ClonableList(ClonableArray):
    """File: /build/sagemath/src/sage/src/sage/structure/list_clone.pyx (starting at line 998)

        List with clone protocol.

        The class of objects which are
        :class:`Element<sage.structure.element.Element>` behave as lists and
        implement the clone protocol. See :class:`ClonableElement` for details
        about clone protocol.

        .. SEEALSO:: :class:`~sage.structure.list_clone_demo.IncreasingList` for
                     an example of usage.
    """
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    @classmethod
    def __init__(cls, *args, **kwargs) -> None:
        """Create and return a new object.  See help(type) for accurate signature."""
    def append(self, el) -> Any:
        """ClonableList.append(self, el)

        File: /build/sagemath/src/sage/src/sage/structure/list_clone.pyx (starting at line 1010)

        Appends ``el`` to ``self``.

        INPUT:

        - ``el`` -- any object

        EXAMPLES::

            sage: from sage.structure.list_clone_demo import IncreasingLists
            sage: el = IncreasingLists()([1])
            sage: el.append(3)
            Traceback (most recent call last):
            ...
            ValueError: object is immutable; please change a copy instead.
            sage: with el.clone() as elc:
            ....:      elc.append(4)
            ....:      elc.append(6)
            sage: elc
            [1, 4, 6]
            sage: with el.clone() as elc:
            ....:      elc.append(4)
            ....:      elc.append(2)
            Traceback (most recent call last):
            ...
            ValueError: array is not increasing"""
    @overload
    def extend(self, it) -> Any:
        """ClonableList.extend(self, it)

        File: /build/sagemath/src/sage/src/sage/structure/list_clone.pyx (starting at line 1041)

        Extend ``self`` by the content of the iterable ``it``.

        INPUT:

        - ``it`` -- any iterable

        EXAMPLES::

            sage: from sage.structure.list_clone_demo import IncreasingLists
            sage: el = IncreasingLists()([1, 4, 5, 8, 9])
            sage: el.extend((10,11))
            Traceback (most recent call last):
            ...
            ValueError: object is immutable; please change a copy instead.

            sage: with el.clone() as elc:
            ....:      elc.extend((10,11))
            sage: elc
            [1, 4, 5, 8, 9, 10, 11]

            sage: el2 = IncreasingLists()([15, 16])
            sage: with el.clone() as elc:
            ....:      elc.extend(el2)
            sage: elc
            [1, 4, 5, 8, 9, 15, 16]

            sage: with el.clone() as elc:
            ....:      elc.extend((6,7))
            Traceback (most recent call last):
            ...
            ValueError: array is not increasing"""
    @overload
    def extend(self, el2) -> Any:
        """ClonableList.extend(self, it)

        File: /build/sagemath/src/sage/src/sage/structure/list_clone.pyx (starting at line 1041)

        Extend ``self`` by the content of the iterable ``it``.

        INPUT:

        - ``it`` -- any iterable

        EXAMPLES::

            sage: from sage.structure.list_clone_demo import IncreasingLists
            sage: el = IncreasingLists()([1, 4, 5, 8, 9])
            sage: el.extend((10,11))
            Traceback (most recent call last):
            ...
            ValueError: object is immutable; please change a copy instead.

            sage: with el.clone() as elc:
            ....:      elc.extend((10,11))
            sage: elc
            [1, 4, 5, 8, 9, 10, 11]

            sage: el2 = IncreasingLists()([15, 16])
            sage: with el.clone() as elc:
            ....:      elc.extend(el2)
            sage: elc
            [1, 4, 5, 8, 9, 15, 16]

            sage: with el.clone() as elc:
            ....:      elc.extend((6,7))
            Traceback (most recent call last):
            ...
            ValueError: array is not increasing"""
    def insert(self, intindex, el) -> Any:
        """ClonableList.insert(self, int index, el)

        File: /build/sagemath/src/sage/src/sage/structure/list_clone.pyx (starting at line 1078)

        Inserts ``el`` in ``self`` at position ``index``.

        INPUT:

        - ``el`` -- any object
        - ``index`` -- any int

        EXAMPLES::

            sage: from sage.structure.list_clone_demo import IncreasingLists
            sage: el = IncreasingLists()([1, 4, 5, 8, 9])
            sage: el.insert(3, 6)
            Traceback (most recent call last):
            ...
            ValueError: object is immutable; please change a copy instead.
            sage: with el.clone() as elc:
            ....:      elc.insert(3, 6)
            sage: elc
            [1, 4, 5, 6, 8, 9]
            sage: with el.clone() as elc:
            ....:      elc.insert(2, 6)
            Traceback (most recent call last):
            ...
            ValueError: array is not increasing"""
    @overload
    def pop(self, intindex=...) -> Any:
        """ClonableList.pop(self, int index=-1)

        File: /build/sagemath/src/sage/src/sage/structure/list_clone.pyx (starting at line 1108)

        Remove ``self[index]`` from ``self`` and returns it.

        INPUT:

        - ``index`` -- integer (default: -1)

        EXAMPLES::

            sage: from sage.structure.list_clone_demo import IncreasingLists
            sage: el = IncreasingLists()([1, 4, 5, 8, 9])
            sage: el.pop()
            Traceback (most recent call last):
            ...
            ValueError: object is immutable; please change a copy instead.
            sage: with el.clone() as elc:
            ....:      print(elc.pop())
            9
            sage: elc
            [1, 4, 5, 8]
            sage: with el.clone() as elc:
            ....:      print(elc.pop(2))
            5
            sage: elc
            [1, 4, 8, 9]"""
    @overload
    def pop(self) -> Any:
        """ClonableList.pop(self, int index=-1)

        File: /build/sagemath/src/sage/src/sage/structure/list_clone.pyx (starting at line 1108)

        Remove ``self[index]`` from ``self`` and returns it.

        INPUT:

        - ``index`` -- integer (default: -1)

        EXAMPLES::

            sage: from sage.structure.list_clone_demo import IncreasingLists
            sage: el = IncreasingLists()([1, 4, 5, 8, 9])
            sage: el.pop()
            Traceback (most recent call last):
            ...
            ValueError: object is immutable; please change a copy instead.
            sage: with el.clone() as elc:
            ....:      print(elc.pop())
            9
            sage: elc
            [1, 4, 5, 8]
            sage: with el.clone() as elc:
            ....:      print(elc.pop(2))
            5
            sage: elc
            [1, 4, 8, 9]"""
    @overload
    def pop(self) -> Any:
        """ClonableList.pop(self, int index=-1)

        File: /build/sagemath/src/sage/src/sage/structure/list_clone.pyx (starting at line 1108)

        Remove ``self[index]`` from ``self`` and returns it.

        INPUT:

        - ``index`` -- integer (default: -1)

        EXAMPLES::

            sage: from sage.structure.list_clone_demo import IncreasingLists
            sage: el = IncreasingLists()([1, 4, 5, 8, 9])
            sage: el.pop()
            Traceback (most recent call last):
            ...
            ValueError: object is immutable; please change a copy instead.
            sage: with el.clone() as elc:
            ....:      print(elc.pop())
            9
            sage: elc
            [1, 4, 5, 8]
            sage: with el.clone() as elc:
            ....:      print(elc.pop(2))
            5
            sage: elc
            [1, 4, 8, 9]"""
    @overload
    def remove(self, el) -> Any:
        """ClonableList.remove(self, el)

        File: /build/sagemath/src/sage/src/sage/structure/list_clone.pyx (starting at line 1138)

        Remove the first occurrence of ``el`` from ``self``.

        INPUT:

        - ``el`` -- any object

        EXAMPLES::

            sage: from sage.structure.list_clone_demo import IncreasingLists
            sage: el = IncreasingLists()([1, 4, 5, 8, 9])
            sage: el.remove(4)
            Traceback (most recent call last):
            ...
            ValueError: object is immutable; please change a copy instead.
            sage: with el.clone() as elc:
            ....:      elc.remove(4)
            sage: elc
            [1, 5, 8, 9]
            sage: with el.clone() as elc:
            ....:      elc.remove(10)
            Traceback (most recent call last):
            ...
            ValueError: list.remove(x): x not in list"""
    @overload
    def remove(self, x) -> Any:
        """ClonableList.remove(self, el)

        File: /build/sagemath/src/sage/src/sage/structure/list_clone.pyx (starting at line 1138)

        Remove the first occurrence of ``el`` from ``self``.

        INPUT:

        - ``el`` -- any object

        EXAMPLES::

            sage: from sage.structure.list_clone_demo import IncreasingLists
            sage: el = IncreasingLists()([1, 4, 5, 8, 9])
            sage: el.remove(4)
            Traceback (most recent call last):
            ...
            ValueError: object is immutable; please change a copy instead.
            sage: with el.clone() as elc:
            ....:      elc.remove(4)
            sage: elc
            [1, 5, 8, 9]
            sage: with el.clone() as elc:
            ....:      elc.remove(10)
            Traceback (most recent call last):
            ...
            ValueError: list.remove(x): x not in list"""
    def __delitem__(self, key) -> Any:
        """ClonableList.__delitem__(self, key)

        File: /build/sagemath/src/sage/src/sage/structure/list_clone.pyx (starting at line 1195)

        Remove the i-th element of ``self``.

        An exception is raised if ``self`` is immutable.

        EXAMPLES::

            sage: from sage.structure.list_clone_demo import IncreasingLists
            sage: el = IncreasingLists()([1, 4, 5, 8, 9])
            sage: del el[3]
            Traceback (most recent call last):
            ...
            ValueError: object is immutable; please change a copy instead.
            sage: with el.clone() as elc:
            ....:      del elc[3]
            sage: elc
            [1, 4, 5, 9]
            sage: with el.clone() as elc:
            ....:      del elc[1:3]
            sage: elc
            [1, 8, 9]"""
    def __setitem__(self, key, value) -> Any:
        """ClonableList.__setitem__(self, key, value)

        File: /build/sagemath/src/sage/src/sage/structure/list_clone.pyx (starting at line 1167)

        Set the i-th element of ``self``.

        An exception is raised if ``self`` is immutable.

        EXAMPLES::

            sage: from sage.structure.list_clone_demo import IncreasingLists
            sage: el = IncreasingLists()([1,2,4,10,15,17])
            sage: el[1] = 3
            Traceback (most recent call last):
            ...
            ValueError: object is immutable; please change a copy instead.

            sage: with el.clone() as elc:
            ....:      elc[3] = 7
            sage: elc
            [1, 2, 4, 7, 15, 17]

            sage: with el.clone(check=False) as elc:
            ....:      elc[1:3]  = [3,5,6,8]
            sage: elc
            [1, 3, 5, 6, 8, 10, 15, 17]"""

class NormalizedClonableList(ClonableList):
    """NormalizedClonableList(Parent parent, lst, check=True, immutable=True)

    File: /build/sagemath/src/sage/src/sage/structure/list_clone.pyx (starting at line 1788)

    List with clone protocol and normal form.

    This is a subclass of :class:`ClonableList` which call a method
    :meth:`normalize` at creation and after any modification of its instance.

    .. SEEALSO:: :class:`~sage.structure.list_clone_demo.SortedList` for an
                 example of usage.

    EXAMPLES:

    We construct a sorted list through its parent::

        sage: from sage.structure.list_clone_demo import SortedLists
        sage: SL = SortedLists()
        sage: sl1 = SL([4,2,6,1]); sl1
        [1, 2, 4, 6]

    Normalization is also performed atfer modification::

        sage: with sl1.clone() as sl2:
        ....:      sl2[1] = 12
        sage: sl2
        [1, 4, 6, 12]"""
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    def __init__(self, Parentparent, lst, check=..., immutable=...) -> Any:
        """File: /build/sagemath/src/sage/src/sage/structure/list_clone.pyx (starting at line 1814)

                TESTS::

                    sage: from sage.structure.list_clone_demo import SortedList, SortedLists
                    sage: SortedList(SortedLists(), [2,3,1])
                    [1, 2, 3]
        """
    @overload
    def normalize(self) -> Any:
        """NormalizedClonableList.normalize(self)

        File: /build/sagemath/src/sage/src/sage/structure/list_clone.pyx (starting at line 1845)

        Normalize ``self``.

        This is an abstract method. Subclasses are supposed to overload
        :meth:`normalize`. The call ``self.normalize()`` is supposed to

        - call ``self._require_mutable()`` to check that ``self`` is in a
          proper mutable state
        - modify ``self`` to put it in a normal form

        EXAMPLES::

            sage: from sage.structure.list_clone_demo import SortedList, SortedLists
            sage: l = SortedList(SortedLists(), [2,3,2], False, False)
            sage: l
            [2, 2, 3]
            sage: l.check()
            Traceback (most recent call last):
            ...
            ValueError: list is not strictly increasing"""
    @overload
    def normalize(self) -> Any:
        """NormalizedClonableList.normalize(self)

        File: /build/sagemath/src/sage/src/sage/structure/list_clone.pyx (starting at line 1845)

        Normalize ``self``.

        This is an abstract method. Subclasses are supposed to overload
        :meth:`normalize`. The call ``self.normalize()`` is supposed to

        - call ``self._require_mutable()`` to check that ``self`` is in a
          proper mutable state
        - modify ``self`` to put it in a normal form

        EXAMPLES::

            sage: from sage.structure.list_clone_demo import SortedList, SortedLists
            sage: l = SortedList(SortedLists(), [2,3,2], False, False)
            sage: l
            [2, 2, 3]
            sage: l.check()
            Traceback (most recent call last):
            ...
            ValueError: list is not strictly increasing"""
    def __exit__(self, typ, value, tracback) -> Any:
        """NormalizedClonableList.__exit__(self, typ, value, tracback)

        File: /build/sagemath/src/sage/src/sage/structure/list_clone.pyx (starting at line 1828)

        TESTS::

            sage: from sage.structure.list_clone_demo import SortedList, SortedLists
            sage: l = SortedList(SortedLists(), [2,3,1], immutable=False); l
            [1, 2, 3]
            sage: l[1] = 5; l
            [1, 5, 3]
            sage: l.__exit__(None, None, None)
            False
            sage: l
            [1, 3, 5]"""
