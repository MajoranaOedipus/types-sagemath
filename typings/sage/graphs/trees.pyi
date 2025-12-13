from sage.cpython.string import bytes_to_str as bytes_to_str, str_to_bytes as str_to_bytes
from sage.graphs.graph import Graph as Graph
from typing import Any, ClassVar, overload

class TreeIterator:
    """TreeIterator(int vertices)

    File: /build/sagemath/src/sage/src/sage/graphs/trees.pyx (starting at line 22)

    This class iterates over all trees with n vertices (up to isomorphism).

    EXAMPLES::

        sage: from sage.graphs.trees import TreeIterator
        sage: def check_trees(n):
        ....:     trees = []
        ....:     for t in TreeIterator(n):
        ....:         if not t.is_tree():
        ....:             return False
        ....:         if t.num_verts() != n:
        ....:             return False
        ....:         if t.num_edges() != n - 1:
        ....:             return False
        ....:         for tree in trees:
        ....:             if tree.is_isomorphic(t):
        ....:                 return False
        ....:         trees.append(t)
        ....:     return True
        sage: check_trees(10)
        True

    ::

        sage: from sage.graphs.trees import TreeIterator
        sage: count = 0
        sage: for t in TreeIterator(15):
        ....:     count += 1
        sage: count
        7741"""
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    @overload
    def __init__(self, intvertices) -> Any:
        """File: /build/sagemath/src/sage/src/sage/graphs/trees.pyx (starting at line 56)

                Initialize an iterator over all trees with `n` vertices.

                EXAMPLES::

                    sage: from sage.graphs.trees import TreeIterator
                    sage: t = TreeIterator(100) # indirect doctest
                    sage: print(t)
                    Iterator over all trees with 100 vertices
        """
    @overload
    def __init__(self, n) -> Any:
        """File: /build/sagemath/src/sage/src/sage/graphs/trees.pyx (starting at line 56)

                Initialize an iterator over all trees with `n` vertices.

                EXAMPLES::

                    sage: from sage.graphs.trees import TreeIterator
                    sage: t = TreeIterator(100) # indirect doctest
                    sage: print(t)
                    Iterator over all trees with 100 vertices
        """
    def __iter__(self) -> Any:
        """TreeIterator.__iter__(self)

        File: /build/sagemath/src/sage/src/sage/graphs/trees.pyx (starting at line 94)

        Return an iterator over all the trees with `n` vertices.

        EXAMPLES::

            sage: from sage.graphs.trees import TreeIterator
            sage: t = TreeIterator(4)
            sage: list(iter(t))
            [Graph on 4 vertices, Graph on 4 vertices]"""
    def __next__(self) -> Any:
        """TreeIterator.__next__(self)

        File: /build/sagemath/src/sage/src/sage/graphs/trees.pyx (starting at line 107)

        Return the next tree with `n` vertices.

        EXAMPLES::

            sage: from sage.graphs.trees import TreeIterator
            sage: T = TreeIterator(5)
            sage: [t for t in T] # indirect doctest
            [Graph on 5 vertices, Graph on 5 vertices, Graph on 5 vertices]


        TESTS:

        This used to be broken for trees with no vertices
        and was fixed in :issue:`13719` ::

            sage: from sage.graphs.trees import TreeIterator
            sage: T = TreeIterator(0)
            sage: [t for t in T] # indirect doctest
            [Graph on 0 vertices]"""
