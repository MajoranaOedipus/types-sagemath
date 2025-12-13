from typing import Any

class SubHypergraphSearch:
    @classmethod
    def __init__(cls, *args, **kwargs) -> None:
        """Create and return a new object.  See help(type) for accurate signature."""
    def relabel_heuristic(self) -> Any:
        """SubHypergraphSearch.relabel_heuristic(self)

        File: /build/sagemath/src/sage/src/sage/combinat/designs/subhypergraph_search.pyx (starting at line 427)

        Relabel `H_2` in order to make the algorithm faster.

        Objective: we try to pick an ordering `p_1,...,p_k` of the points of
        `H_2` that maximizes the number of sets involving the first points in
        the ordering. One way to formalize the problems indicates that it may be
        NP-Hard (generalizes the max clique problem for graphs) so we do not try
        to solve it exactly: we just need a sufficiently good heuristic.

        Assuming that the first points are `p_1,...,p_k`, we determine `p_{k+1}`
        as the point `x` such that the number of sets `S` with `x\\in S` and
        `S\\cap \\{p_1,...,p_k\\}\\neq \\emptyset` is maximal. In case of ties, we
        take a point with maximum degree.

        This function is called when an instance of :class:`SubHypergraphSearch`
        is created.

        EXAMPLES::

            sage: d = designs.projective_plane(3)                                       # needs sage.schemes
            sage: d.isomorphic_substructures_iterator(d).relabel_heuristic()            # needs sage.schemes"""
    def __iter__(self) -> Any:
        """SubHypergraphSearch.__iter__(self)

        File: /build/sagemath/src/sage/src/sage/combinat/designs/subhypergraph_search.pyx (starting at line 475)

        Iterate over all copies of h2 in h1.

        EXAMPLES:

        How many distinct `C_5` in Petersen's graph ? ::

            sage: P = graphs.PetersenGraph()
            sage: C = graphs.CycleGraph(5)
            sage: IP = IncidenceStructure(P.edges(sort=True, labels=False))
            sage: IC = IncidenceStructure(C.edges(sort=True, labels=False))
            sage: sum(1 for _ in IP.isomorphic_substructures_iterator(IC))
            120"""
