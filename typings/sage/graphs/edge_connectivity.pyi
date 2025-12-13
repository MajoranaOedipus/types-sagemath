from sage.cpython.string import bytes_to_str as bytes_to_str, str_to_bytes as str_to_bytes
from typing import Any, ClassVar, overload

class GabowEdgeConnectivity:
    """GabowEdgeConnectivity(G, dfs_preprocessing=True, use_rec=False)

    File: /build/sagemath/src/sage/src/sage/graphs/edge_connectivity.pyx (starting at line 36)

    Gabow's algorithm for finding the edge connectivity of digraphs.

    This class implements the algorithm proposed in [Gabow1995]_ for finding the
    edge connectivity of a directed graph and `k` edge disjoint spanning trees
    if the digraph is `k` edge connected.

    .. WARNING::

        Multiple edges are currently not supported. The current implementation
        act as if the digraph is simple and so the return results might not be
        correct. We therefore raise an error if the digraph has multiple edges.

    INPUT:

    - ``D`` -- a :class:`~sage.graphs.digraph.DiGraph`

    EXAMPLES:

    A random `d`-regular digraph is `d`-edge-connected::

        sage: from sage.graphs.edge_connectivity import GabowEdgeConnectivity
        sage: D = DiGraph(graphs.RandomRegular(6, 50))                                  # needs networkx
        sage: while not D.is_strongly_connected():                                      # needs networkx
        ....:     D = DiGraph(graphs.RandomRegular(6, 50))
        sage: GabowEdgeConnectivity(D).edge_connectivity()                              # needs networkx
        6

    A complete digraph with `n` vertices is `n-1`-edge-connected::

        sage: from sage.graphs.edge_connectivity import GabowEdgeConnectivity
        sage: D = DiGraph(digraphs.Complete(10))
        sage: GabowEdgeConnectivity(D, use_rec=True).edge_connectivity()
        9

    Check that we get the same result when with and without the DFS-based
    speed-up initialization proposed in [GKLP2021]_::

        sage: # needs networkx
        sage: G = graphs.RandomBarabasiAlbert(100, 2)
        sage: D = DiGraph(G)
        sage: ec1 = GabowEdgeConnectivity(D,
        ....:                             dfs_preprocessing=False).edge_connectivity()
        sage: ec2 = GabowEdgeConnectivity(D,
        ....:                             dfs_preprocessing=True).edge_connectivity()
        sage: ec3 = GabowEdgeConnectivity(D, dfs_preprocessing=True,
        ....:                             use_rec=True).edge_connectivity()
        sage: ec1 == ec2 and ec2 == ec3
        True

    TESTS:

    :issue:`32169`::

        sage: dig6_string = r'[E_S?_hKIH@eos[BSg???Q@FShGC?hTHUGM?IPug?'
        sage: dig6_string += r'JOEYCdOzdkQGo@ADA@AAg?GAQW?'
        sage: dig6_string += r'[aIaSwHYcD@qQb@Dd?\\hJTI@OHlJ_?C_OEIKoeCR@_BC?Q?'
        sage: dig6_string += r'?YBFosqITEA?IvCU_'
        sage: D = DiGraph(dig6_string)
        sage: GabowEdgeConnectivity(D).edge_connectivity()
        5
        sage: GabowEdgeConnectivity(D).edge_disjoint_spanning_trees()
        Traceback (most recent call last):
        ...
        NotImplementedError: this method has not been implemented yet

    Corner cases::

        sage: [GabowEdgeConnectivity(DiGraph(n)).edge_connectivity() for n in range(4)]
        [0, 0, 0, 0]
        sage: D = digraphs.Circuit(3) * 2
        sage: D.add_edge(0, 3)
        sage: GabowEdgeConnectivity(D).edge_connectivity()
        0
        sage: D.add_edge(3, 0)
        sage: GabowEdgeConnectivity(D).edge_connectivity()
        1

    Looped digraphs are supported but not digraphs with multiple edges::

        sage: D = digraphs.Complete(5, loops=True)
        sage: GabowEdgeConnectivity(D).edge_connectivity()
        4
        sage: D.allow_multiple_edges(True)
        sage: D.add_edges(D.edges(sort=False))
        sage: GabowEdgeConnectivity(D).edge_connectivity()
        Traceback (most recent call last):
        ...
        ValueError: This method is not known to work on graphs with multiedges. ..."""
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    G: File
    def __init__(self, G, dfs_preprocessing=..., use_rec=...) -> Any:
        """File: /build/sagemath/src/sage/src/sage/graphs/edge_connectivity.pyx (starting at line 202)

                Initialize this object.

                INPUT:

                - ``G`` -- a :class:`~sage.graphs.digraph.DiGraph`

                - ``dfs_preprocessing`` -- boolean (default: ``True``); whether to use
                  the DFS-based speed-up initialization proposed in [GKLP2021]_

                - ``use_rec`` -- boolean (default: ``False``); whether to use a
                  recursive or non-recursive DFS for ``dfs_preprocessing``. The
                  recursive DFS tends to be faster than the non-recursive version on
                  complete digraphs and slower on other graphs. This parameter is
                  ignored when ``dfs_preprocessing`` is ``False``.

                EXAMPLES::

                    sage: from sage.graphs.edge_connectivity import GabowEdgeConnectivity
                    sage: D = digraphs.Complete(5)
                    sage: GabowEdgeConnectivity(D).edge_connectivity()
                    4
        """
    @overload
    def edge_connectivity(self) -> Any:
        """GabowEdgeConnectivity.edge_connectivity(self)

        File: /build/sagemath/src/sage/src/sage/graphs/edge_connectivity.pyx (starting at line 1181)

        Return the edge connectivity of the digraph.

        EXAMPLES::

            sage: from sage.graphs.edge_connectivity import GabowEdgeConnectivity
            sage: D = digraphs.Complete(5)
            sage: GabowEdgeConnectivity(D).edge_connectivity()
            4"""
    @overload
    def edge_connectivity(self) -> Any:
        """GabowEdgeConnectivity.edge_connectivity(self)

        File: /build/sagemath/src/sage/src/sage/graphs/edge_connectivity.pyx (starting at line 1181)

        Return the edge connectivity of the digraph.

        EXAMPLES::

            sage: from sage.graphs.edge_connectivity import GabowEdgeConnectivity
            sage: D = digraphs.Complete(5)
            sage: GabowEdgeConnectivity(D).edge_connectivity()
            4"""
    @overload
    def edge_disjoint_spanning_trees(self) -> Any:
        """GabowEdgeConnectivity.edge_disjoint_spanning_trees(self)

        File: /build/sagemath/src/sage/src/sage/graphs/edge_connectivity.pyx (starting at line 1201)

        Iterator over the edge disjoint spanning trees.

        EXAMPLES::

            sage: from sage.graphs.edge_connectivity import GabowEdgeConnectivity
            sage: D = digraphs.Complete(5)
            sage: GabowEdgeConnectivity(D).edge_disjoint_spanning_trees()
            Traceback (most recent call last):
            ...
            NotImplementedError: this method has not been implemented yet"""
    @overload
    def edge_disjoint_spanning_trees(self) -> Any:
        """GabowEdgeConnectivity.edge_disjoint_spanning_trees(self)

        File: /build/sagemath/src/sage/src/sage/graphs/edge_connectivity.pyx (starting at line 1201)

        Iterator over the edge disjoint spanning trees.

        EXAMPLES::

            sage: from sage.graphs.edge_connectivity import GabowEdgeConnectivity
            sage: D = digraphs.Complete(5)
            sage: GabowEdgeConnectivity(D).edge_disjoint_spanning_trees()
            Traceback (most recent call last):
            ...
            NotImplementedError: this method has not been implemented yet"""
