import _cython_3_2_1
from sage.cpython.string import bytes_to_str as bytes_to_str, str_to_bytes as str_to_bytes
from sage.graphs.graph import Graph as Graph
from typing import Any, ClassVar, overload

simple_connected_graph_genus: _cython_3_2_1.cython_function_or_method

class simple_connected_genus_backtracker:
    '''simple_connected_genus_backtracker(DenseGraph G)

    File: /build/sagemath/src/sage/src/sage/graphs/genus.pyx (starting at line 60)

    A class which computes the genus of a DenseGraph through an extremely slow
    but relatively optimized algorithm.  This is "only" exponential for graphs
    of bounded degree, and feels pretty snappy for 3-regular graphs. The
    generic runtime is

      `|V(G)| \\prod_{v \\in V(G)} (deg(v)-1)!`

    which is `2^{|V(G)|}` for 3-regular graphs, and can achieve `n(n-1)!^{n}`
    for the complete graph on `n` vertices.  We can handily compute the genus of
    `K_6` in milliseconds on modern hardware, but `K_7` may take a few days.
    Don\'t bother with `K_8`, or any graph with more than one vertex of degree 10
    or worse, unless you can find an a priori lower bound on the genus and
    expect the graph to have that genus.

    .. WARNING::

        THIS MAY SEGFAULT OR HANG ON:
            * DISCONNECTED GRAPHS
            * DIRECTED GRAPHS
            * LOOPED GRAPHS
            * MULTIGRAPHS

    EXAMPLES::

        sage: import sage.graphs.genus
        sage: G = graphs.CompleteGraph(6)
        sage: G = Graph(G, sparse=False)
        sage: bt = sage.graphs.genus.simple_connected_genus_backtracker(G._backend.c_graph()[0])
        sage: bt.genus() #long time
        1
        sage: bt.genus(cutoff=1)
        1
        sage: G = graphs.PetersenGraph()
        sage: G = Graph(G, sparse=False)
        sage: bt = sage.graphs.genus.simple_connected_genus_backtracker(G._backend.c_graph()[0])
        sage: bt.genus()
        1
        sage: G = graphs.FlowerSnark()
        sage: G = Graph(G, sparse=False)
        sage: bt = sage.graphs.genus.simple_connected_genus_backtracker(G._backend.c_graph()[0])
        sage: bt.genus()
        2'''
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    def __init__(self, DenseGraphG) -> Any:
        """File: /build/sagemath/src/sage/src/sage/graphs/genus.pyx (starting at line 114)

                Initialize the genus_backtracker object.

                TESTS::

                    sage: import sage.graphs.genus
                    sage: G = Graph(sparse=False)  # indirect doctest
                    sage: gb = sage.graphs.genus.simple_connected_genus_backtracker(G._backend.c_graph()[0])
                    sage: G = Graph(graphs.CompleteGraph(4), sparse=False)
                    sage: gb = sage.graphs.genus.simple_connected_genus_backtracker(G._backend.c_graph()[0])
                    sage: gb.genus()
                    0
        """
    def genus(self, intstyle=..., intcutoff=..., boolrecord_embedding=...) -> Any:
        """simple_connected_genus_backtracker.genus(self, int style=1, int cutoff=0, bool record_embedding=False)

        File: /build/sagemath/src/sage/src/sage/graphs/genus.pyx (starting at line 401)

        Compute the minimal or maximal genus of ``self``'s graph.

        Note, this is a remarkably naive algorithm for a very difficult problem.
        Most interesting cases will take millennia to finish, with the exception
        of graphs with max degree 3.

        INPUT:

        - ``style`` -- integer (default: `1`); find minimum genus if 1,
          maximum genus if 2

        - ``cutoff`` -- integer (default: `0`); stop searching if search style
          is 1 and ``genus`` `\\leq` ``cutoff``, or if style is 2 and ``genus``
          `\\geq` ``cutoff``.  This is useful where the genus of the graph has a
          known bound.

        - ``record_embedding`` -- boolean (default: ``False``); whether or not
          to remember the best embedding seen. This embedding can be retrieved
          with ``self.get_embedding()``.

        OUTPUT: the minimal or maximal genus for ``self``'s graph

        EXAMPLES::

            sage: import sage.graphs.genus
            sage: G = Graph(graphs.CompleteGraph(5), sparse=False)
            sage: gb = sage.graphs.genus.simple_connected_genus_backtracker(G._backend.c_graph()[0])
            sage: gb.genus(cutoff=2, record_embedding=True)
            2
            sage: E = gb.get_embedding()
            sage: gb.genus(record_embedding=False)
            1
            sage: gb.get_embedding() == E
            True
            sage: gb.genus(style=2, cutoff=5)
            3
            sage: G = Graph(sparse=False)
            sage: gb = sage.graphs.genus.simple_connected_genus_backtracker(G._backend.c_graph()[0])
            sage: gb.genus()
            0"""
    @overload
    def get_embedding(self) -> Any:
        """simple_connected_genus_backtracker.get_embedding(self)

        File: /build/sagemath/src/sage/src/sage/graphs/genus.pyx (starting at line 211)

        Return an embedding for the graph.

        If ``min_genus_backtrack`` has been called with ``record_embedding =
        True``, then this will return the first minimal embedding that we found.
        Otherwise, this returns the first embedding considered.

        EXAMPLES::

            sage: import sage.graphs.genus
            sage: G = Graph(graphs.CompleteGraph(5), sparse=False)
            sage: gb = sage.graphs.genus.simple_connected_genus_backtracker(G._backend.c_graph()[0])
            sage: gb.genus(record_embedding=True)
            1
            sage: gb.get_embedding()
            {0: [1, 2, 3, 4], 1: [0, 2, 3, 4], 2: [0, 1, 4, 3], 3: [0, 2, 1, 4], 4: [0, 3, 1, 2]}
            sage: G = Graph(sparse=False)
            sage: G.add_edge(0,1)
            sage: gb = sage.graphs.genus.simple_connected_genus_backtracker(G._backend.c_graph()[0])
            sage: gb.get_embedding()
            {0: [1], 1: [0]}
            sage: G = Graph(sparse=False)
            sage: gb = sage.graphs.genus.simple_connected_genus_backtracker(G._backend.c_graph()[0])
            sage: gb.get_embedding()
            {}"""
    @overload
    def get_embedding(self) -> Any:
        """simple_connected_genus_backtracker.get_embedding(self)

        File: /build/sagemath/src/sage/src/sage/graphs/genus.pyx (starting at line 211)

        Return an embedding for the graph.

        If ``min_genus_backtrack`` has been called with ``record_embedding =
        True``, then this will return the first minimal embedding that we found.
        Otherwise, this returns the first embedding considered.

        EXAMPLES::

            sage: import sage.graphs.genus
            sage: G = Graph(graphs.CompleteGraph(5), sparse=False)
            sage: gb = sage.graphs.genus.simple_connected_genus_backtracker(G._backend.c_graph()[0])
            sage: gb.genus(record_embedding=True)
            1
            sage: gb.get_embedding()
            {0: [1, 2, 3, 4], 1: [0, 2, 3, 4], 2: [0, 1, 4, 3], 3: [0, 2, 1, 4], 4: [0, 3, 1, 2]}
            sage: G = Graph(sparse=False)
            sage: G.add_edge(0,1)
            sage: gb = sage.graphs.genus.simple_connected_genus_backtracker(G._backend.c_graph()[0])
            sage: gb.get_embedding()
            {0: [1], 1: [0]}
            sage: G = Graph(sparse=False)
            sage: gb = sage.graphs.genus.simple_connected_genus_backtracker(G._backend.c_graph()[0])
            sage: gb.get_embedding()
            {}"""
    @overload
    def get_embedding(self) -> Any:
        """simple_connected_genus_backtracker.get_embedding(self)

        File: /build/sagemath/src/sage/src/sage/graphs/genus.pyx (starting at line 211)

        Return an embedding for the graph.

        If ``min_genus_backtrack`` has been called with ``record_embedding =
        True``, then this will return the first minimal embedding that we found.
        Otherwise, this returns the first embedding considered.

        EXAMPLES::

            sage: import sage.graphs.genus
            sage: G = Graph(graphs.CompleteGraph(5), sparse=False)
            sage: gb = sage.graphs.genus.simple_connected_genus_backtracker(G._backend.c_graph()[0])
            sage: gb.genus(record_embedding=True)
            1
            sage: gb.get_embedding()
            {0: [1, 2, 3, 4], 1: [0, 2, 3, 4], 2: [0, 1, 4, 3], 3: [0, 2, 1, 4], 4: [0, 3, 1, 2]}
            sage: G = Graph(sparse=False)
            sage: G.add_edge(0,1)
            sage: gb = sage.graphs.genus.simple_connected_genus_backtracker(G._backend.c_graph()[0])
            sage: gb.get_embedding()
            {0: [1], 1: [0]}
            sage: G = Graph(sparse=False)
            sage: gb = sage.graphs.genus.simple_connected_genus_backtracker(G._backend.c_graph()[0])
            sage: gb.get_embedding()
            {}"""
    @overload
    def get_embedding(self) -> Any:
        """simple_connected_genus_backtracker.get_embedding(self)

        File: /build/sagemath/src/sage/src/sage/graphs/genus.pyx (starting at line 211)

        Return an embedding for the graph.

        If ``min_genus_backtrack`` has been called with ``record_embedding =
        True``, then this will return the first minimal embedding that we found.
        Otherwise, this returns the first embedding considered.

        EXAMPLES::

            sage: import sage.graphs.genus
            sage: G = Graph(graphs.CompleteGraph(5), sparse=False)
            sage: gb = sage.graphs.genus.simple_connected_genus_backtracker(G._backend.c_graph()[0])
            sage: gb.genus(record_embedding=True)
            1
            sage: gb.get_embedding()
            {0: [1, 2, 3, 4], 1: [0, 2, 3, 4], 2: [0, 1, 4, 3], 3: [0, 2, 1, 4], 4: [0, 3, 1, 2]}
            sage: G = Graph(sparse=False)
            sage: G.add_edge(0,1)
            sage: gb = sage.graphs.genus.simple_connected_genus_backtracker(G._backend.c_graph()[0])
            sage: gb.get_embedding()
            {0: [1], 1: [0]}
            sage: G = Graph(sparse=False)
            sage: gb = sage.graphs.genus.simple_connected_genus_backtracker(G._backend.c_graph()[0])
            sage: gb.get_embedding()
            {}"""
