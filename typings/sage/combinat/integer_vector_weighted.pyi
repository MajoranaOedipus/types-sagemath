from _typeshed import Incomplete
from collections.abc import Generator
from sage.categories.finite_enumerated_sets import FiniteEnumeratedSets as FiniteEnumeratedSets
from sage.categories.infinite_enumerated_sets import InfiniteEnumeratedSets as InfiniteEnumeratedSets
from sage.categories.sets_with_grading import SetsWithGrading as SetsWithGrading
from sage.combinat.integer_vector import IntegerVector as IntegerVector
from sage.combinat.permutation import Permutation as Permutation
from sage.misc.lazy_import import lazy_import as lazy_import
from sage.misc.persist import register_unpickle_override as register_unpickle_override
from sage.rings.integer import Integer as Integer
from sage.rings.integer_ring import ZZ as ZZ
from sage.sets.disjoint_union_enumerated_sets import DisjointUnionEnumeratedSets as DisjointUnionEnumeratedSets
from sage.structure.parent import Parent as Parent
from sage.structure.unique_representation import UniqueRepresentation as UniqueRepresentation

class WeightedIntegerVectors(Parent, UniqueRepresentation):
    """
    The class of integer vectors of `n` weighted by ``weight``, that is, the
    nonnegative integer vectors `(v_1, \\ldots, v_{\\ell})`
    satisfying `\\sum_{i=1}^{\\ell} v_i w_i = n` where `\\ell` is
    ``length(weight)`` and `w_i` is ``weight[i]``.

    INPUT:

    - ``n`` -- nonnegative integer (optional)

    - ``weight`` -- tuple (or list or iterable) of positive integers

    EXAMPLES::

        sage: WeightedIntegerVectors(8, [1,1,2])
        Integer vectors of 8 weighted by [1, 1, 2]
        sage: WeightedIntegerVectors(8, [1,1,2]).first()
        [0, 0, 4]
        sage: WeightedIntegerVectors(8, [1,1,2]).last()
        [8, 0, 0]
        sage: WeightedIntegerVectors(8, [1,1,2]).cardinality()
        25
        sage: w = WeightedIntegerVectors(8, [1,1,2]).random_element()
        sage: w.parent() is WeightedIntegerVectors(8, [1,1,2])
        True

        sage: WeightedIntegerVectors([1,1,2])
        Integer vectors weighted by [1, 1, 2]
        sage: WeightedIntegerVectors([1,1,2]).cardinality()
        +Infinity
        sage: WeightedIntegerVectors([1,1,2]).first()
        [0, 0, 0]

    TESTS::

        sage: WeightedIntegerVectors(None,None)
        Traceback (most recent call last):
        ...
        ValueError: the weights must be specified

    .. TODO::

        Should the order of the arguments ``n`` and ``weight`` be
        exchanged to simplify the logic?
    """
    @staticmethod
    def __classcall_private__(cls, n=None, weight=None):
        """
        Normalize inputs to ensure a unique representation.

        TESTS::

            sage: W = WeightedIntegerVectors(8, [1,1,2])
            sage: W2 = WeightedIntegerVectors(int(8), (1,1,2))
            sage: W is W2
            True
        """
    def __init__(self, n, weight) -> None:
        """
        TESTS::

            sage: WIV = WeightedIntegerVectors(8, [1,1,2])
            sage: TestSuite(WIV).run()
        """
    Element = IntegerVector
    def __contains__(self, x) -> bool:
        """
        EXAMPLES::

            sage: [] in WeightedIntegerVectors(0, [])
            True
            sage: [] in WeightedIntegerVectors(1, [])
            False
            sage: [3,0,0] in WeightedIntegerVectors(6, [2,1,1])
            True
            sage: [1] in WeightedIntegerVectors(1, [1])
            True
            sage: [1] in WeightedIntegerVectors(2, [2])
            True
            sage: [2] in WeightedIntegerVectors(4, [2])
            True
            sage: [2, 0] in WeightedIntegerVectors(4, [2, 2])
            True
            sage: [2, 1] in WeightedIntegerVectors(4, [2, 2])
            False
            sage: [2, 1] in WeightedIntegerVectors(6, [2, 2])
            True
            sage: [2, 1, 0] in WeightedIntegerVectors(6, [2, 2])
            False
            sage: [0] in WeightedIntegerVectors(0, [])
            False
        """
    def __iter__(self):
        """
        TESTS::

            sage: WeightedIntegerVectors(7, [2,2]).list()
            []
            sage: WeightedIntegerVectors(3, [2,1,1]).list()
            [[1, 0, 1], [1, 1, 0], [0, 0, 3], [0, 1, 2], [0, 2, 1], [0, 3, 0]]

        ::

            sage: ivw = [ WeightedIntegerVectors(k, [1,1,1]) for k in range(11) ]
            sage: iv  = [ IntegerVectors(k, 3) for k in range(11) ]
            sage: all(sorted(map(list, iv[k])) == sorted(map(list, ivw[k])) for k in range(11))
            True

        ::

            sage: ivw = [ WeightedIntegerVectors(k, [2,3,7]) for k in range(11) ]
            sage: all(i.cardinality() == len(i.list()) for i in ivw)
            True
        """

class WeightedIntegerVectors_all(DisjointUnionEnumeratedSets):
    """
    Set of weighted integer vectors.

    EXAMPLES::

        sage: W = WeightedIntegerVectors([3,1,1,2,1]); W
        Integer vectors weighted by [3, 1, 1, 2, 1]
        sage: W.cardinality()
        +Infinity

        sage: W12 = W.graded_component(12)
        sage: W12.an_element()
        [4, 0, 0, 0, 0]
        sage: W12.last()
        [0, 12, 0, 0, 0]
        sage: W12.cardinality()
        441
        sage: for w in W12: print(w)
        [4, 0, 0, 0, 0]
        [3, 0, 0, 1, 1]
        [3, 0, 1, 1, 0]
        ...
        [0, 11, 1, 0, 0]
        [0, 12, 0, 0, 0]
    """
    def __init__(self, weight) -> None:
        """
        TESTS::

            sage: C = WeightedIntegerVectors([2,1,3])
            sage: C.category()
            Category of facade infinite enumerated sets with grading
            sage: TestSuite(C).run()
        """
    def __contains__(self, x) -> bool:
        """
        EXAMPLES::

            sage: [] in WeightedIntegerVectors([])
            True
            sage: [3,0,0] in WeightedIntegerVectors([2,1,1])
            True
            sage: [3,0] in WeightedIntegerVectors([2,1,1])
            False
            sage: [3,-1,0] in WeightedIntegerVectors([2,1,1])
            False
        """
    def subset(self, size=None):
        """
        EXAMPLES::

            sage: C = WeightedIntegerVectors([2,1,3])
            sage: C.subset(4)
            Integer vectors of 4 weighted by [2, 1, 3]
        """
    def grading(self, x):
        """
        EXAMPLES::

            sage: C = WeightedIntegerVectors([2,1,3])
            sage: C.grading((2,1,1))
            8
        """

def iterator_fast(n, l) -> Generator[Incomplete]:
    """
    Iterate over all ``l`` weighted integer vectors with total weight ``n``.

    INPUT:

    - ``n`` -- integer
    - ``l`` -- the weights in weakly decreasing order

    EXAMPLES::

        sage: from sage.combinat.integer_vector_weighted import iterator_fast
        sage: list(iterator_fast(3, [2,1,1]))
        [[1, 1, 0], [1, 0, 1], [0, 3, 0], [0, 2, 1], [0, 1, 2], [0, 0, 3]]
        sage: list(iterator_fast(2, [2]))
        [[1]]

    Test that :issue:`20491` is fixed::

        sage: type(list(iterator_fast(2, [2]))[0][0])
        <class 'sage.rings.integer.Integer'>
    """
