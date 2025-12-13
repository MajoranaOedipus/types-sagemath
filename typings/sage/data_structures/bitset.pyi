import _cython_3_2_1
from sage.cpython.string import bytes_to_str as bytes_to_str, str_to_bytes as str_to_bytes
from typing import Any, ClassVar, overload

test_bitset: _cython_3_2_1.cython_function_or_method
test_bitset_copy_flex: _cython_3_2_1.cython_function_or_method
test_bitset_pop: _cython_3_2_1.cython_function_or_method
test_bitset_remove: _cython_3_2_1.cython_function_or_method
test_bitset_set_first_n: _cython_3_2_1.cython_function_or_method
test_bitset_unpickle: _cython_3_2_1.cython_function_or_method

class Bitset(FrozenBitset):
    """File: /build/sagemath/src/sage/src/sage/data_structures/bitset.pyx (starting at line 1240)

        A bitset class which leverages inline Cython functions for creating
        and manipulating bitsets. See the class documentation of
        :class:`FrozenBitset` for details on the parameters of the constructor
        and how to interpret the string representation of a :class:`Bitset`.

        A bitset can be thought of in two ways.  First, as a set of elements
        from the universe of the `n` natural numbers `0, 1, \\dots, n-1` (where
        the capacity `n` can be specified), with typical set operations such as
        intersection, union, symmetric difference, etc.  Secondly, a bitset can
        be thought of as a binary vector with typical binary operations such as
        ``and``, ``or``, ``xor``, etc.  This class supports both interfaces.

        The interface in this class mirrors the interface in the ``set``
        data type of Python.

        .. warning::

            This class is most likely to be useful as a way to store
            Cython bitsets in Python data structures, acting on them using
            the Cython inline functions.  If you want to use this class
            for a Python set type, the Python ``set`` data type may be
            faster.

        .. SEEALSO::

            - :class:`FrozenBitset`
            - Python's `set types <https://docs.python.org/library/stdtypes.html#set-types-set-frozenset>`_

        EXAMPLES::

            sage: a = Bitset('1101')
            sage: loads(dumps(a)) == a
            True
            sage: a = Bitset('1101' * 32)
            sage: loads(dumps(a)) == a
            True
    """
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    @classmethod
    def __init__(cls, *args, **kwargs) -> None:
        """Create and return a new object.  See help(type) for accurate signature."""
    @overload
    def add(self, unsignedlongn) -> Any:
        """Bitset.add(self, unsigned long n)

        File: /build/sagemath/src/sage/src/sage/data_structures/bitset.pyx (starting at line 1760)

        Update the bitset by adding ``n``.

        EXAMPLES::

            sage: a = Bitset('110')
            sage: a.add(5)
            sage: a
            110001
            sage: a.add(100)
            sage: sorted(list(a))
            [0, 1, 5, 100]
            sage: a.capacity()
            101

        TESTS:

        The input ``n`` must be an integer. ::

            sage: Bitset('110').add(None)
            Traceback (most recent call last):
            ...
            TypeError: an integer is required"""
    @overload
    def add(self, _None) -> Any:
        """Bitset.add(self, unsigned long n)

        File: /build/sagemath/src/sage/src/sage/data_structures/bitset.pyx (starting at line 1760)

        Update the bitset by adding ``n``.

        EXAMPLES::

            sage: a = Bitset('110')
            sage: a.add(5)
            sage: a
            110001
            sage: a.add(100)
            sage: sorted(list(a))
            [0, 1, 5, 100]
            sage: a.capacity()
            101

        TESTS:

        The input ``n`` must be an integer. ::

            sage: Bitset('110').add(None)
            Traceback (most recent call last):
            ...
            TypeError: an integer is required"""
    @overload
    def clear(self) -> Any:
        """Bitset.clear(self)

        File: /build/sagemath/src/sage/src/sage/data_structures/bitset.pyx (starting at line 1893)

        Remove all elements from the bitset.

        EXAMPLES::

            sage: a = Bitset('011')
            sage: a.clear()
            sage: a
            000
            sage: a = Bitset('011' * 32)
            sage: a.clear()
            sage: set(a)
            set()"""
    @overload
    def clear(self) -> Any:
        """Bitset.clear(self)

        File: /build/sagemath/src/sage/src/sage/data_structures/bitset.pyx (starting at line 1893)

        Remove all elements from the bitset.

        EXAMPLES::

            sage: a = Bitset('011')
            sage: a.clear()
            sage: a
            000
            sage: a = Bitset('011' * 32)
            sage: a.clear()
            sage: set(a)
            set()"""
    @overload
    def clear(self) -> Any:
        """Bitset.clear(self)

        File: /build/sagemath/src/sage/src/sage/data_structures/bitset.pyx (starting at line 1893)

        Remove all elements from the bitset.

        EXAMPLES::

            sage: a = Bitset('011')
            sage: a.clear()
            sage: a
            000
            sage: a = Bitset('011' * 32)
            sage: a.clear()
            sage: set(a)
            set()"""
    @overload
    def difference_update(self, FrozenBitsetother) -> Any:
        """Bitset.difference_update(self, FrozenBitset other)

        File: /build/sagemath/src/sage/src/sage/data_structures/bitset.pyx (starting at line 1570)

        Update the bitset to the difference of ``self`` and ``other``.

        EXAMPLES::

            sage: a = Bitset('110')
            sage: a.difference_update(Bitset('0101'))
            sage: a
            1000
            sage: a_set = set(a)
            sage: a.difference_update(FrozenBitset('010101' * 10)); a
            100000000000000000000000000000000000000000000000000000000000
            sage: a_set.difference_update(FrozenBitset('010101' * 10))
            sage: a_set == set(a)
            True
            sage: a.difference_update(FrozenBitset('110'))
            sage: a_set.difference_update(FrozenBitset('110'))
            sage: a_set == set(a)
            True
            sage: a.difference_update(FrozenBitset('01010' * 20)); a
            0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
            sage: a_set.difference_update(FrozenBitset('01010' * 20))
            sage: a_set == set(a)
            True
            sage: b = Bitset('10101' * 20)
            sage: b_set = set(b)
            sage: b.difference_update(FrozenBitset('1' * 5)); b
            0000010101101011010110101101011010110101101011010110101101011010110101101011010110101101011010110101
            sage: b_set.difference_update(FrozenBitset('1' * 5))
            sage: b_set == set(b)
            True

        TESTS::

            sage: Bitset('110').difference_update(None)
            Traceback (most recent call last):
            ...
            TypeError: other cannot be None"""
    @overload
    def difference_update(self, _None) -> Any:
        """Bitset.difference_update(self, FrozenBitset other)

        File: /build/sagemath/src/sage/src/sage/data_structures/bitset.pyx (starting at line 1570)

        Update the bitset to the difference of ``self`` and ``other``.

        EXAMPLES::

            sage: a = Bitset('110')
            sage: a.difference_update(Bitset('0101'))
            sage: a
            1000
            sage: a_set = set(a)
            sage: a.difference_update(FrozenBitset('010101' * 10)); a
            100000000000000000000000000000000000000000000000000000000000
            sage: a_set.difference_update(FrozenBitset('010101' * 10))
            sage: a_set == set(a)
            True
            sage: a.difference_update(FrozenBitset('110'))
            sage: a_set.difference_update(FrozenBitset('110'))
            sage: a_set == set(a)
            True
            sage: a.difference_update(FrozenBitset('01010' * 20)); a
            0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
            sage: a_set.difference_update(FrozenBitset('01010' * 20))
            sage: a_set == set(a)
            True
            sage: b = Bitset('10101' * 20)
            sage: b_set = set(b)
            sage: b.difference_update(FrozenBitset('1' * 5)); b
            0000010101101011010110101101011010110101101011010110101101011010110101101011010110101101011010110101
            sage: b_set.difference_update(FrozenBitset('1' * 5))
            sage: b_set == set(b)
            True

        TESTS::

            sage: Bitset('110').difference_update(None)
            Traceback (most recent call last):
            ...
            TypeError: other cannot be None"""
    @overload
    def discard(self, unsignedlongn) -> Any:
        """Bitset.discard(self, unsigned long n)

        File: /build/sagemath/src/sage/src/sage/data_structures/bitset.pyx (starting at line 1831)

        Update the bitset by removing ``n``.

        EXAMPLES::

            sage: a = Bitset('110')
            sage: a.discard(1)
            sage: a
            100
            sage: a.discard(2)
            sage: a.discard(4)
            sage: a
            100
            sage: a = Bitset('000001' * 15); sorted(list(a))
            [5, 11, 17, 23, 29, 35, 41, 47, 53, 59, 65, 71, 77, 83, 89]
            sage: a.discard(83); sorted(list(a))
            [5, 11, 17, 23, 29, 35, 41, 47, 53, 59, 65, 71, 77, 89]
            sage: a.discard(82); sorted(list(a))
            [5, 11, 17, 23, 29, 35, 41, 47, 53, 59, 65, 71, 77, 89]

        TESTS:

        The input ``n`` must be an integer. ::

            sage: Bitset('110').discard(None)
            Traceback (most recent call last):
            ...
            TypeError: an integer is required"""
    @overload
    def discard(self, _None) -> Any:
        """Bitset.discard(self, unsigned long n)

        File: /build/sagemath/src/sage/src/sage/data_structures/bitset.pyx (starting at line 1831)

        Update the bitset by removing ``n``.

        EXAMPLES::

            sage: a = Bitset('110')
            sage: a.discard(1)
            sage: a
            100
            sage: a.discard(2)
            sage: a.discard(4)
            sage: a
            100
            sage: a = Bitset('000001' * 15); sorted(list(a))
            [5, 11, 17, 23, 29, 35, 41, 47, 53, 59, 65, 71, 77, 83, 89]
            sage: a.discard(83); sorted(list(a))
            [5, 11, 17, 23, 29, 35, 41, 47, 53, 59, 65, 71, 77, 89]
            sage: a.discard(82); sorted(list(a))
            [5, 11, 17, 23, 29, 35, 41, 47, 53, 59, 65, 71, 77, 89]

        TESTS:

        The input ``n`` must be an integer. ::

            sage: Bitset('110').discard(None)
            Traceback (most recent call last):
            ...
            TypeError: an integer is required"""
    @overload
    def intersection_update(self, FrozenBitsetother) -> Any:
        """Bitset.intersection_update(self, FrozenBitset other)

        File: /build/sagemath/src/sage/src/sage/data_structures/bitset.pyx (starting at line 1501)

        Update the bitset to the intersection of ``self`` and ``other``.

        EXAMPLES::

            sage: a = Bitset('110')
            sage: a.intersection_update(Bitset('0101'))
            sage: a
            0100
            sage: a_set = set(a)
            sage: a.intersection_update(Bitset('0110' * 25))
            sage: a
            0100000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
            sage: a_set.intersection_update(Bitset('0110' * 25))
            sage: set(a) == a_set
            True

        TESTS::

            sage: Bitset('110').intersection_update(None)
            Traceback (most recent call last):
            ...
            TypeError: other cannot be None"""
    @overload
    def intersection_update(self, _None) -> Any:
        """Bitset.intersection_update(self, FrozenBitset other)

        File: /build/sagemath/src/sage/src/sage/data_structures/bitset.pyx (starting at line 1501)

        Update the bitset to the intersection of ``self`` and ``other``.

        EXAMPLES::

            sage: a = Bitset('110')
            sage: a.intersection_update(Bitset('0101'))
            sage: a
            0100
            sage: a_set = set(a)
            sage: a.intersection_update(Bitset('0110' * 25))
            sage: a
            0100000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
            sage: a_set.intersection_update(Bitset('0110' * 25))
            sage: set(a) == a_set
            True

        TESTS::

            sage: Bitset('110').intersection_update(None)
            Traceback (most recent call last):
            ...
            TypeError: other cannot be None"""
    @overload
    def pop(self) -> Any:
        """Bitset.pop(self)

        File: /build/sagemath/src/sage/src/sage/data_structures/bitset.pyx (starting at line 1864)

        Remove and return an arbitrary element from the set.

        This raises a :exc:`KeyError` if the set is empty.

        EXAMPLES::

            sage: a = Bitset('011')
            sage: a.pop()
            1
            sage: a
            001
            sage: a.pop()
            2
            sage: a
            000
            sage: a.pop()
            Traceback (most recent call last):
            ...
            KeyError: 'pop from an empty set'
            sage: a = Bitset('0001'*32)
            sage: a.pop()
            3
            sage: [a.pop() for _ in range(20)]
            [7, 11, 15, 19, 23, 27, 31, 35, 39, 43, 47, 51, 55, 59, 63, 67, 71, 75, 79, 83]"""
    @overload
    def pop(self) -> Any:
        """Bitset.pop(self)

        File: /build/sagemath/src/sage/src/sage/data_structures/bitset.pyx (starting at line 1864)

        Remove and return an arbitrary element from the set.

        This raises a :exc:`KeyError` if the set is empty.

        EXAMPLES::

            sage: a = Bitset('011')
            sage: a.pop()
            1
            sage: a
            001
            sage: a.pop()
            2
            sage: a
            000
            sage: a.pop()
            Traceback (most recent call last):
            ...
            KeyError: 'pop from an empty set'
            sage: a = Bitset('0001'*32)
            sage: a.pop()
            3
            sage: [a.pop() for _ in range(20)]
            [7, 11, 15, 19, 23, 27, 31, 35, 39, 43, 47, 51, 55, 59, 63, 67, 71, 75, 79, 83]"""
    @overload
    def pop(self) -> Any:
        """Bitset.pop(self)

        File: /build/sagemath/src/sage/src/sage/data_structures/bitset.pyx (starting at line 1864)

        Remove and return an arbitrary element from the set.

        This raises a :exc:`KeyError` if the set is empty.

        EXAMPLES::

            sage: a = Bitset('011')
            sage: a.pop()
            1
            sage: a
            001
            sage: a.pop()
            2
            sage: a
            000
            sage: a.pop()
            Traceback (most recent call last):
            ...
            KeyError: 'pop from an empty set'
            sage: a = Bitset('0001'*32)
            sage: a.pop()
            3
            sage: [a.pop() for _ in range(20)]
            [7, 11, 15, 19, 23, 27, 31, 35, 39, 43, 47, 51, 55, 59, 63, 67, 71, 75, 79, 83]"""
    @overload
    def pop(self) -> Any:
        """Bitset.pop(self)

        File: /build/sagemath/src/sage/src/sage/data_structures/bitset.pyx (starting at line 1864)

        Remove and return an arbitrary element from the set.

        This raises a :exc:`KeyError` if the set is empty.

        EXAMPLES::

            sage: a = Bitset('011')
            sage: a.pop()
            1
            sage: a
            001
            sage: a.pop()
            2
            sage: a
            000
            sage: a.pop()
            Traceback (most recent call last):
            ...
            KeyError: 'pop from an empty set'
            sage: a = Bitset('0001'*32)
            sage: a.pop()
            3
            sage: [a.pop() for _ in range(20)]
            [7, 11, 15, 19, 23, 27, 31, 35, 39, 43, 47, 51, 55, 59, 63, 67, 71, 75, 79, 83]"""
    @overload
    def pop(self) -> Any:
        """Bitset.pop(self)

        File: /build/sagemath/src/sage/src/sage/data_structures/bitset.pyx (starting at line 1864)

        Remove and return an arbitrary element from the set.

        This raises a :exc:`KeyError` if the set is empty.

        EXAMPLES::

            sage: a = Bitset('011')
            sage: a.pop()
            1
            sage: a
            001
            sage: a.pop()
            2
            sage: a
            000
            sage: a.pop()
            Traceback (most recent call last):
            ...
            KeyError: 'pop from an empty set'
            sage: a = Bitset('0001'*32)
            sage: a.pop()
            3
            sage: [a.pop() for _ in range(20)]
            [7, 11, 15, 19, 23, 27, 31, 35, 39, 43, 47, 51, 55, 59, 63, 67, 71, 75, 79, 83]"""
    @overload
    def pop(self) -> Any:
        """Bitset.pop(self)

        File: /build/sagemath/src/sage/src/sage/data_structures/bitset.pyx (starting at line 1864)

        Remove and return an arbitrary element from the set.

        This raises a :exc:`KeyError` if the set is empty.

        EXAMPLES::

            sage: a = Bitset('011')
            sage: a.pop()
            1
            sage: a
            001
            sage: a.pop()
            2
            sage: a
            000
            sage: a.pop()
            Traceback (most recent call last):
            ...
            KeyError: 'pop from an empty set'
            sage: a = Bitset('0001'*32)
            sage: a.pop()
            3
            sage: [a.pop() for _ in range(20)]
            [7, 11, 15, 19, 23, 27, 31, 35, 39, 43, 47, 51, 55, 59, 63, 67, 71, 75, 79, 83]"""
    @overload
    def remove(self, unsignedlongn) -> Any:
        """Bitset.remove(self, unsigned long n)

        File: /build/sagemath/src/sage/src/sage/data_structures/bitset.pyx (starting at line 1789)

        Update the bitset by removing ``n``.

        This raises a :exc:`KeyError` if ``n`` is not contained
        in the bitset.

        EXAMPLES::

            sage: a = Bitset('110')
            sage: a.remove(1)
            sage: a
            100
            sage: a.remove(2)
            Traceback (most recent call last):
            ...
            KeyError: 2
            sage: a.remove(4)
            Traceback (most recent call last):
            ...
            KeyError: 4
            sage: a
            100
            sage: a = Bitset('000001' * 15); sorted(list(a))
            [5, 11, 17, 23, 29, 35, 41, 47, 53, 59, 65, 71, 77, 83, 89]
            sage: a.remove(83); sorted(list(a))
            [5, 11, 17, 23, 29, 35, 41, 47, 53, 59, 65, 71, 77, 89]

        TESTS:

        The input ``n`` must be an integer. ::

            sage: Bitset('110').remove(None)
            Traceback (most recent call last):
            ...
            TypeError: an integer is required"""
    @overload
    def remove(self, _None) -> Any:
        """Bitset.remove(self, unsigned long n)

        File: /build/sagemath/src/sage/src/sage/data_structures/bitset.pyx (starting at line 1789)

        Update the bitset by removing ``n``.

        This raises a :exc:`KeyError` if ``n`` is not contained
        in the bitset.

        EXAMPLES::

            sage: a = Bitset('110')
            sage: a.remove(1)
            sage: a
            100
            sage: a.remove(2)
            Traceback (most recent call last):
            ...
            KeyError: 2
            sage: a.remove(4)
            Traceback (most recent call last):
            ...
            KeyError: 4
            sage: a
            100
            sage: a = Bitset('000001' * 15); sorted(list(a))
            [5, 11, 17, 23, 29, 35, 41, 47, 53, 59, 65, 71, 77, 83, 89]
            sage: a.remove(83); sorted(list(a))
            [5, 11, 17, 23, 29, 35, 41, 47, 53, 59, 65, 71, 77, 89]

        TESTS:

        The input ``n`` must be an integer. ::

            sage: Bitset('110').remove(None)
            Traceback (most recent call last):
            ...
            TypeError: an integer is required"""
    @overload
    def symmetric_difference_update(self, FrozenBitsetother) -> Any:
        """Bitset.symmetric_difference_update(self, FrozenBitset other)

        File: /build/sagemath/src/sage/src/sage/data_structures/bitset.pyx (starting at line 1667)

        Update the bitset to the symmetric difference of ``self`` and
        ``other``.

        EXAMPLES::

            sage: a = Bitset('110')
            sage: a.symmetric_difference_update(Bitset('0101'))
            sage: a
            1001
            sage: a_set = set(a)
            sage: a.symmetric_difference_update(FrozenBitset('010101' * 10)); a
            110001010101010101010101010101010101010101010101010101010101
            sage: a_set.symmetric_difference_update(FrozenBitset('010101' * 10))
            sage: a_set == set(a)
            True
            sage: a.symmetric_difference_update(FrozenBitset('01010' * 20)); a
            1001011111000001111100000111110000011111000001111100000111110101001010010100101001010010100101001010
            sage: a_set.symmetric_difference_update(FrozenBitset('01010' * 20))
            sage: a_set == set(a)
            True
            sage: b = Bitset('10101' * 20)
            sage: b_set = set(b)
            sage: b.symmetric_difference_update( FrozenBitset('1' * 5)); b
            0101010101101011010110101101011010110101101011010110101101011010110101101011010110101101011010110101
            sage: b_set.symmetric_difference_update( FrozenBitset('1' * 5))
            sage: b_set == set(b)
            True

        TESTS::

            sage: Bitset('110').symmetric_difference_update(None)
            Traceback (most recent call last):
            ...
            TypeError: other cannot be None"""
    @overload
    def symmetric_difference_update(self, _None) -> Any:
        """Bitset.symmetric_difference_update(self, FrozenBitset other)

        File: /build/sagemath/src/sage/src/sage/data_structures/bitset.pyx (starting at line 1667)

        Update the bitset to the symmetric difference of ``self`` and
        ``other``.

        EXAMPLES::

            sage: a = Bitset('110')
            sage: a.symmetric_difference_update(Bitset('0101'))
            sage: a
            1001
            sage: a_set = set(a)
            sage: a.symmetric_difference_update(FrozenBitset('010101' * 10)); a
            110001010101010101010101010101010101010101010101010101010101
            sage: a_set.symmetric_difference_update(FrozenBitset('010101' * 10))
            sage: a_set == set(a)
            True
            sage: a.symmetric_difference_update(FrozenBitset('01010' * 20)); a
            1001011111000001111100000111110000011111000001111100000111110101001010010100101001010010100101001010
            sage: a_set.symmetric_difference_update(FrozenBitset('01010' * 20))
            sage: a_set == set(a)
            True
            sage: b = Bitset('10101' * 20)
            sage: b_set = set(b)
            sage: b.symmetric_difference_update( FrozenBitset('1' * 5)); b
            0101010101101011010110101101011010110101101011010110101101011010110101101011010110101101011010110101
            sage: b_set.symmetric_difference_update( FrozenBitset('1' * 5))
            sage: b_set == set(b)
            True

        TESTS::

            sage: Bitset('110').symmetric_difference_update(None)
            Traceback (most recent call last):
            ...
            TypeError: other cannot be None"""
    @overload
    def update(self, FrozenBitsetother) -> Any:
        """Bitset.update(self, FrozenBitset other)

        File: /build/sagemath/src/sage/src/sage/data_structures/bitset.pyx (starting at line 1429)

        Update the bitset to include items in ``other``.

        EXAMPLES::

            sage: a = Bitset('110')
            sage: a.update(Bitset('0101'))
            sage: a
            1101
            sage: a_set = set(a)
            sage: a.update(Bitset('00011' * 25))
            sage: a
            11011000110001100011000110001100011000110001100011000110001100011000110001100011000110001100011000110001100011000110001100011
            sage: a_set.update(Bitset('00011' * 25))
            sage: set(a) == a_set
            True

        TESTS:

        During update, ``other`` cannot be ``None``. ::

            sage: a = Bitset('1101')
            sage: a.update(None)
            Traceback (most recent call last):
            ...
            TypeError: other cannot be None"""
    @overload
    def update(self, _None) -> Any:
        """Bitset.update(self, FrozenBitset other)

        File: /build/sagemath/src/sage/src/sage/data_structures/bitset.pyx (starting at line 1429)

        Update the bitset to include items in ``other``.

        EXAMPLES::

            sage: a = Bitset('110')
            sage: a.update(Bitset('0101'))
            sage: a
            1101
            sage: a_set = set(a)
            sage: a.update(Bitset('00011' * 25))
            sage: a
            11011000110001100011000110001100011000110001100011000110001100011000110001100011000110001100011000110001100011000110001100011
            sage: a_set.update(Bitset('00011' * 25))
            sage: set(a) == a_set
            True

        TESTS:

        During update, ``other`` cannot be ``None``. ::

            sage: a = Bitset('1101')
            sage: a.update(None)
            Traceback (most recent call last):
            ...
            TypeError: other cannot be None"""
    def __copy__(self) -> Any:
        """Bitset.__copy__(self)

        File: /build/sagemath/src/sage/src/sage/data_structures/bitset.pyx (starting at line 1280)

        Return a copy of ``self``.

        EXAMPLES::

            sage: a = Bitset('10101')
            sage: from copy import copy
            sage: b = copy(a)
            sage: b is a
            False
            sage: b == a
            True
            sage: c = Bitset('1010' * 32)
            sage: d = copy(c)
            sage: d is c
            False
            sage: d == c
            True"""
    def __eq__(self, other: object) -> bool:
        """Return self==value."""
    def __ge__(self, other: object) -> bool:
        """Return self>=value."""
    def __gt__(self, other: object) -> bool:
        """Return self>value."""
    def __hash__(self) -> Any:
        """Bitset.__hash__(self)

        File: /build/sagemath/src/sage/src/sage/data_structures/bitset.pyx (starting at line 1304)

        Raise an error, since mutable ``Bitset``s are not hashable.

        EXAMPLES::

            sage: hash(Bitset('110'))
            Traceback (most recent call last):
            ...
            TypeError: Bitset objects are unhashable; use FrozenBitset"""
    def __iand__(self, FrozenBitsetother) -> Any:
        """Bitset.__iand__(self, FrozenBitset other)

        File: /build/sagemath/src/sage/src/sage/data_structures/bitset.pyx (starting at line 1541)

        Update the bitset to the intersection of ``self`` and ``other``.

        EXAMPLES::

            sage: a = Bitset('110')
            sage: a &= Bitset('0101')
            sage: a
            0100
            sage: a_set = set(a)
            sage: a &= Bitset('0110' * 25)
            sage: a
            0100000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
            sage: a_set &= set(Bitset('0110' * 25))
            sage: a_set == set(a)
            True

        TESTS::

            sage: a = Bitset('110')
            sage: a &= None
            Traceback (most recent call last):
            ...
            TypeError: Argument 'other' has incorrect type (expected sage.data_structures.bitset.FrozenBitset, got NoneType)"""
    def __ior__(self, FrozenBitsetother) -> Any:
        """Bitset.__ior__(self, FrozenBitset other)

        File: /build/sagemath/src/sage/src/sage/data_structures/bitset.pyx (starting at line 1472)

        Update the bitset to include items in ``other``.

        EXAMPLES::

            sage: a = Bitset('110')
            sage: a |= Bitset('0101')
            sage: a
            1101
            sage: a_set = set(a)
            sage: a |= Bitset('00011' * 25)
            sage: a
            11011000110001100011000110001100011000110001100011000110001100011000110001100011000110001100011000110001100011000110001100011
            sage: a_set |= set(Bitset('00011' * 25))
            sage: set(a) == a_set
            True

        TESTS::

            sage: a = Bitset('110')
            sage: a |= None
            Traceback (most recent call last):
            ...
            TypeError: Argument 'other' has incorrect type (expected sage.data_structures.bitset.FrozenBitset, got NoneType)"""
    def __isub__(self, FrozenBitsetother) -> Any:
        """Bitset.__isub__(self, FrozenBitset other)

        File: /build/sagemath/src/sage/src/sage/data_structures/bitset.pyx (starting at line 1625)

        Update the bitset to the difference of ``self`` and ``other``.

        EXAMPLES::

            sage: a = Bitset('110')
            sage: a -= Bitset('0101')
            sage: a
            1000
            sage: a_set = set(a)
            sage: a -= FrozenBitset('010101' * 10); a
            100000000000000000000000000000000000000000000000000000000000
            sage: a_set -= set(FrozenBitset('010101' * 10))
            sage: a_set == set(a)
            True
            sage: a = Bitset('110')
            sage: a_set = set(a)
            sage: a -= FrozenBitset('01010' * 20); a
            1000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
            sage: a_set -= set(FrozenBitset('01010' * 20))
            sage: a_set == set(a)
            True
            sage: b = FrozenBitset('10101' * 20)
            sage: b_set = set(b)
            sage: b -= FrozenBitset('1' * 5); b
            0000010101101011010110101101011010110101101011010110101101011010110101101011010110101101011010110101
            sage: b_set -= FrozenBitset('1' * 5)
            sage: b_set == set(b)
            True

        TESTS::

            sage: a = Bitset('110')
            sage: a -= None
            Traceback (most recent call last):
            ...
            TypeError: Argument 'other' has incorrect type (expected sage.data_structures.bitset.FrozenBitset, got NoneType)"""
    def __ixor__(self, FrozenBitsetother) -> Any:
        """Bitset.__ixor__(self, FrozenBitset other)

        File: /build/sagemath/src/sage/src/sage/data_structures/bitset.pyx (starting at line 1719)

        Update the bitset to the symmetric difference of ``self`` and
        ``other``.

        EXAMPLES::

            sage: a = Bitset('110')
            sage: a ^^=Bitset('0101')
            sage: a
            1001
            sage: a_set = set(a)
            sage: a ^^= FrozenBitset('010101' * 10); a
            110001010101010101010101010101010101010101010101010101010101
            sage: a_set ^^= set(FrozenBitset('010101' * 10))
            sage: a_set == set(a)
            True
            sage: a ^^= FrozenBitset('01010' * 20); a
            1001011111000001111100000111110000011111000001111100000111110101001010010100101001010010100101001010
            sage: a_set ^^= set(FrozenBitset('01010' * 20))
            sage: a_set == set(a)
            True
            sage: b = Bitset('10101' * 20)
            sage: b_set = set(b)
            sage: b ^^= FrozenBitset('1' * 5); b
            0101010101101011010110101101011010110101101011010110101101011010110101101011010110101101011010110101
            sage: b_set ^^= set(FrozenBitset('1' * 5))
            sage: b_set == set(b)
            True

        TESTS::

            sage: a = Bitset('110')
            sage: a ^^= None
            Traceback (most recent call last):
            ...
            TypeError: Argument 'other' has incorrect type (expected sage.data_structures.bitset.FrozenBitset, got NoneType)"""
    def __le__(self, other: object) -> bool:
        """Return self<=value."""
    def __lt__(self, other: object) -> bool:
        """Return self<value."""
    def __ne__(self, other: object) -> bool:
        """Return self!=value."""

class FrozenBitset:
    '''FrozenBitset(iter=None, capacity=None)

    File: /build/sagemath/src/sage/src/sage/data_structures/bitset.pyx (starting at line 38)

    A frozen bitset class which leverages inline Cython functions for
    creating and manipulating bitsets.

    A bitset can be thought of in two ways.  First, as a set of elements
    from the universe of the `n` natural numbers `0, 1, \\dots, n-1` (where
    the capacity `n` can be specified), with typical set operations such as
    intersection, union, symmetric difference, etc.  Secondly, a bitset can
    be thought of as a binary vector with typical binary operations such as
    ``and``, ``or``, ``xor``, etc.  This class supports both interfaces.

    The interface in this class mirrors the interface in the ``frozenset``
    data type of Python. See the Python documentation on `set types
    <https://docs.python.org/library/stdtypes.html#set-types-set-frozenset>`_
    for more details on Python\'s ``set`` and ``frozenset`` classes.

    .. warning::

        This class is most likely to be useful as a way to store
        Cython bitsets in Python data structures, acting on them using
        the Cython inline functions.  If you want to use this class
        for a Python set type, the Python ``frozenset`` data type may
        be faster.

    INPUT:

    - ``iter`` -- initialization parameter (default: ``None``); valid inputs
      are:

      - :class:`Bitset` and :class:`FrozenBitset` -- If this is a
        :class:`Bitset` or :class:`FrozenBitset`, then it is copied

      - ``None`` -- if ``None``, then the bitset is set to the empty set

      - ``string`` -- if a nonempty string, then the bitset is initialized by
        including an element if the index of the string is ``1``. If the
        string is empty, then raise a :exc:`ValueError`.

      - ``iterable`` -- if an iterable, then it is assumed to contain a list of
        nonnegative integers and those integers are placed in the set

    - ``capacity`` -- (default: ``None``) the maximum capacity of the bitset.
      If this is not specified, then it is automatically calculated from the
      passed iterable.  It must be at least one.

    OUTPUT: none

    The string representation of a :class:`FrozenBitset` ``FB`` can be
    understood as follows. Let `B = b_0 b_1 b_2 \\cdots b_k` be the string
    representation of the bitset ``FB``, where each `b_i \\in \\{0, 1\\}`. We
    read the `b_i` from left to right. If `b_i = 1`, then the nonnegative
    integer `i` is in the bitset ``FB``. Similarly, if `b_i = 0`, then `i`
    is not in ``FB``. In other words, ``FB`` is a subset of
    `\\{0, 1, 2, \\dots, k\\}` and the membership in ``FB`` of each `i` is
    determined by the binary value `b_i`.

    .. SEEALSO::

        - :class:`Bitset`

        - Python\'s `set types <https://docs.python.org/library/stdtypes.html#set-types-set-frozenset>`_

    EXAMPLES:

    The default bitset, which has capacity 1::

        sage: FrozenBitset()
        0
        sage: FrozenBitset(None)
        0

    Trying to create an empty bitset fails::

        sage: FrozenBitset([])
        Traceback (most recent call last):
        ...
        ValueError: Bitsets must not be empty
        sage: FrozenBitset(list())
        Traceback (most recent call last):
        ...
        ValueError: Bitsets must not be empty
        sage: FrozenBitset(())
        Traceback (most recent call last):
        ...
        ValueError: Bitsets must not be empty
        sage: FrozenBitset(tuple())
        Traceback (most recent call last):
        ...
        ValueError: Bitsets must not be empty
        sage: FrozenBitset("")
        Traceback (most recent call last):
        ...
        ValueError: Bitsets must not be empty

    We can create the all-zero bitset as follows::

        sage: FrozenBitset(capacity=10)
        0000000000
        sage: FrozenBitset([], capacity=10)
        0000000000

    We can initialize a :class:`FrozenBitset` with a :class:`Bitset` or
    another :class:`FrozenBitset`, and compare them for equality. As they
    are logically the same bitset, the equality test should return ``True``.
    Furthermore, each bitset is a subset of the other. ::

        sage: def bitcmp(a, b, c):  # custom function for comparing bitsets
        ....:     print(a == b == c)
        ....:     print((a <= b, b <= c, a <= c))
        ....:     print((a >= b, b >= c, a >= c))
        ....:     print((a != b, b != c, a != c))
        sage: a = Bitset("1010110"); b = FrozenBitset(a); c = FrozenBitset(b)
        sage: a; b; c
        1010110
        1010110
        1010110
        sage: a < b, b < c, a < c
        (False, False, False)
        sage: a > b, b > c, a > c
        (False, False, False)
        sage: bitcmp(a, b, c)
        True
        (True, True, True)
        (True, True, True)
        (False, False, False)

    Try a random bitset::

        sage: a = Bitset(randint(0, 1) for n in range(randint(1, 10^4)))
        sage: b = FrozenBitset(a); c = FrozenBitset(b)
        sage: bitcmp(a, b, c)
        True
        (True, True, True)
        (True, True, True)
        (False, False, False)

    A bitset with a hard-coded bitstring::

        sage: FrozenBitset(\'101\')
        101

    For a string, only those positions with ``1`` would be initialized to ``1``
    in the corresponding position in the bitset. All other characters in the
    string, including ``0``, are set to ``0`` in the resulting bitset. ::

        sage: FrozenBitset(\'a\')
        0
        sage: FrozenBitset(\'abc\')
        000
        sage: FrozenBitset(\'abc1\')
        0001
        sage: FrozenBitset(\'0abc1\')
        00001
        sage: FrozenBitset(\'0abc10\')
        000010
        sage: FrozenBitset(\'0a*c10\')
        000010

    Represent the first 10 primes as a bitset. The primes are stored as a
    list and as a tuple. We then recover the primes from its bitset
    representation, and query the bitset for its length (how many elements
    it contains) and whether an element is in the bitset. Note that the
    length of a bitset is different from its capacity. The length counts
    the number of elements currently in the bitset, while the capacity
    is the number of elements that the bitset can hold. ::

        sage: p = primes_first_n(10); p                                                 # needs sage.libs.pari
        [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
        sage: tuple(p)                                                                  # needs sage.libs.pari
        (2, 3, 5, 7, 11, 13, 17, 19, 23, 29)
        sage: F = FrozenBitset(p); F; FrozenBitset(tuple(p))                            # needs sage.libs.pari
        001101010001010001010001000001
        001101010001010001010001000001

    Recover the primes from the bitset::

        sage: for b in F:                                                               # needs sage.libs.pari
        ....:     print(b)
        2
        3
        ...
        29
        sage: list(F)                                                                   # needs sage.libs.pari
        [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]

    Query the bitset::

        sage: # needs sage.libs.pari
        sage: len(F)
        10
        sage: len(list(F))
        10
        sage: F.capacity()
        30
        sage: s = str(F); len(s)
        30
        sage: 2 in F
        True
        sage: 1 in F
        False

    A random iterable, with all duplicate elements removed::

        sage: L = [randint(0, 100) for n in range(randint(1, 10^4))]
        sage: FrozenBitset(L) == FrozenBitset(list(set(L)))
        True
        sage: FrozenBitset(tuple(L)) == FrozenBitset(tuple(set(L)))
        True

    TESTS:

    Loading and dumping objects::

        sage: a = FrozenBitset(\'1101\')
        sage: loads(dumps(a)) == a
        True
        sage: a = FrozenBitset(\'1101\' * 64)
        sage: loads(dumps(a)) == a
        True

    If ``iter`` is a nonempty string and ``capacity`` is specified, then
    ``capacity`` must match the number of elements in ``iter``::

        sage: FrozenBitset("110110", capacity=3)
        Traceback (most recent call last):
        ...
        ValueError: bitset capacity does not match passed string
        sage: FrozenBitset("110110", capacity=100)
        Traceback (most recent call last):
        ...
        ValueError: bitset capacity does not match passed string

    The parameter ``capacity`` must be positive::

        sage: FrozenBitset("110110", capacity=0)
        Traceback (most recent call last):
        ...
        ValueError: bitset capacity must be greater than 0
        sage: FrozenBitset("110110", capacity=-2)
        Traceback (most recent call last):
        ...
        OverflowError: can...t convert negative value to mp_bitcnt_t'''
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    def __init__(self, iter=..., capacity=...) -> Any:
        """File: /build/sagemath/src/sage/src/sage/data_structures/bitset.pyx (starting at line 314)

                Initialize a bitset.

                See the class documentation of ``FrozenBitset`` for details on the
                parameters.

                EXAMPLES::

                    sage: FrozenBitset(capacity=3)
                    000
                    sage: FrozenBitset('11011')
                    11011
                    sage: FrozenBitset('110' * 32)
                    110110110110110110110110110110110110110110110110110110110110110110110110110110110110110110110110
                    sage: FrozenBitset([0,3,2])
                    1011
                    sage: FrozenBitset(set([0,3,2]))
                    1011
                    sage: FrozenBitset(FrozenBitset('11011'))
                    11011
                    sage: FrozenBitset([0,3,2], capacity=10)
                    1011000000
                    sage: FrozenBitset([i for i in range(100) if i % 2 == 0])
                    101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101

                TESTS:

                The capacity must be at least one::

                    sage: FrozenBitset()
                    0

                If capacity is specified, it must match up with the
                initialization items::

                    sage: FrozenBitset('10', capacity=3)
                    Traceback (most recent call last):
                    ...
                    ValueError: bitset capacity does not match passed string
                    sage: FrozenBitset([0,3,2], capacity=2)
                    Traceback (most recent call last):
                    ...
                    ValueError: bitset capacity does not allow storing the passed iterable
                    sage: FrozenBitset(FrozenBitset('1101'), capacity=2)
                    Traceback (most recent call last):
                    ...
                    ValueError: bitset capacity does not match passed bitset
                    sage: FrozenBitset(FrozenBitset('1101'), capacity=5)
                    Traceback (most recent call last):
                    ...
                    ValueError: bitset capacity does not match passed bitset
        """
    @overload
    def capacity(self) -> long:
        """FrozenBitset.capacity(self) -> long

        File: /build/sagemath/src/sage/src/sage/data_structures/bitset.pyx (starting at line 519)

        Return the size of the underlying bitset.

        The maximum value that can be stored in the current underlying
        bitset is ``self.capacity() - 1``.

        EXAMPLES::

            sage: FrozenBitset('11000').capacity()
            5
            sage: FrozenBitset('110' * 32).capacity()
            96
            sage: FrozenBitset(range(20), capacity=450).capacity()
            450"""
    @overload
    def capacity(self) -> Any:
        """FrozenBitset.capacity(self) -> long

        File: /build/sagemath/src/sage/src/sage/data_structures/bitset.pyx (starting at line 519)

        Return the size of the underlying bitset.

        The maximum value that can be stored in the current underlying
        bitset is ``self.capacity() - 1``.

        EXAMPLES::

            sage: FrozenBitset('11000').capacity()
            5
            sage: FrozenBitset('110' * 32).capacity()
            96
            sage: FrozenBitset(range(20), capacity=450).capacity()
            450"""
    @overload
    def capacity(self) -> Any:
        """FrozenBitset.capacity(self) -> long

        File: /build/sagemath/src/sage/src/sage/data_structures/bitset.pyx (starting at line 519)

        Return the size of the underlying bitset.

        The maximum value that can be stored in the current underlying
        bitset is ``self.capacity() - 1``.

        EXAMPLES::

            sage: FrozenBitset('11000').capacity()
            5
            sage: FrozenBitset('110' * 32).capacity()
            96
            sage: FrozenBitset(range(20), capacity=450).capacity()
            450"""
    @overload
    def capacity(self) -> Any:
        """FrozenBitset.capacity(self) -> long

        File: /build/sagemath/src/sage/src/sage/data_structures/bitset.pyx (starting at line 519)

        Return the size of the underlying bitset.

        The maximum value that can be stored in the current underlying
        bitset is ``self.capacity() - 1``.

        EXAMPLES::

            sage: FrozenBitset('11000').capacity()
            5
            sage: FrozenBitset('110' * 32).capacity()
            96
            sage: FrozenBitset(range(20), capacity=450).capacity()
            450"""
    @overload
    def capacity(self) -> Any:
        """FrozenBitset.capacity(self) -> long

        File: /build/sagemath/src/sage/src/sage/data_structures/bitset.pyx (starting at line 519)

        Return the size of the underlying bitset.

        The maximum value that can be stored in the current underlying
        bitset is ``self.capacity() - 1``.

        EXAMPLES::

            sage: FrozenBitset('11000').capacity()
            5
            sage: FrozenBitset('110' * 32).capacity()
            96
            sage: FrozenBitset(range(20), capacity=450).capacity()
            450"""
    def complement(self) -> Any:
        """FrozenBitset.complement(self)

        File: /build/sagemath/src/sage/src/sage/data_structures/bitset.pyx (starting at line 1176)

        Return the complement of ``self``.

        EXAMPLES::

            sage: ~FrozenBitset('10101')
            01010
            sage: ~FrozenBitset('11111'*10)
            00000000000000000000000000000000000000000000000000
            sage: x = FrozenBitset('10'*40)
            sage: x == ~x
            False
            sage: x == ~~x
            True
            sage: x|(~x) == FrozenBitset('11'*40)
            True
            sage: ~x == FrozenBitset('01'*40)
            True"""
    @overload
    def difference(self, FrozenBitsetother) -> Any:
        """FrozenBitset.difference(self, FrozenBitset other)

        File: /build/sagemath/src/sage/src/sage/data_structures/bitset.pyx (starting at line 1034)

        Return the difference of ``self`` and ``other``.

        EXAMPLES::

            sage: FrozenBitset('10101').difference(FrozenBitset('11100'))
            00001
            sage: FrozenBitset('11111' * 10).difference(FrozenBitset('010101' * 10))
            101010101010101010101010101010101010101010101010100000000000

        TESTS::

            sage: set(FrozenBitset('11111' * 10).difference(FrozenBitset('010101' * 10))) == set(FrozenBitset('11111' * 10)).difference(FrozenBitset('010101' * 10))
            True
            sage: set(FrozenBitset('1' * 5).difference(FrozenBitset('01010' * 20))) == set(FrozenBitset('1' * 5)).difference(FrozenBitset('01010' * 20))
            True
            sage: set(FrozenBitset('10101' * 20).difference(FrozenBitset('1' * 5))) == set(FrozenBitset('10101' * 20)).difference(FrozenBitset('1' * 5))
            True
            sage: FrozenBitset('10101').difference(None)
            Traceback (most recent call last):
            ...
            ValueError: other cannot be None"""
    @overload
    def difference(self, _None) -> Any:
        """FrozenBitset.difference(self, FrozenBitset other)

        File: /build/sagemath/src/sage/src/sage/data_structures/bitset.pyx (starting at line 1034)

        Return the difference of ``self`` and ``other``.

        EXAMPLES::

            sage: FrozenBitset('10101').difference(FrozenBitset('11100'))
            00001
            sage: FrozenBitset('11111' * 10).difference(FrozenBitset('010101' * 10))
            101010101010101010101010101010101010101010101010100000000000

        TESTS::

            sage: set(FrozenBitset('11111' * 10).difference(FrozenBitset('010101' * 10))) == set(FrozenBitset('11111' * 10)).difference(FrozenBitset('010101' * 10))
            True
            sage: set(FrozenBitset('1' * 5).difference(FrozenBitset('01010' * 20))) == set(FrozenBitset('1' * 5)).difference(FrozenBitset('01010' * 20))
            True
            sage: set(FrozenBitset('10101' * 20).difference(FrozenBitset('1' * 5))) == set(FrozenBitset('10101' * 20)).difference(FrozenBitset('1' * 5))
            True
            sage: FrozenBitset('10101').difference(None)
            Traceback (most recent call last):
            ...
            ValueError: other cannot be None"""
    @overload
    def intersection(self, FrozenBitsetother) -> Any:
        '''FrozenBitset.intersection(self, FrozenBitset other)

        File: /build/sagemath/src/sage/src/sage/data_structures/bitset.pyx (starting at line 964)

        Return the intersection of ``self`` and ``other``.

        EXAMPLES::

            sage: FrozenBitset(\'10101\').intersection(FrozenBitset(\'11100\'))
            10100
            sage: FrozenBitset(\'11111\' * 10).intersection(FrozenBitset(\'010101\' * 10))
            010101010101010101010101010101010101010101010101010000000000

        TESTS::

            sage: set(FrozenBitset(\'11111\' * 10).intersection(FrozenBitset(\'010101\' * 10))) == set(FrozenBitset(\'11111\' * 10)).intersection(FrozenBitset(\'010101\' * 10))
            True
            sage: set(FrozenBitset(\'1\' * 5).intersection(FrozenBitset(\'01010\' * 20))) == set(FrozenBitset(\'1\' * 5)).intersection(FrozenBitset(\'01010\' * 20))
            True
            sage: set(FrozenBitset(\'10101\' * 20).intersection(FrozenBitset(\'1\' * 5))) == set(FrozenBitset(\'10101\' * 20)).intersection(FrozenBitset(\'1\' * 5))
            True
            sage: FrozenBitset("101011").intersection(None)
            Traceback (most recent call last):
            ...
            ValueError: other cannot be None'''
    @overload
    def intersection(self, _None) -> Any:
        '''FrozenBitset.intersection(self, FrozenBitset other)

        File: /build/sagemath/src/sage/src/sage/data_structures/bitset.pyx (starting at line 964)

        Return the intersection of ``self`` and ``other``.

        EXAMPLES::

            sage: FrozenBitset(\'10101\').intersection(FrozenBitset(\'11100\'))
            10100
            sage: FrozenBitset(\'11111\' * 10).intersection(FrozenBitset(\'010101\' * 10))
            010101010101010101010101010101010101010101010101010000000000

        TESTS::

            sage: set(FrozenBitset(\'11111\' * 10).intersection(FrozenBitset(\'010101\' * 10))) == set(FrozenBitset(\'11111\' * 10)).intersection(FrozenBitset(\'010101\' * 10))
            True
            sage: set(FrozenBitset(\'1\' * 5).intersection(FrozenBitset(\'01010\' * 20))) == set(FrozenBitset(\'1\' * 5)).intersection(FrozenBitset(\'01010\' * 20))
            True
            sage: set(FrozenBitset(\'10101\' * 20).intersection(FrozenBitset(\'1\' * 5))) == set(FrozenBitset(\'10101\' * 20)).intersection(FrozenBitset(\'1\' * 5))
            True
            sage: FrozenBitset("101011").intersection(None)
            Traceback (most recent call last):
            ...
            ValueError: other cannot be None'''
    @overload
    def isdisjoint(self, FrozenBitsetother) -> bool:
        """FrozenBitset.isdisjoint(self, FrozenBitset other) -> bool

        File: /build/sagemath/src/sage/src/sage/data_structures/bitset.pyx (starting at line 746)

        Test to see if ``self`` is disjoint from ``other``.

        EXAMPLES::

            sage: FrozenBitset('11').isdisjoint(FrozenBitset('01'))
            False
            sage: FrozenBitset('01').isdisjoint(FrozenBitset('001'))
            True
            sage: FrozenBitset('00101').isdisjoint(FrozenBitset('110' * 35))
            False

        TESTS::

            sage: FrozenBitset('11').isdisjoint(None)
            Traceback (most recent call last):
            ...
            ValueError: other cannot be None"""
    @overload
    def isdisjoint(self, _None) -> Any:
        """FrozenBitset.isdisjoint(self, FrozenBitset other) -> bool

        File: /build/sagemath/src/sage/src/sage/data_structures/bitset.pyx (starting at line 746)

        Test to see if ``self`` is disjoint from ``other``.

        EXAMPLES::

            sage: FrozenBitset('11').isdisjoint(FrozenBitset('01'))
            False
            sage: FrozenBitset('01').isdisjoint(FrozenBitset('001'))
            True
            sage: FrozenBitset('00101').isdisjoint(FrozenBitset('110' * 35))
            False

        TESTS::

            sage: FrozenBitset('11').isdisjoint(None)
            Traceback (most recent call last):
            ...
            ValueError: other cannot be None"""
    @overload
    def isempty(self) -> bool:
        """FrozenBitset.isempty(self) -> bool

        File: /build/sagemath/src/sage/src/sage/data_structures/bitset.pyx (starting at line 557)

        Test if the bitset is empty.

        OUTPUT: boolean

        EXAMPLES::

            sage: FrozenBitset().isempty()
            True
            sage: FrozenBitset([1]).isempty()
            False
            sage: FrozenBitset([], capacity=110).isempty()
            True
            sage: FrozenBitset(range(99)).isempty()
            False"""
    @overload
    def isempty(self) -> Any:
        """FrozenBitset.isempty(self) -> bool

        File: /build/sagemath/src/sage/src/sage/data_structures/bitset.pyx (starting at line 557)

        Test if the bitset is empty.

        OUTPUT: boolean

        EXAMPLES::

            sage: FrozenBitset().isempty()
            True
            sage: FrozenBitset([1]).isempty()
            False
            sage: FrozenBitset([], capacity=110).isempty()
            True
            sage: FrozenBitset(range(99)).isempty()
            False"""
    @overload
    def isempty(self) -> Any:
        """FrozenBitset.isempty(self) -> bool

        File: /build/sagemath/src/sage/src/sage/data_structures/bitset.pyx (starting at line 557)

        Test if the bitset is empty.

        OUTPUT: boolean

        EXAMPLES::

            sage: FrozenBitset().isempty()
            True
            sage: FrozenBitset([1]).isempty()
            False
            sage: FrozenBitset([], capacity=110).isempty()
            True
            sage: FrozenBitset(range(99)).isempty()
            False"""
    @overload
    def isempty(self) -> Any:
        """FrozenBitset.isempty(self) -> bool

        File: /build/sagemath/src/sage/src/sage/data_structures/bitset.pyx (starting at line 557)

        Test if the bitset is empty.

        OUTPUT: boolean

        EXAMPLES::

            sage: FrozenBitset().isempty()
            True
            sage: FrozenBitset([1]).isempty()
            False
            sage: FrozenBitset([], capacity=110).isempty()
            True
            sage: FrozenBitset(range(99)).isempty()
            False"""
    @overload
    def isempty(self) -> Any:
        """FrozenBitset.isempty(self) -> bool

        File: /build/sagemath/src/sage/src/sage/data_structures/bitset.pyx (starting at line 557)

        Test if the bitset is empty.

        OUTPUT: boolean

        EXAMPLES::

            sage: FrozenBitset().isempty()
            True
            sage: FrozenBitset([1]).isempty()
            False
            sage: FrozenBitset([], capacity=110).isempty()
            True
            sage: FrozenBitset(range(99)).isempty()
            False"""
    @overload
    def issubset(self, FrozenBitsetother) -> bool:
        """FrozenBitset.issubset(self, FrozenBitset other) -> bool

        File: /build/sagemath/src/sage/src/sage/data_structures/bitset.pyx (starting at line 680)

        Test to see if ``self`` is a subset of ``other``.

        EXAMPLES::

            sage: FrozenBitset('11').issubset(FrozenBitset('01'))
            False
            sage: FrozenBitset('01').issubset(FrozenBitset('11'))
            True
            sage: FrozenBitset('01').issubset(FrozenBitset('01' * 45))
            True

        TESTS::

            sage: FrozenBitset('11').issubset(None)
            Traceback (most recent call last):
            ...
            ValueError: other cannot be None"""
    @overload
    def issubset(self, _None) -> Any:
        """FrozenBitset.issubset(self, FrozenBitset other) -> bool

        File: /build/sagemath/src/sage/src/sage/data_structures/bitset.pyx (starting at line 680)

        Test to see if ``self`` is a subset of ``other``.

        EXAMPLES::

            sage: FrozenBitset('11').issubset(FrozenBitset('01'))
            False
            sage: FrozenBitset('01').issubset(FrozenBitset('11'))
            True
            sage: FrozenBitset('01').issubset(FrozenBitset('01' * 45))
            True

        TESTS::

            sage: FrozenBitset('11').issubset(None)
            Traceback (most recent call last):
            ...
            ValueError: other cannot be None"""
    @overload
    def issuperset(self, FrozenBitsetother) -> bool:
        """FrozenBitset.issuperset(self, FrozenBitset other) -> bool

        File: /build/sagemath/src/sage/src/sage/data_structures/bitset.pyx (starting at line 713)

        Test to see if ``self`` is a superset of ``other``.

        EXAMPLES::

            sage: FrozenBitset('11').issuperset(FrozenBitset('01'))
            True
            sage: FrozenBitset('01').issuperset(FrozenBitset('11'))
            False
            sage: FrozenBitset('01').issuperset(FrozenBitset('10' * 45))
            False

        TESTS::

            sage: FrozenBitset('11').issuperset(None)
            Traceback (most recent call last):
            ...
            ValueError: other cannot be None"""
    @overload
    def issuperset(self, _None) -> Any:
        """FrozenBitset.issuperset(self, FrozenBitset other) -> bool

        File: /build/sagemath/src/sage/src/sage/data_structures/bitset.pyx (starting at line 713)

        Test to see if ``self`` is a superset of ``other``.

        EXAMPLES::

            sage: FrozenBitset('11').issuperset(FrozenBitset('01'))
            True
            sage: FrozenBitset('01').issuperset(FrozenBitset('11'))
            False
            sage: FrozenBitset('01').issuperset(FrozenBitset('10' * 45))
            False

        TESTS::

            sage: FrozenBitset('11').issuperset(None)
            Traceback (most recent call last):
            ...
            ValueError: other cannot be None"""
    @overload
    def symmetric_difference(self, FrozenBitsetother) -> Any:
        """FrozenBitset.symmetric_difference(self, FrozenBitset other)

        File: /build/sagemath/src/sage/src/sage/data_structures/bitset.pyx (starting at line 1103)

        Return the symmetric difference of ``self`` and ``other``.

        EXAMPLES::

            sage: FrozenBitset('10101').symmetric_difference(FrozenBitset('11100'))
            01001
            sage: FrozenBitset('11111' * 10).symmetric_difference(FrozenBitset('010101' * 10))
            101010101010101010101010101010101010101010101010100101010101

        TESTS::

            sage: set(FrozenBitset('11111' * 10).symmetric_difference(FrozenBitset('010101' * 10))) == set(FrozenBitset('11111' * 10)).symmetric_difference(FrozenBitset('010101' * 10))
            True
            sage: set(FrozenBitset('1' * 5).symmetric_difference(FrozenBitset('01010' * 20))) == set(FrozenBitset('1' * 5)).symmetric_difference(FrozenBitset('01010' * 20))
            True
            sage: set(FrozenBitset('10101' * 20).symmetric_difference(FrozenBitset('1' * 5))) == set(FrozenBitset('10101' * 20)).symmetric_difference(FrozenBitset('1' * 5))
            True
            sage: FrozenBitset('11111' * 10).symmetric_difference(None)
            Traceback (most recent call last):
            ...
            ValueError: other cannot be None"""
    @overload
    def symmetric_difference(self, _None) -> Any:
        """FrozenBitset.symmetric_difference(self, FrozenBitset other)

        File: /build/sagemath/src/sage/src/sage/data_structures/bitset.pyx (starting at line 1103)

        Return the symmetric difference of ``self`` and ``other``.

        EXAMPLES::

            sage: FrozenBitset('10101').symmetric_difference(FrozenBitset('11100'))
            01001
            sage: FrozenBitset('11111' * 10).symmetric_difference(FrozenBitset('010101' * 10))
            101010101010101010101010101010101010101010101010100101010101

        TESTS::

            sage: set(FrozenBitset('11111' * 10).symmetric_difference(FrozenBitset('010101' * 10))) == set(FrozenBitset('11111' * 10)).symmetric_difference(FrozenBitset('010101' * 10))
            True
            sage: set(FrozenBitset('1' * 5).symmetric_difference(FrozenBitset('01010' * 20))) == set(FrozenBitset('1' * 5)).symmetric_difference(FrozenBitset('01010' * 20))
            True
            sage: set(FrozenBitset('10101' * 20).symmetric_difference(FrozenBitset('1' * 5))) == set(FrozenBitset('10101' * 20)).symmetric_difference(FrozenBitset('1' * 5))
            True
            sage: FrozenBitset('11111' * 10).symmetric_difference(None)
            Traceback (most recent call last):
            ...
            ValueError: other cannot be None"""
    @overload
    def union(self, FrozenBitsetother) -> Any:
        """FrozenBitset.union(self, FrozenBitset other)

        File: /build/sagemath/src/sage/src/sage/data_structures/bitset.pyx (starting at line 908)

        Return the union of ``self`` and ``other``.

        EXAMPLES::

            sage: FrozenBitset('10101').union(FrozenBitset('11100'))
            11101
            sage: FrozenBitset('10101' * 10).union(FrozenBitset('01010' * 10))
            11111111111111111111111111111111111111111111111111

        TESTS::

            sage: set(FrozenBitset('10101' * 10).union(FrozenBitset('01010' * 10))) == set(FrozenBitset('10101' * 10)).union(FrozenBitset('01010' * 10))
            True
            sage: set(FrozenBitset('10101').union(FrozenBitset('01010' * 20))) == set(FrozenBitset('10101')).union(FrozenBitset('01010' * 20))
            True
            sage: set(FrozenBitset('10101' * 20).union(FrozenBitset('01010'))) == set(FrozenBitset('10101' * 20)).union(FrozenBitset('01010'))
            True
            sage: FrozenBitset('10101' * 10).union(None)
            Traceback (most recent call last):
            ...
            ValueError: other cannot be None"""
    @overload
    def union(self, _None) -> Any:
        """FrozenBitset.union(self, FrozenBitset other)

        File: /build/sagemath/src/sage/src/sage/data_structures/bitset.pyx (starting at line 908)

        Return the union of ``self`` and ``other``.

        EXAMPLES::

            sage: FrozenBitset('10101').union(FrozenBitset('11100'))
            11101
            sage: FrozenBitset('10101' * 10).union(FrozenBitset('01010' * 10))
            11111111111111111111111111111111111111111111111111

        TESTS::

            sage: set(FrozenBitset('10101' * 10).union(FrozenBitset('01010' * 10))) == set(FrozenBitset('10101' * 10)).union(FrozenBitset('01010' * 10))
            True
            sage: set(FrozenBitset('10101').union(FrozenBitset('01010' * 20))) == set(FrozenBitset('10101')).union(FrozenBitset('01010' * 20))
            True
            sage: set(FrozenBitset('10101' * 20).union(FrozenBitset('01010'))) == set(FrozenBitset('10101' * 20)).union(FrozenBitset('01010'))
            True
            sage: FrozenBitset('10101' * 10).union(None)
            Traceback (most recent call last):
            ...
            ValueError: other cannot be None"""
    def __and__(self, FrozenBitsetother) -> Any:
        '''FrozenBitset.__and__(self, FrozenBitset other)

        File: /build/sagemath/src/sage/src/sage/data_structures/bitset.pyx (starting at line 1004)

        Return the intersection of ``self`` and ``other``.

        EXAMPLES::

            sage: FrozenBitset(\'10101\') & FrozenBitset(\'11100\')
            10100
            sage: FrozenBitset(\'11111\' * 10) & FrozenBitset(\'010101\' * 10)
            010101010101010101010101010101010101010101010101010000000000

        TESTS::

            sage: set(FrozenBitset(\'11111\' * 10) & FrozenBitset(\'010101\' * 10)) == set(FrozenBitset(\'11111\' * 10)) & set(FrozenBitset(\'010101\' * 10))
            True
            sage: set(FrozenBitset(\'1\' * 5) & FrozenBitset(\'01010\' * 20)) == set(FrozenBitset(\'1\' * 5)) & set(FrozenBitset(\'01010\' * 20))
            True
            sage: set(FrozenBitset(\'10101\' * 20) & FrozenBitset(\'1\' * 5)) == set(FrozenBitset(\'10101\' * 20)) & set(FrozenBitset(\'1\' * 5))
            True
            sage: FrozenBitset("101011") & None
            Traceback (most recent call last):
            ...
            TypeError: Argument \'other\' has incorrect type (expected sage.data_structures.bitset.FrozenBitset, got NoneType)
            sage: None & FrozenBitset("101011")
            Traceback (most recent call last):
            ...
            AttributeError: \'NoneType\' object has no attribute \'intersection\'...'''
    def __bytes__(self) -> Any:
        """FrozenBitset.__bytes__(self)

        File: /build/sagemath/src/sage/src/sage/data_structures/bitset.pyx (starting at line 837)

        Return a bytes object representing the bitset as a binary vector.

        EXAMPLES::

            sage: a = FrozenBitset('10110')
            sage: bytes(a) == b'10110'
            True
            sage: bytes(FrozenBitset('110' * 32)) == b'110' * 32
            True"""
    def __contains__(self, unsignedlongn) -> bool:
        """FrozenBitset.__contains__(self, unsigned long n) -> bool

        File: /build/sagemath/src/sage/src/sage/data_structures/bitset.pyx (starting at line 780)

        Test to see if ``n`` is in ``self``.

        EXAMPLES::

            sage: 0 in FrozenBitset([0,1])
            True
            sage: 0 in FrozenBitset([1,2])
            False
            sage: 10 in FrozenBitset([0,1])
            False
            sage: 121 in FrozenBitset('110' * 50)
            True
            sage: 122 in FrozenBitset('110' * 50)
            False

        TESTS::

            sage: None in FrozenBitset([0,1])
            Traceback (most recent call last):
            ...
            TypeError: an integer is required"""
    def __copy__(self) -> Any:
        """FrozenBitset.__copy__(self)

        File: /build/sagemath/src/sage/src/sage/data_structures/bitset.pyx (starting at line 1222)

        Return ``self`` (since ``self`` is immutable).

        EXAMPLES::

            sage: a = FrozenBitset('10101')
            sage: from copy import copy
            sage: b = copy(a)
            sage: b is a
            True
            sage: c = FrozenBitset('1010' * 32)
            sage: d = copy(c)
            sage: d is c
            True"""
    def __eq__(self, other: object) -> bool:
        """Return self==value."""
    def __ge__(self, other: object) -> bool:
        """Return self>=value."""
    def __gt__(self, other: object) -> bool:
        """Return self>value."""
    def __hash__(self) -> Any:
        """FrozenBitset.__hash__(self)

        File: /build/sagemath/src/sage/src/sage/data_structures/bitset.pyx (starting at line 537)

        Return a hash value for a bitset.

        EXAMPLES::

            sage: hash(FrozenBitset(capacity=5))
            0
            sage: hash(FrozenBitset('10110'))
            13
            sage: hash(FrozenBitset('10110' + '0' * 120, capacity=125))
            13"""
    def __invert__(self) -> Any:
        """FrozenBitset.__invert__(self)

        File: /build/sagemath/src/sage/src/sage/data_structures/bitset.pyx (starting at line 1200)

        Return the complement of ``self``.

        EXAMPLES::

            sage: ~FrozenBitset('10101')
            01010
            sage: ~FrozenBitset('11111'*10)
            00000000000000000000000000000000000000000000000000
            sage: x = FrozenBitset('10'*40)
            sage: x == ~x
            False
            sage: x == ~~x
            True
            sage: x|(~x) == FrozenBitset('11'*40)
            True
            sage: ~x == FrozenBitset('01'*40)
            True"""
    def __iter__(self) -> Any:
        """FrozenBitset.__iter__(self)

        File: /build/sagemath/src/sage/src/sage/data_structures/bitset.pyx (starting at line 444)

        Return an iterator over ``self``.

        EXAMPLES::

            sage: list(FrozenBitset('11011'))
            [0, 1, 3, 4]
            sage: list(FrozenBitset('00001' * 20))
            [4, 9, 14, 19, 24, 29, 34, 39, 44, 49, 54, 59, 64, 69, 74, 79, 84, 89, 94, 99]
            sage: set(FrozenBitset('11011'))
            {0, 1, 3, 4}"""
    def __le__(self, other: object) -> bool:
        """Return self<=value."""
    def __len__(self) -> Any:
        """FrozenBitset.__len__(self)

        File: /build/sagemath/src/sage/src/sage/data_structures/bitset.pyx (starting at line 809)

        Return the number of elements in the bitset (which may be
        different from the capacity of the bitset).

        EXAMPLES::

            sage: len(FrozenBitset([0,1], capacity=10))
            2
            sage: len(FrozenBitset(range(98)))
            98"""
    def __lt__(self, other: object) -> bool:
        """Return self<value."""
    def __ne__(self, other: object) -> bool:
        """Return self!=value."""
    def __or__(self, FrozenBitsetother) -> Any:
        """FrozenBitset.__or__(self, FrozenBitset other)

        File: /build/sagemath/src/sage/src/sage/data_structures/bitset.pyx (starting at line 934)

         Return the union of ``self`` and ``other``.

         EXAMPLES::

             sage: FrozenBitset('10101') | FrozenBitset('11100')
             11101
             sage: FrozenBitset('10101' * 10) | FrozenBitset('01010' * 10)
             11111111111111111111111111111111111111111111111111

        TESTS::

             sage: set(FrozenBitset('10101' * 10) | FrozenBitset('01010' * 10)) == set(FrozenBitset('10101' * 10)) | set(FrozenBitset('01010' * 10))
             True
             sage: set(FrozenBitset('10101') | FrozenBitset('01010' * 20)) == set(FrozenBitset('10101')) | set(FrozenBitset('01010' * 20))
             True
             sage: set(FrozenBitset('10101' * 20) | FrozenBitset('01010')) == set(FrozenBitset('10101' * 20)) | set(FrozenBitset('01010'))
             True
             sage: FrozenBitset('10101') | None
             Traceback (most recent call last):
             ...
             TypeError: Argument 'other' has incorrect type (expected sage.data_structures.bitset.FrozenBitset, got NoneType)
             sage: None | FrozenBitset('10101')
             Traceback (most recent call last):
             ...
             AttributeError: 'NoneType' object has no attribute '_union'...
 """
    def __rand__(self, other):
        """Return value&self."""
    def __reversed__(self) -> Any:
        """FrozenBitset.__reversed__(self)

        File: /build/sagemath/src/sage/src/sage/data_structures/bitset.pyx (starting at line 459)

        Return an iterator over ``self``, starting with the largest element.

        EXAMPLES::

            sage: list(reversed(FrozenBitset('11011')))
            [4, 3, 1, 0]
            sage: list(reversed(FrozenBitset('00001' * 20)))
            [99, 94, 89, 84, 79, 74, 69, 64, 59, 54, 49, 44, 39, 34, 29, 24, 19, 14, 9, 4]"""
    def __ror__(self, other):
        """Return value|self."""
    def __rsub__(self, other):
        """Return value-self."""
    def __rxor__(self, other):
        """Return value^self."""
    def __sub__(self, FrozenBitsetother) -> Any:
        """FrozenBitset.__sub__(self, FrozenBitset other)

        File: /build/sagemath/src/sage/src/sage/data_structures/bitset.pyx (starting at line 1073)

        Return the difference of ``self`` and ``other``.

        EXAMPLES::

            sage: FrozenBitset('10101') - FrozenBitset('11100')
            00001
            sage: FrozenBitset('11111' * 10)-FrozenBitset('010101' * 10)
            101010101010101010101010101010101010101010101010100000000000

        TESTS::

            sage: set(FrozenBitset('11111' * 10)-FrozenBitset('010101' * 10)) == set(FrozenBitset('11111' * 10))-set(FrozenBitset('010101' * 10))
            True
            sage: set(FrozenBitset('1' * 5)-FrozenBitset('01010' * 20)) == set(FrozenBitset('1' * 5))-set(FrozenBitset('01010' * 20))
            True
            sage: set(FrozenBitset('10101' * 20)-FrozenBitset('1' * 5)) == set(FrozenBitset('10101' * 20))-set(FrozenBitset('1' * 5))
            True
            sage: FrozenBitset('10101') - None
            Traceback (most recent call last):
            ...
            TypeError: Argument 'other' has incorrect type (expected sage.data_structures.bitset.FrozenBitset, got NoneType)
            sage: None - FrozenBitset('10101')
            Traceback (most recent call last):
            ...
            AttributeError: 'NoneType' object has no attribute 'difference'..."""
    def __xor__(self, FrozenBitsetother) -> Any:
        """FrozenBitset.__xor__(self, FrozenBitset other)

        File: /build/sagemath/src/sage/src/sage/data_structures/bitset.pyx (starting at line 1143)

        Return the symmetric difference of ``self`` and ``other``.

        Note that because of the Sage preprocessor, in Sage, ``^^`` is the
        exclusive or, rather than ``^``.

        EXAMPLES::

            sage: FrozenBitset('10101') ^^ FrozenBitset('11100')
            01001
            sage: FrozenBitset('11111' * 10) ^^ FrozenBitset('010101' * 10)
            101010101010101010101010101010101010101010101010100101010101

        TESTS::

            sage: set(FrozenBitset('11111' * 10) ^^ FrozenBitset('010101' * 10)) == set(FrozenBitset('11111' * 10)) ^^ set(FrozenBitset('010101' * 10))
            True
            sage: set(FrozenBitset('1' * 5) ^^ FrozenBitset('01010' * 20)) == set(FrozenBitset('1' * 5)) ^^ set(FrozenBitset('01010' * 20))
            True
            sage: set(FrozenBitset('10101' * 20) ^^ FrozenBitset('1' * 5)) == set(FrozenBitset('10101' * 20)) ^^ set(FrozenBitset('1' * 5))
            True
            sage: FrozenBitset('11111' * 10) ^^ None
            Traceback (most recent call last):
            ...
            TypeError: Argument 'other' has incorrect type (expected sage.data_structures.bitset.FrozenBitset, got NoneType)
            sage: None ^^ FrozenBitset('11111' * 10)
            Traceback (most recent call last):
            ...
            AttributeError: 'NoneType' object has no attribute 'symmetric_difference'..."""
