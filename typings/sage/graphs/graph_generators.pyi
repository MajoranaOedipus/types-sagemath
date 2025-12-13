from . import graph as graph, strongly_regular_db as strongly_regular_db
from .generators import basic as basic, chessboard as chessboard, classical_geometries as classical_geometries, degree_sequence as degree_sequence, distance_regular as distance_regular, families as families, intersection as intersection, platonic_solids as platonic_solids, random as random, smallgraphs as smallgraphs, world_map as world_map
from _typeshed import Incomplete
from collections.abc import Generator

class GraphGenerators:
    '''
    A class consisting of constructors for several common graphs, as well as
    orderly generation of isomorphism class representatives. See the
    :mod:`module\'s help <sage.graphs.graph_generators>` for a list of supported
    constructors.

    A list of all graphs and graph structures (other than isomorphism class
    representatives) in this database is available via tab completion. Type
    "graphs." and then hit the :kbd:`Tab` key to see which graphs are available.

    The docstrings include educational information about each named
    graph with the hopes that this class can be used as a reference.

    For all the constructors in this class (except the octahedral,
    dodecahedral, random and empty graphs), the position dictionary is
    filled to override the spring-layout algorithm.


    ORDERLY GENERATION::

        graphs(vertices, property=lambda x: True, augment=\'edges\', size=None)

    This syntax accesses the generator of isomorphism class
    representatives. Iterates over distinct, exhaustive
    representatives.

    Also: see the use of the nauty package for generating graphs
    at the :meth:`nauty_geng` method.

    INPUT:

    - ``vertices`` -- a natural number or ``None`` to infinitely generate
      bigger and bigger graphs

    - ``property`` -- (default: ``lambda x: True``) any property to be
      tested on graphs before generation, but note that in general the
      graphs produced are not the same as those produced by using the
      property function to filter a list of graphs produced by using
      the ``lambda x: True`` default. The generation process assumes
      the property has certain characteristics set by the ``augment``
      argument, and only in the case of inherited properties such that
      all subgraphs of the relevant kind (for ``augment=\'edges\'`` or
      ``augment=\'vertices\'``) of a graph with the property also
      possess the property will there be no missing graphs.  (The
      ``property`` argument is ignored if ``degree_sequence`` is
      specified.)

    - ``augment`` -- (default: ``\'edges\'``) possible values:

      - ``\'edges\'`` -- augments a fixed number of vertices by
        adding one edge. In this case, all graphs on *exactly* ``n=vertices`` are
        generated. If for any graph G satisfying the property, every
        subgraph, obtained from G by deleting one edge but not the vertices
        incident to that edge, satisfies the property, then this will
        generate all graphs with that property. If this does not hold, then
        all the graphs generated will satisfy the property, but there will
        be some missing.

      - ``\'vertices\'`` -- augments by adding a vertex and
        edges incident to that vertex. In this case, all graphs *up to*
        ``n=vertices`` are generated. If for any graph G satisfying the
        property, every subgraph, obtained from G by deleting one vertex
        and only edges incident to that vertex, satisfies the property,
        then this will generate all graphs with that property. If this does
        not hold, then all the graphs generated will satisfy the property,
        but there will be some missing.

    - ``size`` -- (default: ``None``) the size of the graph to be generated

    - ``degree_sequence`` -- (default: ``None``) a sequence of nonnegative integers,
      or ``None``. If specified, the generated graphs will have these
      integers for degrees. In this case, property and size are both
      ignored.

    - ``loops`` -- boolean (default: ``False``); whether to allow loops in the graph
      or not

    - ``sparse`` -- (default: ``True``) whether to use a sparse or dense data
      structure. See the documentation of :class:`~sage.graphs.graph.Graph`.

    - ``copy`` -- boolean (default: ``True``); whether to return copies. If set
      to ``False`` the method returns the graph it is working on. The second
      alternative is faster, but modifying any of the graph instances returned
      by the method may break the function\'s behaviour, as it is using these
      graphs to compute the next ones: only use ``copy=False`` when you stick
      to *reading* the graphs returned.

      This parameter is ignored when ``immutable`` is set to ``True``, in which
      case returned graphs are always copies.

    - ``immutable`` -- boolean (default: ``False``); whether to return immutable
      or mutable graphs. When set to ``True``, this parameter implies
      ``copy=True``.

    EXAMPLES:

    Print graphs on 3 or less vertices::

        sage: for G in graphs(3, augment=\'vertices\'):
        ....:     print(G)
        Graph on 0 vertices
        Graph on 1 vertex
        Graph on 2 vertices
        Graph on 3 vertices
        Graph on 3 vertices
        Graph on 3 vertices
        Graph on 2 vertices
        Graph on 3 vertices

    Print graphs on 3 vertices.

    ::

        sage: for G in graphs(3):
        ....:    print(G)
        Graph on 3 vertices
        Graph on 3 vertices
        Graph on 3 vertices
        Graph on 3 vertices

    Generate all graphs with 5 vertices and 4 edges.

    ::

        sage: L = graphs(5, size=4)
        sage: len(list(L))
        6

    Generate all graphs with 5 vertices and up to 4 edges.

    ::

        sage: L = list(graphs(5, lambda G: G.size() <= 4))
        sage: len(L)
        14
        sage: graphs_list.show_graphs(L)        # long time                             # needs sage.plot

    Generate all graphs with up to 5 vertices and up to 4 edges.

    ::

        sage: L = list(graphs(5, lambda G: G.size() <= 4, augment=\'vertices\'))
        sage: len(L)
        31
        sage: graphs_list.show_graphs(L)        # long time                             # needs sage.plot

    Generate all graphs with degree at most 2, up to 6 vertices.

    ::

        sage: property = lambda G: ( max([G.degree(v) for v in G] + [0]) <= 2 )
        sage: L = list(graphs(6, property, augment=\'vertices\'))
        sage: len(L)
        45

    Generate all bipartite graphs on up to 7 vertices: (see
    :oeis:`A033995`)

    ::

        sage: L = list( graphs(7, lambda G: G.is_bipartite(), augment=\'vertices\') )
        sage: [len([g for g in L if g.order() == i]) for i in [1..7]]
        [1, 2, 3, 7, 13, 35, 88]

    Generate all bipartite graphs on exactly 7 vertices::

        sage: L = list( graphs(7, lambda G: G.is_bipartite()) )
        sage: len(L)
        88

    Generate all bipartite graphs on exactly 8 vertices::

        sage: L = list( graphs(8, lambda G: G.is_bipartite()) ) # long time
        sage: len(L)                                            # long time
        303

    Remember that the property argument does not behave as a filter,
    except for appropriately inheritable properties::

        sage: property = lambda G: G.is_vertex_transitive()
        sage: len(list(graphs(4, property)))                                            # needs sage.groups
        1
        sage: sum(1 for g in graphs(4) if property(g))                                  # needs sage.groups
        4

        sage: property = lambda G: G.is_bipartite()
        sage: len(list(graphs(4, property)))
        7
        sage: sum(1 for g in graphs(4) if property(g))
        7

    Generate graphs on the fly: (see :oeis:`A000088`)

    ::

        sage: for i in range(7):
        ....:     print(len(list(graphs(i))))
        1
        1
        2
        4
        11
        34
        156

    Generate all simple graphs, allowing loops: (see :oeis:`A000666`)

    ::

        sage: L = list(graphs(5,augment=\'vertices\',loops=True))               # long time
        sage: for i in [0..5]:  # long time
        ....:     print((i, len([g for g in L if g.order() == i])))
        (0, 1)
        (1, 2)
        (2, 6)
        (3, 20)
        (4, 90)
        (5, 544)

    Generate all graphs with a specified degree sequence (see :oeis:`A002851`)::

        sage: for i in [4,6,8]:  # long time (4s on sage.math, 2012)
        ....:     print((i, len([g for g in graphs(i, degree_sequence=[3]*i) if g.is_connected()])))
        (4, 1)
        (6, 2)
        (8, 5)
        sage: for i in [4,6,8]:  # long time (7s on sage.math, 2012)
        ....:     print((i, len([g for g in graphs(i, augment=\'vertices\', degree_sequence=[3]*i) if g.is_connected()])))
        (4, 1)
        (6, 2)
        (8, 5)

    ::

        sage: print((10, len([g for g in graphs(10,degree_sequence=[3]*10) if g.is_connected()]))) # not tested
        (10, 19)

    Make sure that the graphs are really independent and the generator
    survives repeated vertex removal (:issue:`8458`)::

        sage: for G in graphs(3):
        ....:     G.delete_vertex(0)
        ....:     print(G.order())
        2
        2
        2
        2

    Returned graphs can be mutable or immutable::

        sage: G = next(graphs(3, immutable=False))
        sage: G.delete_vertex(0)
        sage: G = next(graphs(3, immutable=True))
        sage: G.delete_vertex(0)
        Traceback (most recent call last):
        ...
        TypeError: this graph is immutable and so cannot be changed
        sage: G = next(graphs(4, degree_sequence=[3]*4))
        sage: G.delete_vertex(0)
        sage: G = next(graphs(4, degree_sequence=[3]*4, immutable=True))
        sage: G.delete_vertex(0)
        Traceback (most recent call last):
        ...
        TypeError: this graph is immutable and so cannot be changed

    REFERENCE:

    - Brendan D. McKay, Isomorph-Free Exhaustive generation.  *Journal
      of Algorithms*, Volume 26, Issue 2, February 1998, pages 306-324.
    '''
    def __call__(self, vertices=None, property=None, augment: str = 'edges', size=None, degree_sequence=None, loops: bool = False, sparse: bool = True, copy: bool = True, immutable: bool = False) -> Generator[Incomplete, Incomplete, Incomplete]:
        """
        Access the generator of isomorphism class representatives.
        Iterates over distinct, exhaustive representatives. See the docstring
        of this class for full documentation.

        EXAMPLES:

        Print graphs on 3 or less vertices::

            sage: for G in graphs(3, augment='vertices'):
            ....:    print(G)
            Graph on 0 vertices
            Graph on 1 vertex
            Graph on 2 vertices
            Graph on 3 vertices
            Graph on 3 vertices
            Graph on 3 vertices
            Graph on 2 vertices
            Graph on 3 vertices

        ::

            sage: for g in graphs():
            ....:    if g.num_verts() > 3: break
            ....:    print(g)
            Graph on 0 vertices
            Graph on 1 vertex
            Graph on 2 vertices
            Graph on 2 vertices
            Graph on 3 vertices
            Graph on 3 vertices
            Graph on 3 vertices
            Graph on 3 vertices

        For more examples, see the class level documentation, or type::

            sage: graphs? # not tested

        REFERENCE:

        - Brendan D. McKay, Isomorph-Free Exhaustive generation.
          Journal of Algorithms Volume 26, Issue 2, February 1998,
          pages 306-324.
        """
    def nauty_geng(self, options: str = '', debug: bool = False, immutable: bool = False) -> Generator[Incomplete]:
        '''
        Return a generator which creates graphs from nauty\'s geng program.

        INPUT:

        - ``options`` -- string (default: ``\'\'``); a string passed to ``geng``
          as if it was run at a system command line. At a minimum, you *must*
          pass the number of vertices you desire.  Sage expects the graphs to be
          in nauty\'s "graph6" format, do not set an option to change this
          default or results will be unpredictable.

        - ``debug`` -- boolean (default: ``False``); if ``True`` the first line
          of ``geng``\'s output to standard error is captured and the first call
          to the generator\'s ``next()`` function will return this line as a
          string.  A line leading with ">A" indicates a successful initiation of
          the program with some information on the arguments, while a line
          beginning with ">E" indicates an error with the input.

        - ``immutable`` -- boolean (default: ``False``); whether to return
          immutable or mutable graphs

        The possible options, obtained as output of ``geng --help``::

                 n       : the number of vertices
            mine:maxe    : <int>:<int> a range for the number of edges
                            <int>:0 means \'<int> or more\' except in the case 0:0
              res/mod : only generate subset res out of subsets 0..mod-1

                -c       : only write connected graphs
                -C       : only write biconnected graphs
                -t       : only generate triangle-free graphs
                -f       : only generate 4-cycle-free graphs
                -b       : only generate bipartite graphs
                              (-t, -f and -b can be used in any combination)
                -m       : save memory at the expense of time (only makes a
                              difference in the absence of -b, -t, -f and n <= 28).
                -d<int>  : a lower bound for the minimum degree
                -D<int>  : a upper bound for the maximum degree
                -v       : display counts by number of edges
                -l       : canonically label output graphs

                -q       : suppress auxiliary output (except from -v)

        Options which cause ``geng`` to use an output format different than the
        graph6 format are not listed above (-u, -g, -s, -y, -h) as they will
        confuse the creation of a Sage graph.  The res/mod option can be useful
        when using the output in a routine run several times in parallel.

        OUTPUT:

        A generator which will produce the graphs as Sage graphs.
        These will be simple graphs: no loops, no multiple edges, no
        directed edges.

        .. SEEALSO::

            :meth:`Graph.is_strongly_regular` -- tests whether a graph is
            strongly regular and/or returns its parameters.

        EXAMPLES:

        The generator can be used to construct graphs for testing,
        one at a time (usually inside a loop).  Or it can be used to
        create an entire list all at once if there is sufficient memory
        to contain it.  ::

            sage: gen = graphs.nauty_geng("2")
            sage: next(gen)
            Graph on 2 vertices
            sage: next(gen)
            Graph on 2 vertices
            sage: next(gen)
            Traceback (most recent call last):
            ...
            StopIteration

        A list of all graphs on 7 vertices.  This agrees with
        :oeis:`A000088`.  ::

            sage: gen = graphs.nauty_geng("7")
            sage: len(list(gen))
            1044

        A list of just the connected graphs on 7 vertices.  This agrees with
        :oeis:`A001349`.  ::

            sage: gen = graphs.nauty_geng("7 -c")
            sage: len(list(gen))
            853

        A list of connected degree exactly 2 graphs on 5 vertices. ::

            sage: gen = graphs.nauty_geng("5 -c -d2 -D2")
            sage: len(list(gen))
            1

        The ``debug`` switch can be used to examine ``geng``\'s reaction to the
        input in the ``options`` string.  We illustrate success.  (A failure
        will be a string beginning with ">E".)  Passing the "-q" switch to
        ``geng`` will suppress the indicator of a successful initiation, and so
        the first returned value might be an empty string if ``debug`` is
        ``True``::

            sage: gen = graphs.nauty_geng("4", debug=True)
            sage: print(next(gen))
            >A ...geng -d0D3 n=4 e=0-6
            sage: gen = graphs.nauty_geng("4 -q", debug=True)
            sage: next(gen)
            \'\'

        TESTS:

        Wrong input, ``"-c3"`` instead of ``"-c 3"`` (:issue:`14068`)::

            sage: list(graphs.nauty_geng("-c3", debug=False))
            Traceback (most recent call last):
            ...
            ValueError: wrong format of parameter option
            sage: list(graphs.nauty_geng("-c3", debug=True))
            [\'>E Usage: ...geng ...\\n\']
            sage: list(graphs.nauty_geng("-c 3", debug=True))
            [\'>A ...geng -cd1D2 n=3 e=2-3\\n\', Graph on 3 vertices, Graph on 3 vertices]
        '''
    def nauty_genbg(self, options: str = '', debug: bool = False, immutable: bool = False) -> Generator[Incomplete]:
        '''
        Return a generator which creates bipartite graphs from nauty\'s ``genbgL``
        program.

        INPUT:

        - ``options`` -- string (default: ``""``); a string passed to ``genbgL``
          as if it was run at a system command line. At a minimum, you *must*
          pass the number of vertices you desire in each side. Sage expects the
          bipartite graphs to be in nauty\'s "graph6" format, do not set an
          option to change this default or results will be unpredictable.

        - ``debug`` -- boolean (default: ``False``); if ``True`` the first line
          of ``geng``\'s output to standard error is captured and the first call
          to the generator\'s ``next()`` function will return this line as a
          string. A line leading with ">A" indicates a successful initiation of
          the program with some information on the arguments, while a line
          beginning with ">E" indicates an error with the input.

        - ``immutable`` -- boolean (default: ``False``); whether to return
          immutable or mutable graphs

        The possible options, obtained as output of ``genbgL --help``::

                n1       : the number of vertices in the first class.
                           We must have n1=1..30.
                n2       : the number of vertices in the second class.
                           We must have n2=0..64 and n1+n2=1..64.
            mine:maxe    : <int>:<int> a range for the number of edges
                            <int>:0 means \'<int> or more\' except in the case 0:0
              res/mod    : only generate subset res out of subsets 0..mod-1
                -c       : only write connected graphs
                -z       : all the vertices in the second class must have
                           different neighbourhoods
                -F       : the vertices in the second class must have at least
                           two neighbours of degree at least 2
                -L       : there is no vertex in the first class whose removal
                           leaves the vertices in the second class unreachable
                           from each other
                -Y<int>  : two vertices in the second class must have at least
                           <int> common neighbours
                -Z<int>  : two vertices in the second class must have at most
                           <int> common neighbours
                -A       : no vertex in the second class has a neighbourhood
                           which is a subset of another vertex\'s neighbourhood
                           in the second class
                -D<int>  : specify an upper bound for the maximum degree
                           Example: -D6. You can also give separate maxima for
                           the two parts, for example: -D5:6
                -d<int>  : specify a lower bound for the minimum degree
                           Again, you can specify it separately for the two parts,
                           for example -d1:2
                -v       : display counts by number of edges to stderr
                -l       : canonically label output graphs

        Options which cause ``genbgL`` to use an output format different than
        the ``graph6`` format are not listed above (``-s``, ``-a``) as they will
        confuse the creation of a Sage graph. Option ``-q`` which suppress
        auxiliary output (except from ``-v``) should never be used as we are
        unable to recover the partition of the vertices of the bipartite graph
        without the auxiliary output. Hence the partition of the vertices of
        returned bipartite graphs might not respect the requirement.

        The res/mod option can be useful when using the output in a routine run
        several times in parallel.

        OUTPUT:

        A generator which will produce the graphs as
        :class:`~sage/graphs.bipartite_graph.BipartiteGraph`. These will be
        simple bipartite graphs: no loops, no multiple edges, no directed edges.

        EXAMPLES:

        The generator can be used to construct bipartite graphs for testing,
        one at a time (usually inside a loop).  Or it can be used to
        create an entire list all at once if there is sufficient memory
        to contain it::

            sage: gen = graphs.nauty_genbg("1 1")
            sage: next(gen)
            Bipartite graph on 2 vertices
            sage: next(gen)
            Bipartite graph on 2 vertices
            sage: next(gen)
            Traceback (most recent call last):
            ...
            StopIteration

        Connected bipartite graphs of order 6 with different number of vertices
        in each side::

            sage: gen = graphs.nauty_genbg("1 5 -c")
            sage: len(list(gen))
            1
            sage: gen = graphs.nauty_genbg("2 4 -c")
            sage: len(list(gen))
            6
            sage: gen = graphs.nauty_genbg("3 3 -c")
            sage: len(list(gen))
            13

        Use :meth:`nauty_geng` instead if you want the list of all bipartite
        graphs of order `n`. For instance, the list of all connected bipartite
        graphs of order 6, which agrees with :oeis:`A005142`::

            sage: gen = graphs.nauty_geng("-b -c 6")
            sage: len(list(gen))
            17

        The ``debug`` switch can be used to examine ``genbgL``\'s reaction to the
        input in the ``options`` string. A message starting with ">A" indicates
        success and a message starting with ">E" indicates a failure::

            sage: gen = graphs.nauty_genbg("2 3", debug=True)
            sage: print(next(gen))
            >A ...genbg... n=2+3 e=0:6 d=0:0 D=3:2
            sage: gen = graphs.nauty_genbg("-c2 3", debug=True)
            sage: next(gen)
            \'>E Usage: ...genbg... [-c -ugs -vq -lzF] [-Z#] [-D#] [-A] [-d#|-d#:#] [-D#|-D#:#] n1 n2...

        Check that the partition of the bipartite graph is consistent::

            sage: gen = graphs.nauty_genbg("3 3")
            sage: left = set(range(3))
            sage: for g in gen:
            ....:     if g.left != left:
            ....:         raise ValueError(\'wrong partition\')

        TESTS:

        Wrong input::

            sage: list(graphs.nauty_genbg("-c1 2", debug=False))
            Traceback (most recent call last):
            ...
            ValueError: wrong format of parameter options
            sage: list(graphs.nauty_genbg("-c1 2", debug=True))
            [\'>E Usage: ...genbg... [-c -ugs -vq -lzF] [-Z#] [-D#] [-A] [-d#|-d#:#] [-D#|-D#:#] n1 n2...
            sage: list(graphs.nauty_genbg("-c 1 2", debug=True))
            [\'>A ...genbg... n=1+2 e=2:2 d=1:1 D=2:1 c...\\n\', Bipartite graph on 3 vertices]

        We must have n1=1..30, n2=0..64 and n1+n2=1..64 (:issue:`34179`,
        :issue:`38618`)::

            sage: next(graphs.nauty_genbg("31 1", debug=False))
            Traceback (most recent call last):
            ...
            ValueError: wrong format of parameter options
            sage: next(graphs.nauty_genbg("31 1", debug=True))
            \'>E ...genbg...: must have n1=1..30, n1+n2=1..64...
            sage: next(graphs.nauty_genbg("30 40", debug=True))
            \'>E ...genbg...: must have n1=1..30, n1+n2=1..64...
            sage: next(graphs.nauty_genbg("1 63", debug=False))
            Bipartite graph on 64 vertices
            sage: next(graphs.nauty_genbg("1 64", debug=True))
            \'>E ...genbg...: must have n1=1..30, n1+n2=1..64...
            sage: next(graphs.nauty_genbg("0 2", debug=True))
            \'>E ...genbg...: must have n1=1..30, n1+n2=1..64...
            sage: next(graphs.nauty_genbg("2 0", debug=False))
            Bipartite graph on 2 vertices
            sage: next(graphs.nauty_genbg("2 -1", debug=True))
            \'>E Usage: ...genbg... [-c -ugs -vq -lzF] [-Z#] [-D#] [-A] [-d#|-d#:#] [-D#|-D#:#] n1 n2...
        '''
    def nauty_genktreeg(self, options: str = '', debug: bool = False, immutable: bool = False) -> Generator[Incomplete]:
        '''
        Return a generator which creates all `k`-trees using nauty..

        A `k`-tree is an undirected graph formed by starting with a complete
        graph on `k + 1` vertices and then repeatedly add vertices in such a
        way that each added vertex `v` has exactly `k` neighbors `U` such that,
        together, the `k + 1` vertices formed by `v` and `U` form a clique.
        See the :wikipedia:`K-tree` for more details.

        INPUT:

        - ``options`` -- string (default: ``""``); a string passed to
          ``genktreeg`` as if it was run at a system command line. At a minimum,
          you *must* pass the number of vertices you desire. Sage expects the
          graphs to be in nauty\'s "graph6" format, do not set an option to
          change this default or results will be unpredictable.

        - ``debug`` -- boolean (default: ``False``); if ``True`` the first line
          of ``genktreeg``\'s output to standard error is captured and the first
          call to the generator\'s ``next()`` function will return this line as a
          string. A line leading with ">A" indicates a successful initiation of
          the program with some information on the arguments, while a line
          beginning with ">E" indicates an error with the input.

        - ``immutable`` -- boolean (default: ``False``); whether to return
          immutable or mutable graphs

        The possible options, obtained as output of ``genktreeg --help``::

                 n       : the number of vertices
                -k<int>  : the value of `k`(default: 2)
              res/mod    : only generate subset res out of subsets 0..mod-1
                -l       : canonically label output graphs

        Options which cause ``genktreeg`` to use an output format different than
        the graph6 format are not listed above (-u, -s, -h) as they will confuse
        the creation of a Sage graph. The res/mod option can be useful when
        using the output in a routine run several times in parallel.

        OUTPUT:

        A generator which will produce the graphs as Sage graphs.
        These will be simple graphs: no loops, no multiple edges, no
        directed edges.

        EXAMPLES:

        A `k`-tree is a maximal graph with treewidth `k`::

            sage: # needs nauty
            sage: gen = graphs.nauty_genktreeg("10 -k4")
            sage: G = next(gen); G
            Graph on 10 vertices
            sage: G.treewidth()
            4

        A list of all 2-trees with 6, 7 and 8 vertices. This agrees with
        :oeis:`A054581`::

            sage: # needs nauty
            sage: gen = graphs.nauty_genktreeg("6")
            sage: len(list(gen))
            5
            sage: gen = graphs.nauty_genktreeg("7")
            sage: len(list(gen))
            12
            sage: gen = graphs.nauty_genktreeg("8")
            sage: len(list(gen))
            39

        The ``debug`` switch can be used to examine ``geng``\'s reaction to the
        input in the ``options`` string.  We illustrate success.  (A failure
        will be a string beginning with ">E".)  Passing the "-q" switch to
        ``geng`` will suppress the indicator of a successful initiation, and so
        the first returned value might be an empty string if ``debug`` is
        ``True``::

            sage: gen = graphs.nauty_genktreeg("7", debug=True)                         # needs nauty
            sage: print(next(gen))                                                      # needs nauty
            >A ...genktreeg k=2 n=7

        TESTS:

        Wrong input::

            sage: # needs nauty
            sage: list(graphs.nauty_genktreeg("4 -k5", debug=True))
            [\'>E genktreeg: n cannot be less than k\\n\']
            sage: list(graphs.nauty_genktreeg("10 -k 4", debug=True))
            [\'>E genktreeg -k: missing argument value\\n\']
            sage: list(graphs.nauty_genktreeg("-c3", debug=False))
            Traceback (most recent call last):
            ...
            ValueError: wrong format of parameter option
        '''
    def cospectral_graphs(self, vertices, matrix_function=None, graphs=None, immutable: bool = False):
        """
        Find all sets of graphs on ``vertices`` vertices (with
        possible restrictions) which are cospectral with respect to a
        constructed matrix.

        INPUT:

        - ``vertices`` -- the number of vertices in the graphs to be tested

        - ``matrix_function`` -- a function taking a graph and giving back
          a matrix.  This defaults to the adjacency matrix.  The spectra
          examined are the spectra of these matrices.

        - ``graphs`` -- one of three things:

           - ``None`` -- default; test all graphs having ``vertices``
             vertices

           - a function taking a graph and returning ``True`` or ``False``
             - test only the graphs on ``vertices`` vertices for which
             the function returns ``True``

           - a list of graphs (or other iterable object) -- these graphs
             are tested for cospectral sets.  In this case,
             ``vertices`` is ignored.

        - ``immutable`` -- boolean (default: ``False``); whether to return
          immutable or mutable graphs

        OUTPUT:

           A list of lists of graphs.  Each sublist will be a list of
           cospectral graphs (lists of cardinality 1 being omitted).

        .. SEEALSO::

            :meth:`Graph.is_strongly_regular` -- tests whether a graph is
            strongly regular and/or returns its parameters.

        EXAMPLES::

            sage: g = graphs.cospectral_graphs(5)                                       # needs sage.modules
            sage: sorted(sorted(g.graph6_string() for g in glist) for glist in g)       # needs sage.modules
            [['Dr?', 'Ds_']]
            sage: g[0][1].am().charpoly()==g[0][1].am().charpoly()                      # needs sage.modules
            True

        There are two sets of cospectral graphs on six vertices with no isolated vertices::

            sage: # needs sage.modules
            sage: g = graphs.cospectral_graphs(6, graphs=lambda x: min(x.degree())>0)
            sage: sorted(sorted(g.graph6_string() for g in glist) for glist in g)
            [['Ep__', 'Er?G'], ['ExGg', 'ExoG']]
            sage: g[0][1].am().charpoly()==g[0][1].am().charpoly()
            True
            sage: g[1][1].am().charpoly()==g[1][1].am().charpoly()
            True

        There is one pair of cospectral trees on eight vertices::

            sage: g = graphs.cospectral_graphs(6, graphs=graphs.trees(8))               # needs sage.modules
            sage: sorted(sorted(g.graph6_string() for g in glist) for glist in g)       # needs sage.modules
            [['GiPC?C', 'GiQCC?']]
            sage: g[0][1].am().charpoly()==g[0][1].am().charpoly()                      # needs sage.modules
            True

        There are two sets of cospectral graphs (with respect to the
        Laplacian matrix) on six vertices::

            sage: # needs sage.modules
            sage: g = graphs.cospectral_graphs(6, matrix_function=lambda g: g.laplacian_matrix())
            sage: sorted(sorted(g.graph6_string() for g in glist) for glist in g)
            [['Edq_', 'ErcG'], ['Exoo', 'EzcG']]
            sage: g[0][1].laplacian_matrix().charpoly()==g[0][1].laplacian_matrix().charpoly()
            True
            sage: g[1][1].laplacian_matrix().charpoly()==g[1][1].laplacian_matrix().charpoly()
            True

        To find cospectral graphs with respect to the normalized
        Laplacian, assuming the graphs do not have an isolated vertex, it
        is enough to check the spectrum of the matrix `D^{-1}A`, where `D`
        is the diagonal matrix of vertex degrees, and A is the adjacency
        matrix.  We find two such cospectral graphs (for the normalized
        Laplacian) on five vertices::

            sage: def DinverseA(g):
            ....:   A = g.adjacency_matrix().change_ring(QQ)
            ....:   for i in range(g.order()):
            ....:       A.rescale_row(i, 1 / len(A.nonzero_positions_in_row(i)))
            ....:   return A
            sage: g = graphs.cospectral_graphs(5, matrix_function=DinverseA,            # needs sage.libs.pari sage.modules
            ....:                              graphs=lambda g: min(g.degree()) > 0)
            sage: sorted(sorted(g.graph6_string() for g in glist) for glist in g)       # needs sage.modules
            [['Dlg', 'Ds_']]
            sage: (g[0][1].laplacian_matrix(normalized=True).charpoly()                 # needs sage.modules sage.symbolic
            ....:   == g[0][1].laplacian_matrix(normalized=True).charpoly())
            True
        """
    def fullerenes(self, order, ipr: bool = False, immutable: bool = False) -> Generator[Incomplete, Incomplete]:
        """
        Return a generator which creates fullerene graphs using
        the buckygen generator (see [BGM2012]_).

        INPUT:

        - ``order`` -- a positive even integer smaller than or equal to 254
          This specifies the number of vertices in the generated fullerenes

        - ``ipr`` -- boolean (default: ``False``); if ``True`` only fullerenes
          that satisfy the Isolated Pentagon Rule are generated. This means that
          no pentagonal faces share an edge.

        - ``immutable`` -- boolean (default: ``False``); whether to return
          immutable or mutable graphs

        OUTPUT:

        A generator which will produce the fullerene graphs as Sage graphs
        with an embedding set. These will be simple graphs: no loops, no
        multiple edges, no directed edges.

        .. SEEALSO::

            - :meth:`~sage.graphs.generic_graph.GenericGraph.set_embedding`,
              :meth:`~sage.graphs.generic_graph.GenericGraph.get_embedding` --
              get/set methods for embeddings.

        EXAMPLES:

        There are 1812 isomers of `\\textrm{C}_{60}`, i.e., 1812 fullerene graphs
        on 60 vertices::

            sage: gen = graphs.fullerenes(60)  # optional - buckygen
            sage: len(list(gen))               # optional - buckygen
            1812

        However, there is only one IPR fullerene graph on 60 vertices: the famous
        Buckminster Fullerene::

            sage: gen = graphs.fullerenes(60, ipr=True)  # optional - buckygen
            sage: next(gen)                              # optional - buckygen
            Graph on 60 vertices
            sage: next(gen)                              # optional - buckygen
            Traceback (most recent call last):
            ...
            StopIteration

        The unique fullerene graph on 20 vertices is isomorphic to the dodecahedron
        graph. ::

            sage: # optional - buckygen
            sage: gen = graphs.fullerenes(20)
            sage: g = next(gen)
            sage: g.is_isomorphic(graphs.DodecahedralGraph())
            True
            sage: g.get_embedding()
            {1: [2, 3, 4],
             2: [1, 5, 6],
             3: [1, 7, 8],
             4: [1, 9, 10],
             5: [2, 10, 11],
             6: [2, 12, 7],
             7: [3, 6, 13],
             8: [3, 14, 9],
             9: [4, 8, 15],
             10: [4, 16, 5],
             11: [5, 17, 12],
             12: [6, 11, 18],
             13: [7, 18, 14],
             14: [8, 13, 19],
             15: [9, 19, 16],
             16: [10, 15, 17],
             17: [11, 16, 20],
             18: [12, 20, 13],
             19: [14, 20, 15],
             20: [17, 19, 18]}
            sage: g.plot3d(layout='spring')
            Graphics3d Object
        """
    def fusenes(self, hexagon_count, benzenoids: bool = False, immutable: bool = False) -> Generator[Incomplete, Incomplete]:
        """
        Return a generator which creates fusenes and benzenoids using
        the benzene generator (see [BCH2002]_). Fusenes are planar
        polycyclic hydrocarbons with all bounded faces hexagons. Benzenoids
        are fusenes that are subgraphs of the hexagonal lattice.

        INPUT:

        - ``hexagon_count`` -- positive integer smaller than or equal to 30;
          this specifies the number of hexagons in the generated benzenoids

        - ``benzenoids`` -- boolean (default: ``False``); if ``True`` only
          benzenoids are generated

        - ``immutable`` -- boolean (default: ``False``); whether to return
          immutable or mutable graphs

        OUTPUT:

        A generator which will produce the fusenes as Sage graphs
        with an embedding set. These will be simple graphs: no loops, no
        multiple edges, no directed edges.

        .. SEEALSO::

            - :meth:`~sage.graphs.generic_graph.GenericGraph.set_embedding`,
              :meth:`~sage.graphs.generic_graph.GenericGraph.get_embedding` --
              get/set methods for embeddings.

        EXAMPLES:

        There is a unique fusene with 2 hexagons::

            sage: gen = graphs.fusenes(2)  # optional - benzene
            sage: len(list(gen))           # optional - benzene
            1

        This fusene is naphthalene (`\\textrm{C}_{10}\\textrm{H}_{8}`).
        In the fusene graph the H-atoms are not stored, so this is
        a graph on just 10 vertices::

            sage: gen = graphs.fusenes(2)  # optional - benzene
            sage: next(gen)                # optional - benzene
            Graph on 10 vertices
            sage: next(gen)                # optional - benzene
            Traceback (most recent call last):
            ...
            StopIteration

        There are 6505 benzenoids with 9 hexagons::

            sage: gen = graphs.fusenes(9, benzenoids=True)  # optional - benzene
            sage: len(list(gen))                            # optional - benzene
            6505
        """
    def plantri_gen(self, options: str = '', immutable: bool = False) -> Generator[Incomplete, Incomplete]:
        '''
        Iterator over planar graphs created using the ``plantri`` generator.

        ``plantri`` is a (optional) program that generates certain types of
        graphs that are embedded on the sphere. It outputs exactly one member of
        each isomorphism class, using an amount of memory almost independent of
        the number of graphs produced. Isomorphisms are defined with respect to
        the embeddings, so in some cases outputs may be isomorphic as abstract
        graphs.

        This method allows for passing command directly to ``plantry``,
        similarly to method :meth:`nauty_geng`, provide that the output format
        is not changed.

        INPUT:

        - ``options`` -- string (default: ``""``); a string passed to
          ``plantri`` as if it was run at a system command line. At a minimum,
          you *must* pass the number of vertices you desire. Sage expects the
          output of plantri to be in "planar code" format, so do not set an
          option to change this default or results will be unpredictable.

        - ``immutable`` -- boolean (default: ``False``); whether to return
          immutable or mutable graphs

        The possible options are::

            n       : the number of vertices (the only compulsory parameter).
                      This number must be in range `3\\cdots 64`.
                      It can also be given as "nd", where the suffix "d" means
                      "dual", in which case it is converted by adding 4 then
                      dividing by 2, i.e., `(28+4)/2 = 16`. In the case of
                      triangulations, this calculation yields the number of
                      faces, which is the number of vertices in the dual cubic
                      graph.

            -d      : output the dual instead of the original graph.
                      Note that it is applied only at the output stage. All
                      other switches refer to the original graph before the dual
                      is taken.

            -o      : Normally, one member of each isomorphism class is written.
                      If this switch is given, one member of each O-P
                      isomorphism class is written.

            -V      : output only graphs with non-trivial group. If -o is
                      given the O-P group is used, the full group otherwise.

            -m<int> : lower bound on the minimum degree. The default is -m3.
                      In the dual graph, this means a lower bound on the minimum
                      face size.

            -c<int> : lower bound on the connectivity. The default is -c3.

            -x      : when used in combination with -cN, the connectivity must
                      be exactly N rather than at least N.

            -e      : used to specify bounds on the number of edges.
                      There are four possible forms:
                          -e<int>        exactly <int> edges
                          -e:<int>       at most <int> edges
                          -e<int>:       at least <int> edges
                          -e<int>:<int>  between <int> and <int> edges

            -f<int> : upper bound on the size of a face, and so on the maximum
                      degree of the dual.

            -b but not -p : select eulerian triangulations, where "eulerian"
                            means that every vertex has even degree.
                            This parameter can be used in combination with
                            parameters -c and -x.

            -p but not -b : select general planar simple graphs.
                            This parameter can be used in combination with
                            parameters -m, -c, -x, -e and -f.

            -bp or -pb    : select general planar simple bipartite graphs.
                            This parameter can be used in combination with
                            parameters -m, -c, -x, -e and -f, except -c4, -m4,
                            -m5 and -f3.

            -P<int> : select triangulations of a disk. These are embedded simple
                      graphs with a distinguished "outer" face. The outer face
                      can be of any size (here called the disk size) but the
                      other faces must be triangles.  The argument <int> to -P
                      is the disk size. If no argument (or 0) is given, all disk
                      sizes are permitted.
                      This parameter can be used in combination with
                      parameters -m, -c, and -x.

            -q      : select simple quadrangulations. These are planar simple
                      graphs for which every face has length 4.
                      This parameter can be used in combination with parameters
                      -c and -m.

            -A      : select Appolonian networks. These are simple planar
                      triangulations that can be formed starting with `K_4` then
                      repeatedly dividing a face into three by addition of a new
                      vertex. They all have minimum degree and connectivity
                      equal to 3.

            res/mod : only generate subset res out of subsets 0..mod-1.
                      The set of objects is divided into mod disjoint classes
                      and only the res-th class is generated.

        If -b, -q, -p, -P and -A are absent, the graphs found are triangulations
        only restricted by connectivity and minimum degree. In this case,
        there is the possibility of connectivity lower than 3.

        Other options listed in the ``plantri`` guide might cause unpredictable
        behavior, in particular those changing the output format of ``plantri``
        as they will confuse the creation of a Sage graph.

        OUTPUT:

        An iterator which yields the graphs generated by ``plantri`` as Sage
        :class:`~sage.graphs.graph.Graph`.

        .. SEEALSO::

            - :meth:`planar_graphs` -- iterator over connected planar graphs
              using the ``plantri`` generator
            - :meth:`triangulations` -- iterator over connected planar
              triangulations using the ``plantri`` generator
            - :meth:`quadrangulations` -- iterator over connected planar
              quadrangulations using the ``plantri`` generator

        EXAMPLES:

        The generator can be used to construct graphs for testing, one at a time
        (usually inside a loop). Or it can be used to create an entire list all
        at once if there is sufficient memory to contain it::

            sage: # optional - plantri
            sage: gen = graphs.plantri_gen("6")
            sage: next(gen)
            Graph on 6 vertices
            sage: next(gen)
            Graph on 6 vertices
            sage: next(gen)
            Traceback (most recent call last):
            ...
            StopIteration

        An overview of the number of quadrangulations on up to 12 vertices. This
        agrees with :oeis:`A113201`::

            sage: for i in range(4, 13):                        # optional - plantri
            ....:     cmd = \'-qm2c2 {}\'.format(i)
            ....:     L = len(list(graphs.plantri_gen(cmd)))
            ....:     print("{:2d}   {:3d}".format(i, L))
             4     1
             5     1
             6     2
             7     3
             8     9
             9    18
            10    62
            11   198
            12   803

        TESTS:

        Wrong input, ``"-c=3"`` instead of ``"-c3"``::

            sage: list(graphs.plantri_gen("6 -c3"))  # optional - plantri
            [Graph on 6 vertices, Graph on 6 vertices]
            sage: list(graphs.plantri_gen("6 -c=3"))  # optional - plantri
            Traceback (most recent call last):
            ...
            AttributeError: invalid options \'6 -c=3\'
        '''
    def planar_graphs(self, order, minimum_degree=None, minimum_connectivity=None, exact_connectivity: bool = False, minimum_edges=None, maximum_edges=None, maximum_face_size=None, only_bipartite: bool = False, dual: bool = False, immutable: bool = False) -> Generator[Incomplete, Incomplete]:
        """
        An iterator over connected planar graphs using the plantri generator.

        This uses the plantri generator (see [BM2007]_) which is available
        through the optional package plantri.

        .. NOTE::

            The non-3-connected graphs will be returned several times, with all
            its possible embeddings.

        INPUT:

        - ``order`` -- positive integer smaller than or equal to 64;
          this specifies the number of vertices in the generated graphs

        - ``minimum_degree`` -- (default: ``None``) a value `\\geq 1` and `\\leq
          5`, or ``None``. This specifies the minimum degree of the generated
          graphs. If this is ``None`` and the order is 1, then this is set to
          0. If this is ``None`` and the minimum connectivity is specified, then
          this is set to the same value as the minimum connectivity.  If the
          minimum connectivity is also equal to ``None``, then this is set to 1.

        - ``minimum_connectivity`` -- (default: ``None``) a value `\\geq 1`
          and `\\leq 3`, or ``None``. This specifies the minimum connectivity of the
          generated graphs. If this is ``None`` and the minimum degree is
          specified, then this is set to the minimum of the minimum degree
          and 3. If the minimum degree is also equal to ``None``, then this
          is set to 1.

        - ``exact_connectivity`` -- (default: ``False``) if ``True`` only
          graphs with exactly the specified connectivity will be generated.
          This option cannot be used with ``minimum_connectivity=3``, or if
          the minimum connectivity is not explicitly set.

        - ``minimum_edges`` -- integer (default: ``None``); lower bound on the
          number of edges

        - ``maximum_edges`` -- integer (default: ``None``); upper bound on the
          number of edges

        - ``maximum_face_size`` -- integer (default: ``None``); upper bound on
          the size of a face and so on the maximum degree of the dual graph

        - ``only_bipartite`` -- (default: ``False``) if ``True`` only bipartite
          graphs will be generated. This option cannot be used for graphs with
          a minimum degree larger than 3.

        - ``dual`` -- (default: ``False``) if ``True`` return instead the
          planar duals of the generated graphs

        - ``immutable`` -- boolean (default: ``False``); whether to return
          immutable or mutable graphs

        OUTPUT:

        An iterator which will produce all planar graphs with the given
        number of vertices as Sage graphs with an embedding set. These will be
        simple graphs (no loops, no multiple edges, no directed edges)
        unless the option ``dual=True`` is used.

        .. SEEALSO::

            - :meth:`~sage.graphs.generic_graph.GenericGraph.set_embedding`,
              :meth:`~sage.graphs.generic_graph.GenericGraph.get_embedding` --
              get/set methods for embeddings.

        EXAMPLES:

        There are 6 planar graphs on 4 vertices::

            sage: gen = graphs.planar_graphs(4)  # optional - plantri
            sage: len(list(gen))                 # optional - plantri
            6

        Three of these planar graphs are bipartite::

            sage: gen = graphs.planar_graphs(4, only_bipartite=True)  # optional - plantri
            sage: len(list(gen))                                      # optional - plantri
            3

        Setting ``dual=True`` gives the planar dual graphs::

            sage: gen = graphs.planar_graphs(4, dual=True)  # optional - plantri
            sage: [u for u in list(gen)]                    # optional - plantri
            [Graph on 4 vertices,
            Multi-graph on 3 vertices,
            Multi-graph on 2 vertices,
            Looped multi-graph on 2 vertices,
            Looped multi-graph on 1 vertex,
            Looped multi-graph on 1 vertex]

        The cycle of length 4 is the only 2-connected bipartite planar graph
        on 4 vertices::

            sage: l = list(graphs.planar_graphs(4, minimum_connectivity=2, only_bipartite=True))  # optional - plantri
            sage: l[0].get_embedding()                                                            # optional - plantri
            {1: [2, 3],
             2: [1, 4],
             3: [1, 4],
             4: [2, 3]}

        There is one planar graph with one vertex. This graph obviously has
        minimum degree equal to 0::

            sage: list(graphs.planar_graphs(1))                    # optional - plantri
            [Graph on 1 vertex]
            sage: list(graphs.planar_graphs(1, minimum_degree=1))  # optional - plantri
            []

        Specifying lower and upper bounds on the number of edges::

            sage: # optional - plantri
            sage: len(list(graphs.planar_graphs(4)))
            6
            sage: len(list(graphs.planar_graphs(4, minimum_edges=4)))
            4
            sage: len(list(graphs.planar_graphs(4, maximum_edges=4)))
            4
            sage: len(list(graphs.planar_graphs(4, minimum_edges=4, maximum_edges=4)))
            2

        Specifying the maximum size of a face::

            sage: len(list(graphs.planar_graphs(4, maximum_face_size=3)))  # optional - plantri
            1
            sage: len(list(graphs.planar_graphs(4, maximum_face_size=4)))  # optional - plantri
            3

        TESTS:

        The number of edges in a planar graph is equal to the number of edges in
        its dual::

            sage: # optional - plantri
            sage: planar      = list(graphs.planar_graphs(5,dual=True))
            sage: dual_planar = list(graphs.planar_graphs(5,dual=False))
            sage: planar_sizes      = [g.size() for g in planar]
            sage: dual_planar_sizes = [g.size() for g in dual_planar]
            sage: planar_sizes == dual_planar_sizes
            True
        """
    def triangulations(self, order, minimum_degree=None, minimum_connectivity=None, exact_connectivity: bool = False, only_eulerian: bool = False, dual: bool = False, immutable: bool = False) -> Generator[Incomplete, Incomplete]:
        '''
        An iterator over connected planar triangulations using the plantri generator.

        This uses the plantri generator (see [BM2007]_) which is available
        through the optional package plantri.

        INPUT:

        - ``order`` -- positive integer smaller than or equal to 64;
          this specifies the number of vertices in the generated triangulations

        - ``minimum_degree`` -- (default: ``None``) a value `\\geq 3` and `\\leq 5`,
          or ``None``. This specifies the minimum degree of the generated
          triangulations. If this is ``None`` and the minimum connectivity
          is specified, then this is set to the same value as the minimum
          connectivity. If the minimum connectivity is also equal to ``None``,
          then this is set to 3.

        - ``minimum_connectivity`` -- (default: ``None``) a value `\\geq 3` and
          `\\leq 5`, or ``None``. This specifies the minimum connectivity of the
          generated triangulations. If this is ``None`` and the minimum degree
          is specified, then this is set to the minimum of the minimum degree
          and 3. If the minimum degree is also equal to ``None``, then this is
          set to 3.

        - ``exact_connectivity`` -- (default: ``False``) if ``True`` only
          triangulations with exactly the specified connectivity will be generated.
          This option cannot be used with ``minimum_connectivity=3``, or if
          the minimum connectivity is not explicitly set.

        - ``only_eulerian`` -- (default: ``False``) if ``True`` only Eulerian
          triangulations will be generated. This option cannot be used if the
          minimum degree is explicitly set to anything else than 4.

        - ``dual`` -- (default: ``False``) if ``True`` return instead the
          planar duals of the generated graphs

        - ``immutable`` -- boolean (default: ``False``); whether to return
          immutable or mutable graphs

        OUTPUT:

        An iterator which will produce all planar triangulations with the given
        number of vertices as Sage graphs with an embedding set. These will be
        simple graphs (no loops, no multiple edges, no directed edges).

        .. SEEALSO::

            - :meth:`~sage.graphs.generic_graph.GenericGraph.set_embedding`,
              :meth:`~sage.graphs.generic_graph.GenericGraph.get_embedding` --
              get/set methods for embeddings.

            - :meth:`~sage.graphs.graph_generators.GraphGenerators.RandomTriangulation`
              -- build a random triangulation.

        EXAMPLES:

        The unique planar embedding of the `K_4` is the only planar triangulations
        on 4 vertices::

            sage: gen = graphs.triangulations(4)    # optional - plantri
            sage: [g.get_embedding() for g in gen]  # optional - plantri
            [{1: [2, 3, 4], 2: [1, 4, 3], 3: [1, 2, 4], 4: [1, 3, 2]}]

        but, of course, this graph is not Eulerian::

            sage: gen = graphs.triangulations(4, only_eulerian=True)  # optional - plantri
            sage: len(list(gen))                                      # optional - plantri
            0

        The unique Eulerian triangulation on 6 vertices is isomorphic to the octahedral
        graph. ::

            sage: gen = graphs.triangulations(6, only_eulerian=True)  # optional - plantri
            sage: g = next(gen)                                       # optional - plantri
            sage: g.is_isomorphic(graphs.OctahedralGraph())           # optional - plantri
            True

        The minimum degree of a triangulation is 3, so the method can not output
        a triangle::

            sage: list(graphs.triangulations(3))                      # optional - plantri
            []

        An overview of the number of 5-connected triangulations on up to 22 vertices. This
        agrees with :oeis:`A081621`::

            sage: for i in range(12, 23):                                             # optional - plantri
            ....:     L = len(list(graphs.triangulations(i, minimum_connectivity=5)))
            ....:     print("{}   {:3d}".format(i,L))
            12     1
            13     0
            14     1
            15     1
            16     3
            17     4
            18    12
            19    23
            20    71
            21   187
            22   627

        The minimum connectivity can be at most the minimum degree::

            sage: gen = next(graphs.triangulations(10, minimum_degree=3,     # optional - plantri
            ....:                                  minimum_connectivity=5))
            Traceback (most recent call last):
            ...
            ValueError: Minimum connectivity can be at most the minimum degree.

        There are 5 triangulations with 9 vertices and minimum degree equal to 4
        that are 3-connected, but only one of them is not 4-connected::

            sage: len([g for g in graphs.triangulations(9, minimum_degree=4,        # optional - plantri
            ....:                                       minimum_connectivity=3)])
            5
            sage: len([g for g in graphs.triangulations(9, minimum_degree=4,        # optional - plantri
            ....:                                       minimum_connectivity=3,
            ....:                                       exact_connectivity=True)])
            1

        Setting ``dual=True`` gives the planar dual graphs::

            sage: [len(g) for g in graphs.triangulations(9, minimum_degree=4,       # optional plantri
            ....:                                        minimum_connectivity=3, dual=True)]
            [14, 14, 14, 14, 14]

        TESTS::

            sage: [g.size() for g in graphs.triangulations(6, minimum_connectivity=3)]  # optional - plantri
            [12, 12]
        '''
    def quadrangulations(self, order, minimum_degree=None, minimum_connectivity=None, no_nonfacial_quadrangles: bool = False, dual: bool = False, immutable: bool = False) -> Generator[Incomplete, Incomplete]:
        '''
        An iterator over planar quadrangulations using the plantri generator.

        This uses the plantri generator (see [BM2007]_) which is available
        through the optional package plantri.

        INPUT:

        - ``order`` -- positive integer smaller than or equal to 64;
          this specifies the number of vertices in the generated quadrangulations

        - ``minimum_degree`` -- (default: ``None``) a value `\\geq 2` and `\\leq
          3`, or ``None``. This specifies the minimum degree of the generated
          quadrangulations. If this is ``None`` and the minimum connectivity is
          specified, then this is set to the same value as the minimum
          connectivity. If the minimum connectivity is also equal to ``None``,
          then this is set to 2.

        - ``minimum_connectivity`` -- (default: ``None``) a value `\\geq 2` and
          `\\leq 3`, or ``None``. This specifies the minimum connectivity of the
          generated quadrangulations. If this is ``None`` and the option
          ``no_nonfacial_quadrangles`` is set to ``True``, then this is set to
          3. Otherwise if this is ``None`` and the minimum degree is specified,
          then this is set to the minimum degree. If the minimum degree is also
          equal to ``None``, then this is set to 3.

        - ``no_nonfacial_quadrangles`` -- (default: ``False``) if ``True`` only
          quadrangulations with no non-facial quadrangles are generated. This
          option cannot be used if ``minimum_connectivity`` is set to 2.

        - ``dual`` -- (default: ``False``) if ``True`` return instead the
          planar duals of the generated graphs

        - ``immutable`` -- boolean (default: ``False``); whether to return
          immutable or mutable graphs

        OUTPUT:

        An iterator which will produce all planar quadrangulations with the given
        number of vertices as Sage graphs with an embedding set. These will be
        simple graphs (no loops, no multiple edges, no directed edges).

        .. SEEALSO::

            - :meth:`~sage.graphs.generic_graph.GenericGraph.set_embedding`,
              :meth:`~sage.graphs.generic_graph.GenericGraph.get_embedding` --
              get/set methods for embeddings.

        EXAMPLES:

        The cube is the only 3-connected planar quadrangulation on 8 vertices::

            sage: # optional - plantri
            sage: gen = graphs.quadrangulations(8, minimum_connectivity=3)
            sage: g = next(gen)
            sage: g.is_isomorphic(graphs.CubeGraph(3))
            True
            sage: next(gen)
            Traceback (most recent call last):
            ...
            StopIteration

        An overview of the number of quadrangulations on up to 12 vertices. This
        agrees with :oeis:`A113201`::

            sage: for i in range(4,13):                          # optional - plantri
            ....:     L =  len(list(graphs.quadrangulations(i)))
            ....:     print("{:2d}   {:3d}".format(i,L))
             4     1
             5     1
             6     2
             7     3
             8     9
             9    18
            10    62
            11   198
            12   803

        There are 2 planar quadrangulation on 12 vertices that do not have a
        non-facial quadrangle::

            sage: len([g for g in graphs.quadrangulations(12, no_nonfacial_quadrangles=True)])  # optional - plantri
            2

        Setting ``dual=True`` gives the planar dual graphs::

            sage: [len(g) for g in graphs.quadrangulations(12, no_nonfacial_quadrangles=True, dual=True)]  # optional - plantri
            [10, 10]
        '''
    BullGraph: Incomplete
    ButterflyGraph: Incomplete
    CircularLadderGraph: Incomplete
    ClawGraph: Incomplete
    CycleGraph: Incomplete
    CompleteGraph: Incomplete
    CompleteBipartiteGraph: Incomplete
    CompleteMultipartiteGraph: Incomplete
    CorrelationGraph: Incomplete
    DiamondGraph: Incomplete
    GemGraph: Incomplete
    DartGraph: Incomplete
    ForkGraph: Incomplete
    EmptyGraph: Incomplete
    Grid2dGraph: Incomplete
    GridGraph: Incomplete
    HouseGraph: Incomplete
    HouseXGraph: Incomplete
    LadderGraph: Incomplete
    MoebiusLadderGraph: Incomplete
    PathGraph: Incomplete
    StarGraph: Incomplete
    Toroidal6RegularGrid2dGraph: Incomplete
    ToroidalGrid2dGraph: Incomplete
    Balaban10Cage: Incomplete
    Balaban11Cage: Incomplete
    BidiakisCube: Incomplete
    BiggsSmithGraph: Incomplete
    BlanusaFirstSnarkGraph: Incomplete
    BlanusaSecondSnarkGraph: Incomplete
    BrinkmannGraph: Incomplete
    BrouwerHaemersGraph: Incomplete
    BuckyBall: Incomplete
    CameronGraph: Incomplete
    Cell600: Incomplete
    Cell120: Incomplete
    ChvatalGraph: Incomplete
    ClebschGraph: Incomplete
    cocliques_HoffmannSingleton: Incomplete
    ConwaySmith_for_3S7: Incomplete
    CoxeterGraph: Incomplete
    CubeplexGraph: Incomplete
    DejterGraph: Incomplete
    DesarguesGraph: Incomplete
    distance_3_doubly_truncated_Golay_code_graph: Incomplete
    DoubleStarSnark: Incomplete
    DoublyTruncatedWittGraph: Incomplete
    DurerGraph: Incomplete
    DyckGraph: Incomplete
    EllinghamHorton54Graph: Incomplete
    EllinghamHorton78Graph: Incomplete
    ErreraGraph: Incomplete
    F26AGraph: Incomplete
    FlowerSnark: Incomplete
    FolkmanGraph: Incomplete
    FosterGraph: Incomplete
    FosterGraph3S6: Incomplete
    FranklinGraph: Incomplete
    FruchtGraph: Incomplete
    GoldnerHararyGraph: Incomplete
    GolombGraph: Incomplete
    GossetGraph: Incomplete
    graph_3O73: Incomplete
    GrayGraph: Incomplete
    GritsenkoGraph: Incomplete
    GrotzschGraph: Incomplete
    HallJankoGraph: Incomplete
    WellsGraph: Incomplete
    HarborthGraph: Incomplete
    HarriesGraph: Incomplete
    HarriesWongGraph: Incomplete
    HeawoodGraph: Incomplete
    HerschelGraph: Incomplete
    HigmanSimsGraph: Incomplete
    HoffmanGraph: Incomplete
    HoffmanSingletonGraph: Incomplete
    HoltGraph: Incomplete
    HortonGraph: Incomplete
    IoninKharaghani765Graph: Incomplete
    IvanovIvanovFaradjevGraph: Incomplete
    J2Graph: Incomplete
    JankoKharaghaniGraph: Incomplete
    JankoKharaghaniTonchevGraph: Incomplete
    KittellGraph: Incomplete
    KrackhardtKiteGraph: Incomplete
    Klein3RegularGraph: Incomplete
    Klein7RegularGraph: Incomplete
    LargeWittGraph: Incomplete
    LeonardGraph: Incomplete
    LjubljanaGraph: Incomplete
    vanLintSchrijverGraph: Incomplete
    LivingstoneGraph: Incomplete
    locally_GQ42_distance_transitive_graph: Incomplete
    LocalMcLaughlinGraph: Incomplete
    M22Graph: Incomplete
    MarkstroemGraph: Incomplete
    MathonStronglyRegularGraph: Incomplete
    McGeeGraph: Incomplete
    McLaughlinGraph: Incomplete
    MeredithGraph: Incomplete
    MoebiusKantorGraph: Incomplete
    MoserSpindle: Incomplete
    MurtyGraph: Incomplete
    NauruGraph: Incomplete
    PappusGraph: Incomplete
    PoussinGraph: Incomplete
    PerkelGraph: Incomplete
    PetersenGraph: Incomplete
    RobertsonGraph: Incomplete
    SchlaefliGraph: Incomplete
    shortened_00_11_binary_Golay_code_graph: Incomplete
    shortened_000_111_extended_binary_Golay_code_graph: Incomplete
    ShrikhandeGraph: Incomplete
    SimsGewirtzGraph: Incomplete
    SousselierGraph: Incomplete
    SylvesterGraph: Incomplete
    SzekeresSnarkGraph: Incomplete
    ThomsenGraph: Incomplete
    TietzeGraph: Incomplete
    TricornGraph: Incomplete
    Tutte12Cage: Incomplete
    TruncatedIcosidodecahedralGraph: Incomplete
    TruncatedTetrahedralGraph: Incomplete
    TruncatedWittGraph: Incomplete
    TutteCoxeterGraph: Incomplete
    TutteGraph: Incomplete
    TwinplexGraph: Incomplete
    U42Graph216: Incomplete
    U42Graph540: Incomplete
    WagnerGraph: Incomplete
    WatkinsSnarkGraph: Incomplete
    WienerArayaGraph: Incomplete
    SuzukiGraph: Incomplete
    DodecahedralGraph: Incomplete
    HexahedralGraph: Incomplete
    IcosahedralGraph: Incomplete
    OctahedralGraph: Incomplete
    TetrahedralGraph: Incomplete
    AlternatingFormsGraph: Incomplete
    AztecDiamondGraph: Incomplete
    BalancedTree: Incomplete
    BarbellGraph: Incomplete
    BilinearFormsGraph: Incomplete
    BiwheelGraph: Incomplete
    BubbleSortGraph: Incomplete
    CaiFurerImmermanGraph: Incomplete
    chang_graphs: Incomplete
    CirculantGraph: Incomplete
    cographs: Incomplete
    CubeGraph: Incomplete
    CubeConnectedCycle: Incomplete
    DipoleGraph: Incomplete
    distance_regular_graph: Incomplete
    DorogovtsevGoltsevMendesGraph: Incomplete
    DoubleGeneralizedPetersenGraph: Incomplete
    DoubleGrassmannGraph: Incomplete
    DoubleOddGraph: Incomplete
    EgawaGraph: Incomplete
    FibonacciTree: Incomplete
    FoldedCubeGraph: Incomplete
    FriendshipGraph: Incomplete
    FurerGadget: Incomplete
    FuzzyBallGraph: Incomplete
    GeneralisedDodecagonGraph: Incomplete
    GeneralisedHexagonGraph: Incomplete
    GeneralisedOctagonGraph: Incomplete
    GeneralizedPetersenGraph: Incomplete
    GeneralizedSierpinskiGraph: Incomplete
    GoethalsSeidelGraph: Incomplete
    GrassmannGraph: Incomplete
    HalfCube: Incomplete
    HammingGraph: Incomplete
    HanoiTowerGraph: Incomplete
    HararyGraph: Incomplete
    HermitianFormsGraph: Incomplete
    HyperStarGraph: Incomplete
    IGraph: Incomplete
    JohnsonGraph: Incomplete
    KneserGraph: Incomplete
    LCFGraph: Incomplete
    line_graph_forbidden_subgraphs: Incomplete
    LollipopGraph: Incomplete
    MathonPseudocyclicMergingGraph: Incomplete
    MathonPseudocyclicStronglyRegularGraph: Incomplete
    MuzychukS6Graph: Incomplete
    MycielskiGraph: Incomplete
    MycielskiStep: Incomplete
    NKStarGraph: Incomplete
    NStarGraph: Incomplete
    OddGraph: Incomplete
    p2_forbidden_minors: Incomplete
    PaleyGraph: Incomplete
    PasechnikGraph: Incomplete
    petersen_family: Incomplete
    RingedTree: Incomplete
    RoseWindowGraph: Incomplete
    SierpinskiGasketGraph: Incomplete
    SquaredSkewHadamardMatrixGraph: Incomplete
    SwitchedSquaredSkewHadamardMatrixGraph: Incomplete
    StaircaseGraph: Incomplete
    strongly_regular_graph: Incomplete
    TabacjnGraph: Incomplete
    TadpoleGraph: Incomplete
    trees: Incomplete
    TruncatedBiwheelGraph: Incomplete
    nauty_gentreeg: Incomplete
    TuranGraph: Incomplete
    UstimenkoGraph: Incomplete
    WheelGraph: Incomplete
    WindmillGraph: Incomplete
    AffineOrthogonalPolarGraph: Incomplete
    AhrensSzekeresGeneralizedQuadrangleGraph: Incomplete
    NonisotropicOrthogonalPolarGraph: Incomplete
    NonisotropicUnitaryPolarGraph: Incomplete
    OrthogonalDualPolarGraph: Incomplete
    OrthogonalPolarGraph: Incomplete
    SymplecticDualPolarGraph: Incomplete
    SymplecticPolarGraph: Incomplete
    TaylorTwographDescendantSRG: Incomplete
    TaylorTwographSRG: Incomplete
    T2starGeneralizedQuadrangleGraph: Incomplete
    Nowhere0WordsTwoWeightCodeGraph: Incomplete
    HaemersGraph: Incomplete
    CossidentePenttilaGraph: Incomplete
    UnitaryDualPolarGraph: Incomplete
    UnitaryPolarGraph: Incomplete
    ChessboardGraphGenerator: Incomplete
    BishopGraph: Incomplete
    KingGraph: Incomplete
    KnightGraph: Incomplete
    QueenGraph: Incomplete
    RookGraph: Incomplete
    IntervalGraph: Incomplete
    IntersectionGraph: Incomplete
    PermutationGraph: Incomplete
    OrthogonalArrayBlockGraph: Incomplete
    ToleranceGraph: Incomplete
    RandomBarabasiAlbert: Incomplete
    RandomBipartite: Incomplete
    RandomRegularBipartite: Incomplete
    RandomBicubicPlanar: Incomplete
    RandomBlockGraph: Incomplete
    RandomBoundedToleranceGraph: Incomplete
    RandomChordalGraph: Incomplete
    RandomGNM: Incomplete
    RandomGNP: Incomplete
    RandomHolmeKim: Incomplete
    RandomIntervalGraph: Incomplete
    RandomLobster: Incomplete
    RandomNewmanWattsStrogatz: Incomplete
    RandomProperIntervalGraph: Incomplete
    RandomRegular: Incomplete
    RandomShell: Incomplete
    RandomKTree: Incomplete
    RandomPartialKTree: Incomplete
    RandomToleranceGraph: Incomplete
    RandomTreePowerlaw: Incomplete
    RandomTree: Incomplete
    RandomTriangulation: Incomplete
    RandomUnitDiskGraph: Incomplete
    WorldMap: Incomplete
    EuropeMap: Incomplete
    AfricaMap: Incomplete
    USAMap: Incomplete
    DegreeSequence: Incomplete
    DegreeSequenceBipartite: Incomplete
    DegreeSequenceConfigurationModel: Incomplete
    DegreeSequenceTree: Incomplete
    DegreeSequenceExpected: Incomplete

def canaug_traverse_vert(g, aut_gens, max_verts, property, dig: bool = False, loops: bool = False, sparse: bool = True) -> Generator[Incomplete]:
    """
    Main function for exhaustive generation. Recursive traversal of a
    canonically generated tree of isomorph free (di)graphs satisfying a
    given property.

    INPUT:

    - ``g`` -- current position on the tree

    - ``aut_gens`` -- list of generators of Aut(g), in list notation

    - ``max_verts`` -- when to retreat

    - ``property`` -- check before traversing below g

    - ``degree_sequence`` -- specify a degree sequence to try to obtain

    EXAMPLES::

        sage: from sage.graphs.graph_generators import canaug_traverse_vert
        sage: list(canaug_traverse_vert(Graph(), [], 3, lambda x: True))
        [Graph on 0 vertices, ... Graph on 3 vertices]

    The best way to access this function is through the graphs()
    iterator:

    Print graphs on 3 or less vertices.

    ::

        sage: for G in graphs(3, augment='vertices'):
        ....:    print(G)
        Graph on 0 vertices
        Graph on 1 vertex
        Graph on 2 vertices
        Graph on 3 vertices
        Graph on 3 vertices
        Graph on 3 vertices
        Graph on 2 vertices
        Graph on 3 vertices

    Print digraphs on 2 or less vertices.

    ::

        sage: for D in digraphs(2, augment='vertices'):
        ....:     print(D)
        Digraph on 0 vertices
        Digraph on 1 vertex
        Digraph on 2 vertices
        Digraph on 2 vertices
        Digraph on 2 vertices
    """
def check_aut(aut_gens, cut_vert, n) -> Generator[Incomplete]:
    """
    Helper function for exhaustive generation.

    At the start, check_aut is given a set of generators for the
    automorphism group, aut_gens. We already know we are looking for
    an element of the auto- morphism group that sends cut_vert to n,
    and check_aut generates these for the canaug_traverse function.

    EXAMPLES:

    Note that the last two entries indicate that none of the
    automorphism group has yet been searched - we are starting at the
    identity [0, 1, 2, 3] and so far that is all we have seen. We
    return automorphisms mapping 2 to 3::

        sage: from sage.graphs.graph_generators import check_aut
        sage: list( check_aut( [ [0, 3, 2, 1], [1, 0, 3, 2], [2, 1, 0, 3] ], 2, 3))
        [[1, 0, 3, 2], [1, 2, 3, 0]]
    """
def canaug_traverse_edge(g, aut_gens, property, dig: bool = False, loops: bool = False, sparse: bool = True) -> Generator[Incomplete]:
    """
    Main function for exhaustive generation. Recursive traversal of a
    canonically generated tree of isomorph free graphs satisfying a
    given property.

    INPUT:

    - ``g`` -- current position on the tree

    - ``aut_gens`` -- list of generators of Aut(g), in list notation

    - ``property`` -- check before traversing below g

    EXAMPLES::

        sage: from sage.graphs.graph_generators import canaug_traverse_edge
        sage: G = Graph(3)
        sage: list(canaug_traverse_edge(G, [], lambda x: True))
        [Graph on 3 vertices, ... Graph on 3 vertices]

    The best way to access this function is through the graphs()
    iterator:

    Print graphs on 3 or less vertices.

    ::

        sage: for G in graphs(3):
        ....:     print(G)
        Graph on 3 vertices
        Graph on 3 vertices
        Graph on 3 vertices
        Graph on 3 vertices

    Print digraphs on 3 or less vertices.

    ::

        sage: for G in digraphs(3):
        ....:     print(G)
        Digraph on 3 vertices
        Digraph on 3 vertices
        ...
        Digraph on 3 vertices
        Digraph on 3 vertices
    """
def check_aut_edge(aut_gens, cut_edge, i, j, n, dig: bool = False) -> Generator[Incomplete]:
    """
    Helper function for exhaustive generation.

    At the start, check_aut_edge is given a set of generators for the
    automorphism group, aut_gens. We already know we are looking for
    an element of the auto- morphism group that sends cut_edge to {i,
    j}, and check_aut generates these for the canaug_traverse
    function.

    EXAMPLES:

    Note that the last two entries indicate that none of the
    automorphism group has yet been searched - we are starting at the
    identity [0, 1, 2, 3] and so far that is all we have seen. We
    return automorphisms mapping 2 to 3::

        sage: from sage.graphs.graph_generators import check_aut
        sage: list( check_aut( [ [0, 3, 2, 1], [1, 0, 3, 2], [2, 1, 0, 3] ], 2, 3))
        [[1, 0, 3, 2], [1, 2, 3, 0]]
    """

graphs: Incomplete
