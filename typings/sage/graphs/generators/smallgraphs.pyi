from sage.graphs.graph import Graph as Graph
from sage.misc.functional import sqrt as sqrt
from sage.rings.rational_field import QQ as QQ

def HarborthGraph():
    """
    Return the Harborth Graph.

    The Harborth graph has 104 edges and 52 vertices, and is the smallest known
    example of a 4-regular matchstick graph. For more information, see the
    :wikipedia:`Harborth_graph`.

    EXAMPLES::

        sage: g = graphs.HarborthGraph(); g
        Harborth Graph: Graph on 52 vertices
        sage: g.is_regular(4)
        True
    """
def HarriesGraph(embedding: int = 1):
    """
    Return the Harries Graph.

    The Harries graph is a Hamiltonian 3-regular graph on 70 vertices.
    See the :wikipedia:`Harries_graph`.

    The default embedding here is to emphasize the graph's 4 orbits. This graph
    actually has a funny construction. The following procedure gives an idea of
    it, though not all the adjacencies are being properly defined.

    #. Take two disjoint copies of a :meth:`Petersen graph
       <PetersenGraph>`. Their vertices will form an orbit of the final graph.

    #. Subdivide all the edges once, to create 15+15=30 new vertices, which
       together form another orbit.

    #. Create 15 vertices, each of them linked to 2 corresponding vertices of
       the previous orbit, one in each of the two subdivided Petersen graphs. At
       the end of this step all vertices from the previous orbit have degree 3,
       and the only vertices of degree 2 in the graph are those that were just
       created.

    #. Create 5 vertices connected only to the ones from the previous orbit so
       that the graph becomes 3-regular.

    INPUT:

    - ``embedding`` -- integer (default: `1`); two embeddings are available,
      and can be selected by setting ``embedding`` to 1 or 2

    EXAMPLES::

        sage: # needs networkx
        sage: g = graphs.HarriesGraph()
        sage: g.order()
        70
        sage: g.size()
        105
        sage: g.girth()
        10
        sage: g.diameter()
        6
        sage: g.show(figsize=[10, 10])          # long time                             # needs sage.plot
        sage: graphs.HarriesGraph(embedding=2).show(figsize=[10, 10])   # long time, needs sage.plot

    TESTS::

        sage: graphs.HarriesGraph(embedding=3)                                          # needs networkx
        Traceback (most recent call last):
        ...
        ValueError: the value of embedding must be 1 or 2
    """
def HarriesWongGraph(embedding: int = 1):
    """
    Return the Harries-Wong Graph.

    See the :wikipedia:`Harries-Wong_graph`.

    *About the default embedding:*

    The default embedding is an attempt to emphasize the graph's 8 (!!!)
    different orbits. In order to understand this better, one can picture the
    graph as being built in the following way.

    #. One first creates a 3-dimensional cube (8 vertices, 12 edges),
       whose vertices define the first orbit of the final graph.

    #. The edges of this graph are subdivided once, to create 12 new vertices
       which define a second orbit.

    #. The edges of the graph are subdivided once more, to create 24 new
       vertices giving a third orbit.

    #. 4 vertices are created and made adjacent to the vertices of the second
       orbit so that they have degree 3. These 4 vertices also define a new
       orbit.

    #. In order to make the vertices from the third orbit 3-regular (they all
       miss one edge), one creates a binary tree on 1 + 3 + 6 + 12 vertices. The
       leaves of this new tree are made adjacent to the 12 vertices of the third
       orbit, and the graph is now 3-regular. This binary tree contributes 4 new
       orbits to the Harries-Wong graph.

    INPUT:

    - ``embedding`` -- integer (default: `1`); two embeddings are available,
      and can be selected by setting ``embedding`` to 1 or 2

    EXAMPLES::

        sage: # needs networkx
        sage: g = graphs.HarriesWongGraph()
        sage: g.order()
        70
        sage: g.size()
        105
        sage: g.girth()
        10
        sage: g.diameter()
        6
        sage: orbits = g.automorphism_group(orbits=True)[-1]    # long time             # needs sage.groups
        sage: g.show(figsize=[15, 15], partition=orbits)        # long time             # needs sage.groups sage.plot

    Alternative embedding::

        sage: graphs.HarriesWongGraph(embedding=2).show()       # long time             # needs networkx sage.plot

    TESTS::

        sage: graphs.HarriesWongGraph(embedding=3)                                      # needs networkx
        Traceback (most recent call last):
        ...
        ValueError: the value of embedding must be 1 or 2
    """
def WellsGraph():
    '''
    Return the Wells graph.

    For more information on the Wells graph (also called Armanios-Wells graph),
    see `this page <https://www.win.tue.nl/~aeb/graphs/Wells.html>`_.

    The implementation follows the construction given on page 266 of [BCN1989]_.
    This requires to create intermediate graphs and run a small isomorphism
    test, while everything could be replaced by a pre-computed list of edges.
    I believe that it is better to keep "the recipe" in the code, however, as it
    is quite unlikely that this could become the most time-consuming operation
    in any sensible algorithm, and .... "preserves knowledge", which is what
    open-source software is meant to do.

    EXAMPLES::

        sage: g = graphs.WellsGraph(); g
        Wells graph: Graph on 32 vertices
        sage: g.order()
        32
        sage: g.size()
        80
        sage: g.girth()
        5
        sage: g.diameter()
        4
        sage: g.chromatic_number()
        4
        sage: g.is_regular(k=5)
        True
    '''
def Cell600(embedding: int = 1):
    """
    Return the 600-Cell graph.

    This is the adjacency graph of the 600-cell. It has 120 vertices and 720
    edges. For more information, see the :wikipedia:`600-cell`.

    INPUT:

    - ``embedding`` -- integer (default: `1`); two different embeddings for a
      plot

    EXAMPLES::

        sage: # long time, needs sage.rings.number_field
        sage: g = graphs.Cell600()
        sage: g.size()
        720
        sage: g.is_regular(12)
        True
        sage: g.is_vertex_transitive()
        True
    """
def Cell120():
    """
    Return the 120-Cell graph.

    This is the adjacency graph of the 120-cell. It has 600 vertices and 1200
    edges. For more information, see the :wikipedia:`120-cell`.

    EXAMPLES::

        sage: # long time, needs sage.rings.number_field
        sage: g = graphs.Cell120()
        sage: g.size()
        1200
        sage: g.is_regular(4)
        True
        sage: g.is_vertex_transitive()
        True
    """
def SuzukiGraph():
    """
    Return the Suzuki Graph.

    The Suzuki graph has 1782 vertices, and is strongly regular with parameters
    `(1782,416,100,96)`. Known as S.15 in [Hub1975]_.

    .. NOTE::

        It takes approximately 50 seconds to build this graph. Do not be too
        impatient.

    EXAMPLES::

        sage: g = graphs.SuzukiGraph(); g  # optional internet # not tested
        Suzuki graph: Graph on 1782 vertices
        sage: g.is_strongly_regular(parameters=True)  # optional internet # not tested
        (1782, 416, 100, 96)
    """
def HallJankoGraph(from_string: bool = True):
    '''
    Return the Hall-Janko graph.

    For more information on the Hall-Janko graph, see the
    :wikipedia:`Hall-Janko_graph`.

    The construction used to generate this graph in Sage is by a 100-point
    permutation representation of the Janko group `J_2`, as described in version
    3 of the ATLAS of Finite Group representations, in particular on the page
    `ATLAS: J2 -- Permutation representation on 100 points
    <http://brauer.maths.qmul.ac.uk/Atlas/v3/permrep/J2G1-p100B0>`_.

    INPUT:

    - ``from_string`` -- boolean (default: ``True``); whether to build the graph
      from its sparse6 string or through GAP. The two methods return the same
      graph though doing it through GAP takes more time.

    EXAMPLES::

        sage: g = graphs.HallJankoGraph()
        sage: g.is_regular(36)
        True
        sage: g.is_vertex_transitive()                                                  # needs sage.groups
        True

    Is it really strongly regular with parameters 14, 12? ::

        sage: nu = set(g.neighbors(0))
        sage: for v in range(1, 100):
        ....:     if v in nu:
        ....:         expected = 14
        ....:     else:
        ....:         expected = 12
        ....:     nv = set(g.neighbors(v))
        ....:     nv.discard(0)
        ....:     if len(nu & nv) != expected:
        ....:         print("Something is wrong here!!!")
        ....:         break

    Some other properties that we know how to check::

        sage: g.diameter()
        2
        sage: g.girth()
        3
        sage: factor(g.characteristic_polynomial())                                     # needs sage.libs.pari sage.modules
        (x - 36) * (x - 6)^36 * (x + 4)^63

    TESTS::

        sage: gg = graphs.HallJankoGraph(from_string=False)  # long time # optional - internet
        sage: g.is_isomorphic(gg)  # long time # optional - internet
        True
    '''
def Balaban10Cage(embedding: int = 1):
    """
    Return the Balaban 10-cage.

    The Balaban 10-cage is a 3-regular graph with 70 vertices and 105 edges. See
    the :wikipedia:`Balaban_10-cage`.

    The default embedding gives a deeper understanding of the graph's
    automorphism group. It is divided into 4 layers (each layer being a set of
    points at equal distance from the drawing's center). From outside to inside:

    - L1: The outer layer (vertices which are the furthest from the origin) is
      actually the disjoint union of two cycles of length 10.

    - L2: The second layer is an independent set of 20 vertices.

    - L3: The third layer is a matching on 10 vertices.

    - L4: The inner layer (vertices which are the closest from the origin) is
      also the disjoint union of two cycles of length 10.

    This graph is not vertex-transitive, and its vertices are partitioned into 3
    orbits: L2, L3, and the union of L1 of L4 whose elements are equivalent.

    INPUT:

    - ``embedding`` -- integer (default: `1`); two embeddings are available,
      and can be selected by setting ``embedding`` to be either 1 or 2

    EXAMPLES::

        sage: # needs networkx
        sage: g = graphs.Balaban10Cage()
        sage: g.girth()
        10
        sage: g.chromatic_number()
        2
        sage: g.diameter()
        6
        sage: g.is_hamiltonian()                                                        # needs sage.numerical.mip
        True
        sage: g.show(figsize=[10,10])           # long time                             # needs sage.plot

    TESTS::

        sage: graphs.Balaban10Cage(embedding='foo')                                     # needs networkx
        Traceback (most recent call last):
        ...
        ValueError: the value of embedding must be 1 or 2
    """
def Balaban11Cage(embedding: int = 1):
    """
    Return the Balaban 11-cage.

    For more information, see the :wikipedia:`Balaban_11-cage`.

    INPUT:

    - ``embedding`` -- integer (default: `1`); three embeddings are available,
      and can be selected by setting ``embedding`` to be 1, 2, or 3

      - The first embedding is the one appearing on page 9 of the Fifth Annual
        Graph Drawing Contest report [EMMN1998]_. It separates vertices based on
        their eccentricity (see :meth:`eccentricity()
        <sage.graphs.generic_graph.GenericGraph.eccentricity>`).

      - The second embedding has been produced just for Sage and is meant to
        emphasize the automorphism group's 6 orbits.

      - The last embedding is the default one produced by the :meth:`LCFGraph`
        constructor.

    .. NOTE::

        The vertex labeling changes according to the value of ``embedding=1``.

    EXAMPLES:

    Basic properties::

        sage: g = graphs.Balaban11Cage()
        sage: g.order()
        112
        sage: g.size()
        168
        sage: g.girth()
        11
        sage: g.diameter()
        8
        sage: g.automorphism_group().cardinality()                                      # needs sage.groups
        64

    Our many embeddings::

        sage: g1 = graphs.Balaban11Cage(embedding=1)
        sage: g2 = graphs.Balaban11Cage(embedding=2)                                    # needs networkx
        sage: g3 = graphs.Balaban11Cage(embedding=3)                                    # needs networkx
        sage: g1.show(figsize=[10,10])          # long time                             # needs sage.plot
        sage: g2.show(figsize=[10,10])          # long time                             # needs networkx sage.plot
        sage: g3.show(figsize=[10,10])          # long time                             # needs networkx sage.plot

    Proof that the embeddings are the same graph::

        sage: g1.is_isomorphic(g2)  # g2 and g3 are obviously isomorphic                # needs networkx
        True

    TESTS::

        sage: graphs.Balaban11Cage(embedding='xyzzy')
        Traceback (most recent call last):
        ...
        ValueError: the value of embedding must be 1, 2, or 3
    """
def BidiakisCube():
    """
    Return the Bidiakis cube.

    For more information, see the :wikipedia:`Bidiakis_cube`.

    EXAMPLES:

    The Bidiakis cube is a 3-regular graph having 12 vertices and 18 edges. This
    means that each vertex has a degree of 3::

        sage: g = graphs.BidiakisCube(); g
        Bidiakis cube: Graph on 12 vertices
        sage: g.show()                          # long time                             # needs sage.plot
        sage: g.order()
        12
        sage: g.size()
        18
        sage: g.is_regular(3)
        True

    It is a Hamiltonian graph with diameter 3 and girth 4::

        sage: g.is_hamiltonian()                                                        # needs sage.numerical.mip
        True
        sage: g.diameter()
        3
        sage: g.girth()
        4

    It is a planar graph with characteristic polynomial
    `(x - 3) (x - 2) (x^4) (x + 1) (x + 2) (x^2 + x - 4)^2` and
    chromatic number 3::

        sage: g.is_planar()
        True
        sage: char_poly = g.characteristic_polynomial()                                 # needs sage.modules
        sage: x = char_poly.parent()('x')                                               # needs sage.modules
        sage: char_poly == (x - 3) * (x - 2) * (x^4) * (x + 1) * (x + 2) * (x^2 + x - 4)^2          # needs sage.modules
        True
        sage: g.chromatic_number()                                                      # needs sage.modules
        3
    """
def BiggsSmithGraph(embedding: int = 1):
    """
    Return the Biggs-Smith graph.

    For more information, see the :wikipedia:`Biggs-Smith_graph`.

    INPUT:

    - ``embedding`` -- integer (default: `1`); two embeddings are available,
      and can be selected by setting ``embedding`` to be 1 or 2

    EXAMPLES:

    Basic properties::

        sage: # needs networkx
        sage: g = graphs.BiggsSmithGraph()
        sage: g.order()
        102
        sage: g.size()
        153
        sage: g.girth()
        9
        sage: g.diameter()
        7
        sage: g.automorphism_group().cardinality()      # long time
        2448
        sage: g.show(figsize=[10, 10])          # long time                             # needs sage.plot

    The other embedding::

        sage: graphs.BiggsSmithGraph(embedding=2).show()        # long time             # needs networkx

    TESTS::

        sage: graphs.BiggsSmithGraph(embedding='xyzzy')                                 # needs networkx
        Traceback (most recent call last):
        ...
        ValueError: the value of embedding must be 1 or 2
    """
def BlanusaFirstSnarkGraph():
    """
    Return the first Blanusa Snark Graph.

    The Blanusa graphs are two snarks on 18 vertices and 27 edges. For more
    information on them, see the :wikipedia:`Blanusa_snarks`.

    .. SEEALSO::

        * :meth:`~sage.graphs.graph_generators.GraphGenerators.BlanusaSecondSnarkGraph`.

    EXAMPLES::

        sage: g = graphs.BlanusaFirstSnarkGraph()
        sage: g.order()
        18
        sage: g.size()
        27
        sage: g.diameter()
        4
        sage: g.girth()
        5
        sage: g.automorphism_group().cardinality()                                      # needs sage.groups
        8
    """
def BlanusaSecondSnarkGraph():
    """
    Return the second Blanusa Snark Graph.

    The Blanusa graphs are two snarks on 18 vertices and 27 edges. For more
    information on them, see the :wikipedia:`Blanusa_snarks`.

    .. SEEALSO::

        * :meth:`~sage.graphs.graph_generators.GraphGenerators.BlanusaFirstSnarkGraph`.

    EXAMPLES::

        sage: g = graphs.BlanusaSecondSnarkGraph()
        sage: g.order()
        18
        sage: g.size()
        27
        sage: g.diameter()
        4
        sage: g.girth()
        5
        sage: g.automorphism_group().cardinality()                                      # needs sage.groups
        4
    """
def BrinkmannGraph():
    """
    Return the Brinkmann graph.

    For more information, see the :wikipedia:`Brinkmann_graph`.

    EXAMPLES:

    The Brinkmann graph is a 4-regular graph having 21 vertices and 42
    edges. This means that each vertex has degree 4::

        sage: G = graphs.BrinkmannGraph(); G
        Brinkmann graph: Graph on 21 vertices
        sage: G.show()                          # long time                             # needs sage.plot
        sage: G.order()
        21
        sage: G.size()
        42
        sage: G.is_regular(4)
        True

    It is an Eulerian graph with radius 3, diameter 3, and girth 5::

        sage: G.is_eulerian()
        True
        sage: G.radius()
        3
        sage: G.diameter()
        3
        sage: G.girth()
        5

    The Brinkmann graph is also Hamiltonian with chromatic number 4::

        sage: G.is_hamiltonian()                                                        # needs sage.numerical.mip
        True
        sage: G.chromatic_number()
        4

    Its automorphism group is isomorphic to `D_7`::

        sage: ag = G.automorphism_group()                                               # needs sage.groups
        sage: ag.is_isomorphic(DihedralGroup(7))                                        # needs sage.groups
        True
    """
def BrouwerHaemersGraph():
    """
    Return the Brouwer-Haemers Graph.

    The Brouwer-Haemers is the only strongly regular graph of parameters
    `(81,20,1,6)`. It is build in Sage as the Affine Orthogonal graph
    `VO^-(6,3)`. For more information on this graph, see its `corresponding page
    on Andries Brouwer's website
    <https://www.win.tue.nl/~aeb/graphs/Brouwer-Haemers.html>`_.

    EXAMPLES::

        sage: g = graphs.BrouwerHaemersGraph(); g                                       # needs sage.modules
        Brouwer-Haemers: Graph on 81 vertices

    It is indeed strongly regular with parameters `(81,20,1,6)`::

        sage: g.is_strongly_regular(parameters=True)    # long time                     # needs sage.modules sage.rings.finite_rings
        (81, 20, 1, 6)

    Its has as eigenvalues `20,2` and `-7`::

        sage: set(g.spectrum()) == {20,2,-7}                                            # needs sage.modules sage.rings.finite_rings
        True
    """
def BuckyBall():
    """
    Return the Bucky Ball graph.

    This graph is a 3-regular 60-vertex planar graph. Its vertices and edges
    correspond precisely to the carbon atoms and bonds in buckminsterfullerene.
    When embedded on a sphere, its 12 pentagon and 20 hexagon faces are arranged
    exactly as the sections of a soccer ball.

    EXAMPLES:

    The Bucky Ball is planar::

        sage: g = graphs.BuckyBall()
        sage: g.is_planar()
        True

    The Bucky Ball can also be created by extracting the 1-skeleton of the Bucky
    Ball polyhedron, but this is much slower::

        sage: # needs sage.geometry.polyhedron sage.groups sage.rings.number_field
        sage: g = polytopes.buckyball().vertex_graph()
        sage: g.remove_loops()
        sage: h = graphs.BuckyBall()
        sage: g.is_isomorphic(h)
        True

    The graph is returned along with an attractive embedding::

        sage: g = graphs.BuckyBall()  # long time
        sage: g.plot(vertex_labels=False, vertex_size=10).show()        # long time, needs sage.plot
    """
def GossetGraph():
    """
    Return the Gosset graph.

    The Gosset graph is the skeleton of the
    :meth:`~sage.geometry.polyhedron.library.Polytopes.Gosset_3_21` polytope. It
    has with 56 vertices and degree 27. For more information, see the
    :wikipedia:`Gosset_graph`.

    EXAMPLES::

        sage: g = graphs.GossetGraph(); g
        Gosset Graph: Graph on 56 vertices
        sage: g.order(), g.size()
        (56, 756)

    TESTS::

        sage: g.is_isomorphic(polytopes.Gosset_3_21().graph())  # not tested (~16s)
        True
    """
def DoubleStarSnark():
    """
    Return the double star snark.

    The double star snark is a 3-regular graph on 30 vertices. See the
    :wikipedia:`Double-star_snark`.

    EXAMPLES::

        sage: g = graphs.DoubleStarSnark()
        sage: g.order()
        30
        sage: g.size()
        45
        sage: g.chromatic_number()
        3
        sage: g.is_hamiltonian()                                                        # needs sage.numerical.mip
        False
        sage: g.automorphism_group().cardinality()                                      # needs sage.groups
        80
        sage: g.show()                                                                  # needs sage.plot
    """
def MeredithGraph():
    """
    Return the Meredith Graph.

    The Meredith Graph is a 4-regular 4-connected non-hamiltonian graph. For
    more information on the Meredith Graph, see the :wikipedia:`Meredith_graph`.

    EXAMPLES::

        sage: g = graphs.MeredithGraph()
        sage: g.is_regular(4)
        True
        sage: g.order()
        70
        sage: g.size()
        140
        sage: g.radius()
        7
        sage: g.diameter()
        8
        sage: g.girth()
        4
        sage: g.chromatic_number()
        3
        sage: g.is_hamiltonian()                # long time                             # needs sage.numerical.mip
        False
    """
def KittellGraph():
    """
    Return the Kittell Graph.

    For more information, see the `Wolfram page about the Kittel Graph
    <http://mathworld.wolfram.com/KittellGraph.html>`_.

    EXAMPLES::

        sage: g = graphs.KittellGraph()
        sage: g.order()
        23
        sage: g.size()
        63
        sage: g.radius()
        3
        sage: g.diameter()
        4
        sage: g.girth()
        3
        sage: g.chromatic_number()
        4
    """
def CameronGraph():
    """
    Return the Cameron graph.

    The Cameron graph is strongly regular with parameters `v = 231, k = 30,
    \\lambda = 9, \\mu = 3`.

    For more information on the Cameron graph, see
    `<https://www.win.tue.nl/~aeb/graphs/Cameron.html>`_.

    EXAMPLES::

        sage: # needs sage.groups
        sage: g = graphs.CameronGraph()
        sage: g.order()
        231
        sage: g.size()
        3465
        sage: g.is_strongly_regular(parameters=True)    # long time
        (231, 30, 9, 3)
    """
def ChvatalGraph():
    """
    Return the Chvatal graph.

    Chvatal graph is one of the few known graphs to satisfy Grunbaum's
    conjecture that for every `m`, `n`, there is an `m`-regular, `m`-chromatic
    graph of girth at least `n`. For more information, see the
    :wikipedia:`Chv%C3%A1tal_graph`.

    EXAMPLES:

    The Chvatal graph has 12 vertices and 24 edges. It is a 4-regular,
    4-chromatic graph with radius 2, diameter 2, and girth 4::

        sage: G = graphs.ChvatalGraph(); G
        Chvatal graph: Graph on 12 vertices
        sage: G.order(); G.size()
        12
        24
        sage: G.degree()
        [4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4]
        sage: G.chromatic_number()
        4
        sage: G.radius(); G.diameter(); G.girth()
        2
        2
        4

    TESTS::

        sage: import networkx                                                           # needs networkx
        sage: G = graphs.ChvatalGraph()
        sage: G.is_isomorphic(Graph(networkx.chvatal_graph()))                          # needs networkx
        True
    """
def ClebschGraph():
    """
    Return the Clebsch graph.

    See the :wikipedia:`Clebsch_graph` for more information.

    EXAMPLES::

        sage: g = graphs.ClebschGraph()
        sage: g.automorphism_group().cardinality()                                      # needs sage.groups
        1920
        sage: g.girth()
        4
        sage: g.chromatic_number()
        4
        sage: g.diameter()
        2
        sage: g.show(figsize=[10, 10])          # long time                             # needs sage.plot
    """
def CoxeterGraph():
    """
    Return the Coxeter graph.

    See the :wikipedia:`Coxeter_graph`.

    EXAMPLES::

        sage: g = graphs.CoxeterGraph()
        sage: g.automorphism_group().cardinality()                                      # needs sage.groups
        336
        sage: g.girth()
        7
        sage: g.chromatic_number()
        3
        sage: g.diameter()
        4
        sage: g.show(figsize=[10, 10])          # long time                             # needs sage.plot
    """
def CubeplexGraph(embedding: str = 'LM'):
    """
    Return the Cubeplex graph.

    The Cubeplex graph is the cubic hamiltonian graph of order 12 that
    corresponds to the graph labeled as `\\Gamma_1` in Fischer and Little
    [FiLi2001]_. It has LCF notation `[-6, -5, -3, -6, 3, 5, -6, -3, 5, -6, -5,
    3]`.

    The Fischer-Little Theorem [FiLi2001]_ may be stated as follows [LM2024]_:

    A near-bipartite graph is non-Pfaffian if and only if it contains one of
    the graphs `K_{3, 3}`, `\\Gamma_1` and `\\Gamma_2` as an `S`-minor.

    Norine and Thomas [NT2007]_ use the term ``Cubeplex`` to describe one of
    the 12-vertex cubic graphs, `\\Gamma_1` and `\\Gamma_2`, as defined by
    Fischer and Little [FiLi2001]_. However, the figure in their paper that
    supposedly provides embeddings for the graphs labeled Cubeplex and Twinplex
    actually shows both embeddings corresponding to Fischer and Little's
    `\\Gamma_1`, which is the Cubeplex graph. Followingly, for
    ``embedding='NT'``, we present only the embedding that is shown by the
    labeling ``Cubeplex`` in the paper of Norine and Thomas [NT2007]_.

    PLOTTING:

    Upon construction, the position dictionary is filled to override
    the spring-layout algorithm. For different values of the parameter
    ``embedding``, the Cubeplex graph is displayed as it is mentioned in the
    respective paper/ book.

    INPUT:

    - ``embedding`` -- string (default: ``'LM'``)

      - ``'LM'`` displays the embedding as shown for `\\Gamma_1` by Lucchesi and
        Murty [LM2024]_

      - ``'FL'`` displays the embedding as shown for `\\Gamma_1` by Fischer and
        Little [FiLi2001]_

      - ``'NT'`` displays the embedding as shown for the ``Cubeplex`` by Norine
        and Thomas [NT2007]_

    OUTPUT:

    - ``G`` -- the Cubeplex graph; note that a :class:`ValueError` is returned
      if ``embedding`` is none of ``'FT'``, ``'NT'`` or ``'LM'``

    EXAMPLES:

    Construct and show the Cubeplex graph::

        sage: g = graphs.CubeplexGraph()
        sage: g.name()
        'Cubeplex Graph'
        sage: g.order()
        12
        sage: g.size()
        18
        sage: g.girth()
        4
        sage: g.diameter()
        3
        sage: g.is_hamiltonian()
        True
        sage: g.crossing_number()
        1
        sage: g.show()                          # long time                             # needs sage.plot

    TESTS:

    Note that all three embeddings refer to the same graph, the Cubeplex graph,
    aka `\\Gamma_1`::

        sage: fl = graphs.CubeplexGraph(embedding='FL')
        sage: nt = graphs.CubeplexGraph(embedding='NT')
        sage: lm = graphs.CubeplexGraph(embedding='LM')
        sage: fl.is_isomorphic(nt) and fl.is_isomorphic(lm)
        True

    The input parameter must be one of 'FL', 'NT' or 'LM'::

        sage: g = graphs.CubeplexGraph(embedding='embedding')
        Traceback (most recent call last):
        ...
        ValueError: parameter 'embedding' must be 'FL', 'NT' or 'LM'

    .. SEEALSO::

        :meth:`~sage.graphs.graph_generators.GraphGenerators.TwinplexGraph`

    AUTHORS:

    - Janmenjaya Panda (2024-08-03)
    """
def DejterGraph():
    """
    Return the Dejter graph.

    The Dejter graph is obtained from the binary 7-cube by deleting a copy of
    the Hamming code of length 7. It is 6-regular, with 112 vertices and 336
    edges. For more information, see the :wikipedia:`Dejter_graph`.

    EXAMPLES::

        sage: g = graphs.DejterGraph(); g                                               # needs sage.rings.finite_rings
        Dejter Graph: Graph on 112 vertices
        sage: g.is_regular(k=6)                                                         # needs sage.rings.finite_rings
        True
        sage: g.girth()                                                                 # needs sage.rings.finite_rings
        4
    """
def DesarguesGraph():
    """
    Return the Desargues graph.

    PLOTTING: The layout chosen is the same as on the cover of [Har1969]_.

    EXAMPLES::

        sage: D = graphs.DesarguesGraph()
        sage: L = graphs.LCFGraph(20,[5,-5,9,-9],5)                                     # needs networkx
        sage: D.is_isomorphic(L)                                                        # needs networkx
        True
        sage: D.show()                          # long time                             # needs sage.plot
    """
def DurerGraph():
    """
    Return the Dürer graph.

    For more information, see the :wikipedia:`D%C3%BCrer_graph`.

    EXAMPLES:

    The Dürer graph is named after Albrecht Dürer. It is a planar graph
    with 12 vertices and 18 edges::

        sage: G = graphs.DurerGraph(); G
        Durer graph: Graph on 12 vertices
        sage: G.is_planar()
        True
        sage: G.order()
        12
        sage: G.size()
        18

    The Dürer graph has chromatic number 3, diameter 4, and girth 3::

        sage: G.chromatic_number()
        3
        sage: G.diameter()
        4
        sage: G.girth()
        3

    Its automorphism group is isomorphic to `D_6`::

        sage: ag = G.automorphism_group()                                               # needs sage.groups
        sage: ag.is_isomorphic(DihedralGroup(6))                                        # needs sage.groups
        True
    """
def DyckGraph():
    """
    Return the Dyck graph.

    For more information, see the `MathWorld article on the Dyck graph
    <http://mathworld.wolfram.com/DyckGraph.html>`_ or the
    :wikipedia:`Dyck_graph`.

    EXAMPLES:

    The Dyck graph was defined by Walther von Dyck in 1881. It has `32` vertices
    and `48` edges, and is a cubic graph (regular of degree `3`)::

        sage: G = graphs.DyckGraph(); G
        Dyck graph: Graph on 32 vertices
        sage: G.order()
        32
        sage: G.size()
        48
        sage: G.is_regular()
        True
        sage: G.is_regular(3)
        True

    It is non-planar and Hamiltonian, as well as bipartite (making it a bicubic
    graph)::

        sage: G.is_planar()
        False
        sage: G.is_hamiltonian()                                                        # needs sage.numerical.mip
        True
        sage: G.is_bipartite()
        True

    It has radius `5`, diameter `5`, and girth `6`::

        sage: G.radius()
        5
        sage: G.diameter()
        5
        sage: G.girth()
        6

    Its chromatic number is `2` and its automorphism group is of order `192`::

        sage: G.chromatic_number()
        2
        sage: G.automorphism_group().cardinality()                                      # needs sage.groups
        192

    It is a non-integral graph as it has irrational eigenvalues::

        sage: G.characteristic_polynomial().factor()                                    # needs sage.libs.pari sage.modules
        (x - 3) * (x + 3) * (x - 1)^9 * (x + 1)^9 * (x^2 - 5)^6

    It is a toroidal graph, and its embedding on a torus is dual to an embedding
    of the Shrikhande graph (:meth:`ShrikhandeGraph
    <GraphGenerators.ShrikhandeGraph>`).
    """
def HortonGraph():
    """
    Return the Horton Graph.

    The Horton graph is a cubic 3-connected non-hamiltonian graph. For more
    information, see the :wikipedia:`Horton_graph`.

    EXAMPLES::

        sage: # needs networkx
        sage: g = graphs.HortonGraph()
        sage: g.order()
        96
        sage: g.size()
        144
        sage: g.radius()
        10
        sage: g.diameter()
        10
        sage: g.girth()
        6
        sage: g.automorphism_group().cardinality()
        96
        sage: g.chromatic_number()
        2
        sage: g.is_hamiltonian()                # not tested (veeeery long)             # needs sage.numerical.mip
        False
    """
def EllinghamHorton54Graph():
    """
    Return the Ellingham-Horton 54-graph.

    For more information, see the :wikipedia:`Ellingham-Horton_graph`.

    EXAMPLES:

    This graph is 3-regular::

        sage: g = graphs.EllinghamHorton54Graph()
        sage: g.is_regular(k=3)
        True

    It is 3-connected and bipartite::

        sage: g.vertex_connectivity()   # not tested - too long
        3
        sage: g.is_bipartite()
        True

    It is not Hamiltonian::

        sage: g.is_hamiltonian()                # not tested                            # needs sage.numerical.mip
        False

    ... and it has a nice drawing ::

        sage: g.show(figsize=[10, 10])  # not tested - too long

    TESTS::

        sage: g.show()                          # long time                             # needs sage.plot
    """
def EllinghamHorton78Graph():
    """
    Return the Ellingham-Horton 78-graph.

    For more information, see the :wikipedia:`Ellingham%E2%80%93Horton_graph`

    EXAMPLES:

    This graph is 3-regular::

        sage: g = graphs.EllinghamHorton78Graph()
        sage: g.is_regular(k=3)
        True

    It is 3-connected and bipartite::

        sage: g.vertex_connectivity()   # not tested (too long)
        3
        sage: g.is_bipartite()
        True

    It is not Hamiltonian::

        sage: g.is_hamiltonian()                # not tested                            # needs sage.numerical.mip
        False

    ... and it has a nice drawing ::

        sage: g.show(figsize=[10,10])   # not tested (too long)

    TESTS::

        sage: g.show(figsize=[10, 10])  # not tested (too long)
    """
def ErreraGraph():
    """
    Return the Errera graph.

    For more information, see the :wikipedia:`Errera_graph`.

    EXAMPLES:

    The Errera graph is named after Alfred Errera. It is a planar graph on 17
    vertices and having 45 edges::

        sage: G = graphs.ErreraGraph(); G
        Errera graph: Graph on 17 vertices
        sage: G.is_planar()
        True
        sage: G.order()
        17
        sage: G.size()
        45

    The Errera graph is Hamiltonian with radius 3, diameter 4, girth 3, and
    chromatic number 4::

        sage: G.is_hamiltonian()                                                        # needs sage.numerical.mip
        True
        sage: G.radius()
        3
        sage: G.diameter()
        4
        sage: G.girth()
        3
        sage: G.chromatic_number()
        4

    Each vertex degree is either 5 or 6. That is, if `f` counts the number of
    vertices of degree 5 and `s` counts the number of vertices of degree 6, then
    `f + s` is equal to the order of the Errera graph::

        sage: D = G.degree_sequence()
        sage: D.count(5) + D.count(6) == G.order()
        True

    The automorphism group of the Errera graph is isomorphic to the dihedral
    group of order 20::

        sage: ag = G.automorphism_group()                                               # needs sage.groups
        sage: ag.is_isomorphic(DihedralGroup(10))                                       # needs sage.groups
        True
    """
def F26AGraph():
    """
    Return the F26A graph.

    The F26A graph is a symmetric bipartite cubic graph with 26 vertices and 39
    edges. For more information, see the :wikipedia:`F26A_graph`.

    EXAMPLES::

        sage: # needs networkx
        sage: g = graphs.F26AGraph(); g
        F26A Graph: Graph on 26 vertices
        sage: g.order(), g.size()
        (26, 39)
        sage: g.automorphism_group().cardinality()
        78
        sage: g.girth()
        6
        sage: g.is_bipartite()
        True
        sage: g.characteristic_polynomial().factor()
        (x - 3) * (x + 3) * (x^4 - 5*x^2 + 3)^6
    """
def FlowerSnark():
    """
    Return a Flower Snark.

    A flower snark has 20 vertices. It is part of the class of biconnected cubic
    graphs with edge chromatic number = 4, known as snarks. (i.e.: the Petersen
    graph). All snarks are not Hamiltonian, non-planar and have Petersen graph
    graph minors. See the :wikipedia:`Flower_snark`.

    PLOTTING: Upon construction, the position dictionary is filled to override
    the spring-layout algorithm. By convention, the nodes are drawn 0-14 on the
    outer circle, and 15-19 in an inner pentagon.

    EXAMPLES: Inspect a flower snark::

        sage: F = graphs.FlowerSnark()
        sage: F
        Flower Snark: Graph on 20 vertices
        sage: F.graph6_string()
        'ShCGHC@?GGg@?@?Gp?K??C?CA?G?_G?Cc'

    Now show it::

        sage: F.show()                          # long time                             # needs sage.plot
    """
def FolkmanGraph():
    """
    Return the Folkman graph.

    See the :wikipedia:`Folkman_graph`.

    EXAMPLES::

        sage: # needs networkx
        sage: g = graphs.FolkmanGraph()
        sage: g.order()
        20
        sage: g.size()
        40
        sage: g.diameter()
        4
        sage: g.girth()
        4
        sage: g.charpoly().factor()
        (x - 4) * (x + 4) * x^10 * (x^2 - 6)^4
        sage: g.chromatic_number()
        2
        sage: g.is_eulerian()
        True
        sage: g.is_hamiltonian()                                                        # needs sage.numerical_mip
        True
        sage: g.is_vertex_transitive()
        False
        sage: g.is_bipartite()
        True
    """
def FosterGraph():
    """
    Return the Foster graph.

    See the :wikipedia:`Foster_graph`.

    EXAMPLES::

        sage: # needs networkx
        sage: g = graphs.FosterGraph()
        sage: g.order()
        90
        sage: g.size()
        135
        sage: g.diameter()
        8
        sage: g.girth()
        10
        sage: g.automorphism_group().cardinality()
        4320
        sage: g.is_hamiltonian()                                                        # needs sage.numerical_mip
        True
    """
def FranklinGraph():
    """
    Return the Franklin graph.

    For more information, see the :wikipedia:`Franklin_graph`.

    EXAMPLES:

    The Franklin graph is named after Philip Franklin. It is a 3-regular graph
    on 12 vertices and having 18 edges::

        sage: G = graphs.FranklinGraph(); G
        Franklin graph: Graph on 12 vertices
        sage: G.is_regular(3)
        True
        sage: G.order()
        12
        sage: G.size()
        18

    The Franklin graph is a Hamiltonian, bipartite graph with radius 3, diameter
    3, and girth 4::

        sage: G.is_hamiltonian()                                                        # needs sage.numerical_mip
        True
        sage: G.is_bipartite()
        True
        sage: G.radius()
        3
        sage: G.diameter()
        3
        sage: G.girth()
        4

    It is a perfect, triangle-free graph having chromatic number 2::

        sage: G.is_perfect()
        True
        sage: G.is_triangle_free()
        True
        sage: G.chromatic_number()
        2
    """
def FruchtGraph():
    """
    Return a Frucht Graph.

    A Frucht graph has 12 nodes and 18 edges. It is the smallest cubic identity
    graph. It is planar and Hamiltonian. See the :wikipedia:`Frucht_graph`.

    PLOTTING: Upon construction, the position dictionary is filled to override
    the spring-layout algorithm. By convention, the first seven nodes are on the
    outer circle, with the next four on an inner circle and the last in the
    center.

    EXAMPLES::

        sage: FRUCHT = graphs.FruchtGraph()
        sage: FRUCHT
        Frucht graph: Graph on 12 vertices
        sage: FRUCHT.graph6_string()
        'KhCKM?_EGK?L'
        sage: (graphs.FruchtGraph()).show()     # long time                             # needs networkx

    TESTS::

        sage: import networkx                                                           # needs networkx
        sage: G = graphs.FruchtGraph()
        sage: G.is_isomorphic(Graph(networkx.frucht_graph()))                           # needs networkx
        True
    """
def GoldnerHararyGraph():
    """
    Return the Goldner-Harary graph.

    For more information, see the :wikipedia:`Goldner%E2%80%93Harary_graph`.

    EXAMPLES:

    The Goldner-Harary graph is named after A. Goldner and Frank Harary. It is
    a planar graph having 11 vertices and 27 edges::

        sage: G = graphs.GoldnerHararyGraph(); G
        Goldner-Harary graph: Graph on 11 vertices
        sage: G.is_planar()
        True
        sage: G.order()
        11
        sage: G.size()
        27

    The Goldner-Harary graph is chordal with radius 2, diameter 2, and girth 3::

        sage: G.is_chordal()
        True
        sage: G.radius()
        2
        sage: G.diameter()
        2
        sage: G.girth()
        3

    Its chromatic number is 4 and its automorphism group is isomorphic to the
    dihedral group `D_6`::

        sage: G.chromatic_number()
        4
        sage: ag = G.automorphism_group()                                               # needs sage.groups
        sage: ag.is_isomorphic(DihedralGroup(6))                                        # needs sage.groups
        True
    """
def GolombGraph():
    """
    Return the Golomb graph.

    See the :wikipedia:`Golomb_graph` for more information.

    EXAMPLES:

    The Golomb graph is a planar and Hamiltonian graph with 10 vertices
    and 18 edges. It has chromatic number 4, diameter 3, radius 2 and
    girth 3. It can be drawn in the plane as a unit distance graph::

        sage: G = graphs.GolombGraph(); G                                               # needs sage.symbolic
        Golomb graph: Graph on 10 vertices
        sage: pos = G.get_pos()                                                         # needs sage.symbolic
        sage: def dist2(u, v):
        ....:     return (u[0]-v[0])**2 + (u[1]-v[1])**2
        sage: all(dist2(pos[u], pos[v]) == 1 for u, v in G.edge_iterator(labels=None))  # needs sage.symbolic
        True
    """
def GrayGraph(embedding: int = 1):
    """
    Return the Gray graph.

    See the :wikipedia:`Gray_graph`.

    INPUT:

    - ``embedding`` -- integer (default: `1`); two embeddings are available,
      and can be selected by setting ``embedding`` to 1 or 2

    EXAMPLES::

        sage: # needs networkx
        sage: g = graphs.GrayGraph()
        sage: g.order()
        54
        sage: g.size()
        81
        sage: g.girth()
        8
        sage: g.diameter()
        6
        sage: g.show(figsize=[10, 10])          # long time                             # needs sage.plot
        sage: graphs.GrayGraph(embedding=2).show(figsize=[10, 10])      # long time, needs sage.plot

    TESTS::

        sage: graphs.GrayGraph(embedding=3)                                             # needs networkx
        Traceback (most recent call last):
        ...
        ValueError: the value of embedding must be 1, 2, or 3
    """
def GrotzschGraph():
    """
    Return the Grötzsch graph.

    The Grötzsch graph is an example of a triangle-free graph with chromatic
    number equal to 4. For more information, see the
    :wikipedia:`Gr%C3%B6tzsch_graph`.

    EXAMPLES:

    The Grötzsch graph is named after Herbert Grötzsch. It is a Hamiltonian
    graph with 11 vertices and 20 edges::

        sage: G = graphs.GrotzschGraph(); G
        Grotzsch graph: Graph on 11 vertices
        sage: G.is_hamiltonian()                                                        # needs sage.numerical.mip
        True
        sage: G.order()
        11
        sage: G.size()
        20

    The Grötzsch graph is triangle-free and having radius 2, diameter 2, and
    girth 4::

        sage: G.is_triangle_free()
        True
        sage: G.radius()
        2
        sage: G.diameter()
        2
        sage: G.girth()
        4

    Its chromatic number is 4 and its automorphism group is isomorphic to the
    dihedral group `D_5`::

        sage: G.chromatic_number()
        4
        sage: ag = G.automorphism_group()                                               # needs sage.groups
        sage: ag.is_isomorphic(DihedralGroup(5))                                        # needs sage.groups
        True
    """
def HeawoodGraph():
    """
    Return a Heawood graph.

    The Heawood graph is a cage graph that has 14 nodes. It is a cubic symmetric
    graph. (See also the Möbius-Kantor graph, :meth:`~MobiusKantorGraph`). It is
    nonplanar and Hamiltonian. It has diameter 3, radius 3, girth 6, and
    chromatic number 2. It is 4-transitive but not 5-transitive.
    See the :wikipedia:`Heawood_graph`.

    PLOTTING: Upon construction, the position dictionary is filled to override
    the spring-layout algorithm. By convention, the nodes are positioned in a
    circular layout with the first node appearing at the top, and then
    continuing counterclockwise.

    EXAMPLES::

        sage: H = graphs.HeawoodGraph()
        sage: H
        Heawood graph: Graph on 14 vertices
        sage: H.graph6_string()
        'MhEGHC@AI?_PC@_G_'
        sage: (graphs.HeawoodGraph()).show()    # long time                             # needs sage.plot

    TESTS::

        sage: import networkx                                                           # needs networkx
        sage: G = graphs.HeawoodGraph()
        sage: G.is_isomorphic(Graph(networkx.heawood_graph()))                          # needs networkx
        True
    """
def HerschelGraph():
    """
    Return the Herschel graph.

    For more information, see the :wikipedia:`Herschel_graph`.

    EXAMPLES:

    The Herschel graph is named after Alexander Stewart Herschel. It is a
    planar, bipartite graph with 11 vertices and 18 edges::

        sage: G = graphs.HerschelGraph(); G
        Herschel graph: Graph on 11 vertices
        sage: G.is_planar()
        True
        sage: G.is_bipartite()
        True
        sage: G.order()
        11
        sage: G.size()
        18

    The Herschel graph is a perfect graph with radius 3, diameter 4, and girth
    4::

        sage: G.is_perfect()
        True
        sage: G.radius()
        3
        sage: G.diameter()
        4
        sage: G.girth()
        4

    Its chromatic number is 2 and its automorphism group is isomorphic to the
    dihedral group `D_6`::

        sage: G.chromatic_number()
        2
        sage: ag = G.automorphism_group()                                               # needs sage.groups
        sage: ag.is_isomorphic(DihedralGroup(6))                                        # needs sage.groups
        True
    """
def GritsenkoGraph():
    """
    Return SRG(65, 32, 15, 16) constructed by Gritsenko.

    We took the adjacency matrix from O. Gritsenko's [Gri2021]_ and extracted
    orbits of the automorphism group on the edges.

    EXAMPLES::

        sage: H = graphs.GritsenkoGraph(); H                                            # needs sage.groups
        Gritsenko strongly regular graph: Graph on 65 vertices
        sage: H.is_strongly_regular(parameters=True)                                    # needs sage.groups
        (65, 32, 15, 16)
    """
def HigmanSimsGraph(relabel: bool = True):
    '''
    Return the Higman-Sims graph.

    The Higman-Sims graph is a remarkable strongly regular graph of degree 22 on
    100 vertices.  For example, it can be split into two sets of 50 vertices
    each, so that each half induces a subgraph isomorphic to the
    Hoffman-Singleton graph (:meth:`~HoffmanSingletonGraph`). This can be done
    in 352 ways (see `Higman-Sims graph
    <https://www.win.tue.nl/~aeb/graphs/Higman-Sims.html>`_ by Andries
    E. Brouwer, accessed 24 October 2009.)

    Its most famous property is that the automorphism group has an index 2
    subgroup which is one of the 26 sporadic groups [HS1968]_.

    The construction used here follows [Haf2004]_.

    See also the :wikipedia:`Higman–Sims_graph`.

    INPUT:

    - ``relabel`` -- boolean (default: ``True``); whether to relabel the
      vertices with consecutive integers. If ``False`` the labels are strings
      that are three digits long. "xyz" means the vertex is in group `x` (zero
      through three), pentagon or pentagram `y` (zero through four), and is
      vertex `z` (zero through four) of that pentagon or pentagram. See
      [Haf2004]_ for more.

    OUTPUT: the Higman-Sims graph

    EXAMPLES:

    A split into the first 50 and last 50 vertices will induce two copies of the
    Hoffman-Singleton graph, and we illustrate another such split, which is
    obvious based on the construction used::

        sage: H = graphs.HigmanSimsGraph()
        sage: A = H.subgraph(range(0,50))
        sage: B = H.subgraph(range(50,100))
        sage: K = graphs.HoffmanSingletonGraph()
        sage: K.is_isomorphic(A) and K.is_isomorphic(B)
        True
        sage: C = H.subgraph(range(25,75))
        sage: D = H.subgraph(list(range(0,25))+list(range(75,100)))
        sage: K.is_isomorphic(C) and K.is_isomorphic(D)
        True

    The automorphism group contains only one nontrivial proper normal subgroup,
    which is of index 2 and is simple.  It is known as the Higman-Sims group::

        sage: H = graphs.HigmanSimsGraph()
        sage: G = H.automorphism_group()                                                # needs sage.groups
        sage: g = G.order(); g                                                          # needs sage.groups
        88704000
        sage: K = G.normal_subgroups()[1]                                               # needs sage.groups
        sage: K.is_simple()                                                             # needs sage.groups
        True
        sage: g//K.order()                                                              # needs sage.groups
        2

    AUTHOR:

        - Rob Beezer (2009-10-24)
    '''
def HoffmanSingletonGraph():
    """
    Return the Hoffman-Singleton graph.

    The Hoffman-Singleton graph is the Moore graph of degree 7, diameter 2 and
    girth 5. The Hoffman-Singleton theorem states that any Moore graph with
    girth 5 must have degree 2, 3, 7 or 57. The first three respectively are the
    pentagon, the Petersen graph, and the Hoffman-Singleton graph. The existence
    of a Moore graph with girth 5 and degree 57 is still open.

    A Moore graph is a graph with diameter `d` and girth `2d + 1`. This implies
    that the graph is regular, and distance regular.

    For more details, see [GR2001]_ and the
    :wikipedia:`Hoffman–Singleton_graph`.

    PLOTTING: Upon construction, the position dictionary is filled to override
    the spring-layout algorithm. A novel algorithm written by Tom Boothby gives
    a random layout which is pleasing to the eye.

    EXAMPLES::

        sage: HS = graphs.HoffmanSingletonGraph()
        sage: Set(HS.degree())
        {7}
        sage: HS.girth()
        5
        sage: HS.diameter()
        2
        sage: HS.num_verts()
        50

    Note that you get a different layout each time you create the graph.  ::

        sage: HS.layout()[1]  # random
        (-0.844..., 0.535...)
        sage: HS = graphs.HoffmanSingletonGraph()
        sage: HS.layout()[1]  # random
        (-0.904..., 0.425...)
    """
def HoffmanGraph():
    """
    Return the Hoffman Graph.

    See the :wikipedia:`Hoffman_graph`.

    EXAMPLES::

        sage: g = graphs.HoffmanGraph()
        sage: g.is_bipartite()
        True
        sage: g.is_hamiltonian()                # long time                             # needs sage.numerical.mip
        True
        sage: g.radius()
        3
        sage: g.diameter()
        4
        sage: g.automorphism_group().cardinality()                                      # needs sage.groups
        48
    """
def HoltGraph():
    """
    Return the Holt graph (also called the Doyle graph).

    See the :wikipedia:`Holt_graph`.

    EXAMPLES::

        sage: g = graphs.HoltGraph();g
        Holt graph: Graph on 27 vertices
        sage: g.is_regular()
        True
        sage: g.is_vertex_transitive()                                                  # needs sage.groups
        True
        sage: g.chromatic_number()
        3
        sage: g.is_hamiltonian()                # long time                             # needs sage.numerical.mip
        True
        sage: g.radius()
        3
        sage: g.diameter()
        3
        sage: g.girth()
        5
        sage: g.automorphism_group().cardinality()                                      # needs sage.groups
        54
    """
def KrackhardtKiteGraph():
    """
    Return a Krackhardt kite graph with 10 nodes.

    The Krackhardt kite graph was originally developed by David Krackhardt for
    the purpose of studying social networks (see [Kre2002]_ and
    the :wikipedia:`Krackhardt_kite_graph`). It is used to show the distinction
    between degree centrality, betweenness centrality, and closeness
    centrality. For more information read the plotting section below in
    conjunction with the example.

    PLOTTING: Upon construction, the position dictionary is filled to override
    the spring-layout algorithm. By convention, the graph is drawn left to
    right, in top to bottom row sequence of [2, 3, 2, 1, 1, 1] nodes on each
    row. This places the fourth node (3) in the center of the kite, with the
    highest degree. But the fourth node only connects nodes that are otherwise
    connected, or those in its clique (i.e.: Degree Centrality). The eighth (7)
    node is where the kite meets the tail. It has degree = 3, less than the
    average, but is the only connection between the kite and tail (i.e.:
    Betweenness Centrality). The sixth and seventh nodes (5 and 6) are drawn in
    the third row and have degree = 5. These nodes have the shortest path to all
    other nodes in the graph (i.e.: Closeness Centrality).  Please execute the
    example for visualization.

    EXAMPLES:

    Construct and show a Krackhardt kite graph ::

        sage: g = graphs.KrackhardtKiteGraph()
        sage: g.show()                          # long time                             # needs sage.plot

    TESTS::

        sage: import networkx                                                           # needs networkx
        sage: G = graphs.KrackhardtKiteGraph()
        sage: G.is_isomorphic(Graph(networkx.krackhardt_kite_graph()))                  # needs networkx
        True
    """
def Klein3RegularGraph():
    """
    Return the Klein 3-regular graph.

    The cubic Klein graph has 56 vertices and can be embedded on a
    surface of genus 3. It is the dual of
    :meth:`~sage.graphs.graph_generators.GraphGenerators.Klein7RegularGraph`.
    For more information, see the :wikipedia:`Klein_graphs`.

    EXAMPLES::

        sage: g = graphs.Klein3RegularGraph(); g
        Klein 3-regular Graph: Graph on 56 vertices
        sage: g.order(), g.size()
        (56, 84)
        sage: g.girth()
        7
        sage: g.automorphism_group().cardinality()                                      # needs sage.groups
        336
        sage: g.chromatic_number()
        3
    """
def Klein7RegularGraph():
    """
    Return the Klein 7-regular graph.

    The 7-valent Klein graph has 24 vertices and can be embedded on a surface of
    genus 3. It is the dual of
    :meth:`~sage.graphs.graph_generators.GraphGenerators.Klein3RegularGraph`.
    For more information, see the :wikipedia:`Klein_graphs`.

    EXAMPLES::

        sage: g = graphs.Klein7RegularGraph(); g
        Klein 7-regular Graph: Graph on 24 vertices
        sage: g.order(), g.size()
        (24, 84)
        sage: g.girth()
        3
        sage: g.automorphism_group().cardinality()                                      # needs sage.groups
        336
        sage: g.chromatic_number()
        4
    """
def LocalMcLaughlinGraph():
    """
    Return the local McLaughlin graph.

    The local McLaughlin graph is a strongly regular graph with parameters
    `(162,56,10,24)`. It can be obtained from
    :meth:`~sage.graphs.graph_generators.GraphGenerators.McLaughlinGraph` by
    considering the stabilizer of a point: one of its orbits has cardinality
    162.

    EXAMPLES::

        sage: g = graphs.LocalMcLaughlinGraph(); g      # long time, optional - gap_package_design
        Local McLaughlin Graph: Graph on 162 vertices
        sage: g.is_strongly_regular(parameters=True)    # long time, optional - gap_package_design
        (162, 56, 10, 24)
    """
def LjubljanaGraph(embedding: int = 1):
    """
    Return the Ljubljana Graph.

    The Ljubljana graph is a bipartite 3-regular graph on 112 vertices and 168
    edges. It is not vertex-transitive as it has two orbits which are also
    independent sets of size 56. See the :wikipedia:`Ljubljana_graph`.

    The default embedding is obtained from the Heawood graph.

    INPUT:

    - ``embedding`` -- integer (default: `1`); two embeddings are available,
      and can be selected by setting ``embedding`` to 1 or 2

    EXAMPLES::

        sage: # needs networkx
        sage: g = graphs.LjubljanaGraph()
        sage: g.order()
        112
        sage: g.size()
        168
        sage: g.girth()
        10
        sage: g.diameter()
        8
        sage: g.show(figsize=[10, 10])          # long time                             # needs sage.plot
        sage: graphs.LjubljanaGraph(embedding=2).show(figsize=[10, 10])         # long time, needs sage.plot

    TESTS::

        sage: graphs.LjubljanaGraph(embedding=3)                                        # needs networkx
        Traceback (most recent call last):
        ...
        ValueError: the value of embedding must be 1 or 2
    """
def LivingstoneGraph():
    """
    Return the Livingstone Graph.

    The Livingstone graph is a distance-transitive graph on 266 vertices whose
    automorphism group is the :class:`J1 group
    <sage.groups.perm_gps.permgroup_named.JankoGroup>`. For more information,
    see the :wikipedia:`Livingstone_graph`.

    EXAMPLES::

        sage: # optional - internet
        sage: g = graphs.LivingstoneGraph()
        sage: g.order()
        266
        sage: g.size()
        1463
        sage: g.girth()
        5
        sage: g.is_vertex_transitive()
        True
        sage: g.is_distance_regular()
        True
    """
def M22Graph():
    """
    Return the M22 graph.

    The `M_{22}` graph is the unique strongly regular graph with parameters
    `v = 77, k = 16, \\lambda = 0, \\mu = 4`.

    For more information on the `M_{22}` graph, see
    `<https://www.win.tue.nl/~aeb/graphs/M22.html>`_.

    EXAMPLES::

        sage: # needs sage.groups
        sage: g = graphs.M22Graph()
        sage: g.order()
        77
        sage: g.size()
        616
        sage: g.is_strongly_regular(parameters=True)
        (77, 16, 0, 4)
    """
def MarkstroemGraph():
    """
    Return the Markström Graph.

    The Markström Graph is a cubic planar graph with no cycles of length 4 nor
    8, but containing cycles of length 16. For more information, see the
    `Wolfram page about the Markström Graph
    <http://mathworld.wolfram.com/MarkstroemGraph.html>`_.

    EXAMPLES::

        sage: g = graphs.MarkstroemGraph()
        sage: g.order()
        24
        sage: g.size()
        36
        sage: g.is_planar()
        True
        sage: g.is_regular(3)
        True
        sage: g.subgraph_search(graphs.CycleGraph(4)) is None                           # needs sage.modules
        True
        sage: g.subgraph_search(graphs.CycleGraph(8)) is None                           # needs sage.modules
        True
        sage: g.subgraph_search(graphs.CycleGraph(16))                                  # needs sage.modules
        Subgraph of (Markstroem Graph): Graph on 16 vertices
    """
def McGeeGraph(embedding: int = 2):
    """
    Return the McGee Graph.

    See the :wikipedia:`McGee_graph`.

    INPUT:

    - ``embedding`` -- integer (default: `2`); two embeddings are available,
      and can be selected by setting ``embedding`` to 1 or 2

    EXAMPLES::

        sage: # needs networkx
        sage: g = graphs.McGeeGraph()
        sage: g.order()
        24
        sage: g.size()
        36
        sage: g.girth()
        7
        sage: g.diameter()
        4
        sage: g.show()                                                                  # needs sage.plot
        sage: graphs.McGeeGraph(embedding=1).show()     # long time                     # needs sage.plot

    TESTS::

        sage: graphs.McGeeGraph(embedding=3)                                            # needs networkx
        Traceback (most recent call last):
        ...
        ValueError: the value of embedding must be 1 or 2
    """
def McLaughlinGraph():
    """
    Return the McLaughlin Graph.

    The McLaughlin Graph is the unique strongly regular graph of parameters
    `(275, 112, 30, 56)`.

    For more information on the McLaughlin Graph, see its web page on `Andries
    Brouwer's website <https://www.win.tue.nl/~aeb/graphs/McL.html>`_ which
    gives the definition that this method implements.

    .. NOTE::

        To create this graph you must have the gap_packages spkg installed.

    EXAMPLES::

        sage: g = graphs.McLaughlinGraph()              # optional - gap_package_design
        sage: g.is_strongly_regular(parameters=True)    # optional - gap_package_design
        (275, 112, 30, 56)
        sage: set(g.spectrum()) == {112, 2, -28}        # optional - gap_package_design
        True
    """
def MoebiusKantorGraph():
    """
    Return a Möbius-Kantor Graph.

    A Möbius-Kantor graph is a cubic symmetric graph. (See also the Heawood
    graph). It has 16 nodes and 24 edges. It is nonplanar and Hamiltonian. It
    has diameter 4, girth 6, and chromatic number 2. It is identical to the
    Generalized Petersen graph, P[8, 3].

    For more details, see `Möbius-Kantor Graph - from Wolfram MathWorld
    <http://mathworld.wolfram.com/Moebius-KantorGraph.html>`_.

    PLOTTING: See the plotting section for the generalized Petersen graphs.

    EXAMPLES::

        sage: MK = graphs.MoebiusKantorGraph()
        sage: MK
        Moebius-Kantor Graph: Graph on 16 vertices
        sage: MK.graph6_string()
        'OhCGKE?O@?ACAC@I?Q_AS'
        sage: (graphs.MoebiusKantorGraph()).show()      # long time                     # needs sage.plot
    """
def MoserSpindle():
    """
    Return the Moser spindle.

    For more information, see the :wikipedia:`Moser_spindle`.

    EXAMPLES:

    The Moser spindle is a planar graph having 7 vertices and 11 edges::

        sage: # needs sage.symbolic
        sage: G = graphs.MoserSpindle(); G
        Moser spindle: Graph on 7 vertices
        sage: G.is_planar()
        True
        sage: G.order()
        7
        sage: G.size()
        11

    It is a Hamiltonian graph with radius 2, diameter 2, and girth 3::

        sage: # needs sage.symbolic
        sage: G.is_hamiltonian()                                                        # needs sage.numerical.mip
        True
        sage: G.radius()
        2
        sage: G.diameter()
        2
        sage: G.girth()
        3

    The Moser spindle can be drawn in the plane as a unit distance graph,
    has chromatic number 4, and its automorphism group is isomorphic to
    the dihedral group `D_4`::

        sage: # needs sage.symbolic
        sage: pos = G.get_pos()
        sage: all(sum((ui-vi)**2 for ui, vi in zip(pos[u], pos[v])) == 1
        ....:         for u, v in G.edge_iterator(labels=None))
        True
        sage: G.chromatic_number()
        4
        sage: ag = G.automorphism_group()
        sage: ag.is_isomorphic(DihedralGroup(4))
        True
    """
def MurtyGraph():
    """
    Return the Murty graph.

    Consider the complete bipartite graph `K_{3, 3}`. There is a set of three
    black vertices and a set of three white vertices. Now, consider splicing
    the complete graph `K_4` with one of the black vertices, this generates the
    graph `K_4 \\odot K_{3, 3}`. The Murty graph is obtained from
    `K_4 \\odot K_{3, 3}` with the addition of an edge joining the remaining two
    black vertices. The Murty graph is free of conformal bicycles; in
    other words, the Murty graph is an example of a graph that is Birkhoff-von
    Neumann as well as PM-compact.

    This is the smallest brick that is Birkhoff-von Neumann, aka a solid
    brick, but is not odd-intercyclic. It is in this context that
    Prof. U.S.R. Murty first stumbled upon this graph, and it also appears in
    the work of Carvalho, Lucchesi, and Murty [CLM2006]_.

    PLOTTING:

    Upon construction, the position dictionary is filled to override
    the spring-layout algorithm. By convention, the Murty graph is
    displayed as mentioned in the paper [CKWL2019]_, with the first two
    (noncubic) vertices on the top row, the second three vertices (that form a
    stable set) in the middle row, and the remaining three vertices (that form
    a triangle) at the bottom.

    OUTPUT:

    - ``G`` -- the Murty graph

    EXAMPLES:

    Construct and show the Murty graph::

        sage: g = graphs.MurtyGraph()
        sage: g.name()
        'Murty Graph'
        sage: g.order()
        8
        sage: g.size()
        13
        sage: g.girth()
        3
        sage: g.diameter()
        2
        sage: g.is_hamiltonian()
        True
        sage: g.show()                          # long time                             # needs sage.plot

    REFERENCES:

    - [CKWL2019]_
    - [CLM2006]_
    - [LM2024]_

    AUTHORS:

    - Janmenjaya Panda (2024-08-03)
    """
def NauruGraph(embedding: int = 2):
    """
    Return the Nauru Graph.

    See the :wikipedia:`Nauru_graph`.

    INPUT:

    - ``embedding`` -- integer (default: `2`); two embeddings are available,
      and can be selected by setting ``embedding`` to 1 or 2

    EXAMPLES::

        sage: g = graphs.NauruGraph()
        sage: g.order()
        24
        sage: g.size()
        36
        sage: g.girth()
        6
        sage: g.diameter()
        4
        sage: g.show()                                                                  # needs sage.plot
        sage: graphs.NauruGraph(embedding=1).show()     # long time                     # needs sage.plot

    TESTS::

        sage: graphs.NauruGraph(embedding=3)
        Traceback (most recent call last):
        ...
        ValueError: the value of embedding must be 1 or 2
        sage: graphs.NauruGraph(embedding=1).is_isomorphic(g)                           # needs networkx
        True
    """
def PappusGraph():
    """
    Return the Pappus graph, a graph on 18 vertices.

    The Pappus graph is cubic, symmetric, and distance-regular.

    EXAMPLES::

        sage: G = graphs.PappusGraph()
        sage: G.show()                          # long time                             # needs sage.plot
        sage: L = graphs.LCFGraph(18, [5,7,-7,7,-7,-5], 3)                              # needs networkx
        sage: L.show()                          # long time                             # needs networkx sage.plot
        sage: G.is_isomorphic(L)                                                        # needs networkx
        True
    """
def PoussinGraph():
    """
    Return the Poussin Graph.

    For more information on the Poussin Graph, see its corresponding `Wolfram
    page <http://mathworld.wolfram.com/PoussinGraph.html>`_.

    EXAMPLES::

        sage: g = graphs.PoussinGraph()
        sage: g.order()
        15
        sage: g.is_planar()
        True
    """
def PetersenGraph():
    """
    Return the Petersen Graph.

    The Petersen Graph is a named graph that consists of 10 vertices and 15
    edges, usually drawn as a five-point star embedded in a pentagon.

    The Petersen Graph is a common counterexample. For example, it is not
    Hamiltonian.

    PLOTTING: See the plotting section for the generalized Petersen graphs.

    EXAMPLES: We compare below the Petersen graph with the default spring-layout
    versus a planned position dictionary of `(x, y)` tuples::

        sage: petersen_spring = Graph({0:[1,4,5], 1:[0,2,6], 2:[1,3,7],
        ....:                          3:[2,4,8], 4:[0,3,9], 5:[0,7,8],
        ....:                          6:[1,8,9], 7:[2,5,9], 8:[3,5,6],
        ....:                          9:[4,6,7]})
        sage: petersen_spring.show()            # long time                             # needs sage.plot
        sage: petersen_database = graphs.PetersenGraph()
        sage: petersen_database.show()          # long time                             # needs sage.plot
    """
def PerkelGraph():
    """
    Return the Perkel Graph.

    The Perkel Graph is a 6-regular graph with `57` vertices and `171` edges. It
    is the unique distance-regular graph with intersection array
    `(6,5,2;1,1,3)`. For more information, see the :wikipedia:`Perkel_graph` or
    https://www.win.tue.nl/~aeb/graphs/Perkel.html.

    EXAMPLES::

        sage: g = graphs.PerkelGraph(); g
        Perkel Graph: Graph on 57 vertices
        sage: g.is_distance_regular(parameters=True)
        ([6, 5, 2, None], [None, 1, 1, 3])
    """
def RobertsonGraph():
    """
    Return the Robertson graph.

    See the :wikipedia:`Robertson_graph`.

    EXAMPLES::

        sage: # needs networkx
        sage: g = graphs.RobertsonGraph()
        sage: g.order()
        19
        sage: g.size()
        38
        sage: g.diameter()
        3
        sage: g.girth()
        5
        sage: g.charpoly().factor()
        (x - 4) * (x - 1)^2 * (x^2 + x - 5) * (x^2 + x - 1)
         * (x^2 - 3)^2 * (x^2 + x - 4)^2 * (x^2 + x - 3)^2
        sage: g.chromatic_number()
        3
        sage: g.is_hamiltonian()                                                        # needs sage.numerical.mip
        True
        sage: g.is_vertex_transitive()
        False
    """
def SchlaefliGraph():
    """
    Return the Schläfli graph.

    The Schläfli graph is the only strongly regular graphs of parameters
    `(27,16,10,8)` (see [GR2001]_).

    For more information, see the :wikipedia:`Schläfli_graph`.

    .. SEEALSO::

        :meth:`Graph.is_strongly_regular` -- tests whether a graph is strongly
        regular and/or returns its parameters.

    .. TODO::

        Find a beautiful layout for this beautiful graph.

    EXAMPLES:

    Checking that the method actually returns the Schläfli graph::

        sage: S = graphs.SchlaefliGraph()
        sage: S.is_strongly_regular(parameters=True)
        (27, 16, 10, 8)

    The graph is vertex-transitive::

        sage: S.is_vertex_transitive()                                                  # needs sage.groups
        True

    The neighborhood of each vertex is isomorphic to the complement of the
    Clebsch graph::

        sage: neighborhood = S.subgraph(vertices=S.neighbors(0))
        sage: graphs.ClebschGraph().complement().is_isomorphic(neighborhood)
        True
    """
def ShrikhandeGraph():
    """
    Return the Shrikhande graph.

    For more information, see the `MathWorld article on the Shrikhande graph
    <http://mathworld.wolfram.com/ShrikhandeGraph.html>`_ or the
    :wikipedia:`Shrikhande_graph`.

    .. SEEALSO::

        :meth:`Graph.is_strongly_regular` -- tests whether a graph is strongly
        regular and/or returns its parameters.

    EXAMPLES:

    The Shrikhande graph was defined by S. S. Shrikhande in 1959. It has `16`
    vertices and `48` edges, and is strongly regular of degree `6` with
    parameters `(2,2)`::

        sage: G = graphs.ShrikhandeGraph(); G
        Shrikhande graph: Graph on 16 vertices
        sage: G.order()
        16
        sage: G.size()
        48
        sage: G.is_regular(6)
        True
        sage: set([ len([x for x in G.neighbors(i) if x in G.neighbors(j)])
        ....:     for i in range(G.order())
        ....:     for j in range(i) ])
        {2}

    It is non-planar, and both Hamiltonian and Eulerian::

        sage: G.is_planar()
        False
        sage: G.is_hamiltonian()                                                        # needs sage.numerical.mip
        True
        sage: G.is_eulerian()
        True

    It has radius `2`, diameter `2`, and girth `3`::

        sage: G.radius()
        2
        sage: G.diameter()
        2
        sage: G.girth()
        3

    Its chromatic number is `4` and its automorphism group is of order `192`::

        sage: G.chromatic_number()
        4
        sage: G.automorphism_group().cardinality()                                      # needs sage.groups
        192

    It is an integral graph since it has only integral eigenvalues::

        sage: G.characteristic_polynomial().factor()                                    # needs sage.libs.pari sage.modules
        (x - 6) * (x - 2)^6 * (x + 2)^9

    It is a toroidal graph, and its embedding on a torus is dual to an
    embedding of the Dyck graph (:meth:`DyckGraph <GraphGenerators.DyckGraph>`).
    """
def SylvesterGraph():
    """
    Return the Sylvester Graph.

    This graph is obtained from the Hoffman Singleton graph by considering the
    graph induced by the vertices at distance two from the vertices of an (any)
    edge.

    For more information on the Sylvester graph, see
    `<https://www.win.tue.nl/~aeb/graphs/Sylvester.html>`_.

    .. SEEALSO::

        * :meth:`~sage.graphs.graph_generators.GraphGenerators.HoffmanSingletonGraph`.

    EXAMPLES::

        sage: g = graphs.SylvesterGraph(); g
        Sylvester Graph: Graph on 36 vertices
        sage: g.order()
        36
        sage: g.size()
        90
        sage: g.is_regular(k=5)
        True
    """
def SimsGewirtzGraph():
    """
    Return the Sims-Gewirtz Graph.

    This graph is obtained from the Higman Sims graph by considering the graph
    induced by the vertices at distance two from the vertices of an (any)
    edge. It is the only strongly regular graph with parameters `v = 56`,
    `k = 10`, `\\lambda = 0`, `\\mu = 2`

    For more information on the Sylvester graph, see
    `<https://www.win.tue.nl/~aeb/graphs/Sims-Gewirtz.html>`_ or its
    :wikipedia:`Gewirtz_graph`.

    .. SEEALSO::

        * :meth:`~sage.graphs.graph_generators.GraphGenerators.HigmanSimsGraph`.

    EXAMPLES::

        sage: g = graphs.SimsGewirtzGraph(); g
        Sims-Gewirtz Graph: Graph on 56 vertices
        sage: g.order()
        56
        sage: g.size()
        280
        sage: g.is_strongly_regular(parameters = True)
        (56, 10, 0, 2)
    """
def SousselierGraph():
    """
    Return the Sousselier Graph.

    The Sousselier graph is a hypohamiltonian graph on 16 vertices and 27
    edges. For more information, see :wikipedia:`Sousselier_graph` or
    the corresponding French
    `Wikipedia page <https://fr.wikipedia.org/wiki/Graphe_de_Sousselier>`_.

    EXAMPLES::

        sage: g = graphs.SousselierGraph()
        sage: g.order()
        16
        sage: g.size()
        27
        sage: g.radius()
        2
        sage: g.diameter()
        3
        sage: g.automorphism_group().cardinality()                                      # needs sage.groups
        2
        sage: g.is_hamiltonian()                                                        # needs sage.numerical.mip
        False
        sage: g.delete_vertex(g.random_vertex())
        sage: g.is_hamiltonian()                                                        # needs sage.numerical.mip
        True
    """
def SzekeresSnarkGraph():
    """
    Return the Szekeres Snark Graph.

    The Szekeres graph is a snark with 50 vertices and 75 edges. For more
    information on this graph, see the :wikipedia:`Szekeres_snark`.

    EXAMPLES::

        sage: g = graphs.SzekeresSnarkGraph()
        sage: g.order()
        50
        sage: g.size()
        75
        sage: g.chromatic_number()
        3
    """
def ThomsenGraph():
    """
    Return the Thomsen Graph.

    The Thomsen Graph is actually a complete bipartite graph with `(n1, n2) =
    (3, 3)`. It is also called the Utility graph.

    PLOTTING: See CompleteBipartiteGraph.

    EXAMPLES::

        sage: T = graphs.ThomsenGraph()
        sage: T
        Thomsen graph: Graph on 6 vertices
        sage: T.graph6_string()
        'EFz_'
        sage: (graphs.ThomsenGraph()).show()    # long time                             # needs sage.plot
    """
def TietzeGraph():
    """
    Return the Tietze Graph.

    For more information on the Tietze Graph, see the
    :wikipedia:`Tietze%27s_graph`.

    EXAMPLES::

        sage: g = graphs.TietzeGraph()
        sage: g.order()
        12
        sage: g.size()
        18
        sage: g.diameter()
        3
        sage: g.girth()
        3
        sage: g.automorphism_group().cardinality()                                      # needs sage.groups
        12
        sage: g.automorphism_group().is_isomorphic(groups.permutation.Dihedral(6))      # needs sage.groups
        True
    """
def TricornGraph():
    """
    Return the Tricorn graph.

    The Tricorn graph is obtained by splicing a complete graph `K_4` with the
    the triangular circular ladder graph `\\overline{C_6}`. (Note that this
    generates a unique graph as both of the graphs `K_4` and `\\overline{C_6}`
    are vertex-transitive). It is a nonsolid brick. This matching covered graph
    is one of the ten extremal cubic bricks. (A matching covered graph `G` is
    *extremal* if `\\Phi(G) = dim(\\mathcal{Lin}(G))`, where `\\Phi(G)` denotes
    the number of perfect matchings of `G`, and `dim(\\mathcal{Lin}(G))` stands
    for the dimension of the linear space of `G`).

    The Tricorn graph has no removable doubletons and has precisely three
    removable edges. The wheel graph `W_5` and the complete graph `K_4` are
    matching minors of the Tricorn graph.

    As per a theorem of Lovász [Lov1983]_, each non bipartite matching covered
    graph has a conformal subgraph which is either a bi-subdivision of `K_4` or
    of `\\overline{C_6}` or both. In their paper, Kothari and Murty [KM2015]_
    characterized those planar bricks that are free of `\\overline{C_6}` (that
    is, the planar bricks that do not contain a bi-subdivision of
    `\\overline{C_6}` as a conformal subgraph). Besides two infinite families of
    matching covered graphs (odd wheel graphs and staircase graphs of order
    *4k*), the Tricorn graph is the only exception brick that is simple, planar
    and free of `\\overline{C_6}`.

    PLOTTING:

    Upon construction, the position dictionary is filled to override
    the spring-layout algorithm. By convention, the Tricorn graph is
    displayed as mentioned in the book [LM2024]_, with the central vertex being
    the `0`-th one. Rest of the nine vertices are shown in groups of three,
    one on the top, rest two on the bottom left and on the bottom right
    corners respectively.

    OUTPUT:

    - ``G`` -- the Tricorn graph

    EXAMPLES:

    Construct and show the Tricorn graph; note that the edges `(2, 3)`,
    `(5, 6)` and `(8, 9)` are the only removable edges of the Tricorn
    graph::

        sage: g = graphs.TricornGraph()
        sage: g.name()
        'Tricorn Graph'
        sage: g.order()
        10
        sage: g.size()
        15
        sage: g.girth()
        3
        sage: g.diameter()
        3
        sage: g.is_hamiltonian()
        True
        sage: g.show()                          # long time                             # needs sage.plot

    REFERENCES:

    - [KM2015]_
    - [LM2024]_
    - [Lov1983]_

    AUTHORS:

    - Janmenjaya Panda (2024-08-02)
    """
def TruncatedIcosidodecahedralGraph():
    """
    Return the truncated icosidodecahedron.

    The truncated icosidodecahedron is an Archimedean solid with 30 square
    faces, 20 regular hexagonal faces, 12 regular decagonal faces, 120 vertices
    and 180 edges. For more information, see the
    :wikipedia:`Truncated_icosidodecahedron`.

    EXAMPLES:

    Unfortunately, this graph can not be constructed currently, due to numerical issues::

        sage: g = graphs.TruncatedIcosidodecahedralGraph(); g                           # needs sage.geometry.polyhedron sage.groups sage.rings.number_field
        Traceback (most recent call last):
        ...
        ValueError: *Error: Numerical inconsistency is found.  Use the GMP exact arithmetic.
        sage: g.order(), g.size()               # not tested                            # needs sage.geometry.polyhedron sage.groups sage.rings.number_field
        (120, 180)
    """
def TruncatedTetrahedralGraph():
    """
    Return the truncated tetrahedron.

    The truncated tetrahedron is an Archimedean solid with 12 vertices and 18
    edges. For more information, see the :wikipedia:`Truncated_tetrahedron`.

    EXAMPLES::

        sage: g = graphs.TruncatedTetrahedralGraph(); g
        Truncated Tetrahedron: Graph on 12 vertices
        sage: g.order(), g.size()
        (12, 18)
        sage: g.is_isomorphic(polytopes.simplex(3).truncation().graph())                # needs sage.geometry.polyhedron
        True
    """
def Tutte12Cage():
    """
    Return the Tutte 12-Cage.

    See the :wikipedia:`Tutte_12-cage`.

    EXAMPLES::

        sage: # needs networkx
        sage: g = graphs.Tutte12Cage()
        sage: g.order()
        126
        sage: g.size()
        189
        sage: g.girth()
        12
        sage: g.diameter()
        6
        sage: g.show()                                                                  # needs sage.plot
    """
def TutteCoxeterGraph(embedding: int = 2):
    """
    Return the Tutte-Coxeter graph.

    See the :wikipedia:`Tutte-Coxeter_graph`.

    INPUT:

    - ``embedding`` -- integer (default: `2`); two embeddings are available,
      and can be selected by setting ``embedding`` to 1 or 2

    EXAMPLES::

        sage: # needs networkx
        sage: g = graphs.TutteCoxeterGraph()
        sage: g.order()
        30
        sage: g.size()
        45
        sage: g.girth()
        8
        sage: g.diameter()
        4
        sage: g.show()                                                                  # needs sage.plot
        sage: graphs.TutteCoxeterGraph(embedding=1).show()      # long time             # needs sage.plot

    TESTS::

        sage: graphs.TutteCoxeterGraph(embedding=3)                                     # needs networkx
        Traceback (most recent call last):
        ...
        ValueError: the value of embedding must be 1 or 2
    """
def TutteGraph():
    """
    Return the Tutte Graph.

    The Tutte graph is a 3-regular, 3-connected, and planar non-hamiltonian
    graph. For more information on the Tutte Graph, see the
    :wikipedia:`Tutte_graph`.

    EXAMPLES::

        sage: g = graphs.TutteGraph()
        sage: g.order()
        46
        sage: g.size()
        69
        sage: g.is_planar()
        True
        sage: g.vertex_connectivity()           # long time                             # needs sage.numerical.mip
        3
        sage: g.girth()
        4
        sage: g.automorphism_group().cardinality()                                      # needs sage.groups
        3
        sage: g.is_hamiltonian()                                                        # needs sage.numerical.mip
        False
    """
def TwinplexGraph(embedding: str = 'LM'):
    """
    Return the Twinplex graph.

    The Twinplex graph is a cubic hamiltonian graph of order 12 with the graph
    crossing number 2 and has a girth 5 (that is the maximal girth among all
    cubic graphs on 12 vertices [CHNP2020]_). It corresponds to the graph
    labeled as `\\Gamma_2` by Fischer and Little [FiLi2001]_. The Twinplex graph
    has LCF notation `[-5, -4, 4, -4, 4, 5, -4, 5, -4, 4, -5, 4]`.

    The Fischer-Little Theorem [FiLi2001]_ may be stated as follows [LM2024]_:

    A near-bipartite graph is non-Pfaffian if and only if it contains one of
    the graphs `K_{3, 3}`, `\\Gamma_1` and `\\Gamma_2` as an `S`-minor.

    Norine and Thomas [NT2007]_ use the term ``Twinplex`` to describe one of
    the 12-vertex cubic graphs, `\\Gamma_1` and `\\Gamma_2`, as defined by
    Fischer and Little [FiLi2001]_. However, the figure in their paper that
    supposedly provides embeddings for the graphs labeled Cubeplex and Twinplex
    actually shows both embeddings corresponding to Fischer and Little's
    `\\Gamma_1`, which is the Cubeplex graph. Followingly, for
    ``embedding='NT'``, we present a correct version of the Twinplex graph
    with a slight modification of the embedding that is labeled as ``Twinplex``
    in the paper of Norine and Thomas [NT2007]_.

    PLOTTING:

    Upon construction, the position dictionary is filled to override
    the spring-layout algorithm. For different values of the parameter
    ``embedding``, the Twinplex graph is displayed as it is mentioned in the
    respective paper/ book. Note that for ``embedding='NT'``, a correct
    embedding of the Twinplex graph is displayed with a minor modification to
    the (incorrect) embedding shown in the paper [NT2007]_.

    INPUT:

    - ``embedding`` -- string (default: ``'LM'``)

      - ``'LM'`` displays the embedding as shown for `\\Gamma_2` by Lucchesi and
        Murty [LM2024]_

      - ``'FL'`` displays the embedding as shown for `\\Gamma_2` by Fischer and
        Little [FiLi2001]_

      - ``'NT'`` displays the correct embedding with a minor modification to
        the one shown as the (incorrect) ``Twinplex`` by Norine and Thomas
        [NT2007]_

      - ``'RST'`` displays the embedding as shown for the ``Twinplex`` by
        Robertson, Seymour and Thomas [RST2019]_

    OUTPUT:

    - ``G`` -- the Twinplex graph; note that a :class:`ValueError` is returned
      if ``embedding`` is none of ``'FT'``, ``'NT'``, ``'RST'`` or ``'LM'``

    EXAMPLES:

    Construct and show the Twinplex graph::

        sage: g = graphs.TwinplexGraph()
        sage: g.name()
        'Twinplex Graph'
        sage: g.order()
        12
        sage: g.size()
        18
        sage: g.girth()
        5
        sage: g.diameter()
        3
        sage: g.is_hamiltonian()
        True
        sage: g.crossing_number()
        2
        sage: g.show()                          # long time                             # needs sage.plot

    TESTS:

    Note that all four embeddings refer to the same graph, the Twinplex graph,
    aka `\\Gamma_2`::

        sage: fl = graphs.TwinplexGraph(embedding='FL')
        sage: nt = graphs.TwinplexGraph(embedding='NT')
        sage: rst = graphs.TwinplexGraph(embedding='RST')
        sage: lm = graphs.TwinplexGraph(embedding='LM')
        sage: all(fl.is_isomorphic(g) for g in (nt, rst, lm))
        True

    The input parameter must be one of 'FL', 'NT', 'RST' or 'LM'::

        sage: g = graphs.TwinplexGraph(embedding='embedding')
        Traceback (most recent call last):
        ...
        ValueError: parameter 'embedding' must be 'FL', 'NT', 'LM' or 'RST'

    .. SEEALSO::

        :meth:`~sage.graphs.graph_generators.GraphGenerators.CubeplexGraph`

    AUTHORS:

    - Janmenjaya Panda (2024-08-03)
    """
def WagnerGraph():
    """
    Return the Wagner Graph.

    See the :wikipedia:`Wagner_graph`.

    EXAMPLES::

        sage: # needs networkx
        sage: g = graphs.WagnerGraph()
        sage: g.order()
        8
        sage: g.size()
        12
        sage: g.girth()
        4
        sage: g.diameter()
        2
        sage: g.show()                                                                  # needs sage.plot
    """
def WatkinsSnarkGraph():
    """
    Return the Watkins Snark Graph.

    The Watkins Graph is a snark with 50 vertices and 75 edges. For more
    information, see the :wikipedia:`Watkins_snark`.

    EXAMPLES::

        sage: g = graphs.WatkinsSnarkGraph()
        sage: g.order()
        50
        sage: g.size()
        75
        sage: g.chromatic_number()
        3
    """
def WienerArayaGraph():
    """
    Return the Wiener-Araya Graph.

    The Wiener-Araya Graph is a planar hypohamiltonian graph on 42 vertices and
    67 edges. For more information, see the `Wolfram Page on the Wiener-Araya
    Graph <http://mathworld.wolfram.com/Wiener-ArayaGraph.html>`_ or
    :wikipedia:`Wiener-Araya_graph`.

    EXAMPLES::

        sage: g = graphs.WienerArayaGraph()
        sage: g.order()
        42
        sage: g.size()
        67
        sage: g.girth()
        4
        sage: g.is_planar()
        True
        sage: g.is_hamiltonian()                # not tested (30s)                      # needs sage.numerical.mip
        False
        sage: g.delete_vertex(g.random_vertex())
        sage: g.is_hamiltonian()                                                        # needs sage.numerical.mip
        True
    """
def MathonStronglyRegularGraph(t):
    """
    Return one of Mathon's graphs on 784 vertices.

    INPUT:

    - ``t`` -- integer; the number of the graph, from 0 to 2

    EXAMPLES::

        sage: # long time, needs sage.libs.gap
        sage: from sage.graphs.generators.smallgraphs import MathonStronglyRegularGraph
        sage: G = MathonStronglyRegularGraph(0)
        sage: G.is_strongly_regular(parameters=True)
        (784, 243, 82, 72)

    TESTS::

        sage: # long time, needs sage.libs.gap
        sage: G = graphs.MathonStronglyRegularGraph(1)
        sage: G.is_strongly_regular(parameters=True)
        (784, 270, 98, 90)
        sage: G = graphs.MathonStronglyRegularGraph(2)
        sage: G.is_strongly_regular(parameters=True)
        (784, 297, 116, 110)
    """
def JankoKharaghaniGraph(v):
    """
    Return a `(936, 375, 150, 150)`-srg or a `(1800, 1029, 588, 588)`-srg.

    This functions returns a strongly regular graph for the two sets of
    parameters shown to be realizable in [JK2002]_. The paper also uses a
    construction from [GM1987]_.

    INPUT:

    - ``v`` -- integer; one of 936 or 1800

    EXAMPLES::

        sage: g = graphs.JankoKharaghaniGraph(936)      # long time                     # needs sage.libs.pari
        sage: g.is_strongly_regular(parameters=True)    # long time                     # needs sage.libs.pari
        (936, 375, 150, 150)

        sage: g = graphs.JankoKharaghaniGraph(1800)     # not tested (30s)
        sage: g.is_strongly_regular(parameters=True)    # not tested (30s)
        (1800, 1029, 588, 588)
    """
def JankoKharaghaniTonchevGraph():
    """
    Return a `(324,153,72,72)`-strongly regular graph from [JKT2001]_.

    Build the graph using the description given in [JKT2001]_, taking sets B1
    and B163 in the text as adjacencies of vertices 1 and 163, respectively, and
    taking the edge orbits of the group `G` provided.

    EXAMPLES::

        sage: Gamma = graphs.JankoKharaghaniTonchevGraph()      # long time             # needs sage.libs.gap
        sage: Gamma.is_strongly_regular(parameters=True)        # long time             # needs sage.libs.gap
        (324, 153, 72, 72)
    """
def IoninKharaghani765Graph():
    """
    Return a `(765, 192, 48, 48)`-strongly regular graph.

    Existence of a strongly regular graph with these parameters was claimed in
    [IK2003]_.  Implementing the construction in the latter did not work,
    however. This function implements the following instructions, shared by Yury
    Ionin and Hadi Kharaghani.

        Let `A` be the affine plane over the field `GF(3)=\\{-1,0,1\\}`. Let

        .. MATH::

            \\phi_1(x,y) &= x\\\\\n            \\phi_2(x,y) &= y\\\\\n            \\phi_3(x,y) &= x+y\\\\\n            \\phi_4(x,y) &= x-y\\\\\n
        For `i=1,2,3,4` and `j\\in GF(3)`, let `L_{i,j}` be the line in `A`
        defined by `\\phi_i(x,y)=j`. Let `\\mathcal M` be the set of all 12 lines
        `L_{i,j}`, plus the empty set. Let `\\pi` be the permutation defined on
        `\\mathcal M` by `\\pi(L_{i,j}) = L_{i,j+1}` and `\\pi(\\emptyset) =
        \\emptyset`, so that `\\pi` has three orbits of cardinality 3 and one of
        cardinality 1.

        Let `A=(p_1,...,p_9)` with `p_1=(-1,1)`, `p_2=(-1,0)`, `p_3=(-1,1)`,
        `p_4=(0,-1)`, `p_5=(0,0)`, `p_6=(0,1)`, `p_7=(1,-1)`, `p_8=(1,0)`,
        `p_9=(1,1)`. Note that `p_i+p_{10-i}=(0,0)`. For any subset `X` of `A`,
        let `M(X)` be the `(0,1)`-matrix of order 9 whose `(i,j)`-entry equals 1
        if and only if `p_{10-i}-p_j\\in X`. Note that `M` is a symmetric matrix.

        An `MF`-tuple is an ordered quintuple `(X_1, X_2, X_3, X_4, X_5)` of
        subsets of `A`, of which one is the empty set and the other four are
        pairwise non-parallel lines. Such a quintuple generates the following
        block matrix:

        .. MATH::

            N(X_1, X_2, X_3, X_4, X_5) = \\left( \\begin{array}{ccccc}
                M(X_1) & M(X_2) & M(X_3) & M(X_4) & M(X_5)\\\\\n                M(X_2) & M(X_3) & M(X_4) & M(X_5) & M(X_1)\\\\\n                M(X_3) & M(X_4) & M(X_5) & M(X_1) & M(X_2)\\\\\n                M(X_4) & M(X_5) & M(X_1) & M(X_2) & M(X_3)\\\\\n                M(X_5) & M(X_1) & M(X_2) & M(X_3) & M(X_4)
                \\end{array}\\right)

        Observe that if `(X_1, X_2, X_3, X_4, X_5)` is an `MF`-tuple, then
        `N(X_1, X_2, X_3, X_4, X_5)` is the symmetric incidence matrix of a
        symmetric `(45, 12, 3)`-design.

        Let `\\mathcal F` be the set of all `MF`-tuples and let `\\sigma` be the
        following permutation of `\\mathcal F`:

        .. MATH::

            \\sigma(X_1, X_2, X_3, X_4, X_5) & = (X_2, X_3, X_4, X_5, X_1)\\\\\n            \\pi(X_1, X_2, X_3, X_4, X_5) & = (\\pi(X_1), \\pi(X_2), \\pi(X_3), \\pi(X_4), \\pi(X_5))\\\\\n
        Observe that `\\sigma` and `\\pi` commute, and generate a (cyclic) group
        `G` of order 15. We will from now on identify `G` with the (cyclic)
        multiplicative group of the field `GF(16)` equal to
        `\\{\\omega^0,...,\\omega^{14}\\}`. Let `W=[w_{ij}]` be the following matrix
        of order 17 over `GF(16)=\\{a_1,...,a_16\\}`:

        .. MATH::

            w_{ij}=\\left\\{\\begin{array}{ll}
                a_i+a_j & \\text{if }1\\leq i\\leq 16, 1\\leq j\\leq 16,\\\\\n                1       & \\text{if }i=17, j\\neq 17,\\\\\n                1       & \\text{if }i\\neq 17, j= 17,\\\\\n                0       & \\text{if }i=j=17
                \\end{array}\\right.

        The diagonal entries of `W` are equal to 0, each off-diagonal entry can
        be represented as `\\omega^k` with `0\\leq k\\leq 14`. Matrix `W` is a
        symmetric `BGW(17,16,15; G)`.

        Fix an `MF`-tuple `(X_1, X_2, X_3, X_4, X_5)` and let `S` be the block
        matrix obtained from `W` by replacing every diagonal entry of `W` by the
        zero matrix of order 45, and every off-diagonal entry `\\omega^k` by the
        matrix `N(\\sigma^k(X_1, X_2, X_3, X_4, X_5))` (through the association
        of `\\omega^k` with an element of `G`). Then `S` is a symmetric incidence
        matrix of a symmetric `(765, 192, 48)`-design with zero diagonal, and
        therefore `S` is an adjacency matrix of a strongly regular graph with
        parameters `(765, 192, 48, 48)`.

    EXAMPLES::

        sage: g = graphs.IoninKharaghani765Graph(); g                                   # needs sage.modules sage.rings.finite_rings
        Ionin-Kharaghani: Graph on 765 vertices

    TESTS::

        sage: graphs.strongly_regular_graph(765, 192, 48, 48)                           # needs sage.modules sage.rings.finite_rings
        Ionin-Kharaghani: Graph on 765 vertices

    .. TODO::

        An update to [IK2003]_ meant to fix the problem encountered became available
        2016/02/24, see http://www.cs.uleth.ca/~hadi/research/IoninKharaghani.pdf
    """
def U42Graph216():
    """
    Return a (216,40,4,8)-strongly regular graph from [CRS2016]_.

    Build the graph, interpreting the `U_4(2)`-action considered in [CRS2016]_
    as the one on the hyperbolic lines of the corresponding unitary polar space,
    and then doing the unique merging of the orbitals leading to a graph with
    the parameters in question.

    EXAMPLES::

        sage: G=graphs.U42Graph216()                    # optional - gap_package_grape
        sage: G.is_strongly_regular(parameters=True)    # optional - gap_package_grape
        (216, 40, 4, 8)
    """
def U42Graph540():
    """
    Return a (540,187,58,68)-strongly regular graph from [CRS2016]_.

    Build the graph, interpreting the `U_4(2)`-action considered in [CRS2016]_
    as the action of `U_4(2)=Sp_4(3)<U_4(3)` on the nonsingular, w.r.t.  to the
    Hermitean form stabilised by `U_4(3)`, points of the 3-dimensional
    projective space over `GF(9)`. There are several possible mergings of
    orbitals, some leading to non-isomorphic graphs with the same parameters. We
    found the merging here using [FK1991]_.

    EXAMPLES::

        sage: G = graphs.U42Graph540()                  # optional - gap_package_grape
        sage: G.is_strongly_regular(parameters=True)    # optional - gap_package_grape
        (540, 187, 58, 68)
    """
