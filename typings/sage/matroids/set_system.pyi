from sage.cpython.string import bytes_to_str as bytes_to_str, str_to_bytes as str_to_bytes
from typing import Any, ClassVar, overload

class SetSystem:
    """SetSystem(groundset, subsets=None, capacity=1)

    File: /build/sagemath/src/sage/src/sage/matroids/set_system.pyx (starting at line 32)

    A ``SetSystem`` is an enumerator of a collection of subsets of a given
    fixed and finite groundset. It offers the possibility to enumerate its
    contents. One is most likely to encounter these as output from some
    Matroid methods::

        sage: M = matroids.catalog.Fano()
        sage: M.circuits()
        SetSystem of 14 sets over 7 elements

    To access the sets in this structure, simply iterate over them. The
    simplest way must be::

        sage: from sage.matroids.set_system import SetSystem
        sage: S = SetSystem([1, 2, 3, 4], [[1, 2], [3, 4], [1, 2, 4]])
        sage: T = list(S)

    Or immediately use it to iterate::

        sage: from sage.matroids.set_system import SetSystem
        sage: S = SetSystem([1, 2, 3, 4], [[1, 2], [3, 4], [1, 2, 4]])
        sage: [min(X) for X in S]
        [1, 3, 1]

    Note that this class is intended for runtime, so no loads/dumps mechanism
    was implemented.

    .. WARNING::

        The only guaranteed behavior of this class is that it is iterable. It
        is expected that M.circuits(), M.bases(), and so on will in the near
        future return actual iterators. All other methods (which are already
        hidden by default) are only for internal use by the Sage matroid code."""
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    def __init__(self, groundset, subsets=..., capacity=...) -> Any:
        """File: /build/sagemath/src/sage/src/sage/matroids/set_system.pyx (starting at line 94)

                Create a SetSystem.

                INPUT:

                - ``groundset`` -- list or tuple of finitely many elements
                - ``subsets`` -- (default: ``None``) enumerator for a set of subsets of
                  ``groundset``
                - ``capacity`` -- (default: ``1``) initial maximal capacity of the set
                  system

                EXAMPLES::

                    sage: from sage.matroids.set_system import SetSystem
                    sage: S = SetSystem([1, 2, 3, 4], [[1, 2], [3, 4], [1, 2, 4]])
                    sage: S
                    SetSystem of 3 sets over 4 elements
                    sage: sorted(S[1])
                    [3, 4]
                    sage: for s in S: print(sorted(s))
                    [1, 2]
                    [3, 4]
                    [1, 2, 4]
        """
    @overload
    def is_connected(self) -> Any:
        """SetSystem.is_connected(self)

        File: /build/sagemath/src/sage/src/sage/matroids/set_system.pyx (starting at line 320)

        Test if the :class:`SetSystem` is connected.

        A :class:`SetSystem` is connected if there is no nonempty proper subset
        ``X`` of the groundset so the each subset is either contained in ``X``
        or disjoint from ``X``.

        EXAMPLES::

            sage: from sage.matroids.set_system import SetSystem
            sage: S = SetSystem([1, 2, 3, 4], [[1, 2], [3, 4], [1, 2, 4]])
            sage: S.is_connected()
            True
            sage: S = SetSystem([1, 2, 3, 4], [[1, 2], [3, 4]])
            sage: S.is_connected()
            False
            sage: S = SetSystem([1], [])
            sage: S.is_connected()
            True"""
    @overload
    def is_connected(self) -> Any:
        """SetSystem.is_connected(self)

        File: /build/sagemath/src/sage/src/sage/matroids/set_system.pyx (starting at line 320)

        Test if the :class:`SetSystem` is connected.

        A :class:`SetSystem` is connected if there is no nonempty proper subset
        ``X`` of the groundset so the each subset is either contained in ``X``
        or disjoint from ``X``.

        EXAMPLES::

            sage: from sage.matroids.set_system import SetSystem
            sage: S = SetSystem([1, 2, 3, 4], [[1, 2], [3, 4], [1, 2, 4]])
            sage: S.is_connected()
            True
            sage: S = SetSystem([1, 2, 3, 4], [[1, 2], [3, 4]])
            sage: S.is_connected()
            False
            sage: S = SetSystem([1], [])
            sage: S.is_connected()
            True"""
    @overload
    def is_connected(self) -> Any:
        """SetSystem.is_connected(self)

        File: /build/sagemath/src/sage/src/sage/matroids/set_system.pyx (starting at line 320)

        Test if the :class:`SetSystem` is connected.

        A :class:`SetSystem` is connected if there is no nonempty proper subset
        ``X`` of the groundset so the each subset is either contained in ``X``
        or disjoint from ``X``.

        EXAMPLES::

            sage: from sage.matroids.set_system import SetSystem
            sage: S = SetSystem([1, 2, 3, 4], [[1, 2], [3, 4], [1, 2, 4]])
            sage: S.is_connected()
            True
            sage: S = SetSystem([1, 2, 3, 4], [[1, 2], [3, 4]])
            sage: S.is_connected()
            False
            sage: S = SetSystem([1], [])
            sage: S.is_connected()
            True"""
    @overload
    def is_connected(self) -> Any:
        """SetSystem.is_connected(self)

        File: /build/sagemath/src/sage/src/sage/matroids/set_system.pyx (starting at line 320)

        Test if the :class:`SetSystem` is connected.

        A :class:`SetSystem` is connected if there is no nonempty proper subset
        ``X`` of the groundset so the each subset is either contained in ``X``
        or disjoint from ``X``.

        EXAMPLES::

            sage: from sage.matroids.set_system import SetSystem
            sage: S = SetSystem([1, 2, 3, 4], [[1, 2], [3, 4], [1, 2, 4]])
            sage: S.is_connected()
            True
            sage: S = SetSystem([1, 2, 3, 4], [[1, 2], [3, 4]])
            sage: S.is_connected()
            False
            sage: S = SetSystem([1], [])
            sage: S.is_connected()
            True"""
    def __getitem__(self, k) -> Any:
        """SetSystem.__getitem__(self, k)

        File: /build/sagemath/src/sage/src/sage/matroids/set_system.pyx (starting at line 160)

        Return the `k`-th subset in this SetSystem.

        INPUT:

        - ``k`` -- integer; the index of the subset in the system

        OUTPUT: the subset at index `k`

        EXAMPLES::

            sage: from sage.matroids.set_system import SetSystem
            sage: S = SetSystem([1, 2, 3, 4], [[1, 2], [3, 4], [1, 2, 4]])
            sage: sorted(S[0])
            [1, 2]
            sage: sorted(S[1])
            [3, 4]
            sage: sorted(S[2])
            [1, 2, 4]"""
    def __iter__(self) -> Any:
        """SetSystem.__iter__(self)

        File: /build/sagemath/src/sage/src/sage/matroids/set_system.pyx (starting at line 145)

        Return an iterator for the subsets in this SetSystem.

        EXAMPLES::

            sage: from sage.matroids.set_system import SetSystem
            sage: S = SetSystem([1, 2, 3, 4], [[1, 2], [3, 4], [1, 2, 4]])
            sage: for s in S: print(sorted(s))
            [1, 2]
            [3, 4]
            [1, 2, 4]"""
    def __len__(self) -> Any:
        """SetSystem.__len__(self)

        File: /build/sagemath/src/sage/src/sage/matroids/set_system.pyx (starting at line 130)

        Return the number of subsets in this SetSystem.

        EXAMPLES::

            sage: from sage.matroids.set_system import SetSystem
            sage: S = SetSystem([1, 2, 3, 4], [[1, 2], [3, 4], [1, 2, 4]])
            sage: S
            SetSystem of 3 sets over 4 elements
            sage: len(S)
            3"""

class SetSystemIterator:
    """SetSystemIterator(H)"""
    def __init__(self, H) -> Any:
        """File: /build/sagemath/src/sage/src/sage/matroids/set_system.pyx (starting at line 758)

                Create an iterator for a SetSystem.

                Called internally when iterating over the contents of a SetSystem.

                EXAMPLES::

                    sage: from sage.matroids.set_system import SetSystem
                    sage: S = SetSystem([1, 2, 3, 4], [[1, 2], [3, 4], [1, 2, 4]])
                    sage: type(S.__iter__())
                    <... 'sage.matroids.set_system.SetSystemIterator'>
        """
    def __iter__(self) -> Any:
        """SetSystemIterator.__iter__(self)

        File: /build/sagemath/src/sage/src/sage/matroids/set_system.pyx (starting at line 775)"""
    @overload
    def __next__(self) -> Any:
        """SetSystemIterator.__next__(self)

        File: /build/sagemath/src/sage/src/sage/matroids/set_system.pyx (starting at line 778)

        Return the next subset of a SetSystem.

        EXAMPLES::

            sage: from sage.matroids.set_system import SetSystem
            sage: S = SetSystem([1, 2, 3, 4], [[1, 2], [3, 4], [1, 2, 4]])
            sage: I = S.__iter__()
            sage: sorted(I.__next__())
            [1, 2]
            sage: sorted(I.__next__())
            [3, 4]
            sage: sorted(I.__next__())
            [1, 2, 4]"""
    @overload
    def __next__(self) -> Any:
        """SetSystemIterator.__next__(self)

        File: /build/sagemath/src/sage/src/sage/matroids/set_system.pyx (starting at line 778)

        Return the next subset of a SetSystem.

        EXAMPLES::

            sage: from sage.matroids.set_system import SetSystem
            sage: S = SetSystem([1, 2, 3, 4], [[1, 2], [3, 4], [1, 2, 4]])
            sage: I = S.__iter__()
            sage: sorted(I.__next__())
            [1, 2]
            sage: sorted(I.__next__())
            [3, 4]
            sage: sorted(I.__next__())
            [1, 2, 4]"""
    @overload
    def __next__(self) -> Any:
        """SetSystemIterator.__next__(self)

        File: /build/sagemath/src/sage/src/sage/matroids/set_system.pyx (starting at line 778)

        Return the next subset of a SetSystem.

        EXAMPLES::

            sage: from sage.matroids.set_system import SetSystem
            sage: S = SetSystem([1, 2, 3, 4], [[1, 2], [3, 4], [1, 2, 4]])
            sage: I = S.__iter__()
            sage: sorted(I.__next__())
            [1, 2]
            sage: sorted(I.__next__())
            [3, 4]
            sage: sorted(I.__next__())
            [1, 2, 4]"""
    @overload
    def __next__(self) -> Any:
        """SetSystemIterator.__next__(self)

        File: /build/sagemath/src/sage/src/sage/matroids/set_system.pyx (starting at line 778)

        Return the next subset of a SetSystem.

        EXAMPLES::

            sage: from sage.matroids.set_system import SetSystem
            sage: S = SetSystem([1, 2, 3, 4], [[1, 2], [3, 4], [1, 2, 4]])
            sage: I = S.__iter__()
            sage: sorted(I.__next__())
            [1, 2]
            sage: sorted(I.__next__())
            [3, 4]
            sage: sorted(I.__next__())
            [1, 2, 4]"""
