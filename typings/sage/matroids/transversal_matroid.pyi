import sage.matroids.basis_exchange_matroid
from sage.cpython.string import bytes_to_str as bytes_to_str, str_to_bytes as str_to_bytes
from sage.graphs.bipartite_graph import BipartiteGraph as BipartiteGraph
from sage.graphs.digraph import DiGraph as DiGraph
from sage.matroids.minor_matroid import MinorMatroid as MinorMatroid
from sage.matroids.utilities import newlabel as newlabel
from typing import Any, ClassVar, overload

class TransversalMatroid(sage.matroids.basis_exchange_matroid.BasisExchangeMatroid):
    """TransversalMatroid(sets, groundset=None, set_labels=None, matching=None)

    File: /build/sagemath/src/sage/src/sage/matroids/transversal_matroid.pyx (starting at line 58)

    The Transversal Matroid class.

    INPUT:

    - ``sets`` -- iterable of iterables of elements
    - ``groundset`` -- (optional) iterable containing names of groundset
      elements
    - ``set_labels`` -- (optional) list of labels in 1-1 correspondence with
      the iterables in ``sets``
    - ``matching`` -- (optional) dictionary specifying a maximal matching
      between elements and set labels

    OUTPUT:

    An instance of ``TransversalMatroid``. The sets specified in ``sets``
    define the matroid. If ``matching`` is not specified, the constructor
    will determine a matching to use for basis exchange.

    EXAMPLES::

        sage: from sage.matroids.transversal_matroid import TransversalMatroid
        sage: sets = [[0, 1, 2, 3]] * 3
        sage: M = TransversalMatroid(sets)
        sage: M.full_rank()
        3
        sage: M.bases_count()
        4
        sage: sum(1 for b in M.bases())
        4

    ::

        sage: from sage.matroids.transversal_matroid import TransversalMatroid
        sage: M = TransversalMatroid(sets=[['a', 'c']], groundset=['a', 'c', 'd'])
        sage: M.loops()
        frozenset({'d'})
        sage: M.full_rank()
        1"""
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    @overload
    def __init__(self, sets, groundset=..., set_labels=..., matching=...) -> Any:
        """File: /build/sagemath/src/sage/src/sage/matroids/transversal_matroid.pyx (starting at line 100)

                See the class definition for full documentation.

                EXAMPLES::

                    sage: from sage.matroids.transversal_matroid import TransversalMatroid
                    sage: sets = [[0, 1, 2, 3], [1, 2], [1, 3, 4]]
                    sage: set_labels = [5, 6, 7]
                    sage: M = TransversalMatroid(sets, set_labels=set_labels)
                    sage: TestSuite(M).run()

                TESTS::

                    sage: from sage.matroids.transversal_matroid import TransversalMatroid
                    sage: M = TransversalMatroid([[0, 1], [1, 2], [2, 3], [3, 4]])
                    sage: TestSuite(M).run()

                    sage: M = TransversalMatroid([[], [], []], groundset=range(3)); M
                    Transversal matroid of rank 0 on 3 elements, with 3 sets
                    sage: sets = [[0, 1, 2, 3, 4], [4, 5]]
                    sage: M = TransversalMatroid(sets, groundset=[0, 1, 2, 3])
                    Traceback (most recent call last):
                    ...
                    ValueError: groundset and sets do not match
                    sage: M = TransversalMatroid(sets, set_labels=[1, 2, 3])
                    Traceback (most recent call last):
                    ...
                    ValueError: set labels do not match sets
                    sage: M = TransversalMatroid(sets, set_labels=[1, 2])
                    Traceback (most recent call last):
                    ...
                    ValueError: set labels cannot be element labels

                    sage: sets = [['s1', 's2'], ['s1', 's3']]
                    sage: M = TransversalMatroid(sets); M
                    Transversal matroid of rank 2 on 3 elements, with 2 sets
                    sage: M.sets()
                    [['s1', 's2'], ['s1', 's3']]
                    sage: M.set_labels()
                    ['s0', 's4']

                Testing the matching parameter::

                    sage: M = TransversalMatroid([range(5)] * 4, set_labels='abcd')
                    sage: M.full_rank()
                    4
                    sage: M.rank([0, 1, 2])
                    3

                ::

                    sage: sets = [[0, 1, 2, 3], [1, 2], [1, 3, 4]]
                    sage: set_labels = [5, 6, 7]
                    sage: m = {0: 5, 1: 6, 3: 7}
                    sage: M = TransversalMatroid(sets, set_labels=set_labels, matching=m)
                    sage: len(M.bases())
                    9
        """
    @overload
    def __init__(self, sets) -> Any:
        """File: /build/sagemath/src/sage/src/sage/matroids/transversal_matroid.pyx (starting at line 100)

                See the class definition for full documentation.

                EXAMPLES::

                    sage: from sage.matroids.transversal_matroid import TransversalMatroid
                    sage: sets = [[0, 1, 2, 3], [1, 2], [1, 3, 4]]
                    sage: set_labels = [5, 6, 7]
                    sage: M = TransversalMatroid(sets, set_labels=set_labels)
                    sage: TestSuite(M).run()

                TESTS::

                    sage: from sage.matroids.transversal_matroid import TransversalMatroid
                    sage: M = TransversalMatroid([[0, 1], [1, 2], [2, 3], [3, 4]])
                    sage: TestSuite(M).run()

                    sage: M = TransversalMatroid([[], [], []], groundset=range(3)); M
                    Transversal matroid of rank 0 on 3 elements, with 3 sets
                    sage: sets = [[0, 1, 2, 3, 4], [4, 5]]
                    sage: M = TransversalMatroid(sets, groundset=[0, 1, 2, 3])
                    Traceback (most recent call last):
                    ...
                    ValueError: groundset and sets do not match
                    sage: M = TransversalMatroid(sets, set_labels=[1, 2, 3])
                    Traceback (most recent call last):
                    ...
                    ValueError: set labels do not match sets
                    sage: M = TransversalMatroid(sets, set_labels=[1, 2])
                    Traceback (most recent call last):
                    ...
                    ValueError: set labels cannot be element labels

                    sage: sets = [['s1', 's2'], ['s1', 's3']]
                    sage: M = TransversalMatroid(sets); M
                    Transversal matroid of rank 2 on 3 elements, with 2 sets
                    sage: M.sets()
                    [['s1', 's2'], ['s1', 's3']]
                    sage: M.set_labels()
                    ['s0', 's4']

                Testing the matching parameter::

                    sage: M = TransversalMatroid([range(5)] * 4, set_labels='abcd')
                    sage: M.full_rank()
                    4
                    sage: M.rank([0, 1, 2])
                    3

                ::

                    sage: sets = [[0, 1, 2, 3], [1, 2], [1, 3, 4]]
                    sage: set_labels = [5, 6, 7]
                    sage: m = {0: 5, 1: 6, 3: 7}
                    sage: M = TransversalMatroid(sets, set_labels=set_labels, matching=m)
                    sage: len(M.bases())
                    9
        """
    @overload
    def __init__(self, sets=..., groundset=...) -> Any:
        """File: /build/sagemath/src/sage/src/sage/matroids/transversal_matroid.pyx (starting at line 100)

                See the class definition for full documentation.

                EXAMPLES::

                    sage: from sage.matroids.transversal_matroid import TransversalMatroid
                    sage: sets = [[0, 1, 2, 3], [1, 2], [1, 3, 4]]
                    sage: set_labels = [5, 6, 7]
                    sage: M = TransversalMatroid(sets, set_labels=set_labels)
                    sage: TestSuite(M).run()

                TESTS::

                    sage: from sage.matroids.transversal_matroid import TransversalMatroid
                    sage: M = TransversalMatroid([[0, 1], [1, 2], [2, 3], [3, 4]])
                    sage: TestSuite(M).run()

                    sage: M = TransversalMatroid([[], [], []], groundset=range(3)); M
                    Transversal matroid of rank 0 on 3 elements, with 3 sets
                    sage: sets = [[0, 1, 2, 3, 4], [4, 5]]
                    sage: M = TransversalMatroid(sets, groundset=[0, 1, 2, 3])
                    Traceback (most recent call last):
                    ...
                    ValueError: groundset and sets do not match
                    sage: M = TransversalMatroid(sets, set_labels=[1, 2, 3])
                    Traceback (most recent call last):
                    ...
                    ValueError: set labels do not match sets
                    sage: M = TransversalMatroid(sets, set_labels=[1, 2])
                    Traceback (most recent call last):
                    ...
                    ValueError: set labels cannot be element labels

                    sage: sets = [['s1', 's2'], ['s1', 's3']]
                    sage: M = TransversalMatroid(sets); M
                    Transversal matroid of rank 2 on 3 elements, with 2 sets
                    sage: M.sets()
                    [['s1', 's2'], ['s1', 's3']]
                    sage: M.set_labels()
                    ['s0', 's4']

                Testing the matching parameter::

                    sage: M = TransversalMatroid([range(5)] * 4, set_labels='abcd')
                    sage: M.full_rank()
                    4
                    sage: M.rank([0, 1, 2])
                    3

                ::

                    sage: sets = [[0, 1, 2, 3], [1, 2], [1, 3, 4]]
                    sage: set_labels = [5, 6, 7]
                    sage: m = {0: 5, 1: 6, 3: 7}
                    sage: M = TransversalMatroid(sets, set_labels=set_labels, matching=m)
                    sage: len(M.bases())
                    9
        """
    @overload
    def graph(self) -> Any:
        """TransversalMatroid.graph(self)

        File: /build/sagemath/src/sage/src/sage/matroids/transversal_matroid.pyx (starting at line 446)

        Return a bipartite graph representing the transversal matroid.

        A transversal matroid can be represented as a set system, or as a
        bipartite graph with one color class corresponding to the groundset
        and the other to the sets of the set system. This method returns
        that bipartite graph.

        OUTPUT: :class:`Graph`

        EXAMPLES::

            sage: from sage.matroids.transversal_matroid import TransversalMatroid
            sage: edgedict = {5: [0, 1, 2, 3], 6: [1, 2], 7: [1, 3, 4]}
            sage: B = BipartiteGraph(edgedict)
            sage: M = TransversalMatroid(edgedict.values(), set_labels=edgedict.keys())
            sage: M.graph() == B
            True
            sage: M2 = TransversalMatroid(edgedict.values())
            sage: B2 = M2.graph()
            sage: B2 == B
            False
            sage: B2.is_isomorphic(B)
            True"""
    @overload
    def graph(self) -> Any:
        """TransversalMatroid.graph(self)

        File: /build/sagemath/src/sage/src/sage/matroids/transversal_matroid.pyx (starting at line 446)

        Return a bipartite graph representing the transversal matroid.

        A transversal matroid can be represented as a set system, or as a
        bipartite graph with one color class corresponding to the groundset
        and the other to the sets of the set system. This method returns
        that bipartite graph.

        OUTPUT: :class:`Graph`

        EXAMPLES::

            sage: from sage.matroids.transversal_matroid import TransversalMatroid
            sage: edgedict = {5: [0, 1, 2, 3], 6: [1, 2], 7: [1, 3, 4]}
            sage: B = BipartiteGraph(edgedict)
            sage: M = TransversalMatroid(edgedict.values(), set_labels=edgedict.keys())
            sage: M.graph() == B
            True
            sage: M2 = TransversalMatroid(edgedict.values())
            sage: B2 = M2.graph()
            sage: B2 == B
            False
            sage: B2.is_isomorphic(B)
            True"""
    @overload
    def graph(self) -> Any:
        """TransversalMatroid.graph(self)

        File: /build/sagemath/src/sage/src/sage/matroids/transversal_matroid.pyx (starting at line 446)

        Return a bipartite graph representing the transversal matroid.

        A transversal matroid can be represented as a set system, or as a
        bipartite graph with one color class corresponding to the groundset
        and the other to the sets of the set system. This method returns
        that bipartite graph.

        OUTPUT: :class:`Graph`

        EXAMPLES::

            sage: from sage.matroids.transversal_matroid import TransversalMatroid
            sage: edgedict = {5: [0, 1, 2, 3], 6: [1, 2], 7: [1, 3, 4]}
            sage: B = BipartiteGraph(edgedict)
            sage: M = TransversalMatroid(edgedict.values(), set_labels=edgedict.keys())
            sage: M.graph() == B
            True
            sage: M2 = TransversalMatroid(edgedict.values())
            sage: B2 = M2.graph()
            sage: B2 == B
            False
            sage: B2.is_isomorphic(B)
            True"""
    @overload
    def is_valid(self, certificate=...) -> Any:
        """TransversalMatroid.is_valid(self, certificate=False)

        File: /build/sagemath/src/sage/src/sage/matroids/transversal_matroid.pyx (starting at line 842)

        Test whether the matching in memory is a valid maximal matching.

        The data for a transversal matroid is a set system, which is always valid,
        but it is possible for a user to provide invalid input with the ``matching``
        parameter. This checks that the matching provided is indeed a matching, fits in
        the set system, and is maximal.

        EXAMPLES::

            sage: from sage.matroids.transversal_matroid import *
            sage: sets = [[0, 1, 2, 3], [1, 2], [1, 3, 4]]
            sage: set_labels = [5, 6, 7]
            sage: M = TransversalMatroid(sets, set_labels=set_labels)
            sage: M.is_valid()
            True
            sage: m = {0: 5, 1: 5, 3: 7}  # not a matching
            sage: TransversalMatroid(sets, set_labels=set_labels, matching=m).is_valid()
            False
            sage: m = {2: 6, 3: 7}  # not maximal
            sage: TransversalMatroid(sets, set_labels=set_labels, matching=m).is_valid()
            False
            sage: m = {0: 6, 1: 5, 3: 7}  # not in the set system
            sage: TransversalMatroid(sets, set_labels=set_labels, matching=m).is_valid()
            False"""
    @overload
    def is_valid(self) -> Any:
        """TransversalMatroid.is_valid(self, certificate=False)

        File: /build/sagemath/src/sage/src/sage/matroids/transversal_matroid.pyx (starting at line 842)

        Test whether the matching in memory is a valid maximal matching.

        The data for a transversal matroid is a set system, which is always valid,
        but it is possible for a user to provide invalid input with the ``matching``
        parameter. This checks that the matching provided is indeed a matching, fits in
        the set system, and is maximal.

        EXAMPLES::

            sage: from sage.matroids.transversal_matroid import *
            sage: sets = [[0, 1, 2, 3], [1, 2], [1, 3, 4]]
            sage: set_labels = [5, 6, 7]
            sage: M = TransversalMatroid(sets, set_labels=set_labels)
            sage: M.is_valid()
            True
            sage: m = {0: 5, 1: 5, 3: 7}  # not a matching
            sage: TransversalMatroid(sets, set_labels=set_labels, matching=m).is_valid()
            False
            sage: m = {2: 6, 3: 7}  # not maximal
            sage: TransversalMatroid(sets, set_labels=set_labels, matching=m).is_valid()
            False
            sage: m = {0: 6, 1: 5, 3: 7}  # not in the set system
            sage: TransversalMatroid(sets, set_labels=set_labels, matching=m).is_valid()
            False"""
    @overload
    def is_valid(self) -> Any:
        """TransversalMatroid.is_valid(self, certificate=False)

        File: /build/sagemath/src/sage/src/sage/matroids/transversal_matroid.pyx (starting at line 842)

        Test whether the matching in memory is a valid maximal matching.

        The data for a transversal matroid is a set system, which is always valid,
        but it is possible for a user to provide invalid input with the ``matching``
        parameter. This checks that the matching provided is indeed a matching, fits in
        the set system, and is maximal.

        EXAMPLES::

            sage: from sage.matroids.transversal_matroid import *
            sage: sets = [[0, 1, 2, 3], [1, 2], [1, 3, 4]]
            sage: set_labels = [5, 6, 7]
            sage: M = TransversalMatroid(sets, set_labels=set_labels)
            sage: M.is_valid()
            True
            sage: m = {0: 5, 1: 5, 3: 7}  # not a matching
            sage: TransversalMatroid(sets, set_labels=set_labels, matching=m).is_valid()
            False
            sage: m = {2: 6, 3: 7}  # not maximal
            sage: TransversalMatroid(sets, set_labels=set_labels, matching=m).is_valid()
            False
            sage: m = {0: 6, 1: 5, 3: 7}  # not in the set system
            sage: TransversalMatroid(sets, set_labels=set_labels, matching=m).is_valid()
            False"""
    @overload
    def is_valid(self) -> Any:
        """TransversalMatroid.is_valid(self, certificate=False)

        File: /build/sagemath/src/sage/src/sage/matroids/transversal_matroid.pyx (starting at line 842)

        Test whether the matching in memory is a valid maximal matching.

        The data for a transversal matroid is a set system, which is always valid,
        but it is possible for a user to provide invalid input with the ``matching``
        parameter. This checks that the matching provided is indeed a matching, fits in
        the set system, and is maximal.

        EXAMPLES::

            sage: from sage.matroids.transversal_matroid import *
            sage: sets = [[0, 1, 2, 3], [1, 2], [1, 3, 4]]
            sage: set_labels = [5, 6, 7]
            sage: M = TransversalMatroid(sets, set_labels=set_labels)
            sage: M.is_valid()
            True
            sage: m = {0: 5, 1: 5, 3: 7}  # not a matching
            sage: TransversalMatroid(sets, set_labels=set_labels, matching=m).is_valid()
            False
            sage: m = {2: 6, 3: 7}  # not maximal
            sage: TransversalMatroid(sets, set_labels=set_labels, matching=m).is_valid()
            False
            sage: m = {0: 6, 1: 5, 3: 7}  # not in the set system
            sage: TransversalMatroid(sets, set_labels=set_labels, matching=m).is_valid()
            False"""
    @overload
    def is_valid(self) -> Any:
        """TransversalMatroid.is_valid(self, certificate=False)

        File: /build/sagemath/src/sage/src/sage/matroids/transversal_matroid.pyx (starting at line 842)

        Test whether the matching in memory is a valid maximal matching.

        The data for a transversal matroid is a set system, which is always valid,
        but it is possible for a user to provide invalid input with the ``matching``
        parameter. This checks that the matching provided is indeed a matching, fits in
        the set system, and is maximal.

        EXAMPLES::

            sage: from sage.matroids.transversal_matroid import *
            sage: sets = [[0, 1, 2, 3], [1, 2], [1, 3, 4]]
            sage: set_labels = [5, 6, 7]
            sage: M = TransversalMatroid(sets, set_labels=set_labels)
            sage: M.is_valid()
            True
            sage: m = {0: 5, 1: 5, 3: 7}  # not a matching
            sage: TransversalMatroid(sets, set_labels=set_labels, matching=m).is_valid()
            False
            sage: m = {2: 6, 3: 7}  # not maximal
            sage: TransversalMatroid(sets, set_labels=set_labels, matching=m).is_valid()
            False
            sage: m = {0: 6, 1: 5, 3: 7}  # not in the set system
            sage: TransversalMatroid(sets, set_labels=set_labels, matching=m).is_valid()
            False"""
    @overload
    def reduce_presentation(self) -> Any:
        """TransversalMatroid.reduce_presentation(self)

        File: /build/sagemath/src/sage/src/sage/matroids/transversal_matroid.pyx (starting at line 592)

        Return an equal transversal matroid where the number of sets equals the rank.

        Every transversal matroid `M` has a presentation with `r(M)` sets, and if `M`
        has no coloops, then every presentation has `r(M)` nonempty sets. This method
        discards extra sets if `M` has coloops.

        OUTPUT: :class:`TransversalMatroid` with a reduced presentation

        EXAMPLES::

            sage: from sage.matroids.transversal_matroid import TransversalMatroid
            sage: sets = [[0, 1], [2], [2]]
            sage: M = TransversalMatroid(sets); M
            Transversal matroid of rank 2 on 3 elements, with 3 sets
            sage: N = M.reduce_presentation(); N
            Transversal matroid of rank 2 on 3 elements, with 2 sets
            sage: N.equals(M)
            True
            sage: N == M
            False
            sage: sets = [[0, 1], [], [], [2]]
            sage: M1 = TransversalMatroid(sets); M1
            Transversal matroid of rank 2 on 3 elements, with 4 sets
            sage: M1.reduce_presentation()
            Transversal matroid of rank 2 on 3 elements, with 2 sets

        ::

            sage: from sage.matroids.transversal_matroid import TransversalMatroid
            sage: sets = [[0, 1, 2, 3]] * 3
            sage: M = TransversalMatroid(sets)
            sage: N = M.reduce_presentation()
            sage: M == N
            True

        TESTS::

            sage: from sage.matroids.transversal_matroid import TransversalMatroid
            sage: sets = [[4], [1, 3], [4], [0, 1], [2, 3], [1]]
            sage: M = TransversalMatroid(sets)
            sage: M1 = M.reduce_presentation(); M1
            Transversal matroid of rank 5 on 5 elements, with 5 sets
            sage: len(M1.graph().edges())
            5"""
    @overload
    def reduce_presentation(self) -> Any:
        """TransversalMatroid.reduce_presentation(self)

        File: /build/sagemath/src/sage/src/sage/matroids/transversal_matroid.pyx (starting at line 592)

        Return an equal transversal matroid where the number of sets equals the rank.

        Every transversal matroid `M` has a presentation with `r(M)` sets, and if `M`
        has no coloops, then every presentation has `r(M)` nonempty sets. This method
        discards extra sets if `M` has coloops.

        OUTPUT: :class:`TransversalMatroid` with a reduced presentation

        EXAMPLES::

            sage: from sage.matroids.transversal_matroid import TransversalMatroid
            sage: sets = [[0, 1], [2], [2]]
            sage: M = TransversalMatroid(sets); M
            Transversal matroid of rank 2 on 3 elements, with 3 sets
            sage: N = M.reduce_presentation(); N
            Transversal matroid of rank 2 on 3 elements, with 2 sets
            sage: N.equals(M)
            True
            sage: N == M
            False
            sage: sets = [[0, 1], [], [], [2]]
            sage: M1 = TransversalMatroid(sets); M1
            Transversal matroid of rank 2 on 3 elements, with 4 sets
            sage: M1.reduce_presentation()
            Transversal matroid of rank 2 on 3 elements, with 2 sets

        ::

            sage: from sage.matroids.transversal_matroid import TransversalMatroid
            sage: sets = [[0, 1, 2, 3]] * 3
            sage: M = TransversalMatroid(sets)
            sage: N = M.reduce_presentation()
            sage: M == N
            True

        TESTS::

            sage: from sage.matroids.transversal_matroid import TransversalMatroid
            sage: sets = [[4], [1, 3], [4], [0, 1], [2, 3], [1]]
            sage: M = TransversalMatroid(sets)
            sage: M1 = M.reduce_presentation(); M1
            Transversal matroid of rank 5 on 5 elements, with 5 sets
            sage: len(M1.graph().edges())
            5"""
    @overload
    def reduce_presentation(self) -> Any:
        """TransversalMatroid.reduce_presentation(self)

        File: /build/sagemath/src/sage/src/sage/matroids/transversal_matroid.pyx (starting at line 592)

        Return an equal transversal matroid where the number of sets equals the rank.

        Every transversal matroid `M` has a presentation with `r(M)` sets, and if `M`
        has no coloops, then every presentation has `r(M)` nonempty sets. This method
        discards extra sets if `M` has coloops.

        OUTPUT: :class:`TransversalMatroid` with a reduced presentation

        EXAMPLES::

            sage: from sage.matroids.transversal_matroid import TransversalMatroid
            sage: sets = [[0, 1], [2], [2]]
            sage: M = TransversalMatroid(sets); M
            Transversal matroid of rank 2 on 3 elements, with 3 sets
            sage: N = M.reduce_presentation(); N
            Transversal matroid of rank 2 on 3 elements, with 2 sets
            sage: N.equals(M)
            True
            sage: N == M
            False
            sage: sets = [[0, 1], [], [], [2]]
            sage: M1 = TransversalMatroid(sets); M1
            Transversal matroid of rank 2 on 3 elements, with 4 sets
            sage: M1.reduce_presentation()
            Transversal matroid of rank 2 on 3 elements, with 2 sets

        ::

            sage: from sage.matroids.transversal_matroid import TransversalMatroid
            sage: sets = [[0, 1, 2, 3]] * 3
            sage: M = TransversalMatroid(sets)
            sage: N = M.reduce_presentation()
            sage: M == N
            True

        TESTS::

            sage: from sage.matroids.transversal_matroid import TransversalMatroid
            sage: sets = [[4], [1, 3], [4], [0, 1], [2, 3], [1]]
            sage: M = TransversalMatroid(sets)
            sage: M1 = M.reduce_presentation(); M1
            Transversal matroid of rank 5 on 5 elements, with 5 sets
            sage: len(M1.graph().edges())
            5"""
    @overload
    def reduce_presentation(self) -> Any:
        """TransversalMatroid.reduce_presentation(self)

        File: /build/sagemath/src/sage/src/sage/matroids/transversal_matroid.pyx (starting at line 592)

        Return an equal transversal matroid where the number of sets equals the rank.

        Every transversal matroid `M` has a presentation with `r(M)` sets, and if `M`
        has no coloops, then every presentation has `r(M)` nonempty sets. This method
        discards extra sets if `M` has coloops.

        OUTPUT: :class:`TransversalMatroid` with a reduced presentation

        EXAMPLES::

            sage: from sage.matroids.transversal_matroid import TransversalMatroid
            sage: sets = [[0, 1], [2], [2]]
            sage: M = TransversalMatroid(sets); M
            Transversal matroid of rank 2 on 3 elements, with 3 sets
            sage: N = M.reduce_presentation(); N
            Transversal matroid of rank 2 on 3 elements, with 2 sets
            sage: N.equals(M)
            True
            sage: N == M
            False
            sage: sets = [[0, 1], [], [], [2]]
            sage: M1 = TransversalMatroid(sets); M1
            Transversal matroid of rank 2 on 3 elements, with 4 sets
            sage: M1.reduce_presentation()
            Transversal matroid of rank 2 on 3 elements, with 2 sets

        ::

            sage: from sage.matroids.transversal_matroid import TransversalMatroid
            sage: sets = [[0, 1, 2, 3]] * 3
            sage: M = TransversalMatroid(sets)
            sage: N = M.reduce_presentation()
            sage: M == N
            True

        TESTS::

            sage: from sage.matroids.transversal_matroid import TransversalMatroid
            sage: sets = [[4], [1, 3], [4], [0, 1], [2, 3], [1]]
            sage: M = TransversalMatroid(sets)
            sage: M1 = M.reduce_presentation(); M1
            Transversal matroid of rank 5 on 5 elements, with 5 sets
            sage: len(M1.graph().edges())
            5"""
    @overload
    def reduce_presentation(self) -> Any:
        """TransversalMatroid.reduce_presentation(self)

        File: /build/sagemath/src/sage/src/sage/matroids/transversal_matroid.pyx (starting at line 592)

        Return an equal transversal matroid where the number of sets equals the rank.

        Every transversal matroid `M` has a presentation with `r(M)` sets, and if `M`
        has no coloops, then every presentation has `r(M)` nonempty sets. This method
        discards extra sets if `M` has coloops.

        OUTPUT: :class:`TransversalMatroid` with a reduced presentation

        EXAMPLES::

            sage: from sage.matroids.transversal_matroid import TransversalMatroid
            sage: sets = [[0, 1], [2], [2]]
            sage: M = TransversalMatroid(sets); M
            Transversal matroid of rank 2 on 3 elements, with 3 sets
            sage: N = M.reduce_presentation(); N
            Transversal matroid of rank 2 on 3 elements, with 2 sets
            sage: N.equals(M)
            True
            sage: N == M
            False
            sage: sets = [[0, 1], [], [], [2]]
            sage: M1 = TransversalMatroid(sets); M1
            Transversal matroid of rank 2 on 3 elements, with 4 sets
            sage: M1.reduce_presentation()
            Transversal matroid of rank 2 on 3 elements, with 2 sets

        ::

            sage: from sage.matroids.transversal_matroid import TransversalMatroid
            sage: sets = [[0, 1, 2, 3]] * 3
            sage: M = TransversalMatroid(sets)
            sage: N = M.reduce_presentation()
            sage: M == N
            True

        TESTS::

            sage: from sage.matroids.transversal_matroid import TransversalMatroid
            sage: sets = [[4], [1, 3], [4], [0, 1], [2, 3], [1]]
            sage: M = TransversalMatroid(sets)
            sage: M1 = M.reduce_presentation(); M1
            Transversal matroid of rank 5 on 5 elements, with 5 sets
            sage: len(M1.graph().edges())
            5"""
    @overload
    def set_labels(self) -> Any:
        """TransversalMatroid.set_labels(self)

        File: /build/sagemath/src/sage/src/sage/matroids/transversal_matroid.pyx (starting at line 571)

        Return the labels used for the transversal sets.

        This method will return a list of the labels used of the non-ground
        set vertices of the bipartite graph used to represent the transversal
        matroid. This method does not set anything.

        OUTPUT: list

        EXAMPLES::

            sage: from sage.matroids.transversal_matroid import TransversalMatroid
            sage: M = TransversalMatroid([[0, 1], [1, 2, 3], [3, 4, 7]])
            sage: M.set_labels()
            ['s0', 's1', 's2']
            sage: M.graph().vertices()
            ['s0', 's1', 's2', 0, 1, 2, 3, 4, 7]"""
    @overload
    def set_labels(self) -> Any:
        """TransversalMatroid.set_labels(self)

        File: /build/sagemath/src/sage/src/sage/matroids/transversal_matroid.pyx (starting at line 571)

        Return the labels used for the transversal sets.

        This method will return a list of the labels used of the non-ground
        set vertices of the bipartite graph used to represent the transversal
        matroid. This method does not set anything.

        OUTPUT: list

        EXAMPLES::

            sage: from sage.matroids.transversal_matroid import TransversalMatroid
            sage: M = TransversalMatroid([[0, 1], [1, 2, 3], [3, 4, 7]])
            sage: M.set_labels()
            ['s0', 's1', 's2']
            sage: M.graph().vertices()
            ['s0', 's1', 's2', 0, 1, 2, 3, 4, 7]"""
    @overload
    def sets(self) -> list:
        """TransversalMatroid.sets(self) -> list

        File: /build/sagemath/src/sage/src/sage/matroids/transversal_matroid.pyx (starting at line 288)

        Return the sets of ``self``.

        A transversal matroid can be viewed as a groundset with a collection
        from its powerset. This is represented as a bipartite graph, where
        an edge represents containment.

        OUTPUT: list of lists that correspond to the sets of the transversal matroid

        EXAMPLES::

            sage: from sage.matroids.transversal_matroid import TransversalMatroid
            sage: sets = [[0, 1, 2, 3], [1, 2], [3, 4]]
            sage: set_labels = [5, 6, 7]
            sage: M = TransversalMatroid(sets, set_labels=set_labels)
            sage: sorted(M.sets()) == sorted(sets)
            True"""
    @overload
    def sets(self) -> Any:
        """TransversalMatroid.sets(self) -> list

        File: /build/sagemath/src/sage/src/sage/matroids/transversal_matroid.pyx (starting at line 288)

        Return the sets of ``self``.

        A transversal matroid can be viewed as a groundset with a collection
        from its powerset. This is represented as a bipartite graph, where
        an edge represents containment.

        OUTPUT: list of lists that correspond to the sets of the transversal matroid

        EXAMPLES::

            sage: from sage.matroids.transversal_matroid import TransversalMatroid
            sage: sets = [[0, 1, 2, 3], [1, 2], [3, 4]]
            sage: set_labels = [5, 6, 7]
            sage: M = TransversalMatroid(sets, set_labels=set_labels)
            sage: sorted(M.sets()) == sorted(sets)
            True"""
    @overload
    def transversal_extension(self, element=..., newset=..., sets=...) -> Any:
        """TransversalMatroid.transversal_extension(self, element=None, newset=False, sets=None)

        File: /build/sagemath/src/sage/src/sage/matroids/transversal_matroid.pyx (starting at line 667)

        Return a :class:`TransversalMatroid` extended by an element.

        This will modify the presentation of the transversal matroid by
        adding a new element, and placing this element in the specified
        sets. It is also possible to use this method to create a new set
        that will have the new element as its only member, making it a coloop.

        INPUT:

        - ``element`` -- (optional) the name for the new element
        - ``newset`` -- (optional) if specified, the element will be
          given its own set
        - ``sets`` -- iterable of labels (default: ``None``) representing the
          sets in the current presentation that the new element will belong to

        OUTPUT:

        A :class:`~sage.matroids.transversal_matroids.TransversalMatroid`
        with a groundset element added to specified sets. Note that the
        ``newset`` option will make the new element a coloop. If
        ``newset == True``, a name will be generated; otherwise the
        value of ``newset`` will be used.

        EXAMPLES::

            sage: from sage.matroids.transversal_matroid import TransversalMatroid
            sage: M = TransversalMatroid([['a', 'c']], groundset=['a', 'c'], set_labels=['b'])
            sage: M1 = M.transversal_extension(element='d', newset='e')
            sage: M2 = M.transversal_extension(element='d', newset=True)
            sage: M1.coloops()
            frozenset({'d'})
            sage: True in M2.graph().vertices()
            False
            sage: M1.is_isomorphic(M2)
            True
            sage: M3 = M.transversal_extension('d', sets=['b'])
            sage: M3.is_isomorphic(matroids.Uniform(1, 3))
            True
            sage: M4 = M.transversal_extension('d', sets=['a'])
            Traceback (most recent call last):
            ...
            ValueError: sets do not match presentation
            sage: M4 = M.transversal_extension('a', sets=['b'])
            Traceback (most recent call last):
            ...
            ValueError: cannot extend by element already in groundset
            sage: M2.transversal_extension(newset='b')
            Traceback (most recent call last):
            ...
            ValueError: newset is already a vertex in the presentation
            sage: M5 = M1.transversal_extension()
            sage: len(M5.loops())
            1
            sage: M2.transversal_extension(element='b')
            Transversal matroid of rank 2 on 4 elements, with 2 sets

        ::

            sage: from sage.matroids.transversal_matroid import TransversalMatroid
            sage: sets = [[0, 1, 2, 3], [1, 2], [1, 3, 4]]
            sage: M = TransversalMatroid(sets, groundset=range(5), set_labels=[5, 6, 7])
            sage: N = M.delete(2)
            sage: M1 = N.transversal_extension(element=2, sets=[5, 6])
            sage: M1 == M
            True

        ::

            sage: from sage.matroids.transversal_matroid import TransversalMatroid
            sage: sets = [[0, 1, 2, 3]] * 3
            sage: M = TransversalMatroid(sets, set_labels=[4, 5, 6])
            sage: N = M.transversal_extension(element='a', newset=True, sets=[4])
            sage: N.graph().degree('a')
            2

        TESTS::

            sage: N = TransversalMatroid(['abc', 'abd', 'cde']); N
            Transversal matroid of rank 3 on 5 elements, with 3 sets
            sage: Ne = N.transversal_extension(element='f', sets=['s2'])"""
    @overload
    def transversal_extension(self, element=..., newset=...) -> Any:
        """TransversalMatroid.transversal_extension(self, element=None, newset=False, sets=None)

        File: /build/sagemath/src/sage/src/sage/matroids/transversal_matroid.pyx (starting at line 667)

        Return a :class:`TransversalMatroid` extended by an element.

        This will modify the presentation of the transversal matroid by
        adding a new element, and placing this element in the specified
        sets. It is also possible to use this method to create a new set
        that will have the new element as its only member, making it a coloop.

        INPUT:

        - ``element`` -- (optional) the name for the new element
        - ``newset`` -- (optional) if specified, the element will be
          given its own set
        - ``sets`` -- iterable of labels (default: ``None``) representing the
          sets in the current presentation that the new element will belong to

        OUTPUT:

        A :class:`~sage.matroids.transversal_matroids.TransversalMatroid`
        with a groundset element added to specified sets. Note that the
        ``newset`` option will make the new element a coloop. If
        ``newset == True``, a name will be generated; otherwise the
        value of ``newset`` will be used.

        EXAMPLES::

            sage: from sage.matroids.transversal_matroid import TransversalMatroid
            sage: M = TransversalMatroid([['a', 'c']], groundset=['a', 'c'], set_labels=['b'])
            sage: M1 = M.transversal_extension(element='d', newset='e')
            sage: M2 = M.transversal_extension(element='d', newset=True)
            sage: M1.coloops()
            frozenset({'d'})
            sage: True in M2.graph().vertices()
            False
            sage: M1.is_isomorphic(M2)
            True
            sage: M3 = M.transversal_extension('d', sets=['b'])
            sage: M3.is_isomorphic(matroids.Uniform(1, 3))
            True
            sage: M4 = M.transversal_extension('d', sets=['a'])
            Traceback (most recent call last):
            ...
            ValueError: sets do not match presentation
            sage: M4 = M.transversal_extension('a', sets=['b'])
            Traceback (most recent call last):
            ...
            ValueError: cannot extend by element already in groundset
            sage: M2.transversal_extension(newset='b')
            Traceback (most recent call last):
            ...
            ValueError: newset is already a vertex in the presentation
            sage: M5 = M1.transversal_extension()
            sage: len(M5.loops())
            1
            sage: M2.transversal_extension(element='b')
            Transversal matroid of rank 2 on 4 elements, with 2 sets

        ::

            sage: from sage.matroids.transversal_matroid import TransversalMatroid
            sage: sets = [[0, 1, 2, 3], [1, 2], [1, 3, 4]]
            sage: M = TransversalMatroid(sets, groundset=range(5), set_labels=[5, 6, 7])
            sage: N = M.delete(2)
            sage: M1 = N.transversal_extension(element=2, sets=[5, 6])
            sage: M1 == M
            True

        ::

            sage: from sage.matroids.transversal_matroid import TransversalMatroid
            sage: sets = [[0, 1, 2, 3]] * 3
            sage: M = TransversalMatroid(sets, set_labels=[4, 5, 6])
            sage: N = M.transversal_extension(element='a', newset=True, sets=[4])
            sage: N.graph().degree('a')
            2

        TESTS::

            sage: N = TransversalMatroid(['abc', 'abd', 'cde']); N
            Transversal matroid of rank 3 on 5 elements, with 3 sets
            sage: Ne = N.transversal_extension(element='f', sets=['s2'])"""
    @overload
    def transversal_extension(self, element=..., newset=...) -> Any:
        """TransversalMatroid.transversal_extension(self, element=None, newset=False, sets=None)

        File: /build/sagemath/src/sage/src/sage/matroids/transversal_matroid.pyx (starting at line 667)

        Return a :class:`TransversalMatroid` extended by an element.

        This will modify the presentation of the transversal matroid by
        adding a new element, and placing this element in the specified
        sets. It is also possible to use this method to create a new set
        that will have the new element as its only member, making it a coloop.

        INPUT:

        - ``element`` -- (optional) the name for the new element
        - ``newset`` -- (optional) if specified, the element will be
          given its own set
        - ``sets`` -- iterable of labels (default: ``None``) representing the
          sets in the current presentation that the new element will belong to

        OUTPUT:

        A :class:`~sage.matroids.transversal_matroids.TransversalMatroid`
        with a groundset element added to specified sets. Note that the
        ``newset`` option will make the new element a coloop. If
        ``newset == True``, a name will be generated; otherwise the
        value of ``newset`` will be used.

        EXAMPLES::

            sage: from sage.matroids.transversal_matroid import TransversalMatroid
            sage: M = TransversalMatroid([['a', 'c']], groundset=['a', 'c'], set_labels=['b'])
            sage: M1 = M.transversal_extension(element='d', newset='e')
            sage: M2 = M.transversal_extension(element='d', newset=True)
            sage: M1.coloops()
            frozenset({'d'})
            sage: True in M2.graph().vertices()
            False
            sage: M1.is_isomorphic(M2)
            True
            sage: M3 = M.transversal_extension('d', sets=['b'])
            sage: M3.is_isomorphic(matroids.Uniform(1, 3))
            True
            sage: M4 = M.transversal_extension('d', sets=['a'])
            Traceback (most recent call last):
            ...
            ValueError: sets do not match presentation
            sage: M4 = M.transversal_extension('a', sets=['b'])
            Traceback (most recent call last):
            ...
            ValueError: cannot extend by element already in groundset
            sage: M2.transversal_extension(newset='b')
            Traceback (most recent call last):
            ...
            ValueError: newset is already a vertex in the presentation
            sage: M5 = M1.transversal_extension()
            sage: len(M5.loops())
            1
            sage: M2.transversal_extension(element='b')
            Transversal matroid of rank 2 on 4 elements, with 2 sets

        ::

            sage: from sage.matroids.transversal_matroid import TransversalMatroid
            sage: sets = [[0, 1, 2, 3], [1, 2], [1, 3, 4]]
            sage: M = TransversalMatroid(sets, groundset=range(5), set_labels=[5, 6, 7])
            sage: N = M.delete(2)
            sage: M1 = N.transversal_extension(element=2, sets=[5, 6])
            sage: M1 == M
            True

        ::

            sage: from sage.matroids.transversal_matroid import TransversalMatroid
            sage: sets = [[0, 1, 2, 3]] * 3
            sage: M = TransversalMatroid(sets, set_labels=[4, 5, 6])
            sage: N = M.transversal_extension(element='a', newset=True, sets=[4])
            sage: N.graph().degree('a')
            2

        TESTS::

            sage: N = TransversalMatroid(['abc', 'abd', 'cde']); N
            Transversal matroid of rank 3 on 5 elements, with 3 sets
            sage: Ne = N.transversal_extension(element='f', sets=['s2'])"""
    @overload
    def transversal_extension(self, newset=...) -> Any:
        """TransversalMatroid.transversal_extension(self, element=None, newset=False, sets=None)

        File: /build/sagemath/src/sage/src/sage/matroids/transversal_matroid.pyx (starting at line 667)

        Return a :class:`TransversalMatroid` extended by an element.

        This will modify the presentation of the transversal matroid by
        adding a new element, and placing this element in the specified
        sets. It is also possible to use this method to create a new set
        that will have the new element as its only member, making it a coloop.

        INPUT:

        - ``element`` -- (optional) the name for the new element
        - ``newset`` -- (optional) if specified, the element will be
          given its own set
        - ``sets`` -- iterable of labels (default: ``None``) representing the
          sets in the current presentation that the new element will belong to

        OUTPUT:

        A :class:`~sage.matroids.transversal_matroids.TransversalMatroid`
        with a groundset element added to specified sets. Note that the
        ``newset`` option will make the new element a coloop. If
        ``newset == True``, a name will be generated; otherwise the
        value of ``newset`` will be used.

        EXAMPLES::

            sage: from sage.matroids.transversal_matroid import TransversalMatroid
            sage: M = TransversalMatroid([['a', 'c']], groundset=['a', 'c'], set_labels=['b'])
            sage: M1 = M.transversal_extension(element='d', newset='e')
            sage: M2 = M.transversal_extension(element='d', newset=True)
            sage: M1.coloops()
            frozenset({'d'})
            sage: True in M2.graph().vertices()
            False
            sage: M1.is_isomorphic(M2)
            True
            sage: M3 = M.transversal_extension('d', sets=['b'])
            sage: M3.is_isomorphic(matroids.Uniform(1, 3))
            True
            sage: M4 = M.transversal_extension('d', sets=['a'])
            Traceback (most recent call last):
            ...
            ValueError: sets do not match presentation
            sage: M4 = M.transversal_extension('a', sets=['b'])
            Traceback (most recent call last):
            ...
            ValueError: cannot extend by element already in groundset
            sage: M2.transversal_extension(newset='b')
            Traceback (most recent call last):
            ...
            ValueError: newset is already a vertex in the presentation
            sage: M5 = M1.transversal_extension()
            sage: len(M5.loops())
            1
            sage: M2.transversal_extension(element='b')
            Transversal matroid of rank 2 on 4 elements, with 2 sets

        ::

            sage: from sage.matroids.transversal_matroid import TransversalMatroid
            sage: sets = [[0, 1, 2, 3], [1, 2], [1, 3, 4]]
            sage: M = TransversalMatroid(sets, groundset=range(5), set_labels=[5, 6, 7])
            sage: N = M.delete(2)
            sage: M1 = N.transversal_extension(element=2, sets=[5, 6])
            sage: M1 == M
            True

        ::

            sage: from sage.matroids.transversal_matroid import TransversalMatroid
            sage: sets = [[0, 1, 2, 3]] * 3
            sage: M = TransversalMatroid(sets, set_labels=[4, 5, 6])
            sage: N = M.transversal_extension(element='a', newset=True, sets=[4])
            sage: N.graph().degree('a')
            2

        TESTS::

            sage: N = TransversalMatroid(['abc', 'abd', 'cde']); N
            Transversal matroid of rank 3 on 5 elements, with 3 sets
            sage: Ne = N.transversal_extension(element='f', sets=['s2'])"""
    @overload
    def transversal_extension(self) -> Any:
        """TransversalMatroid.transversal_extension(self, element=None, newset=False, sets=None)

        File: /build/sagemath/src/sage/src/sage/matroids/transversal_matroid.pyx (starting at line 667)

        Return a :class:`TransversalMatroid` extended by an element.

        This will modify the presentation of the transversal matroid by
        adding a new element, and placing this element in the specified
        sets. It is also possible to use this method to create a new set
        that will have the new element as its only member, making it a coloop.

        INPUT:

        - ``element`` -- (optional) the name for the new element
        - ``newset`` -- (optional) if specified, the element will be
          given its own set
        - ``sets`` -- iterable of labels (default: ``None``) representing the
          sets in the current presentation that the new element will belong to

        OUTPUT:

        A :class:`~sage.matroids.transversal_matroids.TransversalMatroid`
        with a groundset element added to specified sets. Note that the
        ``newset`` option will make the new element a coloop. If
        ``newset == True``, a name will be generated; otherwise the
        value of ``newset`` will be used.

        EXAMPLES::

            sage: from sage.matroids.transversal_matroid import TransversalMatroid
            sage: M = TransversalMatroid([['a', 'c']], groundset=['a', 'c'], set_labels=['b'])
            sage: M1 = M.transversal_extension(element='d', newset='e')
            sage: M2 = M.transversal_extension(element='d', newset=True)
            sage: M1.coloops()
            frozenset({'d'})
            sage: True in M2.graph().vertices()
            False
            sage: M1.is_isomorphic(M2)
            True
            sage: M3 = M.transversal_extension('d', sets=['b'])
            sage: M3.is_isomorphic(matroids.Uniform(1, 3))
            True
            sage: M4 = M.transversal_extension('d', sets=['a'])
            Traceback (most recent call last):
            ...
            ValueError: sets do not match presentation
            sage: M4 = M.transversal_extension('a', sets=['b'])
            Traceback (most recent call last):
            ...
            ValueError: cannot extend by element already in groundset
            sage: M2.transversal_extension(newset='b')
            Traceback (most recent call last):
            ...
            ValueError: newset is already a vertex in the presentation
            sage: M5 = M1.transversal_extension()
            sage: len(M5.loops())
            1
            sage: M2.transversal_extension(element='b')
            Transversal matroid of rank 2 on 4 elements, with 2 sets

        ::

            sage: from sage.matroids.transversal_matroid import TransversalMatroid
            sage: sets = [[0, 1, 2, 3], [1, 2], [1, 3, 4]]
            sage: M = TransversalMatroid(sets, groundset=range(5), set_labels=[5, 6, 7])
            sage: N = M.delete(2)
            sage: M1 = N.transversal_extension(element=2, sets=[5, 6])
            sage: M1 == M
            True

        ::

            sage: from sage.matroids.transversal_matroid import TransversalMatroid
            sage: sets = [[0, 1, 2, 3]] * 3
            sage: M = TransversalMatroid(sets, set_labels=[4, 5, 6])
            sage: N = M.transversal_extension(element='a', newset=True, sets=[4])
            sage: N.graph().degree('a')
            2

        TESTS::

            sage: N = TransversalMatroid(['abc', 'abd', 'cde']); N
            Transversal matroid of rank 3 on 5 elements, with 3 sets
            sage: Ne = N.transversal_extension(element='f', sets=['s2'])"""
    @overload
    def transversal_extension(self, element=...) -> Any:
        """TransversalMatroid.transversal_extension(self, element=None, newset=False, sets=None)

        File: /build/sagemath/src/sage/src/sage/matroids/transversal_matroid.pyx (starting at line 667)

        Return a :class:`TransversalMatroid` extended by an element.

        This will modify the presentation of the transversal matroid by
        adding a new element, and placing this element in the specified
        sets. It is also possible to use this method to create a new set
        that will have the new element as its only member, making it a coloop.

        INPUT:

        - ``element`` -- (optional) the name for the new element
        - ``newset`` -- (optional) if specified, the element will be
          given its own set
        - ``sets`` -- iterable of labels (default: ``None``) representing the
          sets in the current presentation that the new element will belong to

        OUTPUT:

        A :class:`~sage.matroids.transversal_matroids.TransversalMatroid`
        with a groundset element added to specified sets. Note that the
        ``newset`` option will make the new element a coloop. If
        ``newset == True``, a name will be generated; otherwise the
        value of ``newset`` will be used.

        EXAMPLES::

            sage: from sage.matroids.transversal_matroid import TransversalMatroid
            sage: M = TransversalMatroid([['a', 'c']], groundset=['a', 'c'], set_labels=['b'])
            sage: M1 = M.transversal_extension(element='d', newset='e')
            sage: M2 = M.transversal_extension(element='d', newset=True)
            sage: M1.coloops()
            frozenset({'d'})
            sage: True in M2.graph().vertices()
            False
            sage: M1.is_isomorphic(M2)
            True
            sage: M3 = M.transversal_extension('d', sets=['b'])
            sage: M3.is_isomorphic(matroids.Uniform(1, 3))
            True
            sage: M4 = M.transversal_extension('d', sets=['a'])
            Traceback (most recent call last):
            ...
            ValueError: sets do not match presentation
            sage: M4 = M.transversal_extension('a', sets=['b'])
            Traceback (most recent call last):
            ...
            ValueError: cannot extend by element already in groundset
            sage: M2.transversal_extension(newset='b')
            Traceback (most recent call last):
            ...
            ValueError: newset is already a vertex in the presentation
            sage: M5 = M1.transversal_extension()
            sage: len(M5.loops())
            1
            sage: M2.transversal_extension(element='b')
            Transversal matroid of rank 2 on 4 elements, with 2 sets

        ::

            sage: from sage.matroids.transversal_matroid import TransversalMatroid
            sage: sets = [[0, 1, 2, 3], [1, 2], [1, 3, 4]]
            sage: M = TransversalMatroid(sets, groundset=range(5), set_labels=[5, 6, 7])
            sage: N = M.delete(2)
            sage: M1 = N.transversal_extension(element=2, sets=[5, 6])
            sage: M1 == M
            True

        ::

            sage: from sage.matroids.transversal_matroid import TransversalMatroid
            sage: sets = [[0, 1, 2, 3]] * 3
            sage: M = TransversalMatroid(sets, set_labels=[4, 5, 6])
            sage: N = M.transversal_extension(element='a', newset=True, sets=[4])
            sage: N.graph().degree('a')
            2

        TESTS::

            sage: N = TransversalMatroid(['abc', 'abd', 'cde']); N
            Transversal matroid of rank 3 on 5 elements, with 3 sets
            sage: Ne = N.transversal_extension(element='f', sets=['s2'])"""
    @overload
    def transversal_extension(self, element=..., sets=...) -> Any:
        """TransversalMatroid.transversal_extension(self, element=None, newset=False, sets=None)

        File: /build/sagemath/src/sage/src/sage/matroids/transversal_matroid.pyx (starting at line 667)

        Return a :class:`TransversalMatroid` extended by an element.

        This will modify the presentation of the transversal matroid by
        adding a new element, and placing this element in the specified
        sets. It is also possible to use this method to create a new set
        that will have the new element as its only member, making it a coloop.

        INPUT:

        - ``element`` -- (optional) the name for the new element
        - ``newset`` -- (optional) if specified, the element will be
          given its own set
        - ``sets`` -- iterable of labels (default: ``None``) representing the
          sets in the current presentation that the new element will belong to

        OUTPUT:

        A :class:`~sage.matroids.transversal_matroids.TransversalMatroid`
        with a groundset element added to specified sets. Note that the
        ``newset`` option will make the new element a coloop. If
        ``newset == True``, a name will be generated; otherwise the
        value of ``newset`` will be used.

        EXAMPLES::

            sage: from sage.matroids.transversal_matroid import TransversalMatroid
            sage: M = TransversalMatroid([['a', 'c']], groundset=['a', 'c'], set_labels=['b'])
            sage: M1 = M.transversal_extension(element='d', newset='e')
            sage: M2 = M.transversal_extension(element='d', newset=True)
            sage: M1.coloops()
            frozenset({'d'})
            sage: True in M2.graph().vertices()
            False
            sage: M1.is_isomorphic(M2)
            True
            sage: M3 = M.transversal_extension('d', sets=['b'])
            sage: M3.is_isomorphic(matroids.Uniform(1, 3))
            True
            sage: M4 = M.transversal_extension('d', sets=['a'])
            Traceback (most recent call last):
            ...
            ValueError: sets do not match presentation
            sage: M4 = M.transversal_extension('a', sets=['b'])
            Traceback (most recent call last):
            ...
            ValueError: cannot extend by element already in groundset
            sage: M2.transversal_extension(newset='b')
            Traceback (most recent call last):
            ...
            ValueError: newset is already a vertex in the presentation
            sage: M5 = M1.transversal_extension()
            sage: len(M5.loops())
            1
            sage: M2.transversal_extension(element='b')
            Transversal matroid of rank 2 on 4 elements, with 2 sets

        ::

            sage: from sage.matroids.transversal_matroid import TransversalMatroid
            sage: sets = [[0, 1, 2, 3], [1, 2], [1, 3, 4]]
            sage: M = TransversalMatroid(sets, groundset=range(5), set_labels=[5, 6, 7])
            sage: N = M.delete(2)
            sage: M1 = N.transversal_extension(element=2, sets=[5, 6])
            sage: M1 == M
            True

        ::

            sage: from sage.matroids.transversal_matroid import TransversalMatroid
            sage: sets = [[0, 1, 2, 3]] * 3
            sage: M = TransversalMatroid(sets, set_labels=[4, 5, 6])
            sage: N = M.transversal_extension(element='a', newset=True, sets=[4])
            sage: N.graph().degree('a')
            2

        TESTS::

            sage: N = TransversalMatroid(['abc', 'abd', 'cde']); N
            Transversal matroid of rank 3 on 5 elements, with 3 sets
            sage: Ne = N.transversal_extension(element='f', sets=['s2'])"""
    @overload
    def transversal_extension(self, element=..., newset=..., sets=...) -> Any:
        """TransversalMatroid.transversal_extension(self, element=None, newset=False, sets=None)

        File: /build/sagemath/src/sage/src/sage/matroids/transversal_matroid.pyx (starting at line 667)

        Return a :class:`TransversalMatroid` extended by an element.

        This will modify the presentation of the transversal matroid by
        adding a new element, and placing this element in the specified
        sets. It is also possible to use this method to create a new set
        that will have the new element as its only member, making it a coloop.

        INPUT:

        - ``element`` -- (optional) the name for the new element
        - ``newset`` -- (optional) if specified, the element will be
          given its own set
        - ``sets`` -- iterable of labels (default: ``None``) representing the
          sets in the current presentation that the new element will belong to

        OUTPUT:

        A :class:`~sage.matroids.transversal_matroids.TransversalMatroid`
        with a groundset element added to specified sets. Note that the
        ``newset`` option will make the new element a coloop. If
        ``newset == True``, a name will be generated; otherwise the
        value of ``newset`` will be used.

        EXAMPLES::

            sage: from sage.matroids.transversal_matroid import TransversalMatroid
            sage: M = TransversalMatroid([['a', 'c']], groundset=['a', 'c'], set_labels=['b'])
            sage: M1 = M.transversal_extension(element='d', newset='e')
            sage: M2 = M.transversal_extension(element='d', newset=True)
            sage: M1.coloops()
            frozenset({'d'})
            sage: True in M2.graph().vertices()
            False
            sage: M1.is_isomorphic(M2)
            True
            sage: M3 = M.transversal_extension('d', sets=['b'])
            sage: M3.is_isomorphic(matroids.Uniform(1, 3))
            True
            sage: M4 = M.transversal_extension('d', sets=['a'])
            Traceback (most recent call last):
            ...
            ValueError: sets do not match presentation
            sage: M4 = M.transversal_extension('a', sets=['b'])
            Traceback (most recent call last):
            ...
            ValueError: cannot extend by element already in groundset
            sage: M2.transversal_extension(newset='b')
            Traceback (most recent call last):
            ...
            ValueError: newset is already a vertex in the presentation
            sage: M5 = M1.transversal_extension()
            sage: len(M5.loops())
            1
            sage: M2.transversal_extension(element='b')
            Transversal matroid of rank 2 on 4 elements, with 2 sets

        ::

            sage: from sage.matroids.transversal_matroid import TransversalMatroid
            sage: sets = [[0, 1, 2, 3], [1, 2], [1, 3, 4]]
            sage: M = TransversalMatroid(sets, groundset=range(5), set_labels=[5, 6, 7])
            sage: N = M.delete(2)
            sage: M1 = N.transversal_extension(element=2, sets=[5, 6])
            sage: M1 == M
            True

        ::

            sage: from sage.matroids.transversal_matroid import TransversalMatroid
            sage: sets = [[0, 1, 2, 3]] * 3
            sage: M = TransversalMatroid(sets, set_labels=[4, 5, 6])
            sage: N = M.transversal_extension(element='a', newset=True, sets=[4])
            sage: N.graph().degree('a')
            2

        TESTS::

            sage: N = TransversalMatroid(['abc', 'abd', 'cde']); N
            Transversal matroid of rank 3 on 5 elements, with 3 sets
            sage: Ne = N.transversal_extension(element='f', sets=['s2'])"""
    @overload
    def transversal_extension(self, element=..., sets=...) -> Any:
        """TransversalMatroid.transversal_extension(self, element=None, newset=False, sets=None)

        File: /build/sagemath/src/sage/src/sage/matroids/transversal_matroid.pyx (starting at line 667)

        Return a :class:`TransversalMatroid` extended by an element.

        This will modify the presentation of the transversal matroid by
        adding a new element, and placing this element in the specified
        sets. It is also possible to use this method to create a new set
        that will have the new element as its only member, making it a coloop.

        INPUT:

        - ``element`` -- (optional) the name for the new element
        - ``newset`` -- (optional) if specified, the element will be
          given its own set
        - ``sets`` -- iterable of labels (default: ``None``) representing the
          sets in the current presentation that the new element will belong to

        OUTPUT:

        A :class:`~sage.matroids.transversal_matroids.TransversalMatroid`
        with a groundset element added to specified sets. Note that the
        ``newset`` option will make the new element a coloop. If
        ``newset == True``, a name will be generated; otherwise the
        value of ``newset`` will be used.

        EXAMPLES::

            sage: from sage.matroids.transversal_matroid import TransversalMatroid
            sage: M = TransversalMatroid([['a', 'c']], groundset=['a', 'c'], set_labels=['b'])
            sage: M1 = M.transversal_extension(element='d', newset='e')
            sage: M2 = M.transversal_extension(element='d', newset=True)
            sage: M1.coloops()
            frozenset({'d'})
            sage: True in M2.graph().vertices()
            False
            sage: M1.is_isomorphic(M2)
            True
            sage: M3 = M.transversal_extension('d', sets=['b'])
            sage: M3.is_isomorphic(matroids.Uniform(1, 3))
            True
            sage: M4 = M.transversal_extension('d', sets=['a'])
            Traceback (most recent call last):
            ...
            ValueError: sets do not match presentation
            sage: M4 = M.transversal_extension('a', sets=['b'])
            Traceback (most recent call last):
            ...
            ValueError: cannot extend by element already in groundset
            sage: M2.transversal_extension(newset='b')
            Traceback (most recent call last):
            ...
            ValueError: newset is already a vertex in the presentation
            sage: M5 = M1.transversal_extension()
            sage: len(M5.loops())
            1
            sage: M2.transversal_extension(element='b')
            Transversal matroid of rank 2 on 4 elements, with 2 sets

        ::

            sage: from sage.matroids.transversal_matroid import TransversalMatroid
            sage: sets = [[0, 1, 2, 3], [1, 2], [1, 3, 4]]
            sage: M = TransversalMatroid(sets, groundset=range(5), set_labels=[5, 6, 7])
            sage: N = M.delete(2)
            sage: M1 = N.transversal_extension(element=2, sets=[5, 6])
            sage: M1 == M
            True

        ::

            sage: from sage.matroids.transversal_matroid import TransversalMatroid
            sage: sets = [[0, 1, 2, 3]] * 3
            sage: M = TransversalMatroid(sets, set_labels=[4, 5, 6])
            sage: N = M.transversal_extension(element='a', newset=True, sets=[4])
            sage: N.graph().degree('a')
            2

        TESTS::

            sage: N = TransversalMatroid(['abc', 'abd', 'cde']); N
            Transversal matroid of rank 3 on 5 elements, with 3 sets
            sage: Ne = N.transversal_extension(element='f', sets=['s2'])"""
    def transversal_extensions(self, element=..., sets=...) -> Any:
        """TransversalMatroid.transversal_extensions(self, element=None, sets=None)

        File: /build/sagemath/src/sage/src/sage/matroids/transversal_matroid.pyx (starting at line 792)

        Return an iterator of extensions based on the transversal presentation.

        This method will take an extension by adding an element to every possible
        sub-collection of the collection of desired sets. No checking is done
        for equal matroids. It is advised to make sure the presentation has as
        few sets as possible by using
        :meth:`reduce_presentation() <sage.matroids.transversal_matroid.TransversalMatroid.reduce_presentation>`

        INPUT:

        - ``element`` -- (optional) the name of the new element
        - ``sets`` -- (optional) list containing names of sets in the matroid's
          presentation

        OUTPUT: iterator over instances of :class:`TransversalMatroid`

        If ``sets`` is not specified, every set will be used.

        EXAMPLES::

            sage: from sage.matroids.transversal_matroid import TransversalMatroid
            sage: sets = [[3, 4, 5, 6]] * 3
            sage: M = TransversalMatroid(sets, set_labels=[0, 1, 2])
            sage: len([N for N in M.transversal_extensions()])
            8
            sage: len([N for N in M.transversal_extensions(sets=[0, 1])])
            4
            sage: set(sorted([N.groundset() for N in M.transversal_extensions(element=7)]))
            {frozenset({3, 4, 5, 6, 7})}"""
    def __eq__(self, other: object) -> bool:
        """Return self==value."""
    def __ge__(self, other: object) -> bool:
        """Return self>=value."""
    def __gt__(self, other: object) -> bool:
        """Return self>value."""
    def __hash__(self) -> Any:
        """TransversalMatroid.__hash__(self)

        File: /build/sagemath/src/sage/src/sage/matroids/transversal_matroid.pyx (starting at line 375)

        Return the hash of ``self``.

        The hash is based on the groundset and an internal Counter of the
        collection of sets.

        This function is called when matroids are added to a set. It is very
        desirable to override it so it can distinguish matroids on the same
        groundset, which is a very typical use case!

        .. WARNING::

            This method is linked to ``__richcmp__`` (in Cython) and
            ``__eq__`` (in Python). If you override one, you must
            override the other!

        EXAMPLES::

            sage: from sage.matroids.transversal_matroid import TransversalMatroid
            sage: sets1 = [[0, 1, 2, 3], [1, 2], [3, 4]]
            sage: M1 = TransversalMatroid(sets1)
            sage: M2 = TransversalMatroid(sets1, set_labels=[5, 6, 7])
            sage: sets3 = [['a', 'b', 'c'], ['c', 'd'], ['a', 'd', 'e']]
            sage: M3 = TransversalMatroid(sets3)
            sage: hash(M1) == hash(M2)
            True
            sage: hash(M1) == hash(M3)
            False"""
    def __le__(self, other: object) -> bool:
        """Return self<=value."""
    def __lt__(self, other: object) -> bool:
        """Return self<value."""
    def __ne__(self, other: object) -> bool:
        """Return self!=value."""
    def __reduce__(self) -> Any:
        """TransversalMatroid.__reduce__(self)

        File: /build/sagemath/src/sage/src/sage/matroids/transversal_matroid.pyx (starting at line 416)

        Save the matroid for later reloading.

        OUTPUT:

        A tuple ``(unpickle, (version, data))``, where ``unpickle`` is the
        name of a function that, when called with ``(version, data)``,
        produces a matroid isomorphic to ``self``. ``version`` is an integer
        (currently 0) and ``data`` is a tuple ``(sets, E, name)`` where
        ``E`` is the groundset of the matroid, ``sets`` is the subsets of the
        transversal, and ``name`` is a custom name.

        EXAMPLES::

            sage: from sage.matroids.transversal_matroid import *
            sage: sets = [range(6)] * 3
            sage: M = TransversalMatroid(sets)
            sage: M == loads(dumps(M))
            True
            sage: M.rename('U36')
            sage: loads(dumps(M))
            U36"""
