from sage.cpython.string import bytes_to_str as bytes_to_str, str_to_bytes as str_to_bytes
from sage.misc.prandom import shuffle as shuffle
from typing import Any, ClassVar, overload

class PairingHeap_class:
    """File: /build/sagemath/src/sage/src/sage/data_structures/pairing_heap.pyx (starting at line 110)

        Common class and methods for :class:`PairingHeap_of_n_integers` and
        :class:`PairingHeap_of_n_hashables`.
    """
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    @classmethod
    def __init__(cls, *args, **kwargs) -> None:
        """Create and return a new object.  See help(type) for accurate signature."""
    @overload
    def capacity(self) -> size_t:
        """PairingHeap_class.capacity(self) -> size_t

        File: /build/sagemath/src/sage/src/sage/data_structures/pairing_heap.pyx (starting at line 180)

        Return the maximum capacity of the heap.

        EXAMPLES::

            sage: from sage.data_structures.pairing_heap import PairingHeap_of_n_integers
            sage: P = PairingHeap_of_n_integers(5)
            sage: P.capacity()
            5
            sage: P.push(1, 2)
            sage: P.capacity()
            5"""
    @overload
    def capacity(self) -> Any:
        """PairingHeap_class.capacity(self) -> size_t

        File: /build/sagemath/src/sage/src/sage/data_structures/pairing_heap.pyx (starting at line 180)

        Return the maximum capacity of the heap.

        EXAMPLES::

            sage: from sage.data_structures.pairing_heap import PairingHeap_of_n_integers
            sage: P = PairingHeap_of_n_integers(5)
            sage: P.capacity()
            5
            sage: P.push(1, 2)
            sage: P.capacity()
            5"""
    @overload
    def capacity(self) -> Any:
        """PairingHeap_class.capacity(self) -> size_t

        File: /build/sagemath/src/sage/src/sage/data_structures/pairing_heap.pyx (starting at line 180)

        Return the maximum capacity of the heap.

        EXAMPLES::

            sage: from sage.data_structures.pairing_heap import PairingHeap_of_n_integers
            sage: P = PairingHeap_of_n_integers(5)
            sage: P.capacity()
            5
            sage: P.push(1, 2)
            sage: P.capacity()
            5"""
    @overload
    def empty(self) -> bool:
        """PairingHeap_class.empty(self) -> bool

        File: /build/sagemath/src/sage/src/sage/data_structures/pairing_heap.pyx (starting at line 147)

        Check whether the heap is empty.

        EXAMPLES::

            sage: from sage.data_structures.pairing_heap import PairingHeap_of_n_integers
            sage: P = PairingHeap_of_n_integers(5)
            sage: P.empty()
            True
            sage: P.push(1, 2)
            sage: P.empty()
            False"""
    @overload
    def empty(self) -> Any:
        """PairingHeap_class.empty(self) -> bool

        File: /build/sagemath/src/sage/src/sage/data_structures/pairing_heap.pyx (starting at line 147)

        Check whether the heap is empty.

        EXAMPLES::

            sage: from sage.data_structures.pairing_heap import PairingHeap_of_n_integers
            sage: P = PairingHeap_of_n_integers(5)
            sage: P.empty()
            True
            sage: P.push(1, 2)
            sage: P.empty()
            False"""
    @overload
    def empty(self) -> Any:
        """PairingHeap_class.empty(self) -> bool

        File: /build/sagemath/src/sage/src/sage/data_structures/pairing_heap.pyx (starting at line 147)

        Check whether the heap is empty.

        EXAMPLES::

            sage: from sage.data_structures.pairing_heap import PairingHeap_of_n_integers
            sage: P = PairingHeap_of_n_integers(5)
            sage: P.empty()
            True
            sage: P.push(1, 2)
            sage: P.empty()
            False"""
    @overload
    def full(self) -> bool:
        """PairingHeap_class.full(self) -> bool

        File: /build/sagemath/src/sage/src/sage/data_structures/pairing_heap.pyx (starting at line 163)

        Check whether the heap is full.

        EXAMPLES::

            sage: from sage.data_structures.pairing_heap import PairingHeap_of_n_integers
            sage: P = PairingHeap_of_n_integers(2)
            sage: P.full()
            False
            sage: P.push(0, 2)
            sage: P.push(1, 3)
            sage: P.full()
            True"""
    @overload
    def full(self) -> Any:
        """PairingHeap_class.full(self) -> bool

        File: /build/sagemath/src/sage/src/sage/data_structures/pairing_heap.pyx (starting at line 163)

        Check whether the heap is full.

        EXAMPLES::

            sage: from sage.data_structures.pairing_heap import PairingHeap_of_n_integers
            sage: P = PairingHeap_of_n_integers(2)
            sage: P.full()
            False
            sage: P.push(0, 2)
            sage: P.push(1, 3)
            sage: P.full()
            True"""
    @overload
    def full(self) -> Any:
        """PairingHeap_class.full(self) -> bool

        File: /build/sagemath/src/sage/src/sage/data_structures/pairing_heap.pyx (starting at line 163)

        Check whether the heap is full.

        EXAMPLES::

            sage: from sage.data_structures.pairing_heap import PairingHeap_of_n_integers
            sage: P = PairingHeap_of_n_integers(2)
            sage: P.full()
            False
            sage: P.push(0, 2)
            sage: P.push(1, 3)
            sage: P.full()
            True"""
    @overload
    def pop(self) -> void:
        """PairingHeap_class.pop(self) -> void

        File: /build/sagemath/src/sage/src/sage/data_structures/pairing_heap.pyx (starting at line 280)

        Remove the top item from the heap.

        If the heap is already empty, we do nothing.

        EXAMPLES::

            sage: from sage.data_structures.pairing_heap import PairingHeap_of_n_integers
            sage: P = PairingHeap_of_n_integers(5); P
            PairingHeap_of_n_integers: capacity 5, size 0
            sage: P.push(1, 2); P
            PairingHeap_of_n_integers: capacity 5, size 1
            sage: P.pop(); P
            PairingHeap_of_n_integers: capacity 5, size 0
            sage: P.pop(); P
            PairingHeap_of_n_integers: capacity 5, size 0"""
    @overload
    def pop(self) -> Any:
        """PairingHeap_class.pop(self) -> void

        File: /build/sagemath/src/sage/src/sage/data_structures/pairing_heap.pyx (starting at line 280)

        Remove the top item from the heap.

        If the heap is already empty, we do nothing.

        EXAMPLES::

            sage: from sage.data_structures.pairing_heap import PairingHeap_of_n_integers
            sage: P = PairingHeap_of_n_integers(5); P
            PairingHeap_of_n_integers: capacity 5, size 0
            sage: P.push(1, 2); P
            PairingHeap_of_n_integers: capacity 5, size 1
            sage: P.pop(); P
            PairingHeap_of_n_integers: capacity 5, size 0
            sage: P.pop(); P
            PairingHeap_of_n_integers: capacity 5, size 0"""
    @overload
    def pop(self) -> Any:
        """PairingHeap_class.pop(self) -> void

        File: /build/sagemath/src/sage/src/sage/data_structures/pairing_heap.pyx (starting at line 280)

        Remove the top item from the heap.

        If the heap is already empty, we do nothing.

        EXAMPLES::

            sage: from sage.data_structures.pairing_heap import PairingHeap_of_n_integers
            sage: P = PairingHeap_of_n_integers(5); P
            PairingHeap_of_n_integers: capacity 5, size 0
            sage: P.push(1, 2); P
            PairingHeap_of_n_integers: capacity 5, size 1
            sage: P.pop(); P
            PairingHeap_of_n_integers: capacity 5, size 0
            sage: P.pop(); P
            PairingHeap_of_n_integers: capacity 5, size 0"""
    @overload
    def size(self) -> size_t:
        """PairingHeap_class.size(self) -> size_t

        File: /build/sagemath/src/sage/src/sage/data_structures/pairing_heap.pyx (starting at line 196)

        Return the number of items in the heap.

        EXAMPLES::

            sage: from sage.data_structures.pairing_heap import PairingHeap_of_n_integers
            sage: P = PairingHeap_of_n_integers(5)
            sage: P.size()
            0
            sage: P.push(1, 2)
            sage: P.size()
            1

        One may also use Python's ``__len__``::

            sage: len(P)
            1"""
    @overload
    def size(self) -> Any:
        """PairingHeap_class.size(self) -> size_t

        File: /build/sagemath/src/sage/src/sage/data_structures/pairing_heap.pyx (starting at line 196)

        Return the number of items in the heap.

        EXAMPLES::

            sage: from sage.data_structures.pairing_heap import PairingHeap_of_n_integers
            sage: P = PairingHeap_of_n_integers(5)
            sage: P.size()
            0
            sage: P.push(1, 2)
            sage: P.size()
            1

        One may also use Python's ``__len__``::

            sage: len(P)
            1"""
    @overload
    def size(self) -> Any:
        """PairingHeap_class.size(self) -> size_t

        File: /build/sagemath/src/sage/src/sage/data_structures/pairing_heap.pyx (starting at line 196)

        Return the number of items in the heap.

        EXAMPLES::

            sage: from sage.data_structures.pairing_heap import PairingHeap_of_n_integers
            sage: P = PairingHeap_of_n_integers(5)
            sage: P.size()
            0
            sage: P.push(1, 2)
            sage: P.size()
            1

        One may also use Python's ``__len__``::

            sage: len(P)
            1"""
    @overload
    def top(self) -> tuple:
        """PairingHeap_class.top(self) -> tuple

        File: /build/sagemath/src/sage/src/sage/data_structures/pairing_heap.pyx (starting at line 233)

        Return the top pair (item, value) of the heap.

        EXAMPLES::

            sage: from sage.data_structures.pairing_heap import PairingHeap_of_n_integers
            sage: P = PairingHeap_of_n_integers(5)
            sage: P.push(1, 2)
            sage: P.top()
            (1, 2)
            sage: P.push(3, 1)
            sage: P.top()
            (3, 1)

            sage: P = PairingHeap_of_n_integers(3)
            sage: P.top()
            Traceback (most recent call last):
            ...
            ValueError: trying to access the top of an empty heap"""
    @overload
    def top(self) -> Any:
        """PairingHeap_class.top(self) -> tuple

        File: /build/sagemath/src/sage/src/sage/data_structures/pairing_heap.pyx (starting at line 233)

        Return the top pair (item, value) of the heap.

        EXAMPLES::

            sage: from sage.data_structures.pairing_heap import PairingHeap_of_n_integers
            sage: P = PairingHeap_of_n_integers(5)
            sage: P.push(1, 2)
            sage: P.top()
            (1, 2)
            sage: P.push(3, 1)
            sage: P.top()
            (3, 1)

            sage: P = PairingHeap_of_n_integers(3)
            sage: P.top()
            Traceback (most recent call last):
            ...
            ValueError: trying to access the top of an empty heap"""
    @overload
    def top(self) -> Any:
        """PairingHeap_class.top(self) -> tuple

        File: /build/sagemath/src/sage/src/sage/data_structures/pairing_heap.pyx (starting at line 233)

        Return the top pair (item, value) of the heap.

        EXAMPLES::

            sage: from sage.data_structures.pairing_heap import PairingHeap_of_n_integers
            sage: P = PairingHeap_of_n_integers(5)
            sage: P.push(1, 2)
            sage: P.top()
            (1, 2)
            sage: P.push(3, 1)
            sage: P.top()
            (3, 1)

            sage: P = PairingHeap_of_n_integers(3)
            sage: P.top()
            Traceback (most recent call last):
            ...
            ValueError: trying to access the top of an empty heap"""
    @overload
    def top(self) -> Any:
        """PairingHeap_class.top(self) -> tuple

        File: /build/sagemath/src/sage/src/sage/data_structures/pairing_heap.pyx (starting at line 233)

        Return the top pair (item, value) of the heap.

        EXAMPLES::

            sage: from sage.data_structures.pairing_heap import PairingHeap_of_n_integers
            sage: P = PairingHeap_of_n_integers(5)
            sage: P.push(1, 2)
            sage: P.top()
            (1, 2)
            sage: P.push(3, 1)
            sage: P.top()
            (3, 1)

            sage: P = PairingHeap_of_n_integers(3)
            sage: P.top()
            Traceback (most recent call last):
            ...
            ValueError: trying to access the top of an empty heap"""
    @overload
    def top_value(self) -> Any:
        """PairingHeap_class.top_value(self)

        File: /build/sagemath/src/sage/src/sage/data_structures/pairing_heap.pyx (starting at line 256)

        Return the value of the top item of the heap.

        EXAMPLES::

            sage: from sage.data_structures.pairing_heap import PairingHeap_of_n_integers
            sage: P = PairingHeap_of_n_integers(5)
            sage: P.push(1, 2)
            sage: P.top()
            (1, 2)
            sage: P.top_value()
            2

            sage: P = PairingHeap_of_n_integers(3)
            sage: P.top_value()
            Traceback (most recent call last):
            ...
            ValueError: trying to access the top of an empty heap"""
    @overload
    def top_value(self) -> Any:
        """PairingHeap_class.top_value(self)

        File: /build/sagemath/src/sage/src/sage/data_structures/pairing_heap.pyx (starting at line 256)

        Return the value of the top item of the heap.

        EXAMPLES::

            sage: from sage.data_structures.pairing_heap import PairingHeap_of_n_integers
            sage: P = PairingHeap_of_n_integers(5)
            sage: P.push(1, 2)
            sage: P.top()
            (1, 2)
            sage: P.top_value()
            2

            sage: P = PairingHeap_of_n_integers(3)
            sage: P.top_value()
            Traceback (most recent call last):
            ...
            ValueError: trying to access the top of an empty heap"""
    @overload
    def top_value(self) -> Any:
        """PairingHeap_class.top_value(self)

        File: /build/sagemath/src/sage/src/sage/data_structures/pairing_heap.pyx (starting at line 256)

        Return the value of the top item of the heap.

        EXAMPLES::

            sage: from sage.data_structures.pairing_heap import PairingHeap_of_n_integers
            sage: P = PairingHeap_of_n_integers(5)
            sage: P.push(1, 2)
            sage: P.top()
            (1, 2)
            sage: P.top_value()
            2

            sage: P = PairingHeap_of_n_integers(3)
            sage: P.top_value()
            Traceback (most recent call last):
            ...
            ValueError: trying to access the top of an empty heap"""
    def __bool__(self) -> bool:
        """True if self else False"""
    def __len__(self) -> Any:
        """PairingHeap_class.__len__(self)

        File: /build/sagemath/src/sage/src/sage/data_structures/pairing_heap.pyx (starting at line 217)

        Return the number of items in the heap.

        EXAMPLES::

            sage: from sage.data_structures.pairing_heap import PairingHeap_of_n_integers
            sage: P = PairingHeap_of_n_integers(5)
            sage: len(P)
            0
            sage: P.push(1, 2)
            sage: len(P)
            1"""

class PairingHeap_of_n_hashables(PairingHeap_class):
    """PairingHeap_of_n_hashables(size_t n)

    File: /build/sagemath/src/sage/src/sage/data_structures/pairing_heap.pyx (starting at line 648)

    Pairing Heap for `n` hashable items.

    EXAMPLES::

        sage: from sage.data_structures.pairing_heap import PairingHeap_of_n_hashables
        sage: P = PairingHeap_of_n_hashables(5); P
        PairingHeap_of_n_hashables: capacity 5, size 0
        sage: P.push(1, 3)
        sage: P.push('abc', 2); P
        PairingHeap_of_n_hashables: capacity 5, size 2
        sage: P.top()
        ('abc', 2)
        sage: P.decrease(1, 1)
        sage: P.top()
        (1, 1)
        sage: P.pop()
        sage: P.top()
        ('abc', 2)

        sage: P = PairingHeap_of_n_hashables(5)
        sage: P.push(1, (2, 3))
        sage: P.push('a', (2, 2))
        sage: P.push('b', (3, 3))
        sage: P.push('c', (2, 1))
        sage: P.top()
        ('c', (2, 1))
        sage: P.push(Graph(2, immutable=True), (1, 7))
        sage: P.top()
        (Graph on 2 vertices, (1, 7))
        sage: P.decrease('b', (1, 5))
        sage: P.top()
        ('b', (1, 5))

    TESTS::

        sage: from sage.data_structures.pairing_heap import PairingHeap_of_n_hashables
        sage: P = PairingHeap_of_n_hashables(0)
        Traceback (most recent call last):
        ...
        ValueError: the capacity of the heap must be strictly positive
        sage: P = PairingHeap_of_n_hashables(1); P
        PairingHeap_of_n_hashables: capacity 1, size 0
        sage: P.push(11, 3)
        sage: P.push(12, 4)
        Traceback (most recent call last):
        ...
        ValueError: the heap is full

        sage: P = PairingHeap_of_n_hashables(10)
        sage: P.push(1, 'John')
        sage: P.push(4, 42)
        Traceback (most recent call last):
        ...
        TypeError: unsupported operand parent(s) for >=: 'Integer Ring' and '<class 'str'>'"""
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    def __init__(self, size_tn) -> Any:
        '''File: /build/sagemath/src/sage/src/sage/data_structures/pairing_heap.pyx (starting at line 706)

                Construct the ``PairingHeap_of_n_hashables``.

                This pairing heap has a maximum capacity of `n` items and each item is a
                hashable object.

                INPUT:

                - ``n`` -- strictly positive integer; the maximum number of items in the heap

                EXAMPLES::

                    sage: from sage.data_structures.pairing_heap import PairingHeap_of_n_hashables
                    sage: P = PairingHeap_of_n_hashables(2); P
                    PairingHeap_of_n_hashables: capacity 2, size 0
                    sage: P.push(1, 2)
                    sage: P
                    PairingHeap_of_n_hashables: capacity 2, size 1
                    sage: P.push(2, 3)
                    sage: P
                    PairingHeap_of_n_hashables: capacity 2, size 2
                    sage: P.full()
                    True
                    sage: P.push(10, 1)
                    Traceback (most recent call last):
                    ...
                    ValueError: the heap is full
                    sage: P.pop()
                    sage: P
                    PairingHeap_of_n_hashables: capacity 2, size 1
                    sage: P.push(10, 1)

            TESTS::

                    sage: P = PairingHeap_of_n_hashables(0)
                    Traceback (most recent call last):
                    ...
                    ValueError: the capacity of the heap must be strictly positive
                    sage: P = PairingHeap_of_n_hashables(1); P
                    PairingHeap_of_n_hashables: capacity 1, size 0
                    sage: P = PairingHeap_of_n_hashables(6)
                    sage: P.push(1, -0.5); P.push(frozenset(), 1); P.pop(); P.push(\'a\', 3.5)
                    sage: TestSuite(P).run(skip="_test_pickling")
        '''
    def contains(self, *args, **kwargs):
        """PairingHeap_of_n_hashables.__contains__(self, item)

        File: /build/sagemath/src/sage/src/sage/data_structures/pairing_heap.pyx (starting at line 967)

        Check whether the specified item is in the heap.

        INPUT:

        - ``item`` -- the item to consider

        EXAMPLES::

            sage: from sage.data_structures.pairing_heap import PairingHeap_of_n_hashables
            sage: P = PairingHeap_of_n_hashables(5)
            sage: 3 in P
            False
            sage: P.push(3, 33)
            sage: 3 in P
            True
            sage: 100 in P
            False"""
    def decrease(self, item, new_value) -> void:
        """PairingHeap_of_n_hashables.decrease(self, item, new_value) -> void

        File: /build/sagemath/src/sage/src/sage/data_structures/pairing_heap.pyx (starting at line 910)

        Decrease the value of specified item.

        This method is more permissive than it should as it can also be used to
        push an item in the heap.

        INPUT:

        - ``item`` -- the item to consider

        - ``new_value`` -- the new value for ``item``

        EXAMPLES::

            sage: from sage.data_structures.pairing_heap import PairingHeap_of_n_hashables
            sage: P = PairingHeap_of_n_hashables(5)
            sage: 3 in P
            False
            sage: P.decrease(3, 33)
            sage: 3 in P
            True
            sage: P.top()
            (3, 33)
            sage: P.push(1, 10)
            sage: P.top()
            (1, 10)
            sage: P.decrease(3, 7)
            sage: P.top()
            (3, 7)

        TESTS::

            sage: P = PairingHeap_of_n_hashables(5)
            sage: P.push(1, 3)
            sage: P.decrease(1, 2)
            sage: P.decrease(1, 2)
            Traceback (most recent call last):
            ...
            ValueError: the new value must be less than the current value"""
    @overload
    def pop(self) -> void:
        """PairingHeap_of_n_hashables.pop(self) -> void

        File: /build/sagemath/src/sage/src/sage/data_structures/pairing_heap.pyx (starting at line 878)

        Remove the top item from the heap.

        If the heap is already empty, we do nothing.

        EXAMPLES::

            sage: from sage.data_structures.pairing_heap import PairingHeap_of_n_hashables
            sage: P = PairingHeap_of_n_hashables(5); len(P)
            0
            sage: P.push(1, 2); len(P)
            1
            sage: P.push(2, 3); len(P)
            2
            sage: P.pop(); len(P)
            1
            sage: P.pop(); len(P)
            0
            sage: P.pop(); len(P)
            0"""
    @overload
    def pop(self) -> Any:
        """PairingHeap_of_n_hashables.pop(self) -> void

        File: /build/sagemath/src/sage/src/sage/data_structures/pairing_heap.pyx (starting at line 878)

        Remove the top item from the heap.

        If the heap is already empty, we do nothing.

        EXAMPLES::

            sage: from sage.data_structures.pairing_heap import PairingHeap_of_n_hashables
            sage: P = PairingHeap_of_n_hashables(5); len(P)
            0
            sage: P.push(1, 2); len(P)
            1
            sage: P.push(2, 3); len(P)
            2
            sage: P.pop(); len(P)
            1
            sage: P.pop(); len(P)
            0
            sage: P.pop(); len(P)
            0"""
    @overload
    def pop(self) -> Any:
        """PairingHeap_of_n_hashables.pop(self) -> void

        File: /build/sagemath/src/sage/src/sage/data_structures/pairing_heap.pyx (starting at line 878)

        Remove the top item from the heap.

        If the heap is already empty, we do nothing.

        EXAMPLES::

            sage: from sage.data_structures.pairing_heap import PairingHeap_of_n_hashables
            sage: P = PairingHeap_of_n_hashables(5); len(P)
            0
            sage: P.push(1, 2); len(P)
            1
            sage: P.push(2, 3); len(P)
            2
            sage: P.pop(); len(P)
            1
            sage: P.pop(); len(P)
            0
            sage: P.pop(); len(P)
            0"""
    @overload
    def pop(self) -> Any:
        """PairingHeap_of_n_hashables.pop(self) -> void

        File: /build/sagemath/src/sage/src/sage/data_structures/pairing_heap.pyx (starting at line 878)

        Remove the top item from the heap.

        If the heap is already empty, we do nothing.

        EXAMPLES::

            sage: from sage.data_structures.pairing_heap import PairingHeap_of_n_hashables
            sage: P = PairingHeap_of_n_hashables(5); len(P)
            0
            sage: P.push(1, 2); len(P)
            1
            sage: P.push(2, 3); len(P)
            2
            sage: P.pop(); len(P)
            1
            sage: P.pop(); len(P)
            0
            sage: P.pop(); len(P)
            0"""
    def push(self, item, value) -> void:
        """PairingHeap_of_n_hashables.push(self, item, value) -> void

        File: /build/sagemath/src/sage/src/sage/data_structures/pairing_heap.pyx (starting at line 773)

        Insert an item into the heap with specified value (priority).

        INPUT:

        - ``item`` -- a hashable object; the item to add

        - ``value`` -- the value associated with ``item``

        EXAMPLES::

            sage: from sage.data_structures.pairing_heap import PairingHeap_of_n_hashables
            sage: P = PairingHeap_of_n_hashables(5)
            sage: P.push(1, 2)
            sage: P.top()
            (1, 2)
            sage: P.push(3, 1)
            sage: P.top()
            (3, 1)

        TESTS::

            sage: from sage.data_structures.pairing_heap import PairingHeap_of_n_hashables
            sage: P = PairingHeap_of_n_hashables(2)
            sage: P.push(1, 2)
            sage: P.push(1, 2)
            Traceback (most recent call last):
            ...
            ValueError: 1 is already in the heap
            sage: P.push(11, 2)
            sage: P.push(7, 5)
            Traceback (most recent call last):
            ...
            ValueError: the heap is full"""
    @overload
    def top(self) -> tuple:
        """PairingHeap_of_n_hashables.top(self) -> tuple

        File: /build/sagemath/src/sage/src/sage/data_structures/pairing_heap.pyx (starting at line 827)

        Return the top pair (item, value) of the heap.

        EXAMPLES::

            sage: from sage.data_structures.pairing_heap import PairingHeap_of_n_hashables
            sage: P = PairingHeap_of_n_hashables(5)
            sage: P.push(1, 2)
            sage: P.top()
            (1, 2)
            sage: P.push(3, 1)
            sage: P.top()
            (3, 1)

            sage: P = PairingHeap_of_n_hashables(3)
            sage: P.top()
            Traceback (most recent call last):
            ...
            ValueError: trying to access the top of an empty heap"""
    @overload
    def top(self) -> Any:
        """PairingHeap_of_n_hashables.top(self) -> tuple

        File: /build/sagemath/src/sage/src/sage/data_structures/pairing_heap.pyx (starting at line 827)

        Return the top pair (item, value) of the heap.

        EXAMPLES::

            sage: from sage.data_structures.pairing_heap import PairingHeap_of_n_hashables
            sage: P = PairingHeap_of_n_hashables(5)
            sage: P.push(1, 2)
            sage: P.top()
            (1, 2)
            sage: P.push(3, 1)
            sage: P.top()
            (3, 1)

            sage: P = PairingHeap_of_n_hashables(3)
            sage: P.top()
            Traceback (most recent call last):
            ...
            ValueError: trying to access the top of an empty heap"""
    @overload
    def top(self) -> Any:
        """PairingHeap_of_n_hashables.top(self) -> tuple

        File: /build/sagemath/src/sage/src/sage/data_structures/pairing_heap.pyx (starting at line 827)

        Return the top pair (item, value) of the heap.

        EXAMPLES::

            sage: from sage.data_structures.pairing_heap import PairingHeap_of_n_hashables
            sage: P = PairingHeap_of_n_hashables(5)
            sage: P.push(1, 2)
            sage: P.top()
            (1, 2)
            sage: P.push(3, 1)
            sage: P.top()
            (3, 1)

            sage: P = PairingHeap_of_n_hashables(3)
            sage: P.top()
            Traceback (most recent call last):
            ...
            ValueError: trying to access the top of an empty heap"""
    @overload
    def top(self) -> Any:
        """PairingHeap_of_n_hashables.top(self) -> tuple

        File: /build/sagemath/src/sage/src/sage/data_structures/pairing_heap.pyx (starting at line 827)

        Return the top pair (item, value) of the heap.

        EXAMPLES::

            sage: from sage.data_structures.pairing_heap import PairingHeap_of_n_hashables
            sage: P = PairingHeap_of_n_hashables(5)
            sage: P.push(1, 2)
            sage: P.top()
            (1, 2)
            sage: P.push(3, 1)
            sage: P.top()
            (3, 1)

            sage: P = PairingHeap_of_n_hashables(3)
            sage: P.top()
            Traceback (most recent call last):
            ...
            ValueError: trying to access the top of an empty heap"""
    @overload
    def top_item(self) -> Any:
        """PairingHeap_of_n_hashables.top_item(self)

        File: /build/sagemath/src/sage/src/sage/data_structures/pairing_heap.pyx (starting at line 853)

        Return the top item of the heap.

        EXAMPLES::

            sage: from sage.data_structures.pairing_heap import PairingHeap_of_n_hashables
            sage: P = PairingHeap_of_n_hashables(5)
            sage: P.push(1, 2)
            sage: P.top()
            (1, 2)
            sage: P.top_item()
            1

            sage: P = PairingHeap_of_n_hashables(3)
            sage: P.top_item()
            Traceback (most recent call last):
            ...
            ValueError: trying to access the top of an empty heap"""
    @overload
    def top_item(self) -> Any:
        """PairingHeap_of_n_hashables.top_item(self)

        File: /build/sagemath/src/sage/src/sage/data_structures/pairing_heap.pyx (starting at line 853)

        Return the top item of the heap.

        EXAMPLES::

            sage: from sage.data_structures.pairing_heap import PairingHeap_of_n_hashables
            sage: P = PairingHeap_of_n_hashables(5)
            sage: P.push(1, 2)
            sage: P.top()
            (1, 2)
            sage: P.top_item()
            1

            sage: P = PairingHeap_of_n_hashables(3)
            sage: P.top_item()
            Traceback (most recent call last):
            ...
            ValueError: trying to access the top of an empty heap"""
    @overload
    def top_item(self) -> Any:
        """PairingHeap_of_n_hashables.top_item(self)

        File: /build/sagemath/src/sage/src/sage/data_structures/pairing_heap.pyx (starting at line 853)

        Return the top item of the heap.

        EXAMPLES::

            sage: from sage.data_structures.pairing_heap import PairingHeap_of_n_hashables
            sage: P = PairingHeap_of_n_hashables(5)
            sage: P.push(1, 2)
            sage: P.top()
            (1, 2)
            sage: P.top_item()
            1

            sage: P = PairingHeap_of_n_hashables(3)
            sage: P.top_item()
            Traceback (most recent call last):
            ...
            ValueError: trying to access the top of an empty heap"""
    def value(self, item) -> Any:
        """PairingHeap_of_n_hashables.value(self, item)

        File: /build/sagemath/src/sage/src/sage/data_structures/pairing_heap.pyx (starting at line 991)

        Return the value associated with the item.

        INPUT:

        - ``item`` -- the item to consider

        EXAMPLES::

            sage: from sage.data_structures.pairing_heap import PairingHeap_of_n_hashables
            sage: P = PairingHeap_of_n_hashables(5)
            sage: P.push(3, 33)
            sage: P.push(1, 10)
            sage: P.value(3)
            33
            sage: P.value(7)
            Traceback (most recent call last):
            ...
            ValueError: 7 is not in the heap"""
    def __contains__(self, item) -> Any:
        """PairingHeap_of_n_hashables.__contains__(self, item)

        File: /build/sagemath/src/sage/src/sage/data_structures/pairing_heap.pyx (starting at line 967)

        Check whether the specified item is in the heap.

        INPUT:

        - ``item`` -- the item to consider

        EXAMPLES::

            sage: from sage.data_structures.pairing_heap import PairingHeap_of_n_hashables
            sage: P = PairingHeap_of_n_hashables(5)
            sage: 3 in P
            False
            sage: P.push(3, 33)
            sage: 3 in P
            True
            sage: 100 in P
            False"""

class PairingHeap_of_n_integers(PairingHeap_class):
    """PairingHeap_of_n_integers(size_t n)

    File: /build/sagemath/src/sage/src/sage/data_structures/pairing_heap.pyx (starting at line 305)

    Pairing Heap for items in range `[0, n - 1]`.

    EXAMPLES::

        sage: from sage.data_structures.pairing_heap import PairingHeap_of_n_integers
        sage: P = PairingHeap_of_n_integers(5); P
        PairingHeap_of_n_integers: capacity 5, size 0
        sage: P.push(1, 3)
        sage: P.push(2, 2)
        sage: P
        PairingHeap_of_n_integers: capacity 5, size 2
        sage: P.top()
        (2, 2)
        sage: P.decrease(1, 1)
        sage: P.top()
        (1, 1)
        sage: P.pop()
        sage: P.top()
        (2, 2)

    TESTS::

        sage: from sage.data_structures.pairing_heap import PairingHeap_of_n_integers
        sage: P = PairingHeap_of_n_integers(0)
        Traceback (most recent call last):
        ...
        ValueError: the capacity of the heap must be strictly positive
        sage: P = PairingHeap_of_n_integers(1); P
        PairingHeap_of_n_integers: capacity 1, size 0
        sage: P = PairingHeap_of_n_integers(5)
        sage: P.push(11, 3)
        Traceback (most recent call last):
        ...
        ValueError: item must be in range [0, 4]"""
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    def __init__(self, size_tn) -> Any:
        '''File: /build/sagemath/src/sage/src/sage/data_structures/pairing_heap.pyx (starting at line 343)

                Construct the ``PairingHeap_of_n_integers`` where items are integers
                from `0` to `n-1`.

                INPUT:

                - ``n`` -- strictly positive integer; the maximum number of items in the heap

                EXAMPLES::

                    sage: from sage.data_structures.pairing_heap import PairingHeap_of_n_integers
                    sage: P = PairingHeap_of_n_integers(5); P
                    PairingHeap_of_n_integers: capacity 5, size 0
                    sage: P.push(1, 2); P
                    PairingHeap_of_n_integers: capacity 5, size 1
                    sage: P.push(2, 3); P
                    PairingHeap_of_n_integers: capacity 5, size 2
                    sage: P.pop(); P
                    PairingHeap_of_n_integers: capacity 5, size 1
                    sage: P.push(10, 1)
                    Traceback (most recent call last):
                    ...
                    ValueError: item must be in range [0, 4]
                    sage: PairingHeap_of_n_integers(1)
                    PairingHeap_of_n_integers: capacity 1, size 0

                TESTS::

                    sage: PairingHeap_of_n_integers(0)
                    Traceback (most recent call last):
                    ...
                    ValueError: the capacity of the heap must be strictly positive
                    sage: P = PairingHeap_of_n_integers(10)
                    sage: P.push(1, 1); P.push(7, 0); P.push(0, 4); P.pop(); P.push(5, 5)
                    sage: TestSuite(P).run(skip="_test_pickling")
        '''
    def contains(self, *args, **kwargs):
        """PairingHeap_of_n_integers.__contains__(self, size_t item)

        File: /build/sagemath/src/sage/src/sage/data_structures/pairing_heap.pyx (starting at line 592)

        Check whether the specified item is in the heap.

        INPUT:

        - ``item`` -- nonnegative integer; the item to consider

        EXAMPLES::

            sage: from sage.data_structures.pairing_heap import PairingHeap_of_n_integers
            sage: P = PairingHeap_of_n_integers(5)
            sage: 3 in P
            False
            sage: P.push(3, 33)
            sage: 3 in P
            True
            sage: 100 in P
            False"""
    def decrease(self, size_titem, new_value) -> void:
        """PairingHeap_of_n_integers.decrease(self, size_t item, new_value) -> void

        File: /build/sagemath/src/sage/src/sage/data_structures/pairing_heap.pyx (starting at line 535)

        Decrease the value of specified item.

        This method is more permissive than it should as it can also be used to
        push an item in the heap.

        INPUT:

        - ``item`` -- nonnegative integer; the item to consider

        - ``new_value`` -- the new value for ``item``

        EXAMPLES::

            sage: from sage.data_structures.pairing_heap import PairingHeap_of_n_integers
            sage: P = PairingHeap_of_n_integers(5)
            sage: 3 in P
            False
            sage: P.decrease(3, 33)
            sage: 3 in P
            True
            sage: P.top()
            (3, 33)
            sage: P.push(1, 10)
            sage: P.top()
            (1, 10)
            sage: P.decrease(3, 7)
            sage: P.top()
            (3, 7)

        TESTS::

            sage: P = PairingHeap_of_n_integers(5)
            sage: P.push(1, 3)
            sage: P.decrease(1, 2)
            sage: P.decrease(1, 2)
            Traceback (most recent call last):
            ...
            ValueError: the new value must be less than the current value"""
    @overload
    def pop(self) -> void:
        """PairingHeap_of_n_integers.pop(self) -> void

        File: /build/sagemath/src/sage/src/sage/data_structures/pairing_heap.pyx (starting at line 505)

        Remove the top item from the heap.

        If the heap is already empty, we do nothing.

        EXAMPLES::

            sage: from sage.data_structures.pairing_heap import PairingHeap_of_n_integers
            sage: P = PairingHeap_of_n_integers(5); P
            PairingHeap_of_n_integers: capacity 5, size 0
            sage: P.push(1, 2); P
            PairingHeap_of_n_integers: capacity 5, size 1
            sage: P.push(2, 3); P
            PairingHeap_of_n_integers: capacity 5, size 2
            sage: P.pop(); P
            PairingHeap_of_n_integers: capacity 5, size 1
            sage: P.pop(); P
            PairingHeap_of_n_integers: capacity 5, size 0
            sage: P.pop(); P
            PairingHeap_of_n_integers: capacity 5, size 0"""
    @overload
    def pop(self) -> Any:
        """PairingHeap_of_n_integers.pop(self) -> void

        File: /build/sagemath/src/sage/src/sage/data_structures/pairing_heap.pyx (starting at line 505)

        Remove the top item from the heap.

        If the heap is already empty, we do nothing.

        EXAMPLES::

            sage: from sage.data_structures.pairing_heap import PairingHeap_of_n_integers
            sage: P = PairingHeap_of_n_integers(5); P
            PairingHeap_of_n_integers: capacity 5, size 0
            sage: P.push(1, 2); P
            PairingHeap_of_n_integers: capacity 5, size 1
            sage: P.push(2, 3); P
            PairingHeap_of_n_integers: capacity 5, size 2
            sage: P.pop(); P
            PairingHeap_of_n_integers: capacity 5, size 1
            sage: P.pop(); P
            PairingHeap_of_n_integers: capacity 5, size 0
            sage: P.pop(); P
            PairingHeap_of_n_integers: capacity 5, size 0"""
    @overload
    def pop(self) -> Any:
        """PairingHeap_of_n_integers.pop(self) -> void

        File: /build/sagemath/src/sage/src/sage/data_structures/pairing_heap.pyx (starting at line 505)

        Remove the top item from the heap.

        If the heap is already empty, we do nothing.

        EXAMPLES::

            sage: from sage.data_structures.pairing_heap import PairingHeap_of_n_integers
            sage: P = PairingHeap_of_n_integers(5); P
            PairingHeap_of_n_integers: capacity 5, size 0
            sage: P.push(1, 2); P
            PairingHeap_of_n_integers: capacity 5, size 1
            sage: P.push(2, 3); P
            PairingHeap_of_n_integers: capacity 5, size 2
            sage: P.pop(); P
            PairingHeap_of_n_integers: capacity 5, size 1
            sage: P.pop(); P
            PairingHeap_of_n_integers: capacity 5, size 0
            sage: P.pop(); P
            PairingHeap_of_n_integers: capacity 5, size 0"""
    @overload
    def pop(self) -> Any:
        """PairingHeap_of_n_integers.pop(self) -> void

        File: /build/sagemath/src/sage/src/sage/data_structures/pairing_heap.pyx (starting at line 505)

        Remove the top item from the heap.

        If the heap is already empty, we do nothing.

        EXAMPLES::

            sage: from sage.data_structures.pairing_heap import PairingHeap_of_n_integers
            sage: P = PairingHeap_of_n_integers(5); P
            PairingHeap_of_n_integers: capacity 5, size 0
            sage: P.push(1, 2); P
            PairingHeap_of_n_integers: capacity 5, size 1
            sage: P.push(2, 3); P
            PairingHeap_of_n_integers: capacity 5, size 2
            sage: P.pop(); P
            PairingHeap_of_n_integers: capacity 5, size 1
            sage: P.pop(); P
            PairingHeap_of_n_integers: capacity 5, size 0
            sage: P.pop(); P
            PairingHeap_of_n_integers: capacity 5, size 0"""
    def push(self, size_titem, value) -> void:
        """PairingHeap_of_n_integers.push(self, size_t item, value) -> void

        File: /build/sagemath/src/sage/src/sage/data_structures/pairing_heap.pyx (starting at line 401)

        Insert an item into the heap with specified value (priority).

        INPUT:

        - ``item`` -- nonnegative integer; the item to consider

        - ``value`` -- the value associated with ``item``

        EXAMPLES::

            sage: from sage.data_structures.pairing_heap import PairingHeap_of_n_integers
            sage: P = PairingHeap_of_n_integers(5)
            sage: P.push(1, 2)
            sage: P.top()
            (1, 2)
            sage: P.push(3, 1)
            sage: P.top()
            (3, 1)

        TESTS::

            sage: from sage.data_structures.pairing_heap import PairingHeap_of_n_integers
            sage: P = PairingHeap_of_n_integers(5)
            sage: P.push(1, 2)
            sage: P.push(1, 2)
            Traceback (most recent call last):
            ...
            ValueError: 1 is already in the heap
            sage: P.push(11, 2)
            Traceback (most recent call last):
            ...
            ValueError: item must be in range [0, 4]
            sage: P.push(-1, 0)
            Traceback (most recent call last):
            ...
            OverflowError: can't convert negative value to size_t"""
    @overload
    def top(self) -> tuple:
        """PairingHeap_of_n_integers.top(self) -> tuple

        File: /build/sagemath/src/sage/src/sage/data_structures/pairing_heap.pyx (starting at line 456)

        Return the top pair (item, value) of the heap.

        EXAMPLES::

            sage: from sage.data_structures.pairing_heap import PairingHeap_of_n_integers
            sage: P = PairingHeap_of_n_integers(5)
            sage: P.push(1, 2)
            sage: P.top()
            (1, 2)
            sage: P.push(3, 1)
            sage: P.top()
            (3, 1)

            sage: P = PairingHeap_of_n_integers(3)
            sage: P.top()
            Traceback (most recent call last):
            ...
            ValueError: trying to access the top of an empty heap"""
    @overload
    def top(self) -> Any:
        """PairingHeap_of_n_integers.top(self) -> tuple

        File: /build/sagemath/src/sage/src/sage/data_structures/pairing_heap.pyx (starting at line 456)

        Return the top pair (item, value) of the heap.

        EXAMPLES::

            sage: from sage.data_structures.pairing_heap import PairingHeap_of_n_integers
            sage: P = PairingHeap_of_n_integers(5)
            sage: P.push(1, 2)
            sage: P.top()
            (1, 2)
            sage: P.push(3, 1)
            sage: P.top()
            (3, 1)

            sage: P = PairingHeap_of_n_integers(3)
            sage: P.top()
            Traceback (most recent call last):
            ...
            ValueError: trying to access the top of an empty heap"""
    @overload
    def top(self) -> Any:
        """PairingHeap_of_n_integers.top(self) -> tuple

        File: /build/sagemath/src/sage/src/sage/data_structures/pairing_heap.pyx (starting at line 456)

        Return the top pair (item, value) of the heap.

        EXAMPLES::

            sage: from sage.data_structures.pairing_heap import PairingHeap_of_n_integers
            sage: P = PairingHeap_of_n_integers(5)
            sage: P.push(1, 2)
            sage: P.top()
            (1, 2)
            sage: P.push(3, 1)
            sage: P.top()
            (3, 1)

            sage: P = PairingHeap_of_n_integers(3)
            sage: P.top()
            Traceback (most recent call last):
            ...
            ValueError: trying to access the top of an empty heap"""
    @overload
    def top(self) -> Any:
        """PairingHeap_of_n_integers.top(self) -> tuple

        File: /build/sagemath/src/sage/src/sage/data_structures/pairing_heap.pyx (starting at line 456)

        Return the top pair (item, value) of the heap.

        EXAMPLES::

            sage: from sage.data_structures.pairing_heap import PairingHeap_of_n_integers
            sage: P = PairingHeap_of_n_integers(5)
            sage: P.push(1, 2)
            sage: P.top()
            (1, 2)
            sage: P.push(3, 1)
            sage: P.top()
            (3, 1)

            sage: P = PairingHeap_of_n_integers(3)
            sage: P.top()
            Traceback (most recent call last):
            ...
            ValueError: trying to access the top of an empty heap"""
    @overload
    def top_item(self) -> size_t:
        """PairingHeap_of_n_integers.top_item(self) -> size_t

        File: /build/sagemath/src/sage/src/sage/data_structures/pairing_heap.pyx (starting at line 481)

        Return the top item of the heap.

        EXAMPLES::

            sage: from sage.data_structures.pairing_heap import PairingHeap_of_n_integers
            sage: P = PairingHeap_of_n_integers(5)
            sage: P.push(1, 2)
            sage: P.top()
            (1, 2)
            sage: P.top_item()
            1

            sage: P = PairingHeap_of_n_integers(3)
            sage: P.top_item()
            Traceback (most recent call last):
            ...
            ValueError: trying to access the top of an empty heap"""
    @overload
    def top_item(self) -> Any:
        """PairingHeap_of_n_integers.top_item(self) -> size_t

        File: /build/sagemath/src/sage/src/sage/data_structures/pairing_heap.pyx (starting at line 481)

        Return the top item of the heap.

        EXAMPLES::

            sage: from sage.data_structures.pairing_heap import PairingHeap_of_n_integers
            sage: P = PairingHeap_of_n_integers(5)
            sage: P.push(1, 2)
            sage: P.top()
            (1, 2)
            sage: P.top_item()
            1

            sage: P = PairingHeap_of_n_integers(3)
            sage: P.top_item()
            Traceback (most recent call last):
            ...
            ValueError: trying to access the top of an empty heap"""
    @overload
    def top_item(self) -> Any:
        """PairingHeap_of_n_integers.top_item(self) -> size_t

        File: /build/sagemath/src/sage/src/sage/data_structures/pairing_heap.pyx (starting at line 481)

        Return the top item of the heap.

        EXAMPLES::

            sage: from sage.data_structures.pairing_heap import PairingHeap_of_n_integers
            sage: P = PairingHeap_of_n_integers(5)
            sage: P.push(1, 2)
            sage: P.top()
            (1, 2)
            sage: P.top_item()
            1

            sage: P = PairingHeap_of_n_integers(3)
            sage: P.top_item()
            Traceback (most recent call last):
            ...
            ValueError: trying to access the top of an empty heap"""
    def value(self, size_titem) -> Any:
        """PairingHeap_of_n_integers.value(self, size_t item)

        File: /build/sagemath/src/sage/src/sage/data_structures/pairing_heap.pyx (starting at line 618)

        Return the value associated with the item.

        INPUT:

        - ``item`` -- nonnegative integer; the item to consider

        EXAMPLES::

            sage: from sage.data_structures.pairing_heap import PairingHeap_of_n_integers
            sage: P = PairingHeap_of_n_integers(5)
            sage: P.push(3, 33)
            sage: P.push(1, 10)
            sage: P.value(3)
            33
            sage: P.value(7)
            Traceback (most recent call last):
            ...
            ValueError: 7 is not in the heap"""
    def __contains__(self, size_titem) -> Any:
        """PairingHeap_of_n_integers.__contains__(self, size_t item)

        File: /build/sagemath/src/sage/src/sage/data_structures/pairing_heap.pyx (starting at line 592)

        Check whether the specified item is in the heap.

        INPUT:

        - ``item`` -- nonnegative integer; the item to consider

        EXAMPLES::

            sage: from sage.data_structures.pairing_heap import PairingHeap_of_n_integers
            sage: P = PairingHeap_of_n_integers(5)
            sage: 3 in P
            False
            sage: P.push(3, 33)
            sage: 3 in P
            True
            sage: 100 in P
            False"""
