import sage.matroids.matroid
from sage.cpython.string import bytes_to_str as bytes_to_str, str_to_bytes as str_to_bytes
from typing import Any, ClassVar, overload

class MatroidSum(sage.matroids.matroid.Matroid):
    """MatroidSum(summands)

    File: /build/sagemath/src/sage/src/sage/matroids/union_matroid.pyx (starting at line 129)

    Matroid Sum.

    The matroid sum of a list of matroids `(E_1,I_1),\\ldots,(E_n,I_n)` is a matroid
    `(E,I)` where `E= \\bigsqcup_{i=1}^n E_i` and `I= \\bigsqcup_{i=1}^n I_i`.

    INPUT:

    - ``matroids`` -- iterator of matroids

    OUTPUT:

    A ``MatroidSum`` instance, it's a matroid sum of all matroids in ``matroids``."""
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    def __init__(self, summands) -> Any:
        """File: /build/sagemath/src/sage/src/sage/matroids/union_matroid.pyx (starting at line 144)

                See the class definition for full documentation.

                EXAMPLES::

                    sage: from sage.matroids.union_matroid import *
                    sage: MatroidSum([matroids.Uniform(2,4),matroids.Uniform(5,8)])
                    Matroid of rank 7 on 12 elements as matroid sum of
                    Matroid of rank 2 on 4 elements with circuit-closures
                    {2: {{0, 1, 2, 3}}}
                    Matroid of rank 5 on 8 elements with circuit-closures
                    {5: {{0, 1, 2, 3, 4, 5, 6, 7}}}
        """
    @overload
    def groundset(self) -> frozenset:
        """MatroidSum.groundset(self) -> frozenset

        File: /build/sagemath/src/sage/src/sage/matroids/union_matroid.pyx (starting at line 184)

        Return the groundset of the matroid.

        The groundset is the set of elements that comprise the matroid.

        OUTPUT: set

        EXAMPLES::

            sage: from sage.matroids.union_matroid import *
            sage: M = MatroidSum([matroids.Uniform(2,4),matroids.Uniform(2,4)])
            sage: sorted(M.groundset())
            [(0, 0), (0, 1), (0, 2), (0, 3), (1, 0), (1, 1), (1, 2), (1, 3)]"""
    @overload
    def groundset(self) -> Any:
        """MatroidSum.groundset(self) -> frozenset

        File: /build/sagemath/src/sage/src/sage/matroids/union_matroid.pyx (starting at line 184)

        Return the groundset of the matroid.

        The groundset is the set of elements that comprise the matroid.

        OUTPUT: set

        EXAMPLES::

            sage: from sage.matroids.union_matroid import *
            sage: M = MatroidSum([matroids.Uniform(2,4),matroids.Uniform(2,4)])
            sage: sorted(M.groundset())
            [(0, 0), (0, 1), (0, 2), (0, 3), (1, 0), (1, 1), (1, 2), (1, 3)]"""

class MatroidUnion(sage.matroids.matroid.Matroid):
    """MatroidUnion(matroids)

    File: /build/sagemath/src/sage/src/sage/matroids/union_matroid.pyx (starting at line 6)

    Matroid Union.

    The matroid union of a set of matroids `\\{(E_1,I_1),\\ldots,(E_n,I_n)\\}` is
    a matroid `(E,I)` where `E= \\bigcup_{i=1}^n E_i` and

        `I= \\{\\bigcup_{i=1}^n J_i | J_i \\in I_i \\}`.

    EXAMPLES::

        sage: M1 = matroids.Uniform(3,3)
        sage: M2 = Matroid(bases = [frozenset({3}), frozenset({4})])
        sage: M = M1.union(M2); M
        Matroid of rank 4 on 5 elements as matroid union of
        Matroid of rank 3 on 3 elements with circuit-closures
        {}
        Matroid of rank 1 on 2 elements with 2 bases
        sage: M.bases()
        SetSystem of 2 sets over 5 elements
        sage: list(M.circuits())
        [frozenset({3, 4})]

    INPUT:

    - ``matroids`` -- iterator

    OUTPUT: a ``MatroidUnion`` instance; a matroid union of all matroids in ``matroids``"""
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    def __init__(self, matroids) -> Any:
        """File: /build/sagemath/src/sage/src/sage/matroids/union_matroid.pyx (starting at line 35)

                See the class definition for full documentation.

                EXAMPLES::

                    sage: from sage.matroids.union_matroid import *
                    sage: MatroidUnion([matroids.Uniform(2, 4), matroids.Uniform(5, 8)])
                    Matroid of rank 7 on 8 elements as matroid union of
                    Matroid of rank 2 on 4 elements with circuit-closures
                    {2: {{0, 1, 2, 3}}}
                    Matroid of rank 5 on 8 elements with circuit-closures
                    {5: {{0, 1, 2, 3, 4, 5, 6, 7}}}
        """
    @overload
    def groundset(self) -> frozenset:
        """MatroidUnion.groundset(self) -> frozenset

        File: /build/sagemath/src/sage/src/sage/matroids/union_matroid.pyx (starting at line 55)

        Return the groundset of the matroid.

        The groundset is the set of elements that comprise the matroid.

        OUTPUT: set

        EXAMPLES::

            sage: from sage.matroids.union_matroid import *
            sage: M = MatroidUnion([matroids.Uniform(2,4),matroids.Uniform(5,8)])
            sage: sorted(M.groundset())
            [0, 1, 2, 3, 4, 5, 6, 7]"""
    @overload
    def groundset(self) -> Any:
        """MatroidUnion.groundset(self) -> frozenset

        File: /build/sagemath/src/sage/src/sage/matroids/union_matroid.pyx (starting at line 55)

        Return the groundset of the matroid.

        The groundset is the set of elements that comprise the matroid.

        OUTPUT: set

        EXAMPLES::

            sage: from sage.matroids.union_matroid import *
            sage: M = MatroidUnion([matroids.Uniform(2,4),matroids.Uniform(5,8)])
            sage: sorted(M.groundset())
            [0, 1, 2, 3, 4, 5, 6, 7]"""

class PartitionMatroid(sage.matroids.matroid.Matroid):
    """PartitionMatroid(partition)

    File: /build/sagemath/src/sage/src/sage/matroids/union_matroid.pyx (starting at line 233)

    Partition Matroid.

    Given a set of disjoint sets `S=\\{S_1,\\ldots,S_n\\}`, the partition matroid
    on `S` is `(E,I)` where `E=\\bigcup_{i=1}^n S_i` and

        `I= \\{X| |X\\cap S_i|\\leq 1,X\\subset E \\}`.

    INPUT:

    - ``partition`` -- iterator of disjoint sets

    OUTPUT:

    A ``PartitionMatroid`` instance, it's partition matroid of the ``partition``."""
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    def __init__(self, partition) -> Any:
        """File: /build/sagemath/src/sage/src/sage/matroids/union_matroid.pyx (starting at line 250)

                See the class definition for full documentation.

                EXAMPLES::

                    sage: from sage.matroids.union_matroid import *
                    sage: PartitionMatroid([[1,2,3],[4,5,6]])
                    Partition Matroid of rank 2 on 6 elements
                    sage: PartitionMatroid([[1,2],[2,3]])
                    Traceback (most recent call last):
                    ...
                    ValueError: not an iterator of disjoint sets
                    sage: PartitionMatroid([])
                    Partition Matroid of rank 0 on 0 elements
        """
    @overload
    def groundset(self) -> frozenset:
        """PartitionMatroid.groundset(self) -> frozenset

        File: /build/sagemath/src/sage/src/sage/matroids/union_matroid.pyx (starting at line 279)

        Return the groundset of the matroid.

        The groundset is the set of elements that comprise the matroid.

        OUTPUT: set

        EXAMPLES::

            sage: from sage.matroids.union_matroid import *
            sage: M = PartitionMatroid([[1,2,3],[4,5,6]])
            sage: sorted(M.groundset())
            [1, 2, 3, 4, 5, 6]"""
    @overload
    def groundset(self) -> Any:
        """PartitionMatroid.groundset(self) -> frozenset

        File: /build/sagemath/src/sage/src/sage/matroids/union_matroid.pyx (starting at line 279)

        Return the groundset of the matroid.

        The groundset is the set of elements that comprise the matroid.

        OUTPUT: set

        EXAMPLES::

            sage: from sage.matroids.union_matroid import *
            sage: M = PartitionMatroid([[1,2,3],[4,5,6]])
            sage: sorted(M.groundset())
            [1, 2, 3, 4, 5, 6]"""
