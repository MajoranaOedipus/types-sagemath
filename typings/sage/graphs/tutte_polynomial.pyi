from _typeshed import Incomplete
from collections.abc import Generator
from contextlib import contextmanager
from sage.misc.decorators import sage_wraps as sage_wraps
from sage.misc.lazy_attribute import lazy_attribute as lazy_attribute
from sage.misc.misc_c import prod as prod
from sage.rings.integer_ring import ZZ as ZZ

@contextmanager
def removed_multiedge(G, unlabeled_edge) -> Generator[None]:
    """
    A context manager which removes an edge with multiplicity from the
    graph `G` and restores it upon exiting.

    EXAMPLES::

        sage: from sage.graphs.tutte_polynomial import removed_multiedge
        sage: G = Graph(multiedges=True)
        sage: G.add_edges([(0,1,'a'),(0,1,'b')])
        sage: G.edges(sort=True)
        [(0, 1, 'a'), (0, 1, 'b')]
        sage: with removed_multiedge(G,(0,1)) as Y:
        ....:     G.edges(sort=True)
        []
        sage: G.edges(sort=True)
        [(0, 1, 'a'), (0, 1, 'b')]
    """
@contextmanager
def removed_edge(G, edge) -> Generator[None]:
    """
    A context manager which removes an edge from the graph `G` and
    restores it upon exiting.

    EXAMPLES::

        sage: from sage.graphs.tutte_polynomial import removed_edge
        sage: G = Graph()
        sage: G.add_edge(0,1)
        sage: G.edges(sort=True)
        [(0, 1, None)]
        sage: with removed_edge(G,(0,1)) as Y:
        ....:     G.edges(sort=True); G.vertices(sort=True)
        []
        [0, 1]
        sage: G.edges(sort=True)
        [(0, 1, None)]
    """
@contextmanager
def contracted_edge(G, unlabeled_edge) -> Generator[None]:
    """
    Delete the first vertex in the edge, and make all the edges that
    went from it go to the second vertex.

    EXAMPLES::

        sage: from sage.graphs.tutte_polynomial import contracted_edge
        sage: G = Graph(multiedges=True)
        sage: G.add_edges([(0,1,'a'),(1,2,'b'),(0,3,'c')])
        sage: G.edges(sort=True)
        [(0, 1, 'a'), (0, 3, 'c'), (1, 2, 'b')]
        sage: with contracted_edge(G,(0,1)) as Y:
        ....:     G.edges(sort=True); G.vertices(sort=True)
        [(1, 2, 'b'), (1, 3, 'c')]
        [1, 2, 3]
        sage: G.edges(sort=True)
        [(0, 1, 'a'), (0, 3, 'c'), (1, 2, 'b')]
    """
@contextmanager
def removed_loops(G) -> Generator[Incomplete]:
    """
    A context manager which removes all the loops in the graph `G`.
    It yields a list of the loops, and restores the loops upon
    exiting.

    EXAMPLES::

        sage: from sage.graphs.tutte_polynomial import removed_loops
        sage: G = Graph(multiedges=True, loops=True)
        sage: G.add_edges([(0,1,'a'),(1,2,'b'),(0,0,'c')])
        sage: G.edges(sort=True)
        [(0, 0, 'c'), (0, 1, 'a'), (1, 2, 'b')]
        sage: with removed_loops(G) as Y:
        ....:     G.edges(sort=True); G.vertices(sort=True); Y
        [(0, 1, 'a'), (1, 2, 'b')]
        [0, 1, 2]
        [(0, 0, 'c')]
        sage: G.edges(sort=True)
        [(0, 0, 'c'), (0, 1, 'a'), (1, 2, 'b')]
    """
def underlying_graph(G):
    """
    Given a graph `G` with multi-edges, returns a graph where all the
    multi-edges are replaced with a single edge.

    EXAMPLES::

        sage: from sage.graphs.tutte_polynomial import underlying_graph
        sage: G = Graph(multiedges=True)
        sage: G.add_edges([(0,1,'a'),(0,1,'b')])
        sage: G.edges(sort=True)
        [(0, 1, 'a'), (0, 1, 'b')]
        sage: underlying_graph(G).edges(sort=True)
        [(0, 1, None)]
    """
def edge_multiplicities(G):
    """
    Return the dictionary of multiplicities of the edges in the
    graph `G`.

    EXAMPLES::

        sage: from sage.graphs.tutte_polynomial import edge_multiplicities
        sage: G = Graph({1: [2,2,3], 2: [2], 3: [4,4], 4: [2,2,2]})
        sage: sorted(edge_multiplicities(G).items())
        [((1, 2), 2), ((1, 3), 1), ((2, 2), 1), ((2, 4), 3), ((3, 4), 2)]
    """

class Ear:
    """
    An ear is a sequence of vertices

    Here is the definition from [HPR2010]_:

    An ear in a graph is a path `v_1 - v_2 - \\dots - v_n - v_{n+1}`
    where `d(v_1) > 2`, `d(v_{n+1}) > 2` and
    `d(v_2) = d(v_3) = \\dots = d(v_n) = 2`.

    A cycle is viewed as a special ear where `v_1 = v_{n+1}` and the
    restriction on the degree of this vertex is lifted.

    INPUT:
    """
    end_points: Incomplete
    interior: Incomplete
    is_cycle: Incomplete
    graph: Incomplete
    def __init__(self, graph, end_points, interior, is_cycle) -> None:
        """
        EXAMPLES::

            sage: G = graphs.PathGraph(4)
            sage: G.add_edges([(0,4),(0,5),(3,6),(3,7)])
            sage: from sage.graphs.tutte_polynomial import Ear
            sage: E = Ear(G,[0,3],[1,2],False)
        """
    @property
    def s(self):
        """
        Return the number of distinct edges in this ear.

        EXAMPLES::

            sage: G = graphs.PathGraph(4)
            sage: G.add_edges([(0,4),(0,5),(3,6),(3,7)])
            sage: from sage.graphs.tutte_polynomial import Ear
            sage: E = Ear(G,[0,3],[1,2],False)
            sage: E.s
            3
        """
    @property
    def vertices(self):
        """
        Return the vertices of this ear.

        EXAMPLES::

            sage: G = graphs.PathGraph(4)
            sage: G.add_edges([(0,4),(0,5),(3,6),(3,7)])
            sage: from sage.graphs.tutte_polynomial import Ear
            sage: E = Ear(G,[0,3],[1,2],False)
            sage: E.vertices
            [0, 1, 2, 3]
        """
    @lazy_attribute
    def unlabeled_edges(self):
        """
        Return the edges in this ear.

        EXAMPLES::

            sage: G = graphs.PathGraph(4)
            sage: G.add_edges([(0,4),(0,5),(3,6),(3,7)])
            sage: from sage.graphs.tutte_polynomial import Ear
            sage: E = Ear(G,[0,3],[1,2],False)
            sage: E.unlabeled_edges
            [(0, 1), (1, 2), (2, 3)]
        """
    @staticmethod
    def find_ear(g):
        """
        Finds the first ear in a graph.

        EXAMPLES::

            sage: G = graphs.PathGraph(4)
            sage: G.add_edges([(0,4),(0,5),(3,6),(3,7)])
            sage: from sage.graphs.tutte_polynomial import Ear
            sage: E = Ear.find_ear(G)
            sage: E.s
            3
            sage: E.unlabeled_edges
            [(0, 1), (1, 2), (2, 3)]
            sage: E.vertices
            [0, 1, 2, 3]
        """
    @contextmanager
    def removed_from(self, G) -> Generator[None]:
        """
        A context manager which removes the ear from the graph `G`.

        EXAMPLES::

            sage: G = graphs.PathGraph(4)
            sage: G.add_edges([(0,4),(0,5),(3,6),(3,7)])
            sage: len(G.edges(sort=True))
            7
            sage: from sage.graphs.tutte_polynomial import Ear
            sage: E = Ear.find_ear(G)
            sage: with E.removed_from(G) as Y:
            ....:     G.edges(sort=True)
            [(0, 4, None), (0, 5, None), (3, 6, None), (3, 7, None)]
            sage: len(G.edges(sort=True))
            7
        """

class EdgeSelection: ...

class VertexOrder(EdgeSelection):
    order: Incomplete
    inverse_order: Incomplete
    def __init__(self, order) -> None:
        """
        EXAMPLES::

            sage: from sage.graphs.tutte_polynomial import VertexOrder
            sage: A = VertexOrder([4,6,3,2,1,7])
            sage: A.order
            [4, 6, 3, 2, 1, 7]
            sage: A.inverse_order
            {1: 4, 2: 3, 3: 2, 4: 0, 6: 1, 7: 5}
        """
    def __call__(self, graph):
        """
        EXAMPLES::

            sage: from sage.graphs.tutte_polynomial import VertexOrder
            sage: A = VertexOrder([4,0,3,2,1,5])
            sage: G = graphs.PathGraph(6)
            sage: A(G)
            (3, 4, None)
        """

class MinimizeSingleDegree(EdgeSelection):
    def __call__(self, graph):
        """
        EXAMPLES::

            sage: from sage.graphs.tutte_polynomial import MinimizeSingleDegree
            sage: G = graphs.PathGraph(6)
            sage: MinimizeSingleDegree()(G)
            (0, 1, None)
        """

class MinimizeDegree(EdgeSelection):
    def __call__(self, graph):
        """
        EXAMPLES::

            sage: from sage.graphs.tutte_polynomial import MinimizeDegree
            sage: G = graphs.PathGraph(6)
            sage: MinimizeDegree()(G)
            (0, 1, None)
        """

class MaximizeDegree(EdgeSelection):
    def __call__(self, graph):
        """
        EXAMPLES::

            sage: from sage.graphs.tutte_polynomial import MaximizeDegree
            sage: G = graphs.PathGraph(6)
            sage: MaximizeDegree()(G)
            (1, 2, None)
        """

@_cached
def tutte_polynomial(G, edge_selector=None, cache=None):
    """
    Return the Tutte polynomial of the graph `G`.

    INPUT:

    - ``edge_selector`` -- method (optional); this argument allows the user
      to specify his own heuristic for selecting edges used in the deletion
      contraction recurrence

    - ``cache`` -- (optional) dictionary to cache the Tutte
      polynomials generated in the recursive process.  One will be
      created automatically if not provided.

    EXAMPLES:

    The Tutte polynomial of any tree of order `n` is `x^{n-1}`::

        sage: all(T.tutte_polynomial() == x**9 for T in graphs.trees(10))               # needs sage.symbolic
        True

    The Tutte polynomial of the Petersen graph is::

        sage: P = graphs.PetersenGraph()
        sage: P.tutte_polynomial()
        x^9 + 6*x^8 + 21*x^7 + 56*x^6 + 12*x^5*y + y^6 + 114*x^5 + 70*x^4*y
        + 30*x^3*y^2 + 15*x^2*y^3 + 10*x*y^4 + 9*y^5 + 170*x^4 + 170*x^3*y
        + 105*x^2*y^2 + 65*x*y^3 + 35*y^4 + 180*x^3 + 240*x^2*y + 171*x*y^2
        + 75*y^3 + 120*x^2 + 168*x*y + 84*y^2 + 36*x + 36*y

    The Tutte polynomial of a connected graph `G` evaluated at (1,1) is the number of
    spanning trees of `G`::

        sage: G = graphs.RandomGNP(10,0.6)
        sage: while not G.is_connected():
        ....:     G = graphs.RandomGNP(10,0.6)
        sage: G.tutte_polynomial()(1,1) == G.spanning_trees_count()                     # needs sage.modules
        True

    Given that `T(x,y)` is the Tutte polynomial of a graph `G` with
    `n` vertices and `c` connected components, then `(-1)^{n-c} x^k
    T(1-x,0)` is the chromatic polynomial of `G`. ::

        sage: G = graphs.OctahedralGraph()
        sage: T = G.tutte_polynomial()
        sage: R = PolynomialRing(ZZ, 'x')
        sage: R((-1)^5*x*T(1-x,0)).factor()                                             # needs sage.symbolic
        (x - 2) * (x - 1) * x * (x^3 - 9*x^2 + 29*x - 32)
        sage: G.chromatic_polynomial().factor()                                         # needs sage.libs.flint
        (x - 2) * (x - 1) * x * (x^3 - 9*x^2 + 29*x - 32)

    TESTS:

    Providing an external cache::

        sage: cache = {}
        sage: _ = graphs.RandomGNP(7,.5).tutte_polynomial(cache=cache)
        sage: len(cache) > 0
        True

    Verify that :issue:`18366` is fixed::

        sage: g = Graph(multiedges=True)
        sage: g.add_edges([(0,1,1),(1,5,2),(5,3,3),(5,2,4),(2,4,5),(0,2,6),(0,3,7),(0,4,8),(0,5,9)])
        sage: g.tutte_polynomial()(1,1)
        52
        sage: g.spanning_trees_count()                                                  # needs sage.modules
        52
    """
