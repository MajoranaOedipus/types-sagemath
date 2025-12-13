import _cython_3_2_1
from sage.structure.element import have_same_parent as have_same_parent, parent as parent
from typing import Any, overload

strassen_echelon: _cython_3_2_1.cython_function_or_method
strassen_window_multiply: _cython_3_2_1.cython_function_or_method
test: _cython_3_2_1.cython_function_or_method

class int_range:
    """File: /build/sagemath/src/sage/src/sage/matrix/strassen.pyx (starting at line 484)

        Represent a list of integers as a list of integer intervals.

        .. NOTE::

            Repetitions are not considered.

        Useful class for dealing with pivots in the Strassen echelon, could
        have much more general application

        INPUT:

        It can be one of the following:

        - ``indices`` -- integer; start of the unique interval
        - ``range`` -- integer; length of the unique interval

        OR

        - ``indices`` -- list of integers, the integers to wrap into intervals

        OR

        - ``indices`` -- ``None`` (default), shortcut for an empty list

        OUTPUT:

        An instance of ``int_range``, i.e. a list of pairs ``(start, length)``.

        EXAMPLES:

        From a pair of integers::

            sage: from sage.matrix.strassen import int_range
            sage: int_range(2, 4)
            [(2, 4)]

        Default::

            sage: int_range()
            []

        From a list of integers::

            sage: int_range([1,2,3,4])
            [(1, 4)]
            sage: int_range([1,2,3,4,6,7,8])
            [(1, 4), (6, 3)]
            sage: int_range([1,2,3,4,100,101,102])
            [(1, 4), (100, 3)]
            sage: int_range([1,1000,2,101,3,4,100,102])
            [(1, 4), (100, 3), (1000, 1)]

        Repetitions are not considered::

            sage: int_range([1,2,3])
            [(1, 3)]
            sage: int_range([1,1,1,1,2,2,2,3])
            [(1, 3)]

        AUTHORS:

        - Robert Bradshaw
    """
    def __init__(self, indices=..., range=...) -> Any:
        """int_range.__init__(self, indices=None, range=None)

        File: /build/sagemath/src/sage/src/sage/matrix/strassen.pyx (starting at line 549)

        See ``sage.matrix.strassen.int_range`` for full documentation.

        EXAMPLES::

            sage: from sage.matrix.strassen import int_range
            sage: int_range(2, 4)
            [(2, 4)]"""
    @overload
    def intervals(self) -> Any:
        """int_range.intervals(self)

        File: /build/sagemath/src/sage/src/sage/matrix/strassen.pyx (starting at line 594)

        Return the list of intervals.

        OUTPUT: list of pairs of integers

        EXAMPLES::

            sage: from sage.matrix.strassen import int_range
            sage: I = int_range([4,5,6,20,21,22,23])
            sage: I.intervals()
            [(4, 3), (20, 4)]
            sage: type(I.intervals())
            <... 'list'>"""
    @overload
    def intervals(self) -> Any:
        """int_range.intervals(self)

        File: /build/sagemath/src/sage/src/sage/matrix/strassen.pyx (starting at line 594)

        Return the list of intervals.

        OUTPUT: list of pairs of integers

        EXAMPLES::

            sage: from sage.matrix.strassen import int_range
            sage: I = int_range([4,5,6,20,21,22,23])
            sage: I.intervals()
            [(4, 3), (20, 4)]
            sage: type(I.intervals())
            <... 'list'>"""
    @overload
    def intervals(self) -> Any:
        """int_range.intervals(self)

        File: /build/sagemath/src/sage/src/sage/matrix/strassen.pyx (starting at line 594)

        Return the list of intervals.

        OUTPUT: list of pairs of integers

        EXAMPLES::

            sage: from sage.matrix.strassen import int_range
            sage: I = int_range([4,5,6,20,21,22,23])
            sage: I.intervals()
            [(4, 3), (20, 4)]
            sage: type(I.intervals())
            <... 'list'>"""
    @overload
    def to_list(self) -> Any:
        """int_range.to_list(self)

        File: /build/sagemath/src/sage/src/sage/matrix/strassen.pyx (starting at line 611)

        Return the (sorted) list of integers represented by this object.

        OUTPUT: list of integers

        EXAMPLES::

            sage: from sage.matrix.strassen import int_range
            sage: I = int_range([6,20,21,4,5,22,23])
            sage: I.to_list()
            [4, 5, 6, 20, 21, 22, 23]

        ::

            sage: I = int_range(34, 9)
            sage: I.to_list()
            [34, 35, 36, 37, 38, 39, 40, 41, 42]

        Repetitions are not considered::

            sage: I = int_range([1,1,1,1,2,2,2,3])
            sage: I.to_list()
            [1, 2, 3]"""
    @overload
    def to_list(self) -> Any:
        """int_range.to_list(self)

        File: /build/sagemath/src/sage/src/sage/matrix/strassen.pyx (starting at line 611)

        Return the (sorted) list of integers represented by this object.

        OUTPUT: list of integers

        EXAMPLES::

            sage: from sage.matrix.strassen import int_range
            sage: I = int_range([6,20,21,4,5,22,23])
            sage: I.to_list()
            [4, 5, 6, 20, 21, 22, 23]

        ::

            sage: I = int_range(34, 9)
            sage: I.to_list()
            [34, 35, 36, 37, 38, 39, 40, 41, 42]

        Repetitions are not considered::

            sage: I = int_range([1,1,1,1,2,2,2,3])
            sage: I.to_list()
            [1, 2, 3]"""
    @overload
    def to_list(self) -> Any:
        """int_range.to_list(self)

        File: /build/sagemath/src/sage/src/sage/matrix/strassen.pyx (starting at line 611)

        Return the (sorted) list of integers represented by this object.

        OUTPUT: list of integers

        EXAMPLES::

            sage: from sage.matrix.strassen import int_range
            sage: I = int_range([6,20,21,4,5,22,23])
            sage: I.to_list()
            [4, 5, 6, 20, 21, 22, 23]

        ::

            sage: I = int_range(34, 9)
            sage: I.to_list()
            [34, 35, 36, 37, 38, 39, 40, 41, 42]

        Repetitions are not considered::

            sage: I = int_range([1,1,1,1,2,2,2,3])
            sage: I.to_list()
            [1, 2, 3]"""
    @overload
    def to_list(self) -> Any:
        """int_range.to_list(self)

        File: /build/sagemath/src/sage/src/sage/matrix/strassen.pyx (starting at line 611)

        Return the (sorted) list of integers represented by this object.

        OUTPUT: list of integers

        EXAMPLES::

            sage: from sage.matrix.strassen import int_range
            sage: I = int_range([6,20,21,4,5,22,23])
            sage: I.to_list()
            [4, 5, 6, 20, 21, 22, 23]

        ::

            sage: I = int_range(34, 9)
            sage: I.to_list()
            [34, 35, 36, 37, 38, 39, 40, 41, 42]

        Repetitions are not considered::

            sage: I = int_range([1,1,1,1,2,2,2,3])
            sage: I.to_list()
            [1, 2, 3]"""
    def __add__(self, right) -> Any:
        """int_range.__add__(self, right)

        File: /build/sagemath/src/sage/src/sage/matrix/strassen.pyx (starting at line 682)

        Return the union of ``self`` and ``right``.

        INPUT:

        - ``right`` -- an instance of ``int_range``

        OUTPUT: an instance of ``int_range``

        .. NOTE::

            Yes, this two could be a lot faster...
            Basically, this class is for abstracting away what I was trying
            to do by hand in several places

        EXAMPLES::

            sage: from sage.matrix.strassen import int_range
            sage: I = int_range([1,1,1,1,2,2,2,3])
            sage: J = int_range([6,20,21,4,5,22,23])
            sage: I + J
            [(1, 6), (20, 4)]"""
    def __iter__(self) -> Any:
        """int_range.__iter__(self)

        File: /build/sagemath/src/sage/src/sage/matrix/strassen.pyx (starting at line 639)

        Return an iterator over the intervals.

        OUTPUT: iterator

        EXAMPLES::

            sage: from sage.matrix.strassen import int_range
            sage: I = int_range([6,20,21,4,5,22,23])
            sage: it = iter(I)
            sage: next(it)
            (4, 3)
            sage: next(it)
            (20, 4)
            sage: next(it)
            Traceback (most recent call last):
            ...
            StopIteration"""
    def __len__(self) -> Any:
        """int_range.__len__(self)

        File: /build/sagemath/src/sage/src/sage/matrix/strassen.pyx (starting at line 661)

        Return the number of integers represented by this object.

        OUTPUT: Python integer

        EXAMPLES::

            sage: from sage.matrix.strassen import int_range
            sage: I = int_range([6,20,21,4,5,22,23])
            sage: len(I)
            7

        ::

            sage: I = int_range([1,1,1,1,2,2,2,3])
            sage: len(I)
            3"""
    def __mul__(self, right) -> Any:
        """int_range.__mul__(self, right)

        File: /build/sagemath/src/sage/src/sage/matrix/strassen.pyx (starting at line 738)

        Return the intersection of ``self`` and ``right``.

        INPUT:

        - ``right`` -- an instance of ``int_range``

        OUTPUT: an instance of ``int_range``

        EXAMPLES::

            sage: from sage.matrix.strassen import int_range
            sage: I = int_range([1,2,3,4,5])
            sage: J = int_range([6,20,21,4,5,22,23])
            sage: J * I
            [(4, 2)]"""
    def __sub__(self, right) -> Any:
        """int_range.__sub__(self, right)

        File: /build/sagemath/src/sage/src/sage/matrix/strassen.pyx (starting at line 710)

        Return the set difference of ``self`` and ``right``.

        INPUT:

        - ``right`` -- an instance of ``int_range``

        OUTPUT: an instance of ``int_range``

        .. NOTE::

            Yes, this two could be a lot faster...
            Basically, this class is for abstracting away what I was trying
            to do by hand in several places

        EXAMPLES::

            sage: from sage.matrix.strassen import int_range
            sage: I = int_range([1,2,3,4,5])
            sage: J = int_range([6,20,21,4,5,22,23])
            sage: J - I
            [(6, 1), (20, 4)]"""
