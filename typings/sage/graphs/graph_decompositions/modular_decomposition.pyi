import _cython_3_2_1
import enum
from sage.cpython.string import bytes_to_str as bytes_to_str, str_to_bytes as str_to_bytes
from sage.groups.perm_gps.permgroup_element import PermutationGroupElement as PermutationGroupElement
from sage.misc.random_testing import random_testing as random_testing
from typing import Any, Callable, ClassVar, overload

check_algos_are_equivalent: Callable
check_gamma_modules: Callable
check_maximal_modules: _cython_3_2_1.cython_function_or_method
check_modular_decomposition: _cython_3_2_1.cython_function_or_method
check_module: _cython_3_2_1.cython_function_or_method
children_node_type: _cython_3_2_1.cython_function_or_method
corneil_habib_paul_tedder_algorithm: _cython_3_2_1.cython_function_or_method
either_connected_or_not_connected: _cython_3_2_1.cython_function_or_method
equivalent_trees: _cython_3_2_1.cython_function_or_method
form_module: _cython_3_2_1.cython_function_or_method
gamma_classes: _cython_3_2_1.cython_function_or_method
get_module_type: _cython_3_2_1.cython_function_or_method
get_vertices: _cython_3_2_1.cython_function_or_method
habib_maurer_algorithm: _cython_3_2_1.cython_function_or_method
md_tree_to_graph: _cython_3_2_1.cython_function_or_method
modular_decomposition: _cython_3_2_1.cython_function_or_method
nested_tuple_to_tree: _cython_3_2_1.cython_function_or_method
permute_decomposition: Callable
print_md_tree: _cython_3_2_1.cython_function_or_method
random_md_tree: _cython_3_2_1.cython_function_or_method
recreate_decomposition: Callable
relabel_tree: _cython_3_2_1.cython_function_or_method
tree_to_nested_tuple: _cython_3_2_1.cython_function_or_method

class Node:
    """File: /build/sagemath/src/sage/src/sage/graphs/graph_decompositions/modular_decomposition.pyx (starting at line 207)

        Node class stores information about the node type.

        Node type can be ``PRIME``, ``SERIES``, ``PARALLEL``, ``NORMAL`` or
        ``EMPTY``.

        - ``node_type`` -- is of type NodeType and specifies the type of node
    """
    create_leaf: ClassVar[method] = ...
    def __init__(self, node_type) -> Any:
        """Node.__init__(self, node_type)

        File: /build/sagemath/src/sage/src/sage/graphs/graph_decompositions/modular_decomposition.pyx (starting at line 216)

        Create a node with the given node type.

        EXAMPLES::

            sage: from sage.graphs.graph_decompositions.modular_decomposition import *
            sage: n = Node(NodeType.SERIES); n.node_type
            SERIES
            sage: n.children
            []"""
    @overload
    def is_empty(self) -> Any:
        """Node.is_empty(self)

        File: /build/sagemath/src/sage/src/sage/graphs/graph_decompositions/modular_decomposition.pyx (starting at line 265)

        Check whether ``self`` is an empty node.

        EXAMPLES::

            sage: from sage.graphs.graph_decompositions.modular_decomposition import *
            sage: Node(NodeType.EMPTY).is_empty()
            True
            sage: Node.create_leaf(1).is_empty()
            False"""
    @overload
    def is_empty(self) -> Any:
        """Node.is_empty(self)

        File: /build/sagemath/src/sage/src/sage/graphs/graph_decompositions/modular_decomposition.pyx (starting at line 265)

        Check whether ``self`` is an empty node.

        EXAMPLES::

            sage: from sage.graphs.graph_decompositions.modular_decomposition import *
            sage: Node(NodeType.EMPTY).is_empty()
            True
            sage: Node.create_leaf(1).is_empty()
            False"""
    @overload
    def is_empty(self) -> Any:
        """Node.is_empty(self)

        File: /build/sagemath/src/sage/src/sage/graphs/graph_decompositions/modular_decomposition.pyx (starting at line 265)

        Check whether ``self`` is an empty node.

        EXAMPLES::

            sage: from sage.graphs.graph_decompositions.modular_decomposition import *
            sage: Node(NodeType.EMPTY).is_empty()
            True
            sage: Node.create_leaf(1).is_empty()
            False"""
    @overload
    def is_leaf(self) -> Any:
        """Node.is_leaf(self)

        File: /build/sagemath/src/sage/src/sage/graphs/graph_decompositions/modular_decomposition.pyx (starting at line 279)

        Check whether ``self`` is a leaf.

        EXAMPLES::

            sage: from sage.graphs.graph_decompositions.modular_decomposition import *
            sage: n = Node(NodeType.PRIME)
            sage: n.children.append(Node.create_leaf(1))
            sage: n.children.append(Node.create_leaf(2))
            sage: n.is_leaf()
            False
            sage: all(c.is_leaf() for c in n.children)
            True"""
    @overload
    def is_leaf(self) -> Any:
        """Node.is_leaf(self)

        File: /build/sagemath/src/sage/src/sage/graphs/graph_decompositions/modular_decomposition.pyx (starting at line 279)

        Check whether ``self`` is a leaf.

        EXAMPLES::

            sage: from sage.graphs.graph_decompositions.modular_decomposition import *
            sage: n = Node(NodeType.PRIME)
            sage: n.children.append(Node.create_leaf(1))
            sage: n.children.append(Node.create_leaf(2))
            sage: n.is_leaf()
            False
            sage: all(c.is_leaf() for c in n.children)
            True"""
    @overload
    def is_leaf(self) -> Any:
        """Node.is_leaf(self)

        File: /build/sagemath/src/sage/src/sage/graphs/graph_decompositions/modular_decomposition.pyx (starting at line 279)

        Check whether ``self`` is a leaf.

        EXAMPLES::

            sage: from sage.graphs.graph_decompositions.modular_decomposition import *
            sage: n = Node(NodeType.PRIME)
            sage: n.children.append(Node.create_leaf(1))
            sage: n.children.append(Node.create_leaf(2))
            sage: n.is_leaf()
            False
            sage: all(c.is_leaf() for c in n.children)
            True"""
    @overload
    def is_prime(self) -> Any:
        """Node.is_prime(self)

        File: /build/sagemath/src/sage/src/sage/graphs/graph_decompositions/modular_decomposition.pyx (starting at line 231)

        Check whether ``self`` is a prime node.

        EXAMPLES::

            sage: from sage.graphs.graph_decompositions.modular_decomposition import *
            sage: n = Node(NodeType.PRIME)
            sage: n.children.append(Node.create_leaf(1))
            sage: n.children.append(Node.create_leaf(2))
            sage: n.is_prime()
            True
            sage: (n.children[0].is_prime(), n.children[1].is_prime())
            (False, False)"""
    @overload
    def is_prime(self) -> Any:
        """Node.is_prime(self)

        File: /build/sagemath/src/sage/src/sage/graphs/graph_decompositions/modular_decomposition.pyx (starting at line 231)

        Check whether ``self`` is a prime node.

        EXAMPLES::

            sage: from sage.graphs.graph_decompositions.modular_decomposition import *
            sage: n = Node(NodeType.PRIME)
            sage: n.children.append(Node.create_leaf(1))
            sage: n.children.append(Node.create_leaf(2))
            sage: n.is_prime()
            True
            sage: (n.children[0].is_prime(), n.children[1].is_prime())
            (False, False)"""
    @overload
    def is_prime(self) -> Any:
        """Node.is_prime(self)

        File: /build/sagemath/src/sage/src/sage/graphs/graph_decompositions/modular_decomposition.pyx (starting at line 231)

        Check whether ``self`` is a prime node.

        EXAMPLES::

            sage: from sage.graphs.graph_decompositions.modular_decomposition import *
            sage: n = Node(NodeType.PRIME)
            sage: n.children.append(Node.create_leaf(1))
            sage: n.children.append(Node.create_leaf(2))
            sage: n.is_prime()
            True
            sage: (n.children[0].is_prime(), n.children[1].is_prime())
            (False, False)"""
    @overload
    def is_series(self) -> Any:
        """Node.is_series(self)

        File: /build/sagemath/src/sage/src/sage/graphs/graph_decompositions/modular_decomposition.pyx (starting at line 248)

        Check whether ``self`` is a series node.

        EXAMPLES::

            sage: from sage.graphs.graph_decompositions.modular_decomposition import *
            sage: n = Node(NodeType.SERIES)
            sage: n.children.append(Node.create_leaf(1))
            sage: n.children.append(Node.create_leaf(2))
            sage: n.is_series()
            True
            sage: (n.children[0].is_series(), n.children[1].is_series())
            (False, False)"""
    @overload
    def is_series(self) -> Any:
        """Node.is_series(self)

        File: /build/sagemath/src/sage/src/sage/graphs/graph_decompositions/modular_decomposition.pyx (starting at line 248)

        Check whether ``self`` is a series node.

        EXAMPLES::

            sage: from sage.graphs.graph_decompositions.modular_decomposition import *
            sage: n = Node(NodeType.SERIES)
            sage: n.children.append(Node.create_leaf(1))
            sage: n.children.append(Node.create_leaf(2))
            sage: n.is_series()
            True
            sage: (n.children[0].is_series(), n.children[1].is_series())
            (False, False)"""
    @overload
    def is_series(self) -> Any:
        """Node.is_series(self)

        File: /build/sagemath/src/sage/src/sage/graphs/graph_decompositions/modular_decomposition.pyx (starting at line 248)

        Check whether ``self`` is a series node.

        EXAMPLES::

            sage: from sage.graphs.graph_decompositions.modular_decomposition import *
            sage: n = Node(NodeType.SERIES)
            sage: n.children.append(Node.create_leaf(1))
            sage: n.children.append(Node.create_leaf(2))
            sage: n.is_series()
            True
            sage: (n.children[0].is_series(), n.children[1].is_series())
            (False, False)"""
    def __eq__(self, other) -> Any:
        """Node.__eq__(self, other)

        File: /build/sagemath/src/sage/src/sage/graphs/graph_decompositions/modular_decomposition.pyx (starting at line 311)

        Compare two nodes for equality.

        EXAMPLES::

            sage: from sage.graphs.graph_decompositions.modular_decomposition import *
            sage: n1 = Node(NodeType.PRIME)
            sage: n2 = Node(NodeType.PRIME)
            sage: n3 = Node(NodeType.SERIES)
            sage: n1 == n2
            True
            sage: n1 == n3
            False"""

class NodeType(enum.IntEnum):
    """File: /build/sagemath/src/sage/src/sage/graphs/graph_decompositions/modular_decomposition.pyx (starting at line 167)

        NodeType is an enumeration class used to define the various types of nodes
        in modular decomposition tree.

        The various node types defined are

        - ``PARALLEL`` -- indicates the node is a parallel module

        - ``SERIES`` -- indicates the node is a series module

        - ``PRIME`` -- indicates the node is a prime module

        - ``EMPTY`` -- indicates a empty tree

        - ``NORMAL`` -- indicates the node is normal containing a vertex
    """
    __new__: ClassVar[Callable] = ...
    EMPTY: ClassVar[NodeType] = ...
    NORMAL: ClassVar[NodeType] = ...
    PARALLEL: ClassVar[NodeType] = ...
    PRIME: ClassVar[NodeType] = ...
    SERIES: ClassVar[NodeType] = ...
    _generate_next_value_: ClassVar[Callable] = ...
    _hashable_values_: ClassVar[list] = ...
    _member_map_: ClassVar[dict] = ...
    _member_names_: ClassVar[list] = ...
    _member_type_: ClassVar[type[int]] = ...
    _unhashable_values_: ClassVar[list] = ...
    _unhashable_values_map_: ClassVar[dict] = ...
    _use_args_: ClassVar[bool] = ...
    _value2member_map_: ClassVar[dict] = ...
    def __format__(self, *args, **kwargs) -> str:
        """Convert to a string according to format_spec."""
