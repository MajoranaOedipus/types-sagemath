from . import graph as graph
from _typeshed import Incomplete
from collections.abc import Generator
from sage.databases.sql_db import SQLDatabase as SQLDatabase, SQLQuery as SQLQuery
from sage.features.databases import DatabaseGraphs as DatabaseGraphs
from sage.graphs.graph import Graph as Graph
from sage.rings.integer import Integer as Integer

dblocation: Incomplete

def degseq_to_data(degree_sequence):
    """
    Convert a degree sequence list to a sorted (max-min) integer data type.

    The input degree sequence list (of Integers) is converted to a sorted
    (max-min) integer data type, as used for faster access in the underlying
    database.

    INPUT:

    - ``degree_sequence`` -- list of integers; input degree sequence list

    EXAMPLES::

        sage: from sage.graphs.graph_database import degseq_to_data
        sage: degseq_to_data([2,2,3,1])
        3221
    """
def data_to_degseq(data, graph6=None):
    """
    Convert a database integer data type to a degree sequence list.

    INPUT:

    - ``data`` -- integer data type (one digit per vertex representing its
      degree, sorted high to low) to be converted to a degree sequence list

    - ``graph6`` -- string (default: ``None``); the ``graph6`` identifier is
      required for all graphs with no edges, so that the correct number of zeros
      is returned.

    EXAMPLES::

        sage: from sage.graphs.graph_database import data_to_degseq
        sage: data_to_degseq(3221)
        [1, 2, 2, 3]
        sage: data_to_degseq(0, 'D??')
        [0, 0, 0, 0, 0]
    """
def graph6_to_plot(graph6):
    """
    Return a ``Graphics`` object from a ``graph6`` string.

    This method constructs a graph from a ``graph6`` string and returns a
    :class:`sage.plot.graphics.Graphics` object with arguments preset for the
    :meth:`sage.plot.graphics.Graphics.show` method.

    INPUT:

    - ``graph6`` -- a ``graph6`` string

    EXAMPLES::

        sage: from sage.graphs.graph_database import graph6_to_plot
        sage: type(graph6_to_plot('D??'))                                               # needs sage.plot
        <class 'sage.plot.graphics.Graphics'>
    """
def subgraphs_to_query(subgraphs, db):
    """
    Return a GraphQuery object required for the induced_subgraphs parameter.

    This method constructs and returns a :class:`~GraphQuery` object respecting
    the special input required for the ``induced_subgraphs`` parameter.

    INPUT:

    - ``subgraphs`` -- list of strings; the list should be of one of the
      following two formats:

      - ``['one_of', String, ..., String]`` -- will search for graphs containing
        a subgraph isomorphic to *any* of the ``graph6`` strings in the list

      - ``['all_of', String, ..., String]`` -- will search for graphs containing
        a subgraph isomorphic to *each* of the ``graph6`` strings in the list

    - ``db`` -- a :class:`~GraphDatabase`

    .. NOTE::

        This is a helper method called by the :class:`~GraphQuery` constructor
        to handle this special format. This method should not be used on its own
        because it doesn't set any display columns in the query string, causing
        a failure to fetch the data when run.

    EXAMPLES::

        sage: from sage.graphs.graph_database import subgraphs_to_query
        sage: gd = GraphDatabase()
        sage: q = subgraphs_to_query(['all_of', 'A?', 'B?', 'C?'], gd)
        sage: q.get_query_string()
        'SELECT ,,,,,  FROM misc WHERE ( ( misc.induced_subgraphs regexp ? ) AND (
        misc.induced_subgraphs regexp ? ) ) AND ( misc.induced_subgraphs regexp ? )'
    """

aut_grp: Incomplete
degrees: Incomplete
misc: Incomplete
spectrum: Incomplete
graph_data: Incomplete
valid_kwds: Incomplete

def graph_db_info(tablename=None):
    """
    Return a dictionary of allowed table and column names.

    INPUT:

    - ``tablename`` -- restricts the output to a single table

    EXAMPLES::

        sage: sorted(graph_db_info())
        ['aut_grp', 'degrees', 'graph_data', 'misc', 'spectrum']

    ::

        sage: graph_db_info(tablename='graph_data')
        ['complement_graph6',
         'eulerian',
         'graph6',
         'lovasz_number',
         'num_cycles',
         'num_edges',
         'num_hamiltonian_cycles',
         'num_vertices',
         'perfect',
         'planar']
    """

class GenericGraphQuery(SQLQuery):
    def __init__(self, query_string, database=None, param_tuple=None) -> None:
        """
        A query for a :class:`~GraphDatabase`.

        INPUT:

        - ``query_string`` -- string representing the SQL query

        - ``database`` -- (default: ``None``) the :class:`~GraphDatabase`
          instance to query (if ``None`` then a new instance is created)

        - ``param_tuple`` -- tuple of strings (default: ``None``); what to
          replace question marks in ``query_string`` with (optional, but a good
          idea)

        .. NOTE::

           This query class is generally intended for developers and more
           advanced users. It allows you to execute any query, and so may be
           considered unsafe.

        EXAMPLES:

        See :class:`~GraphDatabase` class docstrings or enter::

            sage: G = GraphDatabase()
            sage: G.get_skeleton()
            {...

        to see the underlying structure of the database. Also see
        :class:`sage.databases.sql_db.SQLQuery` in :mod:`sage.databases.sql_db`
        for more info and a tutorial.

        A piece of advice about '?' and param_tuple: it is generally considered
        safer to query with a '?' in place of each value parameter, and using a
        second argument (a tuple of strings) in a call to the ``sqlite``
        database. Successful use of the ``param_tuple`` argument is
        exemplified::

            sage: G = GraphDatabase()
            sage: q = 'select graph_id,graph6,num_vertices,num_edges from graph_data where graph_id<=(?) and num_vertices=(?)'
            sage: param = (22,5)
            sage: Q = SQLQuery(G, q, param)
            sage: Q.show()
            graph_id             graph6               num_vertices         num_edges
            --------------------------------------------------------------------------------
            18                   D??                  5                    0
            19                   D?C                  5                    1
            20                   D?K                  5                    2
            21                   D@O                  5                    2
            22                   D?[                  5                    3
        """

class GraphQuery(GenericGraphQuery):
    __query_string__: Incomplete
    def __init__(self, graph_db=None, query_dict=None, display_cols=None, immutable: bool = False, **kwds) -> None:
        """
        A query for an instance of :class:`~GraphDatabase`.

        This class nicely wraps the :class:`sage.databases.sql_db.SQLQuery`
        class located in :mod:`sage.databases.sql_db` to make the query
        constraints intuitive and with as many pre-definitions as
        possible. (i.e.: since it has to be a :class:`~GraphDatabase`, we
        already know the table structure and types; and since it is immutable,
        we can treat these as a guarantee).

        .. NOTE::

           :class:`sage.databases.sql_db.SQLQuery` functions are available for
           :class:`~GraphQuery`. See :mod:`sage.databases.sql_db` for more
           details.

        INPUT:

        - ``graph_db`` -- :class:`~GraphDatabase` (default: ``None``); instance
          to apply the query to (If ``None``, then a new instance is created)

        - ``query_dict`` -- dictionary (default: ``None``); a dictionary
          specifying the query itself. Format is: ``{'table_name': 'tblname',
          'display_cols': ['col1', 'col2'], 'expression': [col, operator,
          value]}``. If not ``None``, ``query_dict`` will take precedence over
          all other arguments.

        - ``display_cols`` -- list of strings (default: ``None``); a list of
          column names (strings) to display in the result when running or
          showing a query

        - ``immutable`` -- boolean (default: ``False``); whether to return
          immutable or mutable graphs

        - ``kwds`` -- the columns of the database are all keywords. For a
          database table/column structure dictionary, call
          :func:`~graph_db_info`. Keywords accept both single values and lists
          of length 2. The list allows the user to specify an expression other
          than equality. Valid expressions are strings, and for numeric values
          (i.e. Reals and Integers) are: '=','','','=','='. String values also
          accept 'regexp' as an expression argument. The only keyword exception
          to this format is ``induced_subgraphs``, which accepts one of the
          following options:

          - ``['one_of', String, ..., String]`` -- will search for graphs
            containing a subgraph isomorphic to *any* of the ``graph6`` strings
            in the list

          - ``['all_of', String, ..., String]`` -- will search for graphs
            containing a subgraph isomorphic to *each* of the ``graph6`` strings
            in the list

        EXAMPLES::

            sage: Q = GraphQuery(display_cols=['graph6', 'num_vertices', 'degree_sequence'], num_edges=['<=', 5], min_degree=1)
            sage: Q.number_of()
            35
            sage: Q.show()
            Graph6               Num Vertices         Degree Sequence
            ------------------------------------------------------------
            A_                   2                    [1, 1]
            BW                   3                    [1, 1, 2]
            CF                   4                    [1, 1, 1, 3]
            CK                   4                    [1, 1, 1, 1]
            CL                   4                    [1, 1, 2, 2]
            CN                   4                    [1, 2, 2, 3]
            D?{                  5                    [1, 1, 1, 1, 4]
            D@s                  5                    [1, 1, 1, 2, 3]
            D@{                  5                    [1, 1, 2, 2, 4]
            DBg                  5                    [1, 1, 2, 2, 2]
            DBk                  5                    [1, 1, 2, 3, 3]
            DIk                  5                    [1, 2, 2, 2, 3]
            DK[                  5                    [1, 2, 2, 2, 3]
            D_K                  5                    [1, 1, 1, 1, 2]
            D`K                  5                    [1, 1, 2, 2, 2]
            E?Bw                 6                    [1, 1, 1, 1, 1, 5]
            E?Fg                 6                    [1, 1, 1, 1, 2, 4]
            E?N?                 6                    [1, 1, 1, 1, 2, 2]
            E?NG                 6                    [1, 1, 1, 1, 3, 3]
            E@FG                 6                    [1, 1, 1, 2, 2, 3]
            E@N?                 6                    [1, 1, 2, 2, 2, 2]
            E@Q?                 6                    [1, 1, 1, 1, 1, 1]
            E@QW                 6                    [1, 1, 1, 2, 2, 3]
            E@YO                 6                    [1, 1, 2, 2, 2, 2]
            E_?w                 6                    [1, 1, 1, 1, 1, 3]
            E_Cg                 6                    [1, 1, 1, 1, 2, 2]
            E_Cw                 6                    [1, 1, 1, 2, 2, 3]
            E_Ko                 6                    [1, 1, 2, 2, 2, 2]
            F??^?                7                    [1, 1, 1, 1, 1, 2, 3]
            F?LCG                7                    [1, 1, 1, 1, 2, 2, 2]
            FK??W                7                    [1, 1, 1, 1, 1, 1, 2]
            FK?GW                7                    [1, 1, 1, 1, 2, 2, 2]
            F_?@w                7                    [1, 1, 1, 1, 1, 1, 4]
            F_?Hg                7                    [1, 1, 1, 1, 1, 2, 3]
            F_?XO                7                    [1, 1, 1, 1, 2, 2, 2]

        Check the behavior of parameter ``immutable``::

            sage: Q = GraphQuery(display_cols=['graph6'], num_vertices=3)
            sage: any(g.is_immutable() for g in Q)
            False
            sage: Q = GraphQuery(display_cols=['graph6'], num_vertices=3, immutable=True)
            sage: all(g.is_immutable() for g in Q)
            True
        """
    def query_iterator(self, immutable=None) -> Generator[Incomplete]:
        """
        Return an iterator over the results list of the :class:`~GraphQuery`.

        INPUT:

        - ``immutable`` -- boolean (default: ``None``); whether to create
          mutable/immutable graphs. By default (``immutable=None``), follow the
          behavior of ``self``.

        EXAMPLES::

            sage: Q = GraphQuery(display_cols=['graph6'], num_vertices=7, diameter=5)
            sage: for g in Q:
            ....:     print(g.graph6_string())
            F?`po
            F?gqg
            F@?]O
            F@OKg
            F@R@o
            FA_pW
            FEOhW
            FGC{o
            FIAHo
            sage: Q = GraphQuery(display_cols=['graph6'], num_vertices=7, diameter=5)
            sage: it = iter(Q)
            sage: while True:
            ....:     try: print(next(it).graph6_string())
            ....:     except StopIteration: break
            F?`po
            F?gqg
            F@?]O
            F@OKg
            F@R@o
            FA_pW
            FEOhW
            FGC{o
            FIAHo

        Check the behavior of parameter ``immutable``::

            sage: Q = GraphQuery(display_cols=['graph6'], num_vertices=3)
            sage: any(g.is_immutable() for g in Q.query_iterator())
            False
            sage: all(g.is_immutable() for g in Q.query_iterator(immutable=True))
            True
            sage: Q = GraphQuery(display_cols=['graph6'], num_vertices=3, immutable=True)
            sage: all(g.is_immutable() for g in Q.query_iterator())
            True
            sage: any(g.is_immutable() for g in Q.query_iterator(immutable=False))
            False
        """
    __iter__ = query_iterator
    def show(self, max_field_size: int = 20, with_picture: bool = False) -> None:
        """
        Display the results of a query in table format.

        INPUT:

        - ``max_field_size`` -- integer (default: 20); width of fields in
          command prompt version

        - ``with_picture`` -- boolean (default: ``False``); whether or not to
          display results with a picture of the graph (available only in the
          notebook)

        EXAMPLES::

            sage: G = GraphDatabase()
            sage: Q = GraphQuery(G, display_cols=['graph6','num_vertices','aut_grp_size'], num_vertices=4, aut_grp_size=4)
            sage: Q.show()
            Graph6               Num Vertices         Aut Grp Size
            ------------------------------------------------------------
            C@                   4                    4
            C^                   4                    4

        ::

            sage: R = GraphQuery(G, display_cols=['graph6','num_vertices','degree_sequence'], num_vertices=4)
            sage: R.show()
            Graph6               Num Vertices         Degree Sequence
            ------------------------------------------------------------
            C?                   4                    [0, 0, 0, 0]
            C@                   4                    [0, 0, 1, 1]
            CB                   4                    [0, 1, 1, 2]
            CF                   4                    [1, 1, 1, 3]
            CJ                   4                    [0, 2, 2, 2]
            CK                   4                    [1, 1, 1, 1]
            CL                   4                    [1, 1, 2, 2]
            CN                   4                    [1, 2, 2, 3]
            C]                   4                    [2, 2, 2, 2]
            C^                   4                    [2, 2, 3, 3]
            C~                   4                    [3, 3, 3, 3]

        Show the pictures (in notebook mode only)::

            sage: S = GraphQuery(G, display_cols=['graph6','aut_grp_size'], num_vertices=4)
            sage: S.show(with_picture=True)
            Traceback (most recent call last):
            ...
            NotImplementedError: Cannot display plot on command line.

        Note that pictures can be turned off::

            sage: S.show(with_picture=False)
            Graph6               Aut Grp Size
            ----------------------------------------
            C?                   24
            C@                   4
            CB                   2
            CF                   6
            CJ                   6
            CK                   8
            CL                   2
            CN                   2
            C]                   8
            C^                   4
            C~                   24

        Show your own query (note that the output is not reformatted for
        generic queries)::

            sage: (GenericGraphQuery('select degree_sequence from degrees where max_degree=2 and min_degree >= 1', G)).show()
            degree_sequence
            --------------------
            211
            222
            2211
            2222
            21111
            22211
            22211
            22222
            221111
            221111
            222211
            222211
            222211
            222222
            222222
            2111111
            2221111
            2221111
            2221111
            2222211
            2222211
            2222211
            2222211
            2222222
            2222222
        """
    def get_graphs_list(self, immutable=None):
        """
        Return a list of Sage Graph objects that satisfy the query.

        INPUT:

        - ``immutable`` -- boolean (default: ``None``); whether to create
          mutable/immutable graphs. By default (``immutable=None``), follow the
          behavior of ``self``.

        EXAMPLES::

            sage: Q = GraphQuery(display_cols=['graph6', 'num_vertices', 'degree_sequence'], num_edges=['<=', 5], min_degree=1)
            sage: L = Q.get_graphs_list()
            sage: L[0]
            Graph on 2 vertices
            sage: len(L)
            35

        Check the behavior of parameter ``immutable``::

            sage: Q = GraphQuery(display_cols=['graph6'], num_vertices=3)
            sage: any(g.is_immutable() for g in Q.get_graphs_list())
            False
            sage: all(g.is_immutable() for g in Q.get_graphs_list(immutable=True))
            True
            sage: Q = GraphQuery(display_cols=['graph6'], num_vertices=3, immutable=True)
            sage: all(g.is_immutable() for g in Q.get_graphs_list())
            True
            sage: any(g.is_immutable() for g in Q.get_graphs_list(immutable=False))
            False
        """
    def number_of(self):
        """
        Return the number of graphs in the database that satisfy the query.

        EXAMPLES::

            sage: Q = GraphQuery(display_cols=['graph6', 'num_vertices', 'degree_sequence'] ,num_edges=['<=', 5], min_degree=1)
            sage: Q.number_of()
            35
        """

class GraphDatabase(SQLDatabase):
    def __init__(self) -> None:
        """
        Graph Database.

        This class interfaces with the ``sqlite`` database ``graphs.db``. It is
        an immutable database that inherits from
        :class:`~sage.databases.sql_db.SQLDatabase` (see
        :mod:`sage.databases.sql_db`). The display functions and get_graphs_list
        create their own queries, but it is also possible to query the database
        by constructing either a :class:`~sage.databases.sql_db.SQLQuery`.

        The database contains all unlabeled graphs with 7 or fewer nodes. This
        class will also interface with the optional database package containing
        all unlabeled graphs with 8 or fewer nodes. The database consists of
        five tables. For a full table and column structure, call
        :func:`~graph_db_info`.

        The tables are associated by the unique primary key ``graph_id`` (int).

        To query this database, we create a :class:`~GraphQuery`. This can be
        done directly with the :meth:`~GraphDatabase.query` method or by
        initializing one of:

        - :class:`~GenericGraphQuery` -- allows direct entry of a query string
          and tuple of parameters. This is the route for more advanced users
          that are familiar with SQL

        - :class:`~GraphQuery` -- a wrapper of SQLQuery, a general
          database/query wrapper of SQLite for new users

        REFERENCES:

        - Data provided by Jason Grout (Brigham Young
          University). [Online] Available:
          http://artsci.drake.edu/grout/graphs/

        EXAMPLES::

            sage: G = GraphDatabase()
            sage: G.get_skeleton()
            {'aut_grp': {'aut_grp_size': {'index': True,
               'primary_key': False,
               'sql': 'INTEGER',
               'unique': False},
              'edge_transitive': {'index': True,
               'primary_key': False,
               'sql': 'BOOLEAN',
               'unique': False},
              'graph_id': {'index': False,
               'primary_key': False,
               'sql': 'INTEGER',
               'unique': False},
              'num_fixed_points': {'index': True,
               'primary_key': False,
               'sql': 'INTEGER',
               'unique': False},
              'num_orbits': {'index': True,
               'primary_key': False,
               'sql': 'INTEGER',
               'unique': False},
              'vertex_transitive': {'index': True,
               'primary_key': False,
               'sql': 'BOOLEAN',
               'unique': False}},
             'degrees': {'average_degree': {'index': True,
               'primary_key': False,
               'sql': 'REAL',
               'unique': False},
              'degree_sequence': {'index': False,
               'primary_key': False,
               'sql': 'INTEGER',
               'unique': False},
              'degrees_sd': {'index': True,
               'primary_key': False,
               'sql': 'REAL',
               'unique': False},
              'graph_id': {'index': False,
               'primary_key': False,
               'sql': 'INTEGER',
               'unique': False},
              'max_degree': {'index': True,
               'primary_key': False,
               'sql': 'INTEGER',
               'unique': False},
              'min_degree': {'index': True,
               'primary_key': False,
               'sql': 'INTEGER',
               'unique': False},
              'regular': {'index': True,
               'primary_key': False,
               'sql': 'BOOLEAN',
               'unique': False}},
             'graph_data': {'complement_graph6': {'index': True,
               'primary_key': False,
               'sql': 'TEXT',
               'unique': False},
              'eulerian': {'index': True,
               'primary_key': False,
               'sql': 'BOOLEAN',
               'unique': False},
              'graph6': {'index': True,
               'primary_key': False,
               'sql': 'TEXT',
               'unique': False},
              'graph_id': {'index': True,
               'primary_key': False,
               'sql': 'INTEGER',
               'unique': True},
              'lovasz_number': {'index': True,
               'primary_key': False,
               'sql': 'REAL',
               'unique': False},
              'num_cycles': {'index': True,
               'primary_key': False,
               'sql': 'INTEGER',
               'unique': False},
              'num_edges': {'index': True,
               'primary_key': False,
               'sql': 'INTEGER',
               'unique': False},
              'num_hamiltonian_cycles': {'index': True,
               'primary_key': False,
               'sql': 'INTEGER',
               'unique': False},
              'num_vertices': {'index': True,
               'primary_key': False,
               'sql': 'INTEGER',
               'unique': False},
              'perfect': {'index': True,
               'primary_key': False,
               'sql': 'BOOLEAN',
               'unique': False},
              'planar': {'index': True,
               'primary_key': False,
               'sql': 'BOOLEAN',
               'unique': False}},
             'misc': {'clique_number': {'index': True,
               'primary_key': False,
               'sql': 'INTEGER',
               'unique': False},
              'diameter': {'index': True,
               'primary_key': False,
               'sql': 'INTEGER',
               'unique': False},
              'edge_connectivity': {'index': True,
               'primary_key': False,
               'sql': 'BOOLEAN',
               'unique': False},
              'girth': {'index': True,
               'primary_key': False,
               'sql': 'INTEGER',
               'unique': False},
              'graph_id': {'index': False,
               'primary_key': False,
               'sql': 'INTEGER',
               'unique': False},
              'independence_number': {'index': True,
               'primary_key': False,
               'sql': 'INTEGER',
               'unique': False},
              'induced_subgraphs': {'index': True,
               'primary_key': False,
               'sql': 'TEXT',
               'unique': False},
              'min_vertex_cover_size': {'index': True,
               'primary_key': False,
               'sql': 'INTEGER',
               'unique': False},
              'num_components': {'index': True,
               'primary_key': False,
               'sql': 'INTEGER',
               'unique': False},
              'num_cut_vertices': {'index': True,
               'primary_key': False,
               'sql': 'INTEGER',
               'unique': False},
              'num_spanning_trees': {'index': True,
               'primary_key': False,
               'sql': 'INTEGER',
               'unique': False},
              'radius': {'index': True,
               'primary_key': False,
               'sql': 'INTEGER',
               'unique': False},
              'vertex_connectivity': {'index': True,
               'primary_key': False,
               'sql': 'BOOLEAN',
               'unique': False}},
             'spectrum': {'eigenvalues_sd': {'index': True,
               'primary_key': False,
               'sql': 'REAL',
               'unique': False},
              'energy': {'index': True,
               'primary_key': False,
               'sql': 'REAL',
               'unique': False},
              'graph_id': {'index': False,
               'primary_key': False,
               'sql': 'INTEGER',
               'unique': False},
              'max_eigenvalue': {'index': True,
               'primary_key': False,
               'sql': 'REAL',
               'unique': False},
              'min_eigenvalue': {'index': True,
               'primary_key': False,
               'sql': 'REAL',
               'unique': False},
              'spectrum': {'index': False,
               'primary_key': False,
               'sql': 'TEXT',
               'unique': False}}}
        """
    def query(self, query_dict=None, display_cols=None, **kwds):
        """
        Create a GraphQuery on this database.

        For full class details, type ``GraphQuery?``
        and press :kbd:`Shift` + :kbd:`Enter`.

        EXAMPLES::

            sage: D = GraphDatabase()
            sage: q = D.query(display_cols=['graph6', 'num_vertices', 'degree_sequence'], num_edges=['<=', 5])          # needs sage.symbolic
            sage: q.show()                                                              # needs sage.symbolic
            Graph6               Num Vertices         Degree Sequence
            ------------------------------------------------------------
            @                    1                    [0]
            A?                   2                    [0, 0]
            A_                   2                    [1, 1]
            B?                   3                    [0, 0, 0]
            BG                   3                    [0, 1, 1]
            BW                   3                    [1, 1, 2]
            Bw                   3                    [2, 2, 2]
            C?                   4                    [0, 0, 0, 0]
            C@                   4                    [0, 0, 1, 1]
            CB                   4                    [0, 1, 1, 2]
            CF                   4                    [1, 1, 1, 3]
            CJ                   4                    [0, 2, 2, 2]
            CK                   4                    [1, 1, 1, 1]
            CL                   4                    [1, 1, 2, 2]
            CN                   4                    [1, 2, 2, 3]
            C]                   4                    [2, 2, 2, 2]
            C^                   4                    [2, 2, 3, 3]
            D??                  5                    [0, 0, 0, 0, 0]
            D?C                  5                    [0, 0, 0, 1, 1]
            D?K                  5                    [0, 0, 1, 1, 2]
            D?[                  5                    [0, 1, 1, 1, 3]
            D?{                  5                    [1, 1, 1, 1, 4]
            D@K                  5                    [0, 0, 2, 2, 2]
            D@O                  5                    [0, 1, 1, 1, 1]
            D@S                  5                    [0, 1, 1, 2, 2]
            D@[                  5                    [0, 1, 2, 2, 3]
            D@s                  5                    [1, 1, 1, 2, 3]
            D@{                  5                    [1, 1, 2, 2, 4]
            DBW                  5                    [0, 2, 2, 2, 2]
            DB[                  5                    [0, 2, 2, 3, 3]
            DBg                  5                    [1, 1, 2, 2, 2]
            DBk                  5                    [1, 1, 2, 3, 3]
            DIk                  5                    [1, 2, 2, 2, 3]
            DK[                  5                    [1, 2, 2, 2, 3]
            DLo                  5                    [2, 2, 2, 2, 2]
            D_K                  5                    [1, 1, 1, 1, 2]
            D`K                  5                    [1, 1, 2, 2, 2]
            E???                 6                    [0, 0, 0, 0, 0, 0]
            E??G                 6                    [0, 0, 0, 0, 1, 1]
            E??W                 6                    [0, 0, 0, 1, 1, 2]
            E??w                 6                    [0, 0, 1, 1, 1, 3]
            E?@w                 6                    [0, 1, 1, 1, 1, 4]
            E?Bw                 6                    [1, 1, 1, 1, 1, 5]
            E?CW                 6                    [0, 0, 0, 2, 2, 2]
            E?C_                 6                    [0, 0, 1, 1, 1, 1]
            E?Cg                 6                    [0, 0, 1, 1, 2, 2]
            E?Cw                 6                    [0, 0, 1, 2, 2, 3]
            E?Dg                 6                    [0, 1, 1, 1, 2, 3]
            E?Dw                 6                    [0, 1, 1, 2, 2, 4]
            E?Fg                 6                    [1, 1, 1, 1, 2, 4]
            E?Ko                 6                    [0, 0, 2, 2, 2, 2]
            E?Kw                 6                    [0, 0, 2, 2, 3, 3]
            E?LO                 6                    [0, 1, 1, 2, 2, 2]
            E?LW                 6                    [0, 1, 1, 2, 3, 3]
            E?N?                 6                    [1, 1, 1, 1, 2, 2]
            E?NG                 6                    [1, 1, 1, 1, 3, 3]
            E@FG                 6                    [1, 1, 1, 2, 2, 3]
            E@HW                 6                    [0, 1, 2, 2, 2, 3]
            E@N?                 6                    [1, 1, 2, 2, 2, 2]
            E@Ow                 6                    [0, 1, 2, 2, 2, 3]
            E@Q?                 6                    [1, 1, 1, 1, 1, 1]
            E@QW                 6                    [1, 1, 1, 2, 2, 3]
            E@T_                 6                    [0, 2, 2, 2, 2, 2]
            E@YO                 6                    [1, 1, 2, 2, 2, 2]
            EG?W                 6                    [0, 1, 1, 1, 1, 2]
            EGCW                 6                    [0, 1, 1, 2, 2, 2]
            E_?w                 6                    [1, 1, 1, 1, 1, 3]
            E_Cg                 6                    [1, 1, 1, 1, 2, 2]
            E_Cw                 6                    [1, 1, 1, 2, 2, 3]
            E_Ko                 6                    [1, 1, 2, 2, 2, 2]
            F????                7                    [0, 0, 0, 0, 0, 0, 0]
            F???G                7                    [0, 0, 0, 0, 0, 1, 1]
            F???W                7                    [0, 0, 0, 0, 1, 1, 2]
            F???w                7                    [0, 0, 0, 1, 1, 1, 3]
            F??@w                7                    [0, 0, 1, 1, 1, 1, 4]
            F??Bw                7                    [0, 1, 1, 1, 1, 1, 5]
            F??GW                7                    [0, 0, 0, 0, 2, 2, 2]
            F??G_                7                    [0, 0, 0, 1, 1, 1, 1]
            F??Gg                7                    [0, 0, 0, 1, 1, 2, 2]
            F??Gw                7                    [0, 0, 0, 1, 2, 2, 3]
            F??Hg                7                    [0, 0, 1, 1, 1, 2, 3]
            F??Hw                7                    [0, 0, 1, 1, 2, 2, 4]
            F??Jg                7                    [0, 1, 1, 1, 1, 2, 4]
            F??Wo                7                    [0, 0, 0, 2, 2, 2, 2]
            F??Ww                7                    [0, 0, 0, 2, 2, 3, 3]
            F??XO                7                    [0, 0, 1, 1, 2, 2, 2]
            F??XW                7                    [0, 0, 1, 1, 2, 3, 3]
            F??Z?                7                    [0, 1, 1, 1, 1, 2, 2]
            F??ZG                7                    [0, 1, 1, 1, 1, 3, 3]
            F??^?                7                    [1, 1, 1, 1, 1, 2, 3]
            F?CJG                7                    [0, 1, 1, 1, 2, 2, 3]
            F?CPW                7                    [0, 0, 1, 2, 2, 2, 3]
            F?CZ?                7                    [0, 1, 1, 2, 2, 2, 2]
            F?C_w                7                    [0, 0, 1, 2, 2, 2, 3]
            F?Ca?                7                    [0, 1, 1, 1, 1, 1, 1]
            F?CaW                7                    [0, 1, 1, 1, 2, 2, 3]
            F?Ch_                7                    [0, 0, 2, 2, 2, 2, 2]
            F?CqO                7                    [0, 1, 1, 2, 2, 2, 2]
            F?LCG                7                    [1, 1, 1, 1, 2, 2, 2]
            F@??W                7                    [0, 0, 1, 1, 1, 1, 2]
            F@?GW                7                    [0, 0, 1, 1, 2, 2, 2]
            FG??w                7                    [0, 1, 1, 1, 1, 1, 3]
            FG?Gg                7                    [0, 1, 1, 1, 1, 2, 2]
            FG?Gw                7                    [0, 1, 1, 1, 2, 2, 3]
            FG?Wo                7                    [0, 1, 1, 2, 2, 2, 2]
            FK??W                7                    [1, 1, 1, 1, 1, 1, 2]
            FK?GW                7                    [1, 1, 1, 1, 2, 2, 2]
            F_?@w                7                    [1, 1, 1, 1, 1, 1, 4]
            F_?Hg                7                    [1, 1, 1, 1, 1, 2, 3]
            F_?XO                7                    [1, 1, 1, 1, 2, 2, 2]
        """
    def interactive_query(self, display_cols, **kwds) -> None:
        """
        Generate an interact shell to query the database.

        .. WARNING::

            This is no longer implemented since the switch to Python3.

        This method generates an interact shell that allows the user
        to manipulate query parameters and see the updated results.

        .. TODO::

            This function could use improvement. Add full options of typical
            :class:`~GraphQuery` (i.e.: have it accept list input); and update
            options in interact to make it less annoying to put in operators.

        EXAMPLES::

            sage: D = GraphDatabase()
            sage: D.interactive_query(display_cols=['graph6', 'num_vertices', 'degree_sequence'], num_edges=5, max_degree=3)                                    # needs sage.symbolic
            Traceback (most recent call last):
            ...
            NotImplementedError: not available in Jupyter notebook
        """
