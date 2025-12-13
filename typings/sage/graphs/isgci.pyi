from _typeshed import Incomplete
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

graph_classes: Incomplete
