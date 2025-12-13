from _typeshed import Incomplete
from sage.combinat.permutation import Permutations as Permutations
from sage.combinat.posets.posets import Poset as Poset
from sage.graphs.digraph import DiGraph as DiGraph

class ShardPosetElement(tuple):
    """
    An element of the shard poset.

    This is basically a permutation with extra stored arguments:

    - ``p`` -- the permutation itself as a tuple
    - ``runs`` -- the decreasing runs as a tuple of tuples
    - ``run_indices`` -- list; ``integer -> index of the run``
    - ``dpg`` -- the transitive closure of the shard preorder graph
    - ``spg`` -- the transitive reduction of the shard preorder graph

    These elements can easily be converted from and to permutations::

        sage: from sage.combinat.shard_order import ShardPosetElement
        sage: p0 = Permutation([1,3,4,2])
        sage: e0 = ShardPosetElement(p0); e0
        (1, 3, 4, 2)
        sage: Permutation(list(e0)) == p0
        True
    """
    def __new__(cls, p):
        """
        Initialization of the underlying tuple.

        TESTS::

            sage: from sage.combinat.shard_order import ShardPosetElement
            sage: ShardPosetElement(Permutation([1,3,4,2]))
            (1, 3, 4, 2)
        """
    runs: Incomplete
    run_indices: Incomplete
    dpg: Incomplete
    spg: Incomplete
    def __init__(self, p) -> None:
        """
        INPUT:

        - ``p`` -- a permutation

        EXAMPLES::

            sage: from sage.combinat.shard_order import ShardPosetElement
            sage: p0 = Permutation([1,3,4,2])
            sage: e0 = ShardPosetElement(p0); e0
            (1, 3, 4, 2)
            sage: e0.dpg
            Transitive closure of : Digraph on 3 vertices
            sage: e0.spg
            Digraph on 3 vertices
        """
    def __le__(self, other):
        """
        Comparison between two elements of the poset.

        This is the core function in the implementation of the
        shard intersection order.

        One first compares the number of runs, then the set partitions,
        then the pre-orders.

        EXAMPLES::

            sage: from sage.combinat.shard_order import ShardPosetElement
            sage: p0 = Permutation([1,3,4,2])
            sage: p1 = Permutation([1,4,3,2])
            sage: e0 = ShardPosetElement(p0)
            sage: e1 = ShardPosetElement(p1)
            sage: e0 <= e1
            True
            sage: e1 <= e0
            False

            sage: p0 = Permutation([1,2,5,7,3,4,6,8])
            sage: p1 = Permutation([2,5,7,3,4,8,6,1])
            sage: e0 = ShardPosetElement(p0)
            sage: e1 = ShardPosetElement(p1)
            sage: e0 <= e1
            True
            sage: e1 <= e0
            False
        """

def shard_preorder_graph(runs):
    """
    Return the preorder attached to a tuple of decreasing runs.

    This is a directed graph, whose vertices correspond to the runs.

    There is an edge from a run `R` to a run `S` if `R` is before `S`
    in the list of runs and the two intervals defined by the initial and
    final indices of `R` and `S` overlap.

    This only depends on the initial and final indices of the runs.
    For this reason, this input can also be given in that shorten way.

    INPUT:

    - ``runs`` -- either

      - a tuple of tuples, the runs of a permutation, or

      - a tuple of pairs `(i,j)`, each one standing for a run from `i` to `j`

    OUTPUT: a directed graph, with vertices labelled by integers

    EXAMPLES::

        sage: from sage.combinat.shard_order import shard_preorder_graph
        sage: s = Permutation([2,8,3,9,6,4,5,1,7])
        sage: def cut(lr):
        ....:     return tuple((r[0], r[-1]) for r in lr)
        sage: shard_preorder_graph(cut(s.decreasing_runs()))
        Digraph on 5 vertices
        sage: s = Permutation([9,4,3,2,8,6,5,1,7])
        sage: P = shard_preorder_graph(s.decreasing_runs())
        sage: P.is_isomorphic(digraphs.TransitiveTournament(3))
        True
    """
def shard_poset(n):
    """
    Return the shard intersection order on permutations of size `n`.

    This is defined on the set of permutations. To every permutation,
    one can attach a pre-order, using the descending runs and their
    relative positions.

    The shard intersection order is given by the implication (or refinement)
    order on the set of pre-orders defined from all permutations.

    This can also be seen in a geometrical way. Every pre-order defines
    a cone in a vector space of dimension `n`. The shard poset is given by
    the inclusion of these cones.

    .. SEEALSO::

        :func:`~sage.combinat.shard_order.shard_preorder_graph`

    EXAMPLES::

        sage: P = posets.ShardPoset(4); P  # indirect doctest
        Finite poset containing 24 elements
        sage: P.chain_polynomial()
        34*q^4 + 90*q^3 + 79*q^2 + 24*q + 1
        sage: P.characteristic_polynomial()
        q^3 - 11*q^2 + 23*q - 13
        sage: P.zeta_polynomial()
        17/3*q^3 - 6*q^2 + 4/3*q
        sage: P.is_self_dual()
        False
    """
