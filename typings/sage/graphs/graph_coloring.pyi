import _cython_3_2_1
from sage.combinat.matrices.dlxcpp import DLXCPP as DLXCPP
from sage.graphs.independent_sets import IndependentSets as IndependentSets
from sage.misc.lazy_import import LazyImport as LazyImport
from sage.numerical.mip import MixedIntegerLinearProgram as MixedIntegerLinearProgram
from typing import Any

acyclic_edge_coloring: _cython_3_2_1.cython_function_or_method
all_graph_colorings: _cython_3_2_1.cython_function_or_method
b_coloring: _cython_3_2_1.cython_function_or_method
chromatic_number: _cython_3_2_1.cython_function_or_method
edge_coloring: _cython_3_2_1.cython_function_or_method
first_coloring: _cython_3_2_1.cython_function_or_method
format_coloring: _cython_3_2_1.cython_function_or_method
fractional_chromatic_index: _cython_3_2_1.cython_function_or_method
fractional_chromatic_number: _cython_3_2_1.cython_function_or_method
grundy_coloring: _cython_3_2_1.cython_function_or_method
linear_arboricity: _cython_3_2_1.cython_function_or_method
number_of_n_colorings: _cython_3_2_1.cython_function_or_method
numbers_of_colorings: _cython_3_2_1.cython_function_or_method
round_robin: _cython_3_2_1.cython_function_or_method
vertex_coloring: _cython_3_2_1.cython_function_or_method

class Test:
    """File: /build/sagemath/src/sage/src/sage/graphs/graph_coloring.pyx (starting at line 2220)

        This class performs randomized testing for :func:`all_graph_colorings`.

        Since everything else in this file is derived from :func:`all_graph_colorings`, this
        is a pretty good randomized tester for the entire file.  Note that for a
        graph `G`, ``G.chromatic_polynomial()`` uses an entirely different
        algorithm, so we provide a good, independent test.
    """
    @classmethod
    def __init__(cls, *args, **kwargs) -> None:
        """Create and return a new object.  See help(type) for accurate signature."""
    def random(self, tests=...) -> Any:
        """Test.random(self, tests=1000)

        File: /build/sagemath/src/sage/src/sage/graphs/graph_coloring.pyx (starting at line 2230)

        Call ``self.random_all_graph_colorings()``.

        In the future, if other methods are added, it should call them, too.

        TESTS::

            sage: from sage.graphs.graph_coloring import Test
            sage: Test().random(1)                                                      # needs sage.libs.flint"""
    def random_all_graph_colorings(self, tests=...) -> Any:
        """Test.random_all_graph_colorings(self, tests=2)

        File: /build/sagemath/src/sage/src/sage/graphs/graph_coloring.pyx (starting at line 2243)

        Verify the results of ``all_graph_colorings()`` in three ways:

        #. all colorings are unique

        #. number of m-colorings is `P(m)` (where `P` is the chromatic
           polynomial of the graph being tested)

        #. colorings are valid -- that is, that no two vertices of the same
           color share an edge.

        TESTS::

            sage: from sage.graphs.graph_coloring import Test
            sage: Test().random_all_graph_colorings(1)                                  # needs sage.libs.flint"""
