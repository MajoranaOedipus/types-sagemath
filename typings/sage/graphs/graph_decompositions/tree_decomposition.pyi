import _cython_3_2_1
from sage.cpython.string import bytes_to_str as bytes_to_str, str_to_bytes as str_to_bytes
from sage.misc.cachefunc import cached_function as cached_function
from sage.rings.infinity import Infinity as Infinity
from sage.sets.disjoint_set import DisjointSet as DisjointSet
from sage.sets.set import Set as Set
from typing import Any, ClassVar, overload

is_valid_tree_decomposition: _cython_3_2_1.cython_function_or_method
label_nice_tree_decomposition: _cython_3_2_1.cython_function_or_method
length_of_tree_decomposition: _cython_3_2_1.cython_function_or_method
make_nice_tree_decomposition: _cython_3_2_1.cython_function_or_method
reduced_tree_decomposition: _cython_3_2_1.cython_function_or_method
treelength: _cython_3_2_1.cython_function_or_method
treelength_lowerbound: _cython_3_2_1.cython_function_or_method
treewidth: _cython_3_2_1.cython_function_or_method
width_of_tree_decomposition: _cython_3_2_1.cython_function_or_method

class TreelengthConnected:
    """TreelengthConnected(G, k=None, certificate=False)

    File: /build/sagemath/src/sage/src/sage/graphs/graph_decompositions/tree_decomposition.pyx (starting at line 1292)

    Compute the treelength of a connected graph (and provide a decomposition).

    This class implements an algorithm for computing the treelength of a
    connected graph that virtually explores the graph of all pairs
    ``(vertex_cut, connected_component)``, where ``vertex_cut`` is a vertex cut
    of the graph of length `\\leq k`, and ``connected_component`` is a connected
    component of the graph induced by ``G - vertex_cut``.

    We deduce that the pair ``(vertex_cut, connected_component)`` is feasible
    with treelength `k` if ``connected_component`` is empty, or if a vertex
    ``v`` from ``vertex_cut`` can be replaced with a vertex from
    ``connected_component``, such that the pair ``(vertex_cut + v,
    connected_component - v)`` is feasible.

    INPUT:

    - ``G`` -- a sage Graph

    - ``k`` -- integer (default: ``None``); indicates the length to be
      considered. When `k` is an integer, the method checks that the graph has
      treelength `\\leq k`. If `k` is ``None`` (default), the method computes the
      optimal treelength.

    - ``certificate`` -- boolean (default: ``False``); whether to also compute
      the tree-decomposition itself

    OUTPUT:

    ``TreelengthConnected(G)`` returns the treelength of `G`. When `k` is
    specified, it returns ``False`` when no tree-decomposition of length
    `\\leq k` exists or ``True`` otherwise. When ``certificate=True``, the
    tree-decomposition is also returned.

    EXAMPLES:

    A clique has treelength 1::

        sage: from sage.graphs.graph_decompositions.tree_decomposition import TreelengthConnected
        sage: TreelengthConnected(graphs.CompleteGraph(3)).get_length()
        1
        sage: TC = TreelengthConnected(graphs.CompleteGraph(4), certificate=True)
        sage: TC.get_length()
        1
        sage: TC.get_tree_decomposition()
        Tree decomposition of Complete graph: Graph on 1 vertex

    A cycle has treelength `\\lceil n/3 \\rceil`::

        sage: TreelengthConnected(graphs.CycleGraph(6)).get_length()
        2
        sage: TreelengthConnected(graphs.CycleGraph(7)).get_length()
        3
        sage: TreelengthConnected(graphs.CycleGraph(7), k=3).is_less_than_k()
        True
        sage: TreelengthConnected(graphs.CycleGraph(7), k=2).is_less_than_k()
        False

    TESTS:

    The input graph must be connected::

        sage: TreelengthConnected(Graph(2))
        Traceback (most recent call last):
        ...
        ValueError: the graph is not connected

    The parameter `k` must be nonnegative::

        sage: TreelengthConnected(Graph(1), k=-1)
        Traceback (most recent call last):
        ...
        ValueError: k (= -1) must be a nonnegative integer

    Parameter ``certificate`` must be ``True`` to get a tree decomposition::

        sage: TreelengthConnected(Graph(1), certificate=False).get_tree_decomposition()
        Traceback (most recent call last):
        ...
        ValueError: parameter 'certificate' has not been set to True

    When parameter `k` is specified and ``certificate`` is ``True``, the
    computed tree decomposition is any valid tree decomposition with length at
    most `k`. However, this tree decomposition exists only if the treelength of
    `G` is at most `k` (i.e., `tl(G) \\leq k`)::

        sage: G = graphs.Grid2dGraph(2, 3)
        sage: TC = TreelengthConnected(G, k=2, certificate=True)
        sage: TC.is_less_than_k()
        True
        sage: TC.get_tree_decomposition()
        Tree decomposition of 2D Grid Graph for [2, 3]: Graph on 3 vertices
        sage: TC = TreelengthConnected(G, k=1, certificate=True)
        sage: TC.is_less_than_k()
        False
        sage: TC.get_tree_decomposition()
        Traceback (most recent call last):
        ...
        ValueError: no tree decomposition with length <= 1 was found"""
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    def __init__(self, G, k=..., certificate=...) -> Any:
        """File: /build/sagemath/src/sage/src/sage/graphs/graph_decompositions/tree_decomposition.pyx (starting at line 1394)

                Initialize this object and compute the treelength of `G`.

                INPUT:

                - ``G`` -- a sage Graph

                - ``k`` -- integer (default: ``None``); indicates the length to be
                  considered. When `k` is an integer, the method checks that the graph
                  has treelength `\\leq k`. If `k` is ``None`` (default), the method
                  computes the optimal treelength.

                - ``certificate`` -- boolean (default: ``False``); whether to compute
                  the tree-decomposition itself

                TESTS::

                    sage: from sage.graphs.graph_decompositions.tree_decomposition import TreelengthConnected
                    sage: G = graphs.CycleGraph(4)
                    sage: TreelengthConnected(G).get_length()
                    2
        """
    @overload
    def get_length(self) -> Any:
        """TreelengthConnected.get_length(self)

        File: /build/sagemath/src/sage/src/sage/graphs/graph_decompositions/tree_decomposition.pyx (starting at line 1688)

        Return the length of the tree decomposition.

        EXAMPLES::

            sage: from sage.graphs.graph_decompositions.tree_decomposition import TreelengthConnected
            sage: G = graphs.CycleGraph(4)
            sage: TreelengthConnected(G).get_length()
            2
            sage: TreelengthConnected(G, k=2).get_length()
            2
            sage: TreelengthConnected(G, k=1).get_length()
            Traceback (most recent call last):
            ...
            ValueError: no tree decomposition with length <= 1 was found

        TESTS::

            sage: TreelengthConnected(Graph()).get_length()
            0"""
    @overload
    def get_length(self) -> Any:
        """TreelengthConnected.get_length(self)

        File: /build/sagemath/src/sage/src/sage/graphs/graph_decompositions/tree_decomposition.pyx (starting at line 1688)

        Return the length of the tree decomposition.

        EXAMPLES::

            sage: from sage.graphs.graph_decompositions.tree_decomposition import TreelengthConnected
            sage: G = graphs.CycleGraph(4)
            sage: TreelengthConnected(G).get_length()
            2
            sage: TreelengthConnected(G, k=2).get_length()
            2
            sage: TreelengthConnected(G, k=1).get_length()
            Traceback (most recent call last):
            ...
            ValueError: no tree decomposition with length <= 1 was found

        TESTS::

            sage: TreelengthConnected(Graph()).get_length()
            0"""
    @overload
    def get_length(self) -> Any:
        """TreelengthConnected.get_length(self)

        File: /build/sagemath/src/sage/src/sage/graphs/graph_decompositions/tree_decomposition.pyx (starting at line 1688)

        Return the length of the tree decomposition.

        EXAMPLES::

            sage: from sage.graphs.graph_decompositions.tree_decomposition import TreelengthConnected
            sage: G = graphs.CycleGraph(4)
            sage: TreelengthConnected(G).get_length()
            2
            sage: TreelengthConnected(G, k=2).get_length()
            2
            sage: TreelengthConnected(G, k=1).get_length()
            Traceback (most recent call last):
            ...
            ValueError: no tree decomposition with length <= 1 was found

        TESTS::

            sage: TreelengthConnected(Graph()).get_length()
            0"""
    @overload
    def get_length(self) -> Any:
        """TreelengthConnected.get_length(self)

        File: /build/sagemath/src/sage/src/sage/graphs/graph_decompositions/tree_decomposition.pyx (starting at line 1688)

        Return the length of the tree decomposition.

        EXAMPLES::

            sage: from sage.graphs.graph_decompositions.tree_decomposition import TreelengthConnected
            sage: G = graphs.CycleGraph(4)
            sage: TreelengthConnected(G).get_length()
            2
            sage: TreelengthConnected(G, k=2).get_length()
            2
            sage: TreelengthConnected(G, k=1).get_length()
            Traceback (most recent call last):
            ...
            ValueError: no tree decomposition with length <= 1 was found

        TESTS::

            sage: TreelengthConnected(Graph()).get_length()
            0"""
    @overload
    def get_length(self) -> Any:
        """TreelengthConnected.get_length(self)

        File: /build/sagemath/src/sage/src/sage/graphs/graph_decompositions/tree_decomposition.pyx (starting at line 1688)

        Return the length of the tree decomposition.

        EXAMPLES::

            sage: from sage.graphs.graph_decompositions.tree_decomposition import TreelengthConnected
            sage: G = graphs.CycleGraph(4)
            sage: TreelengthConnected(G).get_length()
            2
            sage: TreelengthConnected(G, k=2).get_length()
            2
            sage: TreelengthConnected(G, k=1).get_length()
            Traceback (most recent call last):
            ...
            ValueError: no tree decomposition with length <= 1 was found

        TESTS::

            sage: TreelengthConnected(Graph()).get_length()
            0"""
    @overload
    def get_tree_decomposition(self) -> Any:
        """TreelengthConnected.get_tree_decomposition(self)

        File: /build/sagemath/src/sage/src/sage/graphs/graph_decompositions/tree_decomposition.pyx (starting at line 1654)

        Return the tree-decomposition.

        EXAMPLES::

            sage: from sage.graphs.graph_decompositions.tree_decomposition import TreelengthConnected
            sage: G = graphs.CycleGraph(4)
            sage: TreelengthConnected(G, certificate=True).get_tree_decomposition()
            Tree decomposition of Cycle graph: Graph on 2 vertices
            sage: G.diameter()
            2
            sage: TreelengthConnected(G, k=2, certificate=True).get_tree_decomposition()
            Tree decomposition of Cycle graph: Graph on 1 vertex
            sage: TreelengthConnected(G, k=1, certificate=True).get_tree_decomposition()
            Traceback (most recent call last):
            ...
            ValueError: no tree decomposition with length <= 1 was found

        TESTS::

            sage: G = graphs.CycleGraph(4)
            sage: TreelengthConnected(G, certificate=False).get_tree_decomposition()
            Traceback (most recent call last):
            ...
            ValueError: parameter 'certificate' has not been set to True"""
    @overload
    def get_tree_decomposition(self) -> Any:
        """TreelengthConnected.get_tree_decomposition(self)

        File: /build/sagemath/src/sage/src/sage/graphs/graph_decompositions/tree_decomposition.pyx (starting at line 1654)

        Return the tree-decomposition.

        EXAMPLES::

            sage: from sage.graphs.graph_decompositions.tree_decomposition import TreelengthConnected
            sage: G = graphs.CycleGraph(4)
            sage: TreelengthConnected(G, certificate=True).get_tree_decomposition()
            Tree decomposition of Cycle graph: Graph on 2 vertices
            sage: G.diameter()
            2
            sage: TreelengthConnected(G, k=2, certificate=True).get_tree_decomposition()
            Tree decomposition of Cycle graph: Graph on 1 vertex
            sage: TreelengthConnected(G, k=1, certificate=True).get_tree_decomposition()
            Traceback (most recent call last):
            ...
            ValueError: no tree decomposition with length <= 1 was found

        TESTS::

            sage: G = graphs.CycleGraph(4)
            sage: TreelengthConnected(G, certificate=False).get_tree_decomposition()
            Traceback (most recent call last):
            ...
            ValueError: parameter 'certificate' has not been set to True"""
    @overload
    def get_tree_decomposition(self) -> Any:
        """TreelengthConnected.get_tree_decomposition(self)

        File: /build/sagemath/src/sage/src/sage/graphs/graph_decompositions/tree_decomposition.pyx (starting at line 1654)

        Return the tree-decomposition.

        EXAMPLES::

            sage: from sage.graphs.graph_decompositions.tree_decomposition import TreelengthConnected
            sage: G = graphs.CycleGraph(4)
            sage: TreelengthConnected(G, certificate=True).get_tree_decomposition()
            Tree decomposition of Cycle graph: Graph on 2 vertices
            sage: G.diameter()
            2
            sage: TreelengthConnected(G, k=2, certificate=True).get_tree_decomposition()
            Tree decomposition of Cycle graph: Graph on 1 vertex
            sage: TreelengthConnected(G, k=1, certificate=True).get_tree_decomposition()
            Traceback (most recent call last):
            ...
            ValueError: no tree decomposition with length <= 1 was found

        TESTS::

            sage: G = graphs.CycleGraph(4)
            sage: TreelengthConnected(G, certificate=False).get_tree_decomposition()
            Traceback (most recent call last):
            ...
            ValueError: parameter 'certificate' has not been set to True"""
    @overload
    def get_tree_decomposition(self) -> Any:
        """TreelengthConnected.get_tree_decomposition(self)

        File: /build/sagemath/src/sage/src/sage/graphs/graph_decompositions/tree_decomposition.pyx (starting at line 1654)

        Return the tree-decomposition.

        EXAMPLES::

            sage: from sage.graphs.graph_decompositions.tree_decomposition import TreelengthConnected
            sage: G = graphs.CycleGraph(4)
            sage: TreelengthConnected(G, certificate=True).get_tree_decomposition()
            Tree decomposition of Cycle graph: Graph on 2 vertices
            sage: G.diameter()
            2
            sage: TreelengthConnected(G, k=2, certificate=True).get_tree_decomposition()
            Tree decomposition of Cycle graph: Graph on 1 vertex
            sage: TreelengthConnected(G, k=1, certificate=True).get_tree_decomposition()
            Traceback (most recent call last):
            ...
            ValueError: no tree decomposition with length <= 1 was found

        TESTS::

            sage: G = graphs.CycleGraph(4)
            sage: TreelengthConnected(G, certificate=False).get_tree_decomposition()
            Traceback (most recent call last):
            ...
            ValueError: parameter 'certificate' has not been set to True"""
    @overload
    def get_tree_decomposition(self) -> Any:
        """TreelengthConnected.get_tree_decomposition(self)

        File: /build/sagemath/src/sage/src/sage/graphs/graph_decompositions/tree_decomposition.pyx (starting at line 1654)

        Return the tree-decomposition.

        EXAMPLES::

            sage: from sage.graphs.graph_decompositions.tree_decomposition import TreelengthConnected
            sage: G = graphs.CycleGraph(4)
            sage: TreelengthConnected(G, certificate=True).get_tree_decomposition()
            Tree decomposition of Cycle graph: Graph on 2 vertices
            sage: G.diameter()
            2
            sage: TreelengthConnected(G, k=2, certificate=True).get_tree_decomposition()
            Tree decomposition of Cycle graph: Graph on 1 vertex
            sage: TreelengthConnected(G, k=1, certificate=True).get_tree_decomposition()
            Traceback (most recent call last):
            ...
            ValueError: no tree decomposition with length <= 1 was found

        TESTS::

            sage: G = graphs.CycleGraph(4)
            sage: TreelengthConnected(G, certificate=False).get_tree_decomposition()
            Traceback (most recent call last):
            ...
            ValueError: parameter 'certificate' has not been set to True"""
    @overload
    def is_less_than_k(self) -> Any:
        """TreelengthConnected.is_less_than_k(self)

        File: /build/sagemath/src/sage/src/sage/graphs/graph_decompositions/tree_decomposition.pyx (starting at line 1714)

        Return whether a tree decomposition with length at most `k` was found.

        EXAMPLES::

            sage: from sage.graphs.graph_decompositions.tree_decomposition import TreelengthConnected
            sage: G = graphs.CycleGraph(4)
            sage: TreelengthConnected(G, k=1).is_less_than_k()
            False
            sage: TreelengthConnected(G, k=2).is_less_than_k()
            True
            sage: TreelengthConnected(G).is_less_than_k()
            Traceback (most recent call last):
            ...
            ValueError: parameter 'k' has not been specified

        TESTS::

            sage: TreelengthConnected(Graph(), k=1).is_less_than_k()
            True"""
    @overload
    def is_less_than_k(self) -> Any:
        """TreelengthConnected.is_less_than_k(self)

        File: /build/sagemath/src/sage/src/sage/graphs/graph_decompositions/tree_decomposition.pyx (starting at line 1714)

        Return whether a tree decomposition with length at most `k` was found.

        EXAMPLES::

            sage: from sage.graphs.graph_decompositions.tree_decomposition import TreelengthConnected
            sage: G = graphs.CycleGraph(4)
            sage: TreelengthConnected(G, k=1).is_less_than_k()
            False
            sage: TreelengthConnected(G, k=2).is_less_than_k()
            True
            sage: TreelengthConnected(G).is_less_than_k()
            Traceback (most recent call last):
            ...
            ValueError: parameter 'k' has not been specified

        TESTS::

            sage: TreelengthConnected(Graph(), k=1).is_less_than_k()
            True"""
    @overload
    def is_less_than_k(self) -> Any:
        """TreelengthConnected.is_less_than_k(self)

        File: /build/sagemath/src/sage/src/sage/graphs/graph_decompositions/tree_decomposition.pyx (starting at line 1714)

        Return whether a tree decomposition with length at most `k` was found.

        EXAMPLES::

            sage: from sage.graphs.graph_decompositions.tree_decomposition import TreelengthConnected
            sage: G = graphs.CycleGraph(4)
            sage: TreelengthConnected(G, k=1).is_less_than_k()
            False
            sage: TreelengthConnected(G, k=2).is_less_than_k()
            True
            sage: TreelengthConnected(G).is_less_than_k()
            Traceback (most recent call last):
            ...
            ValueError: parameter 'k' has not been specified

        TESTS::

            sage: TreelengthConnected(Graph(), k=1).is_less_than_k()
            True"""
    @overload
    def is_less_than_k(self) -> Any:
        """TreelengthConnected.is_less_than_k(self)

        File: /build/sagemath/src/sage/src/sage/graphs/graph_decompositions/tree_decomposition.pyx (starting at line 1714)

        Return whether a tree decomposition with length at most `k` was found.

        EXAMPLES::

            sage: from sage.graphs.graph_decompositions.tree_decomposition import TreelengthConnected
            sage: G = graphs.CycleGraph(4)
            sage: TreelengthConnected(G, k=1).is_less_than_k()
            False
            sage: TreelengthConnected(G, k=2).is_less_than_k()
            True
            sage: TreelengthConnected(G).is_less_than_k()
            Traceback (most recent call last):
            ...
            ValueError: parameter 'k' has not been specified

        TESTS::

            sage: TreelengthConnected(Graph(), k=1).is_less_than_k()
            True"""
    @overload
    def is_less_than_k(self) -> Any:
        """TreelengthConnected.is_less_than_k(self)

        File: /build/sagemath/src/sage/src/sage/graphs/graph_decompositions/tree_decomposition.pyx (starting at line 1714)

        Return whether a tree decomposition with length at most `k` was found.

        EXAMPLES::

            sage: from sage.graphs.graph_decompositions.tree_decomposition import TreelengthConnected
            sage: G = graphs.CycleGraph(4)
            sage: TreelengthConnected(G, k=1).is_less_than_k()
            False
            sage: TreelengthConnected(G, k=2).is_less_than_k()
            True
            sage: TreelengthConnected(G).is_less_than_k()
            Traceback (most recent call last):
            ...
            ValueError: parameter 'k' has not been specified

        TESTS::

            sage: TreelengthConnected(Graph(), k=1).is_less_than_k()
            True"""
