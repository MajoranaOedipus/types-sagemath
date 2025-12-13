import _cython_3_2_1
from sage.cpython.string import bytes_to_str as bytes_to_str, str_to_bytes as str_to_bytes
from sage.structure.element import have_same_parent as have_same_parent, parent as parent

all_labeled_graphs: _cython_3_2_1.cython_function_or_method
coarsest_equitable_refinement: _cython_3_2_1.cython_function_or_method
generate_dense_graphs_edge_addition: _cython_3_2_1.cython_function_or_method
generate_dense_graphs_vert_addition: _cython_3_2_1.cython_function_or_method
get_orbits: _cython_3_2_1.cython_function_or_method
isomorphic: _cython_3_2_1.cython_function_or_method
orbit_partition: _cython_3_2_1.cython_function_or_method
random_tests: _cython_3_2_1.cython_function_or_method
search_tree: _cython_3_2_1.cython_function_or_method

class GraphStruct:
    @classmethod
    def __init__(cls, *args, **kwargs) -> None:
        """Create and return a new object.  See help(type) for accurate signature."""
