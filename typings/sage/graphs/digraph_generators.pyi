r"""
Common digraphs

All digraphs in Sage can be built through the ``digraphs`` object. In order to
build a circuit on 15 elements, one can do::

    sage: g = digraphs.Circuit(15)

To get a circulant graph on 10 vertices in which a vertex `i` has `i+2` and
`i+3` as outneighbors::

    sage: p = digraphs.Circulant(10,[2,3])

More interestingly, one can get the list of all digraphs that Sage knows how to
build by typing ``digraphs.`` in Sage and then hitting :kbd:`Tab`.

.. csv-table::
    :class: contentstable
    :widths: 30, 70
    :delim: |

    :meth:`~DiGraphGenerators.ButterflyGraph`      | Return a `n`-dimensional butterfly graph.
    :meth:`~DiGraphGenerators.Circuit`             | Return the circuit on `n` vertices.
    :meth:`~DiGraphGenerators.Circulant`           | Return a circulant digraph on `n` vertices from a set of integers.
    :meth:`~DiGraphGenerators.Complete`            | Return a complete digraph on `n` vertices.
    :meth:`~DiGraphGenerators.DeBruijn`            | Return the De Bruijn digraph with parameters `k,n`.
    :meth:`~DiGraphGenerators.GeneralizedDeBruijn` | Return the generalized de Bruijn digraph of order `n` and degree `d`.
    :meth:`~DiGraphGenerators.ImaseItoh`           | Return the digraph of Imase and Itoh of order `n` and degree `d`.
    :meth:`~DiGraphGenerators.Kautz`               | Return the Kautz digraph of degree `d` and diameter `D`.
    :meth:`~DiGraphGenerators.nauty_directg`       | Return an iterator yielding digraphs using nauty's ``directg`` program.
    :meth:`~DiGraphGenerators.nauty_posetg`        | Return an iterator yielding Hasse diagrams of posets using nauty's ``genposetg`` program.
    :meth:`~DiGraphGenerators.Paley`               | Return a Paley digraph on `q` vertices.
    :meth:`~DiGraphGenerators.Path`                | Return a directed path on `n` vertices.
    :meth:`~DiGraphGenerators.RandomDirectedAcyclicGraph` | Return a random (weighted) directed acyclic graph of order `n`.
    :meth:`~DiGraphGenerators.RandomDirectedGNC`   | Return a random growing network with copying (GNC) digraph with `n` vertices.
    :meth:`~DiGraphGenerators.RandomDirectedGNM`   | Return a random labelled digraph on `n` nodes and `m` arcs.
    :meth:`~DiGraphGenerators.RandomDirectedGNP`   | Return a random digraph on `n` nodes.
    :meth:`~DiGraphGenerators.RandomDirectedGN`    | Return a random growing network (GN) digraph with `n` vertices.
    :meth:`~DiGraphGenerators.RandomDirectedGNR`   | Return a random growing network with redirection (GNR) digraph.
    :meth:`~DiGraphGenerators.RandomSemiComplete`  | Return a random semi-complete digraph of order `n`.
    :meth:`~DiGraphGenerators.RandomTournament`    | Return a random tournament on `n` vertices.
    :meth:`~DiGraphGenerators.TransitiveTournament`| Return a transitive tournament on `n` vertices.
    :meth:`~DiGraphGenerators.tournaments_nauty`   | Iterator over all tournaments on `n` vertices using Nauty.


AUTHORS:

- Robert L. Miller (2006)
- Emily A. Kirkman (2006)
- Michael C. Yurko (2009)
- David Coudert    (2012)
- Janmenjaya Panda (2024)

Functions and methods
---------------------
"""
from _typeshed import Incomplete
from collections.abc import Generator
from sage.cpython.string import bytes_to_str as bytes_to_str
from sage.graphs.digraph import DiGraph as DiGraph
from sage.graphs.graph import Graph as Graph
from sage.misc.randstate import current_randstate as current_randstate

class DiGraphGenerators:
    """
    A class consisting of constructors for several common digraphs,
    including orderly generation of isomorphism class representatives.

    A list of all graphs and graph structures in this database is available via
    tab completion. Type ``digraphs.`` and then hit :kbd:`Tab` to see which
    digraphs are available.

    The docstrings include educational information about each named
    digraph with the hopes that this class can be used as a reference.

    The constructors currently in this class include::

                Random Directed Graphs:
                    - RandomDirectedAcyclicGraph
                    - RandomDirectedGN
                    - RandomDirectedGNC
                    - RandomDirectedGNP
                    - RandomDirectedGNM
                    - RandomDirectedGNR
                    - RandomTournament
                    - RandomSemiComplete

                Families of Graphs:
                    - Complete
                    - DeBruijn
                    - GeneralizedDeBruijn
                    - Kautz
                    - Path
                    - ImaseItoh
                    - RandomTournament
                    - TransitiveTournament
                    - tournaments_nauty


    ORDERLY GENERATION: digraphs(vertices, property=lambda x: True,
    augment='edges', size=None)

    Accesses the generator of isomorphism class representatives [McK1998]_.
    Iterates over distinct, exhaustive representatives.

    INPUT:

    - ``vertices`` -- natural number or ``None`` to infinitely generate bigger
      and bigger digraphs

    - ``property`` -- any property to be tested on digraphs before generation

    - ``augment`` -- choices:

      - ``'vertices'`` -- augments by adding a vertex, and edges incident to
        that vertex. In this case, all digraphs on *up to* n=vertices are
        generated. If for any digraph G satisfying the property, every subgraph,
        obtained from G by deleting one vertex and only edges incident to that
        vertex, satisfies the property, then this will generate all digraphs
        with that property. If this does not hold, then all the digraphs
        generated will satisfy the property, but there will be some missing.

      - ``'edges'`` -- augments a fixed number of vertices by adding one
        edge. In this case, all digraphs on *exactly* n=vertices are
        generated. If for any graph G satisfying the property, every subgraph,
        obtained from G by deleting one edge but not the vertices incident to
        that edge, satisfies the property, then this will generate all digraphs
        with that property. If this does not hold, then all the digraphs
        generated will satisfy the property, but there will be some missing.

    - ``implementation`` -- which underlying implementation to use
      (see DiGraph?)

    - ``sparse`` -- boolean (default: ``True``); whether to use a sparse or
      dense data structure. See the documentation of
      :class:`~sage.graphs.graph.Graph`.

    - ``copy`` -- boolean (default: ``True``); whether to make copies of the
      digraphs before returning them. If set to ``False`` the method returns the
      digraph it is working on. The second alternative is faster, but modifying
      any of the digraph instances returned by the method may break the
      function's behaviour, as it is using these digraphs to compute the next
      ones: only use ``copy = False`` when you stick to *reading* the digraphs
      returned.

      This parameter is ignored when ``immutable`` is set to ``True``, in which
      case returned graphs are always copies.

    - ``immutable`` -- boolean (default: ``False``); whether to return immutable
      or mutable digraphs. When set to ``True``, this parameter implies
      ``copy=True``.

    EXAMPLES:

    Print digraphs on 2 or less vertices::

        sage: for D in digraphs(2, augment='vertices'):
        ....:     print(D)
        Digraph on 0 vertices
        Digraph on 1 vertex
        Digraph on 2 vertices
        Digraph on 2 vertices
        Digraph on 2 vertices

    Print digraphs on 3 vertices::

        sage: for D in digraphs(3):
        ....:     print(D)
        Digraph on 3 vertices
        Digraph on 3 vertices
        ...
        Digraph on 3 vertices
        Digraph on 3 vertices

    Generate all digraphs with 4 vertices and 3 edges::

        sage: L = digraphs(4, size=3)
        sage: len(list(L))
        13

    Generate all digraphs with 4 vertices and up to 3 edges::

        sage: L = list(digraphs(4, lambda G: G.size() <= 3))
        sage: len(L)
        20
        sage: graphs_list.show_graphs(L)        # long time                             # needs sage.plot

    Generate all digraphs with degree at most 2, up to 5 vertices::

        sage: property = lambda G: (max([G.degree(v) for v in G] + [0]) <= 2)
        sage: L = list(digraphs(5, property, augment='vertices'))
        sage: len(L)
        75

    Generate digraphs on the fly (see http://oeis.org/classic/A000273)::

        sage: for i in range(5):
        ....:     print(len(list(digraphs(i))))
        1
        1
        3
        16
        218
    """
    def ButterflyGraph(self, n, vertices: str = 'strings', immutable: bool = False):
        """
        Return a `n`-dimensional butterfly graph.

        The vertices consist of pairs `(v, i)`, where `v` is an `n`-dimensional
        tuple (vector) with binary entries (or a string representation of such)
        and `i` is an integer in `[0..n]`. A directed edge goes from `(v, i)` to
        `(w, i + 1)` if `v` and `w` are identical except for possibly when `v[i]
        \\neq w[i]`.

        A butterfly graph has `(2^n)(n+1)` vertices and `n2^{n+1}` edges.

        INPUT:

        - ``n`` -- nonnegative integer; the dimension of the butterfly graph

        - ``vertices`` -- string (default: ``'strings'``); specifies whether the
          vertices are zero-one strings (default) or tuples over GF(2)
          (``vertices='vectors'``)

        - ``immutable`` -- boolean (default: ``False``); whether to return
          an immutable or mutable digraph

        EXAMPLES::

            sage: digraphs.ButterflyGraph(2).edges(sort=True, labels=False)
            [(('00', 0), ('00', 1)),
             (('00', 0), ('10', 1)),
             (('00', 1), ('00', 2)),
             (('00', 1), ('01', 2)),
             (('01', 0), ('01', 1)),
             (('01', 0), ('11', 1)),
             (('01', 1), ('00', 2)),
             (('01', 1), ('01', 2)),
             (('10', 0), ('00', 1)),
             (('10', 0), ('10', 1)),
             (('10', 1), ('10', 2)),
             (('10', 1), ('11', 2)),
             (('11', 0), ('01', 1)),
             (('11', 0), ('11', 1)),
             (('11', 1), ('10', 2)),
             (('11', 1), ('11', 2))]
            sage: digraphs.ButterflyGraph(2, vertices='vectors').edges(sort=True,       # needs sage.modules sage.rings.finite_rings
            ....:                                                      labels=False)
            [(((0, 0), 0), ((0, 0), 1)),
             (((0, 0), 0), ((1, 0), 1)),
             (((0, 0), 1), ((0, 0), 2)),
             (((0, 0), 1), ((0, 1), 2)),
             (((0, 1), 0), ((0, 1), 1)),
             (((0, 1), 0), ((1, 1), 1)),
             (((0, 1), 1), ((0, 0), 2)),
             (((0, 1), 1), ((0, 1), 2)),
             (((1, 0), 0), ((0, 0), 1)),
             (((1, 0), 0), ((1, 0), 1)),
             (((1, 0), 1), ((1, 0), 2)),
             (((1, 0), 1), ((1, 1), 2)),
             (((1, 1), 0), ((0, 1), 1)),
             (((1, 1), 0), ((1, 1), 1)),
             (((1, 1), 1), ((1, 0), 2)),
             (((1, 1), 1), ((1, 1), 2))]
            sage: pos = digraphs.ButterflyGraph(2).get_pos()
            sage: pos['11', 0]
            (0, 0)

        TESTS::

            sage: digraphs.ButterflyGraph(0)
            0-dimensional Butterfly: Digraph on 0 vertices
            sage: digraphs.ButterflyGraph(-1)
            Traceback (most recent call last):
            ...
            ValueError: the number of dimensions must be positive
        """
    def Path(self, n, immutable: bool = False):
        """
        Return a directed path on `n` vertices.

        INPUT:

        - ``n`` -- integer; number of vertices in the path

        - ``immutable`` -- boolean (default: ``False``); whether to return
          an immutable or mutable digraph

        EXAMPLES::

            sage: g = digraphs.Path(5)
            sage: g.vertices(sort=True)
            [0, 1, 2, 3, 4]
            sage: g.size()
            4
            sage: g.automorphism_group().cardinality()                                  # needs sage.groups
            1
        """
    def StronglyRegular(self, n, immutable: bool = False):
        """
        Return a Strongly Regular digraph with `n` vertices.

        The adjacency matrix of the graph is constructed from a skew Hadamard
        matrix of order `n+1`. These graphs were first constructed in [Duv1988]_.

        INPUT:

        - ``n`` -- integer; the number of vertices of the digraph

        - ``immutable`` -- boolean (default: ``False``); whether to return
          an immutable or mutable digraph

        .. SEEALSO::

            - :func:`sage.combinat.matrices.hadamard_matrix.skew_hadamard_matrix`
            - :meth:`Paley`

        EXAMPLES:

        A Strongly Regular digraph satisfies the condition `AJ = JA = kJ` where
        `A` is the adjacency matrix::

            sage: # needs sage.combinat sage.modules
            sage: g = digraphs.StronglyRegular(7); g
            Strongly regular digraph: Digraph on 7 vertices
            sage: A = g.adjacency_matrix()*ones_matrix(7)
            sage: B = ones_matrix(7)*g.adjacency_matrix()
            sage: A == B == A[0, 0]*ones_matrix(7)
            True

        TESTS:

        Wrong parameter::

            sage: digraphs.StronglyRegular(73)                                          # needs sage.combinat sage.modules
            Traceback (most recent call last):
            ...
            ValueError: strongly regular digraph with 73 vertices not yet implemented
        """
    def Paley(self, q, immutable: bool = False):
        """
        Return a Paley digraph on `q` vertices.

        Parameter `q` must be the power of a prime number and congruent to 3 mod
        4.

        INPUT:

        - ``q`` -- integer; the number of vertices of the digraph

        - ``immutable`` -- boolean (default: ``False``); whether to return
          an immutable or mutable digraph

        .. SEEALSO::

            - :wikipedia:`Paley_graph`
            - :meth:`~sage.graphs.graph_generators.GraphGenerators.PaleyGraph`

        EXAMPLES:

        A Paley digraph has `n * (n-1) / 2` edges, its underlying graph is a
        clique, and so it is a tournament::

            sage: g = digraphs.Paley(7); g                                              # needs sage.rings.finite_rings
            Paley digraph with parameter 7: Digraph on 7 vertices
            sage: g.size() == g.order() * (g.order() - 1) / 2                           # needs sage.rings.finite_rings
            True
            sage: g.to_undirected().is_clique()                                         # needs sage.rings.finite_rings
            True

        A Paley digraph is always self-complementary::

            sage: g.complement().is_isomorphic(g)                                       # needs sage.rings.finite_rings
            True

        TESTS:

        Wrong parameter::

            sage: digraphs.Paley(6)
            Traceback (most recent call last):
            ...
            ValueError: parameter q must be a prime power
            sage: digraphs.Paley(5)
            Traceback (most recent call last):
            ...
            ValueError: parameter q must be congruent to 3 mod 4
        """
    def TransitiveTournament(self, n, immutable: bool = False):
        """
        Return a transitive tournament on `n` vertices.

        In this tournament there is an edge from `i` to `j` if `i<j`.

        See the :wikipedia:`Tournament_(graph_theory)` for more information.

        INPUT:

        - ``n`` -- integer; number of vertices in the tournament

        - ``immutable`` -- boolean (default: ``False``); whether to return
          an immutable or mutable digraph

        EXAMPLES::

            sage: g = digraphs.TransitiveTournament(5)
            sage: g.vertices(sort=True)
            [0, 1, 2, 3, 4]
            sage: g.size()
            10
            sage: g.automorphism_group().cardinality()                                  # needs sage.groups
            1

        .. SEEALSO::

            - :wikipedia:`Tournament_(graph_theory)`
            - :meth:`~sage.graphs.digraph.DiGraph.is_tournament`
            - :meth:`~sage.graphs.digraph.DiGraph.is_transitive`
            - :meth:`~sage.graphs.digraph_generators.DiGraphGenerators.RandomTournament`

        TESTS::

            sage: digraphs.TransitiveTournament(-1)
            Traceback (most recent call last):
            ...
            ValueError: the number of vertices cannot be strictly negative
        """
    def RandomTournament(self, n, immutable: bool = False):
        """
        Return a random tournament on `n` vertices.

        For every pair of vertices, the tournament has an edge from
        `i` to `j` with probability `1/2`, otherwise it has an edge
        from `j` to `i`.

        INPUT:

        - ``n`` -- integer; number of vertices

        - ``immutable`` -- boolean (default: ``False``); whether to return
          an immutable or mutable digraph

        EXAMPLES::

            sage: T = digraphs.RandomTournament(10); T
            Random Tournament: Digraph on 10 vertices
            sage: T.size() == binomial(10, 2)                                           # needs sage.symbolic
            True
            sage: T.is_tournament()
            True
            sage: digraphs.RandomTournament(-1)
            Traceback (most recent call last):
            ...
            ValueError: the number of vertices cannot be strictly negative

        .. SEEALSO::

            - :wikipedia:`Tournament_(graph_theory)`
            - :meth:`~sage.graphs.digraph.DiGraph.is_tournament`
            - :meth:`~sage.graphs.digraph_generators.DiGraphGenerators.TransitiveTournament`
            - :meth:`~sage.graphs.digraph_generators.DiGraphGenerators.Complete`
            - :meth:`~sage.graphs.digraph_generators.DiGraphGenerators.RandomSemiComplete`
        """
    def tournaments_nauty(self, n, min_out_degree=None, max_out_degree=None, strongly_connected: bool = False, debug: bool = False, options: str = '', immutable: bool = False) -> Generator[Incomplete]:
        '''
        Iterator over all tournaments on `n` vertices using Nauty.

        INPUT:

        - ``n`` -- integer; number of vertices

        - ``min_out_degree``, ``max_out_degree`` -- integers; if set to
          ``None`` (default), then the min/max out-degree is not constrained

        - ``debug`` -- boolean (default: ``False``); if ``True`` the first line
          of gentourng\'s output to standard error is captured and the first call
          to the generator\'s ``next()`` function will return this line as a
          string.  A line leading with ">A" indicates a successful initiation of
          the program with some information on the arguments, while a line
          beginning with ">E" indicates an error with the input.

        - ``options`` -- string; anything else that should be forwarded as input
          to Nauty\'s gentourng. See its documentation for more information :
          `<https://pallini.di.uniroma1.it>`_.

        - ``immutable`` -- boolean (default: ``False``); whether to return
          immutable or mutable digraphs

        EXAMPLES::

            sage: for g in digraphs.tournaments_nauty(4):
            ....:     print(g.edges(sort=True, labels = False))
            [(1, 0), (2, 0), (2, 1), (3, 0), (3, 1), (3, 2)]
            [(1, 0), (1, 3), (2, 0), (2, 1), (3, 0), (3, 2)]
            [(0, 2), (1, 0), (2, 1), (3, 0), (3, 1), (3, 2)]
            [(0, 2), (0, 3), (1, 0), (2, 1), (3, 1), (3, 2)]
            sage: tournaments = digraphs.tournaments_nauty
            sage: [len(list(tournaments(x))) for x in range(1,8)]
            [1, 1, 2, 4, 12, 56, 456]
            sage: [len(list(tournaments(x, strongly_connected = True))) for x in range(1,9)]
            [1, 0, 1, 1, 6, 35, 353, 6008]
        '''
    def nauty_directg(self, graphs, options: str = '', debug: bool = False, immutable: bool = False) -> Generator[Incomplete]:
        '''
        Return an iterator yielding digraphs using nauty\'s ``directg`` program.

        Description from ``directg --help``:
        Read undirected graphs and orient their edges in all possible ways.
        Edges can be oriented in either or both directions (3 possibilities).
        Isomorphic directed graphs derived from the same input are suppressed.
        If the input graphs are non-isomorphic then the output graphs are also.

        INPUT:

        - ``graphs`` -- a :class:`Graph` or an iterable containing
          :class:`Graph`.  The graph6 string of these graphs is used as an input
          for ``directg``.

        - ``options`` -- string passed to ``directg`` as if it was run at
          a system command line. Available options from ``directg --help``::

            -e<int> | -e<int>:<int>  specify a value or range of the total number of arcs
            -o       orient each edge in only one direction, never both
            -a       only make acyclic orientations (implies -o)
            -f<int>  Use only the subgroup that fixes the first <int> vertices setwise
            -V       only output graphs with nontrivial groups (including exchange of
                     isolated vertices).  The -f option is respected.
            -s<int>/<int>  Make only a fraction of the orientations: The first integer is
                     the part number (first is 0) and the second is the number of
                     parts. Splitting is done per input graph independently.

        - ``debug`` -- boolean (default: ``False``); if ``True`` ``directg``
          standard error and standard output are displayed

        - ``immutable`` -- boolean (default: ``False``); whether to return
          immutable or mutable digraphs

        EXAMPLES::

            sage: gen = graphs.nauty_geng("-c 3")
            sage: dgs = list(digraphs.nauty_directg(gen))
            sage: len(dgs)
            13
            sage: dgs[0]
            Digraph on 3 vertices
            sage: dgs[0]._bit_vector()
            \'001001000\'
            sage: len(list(digraphs.nauty_directg(graphs.PetersenGraph(), options=\'-o\')))
            324

        Generate non-isomorphic acyclic orientations::

            sage: K = graphs.CompleteGraph(4)
            sage: all(d.is_directed_acyclic() for d in digraphs.nauty_directg(K, options=\'-a\'))
            True
            sage: sum(1 for _ in digraphs.nauty_directg(K, options=\'-a\'))
            1
            sage: S = graphs.StarGraph(4)
            sage: all(d.is_directed_acyclic() for d in digraphs.nauty_directg(S, options=\'-a\'))
            True
            sage: sum(1 for _ in digraphs.nauty_directg(S, options=\'-a\'))
            5

        TESTS::

            sage: g = digraphs.nauty_directg(graphs.PetersenGraph(), options="-o -G")
            sage: next(g)
            Traceback (most recent call last):
            ...
            ValueError: directg output options [-u|-T|-G] are not allowed
            sage: next(digraphs.nauty_directg(graphs.nauty_geng("-c 3"),
            ....:     options=\'-o\', debug=True))
            &BH?
            &BGO
            &B?o
            &BX?
            &BP_
            <BLANKLINE>
            Digraph on 3 vertices

        .. SEEALSO::

            - :meth:`~sage.graphs.graph.Graph.orientations`
            - :meth:`~sage.graphs.graph.Graph.strong_orientation`
            - :meth:`~sage.graphs.orientations.strong_orientations_iterator`
            - :meth:`~sage.graphs.orientations.random_orientation`
        '''
    def nauty_posetg(self, options: str = '', debug: bool = False, immutable: bool = False) -> Generator[Incomplete]:
        '''
        Return a generator which creates all posets using ``nauty``.

        Here a poset is seen through its Hasse diagram, which is
        an acyclic and transitively reduced digraph.

        INPUT:

        - ``options`` -- string (default: ``""``); a string passed to
          ``genposetg`` as if it was run at a system command line.
          At a minimum, you *must* pass the number of vertices you desire
          and a choice between ``o`` and ``t`` for the output order.

        - ``debug`` -- boolean (default: ``False``); if ``True`` the first line
          of ``genposetg``\'s output to standard error is captured and the first
          call to the generator\'s ``next()`` function will return this line as a
          string. A line leading with ">A" indicates a successful initiation of
          the program with some information on the arguments, while a line
          beginning with ">E" indicates an error with the input.

        - ``immutable`` -- boolean (default: ``False``); whether to return
          immutable or mutable posets

        The possible options, obtained as output of ``genposetg --help``::

            n: the number of vertices, between 0 and 16
            o: digraph6 output in arbitrary order
            t: digraph6 output in topological order

        EXAMPLES::

            sage: gen = digraphs.nauty_posetg("5 o")
            sage: len(list(gen))
            63

        This coincides with :oeis:`A000112`.
        '''
    def Complete(self, n, loops: bool = False, immutable: bool = False):
        """
        Return the complete digraph on `n` vertices.

        INPUT:

        - ``n`` -- integer; number of vertices

        - ``loops`` -- boolean (default: ``False``); whether to add loops or
          not, i.e., edges from `u` to itself

        - ``immutable`` -- boolean (default: ``False``); whether to return
          an immutable or mutable digraph

        .. SEEALSO::

            - :meth:`~sage.graphs.digraph_generators.DiGraphGenerators.RandomSemiComplete`

            - :meth:`~sage.graphs.digraph_generators.DiGraphGenerators.RandomTournament`

        EXAMPLES::

            sage: n = 10
            sage: G = digraphs.Complete(n); G
            Complete digraph: Digraph on 10 vertices
            sage: G.size() == n*(n-1)
            True
            sage: G = digraphs.Complete(n, loops=True); G
            Complete digraph with loops: Looped digraph on 10 vertices
            sage: G.size() == n*n
            True
            sage: digraphs.Complete(-1)
            Traceback (most recent call last):
            ...
            ValueError: the number of vertices cannot be strictly negative
        """
    def Circuit(self, n, immutable: bool = False):
        """
        Return the circuit on `n` vertices.

        The circuit is an oriented
        :meth:`~sage.graphs.graph_generators.GraphGenerators.CycleGraph`.

        INPUT:

        - ``n`` -- integer; number of vertices

        - ``immutable`` -- boolean (default: ``False``); whether to return
          an immutable or mutable digraph

        EXAMPLES:

        A circuit is the smallest strongly connected digraph::

            sage: circuit = digraphs.Circuit(15)
            sage: len(circuit.strongly_connected_components()) == 1
            True
        """
    def Circulant(self, n, integers, immutable: bool = False):
        '''
        Return a circulant digraph on `n` vertices from a set of integers.

        A circulant digraph of order `n` has an arc from vertex `i` to
        vertex `i+j \\pmod{n}`, for each `j` in ``integers``.

        INPUT:

        - ``n`` -- integer; number of vertices

        - ``integers`` -- iterable container (list, set, etc.) of integers such
          that there is an edge from `i` to `j` if and only if `(j-i) \\pmod{n}`
          is an integer

        - ``immutable`` -- boolean (default: ``False``); whether to return
          an immutable or mutable digraph

        EXAMPLES:

        Construct and show the circulant graph [3, 5, 7], a digraph on 13
        vertices::

            sage: g = digraphs.Circulant(13, [3, 5, 7])
            sage: g.show()                          # long time                             # needs sage.plot

        The Koh-Tindell digraph [LM2024]_ is the circulant digraph of order 7
        with parameters `[1, 5]`.  This `2`-diregular digraph is
        vertex-transitive but not arc-transitive. The associated bipartite
        digraph of the Koh-Tindell digraph is a Pfaffian orientation of the
        Heawood graph. Construct and show the Koh-Tindell digraph::

            sage: kohTindellDigraph = digraphs.Circulant(7, [1, 5])
            sage: kohTindellDigraph.show()          # long time                             # needs sage.plot

        TESTS:

            sage: digraphs.Circulant(13, [3, 5, 7, "hey"])
            Traceback (most recent call last):
            ...
            ValueError: the list must contain only integers
            sage: digraphs.Circulant(3, [3, 5, 7, 3.4])
            Traceback (most recent call last):
            ...
            ValueError: the list must contain only integers
        '''
    def DeBruijn(self, k, n, vertices: str = 'strings', immutable: bool = False):
        """
        Return the De Bruijn digraph with parameters `k,n`.

        The De Bruijn digraph with parameters `k,n` is built upon a set of
        vertices equal to the set of words of length `n` from a dictionary of
        `k` letters.

        In this digraph, there is an arc `w_1w_2` if `w_2` can be obtained from
        `w_1` by removing the leftmost letter and adding a new letter at its
        right end.  For more information, see the :wikipedia:`De_Bruijn_graph`.

        INPUT:

        - ``k`` -- two possibilities for this parameter :
            - An integer equal to the cardinality of the alphabet to use, that
              is, the degree of the digraph to be produced.
            - An iterable object to be used as the set of letters. The degree
              of the resulting digraph is the cardinality of the set of letters.

        - ``n`` -- integer; length of words in the De Bruijn digraph when
          ``vertices == 'strings'``, and also the diameter of the digraph

        - ``vertices`` -- string (default: ``'strings'``); whether the vertices
          are words over an alphabet (default) or integers
          (``vertices='string'``)

        - ``immutable`` -- boolean (default: ``False``); whether to return
          an immutable or mutable digraph

        EXAMPLES:

        de Bruijn digraph of degree 2 and diameter 2::

            sage: db = digraphs.DeBruijn(2, 2); db                                      # needs sage.combinat
            De Bruijn digraph (k=2, n=2): Looped digraph on 4 vertices
            sage: db.order(), db.size()                                                 # needs sage.combinat
            (4, 8)
            sage: db.diameter()                                                         # needs sage.combinat
            2

        Building a de Bruijn digraph on a different alphabet::

            sage: # needs sage.combinat
            sage: g = digraphs.DeBruijn(['a', 'b'], 2)
            sage: g.vertices(sort=True)
            ['aa', 'ab', 'ba', 'bb']
            sage: g.is_isomorphic(db)
            True
            sage: g = digraphs.DeBruijn(['AA', 'BB'], 2)
            sage: g.vertices(sort=True)
            ['AA,AA', 'AA,BB', 'BB,AA', 'BB,BB']
            sage: g.is_isomorphic(db)
            True

        TESTS:

        Alphabet of null size or words of length zero::

            sage: digraphs.DeBruijn(5, 0)                                               # needs sage.combinat
            De Bruijn digraph (k=5, n=0): Looped multi-digraph on 1 vertex
            sage: digraphs.DeBruijn(0, 0)                                               # needs sage.combinat
            De Bruijn digraph (k=0, n=0): Looped multi-digraph on 0 vertices

        :issue:`22355`::

            sage: db = digraphs.DeBruijn(2, 2, vertices='strings')                      # needs sage.combinat
            sage: db.vertices(sort=True)                                                # needs sage.combinat
            ['00', '01', '10', '11']
            sage: h = digraphs.DeBruijn(2, 2, vertices='integers')
            sage: h.vertices(sort=True)
            [0, 1, 2, 3]
            sage: db.is_isomorphic(h)                                                   # needs sage.combinat
            True
            sage: digraphs.DeBruijn(0, 0, vertices='integers')
            De Bruijn digraph (k=0, n=0): Looped multi-digraph on 0 vertices
            sage: digraphs.DeBruijn(2, 2, vertices='circles')
            Traceback (most recent call last):
            ...
            ValueError: unknown type for vertices
        """
    def GeneralizedDeBruijn(self, n, d, immutable: bool = False, name=None):
        """
        Return the generalized de Bruijn digraph of order `n` and degree `d`.

        The generalized de Bruijn digraph was defined in [RPK1980]_ [RPK1983]_.
        It has vertex set `V=\\{0, 1,..., n-1\\}` and there is an arc from vertex
        `u \\in V` to all vertices `v \\in V` such that `v \\equiv (u*d + a)
        \\mod{n}` with `0 \\leq a < d`.

        When `n = d^{D}`, the generalized de Bruijn digraph is isomorphic to
        the de Bruijn digraph of degree `d` and diameter `D`.

        INPUT:

        - ``n`` -- integer; number of vertices of the digraph (must be at least
          one)

        - ``d`` -- integer; degree of the digraph (must be at least one)

        - ``immutable`` -- boolean (default: ``False``); whether to return
          an immutable or mutable digraph

        - ``name`` -- string (default: ``None``); when set, the specified name
          is used instead of the default one

        .. SEEALSO::

            * :meth:`sage.graphs.generic_graph.GenericGraph.is_circulant` --
              checks whether a (di)graph is circulant, and/or returns all
              possible sets of parameters.

        EXAMPLES::

            sage: GB = digraphs.GeneralizedDeBruijn(8, 2)
            sage: GB.is_isomorphic(digraphs.DeBruijn(2, 3), certificate=True)           # needs sage.combinat
            (True, {0: '000', 1: '001', 2: '010', 3: '011',
                    4: '100', 5: '101', 6: '110', 7: '111'})

        TESTS:

        An exception is raised when the degree is less than one::

            sage: G = digraphs.GeneralizedDeBruijn(2, 0)
            Traceback (most recent call last):
            ...
            ValueError: degree must be greater than or equal to one

        An exception is raised when the order of the graph is less than one::

            sage: G = digraphs.GeneralizedDeBruijn(0, 2)
            Traceback (most recent call last):
            ...
            ValueError: order must be greater than or equal to one
        """
    def ImaseItoh(self, n, d, immutable: bool = False, name=None):
        """
        Return the Imase-Itoh digraph of order `n` and degree `d`.

        The Imase-Itoh digraph was defined in [II1983]_. It has vertex set
        `V=\\{0, 1,..., n-1\\}` and there is an arc from vertex `u \\in V` to all
        vertices `v \\in V` such that `v \\equiv (-u*d-a-1) \\mod{n}` with `0 \\leq
        a < d`.

        When `n = d^{D}`, the Imase-Itoh digraph is isomorphic to the de Bruijn
        digraph of degree `d` and diameter `D`. When `n = d^{D-1}(d+1)`, the
        Imase-Itoh digraph is isomorphic to the Kautz digraph [Kau1968]_ of
        degree `d` and diameter `D`.

        INPUT:

        - ``n`` -- integer; number of vertices of the digraph (must be greater
          than or equal to two)

        - ``d`` -- integer; degree of the digraph (must be greater than or
          equal to one)

        - ``immutable`` -- boolean (default: ``False``); whether to return
          an immutable or mutable digraph

        - ``name`` -- string (default: ``None``); when set, the specified name
          is used instead of the default one

        EXAMPLES::

            sage: II = digraphs.ImaseItoh(8, 2)
            sage: II.is_isomorphic(digraphs.DeBruijn(2, 3), certificate=True)           # needs sage.combinat
            (True, {0: '010', 1: '011', 2: '000', 3: '001',
                    4: '110', 5: '111', 6: '100', 7: '101'})

            sage: II = digraphs.ImaseItoh(12, 2)
            sage: b,D = II.is_isomorphic(digraphs.Kautz(2, 3), certificate=True)        # needs sage.combinat
            sage: b                                                                     # needs sage.combinat
            True
            sage: D   # random isomorphism                                              # needs sage.combinat
            {0: '202', 1: '201', 2: '210', 3: '212', 4: '121',
             5: '120', 6: '102', 7: '101', 8: '010', 9: '012',
             10: '021', 11: '020'}

        TESTS:

        An exception is raised when the degree is less than one::

            sage: G = digraphs.ImaseItoh(2, 0)
            Traceback (most recent call last):
            ...
            ValueError: degree must be greater than or equal to one

        An exception is raised when the order of the graph is less than two::

            sage: G = digraphs.ImaseItoh(1, 2)
            Traceback (most recent call last):
            ...
            ValueError: order must be greater than or equal to two
        """
    def Kautz(self, k, D, vertices: str = 'strings', immutable: bool = False):
        """
        Return the Kautz digraph of degree `d` and diameter `D`.

        The Kautz digraph has been defined in [Kau1968]_. The Kautz digraph of
        degree `d` and diameter `D` has `d^{D-1}(d+1)` vertices. This digraph
        is built from a set of vertices equal to the set of words of length `D`
        over an alphabet of `d+1` letters such that consecutive letters are
        different. There is an arc from vertex `u` to vertex `v` if `v` can be
        obtained from `u` by removing the leftmost letter and adding a new
        letter, distinct from the rightmost letter of `u`, at the right end.

        The Kautz digraph of degree `d` and diameter `D` is isomorphic to the
        Imase-Itoh digraph [II1983]_ of degree `d` and order `d^{D-1}(d+1)`.

        See the :wikipedia:`Kautz_graph` for more information.

        INPUT:

        - ``k`` -- two possibilities for this parameter. In either case the
          degree must be at least one:

            - An integer equal to the degree of the digraph to be produced,
              that is, the cardinality of the alphabet to be used minus one.
            - An iterable object to be used as the set of letters. The degree
              of the resulting digraph is the cardinality of the set of letters
              minus one.

        - ``D`` -- integer; diameter of the digraph, and length of a vertex
          label when ``vertices == 'strings'`` (must be at least one)

        - ``vertices`` -- string (default: ``'strings'``); whether the vertices
          are words over an alphabet (default) or integers
          (``vertices='strings'``)

        - ``immutable`` -- boolean (default: ``False``); whether to return
          an immutable or mutable digraph

        EXAMPLES::

            sage: # needs sage.combinat
            sage: K = digraphs.Kautz(2, 3)
            sage: b, D = K.is_isomorphic(digraphs.ImaseItoh(12, 2), certificate=True)
            sage: b
            True
            sage: D  # random isomorphism
            {'010': 8, '012': 9, '020': 11, '021': 10, '101': 7,  '102': 6,
             '120': 5, '121': 4, '201': 1, '202': 0, '210': 2, '212': 3}

            sage: K = digraphs.Kautz([1,'a','B'], 2)                                    # needs sage.combinat
            sage: K.edges(sort=True)                                                    # needs sage.combinat
            [('1B', 'B1', '1'), ('1B', 'Ba', 'a'), ('1a', 'a1', '1'),
             ('1a', 'aB', 'B'), ('B1', '1B', 'B'), ('B1', '1a', 'a'),
             ('Ba', 'a1', '1'), ('Ba', 'aB', 'B'), ('a1', '1B', 'B'),
             ('a1', '1a', 'a'), ('aB', 'B1', '1'), ('aB', 'Ba', 'a')]

            sage: K = digraphs.Kautz([1,'aA','BB'], 2)                                  # needs sage.combinat
            sage: K.edges(sort=True)                                                    # needs sage.combinat
            [('1,BB', 'BB,1', '1'), ('1,BB', 'BB,aA', 'aA'),
             ('1,aA', 'aA,1', '1'), ('1,aA', 'aA,BB', 'BB'),
             ('BB,1', '1,BB', 'BB'), ('BB,1', '1,aA', 'aA'),
             ('BB,aA', 'aA,1', '1'), ('BB,aA', 'aA,BB', 'BB'),
             ('aA,1', '1,BB', 'BB'), ('aA,1', '1,aA', 'aA'),
             ('aA,BB', 'BB,1', '1'), ('aA,BB', 'BB,aA', 'aA')]

        TESTS:

        An exception is raised when the degree is less than one::

            sage: G = digraphs.Kautz(0, 2)                                              # needs sage.combinat
            Traceback (most recent call last):
            ...
            ValueError: degree must be greater than or equal to one

            sage: G = digraphs.Kautz(['a'], 2)                                          # needs sage.combinat
            Traceback (most recent call last):
            ...
            ValueError: degree must be greater than or equal to one

        An exception is raised when the diameter of the graph is less than
        one::

            sage: G = digraphs.Kautz(2, 0)                                              # needs sage.combinat
            Traceback (most recent call last):
            ...
            ValueError: diameter must be greater than or equal to one

        :issue:`22355`::

            sage: K = digraphs.Kautz(2, 2, vertices='strings')                          # needs sage.combinat
            sage: K.vertices(sort=True)                                                 # needs sage.combinat
            ['01', '02', '10', '12', '20', '21']
            sage: h = digraphs.Kautz(2, 2, vertices='integers')
            sage: h.vertices(sort=True)
            [0, 1, 2, 3, 4, 5]
            sage: h.is_isomorphic(K)                                                    # needs sage.combinat
            True
            sage: h = digraphs.Kautz([1,'aA','BB'], 2, vertices='integers')
            sage: h.is_isomorphic(K)                                                    # needs sage.combinat
            True
            sage: h.vertices(sort=True)
            [0, 1, 2, 3, 4, 5]
            sage: digraphs.Kautz(2, 2, vertices='circles')
            Traceback (most recent call last):
            ...
            ValueError: unknown type for vertices
        """
    def RandomDirectedAcyclicGraph(self, n, p, weight_max=None, immutable: bool = False):
        """
        Return a random (weighted) directed acyclic graph of order `n`.

        The method starts with the sink vertex and adds vertices one at a time.
        A vertex is connected only to previously defined vertices, and the
        probability of each possible connection is given by the probability `p`.
        The weight of an edge is a random integer between ``1`` and
        ``weight_max``.

        INPUT:

        - ``n`` -- number of nodes of the graph

        - ``p`` -- probability of an edge

        - ``weight_max`` -- (default: ``None``) by default, the returned DAG is
          unweighted. When ``weight_max`` is set to a positive integer, edges
          are assigned a random integer weight between ``1`` and ``weight_max``.

        - ``immutable`` -- boolean (default: ``False``); whether to return an
          immutable or mutable digraph

        EXAMPLES::

            sage: D = digraphs.RandomDirectedAcyclicGraph(5, .5); D
            RandomDAG(5, 0.500000000000000): Digraph on 5 vertices
            sage: D.is_directed_acyclic()
            True
            sage: D = digraphs.RandomDirectedAcyclicGraph(5, .5, weight_max=3); D
            RandomWeightedDAG(5, 0.500000000000000, 3): Digraph on 5 vertices
            sage: D.is_directed_acyclic()
            True

        TESTS:

        Check special cases::

            sage: digraphs.RandomDirectedAcyclicGraph(0, .5).order() == 0
            True
            sage: digraphs.RandomDirectedAcyclicGraph(4, 0).size() == 0
            True
            sage: digraphs.RandomDirectedAcyclicGraph(4, 1).size() == 6
            True

        Check that bad inputs are rejected::

            sage: digraphs.RandomDirectedAcyclicGraph(-1, .5)
            Traceback (most recent call last):
            ...
            ValueError: the number of nodes must be positive or null
            sage: digraphs.RandomDirectedAcyclicGraph(5, 1.1)
            Traceback (most recent call last):
            ...
            ValueError: the probability p must be in [0..1]
            sage: digraphs.RandomDirectedAcyclicGraph(5, .5, weight_max=-1)
            Traceback (most recent call last):
            ...
            ValueError: parameter weight_max must be a positive integer
        """
    def RandomDirectedGN(self, n, kernel=None, seed=None, immutable: bool = False):
        """
        Return a random growing network (GN) digraph with `n` vertices.

        The digraph is constructed by adding vertices with a link to one
        previously added vertex. The vertex to link to is chosen with a
        preferential attachment model, i.e. probability is proportional to
        degree. The default attachment kernel is a linear function of
        degree. The digraph is always a tree, so in particular it is a
        directed acyclic graph. See [KR2001b]_ for more details.

        INPUT:

        - ``n`` -- integer; number of vertices

        - ``kernel`` -- the attachment kernel (default: identity function)

        - ``seed`` -- a ``random.Random`` seed or a Python ``int`` for the
          random number generator (default: ``None``)

        - ``immutable`` -- boolean (default: ``False``); whether to return an
          immutable or mutable digraph

        EXAMPLES::

            sage: # needs networkx
            sage: D = digraphs.RandomDirectedGN(25)
            sage: D.num_verts()
            25
            sage: D.num_edges()
            24
            sage: D.is_connected()
            True
            sage: D.parent() is DiGraph
            True
            sage: D.show()                      # long time
        """
    def RandomDirectedGNC(self, n, seed=None, immutable: bool = False):
        """
        Return a random growing network with copying (GNC) digraph with `n`
        vertices.

        The digraph is constructed by adding vertices with a link to one
        previously added vertex. The vertex to link to is chosen with a
        preferential attachment model, i.e. probability is proportional to
        degree. The new vertex is also linked to all of the previously
        added vertex's successors. See [KR2005]_ for more details.

        INPUT:

        - ``n`` -- integer; number of vertices

        - ``seed`` -- a ``random.Random`` seed or a Python ``int`` for the
          random number generator (default: ``None``)

        - ``immutable`` -- boolean (default: ``False``); whether to return an
          immutable or mutable digraph

        EXAMPLES::

            sage: # needs networkx
            sage: D = digraphs.RandomDirectedGNC(25)
            sage: D.is_directed_acyclic()
            True
            sage: D.topological_sort()
            [24, 23, ..., 1, 0]
            sage: D.show()                      # long time
        """
    def RandomDirectedGNP(self, n, p, loops: bool = False, seed=None, immutable: bool = False):
        """
        Return a random digraph on `n` nodes.

        Each edge is inserted independently with probability `p`.
        See [ER1959]_ and [Gil1959]_ for more details.

        INPUT:

        - ``n`` -- integer; number of nodes of the digraph

        - ``p`` -- float; probability of an edge

        - ``loops`` -- boolean (default: ``False``); whether the random digraph
          may have loops

        - ``seed`` -- integer (default: ``None``); seed for random number
          generator

        - ``immutable`` -- boolean (default: ``False``); whether to return an
          immutable or mutable digraph

        PLOTTING: When plotting, this graph will use the default spring-layout
        algorithm, unless a position dictionary is specified.

        EXAMPLES::

            sage: D = digraphs.RandomDirectedGNP(10, .2)
            sage: D.num_verts()
            10
            sage: D.parent() is DiGraph
            True
        """
    def RandomDirectedGNM(self, n, m, loops: bool = False, immutable: bool = False):
        """
        Return a random labelled digraph on `n` nodes and `m` arcs.

        INPUT:

        - ``n`` -- integer; number of vertices

        - ``m`` -- integer; number of edges

        - ``loops`` -- boolean (default: ``False``); whether to allow loops

        - ``immutable`` -- boolean (default: ``False``); whether to return an
          immutable or mutable digraph

        PLOTTING: When plotting, this graph will use the default spring-layout
        algorithm, unless a position dictionary is specified.

        EXAMPLES::

            sage: D = digraphs.RandomDirectedGNM(10, 5)
            sage: D.num_verts()
            10
            sage: D.num_edges()
            5

        With loops::

            sage: D = digraphs.RandomDirectedGNM(10, 100, loops = True)
            sage: D.num_verts()
            10
            sage: D.loops()
            [(0, 0, None), (1, 1, None), (2, 2, None), (3, 3, None),
             (4, 4, None), (5, 5, None), (6, 6, None), (7, 7, None),
             (8, 8, None), (9, 9, None)]

        TESTS::

            sage: digraphs.RandomDirectedGNM(10,-3)
            Traceback (most recent call last):
            ...
            ValueError: the number of edges must satisfy 0 <= m <= n(n-1) when no loops are allowed, and 0 <= m <= n^2 otherwise

            sage: digraphs.RandomDirectedGNM(10,100)
            Traceback (most recent call last):
            ...
            ValueError: the number of edges must satisfy 0 <= m <= n(n-1) when no loops are allowed, and 0 <= m <= n^2 otherwise
        """
    def RandomDirectedGNR(self, n, p, seed=None, immutable: bool = False):
        """
        Return a random growing network with redirection (GNR) digraph
        with `n` vertices and redirection probability `p`.

        The digraph is constructed by adding vertices with a link to one
        previously added vertex. The vertex to link to is chosen uniformly.
        With probability p, the arc is instead redirected to the successor
        vertex. The digraph is always a tree.
        See [KR2001b]_ for more details.

        INPUT:

        - ``n`` -- integer; number of vertices

        - ``p`` -- redirection probability

        - ``seed`` -- a ``random.Random`` seed or a Python ``int`` for the
          random number generator (default: ``None``)

        - ``immutable`` -- boolean (default: ``False``); whether to return an
          immutable or mutable digraph

        EXAMPLES::

            sage: # needs networkx
            sage: D = digraphs.RandomDirectedGNR(25, .2)
            sage: D.is_directed_acyclic()
            True
            sage: D.to_undirected().is_tree()
            True
            sage: D.show()                      # long time                             # needs sage.plot
        """
    def RandomSemiComplete(self, n, immutable: bool = False):
        """
        Return a random semi-complete digraph on `n` vertices.

        A directed graph `G=(V,E)` is *semi-complete* if for any pair of
        vertices `u` and `v`, there is *at least* one arc between them.

        To generate randomly a semi-complete digraph, we have to ensure, for any
        pair of distinct vertices `u` and `v`, that with probability `1/3` we
        have only arc `uv`, with probability `1/3` we have only arc `vu`, and
        with probability `1/3` we have both arc `uv` and arc `vu`. We do so by
        selecting a random integer `coin` in `[1,3]`. When `coin==1` we select
        only arc `uv`, when `coin==3` we select only arc `vu`, and when
        `coin==2` we select both arcs. In other words, we select arc `uv` when
        `coin\\leq 2` and arc `vu` when `coin\\geq 2`.

        INPUT:

        - ``n`` -- integer; the number of nodes

        - ``immutable`` -- boolean (default: ``False``); whether to return an
          immutable or mutable digraph

        .. SEEALSO::

            - :meth:`~sage.graphs.digraph_generators.DiGraphGenerators.Complete`

            - :meth:`~sage.graphs.digraph_generators.DiGraphGenerators.RandomTournament`

        EXAMPLES::

            sage: SC = digraphs.RandomSemiComplete(10); SC
            Random Semi-Complete digraph: Digraph on 10 vertices
            sage: SC.size() >= binomial(10, 2)                                          # needs sage.symbolic
            True
            sage: digraphs.RandomSemiComplete(-1)
            Traceback (most recent call last):
            ...
            ValueError: the number of vertices cannot be strictly negative
        """
    def __call__(self, vertices=None, property=..., augment: str = 'edges', size=None, sparse: bool = True, copy: bool = True, immutable: bool = False) -> Generator[Incomplete, Incomplete, Incomplete]:
        """
        Access the generator of isomorphism class representatives [McK1998]_.
        Iterates over distinct, exhaustive representatives.

        INPUT:

        - ``vertices`` -- natural number or ``None`` to generate all digraphs

        - ``property`` -- any property to be tested on digraphs before
          generation

        - ``augment`` -- choices:

          - ``'vertices'`` -- augments by adding a vertex, and edges incident to
            that vertex. In this case, all digraphs on up to n=vertices are
            generated. If for any digraph G satisfying the property, every
            subgraph, obtained from G by deleting one vertex and only edges
            incident to that vertex, satisfies the property, then this will
            generate all digraphs with that property. If this does not hold,
            then all the digraphs generated will satisfy the property, but there
            will be some missing.

          - ``'edges'`` -- augments a fixed number of vertices by adding one
            edge. In this case, all digraphs on exactly n=vertices are
            generated. If for any graph G satisfying the property, every
            subgraph, obtained from G by deleting one edge but not the vertices
            incident to that edge, satisfies the property, then this will
            generate all digraphs with that property. If this does not hold,
            then all the digraphs generated will satisfy the property, but there
            will be some missing.

        - ``sparse`` -- boolean (default: ``True``); whether to use a sparse or
          dense data structure. See the documentation of
          :class:`~sage.graphs.graph.Graph`.

        - ``copy`` -- boolean (default: ``True``); whether to make copies of the
          digraphs before returning them. If set to ``False`` the method returns
          the digraph it is working on. The second alternative is faster, but
          modifying any of the digraph instances returned by the method may
          break the function's behaviour, as it is using these digraphs to
          compute the next ones: only use ``copy = False`` when you stick to
          *reading* the digraphs returned.

          This parameter is ignored when ``immutable`` is set to ``True``, in
          which case returned graphs are always copies.

        - ``immutable`` -- boolean (default: ``False``); whether to return
          immutable or mutable digraphs. When set to ``True``, this parameter
          implies ``copy=True``.

        EXAMPLES:

        Print digraphs on 2 or less vertices::

            sage: for D in digraphs(2, augment='vertices'):
            ....:     print(D)
            Digraph on 0 vertices
            Digraph on 1 vertex
            Digraph on 2 vertices
            Digraph on 2 vertices
            Digraph on 2 vertices

        Print digraphs on 3 vertices::

            sage: for D in digraphs(3):
            ....:     print(D)
            Digraph on 3 vertices
            Digraph on 3 vertices
            ...
            Digraph on 3 vertices
            Digraph on 3 vertices

        For more examples, see the class level documentation, or type ::

            sage: digraphs?  # not tested
        """

digraphs: DiGraphGenerators
