from sage.combinat.backtrack import GenericBacktracker as GenericBacktracker

class CrystalBacktracker(GenericBacktracker):
    def __init__(self, crystal, index_set=None) -> None:
        """
        Time complexity: `O(nF)` amortized for each produced
        element, where `n` is the size of the index set, and `F` is
        the cost of computing `e` and `f` operators.

        Memory complexity: `O(D)` where `D` is the depth of the crystal.

        Principle of the algorithm:

        Let `C` be a classical crystal. It's an acyclic graph where each
        connected component has a unique element without predecessors (the
        highest weight element for this component). Let's assume for
        simplicity that `C` is irreducible (i.e. connected) with highest
        weight element `u`.

        One can define a natural spanning tree of `C` by taking
        `u` as the root of the tree, and for any other element
        `y` taking as ancestor the element `x` such that
        there is an `i`-arrow from `x` to `y` with
        `i` minimal. Then, a path from `u` to `y`
        describes the lexicographically smallest sequence
        `i_1,\\dots,i_k` such that
        `(f_{i_k} \\circ f_{i_1})(u)=y`.

        Morally, the iterator implemented below just does a depth first
        search walk through this spanning tree. In practice, this can be
        achieved recursively as follows: take an element `x`, and
        consider in turn each successor `y = f_i(x)`, ignoring
        those such that `y = f_j(x^{\\prime})` for some `x^{\\prime}` and
        `j<i` (this can be tested by computing `e_j(y)`
        for `j<i`).

        EXAMPLES::

            sage: from sage.combinat.crystals.crystals import CrystalBacktracker
            sage: C = crystals.Tableaux(['B',3],shape=[3,2,1])
            sage: CB = CrystalBacktracker(C)
            sage: len(list(CB))
            1617
            sage: CB = CrystalBacktracker(C, [1,2])
            sage: len(list(CB))
            8
        """
