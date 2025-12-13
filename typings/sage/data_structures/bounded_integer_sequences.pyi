import _cython_3_2_1
from sage.cpython.string import bytes_to_str as bytes_to_str, str_to_bytes as str_to_bytes
from sage.structure.element import have_same_parent as have_same_parent, parent as parent
from sage.structure.richcmp import revop as revop, rich_to_bool as rich_to_bool, rich_to_bool_sgn as rich_to_bool_sgn, richcmp as richcmp, richcmp_not_equal as richcmp_not_equal
from typing import Any, ClassVar, overload

NewBISEQ: _cython_3_2_1.cython_function_or_method
__pyx_capi__: dict

class BoundedIntegerSequence:
    """BoundedIntegerSequence(bound, data)

    File: /build/sagemath/src/sage/src/sage/data_structures/bounded_integer_sequences.pyx (starting at line 443)

    A sequence of nonnegative uniformly bounded integers.

    INPUT:

    - ``bound`` -- nonnegative integer. When zero, a :exc:`ValueError`
      will be raised. Otherwise, the given bound is replaced by the
      power of two that is at least the given bound.
    - ``data`` -- list of integers

    EXAMPLES:

    We showcase the similarities and differences between bounded integer
    sequences and lists respectively tuples.

    To distinguish from tuples or lists, we use pointed brackets for the
    string representation of bounded integer sequences::

        sage: from sage.data_structures.bounded_integer_sequences import BoundedIntegerSequence
        sage: S = BoundedIntegerSequence(21, [2, 7, 20]); S
        <2, 7, 20>

    Each bounded integer sequence has a bound that is a power of two, such
    that all its item are less than this bound::

        sage: S.bound()
        32
        sage: BoundedIntegerSequence(16, [2, 7, 20])
        Traceback (most recent call last):
        ...
        OverflowError: list item 20 larger than 15

    Bounded integer sequences are iterable, and we see that we can recover the
    originally given list::

        sage: L = [randint(0,31) for i in range(5000)]
        sage: S = BoundedIntegerSequence(32, L)
        sage: list(L) == L
        True

    Getting items and slicing works in the same way as for lists::

        sage: n = randint(0,4999)
        sage: S[n] == L[n]
        True
        sage: m = randint(0,1000)
        sage: n = randint(3000,4500)
        sage: s = randint(1, 7)
        sage: list(S[m:n:s]) == L[m:n:s]
        True
        sage: list(S[n:m:-s]) == L[n:m:-s]
        True

    The :meth:`index` method works different for bounded integer sequences and
    tuples or lists. If one asks for the index of an item, the behaviour is
    the same. But we can also ask for the index of a sub-sequence::

        sage: L.index(L[200]) == S.index(L[200])
        True
        sage: S.index(S[100:2000])    # random
        100

    Similarly, containment tests work for both items and sub-sequences::

        sage: S[200] in S
        True
        sage: S[200:400] in S
        True
        sage: S[200]+S.bound() in S
        False

    Bounded integer sequences are immutable, and thus copies are
    identical. This is the same for tuples, but of course not for lists::

        sage: T = tuple(S)
        sage: copy(T) is T
        True
        sage: copy(S) is S
        True
        sage: copy(L) is L
        False

    Concatenation works in the same way for lists, tuples and bounded
    integer sequences::

        sage: M = [randint(0,31) for i in range(5000)]
        sage: T = BoundedIntegerSequence(32, M)
        sage: list(S+T)==L+M
        True
        sage: list(T+S)==M+L
        True
        sage: (T+S == S+T) == (M+L == L+M)
        True

    However, comparison works different for lists and bounded integer
    sequences. Bounded integer sequences are first compared by bound, then by
    length, and eventually by *reverse* lexicographical ordering::

        sage: S = BoundedIntegerSequence(21, [4,1,6,2,7,20,9])
        sage: T = BoundedIntegerSequence(51, [4,1,6,2,7,20])
        sage: S < T   # compare by bound, not length
        True
        sage: T < S
        False
        sage: S.bound() < T.bound()
        True
        sage: len(S) > len(T)
        True

    ::

        sage: T = BoundedIntegerSequence(21, [0,0,0,0,0,0,0,0])
        sage: S < T    # compare by length, not lexicographically
        True
        sage: T < S
        False
        sage: list(T) < list(S)
        True
        sage: len(T) > len(S)
        True

    ::

        sage: T = BoundedIntegerSequence(21, [4,1,5,2,8,20,9])
        sage: T > S   # compare by reverse lexicographic ordering...
        True
        sage: S > T
        False
        sage: len(S) == len(T)
        True
        sage: list(S) > list(T) # direct lexicographic ordering is different
        True

    TESTS:

    We test against various corner cases::

        sage: BoundedIntegerSequence(16, [2, 7, -20])
        Traceback (most recent call last):
        ...
        OverflowError: can...t convert negative value to size_t
        sage: BoundedIntegerSequence(1, [0, 0, 0])
        <0, 0, 0>
        sage: BoundedIntegerSequence(1, [0, 1, 0])
        Traceback (most recent call last):
        ...
        OverflowError: list item 1 larger than 0
        sage: BoundedIntegerSequence(0, [0, 1, 0])
        Traceback (most recent call last):
        ...
        ValueError: positive bound expected
        sage: BoundedIntegerSequence(2, [])
        <>
        sage: BoundedIntegerSequence(2, []) == BoundedIntegerSequence(4, []) # The bounds differ
        False
        sage: BoundedIntegerSequence(16, [2, 7, 4])[1:1]
        <>"""
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    def __init__(self, bound, data) -> Any:
        """File: /build/sagemath/src/sage/src/sage/data_structures/bounded_integer_sequences.pyx (starting at line 637)

                INPUT:

                - ``bound`` -- positive integer; the given bound is replaced by
                  the next power of two that is greater than the given bound

                - ``data`` -- list of nonnegative integers; all less than
                  ``bound``

                EXAMPLES::

                    sage: from sage.data_structures.bounded_integer_sequences import BoundedIntegerSequence
                    sage: L = [randint(0,26) for i in range(5000)]
                    sage: S = BoundedIntegerSequence(57, L)   # indirect doctest
                    sage: list(S) == L
                    True
                    sage: S = BoundedIntegerSequence(11, [4,1,6,2,7,4,9]); S
                    <4, 1, 6, 2, 7, 4, 9>
                    sage: S.bound()
                    16

                Non-positive bounds or bounds which are too large result in errors::

                    sage: BoundedIntegerSequence(-1, L)
                    Traceback (most recent call last):
                    ...
                    ValueError: positive bound expected
                    sage: BoundedIntegerSequence(0, L)
                    Traceback (most recent call last):
                    ...
                    ValueError: positive bound expected
                    sage: BoundedIntegerSequence(2^64+1, L)
                    Traceback (most recent call last):
                    ...
                    OverflowError: ... int too large to convert...

                We are testing the corner case of the maximal possible bound::

                    sage: S = BoundedIntegerSequence(2*(sys.maxsize+1), [8, 8, 26, 18, 18, 8, 22, 4, 17, 22, 22, 7, 12, 4, 1, 7, 21, 7, 10, 10])
                    sage: S
                    <8, 8, 26, 18, 18, 8, 22, 4, 17, 22, 22, 7, 12, 4, 1, 7, 21, 7, 10, 10>

                Items that are too large::

                    sage: BoundedIntegerSequence(100, [2^256])
                    Traceback (most recent call last):
                    ...
                    OverflowError: ... int too large to convert...
                    sage: BoundedIntegerSequence(100, [100])
                    Traceback (most recent call last):
                    ...
                    OverflowError: list item 100 larger than 99

                Bounds that are too large::

                    sage: BoundedIntegerSequence(2^256, [200])
                    Traceback (most recent call last):
                    ...
                    OverflowError: ... int too large to convert...
        """
    @overload
    def bound(self) -> Any:
        """BoundedIntegerSequence.bound(self)

        File: /build/sagemath/src/sage/src/sage/data_structures/bounded_integer_sequences.pyx (starting at line 791)

        Return the bound of this bounded integer sequence.

        All items of this sequence are nonnegative integers less than the
        returned bound. The bound is a power of two.

        EXAMPLES::

            sage: from sage.data_structures.bounded_integer_sequences import BoundedIntegerSequence
            sage: S = BoundedIntegerSequence(21, [4,1,6,2,7,20,9])
            sage: T = BoundedIntegerSequence(51, [4,1,6,2,7,20,9])
            sage: S.bound()
            32
            sage: T.bound()
            64"""
    @overload
    def bound(self) -> Any:
        """BoundedIntegerSequence.bound(self)

        File: /build/sagemath/src/sage/src/sage/data_structures/bounded_integer_sequences.pyx (starting at line 791)

        Return the bound of this bounded integer sequence.

        All items of this sequence are nonnegative integers less than the
        returned bound. The bound is a power of two.

        EXAMPLES::

            sage: from sage.data_structures.bounded_integer_sequences import BoundedIntegerSequence
            sage: S = BoundedIntegerSequence(21, [4,1,6,2,7,20,9])
            sage: T = BoundedIntegerSequence(51, [4,1,6,2,7,20,9])
            sage: S.bound()
            32
            sage: T.bound()
            64"""
    @overload
    def bound(self) -> Any:
        """BoundedIntegerSequence.bound(self)

        File: /build/sagemath/src/sage/src/sage/data_structures/bounded_integer_sequences.pyx (starting at line 791)

        Return the bound of this bounded integer sequence.

        All items of this sequence are nonnegative integers less than the
        returned bound. The bound is a power of two.

        EXAMPLES::

            sage: from sage.data_structures.bounded_integer_sequences import BoundedIntegerSequence
            sage: S = BoundedIntegerSequence(21, [4,1,6,2,7,20,9])
            sage: T = BoundedIntegerSequence(51, [4,1,6,2,7,20,9])
            sage: S.bound()
            32
            sage: T.bound()
            64"""
    def index(self, other) -> Any:
        '''BoundedIntegerSequence.index(self, other)

        File: /build/sagemath/src/sage/src/sage/data_structures/bounded_integer_sequences.pyx (starting at line 1086)

        The index of a given item or sub-sequence of ``self``.

        EXAMPLES::

            sage: from sage.data_structures.bounded_integer_sequences import BoundedIntegerSequence
            sage: S = BoundedIntegerSequence(21, [4,1,6,2,6,20,9,0])
            sage: S.index(6)
            2
            sage: S.index(5)
            Traceback (most recent call last):
            ...
            ValueError: 5 is not in sequence
            sage: S.index(BoundedIntegerSequence(21, [6, 2, 6]))
            2
            sage: S.index(BoundedIntegerSequence(21, [6, 2, 7]))
            Traceback (most recent call last):
            ...
            ValueError: not a sub-sequence

        The bound of (sub-)sequences matters::

            sage: S.index(BoundedIntegerSequence(51, [6, 2, 6]))
            Traceback (most recent call last):
            ...
            ValueError: not a sub-sequence
            sage: S.index(0)
            7
            sage: S.index(S.bound())
            Traceback (most recent call last):
            ...
            ValueError: 32 is not in sequence

        TESTS::

            sage: S = BoundedIntegerSequence(10^9, [2, 2, 2, 1, 2, 4, 3, 3, 3, 2, 2, 0])
            sage: S[11]
            0
            sage: S.index(0)
            11

        ::

            sage: S.index(-3)
            Traceback (most recent call last):
            ...
            ValueError: -3 is not in sequence
            sage: S.index(2^100)
            Traceback (most recent call last):
            ...
            ValueError: 1267650600228229401496703205376 is not in sequence
            sage: S.index("hello")
            Traceback (most recent call last):
            ...
            TypeError: an integer is required'''
    @overload
    def list(self) -> list:
        """BoundedIntegerSequence.list(self) -> list

        File: /build/sagemath/src/sage/src/sage/data_structures/bounded_integer_sequences.pyx (starting at line 1026)

        Convert this bounded integer sequence to a list.

        NOTE:

        A conversion to a list is also possible by iterating over the
        sequence.

        EXAMPLES::

            sage: from sage.data_structures.bounded_integer_sequences import BoundedIntegerSequence
            sage: L = [randint(0,26) for i in range(5000)]
            sage: S = BoundedIntegerSequence(32, L)
            sage: S.list() == list(S) == L
            True

        The discussion at :issue:`15820` explains why the following is a good test::

            sage: (BoundedIntegerSequence(21, [0,0]) + BoundedIntegerSequence(21, [0,0])).list()
            [0, 0, 0, 0]"""
    @overload
    def list(self, S) -> Any:
        """BoundedIntegerSequence.list(self) -> list

        File: /build/sagemath/src/sage/src/sage/data_structures/bounded_integer_sequences.pyx (starting at line 1026)

        Convert this bounded integer sequence to a list.

        NOTE:

        A conversion to a list is also possible by iterating over the
        sequence.

        EXAMPLES::

            sage: from sage.data_structures.bounded_integer_sequences import BoundedIntegerSequence
            sage: L = [randint(0,26) for i in range(5000)]
            sage: S = BoundedIntegerSequence(32, L)
            sage: S.list() == list(S) == L
            True

        The discussion at :issue:`15820` explains why the following is a good test::

            sage: (BoundedIntegerSequence(21, [0,0]) + BoundedIntegerSequence(21, [0,0])).list()
            [0, 0, 0, 0]"""
    @overload
    def list(self) -> Any:
        """BoundedIntegerSequence.list(self) -> list

        File: /build/sagemath/src/sage/src/sage/data_structures/bounded_integer_sequences.pyx (starting at line 1026)

        Convert this bounded integer sequence to a list.

        NOTE:

        A conversion to a list is also possible by iterating over the
        sequence.

        EXAMPLES::

            sage: from sage.data_structures.bounded_integer_sequences import BoundedIntegerSequence
            sage: L = [randint(0,26) for i in range(5000)]
            sage: S = BoundedIntegerSequence(32, L)
            sage: S.list() == list(S) == L
            True

        The discussion at :issue:`15820` explains why the following is a good test::

            sage: (BoundedIntegerSequence(21, [0,0]) + BoundedIntegerSequence(21, [0,0])).list()
            [0, 0, 0, 0]"""
    def maximal_overlap(self, BoundedIntegerSequenceother) -> BoundedIntegerSequence:
        """BoundedIntegerSequence.maximal_overlap(self, BoundedIntegerSequence other) -> BoundedIntegerSequence

        File: /build/sagemath/src/sage/src/sage/data_structures/bounded_integer_sequences.pyx (starting at line 1217)

        Return ``self``'s maximal trailing sub-sequence that ``other`` starts with.

        Return ``None`` if there is no overlap.

        EXAMPLES::

            sage: from sage.data_structures.bounded_integer_sequences import BoundedIntegerSequence
            sage: X = BoundedIntegerSequence(21, [4,1,6,2,7,2,3])
            sage: S = BoundedIntegerSequence(21, [0,0,0,0,0,0,0])
            sage: T = BoundedIntegerSequence(21, [2,7,2,3,0,0,0,0,0,0,0,1])
            sage: (X+S).maximal_overlap(T)
            <2, 7, 2, 3, 0, 0, 0, 0, 0, 0, 0>
            sage: print((X+S).maximal_overlap(BoundedIntegerSequence(21, [2,7,2,3,0,0,0,0,0,1])))
            None
            sage: (X+S).maximal_overlap(BoundedIntegerSequence(21, [0,0]))
            <0, 0>
            sage: B1 = BoundedIntegerSequence(4,[1,2,3,2,3,2,3])
            sage: B2 = BoundedIntegerSequence(4,[2,3,2,3,2,3,1])
            sage: B1.maximal_overlap(B2)
            <2, 3, 2, 3, 2, 3>"""
    @overload
    def startswith(self, BoundedIntegerSequenceother) -> bool:
        """BoundedIntegerSequence.startswith(self, BoundedIntegerSequence other) -> bool

        File: /build/sagemath/src/sage/src/sage/data_structures/bounded_integer_sequences.pyx (starting at line 1051)

        Tells whether ``self`` starts with a given bounded integer sequence

        EXAMPLES::

            sage: from sage.data_structures.bounded_integer_sequences import BoundedIntegerSequence
            sage: L = [randint(0,26) for i in range(5000)]
            sage: S = BoundedIntegerSequence(27, L)
            sage: L0 = L[:1000]
            sage: T = BoundedIntegerSequence(27, L0)
            sage: S.startswith(T)
            True
            sage: L0[-1] = (L0[-1] + 1) % 27
            sage: T = BoundedIntegerSequence(27, L0)
            sage: S.startswith(T)
            False
            sage: L0[-1] = (L0[-1] - 1) % 27
            sage: L0[0] = (L0[0] + 1) % 27
            sage: T = BoundedIntegerSequence(27, L0)
            sage: S.startswith(T)
            False
            sage: L0[0] = (L0[0] - 1) % 27

        The bounds of the sequences must be compatible, or :meth:`startswith`
        returns ``False``::

            sage: T = BoundedIntegerSequence(51, L0)
            sage: S.startswith(T)
            False"""
    @overload
    def startswith(self, T) -> Any:
        """BoundedIntegerSequence.startswith(self, BoundedIntegerSequence other) -> bool

        File: /build/sagemath/src/sage/src/sage/data_structures/bounded_integer_sequences.pyx (starting at line 1051)

        Tells whether ``self`` starts with a given bounded integer sequence

        EXAMPLES::

            sage: from sage.data_structures.bounded_integer_sequences import BoundedIntegerSequence
            sage: L = [randint(0,26) for i in range(5000)]
            sage: S = BoundedIntegerSequence(27, L)
            sage: L0 = L[:1000]
            sage: T = BoundedIntegerSequence(27, L0)
            sage: S.startswith(T)
            True
            sage: L0[-1] = (L0[-1] + 1) % 27
            sage: T = BoundedIntegerSequence(27, L0)
            sage: S.startswith(T)
            False
            sage: L0[-1] = (L0[-1] - 1) % 27
            sage: L0[0] = (L0[0] + 1) % 27
            sage: T = BoundedIntegerSequence(27, L0)
            sage: S.startswith(T)
            False
            sage: L0[0] = (L0[0] - 1) % 27

        The bounds of the sequences must be compatible, or :meth:`startswith`
        returns ``False``::

            sage: T = BoundedIntegerSequence(51, L0)
            sage: S.startswith(T)
            False"""
    @overload
    def startswith(self, T) -> Any:
        """BoundedIntegerSequence.startswith(self, BoundedIntegerSequence other) -> bool

        File: /build/sagemath/src/sage/src/sage/data_structures/bounded_integer_sequences.pyx (starting at line 1051)

        Tells whether ``self`` starts with a given bounded integer sequence

        EXAMPLES::

            sage: from sage.data_structures.bounded_integer_sequences import BoundedIntegerSequence
            sage: L = [randint(0,26) for i in range(5000)]
            sage: S = BoundedIntegerSequence(27, L)
            sage: L0 = L[:1000]
            sage: T = BoundedIntegerSequence(27, L0)
            sage: S.startswith(T)
            True
            sage: L0[-1] = (L0[-1] + 1) % 27
            sage: T = BoundedIntegerSequence(27, L0)
            sage: S.startswith(T)
            False
            sage: L0[-1] = (L0[-1] - 1) % 27
            sage: L0[0] = (L0[0] + 1) % 27
            sage: T = BoundedIntegerSequence(27, L0)
            sage: S.startswith(T)
            False
            sage: L0[0] = (L0[0] - 1) % 27

        The bounds of the sequences must be compatible, or :meth:`startswith`
        returns ``False``::

            sage: T = BoundedIntegerSequence(51, L0)
            sage: S.startswith(T)
            False"""
    @overload
    def startswith(self, T) -> Any:
        """BoundedIntegerSequence.startswith(self, BoundedIntegerSequence other) -> bool

        File: /build/sagemath/src/sage/src/sage/data_structures/bounded_integer_sequences.pyx (starting at line 1051)

        Tells whether ``self`` starts with a given bounded integer sequence

        EXAMPLES::

            sage: from sage.data_structures.bounded_integer_sequences import BoundedIntegerSequence
            sage: L = [randint(0,26) for i in range(5000)]
            sage: S = BoundedIntegerSequence(27, L)
            sage: L0 = L[:1000]
            sage: T = BoundedIntegerSequence(27, L0)
            sage: S.startswith(T)
            True
            sage: L0[-1] = (L0[-1] + 1) % 27
            sage: T = BoundedIntegerSequence(27, L0)
            sage: S.startswith(T)
            False
            sage: L0[-1] = (L0[-1] - 1) % 27
            sage: L0[0] = (L0[0] + 1) % 27
            sage: T = BoundedIntegerSequence(27, L0)
            sage: S.startswith(T)
            False
            sage: L0[0] = (L0[0] - 1) % 27

        The bounds of the sequences must be compatible, or :meth:`startswith`
        returns ``False``::

            sage: T = BoundedIntegerSequence(51, L0)
            sage: S.startswith(T)
            False"""
    @overload
    def startswith(self, T) -> Any:
        """BoundedIntegerSequence.startswith(self, BoundedIntegerSequence other) -> bool

        File: /build/sagemath/src/sage/src/sage/data_structures/bounded_integer_sequences.pyx (starting at line 1051)

        Tells whether ``self`` starts with a given bounded integer sequence

        EXAMPLES::

            sage: from sage.data_structures.bounded_integer_sequences import BoundedIntegerSequence
            sage: L = [randint(0,26) for i in range(5000)]
            sage: S = BoundedIntegerSequence(27, L)
            sage: L0 = L[:1000]
            sage: T = BoundedIntegerSequence(27, L0)
            sage: S.startswith(T)
            True
            sage: L0[-1] = (L0[-1] + 1) % 27
            sage: T = BoundedIntegerSequence(27, L0)
            sage: S.startswith(T)
            False
            sage: L0[-1] = (L0[-1] - 1) % 27
            sage: L0[0] = (L0[0] + 1) % 27
            sage: T = BoundedIntegerSequence(27, L0)
            sage: S.startswith(T)
            False
            sage: L0[0] = (L0[0] - 1) % 27

        The bounds of the sequences must be compatible, or :meth:`startswith`
        returns ``False``::

            sage: T = BoundedIntegerSequence(51, L0)
            sage: S.startswith(T)
            False"""
    def __add__(self, other) -> Any:
        """BoundedIntegerSequence.__add__(self, other)

        File: /build/sagemath/src/sage/src/sage/data_structures/bounded_integer_sequences.pyx (starting at line 1162)

        Concatenation of bounded integer sequences.

        NOTE:

        There is no coercion happening, as bounded integer sequences are not
        considered to be elements of an object.

        EXAMPLES::

            sage: from sage.data_structures.bounded_integer_sequences import BoundedIntegerSequence
            sage: S = BoundedIntegerSequence(21, [4,1,6,2,7,20,9])
            sage: T = BoundedIntegerSequence(21, [4,1,6,2,8,15])
            sage: S+T
            <4, 1, 6, 2, 7, 20, 9, 4, 1, 6, 2, 8, 15>
            sage: T+S
            <4, 1, 6, 2, 8, 15, 4, 1, 6, 2, 7, 20, 9>
            sage: S in S+T
            True
            sage: T in S+T
            True
            sage: BoundedIntegerSequence(21, [4,1,6,2,7,20,9,4]) in S+T
            True
            sage: T+list(S)
            Traceback (most recent call last):
            ...
            TypeError: Cannot convert list to sage.data_structures.bounded_integer_sequences.BoundedIntegerSequence
            sage: T+None
            Traceback (most recent call last):
            ...
            TypeError: cannot concatenate bounded integer sequence and None

        TESTS:

        The discussion at :issue:`15820` explains why the following are good tests::

            sage: BoundedIntegerSequence(21, [0,0]) + BoundedIntegerSequence(21, [0,0])
            <0, 0, 0, 0>
            sage: B1 = BoundedIntegerSequence(2^30, [10^9+1, 10^9+2])
            sage: B2 = BoundedIntegerSequence(2^30, [10^9+3, 10^9+4])
            sage: B1 + B2
            <1000000001, 1000000002, 1000000003, 1000000004>"""
    def __bool__(self) -> bool:
        """True if self else False"""
    def __contains__(self, other) -> Any:
        """BoundedIntegerSequence.__contains__(self, other)

        File: /build/sagemath/src/sage/src/sage/data_structures/bounded_integer_sequences.pyx (starting at line 952)

        Tells whether this bounded integer sequence contains an item or a sub-sequence.

        EXAMPLES::

            sage: from sage.data_structures.bounded_integer_sequences import BoundedIntegerSequence
            sage: S = BoundedIntegerSequence(21, [4,1,6,2,7,20,9])
            sage: 6 in S
            True
            sage: BoundedIntegerSequence(21, [2, 7, 20]) in S
            True

        The bound of the sequences matters::

            sage: BoundedIntegerSequence(51, [2, 7, 20]) in S
            False

        ::

            sage: 6+S.bound() in S
            False
            sage: S.index(6+S.bound())
            Traceback (most recent call last):
            ...
            ValueError: 38 is not in sequence

        TESTS:

        The discussion at :issue:`15820` explains why the following are good tests::

            sage: X = BoundedIntegerSequence(21, [4,1,6,2,7,2,3])
            sage: S = BoundedIntegerSequence(21, [0,0,0,0,0,0,0])
            sage: loads(dumps(X+S))
            <4, 1, 6, 2, 7, 2, 3, 0, 0, 0, 0, 0, 0, 0>
            sage: loads(dumps(X+S)) == X+S
            True
            sage: T = BoundedIntegerSequence(21, [0,4,0,1,0,6,0,2,0,7,0,2,0,3,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
            sage: T[3::2]==(X+S)[1:]
            True
            sage: T[3::2] in X+S
            True
            sage: T = BoundedIntegerSequence(21, [0,4,0,1,0,6,0,2,0,7,0,2,0,3,0,0,0,16,0,0,0,0,0,0,0,0,0,0])
            sage: T[3::2] in (X+S)
            False

        ::

            sage: S1 = BoundedIntegerSequence(4, [1,3])
            sage: S2 = BoundedIntegerSequence(4, [0])
            sage: S2 in S1
            False

        ::

            sage: B = BoundedIntegerSequence(27, [8, 8, 26, 18, 18, 8, 22, 4, 17, 22, 22, 7, 12, 4, 1, 7, 21, 7, 10, 10])
            sage: B.index(B[8:])
            8

        ::

            sage: -1 in B
            False"""
    def __copy__(self) -> Any:
        """BoundedIntegerSequence.__copy__(self)

        File: /build/sagemath/src/sage/src/sage/data_structures/bounded_integer_sequences.pyx (starting at line 702)

        :class:`BoundedIntegerSequence` is immutable, copying returns ``self``.

        EXAMPLES::

            sage: from sage.data_structures.bounded_integer_sequences import BoundedIntegerSequence
            sage: S = BoundedIntegerSequence(21, [4,1,6,2,7,20,9])
            sage: copy(S) is S
            True"""
    def __eq__(self, other: object) -> bool:
        """Return self==value."""
    def __ge__(self, other: object) -> bool:
        """Return self>=value."""
    def __getitem__(self, index) -> Any:
        """BoundedIntegerSequence.__getitem__(self, index)

        File: /build/sagemath/src/sage/src/sage/data_structures/bounded_integer_sequences.pyx (starting at line 840)

        Get single items or slices.

        EXAMPLES::

            sage: from sage.data_structures.bounded_integer_sequences import BoundedIntegerSequence
            sage: S = BoundedIntegerSequence(21, [4,1,6,2,7,20,9])
            sage: S[2]
            6
            sage: S[1::2]
            <1, 2, 20>
            sage: S[-1::-2]
            <9, 7, 6, 4>

        TESTS::

            sage: S = BoundedIntegerSequence(10^8, list(range(9)))
            sage: S[-1]
            8
            sage: S[8]
            8
            sage: S[9]
            Traceback (most recent call last):
            ...
            IndexError: index out of range
            sage: S[-10]
            Traceback (most recent call last):
            ...
            IndexError: index out of range
            sage: S[2^63]
            Traceback (most recent call last):
            ...
            OverflowError: ... int too large to convert to ...

        ::

            sage: S[-1::-2]
            <8, 6, 4, 2, 0>
            sage: S[1::2]
            <1, 3, 5, 7>

        ::

            sage: L = [randint(0,26) for i in range(5000)]
            sage: S = BoundedIntegerSequence(27, L)
            sage: S[1234] == L[1234]
            True
            sage: list(S[100:2000:3]) == L[100:2000:3]
            True
            sage: list(S[3000:10:-7]) == L[3000:10:-7]
            True
            sage: S[:] == S
            True
            sage: S[:] is S
            True

        ::

            sage: S = BoundedIntegerSequence(21, [0,0,0,0,0,0,0])
            sage: X = BoundedIntegerSequence(21, [4,1,6,2,7,2,3])
            sage: (X+S)[6]
            3
            sage: (X+S)[10]
            0
            sage: (X+S)[12:]
            <0, 0>

        ::

            sage: S[2:2] == X[4:2]
            True

        ::

            sage: S = BoundedIntegerSequence(6, [3, 5, 3, 1, 5, 2, 2, 5, 3, 3, 4])
            sage: S[10]
            4

        ::

            sage: B = BoundedIntegerSequence(27, [8, 8, 26, 18, 18, 8, 22, 4, 17, 22, 22, 7, 12, 4, 1, 7, 21, 7, 10, 10])
            sage: B[8:]
            <17, 22, 22, 7, 12, 4, 1, 7, 21, 7, 10, 10>

        ::

            sage: B1 = BoundedIntegerSequence(8, [0,7])
            sage: B2 = BoundedIntegerSequence(8, [2,1,4])
            sage: B1[0:1]+B2
            <0, 2, 1, 4>"""
    def __gt__(self, other: object) -> bool:
        """Return self>value."""
    def __hash__(self) -> Any:
        """BoundedIntegerSequence.__hash__(self)

        File: /build/sagemath/src/sage/src/sage/data_structures/bounded_integer_sequences.pyx (starting at line 1305)

        The hash takes into account the content and the bound of the sequence.

        EXAMPLES::

            sage: from sage.data_structures.bounded_integer_sequences import BoundedIntegerSequence
            sage: S = BoundedIntegerSequence(21, [4,1,6,2,7,20,9])
            sage: T = BoundedIntegerSequence(51, [4,1,6,2,7,20,9])
            sage: S == T
            False
            sage: list(S) == list(T)
            True
            sage: S.bound() == T.bound()
            False
            sage: hash(S) == hash(T)
            False
            sage: T = BoundedIntegerSequence(31, [4,1,6,2,7,20,9])
            sage: T.bound() == S.bound()
            True
            sage: hash(S) == hash(T)
            True"""
    def __iter__(self) -> Any:
        """BoundedIntegerSequence.__iter__(self)

        File: /build/sagemath/src/sage/src/sage/data_structures/bounded_integer_sequences.pyx (starting at line 810)

        EXAMPLES::

            sage: from sage.data_structures.bounded_integer_sequences import BoundedIntegerSequence
            sage: L = [randint(0,26) for i in range(5000)]
            sage: S = BoundedIntegerSequence(27, L)
            sage: list(S) == L   # indirect doctest
            True

        TESTS::

            sage: list(BoundedIntegerSequence(1, []))
            []

        The discussion at :issue:`15820` explains why this is a good test::

            sage: S = BoundedIntegerSequence(21, [0,0,0,0,0,0,0])
            sage: X = BoundedIntegerSequence(21, [4,1,6,2,7,2,3])
            sage: list(X)
            [4, 1, 6, 2, 7, 2, 3]
            sage: list(X+S)
            [4, 1, 6, 2, 7, 2, 3, 0, 0, 0, 0, 0, 0, 0]
            sage: list(BoundedIntegerSequence(21, [0,0]) + BoundedIntegerSequence(21, [0,0]))
            [0, 0, 0, 0]"""
    def __le__(self, other: object) -> bool:
        """Return self<=value."""
    def __len__(self) -> Any:
        """BoundedIntegerSequence.__len__(self)

        File: /build/sagemath/src/sage/src/sage/data_structures/bounded_integer_sequences.pyx (starting at line 747)

        EXAMPLES::

            sage: from sage.data_structures.bounded_integer_sequences import BoundedIntegerSequence
            sage: L = [randint(0,26) for i in range(5000)]
            sage: S = BoundedIntegerSequence(57, L)   # indirect doctest
            sage: len(S) == len(L)
            True"""
    def __lt__(self, other: object) -> bool:
        """Return self<value."""
    def __ne__(self, other: object) -> bool:
        """Return self!=value."""
    def __radd__(self, other):
        """Return value+self."""
    def __reduce__(self) -> Any:
        """BoundedIntegerSequence.__reduce__(self)

        File: /build/sagemath/src/sage/src/sage/data_structures/bounded_integer_sequences.pyx (starting at line 715)

        Pickling of :class:`BoundedIntegerSequence`.

        EXAMPLES::

            sage: from sage.data_structures.bounded_integer_sequences import BoundedIntegerSequence
            sage: L = [randint(0,26) for i in range(5000)]
            sage: S = BoundedIntegerSequence(32, L)
            sage: loads(dumps(S)) == S    # indirect doctest
            True

        TESTS:

        The discussion at :issue:`15820` explains why the following is a good test::

            sage: X = BoundedIntegerSequence(21, [4,1,6,2,7,2,3])
            sage: S = BoundedIntegerSequence(21, [0,0,0,0,0,0,0])
            sage: loads(dumps(X+S))
            <4, 1, 6, 2, 7, 2, 3, 0, 0, 0, 0, 0, 0, 0>
            sage: loads(dumps(X+S)) == X+S
            True
            sage: T = BoundedIntegerSequence(21, [0,4,0,1,0,6,0,2,0,7,0,2,0,3,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
            sage: T[1::2]
            <4, 1, 6, 2, 7, 2, 3, 0, 0, 0, 0, 0, 0, 0>
            sage: T[1::2] == X+S
            True
            sage: loads(dumps(X[1::2])) == X[1::2]
            True"""
