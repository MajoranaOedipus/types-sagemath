r"""
ISGCI: Information System on Graph Classes and their Inclusions

This module implements an interface to the
`ISGCI <http://www.graphclasses.org/>`_ database in Sage.

This database gathers information on graph classes and their inclusions in each
other. It also contains information on the complexity of several computational
problems.

It is available on the `GraphClasses.org <http://www.graphclasses.org/>`_
website maintained by H.N. de Ridder et al.

How to use it?
--------------

Presently, it is possible to use this database through the variables and methods
present in the :obj:`graph_classes <GraphClasses>` object.
For instance::

    sage: Trees = graph_classes.Tree
    sage: Chordal = graph_classes.Chordal

Inclusions
^^^^^^^^^^

It is then possible to check the inclusion of classes inside of others, if the
information is available in the database::

    sage: Trees <= Chordal
    True

And indeed, trees are chordal graphs.

The ISGCI database is not all-knowing, and so comparing two classes can return
``True``, ``False``, or ``Unknown`` (see the :mod:`documentation of the Unknown
truth value <sage.misc.unknown>`).

An *unknown* answer to ``A <= B`` only means that ISGCI cannot deduce from the
information in its database that ``A`` is a subclass of ``B`` nor that it is
not. For instance, ISGCI does not know at the moment that some chordal graphs
are not trees::

    sage: graph_classes.Chordal <= graph_classes.Tree
    Unknown

Descriptions
^^^^^^^^^^^^

Given a graph class, one can obtain its associated information in the ISGCI
database with the :meth:`~GraphClass.description` method::

    sage: Chordal.description()
    Class of graphs : Chordal
    -------------------------
    id                             :  gc_32
    name                           :  chordal
    ...
    Problems :
    -----------
    3-Colourability                :  Linear
    Clique                         :  Polynomial
    Clique cover                   :  Polynomial
    ...

It is possible to obtain the complete list of the classes stored in ISGCI by
calling the :meth:`~GraphClasses.show_all` method (beware -- long output)::

    sage: graph_classes.show_all()
    id        | name                                     | type                 | smallgraph
    ----------------------------------------------------------------------------------------------------------------------
    gc_309    | $K_4$--minor--free                       | base                 |
    gc_541    | $N^*$                                    | base                 |
    gc_215    | $N^*$--perfect                           | base                 |
    gc_5      | $P_4$--bipartite                         | base                 |
    gc_3      | $P_4$--brittle                           | base                 |
    gc_6      | $P_4$--comparability                     | base                 |
    gc_7      | $P_4$--extendible                        | base                 |
    ...

Until a proper search method is implemented, this lets one find classes which do
not appear in :obj:`graph_classes.* <GraphClasses>`.

To retrieve a class of graph from its ISGCI ID one may use
the :meth:`~GraphClasses.get_class` method::

    sage: GC = graph_classes.get_class("gc_5")
    sage: GC
    $P_4$--bipartite graphs

Recognition of graphs
^^^^^^^^^^^^^^^^^^^^^

The graph classes represented by the ISGCI database can alternatively be used to
access recognition algorithms. For instance, in order to check that a given
graph is a tree one has the following the options ::

    sage: graphs.PathGraph(5) in graph_classes.Tree
    True

or::

    sage: graphs.PathGraph(5).is_tree()
    True

Furthermore, all ISGCI graph classes which are defined by the exclusion of a
finite sequence of induced subgraphs benefit from a generic recognition
algorithm. For instance ::

    sage: g = graphs.PetersenGraph()
    sage: g in graph_classes.ClawFree
    False
    sage: g.line_graph() in graph_classes.ClawFree
    True

Or directly from ISGCI ::

    sage: gc = graph_classes.get_class("gc_441")
    sage: gc
    diamond--free graphs
    sage: graphs.PetersenGraph() in gc
    True

Predefined classes
------------------

:obj:`graph_classes <GraphClasses>` currently predefines the following graph classes

.. list-table::
   :widths: 20 30
   :header-rows: 1

   * - Class
     - Related methods

   * - Apex

     - :meth:`~sage.graphs.graph.Graph.is_apex`,
       :meth:`~sage.graphs.graph.Graph.apex_vertices`

   * - AT_free

     - :meth:`~sage.graphs.graph.Graph.is_asteroidal_triple_free`

   * - Biconnected

     - :meth:`~sage.graphs.generic_graph.GenericGraph.is_biconnected`,
       :meth:`~sage.graphs.generic_graph.GenericGraph.blocks_and_cut_vertices`,
       :meth:`~sage.graphs.generic_graph.GenericGraph.blocks_and_cuts_tree`

   * - BinaryTrees

     - :meth:`~sage.graphs.graph_generators.GraphGenerators.BalancedTree`,
       :meth:`~sage.graphs.graph.Graph.is_tree`

   * - Bipartite

     - :meth:`~sage.graphs.graph_generators.GraphGenerators.BalancedTree`,
       :meth:`~sage.graphs.generic_graph.GenericGraph.is_bipartite`

   * - Block

     - :meth:`~sage.graphs.graph.Graph.is_block_graph`,
       :meth:`~sage.graphs.generic_graph.GenericGraph.blocks_and_cut_vertices`,
       :meth:`~sage.graphs.graph_generators.GraphGenerators.RandomBlockGraph`

   * - Chordal

     - :meth:`~sage.graphs.generic_graph.GenericGraph.is_chordal`

   * - Claw-Free
     - :meth:`~sage.graphs.graph_generators.GraphGenerators.ClawGraph`

   * - Comparability
     -

   * - Gallai

     - :meth:`~sage.graphs.generic_graph.GenericGraph.is_gallai_tree`

   * - Grid

     - :meth:`~sage.graphs.graph_generators.GraphGenerators.Grid2dGraph`,
       :meth:`~sage.graphs.graph_generators.GraphGenerators.GridGraph`

   * - Interval

     - :meth:`~sage.graphs.graph_generators.GraphGenerators.RandomIntervalGraph`,
       :meth:`~sage.graphs.graph_generators.GraphGenerators.IntervalGraph`,
       :meth:`~sage.graphs.generic_graph.GenericGraph.is_interval`

   * - Line

     - :meth:`~sage.graphs.graph_generators.GraphGenerators.line_graph_forbidden_subgraphs`,
       :meth:`~sage.graphs.graph.Graph.is_line_graph`

   * - Modular

     - :meth:`~sage.graphs.graph.Graph.modular_decomposition`

   * - Outerplanar

     - :meth:`~sage.graphs.generic_graph.GenericGraph.is_circular_planar`

   * - Perfect

     - :meth:`~sage.graphs.graph.Graph.is_perfect`

   * - Planar

     - :meth:`~sage.graphs.generic_graph.GenericGraph.is_planar`

   * - Polyhedral

     - :meth:`~sage.graphs.graph.Graph.is_polyhedral`

   * - Split

     - :meth:`~sage.graphs.graph.Graph.is_split`

   * - Tree

     - :meth:`~sage.graphs.graph_generators.GraphGenerators.trees`,
       :meth:`~Graph.is_tree`

   * - UnitDisk
     - :meth:`~sage.graphs.graph_generators.GraphGenerators.IntervalGraph`

   * - UnitInterval
     - :meth:`~sage.graphs.generic_graph.GenericGraph.is_interval`

Sage's view of ISGCI
--------------------

The database is stored by Sage in two ways.

**The classes**: the list of all graph classes and their properties is stored
in a huge dictionary (see :meth:`~sage.graphs.isgci.GraphClasses.classes`).
Below is what Sage knows of ``gc_249``::

    sage: graph_classes.classes()['gc_249']        # random
    {'problem':
        {'Independent set': 'Polynomial',
         'Treewidth': 'Unknown',
         'Weighted independent set': 'Polynomial',
         'Cliquewidth expression': 'NP-complete',
         'Weighted clique': 'Polynomial',
         'Clique cover': 'Unknown',
         'Domination': 'NP-complete',
         'Clique': 'Polynomial',
         'Colourability': 'NP-complete',
         'Cliquewidth': 'Unbounded',
         '3-Colourability': 'NP-complete',
         'Recognition': 'Linear'},
     'type': 'base',
     'id': 'gc_249',
     'name': 'line'}

**The class inclusion digraph**: Sage remembers the class inclusions through
the inclusion digraph (see :meth:`~sage.graphs.isgci.GraphClasses.inclusion_digraph`).
Its nodes are ID of ISGCI classes::

    sage: d = graph_classes.inclusion_digraph()
    sage: d.vertices(sort=True)[-10:]
    ['gc_990', 'gc_991', 'gc_992', 'gc_993', 'gc_994', 'gc_995', 'gc_996', 'gc_997', 'gc_998', 'gc_999']

An arc from ``gc1`` to ``gc2`` means that ``gc1`` is a superclass of ``gc2``.
This being said, not all edges are stored ! To ensure that a given class is
included in another one, we have to check whether there is in the digraph a
``path`` from the first one to the other::

    sage: bip_id = graph_classes.Bipartite._gc_id
    sage: perfect_id = graph_classes.Perfect._gc_id
    sage: d.has_edge(perfect_id, bip_id)
    False
    sage: d.distance(perfect_id, bip_id)
    2

Hence bipartite graphs are perfect graphs. We can see how ISGCI obtains this
result ::

    sage: p = d.shortest_path(perfect_id, bip_id)
    sage: len(p) - 1
    2
    sage: print(p)                  # random
    ['gc_56', 'gc_76', 'gc_69']
    sage: for c in p:
    ....:     print(graph_classes.get_class(c))
    perfect graphs
    ...
    bipartite graphs

What ISGCI knows is that perfect graphs contain unimodular graph which contain
bipartite graphs. Therefore bipartite graphs are perfect !

.. NOTE::

    The inclusion digraph is **NOT ACYCLIC**. Indeed, several entries exist in
    the ISGCI database which represent the same graph class, for instance
    Perfect graphs and Berge graphs::

        sage: graph_classes.inclusion_digraph().is_directed_acyclic()
        False
        sage: Berge = graph_classes.get_class("gc_274"); Berge
        Berge graphs
        sage: Perfect = graph_classes.get_class("gc_56"); Perfect
        perfect graphs
        sage: Berge <= Perfect
        True
        sage: Perfect <= Berge
        True
        sage: Perfect == Berge
        True

Information for developers
--------------------------

* The database is loaded not *so* large, but it is still preferable to
  only load it on demand. This is achieved through the cached methods
  :meth:`~sage.graphs.isgci.GraphClasses.classes` and
  :meth:`~sage.graphs.isgci.GraphClasses.inclusion_digraph`.

* Upon the first access to the database, the information is extracted
  from the XML file and stored in the cache of three methods:

  * ``sage.graphs.isgci._classes`` (dictionary)
  * ``sage.graphs.isgci._inclusions`` (list of dictionaries)
  * ``sage.graphs.isgci._inclusion_digraph`` (DiGraph)

  Note that the digraph is only built if necessary (for instance if
  the user tries to compare two classes).

.. TODO::

    Technical things:

    * Query the database for non-inclusion results so that comparisons can
      return ``False``, and implement strict inclusions.

    * Implement a proper search method for the classes not listed in
      :obj:`graph_classes <GraphClasses>`

      .. SEEALSO:: :func:`sage.graphs.isgci.show_all`.

    * Some of the graph classes appearing in :obj:`graph_classes
      <GraphClasses>` already have a recognition
      algorithm implemented in Sage. It would be so nice to be able to
      write ``g in Trees``, ``g in Perfect``, ``g in Chordal``, ... :-)

    Long-term stuff:

    * Implement simple accessors for all the information in the ISGCI
      database (as can be done from the website)

    * Implement intersection of graph classes

    * Write generic recognition algorithms for specific classes (when a graph
      class is defined by the exclusion of subgraphs, one can write a generic
      algorithm checking the existence of each of the graphs, and this method
      already exists in Sage).

    * Improve the performance of Sage's graph library by letting it take
      advantage of the properties of graph classes. For example,
      :meth:`Graph.independent_set` could use the library to detect that a given
      graph is, say, a tree or a planar graph, and use a specialized algorithm
      for finding an independent set.

AUTHORS:
--------

* H.N. de Ridder et al. (ISGCI database)
* Nathann Cohen (Sage implementation)

Methods
-------
"""

from sage.features.databases import DatabaseGraphs as DatabaseGraphs
from sage.misc.cachefunc import cached_method as cached_method
from sage.misc.unknown import Unknown as Unknown
from sage.structure.sage_object import SageObject as SageObject
from sage.structure.unique_representation import CachedRepresentation as CachedRepresentation, UniqueRepresentation as UniqueRepresentation

class GraphClass(SageObject, CachedRepresentation):
    """
    An instance of this class represents a Graph Class, matching some entry in
    the ISGCI database.

    EXAMPLES:

    Testing the inclusion of two classes::

        sage: Chordal = graph_classes.Chordal
        sage: Trees = graph_classes.Tree
        sage: Trees <= Chordal
        True
        sage: Chordal <= Trees
        Unknown

    TESTS::

        sage: Trees >= Chordal
        Unknown
        sage: Chordal >= Trees
        True
    """
    def __init__(self, name, gc_id, recognition_function=None) -> None:
        """
        Class constructor.

        INPUT:

        - ``gc_id`` -- the ISGCI class ID

        - ``recognition_function`` -- a function of one argument `g`, which
          return boolean answers to the question : *does ``g`` belong to the
          class represented by ``gc_id`` ?*

        EXAMPLES::

            sage: graph_classes.Chordal  # indirect doctest
            Chordal graphs
        """
    def __hash__(self):
        """
        Return the class' ID hash.

        EXAMPLES::

            sage: hash(graph_classes.Chordal) == hash(graph_classes.Chordal)
            True
        """
    def __le__(self, other):
        """
        <= operator.

        EXAMPLES::

            sage: graph_classes.Chordal <= graph_classes.Tree
            Unknown
        """
    def __ge__(self, other):
        """
        >= operator.

        EXAMPLES::

            sage: graph_classes.Chordal >= graph_classes.Tree
            True
        """
    def __eq__(self, other):
        """
        == operator.

        EXAMPLES::

            sage: graph_classes.Chordal == graph_classes.Tree
            Unknown
        """
    def __lt__(self, other):
        """
        >, !=, and < operators.

        EXAMPLES::

            sage: graph_classes.Chordal > graph_classes.Tree
            Traceback (most recent call last):
            ...
            NotImplementedError
            sage: graph_classes.Chordal < graph_classes.Tree
            Traceback (most recent call last):
            ...
            NotImplementedError
            sage: graph_classes.Chordal != graph_classes.Tree
            Traceback (most recent call last):
            ...
            NotImplementedError
        """
    __gt__ = __lt__
    __ne__ = __lt__
    def forbidden_subgraphs(self):
        """
        Return the list of forbidden induced subgraphs defining the class.

        If the graph class is not defined by a *finite* list of forbidden
        induced subgraphs, ``None`` is returned instead.

        EXAMPLES::

            sage: graph_classes.Perfect.forbidden_subgraphs()
            sage: gc = graph_classes.get_class('gc_62')
            sage: gc
            claw--free graphs
            sage: gc.forbidden_subgraphs()
            [Graph on 4 vertices]
            sage: gc.forbidden_subgraphs()[0].is_isomorphic(graphs.ClawGraph())
            True
        """
    def __contains__(self, g) -> bool:
        """
        Check if ``g`` belongs to the graph class represented by ``self``.

        EXAMPLES::

            sage: graphs.CompleteBipartiteGraph(3,3) in graph_classes.Bipartite
            True
            sage: graphs.CompleteGraph(4) in graph_classes.Chordal
            True
            sage: graphs.CompleteGraph(4) in graph_classes.Comparability
            True
            sage: graphs.CompleteGraph(4) in graph_classes.Interval
            True
            sage: graphs.CompleteGraph(4) in graph_classes.Line
            True
            sage: graphs.CompleteGraph(4) in graph_classes.Perfect
            True
            sage: graphs.CompleteGraph(4) in graph_classes.Planar
            True
            sage: graphs.CompleteGraph(4) in graph_classes.Split
            True
            sage: graphs.PathGraph(4) in graph_classes.Tree
            True
        """
    def description(self) -> None:
        """
        Print the information of ISGCI about the current class.

        EXAMPLES::

            sage: graph_classes.Chordal.description()
            Class of graphs : Chordal
            -------------------------
            id                             :  gc_32
            name                           :  chordal
            ...
            Problems :
            -----------
            3-Colourability                :  Linear
            Clique                         :  Polynomial
            Clique cover                   :  Polynomial
            ...
            Recognition                    :  Linear
            ...
        """

class GraphClasses(UniqueRepresentation):
    def get_class(self, id):
        '''
        Return the class corresponding to the given id in the ISGCI database.

        INPUT:

        - ``id`` -- string; the desired class\' ID

        .. SEEALSO::

            :meth:`~sage.graphs.isgci.GraphClasses.show_all`

        EXAMPLES:

        With an existing id::

            sage: Cographs = graph_classes.get_class("gc_151")
            sage: Cographs
            cograph graphs

        With a wrong id::

            sage: graph_classes.get_class(-1)
            Traceback (most recent call last):
            ...
            ValueError: The given class id does not exist in the ISGCI database. Is the db too old ? You can update it with graph_classes.update_db().
        '''
    @cached_method
    def classes(self):
        '''
        Return the graph classes, as a dictionary.

        Upon the first call, this loads the database from the local XML
        file. Subsequent calls are cached.

        EXAMPLES::

            sage: t = graph_classes.classes()
            sage: type(t)
            <... \'dict\'>
            sage: sorted(t["gc_151"].keys())
            [\'id\', \'name\',... \'problem\',... \'type\']
            sage: t["gc_151"][\'name\']
            \'cograph\'
            sage: t["gc_151"][\'problem\'][\'Clique\']
            {\'complexity\': \'Linear\'}
        '''
    @cached_method
    def inclusions(self):
        """
        Return the graph class inclusions.

        OUTPUT: list of dictionaries

        Upon the first call, this loads the database from the local XML file.
        Subsequent calls are cached.

        EXAMPLES::

            sage: t = graph_classes.inclusions()
            sage: type(t)
            <... 'list'>
            sage: t[0]
            {'sub': 'gc_1', 'super': 'gc_2'}
        """
    @cached_method
    def smallgraphs(self):
        """
        Return a dictionary associating a graph to a graph description string.

        Upon the first call, this loads the database from the local XML files.
        Subsequent calls are cached.

        EXAMPLES::

            sage: t = graph_classes.smallgraphs()
            sage: t['2C_4']
            Graph on 8 vertices
            sage: t['2K_3 + e']
            Graph on 6 vertices
            sage: t['fish']
            Graph on 6 vertices
            sage: t['bull']
            Graph on 5 vertices
        """
    @cached_method
    def inclusion_digraph(self):
        """
        Return the class inclusion digraph.

        Upon the first call, this loads the database from the local XML file.
        Subsequent calls are cached.

        EXAMPLES::

            sage: g = graph_classes.inclusion_digraph(); g
            Digraph on ... vertices
        """
    def update_db(self) -> None:
        """
        Update the ISGCI database by downloading the latest version from
        internet.

        This method downloads the ISGCI database from the website
        `GraphClasses.org <http://www.graphclasses.org/>`_. It then extracts the
        zip file and parses its XML content. The XML file is saved in the directory
        controlled by the :class:`DatabaseGraphs` class (usually, ``$HOME/.sage/db``).

        EXAMPLES::

            sage: graph_classes.update_db()  # optional - internet
            Database downloaded
        """
    def show_all(self):
        """
        Print all graph classes stored in ISGCI.

        EXAMPLES::

            sage: graph_classes.show_all()
            id        | name                                     | type                 | smallgraph
            ----------------------------------------------------------------------------------------------------------------------
            gc_309    | $K_4$--minor--free                       | base                 |
            gc_541    | $N^*$                                    | base                 |
            gc_215    | $N^*$--perfect                           | base                 |
            gc_5      | $P_4$--bipartite                         | base                 |
            gc_3      | $P_4$--brittle                           | base                 |
            gc_6      | $P_4$--comparability                     | base                 |
            gc_7      | $P_4$--extendible                        | base                 |
            ...
        """

graph_classes: GraphClasses
