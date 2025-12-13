import _cython_3_2_1
from typing import Any

__pyx_capi__: dict
test_popcount: _cython_3_2_1.cython_function_or_method

class FastDigraph:
    @classmethod
    def __init__(cls, *args, **kwargs) -> None:
        """Create and return a new object.  See help(type) for accurate signature."""
    def print_adjacency_matrix(self) -> Any:
        """FastDigraph.print_adjacency_matrix(self)

        File: /build/sagemath/src/sage/src/sage/graphs/graph_decompositions/fast_digraph.pyx (starting at line 91)

        Display the adjacency matrix of ``self``.

        EXAMPLES::

            sage: cython_code = [
            ....: 'from sage.graphs.graph import Graph',
            ....: 'from sage.graphs.graph_decompositions.fast_digraph cimport FastDigraph',
            ....: 'FastDigraph(Graph([(0, 1), (1, 2)])).print_adjacency_matrix()']
            sage: cython(os.linesep.join(cython_code))                                  # needs sage.misc.cython
            010
            101
            010"""
