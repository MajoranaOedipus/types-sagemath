from _typeshed import Incomplete
from collections.abc import Generator
from sage.arith.misc import gcd as gcd
from sage.combinat.cluster_algebra_quiver.interact import cluster_interact as cluster_interact
from sage.combinat.cluster_algebra_quiver.mutation_type import is_mutation_finite as is_mutation_finite
from sage.combinat.cluster_algebra_quiver.quiver_mutation_type import QuiverMutationType as QuiverMutationType, QuiverMutationType_Irreducible as QuiverMutationType_Irreducible, QuiverMutationType_Reducible as QuiverMutationType_Reducible
from sage.graphs.digraph import DiGraph as DiGraph
from sage.graphs.graph import Graph as Graph
from sage.graphs.views import EdgesView as EdgesView
from sage.misc.lazy_import import lazy_import as lazy_import
from sage.misc.misc_c import prod as prod
from sage.rings.infinity import infinity as infinity
from sage.rings.integer_ring import ZZ as ZZ
from sage.rings.polynomial.polynomial_ring import polygen as polygen
from sage.rings.rational_field import QQ as QQ
from sage.structure.sage_object import SageObject as SageObject

class ClusterQuiver(SageObject):
    """
    The *quiver* associated to an *exchange matrix*.

    INPUT:

    - ``data`` -- can be any of the following::

      - :class:`QuiverMutationType`

      - :class:`str` -- string representing a :class:`QuiverMutationType`
        or a common quiver type (see Examples)

      - :class:`ClusterQuiver`

      - :class:`Matrix` -- a skew-symmetrizable matrix

      - :class:`DiGraph` -- must be the input data for a quiver

      - List of edges -- must be the edge list of a digraph for a quiver

    - ``frozen`` -- (default: ``None``) sets the list of frozen variables
      if the input type is a :class:`DiGraph`, it is ignored otherwise

    - ``user_labels`` -- (default: ``None``) sets the names of the labels for
      the vertices of the quiver if the input type is not a :class:`DiGraph`;
      otherwise it is ignored

    EXAMPLES:

    From a :class:`QuiverMutationType`::

        sage: Q = ClusterQuiver(['A',5]); Q
        Quiver on 5 vertices of type ['A', 5]

        sage: Q = ClusterQuiver(['B',2]); Q
        Quiver on 2 vertices of type ['B', 2]
        sage: Q2 = ClusterQuiver(['C',2]); Q2
        Quiver on 2 vertices of type ['B', 2]
        sage: MT = Q.mutation_type(); MT.standard_quiver() == Q
        True
        sage: MT = Q2.mutation_type(); MT.standard_quiver() == Q2
        False

        sage: Q = ClusterQuiver(['A',[2,5],1]); Q
        Quiver on 7 vertices of type ['A', [2, 5], 1]

        sage: Q = ClusterQuiver(['A', [5,0],1]); Q
        Quiver on 5 vertices of type ['D', 5]
        sage: Q.is_finite()
        True
        sage: Q.is_acyclic()
        False

        sage: Q = ClusterQuiver(['F', 4, [2,1]]); Q
        Quiver on 6 vertices of type ['F', 4, [1, 2]]
        sage: MT = Q.mutation_type(); MT.standard_quiver() == Q
        False
        sage: dg = Q.digraph(); Q.mutate([2,1,4,0,5,3])
        sage: dg2 = Q.digraph(); dg2.is_isomorphic(dg,edge_labels=True)
        False
        sage: dg2.is_isomorphic(MT.standard_quiver().digraph(),edge_labels=True)
        True

        sage: Q = ClusterQuiver(['G',2, (3,1)]); Q
        Quiver on 4 vertices of type ['G', 2, [1, 3]]
        sage: MT = Q.mutation_type(); MT.standard_quiver() == Q
        False

        sage: Q = ClusterQuiver(['GR',[3,6]]); Q
        Quiver on 4 vertices of type ['D', 4]
        sage: MT = Q.mutation_type(); MT.standard_quiver() == Q
        False

        sage: Q = ClusterQuiver(['GR',[3,7]]); Q
        Quiver on 6 vertices of type ['E', 6]

        sage: Q = ClusterQuiver(['TR',2]); Q
        Quiver on 3 vertices of type ['A', 3]
        sage: MT = Q.mutation_type(); MT.standard_quiver() == Q
        False
        sage: Q.mutate([1,0]); MT.standard_quiver() == Q
        True

        sage: Q = ClusterQuiver(['TR',3]); Q
        Quiver on 6 vertices of type ['D', 6]
        sage: MT = Q.mutation_type(); MT.standard_quiver() == Q
        False

    From a :class:`ClusterQuiver`::

        sage: Q = ClusterQuiver(['A',[2,5],1]); Q
        Quiver on 7 vertices of type ['A', [2, 5], 1]
        sage: T = ClusterQuiver(Q); T
        Quiver on 7 vertices of type ['A', [2, 5], 1]

    From a Matrix::

        sage: Q = ClusterQuiver(['A',[2,5],1]); Q
        Quiver on 7 vertices of type ['A', [2, 5], 1]
        sage: T = ClusterQuiver(Q._M); T
        Quiver on 7 vertices

        sage: Q = ClusterQuiver(matrix([[0,1,-1],[-1,0,1],[1,-1,0],[1,2,3]])); Q
        Quiver on 4 vertices with 1 frozen vertex

        sage: Q = ClusterQuiver(matrix([])); Q
        Quiver without vertices

    From a DiGraph::

        sage: Q = ClusterQuiver(['A',[2,5],1]); Q
        Quiver on 7 vertices of type ['A', [2, 5], 1]
        sage: T = ClusterQuiver(Q._digraph); T
        Quiver on 7 vertices

        sage: Q = ClusterQuiver(DiGraph([[1,2],[2,3],[3,4],[4,1]])); Q
        Quiver on 4 vertices

        sage: Q = ClusterQuiver(DiGraph([['a', 'b'], ['b', 'c'], ['c', 'd'], ['d', 'e']]),
        ....:          frozen=['c']); Q
        Quiver on 5 vertices with 1 frozen vertex
        sage: Q.mutation_type()
        [ ['A', 2], ['A', 2] ]
        sage: Q
        Quiver on 5 vertices of type [ ['A', 2], ['A', 2] ]
        with 1 frozen vertex

    From a List of edges::

        sage: Q = ClusterQuiver(['A',[2,5],1]); Q
        Quiver on 7 vertices of type ['A', [2, 5], 1]
        sage: T = ClusterQuiver(Q._digraph.edges(sort=True)); T
        Quiver on 7 vertices

        sage: Q = ClusterQuiver([[1, 2], [2, 3], [3, 4], [4, 1]]); Q
        Quiver on 4 vertices

    TESTS::

        sage: Q = ClusterQuiver(DiGraph([[1,1]]))
        Traceback (most recent call last):
        ...
        ValueError: cannot add edge from 1 to 1 in graph without loops

        sage: Q = ClusterQuiver([[1,1]])
        Traceback (most recent call last):
        ...
        ValueError: cannot add edge from 1 to 1 in graph without loops

        sage: Q = ClusterQuiver(DiGraph([[1, 0],[0,1]]))
        Traceback (most recent call last):
        ...
        ValueError: the input DiGraph contains two-cycles

        sage: Q = ClusterQuiver('whatever')
        Traceback (most recent call last):
        ...
        ValueError: the input data was not recognized
    """
    def __init__(self, data, frozen=None, user_labels=None) -> None:
        """
        TESTS::

            sage: Q = ClusterQuiver(['A',4])
            sage: TestSuite(Q).run()
        """
    def __eq__(self, other) -> bool:
        """
        Return ``True`` if ``self`` and ``other`` represent the same quiver.

        EXAMPLES::

            sage: Q = ClusterQuiver(['A',5])
            sage: T = Q.mutate(2, inplace=False)
            sage: Q.__eq__(T)
            False
            sage: T.mutate(2)
            sage: Q.__eq__(T)
            True
        """
    def __hash__(self) -> int:
        """
        Return a hash of ``self``.

        EXAMPLES::

            sage: Q = ClusterQuiver(['A',5])
            sage: hash(Q)  # indirect doctest
            7654921743699262111  # 64-bit
            -1264862561          # 32-bit
        """
    def plot(self, circular: bool = True, center=(0, 0), directed: bool = True, mark=None, save_pos: bool = False, greens=[]):
        """
        Return the plot of the underlying digraph of ``self``.

        INPUT:

        - ``circular`` -- boolean (default: ``True``); if ``True``, the
          circular plot is chosen, otherwise >>spring<< is used
        - ``center`` -- (default: (0,0)) sets the center of the circular plot,
          otherwise it is ignored
        - ``directed`` -- boolean (default: ``True``); if ``True``, the
          directed version is shown, otherwise the undirected
        - ``mark`` -- (default: ``None``) if set to i, the vertex i is
          highlighted
        - ``save_pos`` -- boolean (default: ``False``); if ``True``, the
          positions of the vertices are saved
        - ``greens`` -- (default: ``[]``) if set to a list, will display the green
          vertices as green

        EXAMPLES::

            sage: Q = ClusterQuiver(['A',5])
            sage: Q.plot()                                                              # needs sage.plot sage.symbolic
            Graphics object consisting of 15 graphics primitives
            sage: Q.plot(circular=True)                                                 # needs sage.plot sage.symbolic
            Graphics object consisting of 15 graphics primitives
            sage: Q.plot(circular=True, mark=1)                                         # needs sage.plot sage.symbolic
            Graphics object consisting of 15 graphics primitives
        """
    def show(self, fig_size: int = 1, circular: bool = False, directed: bool = True, mark=None, save_pos: bool = False, greens=[]) -> None:
        """
        Show the plot of the underlying digraph of ``self``.

        INPUT:

        - ``fig_size`` -- (default: 1) factor by which the size of the plot
          is multiplied
        - ``circular`` -- boolean (default: ``False``); if ``True``, the
          circular plot is chosen, otherwise >>spring<< is used
        - ``directed`` -- boolean (default: ``True``); if ``True``, the directed
          version is shown, otherwise the undirected
        - ``mark`` -- boolean (default: ``None``); if set to i, the vertex i is
          highlighted
        - ``save_pos`` -- boolean (default: ``False``); if ``True``, the
          positions of the vertices are saved
        - ``greens`` -- (default: ``[]``) if set to a list, will display the
          green vertices as green

        TESTS::

            sage: Q = ClusterQuiver(['A',5])
            sage: Q.show() # long time
        """
    def interact(self, fig_size: int = 1, circular: bool = True):
        """
        Start an interactive window for cluster quiver mutations.

        Only in *Jupyter notebook mode*.

        INPUT:

        - ``fig_size`` -- (default: 1) factor by which the size of the
          plot is multiplied

        - ``circular`` -- boolean (default: ``True``); if ``True``, the
          circular plot is chosen, otherwise >>spring<< is used

        TESTS::

            sage: S = ClusterQuiver(['A',4])
            sage: S.interact()                                                          # needs sage.plot sage.symbolic
            ...VBox(children=...
        """
    def save_image(self, filename, circular: bool = False) -> None:
        """
        Save the plot of the underlying digraph of ``self``.

        INPUT:

        - ``filename`` -- the filename the image is saved to
        - ``circular`` -- boolean (default: ``False``); if ``True``, the
          circular plot is chosen, otherwise >>spring<< is used

        EXAMPLES::

            sage: Q = ClusterQuiver(['F',4,[1,2]])
            sage: import tempfile
            sage: with tempfile.NamedTemporaryFile(suffix='.png') as f:                 # needs sage.plot sage.symbolic
            ....:     Q.save_image(f.name)
        """
    def qmu_save(self, filename=None) -> None:
        """
        Save ``self`` in a ``.qmu`` file.

        This file can then be opened in Bernhard Keller's Quiver Applet.

        See https://webusers.imj-prg.fr/~bernhard.keller/quivermutation/

        INPUT:

        - ``filename`` -- the filename the image is saved to

        If a filename is not specified, the default name is
        ``from_sage.qmu`` in the current sage directory.

        EXAMPLES::

            sage: Q = ClusterQuiver(['F',4,[1,2]])
            sage: import tempfile
            sage: with tempfile.NamedTemporaryFile(suffix='.qmu') as f:                 # needs sage.plot sage.symbolic
            ....:     Q.qmu_save(f.name)

        Make sure we can save quivers with `m != n` frozen variables, see :issue:`14851`::

            sage: S = ClusterSeed(['A',3])
            sage: T1 = S.principal_extension()
            sage: Q = T1.quiver()
            sage: import tempfile
            sage: with tempfile.NamedTemporaryFile(suffix='.qmu') as f:                 # needs sage.plot sage.symbolic
            ....:     Q.qmu_save(f.name)
        """
    def b_matrix(self):
        """
        Return the b-matrix of ``self``.

        EXAMPLES::

            sage: ClusterQuiver(['A',4]).b_matrix()
            [ 0  1  0  0]
            [-1  0 -1  0]
            [ 0  1  0  1]
            [ 0  0 -1  0]

            sage: ClusterQuiver(['B',4]).b_matrix()
            [ 0  1  0  0]
            [-1  0 -1  0]
            [ 0  1  0  1]
            [ 0  0 -2  0]

            sage: ClusterQuiver(['D',4]).b_matrix()
            [ 0  1  0  0]
            [-1  0 -1 -1]
            [ 0  1  0  0]
            [ 0  1  0  0]

            sage: ClusterQuiver(QuiverMutationType([['A',2],['B',2]])).b_matrix()
            [ 0  1  0  0]
            [-1  0  0  0]
            [ 0  0  0  1]
            [ 0  0 -2  0]
        """
    def digraph(self):
        """
        Return the underlying digraph of ``self``.

        EXAMPLES::

            sage: ClusterQuiver(['A',1]).digraph()
            Digraph on 1 vertex
            sage: list(ClusterQuiver(['A',1]).digraph())
            [0]
            sage: ClusterQuiver(['A',1]).digraph().edges(sort=True)
            []

            sage: ClusterQuiver(['A',4]).digraph()
            Digraph on 4 vertices
            sage: ClusterQuiver(['A',4]).digraph().edges(sort=True)
            [(0, 1, (1, -1)), (2, 1, (1, -1)), (2, 3, (1, -1))]

            sage: ClusterQuiver(['B',4]).digraph()
            Digraph on 4 vertices
            sage: ClusterQuiver(['A',4]).digraph().edges(sort=True)
            [(0, 1, (1, -1)), (2, 1, (1, -1)), (2, 3, (1, -1))]

            sage: ClusterQuiver(QuiverMutationType([['A',2],['B',2]])).digraph()
            Digraph on 4 vertices

            sage: ClusterQuiver(QuiverMutationType([['A',2],['B',2]])).digraph().edges(sort=True)
            [(0, 1, (1, -1)), (2, 3, (1, -2))]

            sage: ClusterQuiver(['C', 4], user_labels = ['x', 'y', 'z', 'w']).digraph().edges(sort=True)
            [('x', 'y', (1, -1)), ('z', 'w', (2, -1)), ('z', 'y', (1, -1))]
        """
    def mutation_type(self):
        """
        Return the mutation type of ``self``.

        Return the mutation_type of each connected component of ``self`` if it
        can be determined, otherwise, the mutation type of this component is
        set to be unknown.

        The mutation types of the components are ordered by vertex labels.

        If you do many type recognitions, you should consider to save
        exceptional mutation types using
        :meth:`~sage.combinat.cluster_algebra_quiver.quiver_mutation_type.save_quiver_data`

        WARNING:

        - All finite types can be detected,
        - All affine types can be detected, EXCEPT affine type D (the algorithm is not yet implemented)
        - All exceptional types can be detected.

        EXAMPLES::

            sage: ClusterQuiver(['A',4]).mutation_type()
            ['A', 4]
            sage: ClusterQuiver(['A',(3,1),1]).mutation_type()
            ['A', [1, 3], 1]
            sage: ClusterQuiver(['C',2]).mutation_type()
            ['B', 2]
            sage: ClusterQuiver(['B',4,1]).mutation_type()
            ['BD', 4, 1]

        finite types::

            sage: Q = ClusterQuiver(['A',5])
            sage: Q._mutation_type = None
            sage: Q.mutation_type()
            ['A', 5]

            sage: Q = ClusterQuiver([(0,1),(1,2),(2,3),(3,4)])
            sage: Q.mutation_type()
            ['A', 5]

            sage: Q = ClusterQuiver(DiGraph([['a', 'b'], ['c', 'b'], ['c', 'd'], ['e', 'd']]),
            ....:                   frozen=['c'])
            sage: Q.mutation_type()
            [ ['A', 2], ['A', 2] ]

        affine types::

            sage: Q = ClusterQuiver(['E',8,[1,1]]); Q
            Quiver on 10 vertices of type ['E', 8, [1, 1]]
            sage: Q._mutation_type = None; Q
            Quiver on 10 vertices
            sage: Q.mutation_type() # long time
            ['E', 8, [1, 1]]

        the not yet working affine type D (unless user has saved small classical quiver data)::

            sage: Q = ClusterQuiver(['D',4,1])
            sage: Q._mutation_type = None
            sage: Q.mutation_type() # todo: not implemented
            ['D', 4, 1]

        the exceptional types::

            sage: Q = ClusterQuiver(['X',6])
            sage: Q._mutation_type = None
            sage: Q.mutation_type() # long time
            ['X', 6]

        examples from page 8 of [Ke2008]_::

            sage: dg = DiGraph(); dg.add_edges([(9,0),(9,4),(4,6),(6,7),(7,8),(8,3),(3,5),(5,6),(8,1),(2,3)])
            sage: ClusterQuiver(dg).mutation_type() # long time
            ['E', 8, [1, 1]]

            sage: dg = DiGraph({ 0:[3], 1:[0,4], 2:[0,6], 3:[1,2,7], 4:[3,8], 5:[2], 6:[3,5], 7:[4,6], 8:[7] })
            sage: ClusterQuiver(dg).mutation_type() # long time
            ['E', 8, 1]

            sage: dg = DiGraph({ 0:[3,9], 1:[0,4], 2:[0,6], 3:[1,2,7], 4:[3,8], 5:[2], 6:[3,5], 7:[4,6], 8:[7], 9:[1] })
            sage: ClusterQuiver(dg).mutation_type() # long time
            ['E', 8, [1, 1]]

        infinite types::

            sage: Q = ClusterQuiver(['GR',[4,9]])
            sage: Q._mutation_type = None
            sage: Q.mutation_type()
            'undetermined infinite mutation type'

        reducible types::

            sage: Q = ClusterQuiver([['A', 3], ['B', 3]])
            sage: Q._mutation_type = None
            sage: Q.mutation_type()
            [ ['A', 3], ['B', 3] ]

            sage: Q = ClusterQuiver([['A', 3], ['T', [4,4,4]]])
            sage: Q._mutation_type = None
            sage: Q.mutation_type()
            [['A', 3], 'undetermined infinite mutation type']

            sage: Q = ClusterQuiver([['A', 3], ['B', 3], ['T', [4,4,4]]])
            sage: Q._mutation_type = None
            sage: Q.mutation_type()
            [['A', 3], ['B', 3], 'undetermined infinite mutation type']

            sage: Q = ClusterQuiver([[0,1,2],[1,2,2],[2,0,2],[3,4,1],[4,5,1]])
            sage: Q.mutation_type()
            ['undetermined finite mutation type', ['A', 3]]

        TESTS::

            sage: Q = ClusterQuiver(matrix([[0, 3], [-1, 0], [1, 0], [0, 1]]))
            sage: Q.mutation_type()
            ['G', 2]
            sage: Q = ClusterQuiver(matrix([[0, -1, -1, 1, 0], [1, 0, 1, 0, 1], [1, -1, 0, -1, 0], [-1, 0, 1, 0, 1], [0, -1, 0, -1, 0], [0, 1, 0, -1, -1], [0, 1, -1, 0, 0]]))
            sage: Q.mutation_type()
            'undetermined infinite mutation type'
        """
    def n(self):
        """
        Return the number of free vertices of ``self``.

        EXAMPLES::

            sage: ClusterQuiver(['A',4]).n()
            4
            sage: ClusterQuiver(['A',(3,1),1]).n()
            4
            sage: ClusterQuiver(['B',4]).n()
            4
            sage: ClusterQuiver(['B',4,1]).n()
            5
        """
    def m(self):
        """
        Return the number of frozen vertices of ``self``.

        EXAMPLES::

            sage: Q = ClusterQuiver(['A',4])
            sage: Q.m()
            0

            sage: T = ClusterQuiver(Q.digraph().edges(sort=True), frozen=[3])
            sage: T.n()
            3
            sage: T.m()
            1
        """
    def free_vertices(self) -> list:
        """
        Return the list of free vertices of ``self``.

        EXAMPLES::

            sage: Q = ClusterQuiver(DiGraph([['a', 'b'], ['c', 'b'], ['c', 'd'], ['e', 'd']]),
            ....:                   frozen=['b', 'd'])
            sage: Q.free_vertices()
            ['a', 'c', 'e']
        """
    def frozen_vertices(self) -> list:
        """
        Return the list of frozen vertices of ``self``.

        EXAMPLES::

            sage: Q = ClusterQuiver(DiGraph([['a', 'b'], ['c', 'b'], ['c', 'd'], ['e', 'd']]),
            ....:                   frozen=['b', 'd'])
            sage: sorted(Q.frozen_vertices())
            ['b', 'd']
        """
    def canonical_label(self, certificate: bool = False):
        """
        Return the canonical labelling of ``self``.

        See :meth:`sage.graphs.generic_graph.GenericGraph.canonical_label`.

        INPUT:

        - ``certificate`` -- boolean (default: ``False``); if ``True``, the
          dictionary from ``self.vertices()`` to the vertices of the returned
          quiver is returned as well

        EXAMPLES::

            sage: Q = ClusterQuiver(['A',4]); Q.digraph().edges(sort=True)
            [(0, 1, (1, -1)), (2, 1, (1, -1)), (2, 3, (1, -1))]

            sage: T = Q.canonical_label(); T.digraph().edges(sort=True)
            [(0, 3, (1, -1)), (1, 2, (1, -1)), (1, 3, (1, -1))]

            sage: T, iso = Q.canonical_label(certificate=True)
            sage: T.digraph().edges(sort=True); iso
            [(0, 3, (1, -1)), (1, 2, (1, -1)), (1, 3, (1, -1))]
            {0: 0, 1: 3, 2: 1, 3: 2}

            sage: Q = ClusterQuiver(QuiverMutationType([['B',2],['A',1]])); Q
            Quiver on 3 vertices of type [ ['B', 2], ['A', 1] ]

            sage: Q.canonical_label()
            Quiver on 3 vertices of type [ ['A', 1], ['B', 2] ]

            sage: Q.canonical_label(certificate=True)
            (Quiver on 3 vertices of type [ ['A', 1], ['B', 2] ], {0: 1, 1: 2, 2: 0})
        """
    def is_acyclic(self) -> bool:
        """
        Return true if ``self`` is acyclic.

        EXAMPLES::

            sage: ClusterQuiver(['A',4]).is_acyclic()
            True

            sage: ClusterQuiver(['A',[2,1],1]).is_acyclic()
            True

            sage: ClusterQuiver([[0,1],[1,2],[2,0]]).is_acyclic()
            False
        """
    def is_bipartite(self, return_bipartition: bool = False):
        """
        Return ``True`` if ``self`` is bipartite.

        EXAMPLES::

            sage: ClusterQuiver(['A',[3,3],1]).is_bipartite()
            True

            sage: ClusterQuiver(['A',[4,3],1]).is_bipartite()
            False
        """
    def exchangeable_part(self):
        """
        Return the restriction to the principal part (i.e. exchangeable part) of ``self``, the subquiver obtained by deleting the frozen vertices of ``self``.

        EXAMPLES::

            sage: Q = ClusterQuiver(['A',4])
            sage: T = ClusterQuiver(Q.digraph().edges(sort=True), frozen=[3])
            sage: T.digraph().edges(sort=True)
            [(0, 1, (1, -1)), (2, 1, (1, -1)), (2, 3, (1, -1))]

            sage: T.exchangeable_part().digraph().edges(sort=True)
            [(0, 1, (1, -1)), (2, 1, (1, -1))]

            sage: Q2 = Q.principal_extension()
            sage: Q3 = Q2.principal_extension()
            sage: Q2.exchangeable_part() == Q3.exchangeable_part()
            True
        """
    def principal_extension(self, inplace: bool = False):
        """
        Return the principal extension of ``self``, adding n frozen vertices
        to any previously frozen vertices.

        This is the quiver obtained by adding an outgoing edge to
        every mutable vertex of ``self``.

        EXAMPLES::

            sage: Q = ClusterQuiver(['A',2]); Q
            Quiver on 2 vertices of type ['A', 2]
            sage: T = Q.principal_extension(); T
            Quiver on 4 vertices of type ['A', 2] with 2 frozen vertices
            sage: T2 = T.principal_extension(); T2
            Quiver on 6 vertices of type ['A', 2] with 4 frozen vertices
            sage: Q.digraph().edges(sort=True)
            [(0, 1, (1, -1))]
            sage: T.digraph().edges(sort=True)
            [(0, 1, (1, -1)), (2, 0, (1, -1)), (3, 1, (1, -1))]
            sage: T2.digraph().edges(sort=True)
            [(0, 1, (1, -1)), (2, 0, (1, -1)), (3, 1, (1, -1)),
             (4, 0, (1, -1)), (5, 1, (1, -1))]
        """
    def first_sink(self):
        """
        Return the first vertex of ``self`` that is a sink.

        EXAMPLES::

            sage: Q = ClusterQuiver(['A',5])
            sage: Q.mutate([1,2,4,3,2])
            sage: Q.first_sink()
            0
        """
    def sinks(self) -> list:
        """
        Return all vertices of ``self`` that are sinks.

        EXAMPLES::

            sage: Q = ClusterQuiver(['A',5])
            sage: Q.mutate([1,2,4,3,2])
            sage: Q.sinks()
            [0, 2]

            sage: Q = ClusterQuiver(['A',5])
            sage: Q.mutate([2,1,3,4,2])
            sage: Q.sinks()
            [3]
        """
    def first_source(self):
        """
        Return the first vertex of ``self`` that is a source.

        EXAMPLES::

            sage: Q = ClusterQuiver(['A',5])
            sage: Q.mutate([2,1,3,4,2])
            sage: Q.first_source()
            1
        """
    def sources(self) -> list:
        """
        Return all vertices of ``self`` that are sources.

        EXAMPLES::

            sage: Q = ClusterQuiver(['A',5])
            sage: Q.mutate([1,2,4,3,2])
            sage: Q.sources()
            []

            sage: Q = ClusterQuiver(['A',5])
            sage: Q.mutate([2,1,3,4,2])
            sage: Q.sources()
            [1]
        """
    def mutate(self, data, inplace: bool = True):
        """
        Mutate ``self`` at a sequence of vertices.

        INPUT:

        - ``sequence`` -- a vertex of ``self``, an iterator of vertices of
          ``self``, a function which takes in the ClusterQuiver and returns a
          vertex or an iterator of vertices, or a string of the parameter
          wanting to be called on ``ClusterQuiver`` that will return a vertex
          or an iterator of vertices
        - ``inplace`` -- boolean (default: ``True``); if ``False``, the result
          is returned, otherwise ``self`` is modified

        EXAMPLES::

            sage: Q = ClusterQuiver(['A',4]); Q.b_matrix()
            [ 0  1  0  0]
            [-1  0 -1  0]
            [ 0  1  0  1]
            [ 0  0 -1  0]

            sage: Q.mutate(0); Q.b_matrix()
            [ 0 -1  0  0]
            [ 1  0 -1  0]
            [ 0  1  0  1]
            [ 0  0 -1  0]

            sage: T = Q.mutate(0, inplace=False); T
            Quiver on 4 vertices of type ['A', 4]

            sage: Q.mutate(0)
            sage: Q == T
            True

            sage: Q.mutate([0,1,0])
            sage: Q.b_matrix()
            [ 0 -1  1  0]
            [ 1  0  0  0]
            [-1  0  0  1]
            [ 0  0 -1  0]

            sage: Q = ClusterQuiver(QuiverMutationType([['A',1],['A',3]]))
            sage: Q.b_matrix()
            [ 0  0  0  0]
            [ 0  0  1  0]
            [ 0 -1  0 -1]
            [ 0  0  1  0]

            sage: T = Q.mutate(0,inplace=False)
            sage: Q == T
            True

            sage: Q = ClusterQuiver(['A',3]); Q.b_matrix()
            [ 0  1  0]
            [-1  0 -1]
            [ 0  1  0]
            sage: Q.mutate('first_sink'); Q.b_matrix()
            [ 0 -1  0]
            [ 1  0  1]
            [ 0 -1  0]
            sage: Q.mutate('first_source'); Q.b_matrix()
            [ 0  1  0]
            [-1  0 -1]
            [ 0  1  0]

            sage: dg = DiGraph()
            sage: dg.add_vertices(['a','b','c','d','e'])
            sage: dg.add_edges([['a','b'], ['b','c'], ['c','d'], ['d','e']])
            sage: Q2 = ClusterQuiver(dg, frozen=['c']); Q2.b_matrix()
            [ 0  1  0  0]
            [-1  0  0  0]
            [ 0  0  0  1]
            [ 0  0 -1  0]
            [ 0 -1  1  0]
            sage: Q2.mutate('a'); Q2.b_matrix()
            [ 0 -1  0  0]
            [ 1  0  0  0]
            [ 0  0  0  1]
            [ 0  0 -1  0]
            [ 0 -1  1  0]

            sage: dg = DiGraph([['a', 'b'], ['b', 'c']], format='list_of_edges')
            sage: Q = ClusterQuiver(dg);Q
            Quiver on 3 vertices
            sage: Q.mutate(['a','b'],inplace=False).digraph().edges(sort=True)
            [('a', 'b', (1, -1)), ('c', 'b', (1, -1))]

        TESTS::

            sage: Q = ClusterQuiver(['A',4]); Q.mutate(0,1)
            Traceback (most recent call last):
            ...
            ValueError: The second parameter must be boolean.  To mutate at a sequence of length 2, input it as a list.

            sage: Q = ClusterQuiver(['A',4]); Q.mutate(0,0)
            Traceback (most recent call last):
            ...
            ValueError: The second parameter must be boolean.  To mutate at a sequence of length 2, input it as a list.
        """
    def mutation_sequence(self, sequence, show_sequence: bool = False, fig_size: float = 1.2):
        """
        Return a list containing the sequence of quivers obtained from ``self``
        by a sequence of mutations on vertices.

        INPUT:

        - ``sequence`` -- list or tuple of vertices of ``self``
        - ``show_sequence`` -- boolean (default: ``False``); if ``True``, a png
          containing the mutation sequence is shown
        - ``fig_size`` -- (default: 1.2) factor by which the size of the
          sequence is expanded

        EXAMPLES::

            sage: Q = ClusterQuiver(['A',4])
            sage: seq = Q.mutation_sequence([0,1]); seq
            [Quiver on 4 vertices of type ['A', 4],
             Quiver on 4 vertices of type ['A', 4],
             Quiver on 4 vertices of type ['A', 4]]
            sage: [T.b_matrix() for T in seq]
            [
            [ 0  1  0  0]  [ 0 -1  0  0]  [ 0  1 -1  0]
            [-1  0 -1  0]  [ 1  0 -1  0]  [-1  0  1  0]
            [ 0  1  0  1]  [ 0  1  0  1]  [ 1 -1  0  1]
            [ 0  0 -1  0], [ 0  0 -1  0], [ 0  0 -1  0]
            ]
        """
    def reorient(self, data) -> None:
        """
        Reorient ``self`` with respect to the given total order, or
        with respect to an iterator of edges in ``self`` to be
        reverted.

        .. WARNING::

            This operation might change the mutation type of ``self``.

        INPUT:

        - ``data`` -- an iterator defining a total order on
          ``self.vertices()``, or an iterator of edges in ``self`` to
          be reoriented.

        EXAMPLES::

            sage: Q = ClusterQuiver(['A',(2,3),1])
            sage: Q.mutation_type()
            ['A', [2, 3], 1]

            sage: Q.reorient([(0,1),(1,2),(2,3),(3,4)])
            sage: Q.mutation_type()
            ['D', 5]

            sage: Q.reorient([0,1,2,3,4])
            sage: Q.mutation_type()
            ['A', [1, 4], 1]

        TESTS::

            sage: Q = ClusterQuiver(['A',2])
            sage: Q.reorient([])
            Traceback (most recent call last):
            ...
            ValueError: empty input
            sage: Q.reorient([3,4])
            Traceback (most recent call last):
            ...
            ValueError: not a total order on the vertices of the quiver or
            a list of edges to be oriented
        """
    def mutation_class_iter(self, depth=..., show_depth: bool = False, return_paths: bool = False, data_type: str = 'quiver', up_to_equivalence: bool = True, sink_source: bool = False) -> Generator[Incomplete]:
        '''
        Return an iterator for the mutation class of ``self``
        together with certain constraints.

        INPUT:

        - ``depth`` -- integer (default: infinity); only quivers with distance
          at most depth from ``self`` are returned.
        - ``show_depth`` -- boolean (default: ``False``); if ``True``, the
          actual depth of the mutation is shown
        - ``return_paths`` -- boolean (default: ``False``); if ``True``, a
          shortest path of mutation sequences from ``self`` to the given quiver
          is returned as well
        - ``data_type`` -- (default: ``\'quiver\'``) can be one of the following::

            * "quiver"
            * "matrix"
            * "digraph"
            * "dig6"
            * "path"

        - ``up_to_equivalence`` -- boolean (default: ``True``); if ``True``,
          only one quiver for each graph-isomorphism class is recorded
        - ``sink_source`` -- boolean (default: ``False``); if ``True``, only
          mutations at sinks and sources are applied

        EXAMPLES::

            sage: Q = ClusterQuiver([\'A\',3])
            sage: it = Q.mutation_class_iter()
            sage: for T in it: print(T)
            Quiver on 3 vertices of type [\'A\', 3]
            Quiver on 3 vertices of type [\'A\', 3]
            Quiver on 3 vertices of type [\'A\', 3]
            Quiver on 3 vertices of type [\'A\', 3]

            sage: it = Q.mutation_class_iter(depth=1)
            sage: for T in it: print(T)
            Quiver on 3 vertices of type [\'A\', 3]
            Quiver on 3 vertices of type [\'A\', 3]
            Quiver on 3 vertices of type [\'A\', 3]

            sage: it = Q.mutation_class_iter(show_depth=True)
            sage: for T in it: pass
            Depth: 0     found: 1          Time: ... s
            Depth: 1     found: 3          Time: ... s
            Depth: 2     found: 4          Time: ... s

            sage: it = Q.mutation_class_iter(return_paths=True)
            sage: for T in it: print(T)
            (Quiver on 3 vertices of type [\'A\', 3], [])
            (Quiver on 3 vertices of type [\'A\', 3], [1])
            (Quiver on 3 vertices of type [\'A\', 3], [0])
            (Quiver on 3 vertices of type [\'A\', 3], [0, 1])

            sage: it = Q.mutation_class_iter(up_to_equivalence=False)
            sage: for T in it: print(T)
            Quiver on 3 vertices of type [\'A\', 3]
            Quiver on 3 vertices of type [\'A\', 3]
            Quiver on 3 vertices of type [\'A\', 3]
            Quiver on 3 vertices of type [\'A\', 3]
            Quiver on 3 vertices of type [\'A\', 3]
            Quiver on 3 vertices of type [\'A\', 3]
            Quiver on 3 vertices of type [\'A\', 3]
            Quiver on 3 vertices of type [\'A\', 3]
            Quiver on 3 vertices of type [\'A\', 3]
            Quiver on 3 vertices of type [\'A\', 3]
            Quiver on 3 vertices of type [\'A\', 3]
            Quiver on 3 vertices of type [\'A\', 3]
            Quiver on 3 vertices of type [\'A\', 3]
            Quiver on 3 vertices of type [\'A\', 3]

            sage: it = Q.mutation_class_iter(return_paths=True,
            ....:        up_to_equivalence=False)
            sage: mutation_class = list(it)
            sage: len(mutation_class)
            14
            sage: mutation_class[0]
            (Quiver on 3 vertices of type [\'A\', 3], [])

            sage: Q = ClusterQuiver([\'A\',3])
            sage: it = Q.mutation_class_iter(data_type=\'path\')
            sage: for T in it: print(T)
            []
            [1]
            [0]
            [0, 1]

            sage: Q = ClusterQuiver([\'A\',3])
            sage: it = Q.mutation_class_iter(return_paths=True,
            ....:        data_type=\'matrix\')
            sage: next(it)
            (
            [ 0  0  1]
            [ 0  0  1]
            [-1 -1  0], []
            )

            sage: dg = DiGraph([[\'a\', \'b\'], [\'b\', \'c\']],
            ....:        format=\'list_of_edges\')
            sage: S = ClusterQuiver(dg, frozen=[\'b\'])
            sage: S.mutation_class()
            [Quiver on 3 vertices with 1 frozen vertex,
             Quiver on 3 vertices with 1 frozen vertex,
             Quiver on 3 vertices with 1 frozen vertex]
        '''
    def mutation_class(self, depth=..., show_depth: bool = False, return_paths: bool = False, data_type: str = 'quiver', up_to_equivalence: bool = True, sink_source: bool = False):
        """
        Return the mutation class of ``self`` together with certain constraints.

        INPUT:

        - ``depth`` -- (default: ``infinity``) integer, only seeds with
          distance at most depth from ``self`` are returned
        - ``show_depth`` -- boolean (default: ``False``); if ``True``, the
          actual depth of the mutation is shown
        - ``return_paths`` -- boolean (default: ``False``); if ``True``, a
          shortest path of mutation sequences from ``self`` to the given
          quiver is returned as well
        - ``data_type`` -- (default: ``'quiver'``) can be one of
          the following:

          * ``'quiver'`` -- the quiver is returned
          * ``'dig6'`` -- the dig6-data is returned
          * ``'path'`` -- shortest paths of mutation sequences from
            ``self`` are returned

        - ``sink_source`` -- boolean (default: ``False``); if ``True``, only
          mutations at sinks and sources are applied

        EXAMPLES::

            sage: Q = ClusterQuiver(['A',3])
            sage: Ts = Q.mutation_class()
            sage: for T in Ts: print(T)
            Quiver on 3 vertices of type ['A', 3]
            Quiver on 3 vertices of type ['A', 3]
            Quiver on 3 vertices of type ['A', 3]
            Quiver on 3 vertices of type ['A', 3]

            sage: Ts = Q.mutation_class(depth=1)
            sage: for T in Ts: print(T)
            Quiver on 3 vertices of type ['A', 3]
            Quiver on 3 vertices of type ['A', 3]
            Quiver on 3 vertices of type ['A', 3]

            sage: Ts = Q.mutation_class(show_depth=True)
            Depth: 0     found: 1          Time: ... s
            Depth: 1     found: 3          Time: ... s
            Depth: 2     found: 4          Time: ... s

            sage: Ts = Q.mutation_class(return_paths=True)
            sage: for T in Ts: print(T)
            (Quiver on 3 vertices of type ['A', 3], [])
            (Quiver on 3 vertices of type ['A', 3], [1])
            (Quiver on 3 vertices of type ['A', 3], [0])
            (Quiver on 3 vertices of type ['A', 3], [0, 1])

            sage: Ts = Q.mutation_class(up_to_equivalence=False)
            sage: for T in Ts: print(T)
            Quiver on 3 vertices of type ['A', 3]
            Quiver on 3 vertices of type ['A', 3]
            Quiver on 3 vertices of type ['A', 3]
            Quiver on 3 vertices of type ['A', 3]
            Quiver on 3 vertices of type ['A', 3]
            Quiver on 3 vertices of type ['A', 3]
            Quiver on 3 vertices of type ['A', 3]
            Quiver on 3 vertices of type ['A', 3]
            Quiver on 3 vertices of type ['A', 3]
            Quiver on 3 vertices of type ['A', 3]
            Quiver on 3 vertices of type ['A', 3]
            Quiver on 3 vertices of type ['A', 3]
            Quiver on 3 vertices of type ['A', 3]
            Quiver on 3 vertices of type ['A', 3]

            sage: Ts = Q.mutation_class(return_paths=True,up_to_equivalence=False)
            sage: len(Ts)
            14
            sage: Ts[0]
            (Quiver on 3 vertices of type ['A', 3], [])

            sage: Ts = Q.mutation_class(show_depth=True)
            Depth: 0     found: 1          Time: ... s
            Depth: 1     found: 3          Time: ... s
            Depth: 2     found: 4          Time: ... s

            sage: Ts = Q.mutation_class(show_depth=True, up_to_equivalence=False)
            Depth: 0     found: 1          Time: ... s
            Depth: 1     found: 4          Time: ... s
            Depth: 2     found: 6          Time: ... s
            Depth: 3     found: 10        Time: ... s
            Depth: 4     found: 14        Time: ... s

        TESTS::

            sage: all(len(ClusterQuiver(['A',n]).mutation_class())
            ....:     == ClusterQuiver(['A',n]).mutation_type().class_size()
            ....:     for n in [2..6])
            True

            sage: all(len(ClusterQuiver(['B',n]).mutation_class())
            ....:     == ClusterQuiver(['B',n]).mutation_type().class_size()
            ....:     for n in [2..6])
            True
        """
    def is_finite(self) -> bool:
        """
        Return ``True`` if ``self`` is of finite type.

        EXAMPLES::

            sage: Q = ClusterQuiver(['A',3])
            sage: Q.is_finite()
            True
            sage: Q = ClusterQuiver(['A',[2,2],1])
            sage: Q.is_finite()
            False
            sage: Q = ClusterQuiver([['A',3],['B',3]])
            sage: Q.is_finite()
            True
            sage: Q = ClusterQuiver(['T',[4,4,4]])
            sage: Q.is_finite()
            False
            sage: Q = ClusterQuiver([['A',3],['T',[4,4,4]]])
            sage: Q.is_finite()
            False
            sage: Q = ClusterQuiver([['A',3],['T',[2,2,3]]])
            sage: Q.is_finite()
            True
            sage: Q = ClusterQuiver([['A',3],['D',5]])
            sage: Q.is_finite()
            True
            sage: Q = ClusterQuiver([['A',3],['D',5,1]])
            sage: Q.is_finite()
            False

            sage: Q = ClusterQuiver([[0,1,2],[1,2,2],[2,0,2]])
            sage: Q.is_finite()
            False

            sage: Q = ClusterQuiver([[0,1,2],[1,2,2],[2,0,2],[3,4,1],[4,5,1]])
            sage: Q.is_finite()
            False
        """
    def is_mutation_finite(self, nr_of_checks=None, return_path: bool = False) -> bool:
        """
        Return whether ``self`` is mutation-finite.

        This uses a non-deterministic method by random mutations in various
        directions. This can result in a wrong answer.

        INPUT:

        - ``nr_of_checks`` -- (default: ``None``) number of mutations applied;
          Standard is 500*(number of vertices of ``self``)
        - ``return_path`` -- (default: ``False``) if ``True``, in case of
          ``self`` not being mutation finite, a path from ``self`` to a quiver
          with an edge label `(a,-b)` and `a*b > 4` is returned

        ALGORITHM:

        A quiver is mutation infinite if and only if every
        edge label (a,-b) satisfy a*b > 4.
        Thus, we apply random mutations in random directions

        EXAMPLES::

            sage: Q = ClusterQuiver(['A',10])
            sage: Q._mutation_type = None
            sage: Q.is_mutation_finite()
            True

            sage: Q = ClusterQuiver([(0,1),(1,2),(2,3),(3,4),
            ....:                    (4,5),(5,6),(6,7),(7,8),(2,9)])
            sage: Q.is_mutation_finite()
            False
        """
    def number_of_edges(self):
        """
        Return the total number of edges on the quiver.

        .. NOTE::

            This only works with non-valued quivers. If used on a
            non-valued quiver then the positive value is taken to be
            the number of edges added.

        OUTPUT: integer of the number of edges

        EXAMPLES::

            sage: S = ClusterQuiver(['A',4]); S.number_of_edges()
            3

            sage: S = ClusterQuiver(['B',4]); S.number_of_edges()
            3
        """
    def relabel(self, relabelling, inplace: bool = True):
        """
        Return the quiver after doing a relabelling.

        Will relabel the vertices of the quiver.

        INPUT:

        - ``relabelling`` -- dictionary of labels to move around
        - ``inplace`` -- boolean (default: ``True``); if ``True``, will return
          a duplicate of the quiver

        EXAMPLES::

            sage: S = ClusterQuiver(['A',4]).relabel({1:'5',2:'go'})
        """
    def poincare_semistable(self, theta, d):
        """
        Return the Poincaré polynomial of the moduli space of semi-stable
        representations of dimension vector `d`.

        INPUT:

        - ``theta`` -- stability weight, as list or vector of rationals
        - ``d`` -- dimension vector, as list or vector of coprime integers

        The semi-stability is taken with respect to the slope function

        .. MATH::

             \\mu(d) = \\theta(d) / \\operatorname{dim}(d)

        where `d` is a dimension vector.

        This uses the matrix-inversion algorithm from [Rei2002]_.

        EXAMPLES::

            sage: Q = ClusterQuiver(['A',2])
            sage: Q.poincare_semistable([1,0],[1,0])
            1
            sage: Q.poincare_semistable([1,0],[1,1])
            1

            sage: K2 = ClusterQuiver(matrix([[0,2],[-2,0]]))
            sage: theta = (1, 0)
            sage: K2.poincare_semistable(theta, [1,0])
            1
            sage: K2.poincare_semistable(theta, [1,1])
            v^2 + 1
            sage: K2.poincare_semistable(theta, [1,2])
            1
            sage: K2.poincare_semistable(theta, [1,3])
            0

            sage: K3 = ClusterQuiver(matrix([[0,3],[-3,0]]))
            sage: theta = (1, 0)
            sage: K3.poincare_semistable(theta, (2,3))
            v^12 + v^10 + 3*v^8 + 3*v^6 + 3*v^4 + v^2 + 1
            sage: K3.poincare_semistable(theta, (3,4))(1)
            68

        TESTS::

            sage: Q = ClusterQuiver(['A',2])
            sage: Q.poincare_semistable([1,0],[2,2])
            Traceback (most recent call last):
            ...
            ValueError: dimension vector d is not coprime

            sage: Q = ClusterQuiver(['A',3])
            sage: Q.poincare_semistable([1,1,0],[2,3,4])
            0

        REFERENCES:

        .. [Rei2002] Markus Reineke, *The Harder-Narasimhan system in quantum
           groups and cohomology of quiver moduli*, :arxiv:`math/0204059`
        """
    def d_vector_fan(self):
        """
        Return the d-vector fan associated with the quiver.

        It is the fan whose maximal cones are generated by the
        d-matrices of the clusters.

        This is a complete simplicial fan (and even smooth when the
        initial quiver is acyclic). It only makes sense for quivers of
        finite type.

        EXAMPLES::

            sage: # needs sage.geometry.polyhedron sage.libs.singular
            sage: Fd = ClusterQuiver([[1,2]]).d_vector_fan(); Fd
            Rational polyhedral fan in 2-d lattice N
            sage: Fd.ngenerating_cones()
            5
            sage: Fd = ClusterQuiver([[1,2],[2,3]]).d_vector_fan(); Fd
            Rational polyhedral fan in 3-d lattice N
            sage: Fd.ngenerating_cones()
            14
            sage: Fd.is_smooth()
            True
            sage: Fd = ClusterQuiver([[1,2],[2,3],[3,1]]).d_vector_fan(); Fd
            Rational polyhedral fan in 3-d lattice N
            sage: Fd.ngenerating_cones()
            14
            sage: Fd.is_smooth()
            False

        TESTS::

            sage: ClusterQuiver(['A',[2,2],1]).d_vector_fan()
            Traceback (most recent call last):
            ...
            ValueError: only makes sense for quivers of finite type
        """
    def g_vector_fan(self):
        """
        Return the g-vector fan associated with the quiver.

        It is the fan whose maximal cones are generated by the
        g-matrices of the clusters.

        This is a complete simplicial fan. It is only supported for
        quivers of finite type.

        EXAMPLES::

            sage: Fg = ClusterQuiver([[1,2]]).g_vector_fan(); Fg
            Rational polyhedral fan in 2-d lattice N
            sage: Fg.ngenerating_cones()
            5

            sage: Fg = ClusterQuiver([[1,2],[2,3]]).g_vector_fan(); Fg
            Rational polyhedral fan in 3-d lattice N
            sage: Fg.ngenerating_cones()
            14
            sage: Fg.is_smooth()
            True

            sage: Fg = ClusterQuiver([[1,2],[2,3],[3,1]]).g_vector_fan(); Fg
            Rational polyhedral fan in 3-d lattice N
            sage: Fg.ngenerating_cones()
            14
            sage: Fg.is_smooth()
            True

        TESTS::

            sage: ClusterQuiver(['A',[2,2],1]).g_vector_fan()
            Traceback (most recent call last):
            ...
            ValueError: only supported for quivers of finite type
        """
