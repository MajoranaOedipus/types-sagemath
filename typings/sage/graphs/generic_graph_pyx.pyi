import _cython_3_2_1
import sage.structure.sage_object
from sage.cpython.string import bytes_to_str as bytes_to_str, str_to_bytes as str_to_bytes
from sage.misc.prandom import random as random
from typing import Any, overload

__pyx_capi__: dict
binary_string_from_dig6: _cython_3_2_1.cython_function_or_method
binary_string_from_graph6: _cython_3_2_1.cython_function_or_method
binary_string_to_graph6: _cython_3_2_1.cython_function_or_method
find_hamiltonian: _cython_3_2_1.cython_function_or_method
int_to_binary_string: _cython_3_2_1.cython_function_or_method
layout_split: _cython_3_2_1.cython_function_or_method
length_and_string_from_graph6: _cython_3_2_1.cython_function_or_method
small_integer_to_graph6: _cython_3_2_1.cython_function_or_method
spring_layout_fast: _cython_3_2_1.cython_function_or_method
transitive_reduction_acyclic: _cython_3_2_1.cython_function_or_method

class GenericGraph_pyx(sage.structure.sage_object.SageObject):
    @classmethod
    def __init__(cls, *args, **kwargs) -> None:
        """Create and return a new object.  See help(type) for accurate signature."""

class SubgraphSearch:
    """SubgraphSearch(G, H, induced=False)

    File: /build/sagemath/src/sage/src/sage/graphs/generic_graph_pyx.pyx (starting at line 615)

    This class implements methods to exhaustively search for
    copies of a graph `H` in a larger graph `G`.

    It is possible to look for induced subgraphs instead, and to
    iterate or count the number of their occurrences.

    ALGORITHM:

    The algorithm is a brute-force search.  Let `V(H) =
    \\{h_1,\\dots,h_k\\}`.  It first tries to find in `G` a possible
    representative of `h_1`, then a representative of `h_2` compatible
    with `h_1`, then a representative of `h_3` compatible with the first
    two, etc.

    This way, most of the time we need to test far less than `k!
    \\binom{|V(G)|}{k}` subsets, and hope this brute-force technique
    can sometimes be useful.

    .. NOTE::

        This algorithm does not take vertex/edge labels into account."""
    def __init__(self, G, H, induced=...) -> Any:
        """File: /build/sagemath/src/sage/src/sage/graphs/generic_graph_pyx.pyx (starting at line 639)

                Constructor.

                This constructor only checks there is no inconsistency in the
                input : `G` and `H` are both graphs or both digraphs and that `H`
                has order at least 2.

                EXAMPLES::

                    sage: g = graphs.PetersenGraph()
                    sage: g.subgraph_search(graphs.CycleGraph(5))                               # needs sage.modules
                    Subgraph of (Petersen graph): Graph on 5 vertices

                TESTS:

                Test proper initialization and deallocation, see :issue:`14067`.
                We intentionally only create the class without doing any
                computations with it::

                    sage: from sage.graphs.generic_graph_pyx import SubgraphSearch
                    sage: SubgraphSearch(Graph(5), Graph(1))                                    # needs sage.modules
                    Traceback (most recent call last):
                    ...
                    ValueError: searched graph should have at least 2 vertices
                    sage: SubgraphSearch(Graph(5), Graph(2))                                    # needs sage.modules
                    <sage.graphs.generic_graph_pyx.SubgraphSearch ...>
        """
    @overload
    def cardinality(self) -> Any:
        '''SubgraphSearch.cardinality(self)

        File: /build/sagemath/src/sage/src/sage/graphs/generic_graph_pyx.pyx (starting at line 703)

        Return the number of labelled subgraphs of `G` isomorphic to
        `H`.

        .. NOTE::

           This method counts the subgraphs by enumerating them all !
           Hence it probably is not a good idea to count their number
           before enumerating them :-)

        EXAMPLES:

        Counting the number of labelled `P_3` in `P_5`::

            sage: from sage.graphs.generic_graph_pyx import SubgraphSearch
            sage: g = graphs.PathGraph(5)
            sage: h = graphs.PathGraph(3)
            sage: S = SubgraphSearch(g, h)                                              # needs sage.modules
            sage: S.cardinality()                                                       # needs sage.modules
            6

        Check that the method is working even when vertices or edges are of
        incomparable types (see :issue:`35904`)::

            sage: from sage.graphs.generic_graph_pyx import SubgraphSearch
            sage: G = Graph()
            sage: G.add_cycle([\'A\', 1, 2, 3, (\'a\', 1)])
            sage: H = Graph()
            sage: H.add_path("xyz")
            sage: S = SubgraphSearch(G, H)                                              # needs sage.modules
            sage: S.cardinality()                                                       # needs sage.modules
            10'''
    @overload
    def cardinality(self) -> Any:
        '''SubgraphSearch.cardinality(self)

        File: /build/sagemath/src/sage/src/sage/graphs/generic_graph_pyx.pyx (starting at line 703)

        Return the number of labelled subgraphs of `G` isomorphic to
        `H`.

        .. NOTE::

           This method counts the subgraphs by enumerating them all !
           Hence it probably is not a good idea to count their number
           before enumerating them :-)

        EXAMPLES:

        Counting the number of labelled `P_3` in `P_5`::

            sage: from sage.graphs.generic_graph_pyx import SubgraphSearch
            sage: g = graphs.PathGraph(5)
            sage: h = graphs.PathGraph(3)
            sage: S = SubgraphSearch(g, h)                                              # needs sage.modules
            sage: S.cardinality()                                                       # needs sage.modules
            6

        Check that the method is working even when vertices or edges are of
        incomparable types (see :issue:`35904`)::

            sage: from sage.graphs.generic_graph_pyx import SubgraphSearch
            sage: G = Graph()
            sage: G.add_cycle([\'A\', 1, 2, 3, (\'a\', 1)])
            sage: H = Graph()
            sage: H.add_path("xyz")
            sage: S = SubgraphSearch(G, H)                                              # needs sage.modules
            sage: S.cardinality()                                                       # needs sage.modules
            10'''
    @overload
    def cardinality(self) -> Any:
        '''SubgraphSearch.cardinality(self)

        File: /build/sagemath/src/sage/src/sage/graphs/generic_graph_pyx.pyx (starting at line 703)

        Return the number of labelled subgraphs of `G` isomorphic to
        `H`.

        .. NOTE::

           This method counts the subgraphs by enumerating them all !
           Hence it probably is not a good idea to count their number
           before enumerating them :-)

        EXAMPLES:

        Counting the number of labelled `P_3` in `P_5`::

            sage: from sage.graphs.generic_graph_pyx import SubgraphSearch
            sage: g = graphs.PathGraph(5)
            sage: h = graphs.PathGraph(3)
            sage: S = SubgraphSearch(g, h)                                              # needs sage.modules
            sage: S.cardinality()                                                       # needs sage.modules
            6

        Check that the method is working even when vertices or edges are of
        incomparable types (see :issue:`35904`)::

            sage: from sage.graphs.generic_graph_pyx import SubgraphSearch
            sage: G = Graph()
            sage: G.add_cycle([\'A\', 1, 2, 3, (\'a\', 1)])
            sage: H = Graph()
            sage: H.add_path("xyz")
            sage: S = SubgraphSearch(G, H)                                              # needs sage.modules
            sage: S.cardinality()                                                       # needs sage.modules
            10'''
    def __iter__(self) -> Any:
        """SubgraphSearch.__iter__(self)

        File: /build/sagemath/src/sage/src/sage/graphs/generic_graph_pyx.pyx (starting at line 678)

        Return an iterator over all the labeled subgraphs of `G`
        isomorphic to `H`.

        EXAMPLES:

        Iterating through all the `P_3` of `P_5`::

            sage: from sage.graphs.generic_graph_pyx import SubgraphSearch
            sage: g = graphs.PathGraph(5)
            sage: h = graphs.PathGraph(3)
            sage: S = SubgraphSearch(g, h)                                              # needs sage.modules
            sage: for p in S:                                                           # needs sage.modules
            ....:     print(p)
            [0, 1, 2]
            [1, 2, 3]
            [2, 1, 0]
            [2, 3, 4]
            [3, 2, 1]
            [4, 3, 2]"""
    @overload
    def __next__(self) -> Any:
        """SubgraphSearch.__next__(self)

        File: /build/sagemath/src/sage/src/sage/graphs/generic_graph_pyx.pyx (starting at line 893)

        Return the next isomorphic subgraph if any, and raises a
        ``StopIteration`` otherwise.

        EXAMPLES::

            sage: from sage.graphs.generic_graph_pyx import SubgraphSearch
            sage: g = graphs.PathGraph(5)
            sage: h = graphs.PathGraph(3)
            sage: S = SubgraphSearch(g, h)                                              # needs sage.modules
            sage: S.__next__()                                                          # needs sage.modules
            [0, 1, 2]"""
    @overload
    def __next__(self) -> Any:
        """SubgraphSearch.__next__(self)

        File: /build/sagemath/src/sage/src/sage/graphs/generic_graph_pyx.pyx (starting at line 893)

        Return the next isomorphic subgraph if any, and raises a
        ``StopIteration`` otherwise.

        EXAMPLES::

            sage: from sage.graphs.generic_graph_pyx import SubgraphSearch
            sage: g = graphs.PathGraph(5)
            sage: h = graphs.PathGraph(3)
            sage: S = SubgraphSearch(g, h)                                              # needs sage.modules
            sage: S.__next__()                                                          # needs sage.modules
            [0, 1, 2]"""
