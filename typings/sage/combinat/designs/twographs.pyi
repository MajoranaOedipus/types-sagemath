from sage.combinat.designs.incidence_structures import IncidenceStructure as IncidenceStructure

class TwoGraph(IncidenceStructure):
    """
    Two-graphs class.

    A two-graph on `n` points is a 3-uniform hypergraph, i.e.  a family `T
    \\subset \\binom {[n]}{3}` of `3`-sets, such that any `4`-set `S\\subset [n]`
    of size four contains an even number of elements of `T`. For more
    information, see the documentation of the
    :mod:`~sage.combinat.designs.twographs` module.
    """
    def __init__(self, points=None, blocks=None, incidence_matrix=None, name=None, check: bool = False, copy: bool = True) -> None:
        """
        Constructor of the class.

        TESTS::

            sage: from sage.combinat.designs.twographs import TwoGraph
            sage: TwoGraph([[1,2]])
            Incidence structure with 2 points and 1 blocks
            sage: TwoGraph([[1,2]], check=True)
            Traceback (most recent call last):
            ...
            AssertionError: the structure is not a 2-graph!
            sage: p = graphs.PetersenGraph().twograph()                                 # needs sage.modules
            sage: TwoGraph(p, check=True)                                               # needs sage.modules
            Incidence structure with 10 points and 60 blocks
        """
    def is_regular_twograph(self, alpha: bool = False):
        """
        Test if the :class:`TwoGraph` is regular, i.e. is a 2-design.

        Namely, each pair of elements of :meth:`ground_set` is contained in
        exactly ``alpha`` triples.

        INPUT:

        - ``alpha`` -- boolean (default: ``False``); return the value of
          ``alpha``, if possible

        EXAMPLES::

            sage: # needs sage.modules
            sage: p = graphs.PetersenGraph().twograph()
            sage: p.is_regular_twograph(alpha=True)
            4
            sage: p.is_regular_twograph()
            True
            sage: p = graphs.PathGraph(5).twograph()
            sage: p.is_regular_twograph(alpha=True)
            False
            sage: p.is_regular_twograph()
            False
        """
    def descendant(self, v):
        """
        The descendant :class:`graph <sage.graphs.graph.Graph>` at ``v``.

        The :mod:`switching class of graphs <sage.combinat.designs.twographs>`
        corresponding to ``self`` contains a graph ``D`` with ``v`` its own connected
        component; removing ``v`` from ``D``, one obtains the descendant graph of
        ``self`` at ``v``, which is constructed by this method.

        INPUT:

        - ``v`` -- an element of :meth:`ground_set`

        EXAMPLES::

            sage: p = graphs.PetersenGraph().twograph().descendant(0)                   # needs sage.modules
            sage: p.is_strongly_regular(parameters=True)                                # needs sage.modules
            (9, 4, 1, 2)
        """
    def complement(self):
        """
        The two-graph which is the complement of ``self``.

        That is, the two-graph consisting exactly of triples not in ``self``.
        Note that this is different from :meth:`complement
        <sage.combinat.designs.incidence_structures.IncidenceStructure.complement>`
        of the :class:`parent class
        <sage.combinat.designs.incidence_structures.IncidenceStructure>`.

        EXAMPLES::

            sage: p = graphs.CompleteGraph(8).line_graph().twograph()                   # needs sage.modules
            sage: pc = p.complement(); pc                                               # needs sage.modules
            Incidence structure with 28 points and 1260 blocks

        TESTS::

            sage: from sage.combinat.designs.twographs import is_twograph
            sage: is_twograph(pc)                                                       # needs sage.modules
            True
        """

def taylor_twograph(q):
    """
    Constructing Taylor's two-graph for `U_3(q)`, `q` odd prime power.

    The Taylor's two-graph `T` has the `q^3+1` points of the projective plane over `F_{q^2}`
    singular w.r.t. the non-degenerate Hermitean form `S` preserved by `U_3(q)` as its ground set;
    the triples are `\\{x,y,z\\}` satisfying the condition that `S(x,y)S(y,z)S(z,x)` is square
    (respectively non-square) if `q \\cong 1 \\mod 4` (respectively if `q \\cong 3 \\mod 4`).
    See §7E of [BL1984]_.

    There is also a `2-(q^3+1,q+1,1)`-design on these `q^3+1` points, known as the unital of
    order `q`, also invariant under `U_3(q)`.

    INPUT:

    - ``q`` -- a power of an odd prime

    EXAMPLES::

        sage: from sage.combinat.designs.twographs import taylor_twograph
        sage: T = taylor_twograph(3); T                                                 # needs sage.rings.finite_rings
        Incidence structure with 28 points and 1260 blocks
    """
def is_twograph(T) -> bool:
    """
    Check whether the incidence system `T` is a two-graph.

    INPUT:

    - ``T`` -- an :class:`incidence structure <sage.combinat.designs.IncidenceStructure>`

    EXAMPLES:

    a two-graph from a graph::

        sage: from sage.combinat.designs.twographs import (is_twograph, TwoGraph)
        sage: p = graphs.PetersenGraph().twograph()                                     # needs sage.modules
        sage: is_twograph(p)                                                            # needs sage.modules
        True

    a non-regular 2-uniform hypergraph which is a two-graph::

        sage: is_twograph(TwoGraph([[1,2,3],[1,2,4]]))
        True

    TESTS:

    wrong size of blocks::

        sage: is_twograph(designs.projective_plane(3))                                  # needs sage.schemes
        False

    a triple system which is not a two-graph::

        sage: is_twograph(designs.projective_plane(2))                                  # needs sage.schemes
        False
    """
def twograph_descendant(G, v, name=None):
    """
    Return the descendant graph w.r.t. vertex `v` of the two-graph of `G`.

    In the :mod:`switching class <sage.combinat.designs.twographs>` of `G`,
    construct a graph `\\Delta` with `v` an isolated vertex, and return the subgraph
    `\\Delta \\setminus v`. It is equivalent to, although much faster than, computing the
    :meth:`TwoGraph.descendant` of :meth:`two-graph of G <sage.graphs.graph.Graph.twograph>`, as the
    intermediate two-graph is not constructed.

    INPUT:

    - ``G`` -- a :class:`graph <sage.graphs.graph.Graph>`

    - ``v`` -- a vertex of ``G``

    - ``name`` -- (default: ``None``) no name, otherwise derive from the construction

    EXAMPLES:

    one of s.r.g.'s from the :mod:`database <sage.graphs.strongly_regular_db>`::

        sage: from sage.combinat.designs.twographs import twograph_descendant
        sage: A = graphs.strongly_regular_graph(280,135,70)                   # optional - gap_package_design internet
        sage: twograph_descendant(A, 0).is_strongly_regular(parameters=True)  # optional - gap_package_design internet
        (279, 150, 85, 75)

    TESTS::

        sage: T8 = graphs.CompleteGraph(8).line_graph()
        sage: v = T8.vertices(sort=True)[0]
        sage: twograph_descendant(T8, v) == T8.twograph().descendant(v)                 # needs sage.modules
        True
        sage: twograph_descendant(T8, v).is_strongly_regular(parameters=True)
        (27, 16, 10, 8)
        sage: p = graphs.PetersenGraph()
        sage: twograph_descendant(p, 5)
        Graph on 9 vertices
        sage: twograph_descendant(p, 5, name=True)
        descendant of Petersen graph at 5: Graph on 9 vertices
    """
