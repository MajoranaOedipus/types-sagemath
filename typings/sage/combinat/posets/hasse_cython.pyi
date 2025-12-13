import sage.sets.recursively_enumerated_set
from sage.categories.finite_enumerated_sets import FiniteEnumeratedSets as FiniteEnumeratedSets
from sage.combinat.posets.hasse_cython_flint import coxeter_matrix_fast as coxeter_matrix_fast, moebius_matrix_fast as moebius_matrix_fast
from sage.misc.lazy_import import LazyImport as LazyImport
from sage.sets.recursively_enumerated_set import RecursivelyEnumeratedSet_forest as RecursivelyEnumeratedSet_forest
from typing import Any

class IncreasingChains(sage.sets.recursively_enumerated_set.RecursivelyEnumeratedSet_forest):
    """File: /build/sagemath/src/sage/src/sage/combinat/posets/hasse_cython.pyx (starting at line 24)

        The enumerated set of increasing chains.

        INPUT:

        - ``positions`` -- list of sets of integers describing the poset,
          as given by the lazy attribute ``_leq_storage`` of Hasse diagrams

        - ``element_constructor`` -- used to determine the type of chains,
          for example :class:`list` or :class:`tuple`

        - ``exclude`` -- list of integers that should not belong to the chains

        - ``conversion`` -- (optional) list of elements of the poset

        If ``conversion`` is provided, it is used to convert chain elements
        to elements of this list.

        EXAMPLES::

            sage: from sage.combinat.posets.hasse_cython import IncreasingChains
            sage: D = IncreasingChains([{0,1},{1}], list, []); D
            An enumerated set with a forest structure
            sage: D.cardinality()
            4
            sage: list(D)
            [[], [0], [0, 1], [1]]
    """
    def __init__(self, listpositions, element_constructor, listexclude, conversion=...) -> Any:
        """IncreasingChains.__init__(self, list positions, element_constructor, list exclude, conversion=None)

        File: /build/sagemath/src/sage/src/sage/combinat/posets/hasse_cython.pyx (starting at line 53)

        The enumerated set of increasing chains.

        TESTS::

            sage: from sage.combinat.posets.hasse_cython import IncreasingChains
            sage: D = IncreasingChains([{0,1},{1}], list, [])
            sage: TestSuite(D).run(skip='_test_pickling')"""
    def children(self, chain) -> Any:
        """IncreasingChains.children(self, chain)

        File: /build/sagemath/src/sage/src/sage/combinat/posets/hasse_cython.pyx (starting at line 154)

        Return the children of a chain, by adding one largest element.

        EXAMPLES::

            sage: from sage.combinat.posets.hasse_cython import IncreasingChains
            sage: D = IncreasingChains([{0,1},{1}], list, [])
            sage: D.children((0,))
            [(0, 1)]

            sage: P = Poset({'a':['b'],'b':[]})
            sage: next(iter(P.chains()))
            []"""
    def post_process(self, chain) -> Any:
        """IncreasingChains.post_process(self, chain)

        File: /build/sagemath/src/sage/src/sage/combinat/posets/hasse_cython.pyx (starting at line 129)

        Create a chain from the internal object.

        If ``conversion`` was provided, it first converts elements of the
        chain to elements of this list.

        Then the given ``element_constructor`` is applied to the chain.

        EXAMPLES::

            sage: from sage.combinat.posets.hasse_cython import IncreasingChains
            sage: D = IncreasingChains([{0,1},{1}], list, [])
            sage: D.post_process((0,1))
            [0, 1]

            sage: P = Poset({'a':['b'],'b':[]})
            sage: list(P.chains())
            [[], ['a'], ['a', 'b'], ['b']]"""
    def __contains__(self, tup) -> Any:
        """IncreasingChains.__contains__(self, tup)

        File: /build/sagemath/src/sage/src/sage/combinat/posets/hasse_cython.pyx (starting at line 84)

        Membership testing.

        If ``conversion`` was provided, it first converts elements of ``tup``
        to integers.

        EXAMPLES::

            sage: from sage.combinat.posets.hasse_cython import IncreasingChains
            sage: D = IncreasingChains([{0,1},{1}], list, [])
            sage: all(x in D for x in D)
            True
            sage: [2] in D
            False
            sage: [1,1] in D
            False

            sage: P = Poset({'a':['b'],'b':[]})
            sage: ['a'] in P.chains()
            True

        TESTS::

            sage: from sage.combinat.posets.hasse_cython import IncreasingChains
            sage: D = IncreasingChains([{0,1},{1}], list, [])
            sage: all(tuple(x) in D for x in D)
            True"""
