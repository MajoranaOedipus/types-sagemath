from _typeshed import Incomplete
from sage.misc.temporary_file import tmp_filename as tmp_filename
from sage.structure.sage_object import SageObject as SageObject

sqlite_keywords: Incomplete

def regexp(expr, item):
    """
    Function to define regular expressions in pysqlite.

    OUTPUT:

    - ``True`` if parameter ``item`` matches the regular expression
      parameter ``expr``
    - ``False`` otherwise (i.e.: no match)

    REFERENCES:

    - [Ha2005]_

    EXAMPLES::

        sage: from sage.databases.sql_db import regexp
        sage: regexp('.s.*','cs')
        True
        sage: regexp('.s.*','ccs')
        False
        sage: regexp('.s.*','cscccc')
        True
    """
def verify_type(type):
    """
    Verify that the specified ``type`` is one of the allowed strings.

    EXAMPLES::

        sage: from sage.databases.sql_db import verify_type
        sage: verify_type('INT')
        True
        sage: verify_type('int')
        True
        sage: verify_type('float')
        Traceback (most recent call last):
        ...
        TypeError: float is not a legal type.
    """
def verify_column(col_dict):
    """
    Verify that ``col_dict`` is in proper format, and return a dict with
    default values filled in. Proper format::

        {'primary_key':False, 'index':False, 'unique': False, 'sql':'REAL'}

    EXAMPLES::

        sage: from sage.databases.sql_db import verify_column
        sage: col = {'sql':'BOOLEAN'}
        sage: verify_column(col)
        {'index': False, 'primary_key': False, 'sql': 'BOOLEAN', 'unique': False}
        sage: col = {'primary_key':True, 'sql':'INTEGER'}
        sage: verify_column(col)
        {'index': True, 'primary_key': True, 'sql': 'INTEGER', 'unique': True}
        sage: verify_column({})
        Traceback (most recent call last):
        ...
        ValueError: SQL type must be declared, e.g. {'sql':'REAL'}.
    """
def verify_operator(operator):
    """
    Check that ``operator`` is one of the allowed strings.
    Legal operators include the following strings:

    - '='
    - '<='
    - '>='
    - '<'
    - '>'
    - '<>'
    - 'like'
    - 'regexp'
    - 'is null'
    - 'is not null'

    EXAMPLES::

        sage: from sage.databases.sql_db import verify_operator
        sage: verify_operator('<=')
        True
        sage: verify_operator('regexp')
        True
        sage: verify_operator('is null')
        True
        sage: verify_operator('not_an_operator')
        Traceback (most recent call last):
        ...
        TypeError: not_an_operator is not a legal operator.
    """
def construct_skeleton(database):
    """
    Construct a database skeleton from the sql data.  The skeleton data
    structure is a triple indexed dictionary of the following format::

        | - skeleton -- a triple-indexed dictionary
        |   - outer key -- table name
        |     - inner key -- column name
        |       - inner inner key -- one of the following:
        |         - ``primary_key`` -- boolean, whether column has been set as
                    primary key
        |         - ``index`` -- boolean, whether column has been set as index
        |         - ``unique`` -- boolean, whether column has been set as unique
        |         - ``sql`` -- one of ``'TEXT'``, ``'BOOLEAN'``, ``'INTEGER'``,
                    ``'REAL'``, or other user defined type

    An example skeleton of a database with one table, that table with one
    column::

        {'table1':{'col1':{'primary_key':False, 'unique': True, 'index':True, 'sql':'REAL'}}}

    EXAMPLES::

        sage: G = SQLDatabase(GraphDatabase().__dblocation__, False)
        sage: from sage.databases.sql_db import construct_skeleton
        sage: sorted(construct_skeleton(G))
        ['aut_grp', 'degrees', 'graph_data', 'misc', 'spectrum']
    """

p: int

class SQLQuery(SageObject):
    __database__: Incomplete
    __query_string__: str
    __param_tuple__: Incomplete
    __query_dict__: Incomplete
    def __init__(self, database, *args, **kwds) -> None:
        '''
        A query for a SQLite database.

        INPUT:

        - ``database`` -- a SQLDatabase object
        - ``query_dict`` -- dictionary specifying the query itself. The
          format is::

              {\'table_name\':\'tblname\', \'display_cols\':[\'col1\', \'col2\',\'col3\'], \'expression\': [col, operator, value]}

        NOTE:
            Every SQL type we are using is ultimately represented as a string,
            so if you wish to save actual strings to a database, you actually
            need to do something like: \'"value"\'.

        See the documentation of ``SQLDatabase`` for an introduction to using
        SQLite in Sage.

        EXAMPLES::

            sage: D = SQLDatabase()
            sage: D.create_table(\'simon\',{\'a1\':{\'sql\':\'bool\', \'primary_key\':False}, \'b2\':{\'sql\':\'int\'}})
            sage: D.add_data(\'simon\',[(0,0),(1,2),(2,4)])
            sage: r = SQLQuery(D, {\'table_name\':\'simon\', \'display_cols\':[\'a1\'], \'expression\':[\'b2\',\'<=\', 3]})
            sage: r.show()
            a1
            --------------------
            0
            1

        Test that :issue:`27562` is fixed::

            sage: D = SQLDatabase()
            sage: r = SQLQuery(D, {\'table_name\':\'simon\', \'display_cols\':[\'a1\'], \'expression\':[\'b2\',\'<=\', 3]})
            Traceback (most recent call last):
            ...
            ValueError: Database has no table simon
            sage: D.create_table(\'simon\',{\'a1\':{\'sql\':\'bool\', \'primary_key\':False}, \'b2\':{\'sql\':\'int\'}})
            sage: D.create_table(\'simon\',{\'a1\':{\'sql\':\'bool\', \'primary_key\':False}, \'b2\':{\'sql\':\'int\'}})
            Traceback (most recent call last):
            ...
            ValueError: Database already has a table named simon
            sage: SQLQuery(D, {\'table_name\':\'simon\', \'display_cols\':[\'a1\'], \'expression\':[\'c1\',\'>\',2]})
            Traceback (most recent call last):
                ...
            ValueError: Table has no column c1
        '''
    def get_query_string(self):
        """
        Return a copy of the query string.

        EXAMPLES::

            sage: G = GraphDatabase()
            sage: q = 'SELECT graph_id,graph6,num_vertices,num_edges FROM graph_data WHERE graph_id<=(?) AND num_vertices=(?)'
            sage: param = (22,5)
            sage: SQLQuery(G,q,param).get_query_string()
            'SELECT graph_id,graph6,num_vertices,num_edges FROM graph_data
            WHERE graph_id<=(?) AND num_vertices=(?)'
            sage: r = 'SELECT graph6 FROM graph_data WHERE num_vertices<=3'
            sage: SQLQuery(G,r).get_query_string()
            'SELECT graph6 FROM graph_data WHERE num_vertices<=3'
        """
    def __iter__(self):
        """
        Return an iterator over the results of the query.

        EXAMPLES::

            sage: G = GraphDatabase()
            sage: q = 'SELECT graph_id,graph6 FROM graph_data WHERE num_vertices=(?)'
            sage: param = (5,)
            sage: Q = SQLQuery(G,q,param)
            sage: it = Q.__iter__()
            sage: next(it)
            (18, 'D??')
            sage: next(it)
            (19, 'D?C')
            sage: skip = [next(it) for _ in range(15)]
            sage: next(it)
            (35, 'DBk')
        """
    def query_results(self):
        """
        Run the query by executing the ``__query_string__``. Return the
        results of the query in a list.

        EXAMPLES::

            sage: G = GraphDatabase()
            sage: q = 'SELECT graph_id,graph6,num_vertices,num_edges FROM graph_data WHERE graph_id<=(?) AND num_vertices=(?)'
            sage: param = (22,5)
            sage: Q = SQLQuery(G,q,param)
            sage: Q.query_results()
            [(18, 'D??', 5, 0), (19, 'D?C', 5, 1), (20, 'D?K', 5, 2),
             (21, 'D@O', 5, 2), (22, 'D?[', 5, 3)]
            sage: R = SQLQuery(G,{'table_name':'graph_data', 'display_cols':['graph6'], 'expression':['num_vertices','=',4]})
            sage: R.query_results()
            [('C?',), ('C@',), ('CB',), ('CK',), ('CF',), ('CJ',),
             ('CL',), ('CN',), ('C]',), ('C^',), ('C~',)]
        """
    def show(self, **kwds):
        """
        Display the result of the query in table format.

        KEYWORDS:

        - ``max_field_size`` -- how wide each field can be
        - ``format_cols`` -- dictionary that allows the user to specify the
          format of a column's output by supplying a function. The format of
          the dictionary is::

              {'column_name':(lambda x: format_function(x))}

        - ``plot_cols`` -- dictionary that allows the user to specify that a
          plot should be drawn by the object generated by a data slice. Note
          that plot kwds are permitted. The dictionary format is::

              {'column_name':((lambda x: plot_function(x)), **kwds)}

        - ``relabel_cols`` -- dictionary to specify a relabeling of column
          headers. The dictionary format is::

              {'table_name':{'old_col_name':'new_col_name'}}

        - ``id_col`` -- reference to a column that can be used as an object
          identifier for each row

        EXAMPLES::

            sage: DB = SQLDatabase()
            sage: DB.create_table('simon',{'a1':{'sql':'bool', 'primary_key':False}, 'b2':{'sql':'int'}})
            sage: DB.add_data('simon',[(0,0),(1,1),(1,2)])
            sage: r = SQLQuery(DB, {'table_name':'simon', 'display_cols':['a1'], 'expression':['b2','<=', 6]})
            sage: r.show()
            a1
            --------------------
            0
            1
            1
            sage: D = GraphDatabase()
            sage: from sage.graphs.graph_database import valid_kwds, data_to_degseq
            sage: relabel = {}
            sage: for col in valid_kwds:
            ....:     relabel[col] = ' '.join([word.capitalize() for word in col.split('_')])
            sage: q = GraphQuery(display_cols=['graph6','degree_sequence'], num_vertices=4)
            sage: SQLQuery.show(q, format_cols={'degree_sequence':(lambda x,y: data_to_degseq(x,y))}, relabel_cols=relabel, id_col='graph6')
            Graph6               Degree Sequence
            ----------------------------------------
            C?                   [0, 0, 0, 0]
            C@                   [0, 0, 1, 1]
            CB                   [0, 1, 1, 2]
            CF                   [1, 1, 1, 3]
            CJ                   [0, 2, 2, 2]
            CK                   [1, 1, 1, 1]
            CL                   [1, 1, 2, 2]
            CN                   [1, 2, 2, 3]
            C]                   [2, 2, 2, 2]
            C^                   [2, 2, 3, 3]
            C~                   [3, 3, 3, 3]
        """
    def __copy__(self):
        """
        Return a copy of itself.

        EXAMPLES::

            sage: G = GraphDatabase()
            sage: Q = SQLQuery(G, {'table_name':'graph_data', 'display_cols':['graph_id','graph6','num_vertices'], 'expression':['num_edges','<',3]})
            sage: R = copy(Q)
            sage: R.__query_string__ = ''
            sage: Q.__query_string__ == ''
            False
        """
    def intersect(self, other, join_table=None, join_dict=None, in_place: bool = False):
        """
        Return a new ``SQLQuery`` that is the intersection of ``self`` and
        ``other``. ``join_table`` and ``join_dict`` can be ``None`` iff the
        two queries only search one table in the database. All display columns
        will be concatenated in order: ``self`` display cols + other display cols.

        INPUT:

        - ``other`` -- the ``SQLQuery`` to intersect with
        - ``join_table`` -- base table to join on (This table should have at
          least one column in each table to join on).
        - ``join_dict`` -- dictionary that represents the join structure for
          the new query. (Must include a mapping for all tables, including
          those previously joined in either query). Structure is given by::

              {'join_table1':('corr_base_col1', 'col1'), 'join_table2':('corr_base_col2', 'col2')}

          where ``join_table1`` is to be joined with ``join_table`` on
          ``join_table.corr_base_col1 = join_table1.col1``

        EXAMPLES::

            sage: DB = SQLDatabase()
            sage: DB.create_table('simon',{'a1':{'sql':'bool'}, 'b2':{'sql':'int'}})
            sage: DB.create_table('lucy',{'a1':{'sql':'bool'}, 'b2':{'sql':'int'}})
            sage: DB.add_data('simon', [(0,5),(1,4)])
            sage: DB.add_data('lucy', [(1,1),(1,4)])
            sage: q = SQLQuery(DB, {'table_name':'lucy', 'display_cols':['b2'], 'expression':['a1','=',1]})
            sage: r = SQLQuery(DB, {'table_name':'simon', 'display_cols':['a1'], 'expression':['b2','<=', 6]})
            sage: s = q.intersect(r, 'simon', {'lucy':('a1','a1')})
            sage: s.get_query_string()
            'SELECT lucy.b2,simon.a1 FROM simon INNER JOIN lucy ON
            simon.a1=lucy.a1 WHERE ( lucy.a1 = ? ) AND ( simon.b2 <= ? )'
            sage: s.query_results()
            [(1, 1), (4, 1)]
            sage: s = q.intersect(r)
            Traceback (most recent call last):
            ...
            ValueError: Input queries query different tables but join
                parameters are NoneType
            sage: s.__query_string__ == q.__query_string__
            False
            sage: q.intersect(r, 'simon', {'lucy':('a1','a1')}, True)
            sage: q.__query_string__ == s.__query_string__
            True
        """
    def union(self, other, join_table=None, join_dict=None, in_place: bool = False):
        """
        Return a new ``SQLQuery`` that is the union of ``self`` and ``other``.
        ``join_table`` and ``join_dict`` can be ``None`` iff the two queries
        only search one table in the database. All display columns will be
        concatenated in order: ``self`` display cols + other display cols.

        INPUT:

        - ``other`` -- the ``SQLQuery`` to union with
        - ``join_table`` -- base table to join on (This table should have at
          least one column in each table to join on).
        - ``join_dict`` -- dictionary that represents the join structure for
          the new query. (Must include a mapping for all tables, including
          those previously joined in either query). Structure is given by::

              {'join_table1':('corr_base_col1', 'col1'), 'join_table2':('corr_base_col2', 'col2')}

          where ``join_table1`` is to be joined with ``join_table`` on
          ``join_table.corr_base_col1=join_table1.col1``

        EXAMPLES::

            sage: DB = SQLDatabase()
            sage: DB.create_table('simon',{'a1':{'sql':'bool'}, 'b2':{'sql':'int'}})
            sage: DB.create_table('lucy',{'a1':{'sql':'bool'}, 'b2':{'sql':'int'}})
            sage: DB.add_data('simon', [(0,5),(1,4)])
            sage: DB.add_data('lucy', [(1,1),(1,4)])
            sage: q = SQLQuery(DB, {'table_name':'lucy', 'display_cols':['b2'], 'expression':['a1','=',1]})
            sage: r = SQLQuery(DB, {'table_name':'simon', 'display_cols':['a1'], 'expression':['b2','<=', 6]})
            sage: s = q.union(r, 'simon', {'lucy':('a1','a1')})
            sage: s.get_query_string()
            'SELECT lucy.b2,simon.a1 FROM simon INNER JOIN lucy ON
            simon.a1=lucy.a1 WHERE ( lucy.a1 = ? ) OR ( simon.b2 <= ? )'
            sage: s.query_results()
            [(1, 1), (4, 1)]
        """

class SQLDatabase(SageObject):
    __read_only__: Incomplete
    ignore_warnings: bool
    __dblocation__: Incomplete
    __connection__: Incomplete
    __skeleton__: Incomplete
    def __init__(self, filename=None, read_only=None, skeleton=None) -> None:
        """
        A SQL Database object corresponding to a database file.

        INPUT:

        - ``filename`` -- string
        - ``skeleton`` -- a triple-indexed dictionary::

            | - outer key -- table name
            |   - inner key -- column name
            |     - inner inner key -- one of the following:
            |       - ``primary_key`` -- boolean, whether column has been set
                      as primary key
            |       - ``index`` -- boolean, whether column has been set as
                      index
            |       - ``unique`` -- boolean, whether column has been set as
                      unique
            |       - ``sql`` -- one of ``'TEXT'``, ``'BOOLEAN'``,
                      ``'INTEGER'``, ``'REAL'``, or other user defined type

        TUTORIAL:

        The ``SQLDatabase`` class is for interactively building databases
        intended for queries. This may sound redundant, but it is important. If
        you want a database intended for quick lookup of entries in very large
        tables, much like a hash table (such as a Python dictionary), a
        ``SQLDatabase`` may not be what you are looking for. The strength of
        ``SQLDatabases`` is in queries, searches through the database with
        complicated criteria.

        For example, we create a new database for storing isomorphism classes
        of simple graphs::

            sage: D = SQLDatabase()

        In order to generate representatives for the classes, we will import a
        function which generates all labeled graphs (noting that this is not
        the optimal way)::

            sage: from sage.groups.perm_gps.partn_ref.refinement_graphs import all_labeled_graphs

        We will need a table in the database in which to store the graphs, and
        we specify its structure with a Python dictionary, each of whose keys
        is the name of a column::

            sage: from collections import OrderedDict
            sage: table_skeleton = OrderedDict([
            ....: ('graph6',{'sql':'TEXT', 'index':True, 'primary_key':True}),
            ....: ('vertices', {'sql':'INTEGER'}),
            ....: ('edges', {'sql':'INTEGER'})
            ....: ])

        Then we create the table::

            sage: D.create_table('simon', table_skeleton)
            sage: D.show('simon')
            graph6               vertices             edges
            ------------------------------------------------------------

        Now that we have the table, we will begin to populate the table with
        rows. First, add the graph on zero vertices.::

            sage: G = Graph()
            sage: D.add_row('simon',(G.graph6_string(), 0, 0))
            sage: D.show('simon')
            graph6               vertices             edges
            ------------------------------------------------------------
            ?                    0                    0

        Next, add the graph on one vertex.::

            sage: G.add_vertex()
            0
            sage: D.add_row('simon',(G.graph6_string(), 1, 0))
            sage: D.show('simon')
            graph6               vertices             edges
            ------------------------------------------------------------
            ?                    0                    0
            @                    1                    0

        Say we want a database of graphs on four or less vertices::

            sage: labels = {}
            sage: for i in range(2, 5):
            ....:     labels[i] = []
            ....:     for g in all_labeled_graphs(i):
            ....:         g = g.canonical_label(algorithm='sage')
            ....:         if g not in labels[i]:
            ....:             labels[i].append(g)
            ....:             D.add_row('simon', (g.graph6_string(), g.order(), g.size()))
            sage: D.show('simon')
            graph6               vertices             edges
            ------------------------------------------------------------
            ?                    0                    0
            @                    1                    0
            A?                   2                    0
            A_                   2                    1
            B?                   3                    0
            BG                   3                    1
            BW                   3                    2
            Bw                   3                    3
            C?                   4                    0
            C@                   4                    1
            CB                   4                    2
            CF                   4                    3
            CJ                   4                    3
            CK                   4                    2
            CL                   4                    3
            CN                   4                    4
            C]                   4                    4
            C^                   4                    5
            C~                   4                    6

        We can then query the database -- let's ask for all the graphs on four
        vertices with three edges. We do so by creating two queries and asking
        for rows that satisfy them both::

            sage: Q = SQLQuery(D, {'table_name':'simon', 'display_cols':['graph6'], 'expression':['vertices','=',4]})
            sage: Q2 = SQLQuery(D, {'table_name':'simon', 'display_cols':['graph6'], 'expression':['edges','=',3]})
            sage: Q = Q.intersect(Q2)
            sage: len(Q.query_results())
            3
            sage: Q.query_results() # random
            [('CF', 'CF'), ('CJ', 'CJ'), ('CL', 'CL')]

        NOTE: The values of ``display_cols`` are always concatenated in
        intersections and unions.

        Of course, we can save the database to file. Here we use a
        temporary directory that we clean up afterwards::

            sage: import tempfile
            sage: d = tempfile.TemporaryDirectory()
            sage: dbpath = os.path.join(d.name, 'simon.db')
            sage: D.save(dbpath)

        Now the database's hard link is to this file, and not the temporary db
        file. For example, let's say we open the same file with another class
        instance. We can load the file as an immutable database::

            sage: E = SQLDatabase(dbpath)
            sage: E.show('simon')
            graph6               vertices             edges
            ------------------------------------------------------------
            ?                    0                    0
            @                    1                    0
            A?                   2                    0
            A_                   2                    1
            B?                   3                    0
            BG                   3                    1
            BW                   3                    2
            Bw                   3                    3
            C?                   4                    0
            C@                   4                    1
            CB                   4                    2
            CF                   4                    3
            CJ                   4                    3
            CK                   4                    2
            CL                   4                    3
            CN                   4                    4
            C]                   4                    4
            C^                   4                    5
            C~                   4                    6
            sage: E.drop_table('simon')
            Traceback (most recent call last):
            ...
            RuntimeError: Cannot drop tables from a read only database.

        Call ``cleanup()`` on the temporary directory to, well, clean it up::

            sage: d.cleanup()
        """
    def __copy__(self):
        """
        Return an instance of ``SQLDatabase`` that points to a copy database,
        and allows modification.

        EXAMPLES::

            sage: from collections import OrderedDict
            sage: DB = SQLDatabase()
            sage: DB.create_table('lucy', OrderedDict([
            ....: ('id', {'sql':'INTEGER', 'primary_key':True, 'index':True}),
            ....: ('a1', {'sql':'bool'}),
            ....: ('b2', {'sql':'int', 'primary_key':False})
            ....: ]))
            sage: DB.add_rows('lucy', [(0,1,1),(1,1,4),(2,0,7),(3,1,384), (4,1,978932)],['id','a1','b2'])
            sage: d = copy(DB)
            sage: d == DB
            False
            sage: d.show('lucy')
            id                   a1                   b2
            ------------------------------------------------------------
            0                    1                    1
            1                    1                    4
            2                    0                    7
            3                    1                    384
            4                    1                    978932
            sage: DB.show('lucy')
            id                   a1                   b2
            ------------------------------------------------------------
            0                    1                    1
            1                    1                    4
            2                    0                    7
            3                    1                    384
            4                    1                    978932
        """
    def save(self, filename) -> None:
        '''
        Save the database to the specified location.

        EXAMPLES::

            sage: MonicPolys = SQLDatabase()
            sage: MonicPolys.create_table(\'simon\', {\'n\':{\'sql\':\'INTEGER\', \'index\':True}})
            sage: for n in range(20): MonicPolys.add_row(\'simon\', (n,))
            sage: import tempfile
            sage: with tempfile.TemporaryDirectory() as d:
            ....:     dbpath = os.path.join(d, "sage.db")
            ....:     MonicPolys.save(dbpath)
            ....:     N = SQLDatabase(dbpath)
            ....:     N.show(\'simon\')
            n
            --------------------
            0
            1
            2
            3
            4
            5
            6
            7
            8
            9
            10
            11
            12
            13
            14
            15
            16
            17
            18
            19
        '''
    def get_skeleton(self, check: bool = False):
        """
        Return a dictionary representing the hierarchical structure of the
        database, in the following format::

            | - skeleton -- a triple-indexed dictionary
            |   - outer key -- table name
            |     - inner key -- column name
            |       - inner inner key -- one of the following:
            |         - ``primary_key`` -- boolean, whether column has been set as
                        primary key
            |         - ``index`` -- boolean, whether column has been set as index
            |         - ``unique`` -- boolean, whether column has been set as unique
            |         - ``sql`` -- one of ``'TEXT'``, ``'BOOLEAN'``, ``'INTEGER'``,
                        ``'REAL'``, or other user defined type

        For example::

            {'table1':{'col1':{'primary_key':False, 'index':True, 'unique': False,'sql':'REAL'}}}

        INPUT:

        - ``check`` -- if ``True``, checks to make sure the database's actual
          structure matches the skeleton on record

        EXAMPLES::

            sage: GDB = GraphDatabase()
            sage: GDB.get_skeleton()             # slightly random output
            {'aut_grp': {'aut_grp_size': {'index': True,
                                           'unique': False,
                                           'primary_key': False,
                                           'sql': 'INTEGER'},
                         ...
                         'num_vertices': {'index': True,
                                          'unique': False,
                                          'primary_key': False,
                                          'sql': 'INTEGER'}}}
        """
    def query(self, *args, **kwds):
        """
        Create a ``SQLQuery`` on this database.

        For full class details,
        type ``SQLQuery?`` and press :kbd:`Shift` + :kbd:`Enter`.

        EXAMPLES::

            sage: D = SQLDatabase()
            sage: D.create_table('simon', {'wolf':{'sql':'BOOLEAN'}, 'tag':{'sql':'INTEGER'}})
            sage: q = D.query({'table_name':'simon', 'display_cols':['tag'], 'expression':['wolf','=',1]})
            sage: q.get_query_string()
            'SELECT simon.tag FROM simon WHERE simon.wolf = ?'
            sage: q.__param_tuple__
            ('1',)
            sage: q = D.query(query_string='SELECT tag FROM simon WHERE wolf=?',param_tuple=(1,))
            sage: q.get_query_string()
            'SELECT tag FROM simon WHERE wolf=?'
            sage: q.__param_tuple__
            ('1',)
        """
    __call__ = query
    def show(self, table_name, **kwds) -> None:
        """
        Show an entire table from the database.

        EXAMPLES::

            sage: DB = SQLDatabase()
            sage: DB.create_table('simon',{'a1':{'sql':'bool'}, 'b2':{'sql':'int'}})
            sage: DB.add_data('simon',[(0,0),(1,1),(1,2)])
            sage: DB.show('simon')
            a1                   b2
            ----------------------------------------
            0                    0
            1                    1
            1                    2
        """
    def get_cursor(self, ignore_warning=None):
        """
        Return a pysqlite cursor for the database connection.

        A cursor is an input from which you can execute sqlite commands on the
        database.

        Recommended for more advanced users only.

        EXAMPLES::

            sage: DB = SQLDatabase()
            sage: DB.create_table('simon',{'a1':{'sql':'bool'}, 'b2':{'sql':'int'}})
            sage: DB.add_row('simon',(0,1))
            sage: DB.add_rows('simon',[(0,0),(1,1),(1,2)])
            sage: DB.add_rows('simon',[(0,0),(4,0),(5,1)], ['b2','a1'])
            sage: cur = DB.get_cursor()
            sage: (cur.execute('select * from simon')).fetchall()
            [(0, 1), (0, 0), (1, 1), (1, 2), (0, 0), (0, 4), (1, 5)]
        """
    def get_connection(self, ignore_warning=None):
        """
        Return a pysqlite connection to the database.

        You most likely want ``get_cursor()`` instead, which is used for
        executing sqlite commands on the database.

        Recommended for more advanced users only.

        EXAMPLES::

            sage: D = SQLDatabase(read_only=True)
            sage: con = D.get_connection()
            doctest:...: RuntimeWarning: Database is read only, using the connection can alter the stored data. Set self.ignore_warnings to True in order to mute future warnings.
            sage: con = D.get_connection(True)
            sage: D.ignore_warnings = True
            sage: con = D.get_connection()
            sage: t = con.execute('CREATE TABLE simon(n INTEGER, n2 INTEGER)')
            sage: for n in range(10):
            ....:   t = con.execute('INSERT INTO simon VALUES(%d,%d)'%(n,n^2))
            sage: D.show('simon')
            n                    n2
            ----------------------------------------
            0                    0
            1                    1
            2                    4
            3                    9
            4                    16
            5                    25
            6                    36
            7                    49
            8                    64
            9                    81
        """
    def create_table(self, table_name, table_skeleton) -> None:
        """
        Create a new table in the database.

        To create a table, a column structure must be specified. The form for
        this is a Python dict, for example::

            {'col1': {'sql':'INTEGER', 'index':False, 'unique':True, 'primary_key':False}, ...}

        INPUT:

        - ``table_name`` -- string
        - ``table_skeleton`` -- a double-indexed dictionary

            - outer key -- column name

                - inner key -- one of the following:

                    - ``primary_key`` -- boolean, whether column has been set
                      asprimary key
                    - ``index`` -- boolean, whether column has been set as
                      index
                    - ``unique`` -- boolean, whether column has been set as
                      unique
                    - ``sql`` -- one of ``'TEXT'``, ``'BOOLEAN'``,
                      ``'INTEGER'``, ``'REAL'``, or other user defined type

        NOTE:

        Some SQL features, such as automatically incrementing primary key,
        require the full word ``'INTEGER'``, not just ``'INT'``.

        EXAMPLES::

            sage: from collections import OrderedDict
            sage: D = SQLDatabase()
            sage: table_skeleton = OrderedDict([
            ....: ('graph6', {'sql':'TEXT', 'index':True, 'primary_key':True}),
            ....: ('vertices', {'sql':'INTEGER'}),
            ....: ('edges', {'sql':'INTEGER'})
            ....: ])
            sage: D.create_table('simon', table_skeleton)
            sage: D.show('simon')
            graph6               vertices             edges
            ------------------------------------------------------------
        """
    def add_column(self, table_name, col_name, col_dict, default: str = 'NULL') -> None:
        """
        Add a column named ``col_name`` to table ``table_name``, whose data
        types are described by ``col_dict``. The format for this is::

            {'col1':{'primary_key':False, 'unique': True, 'index':True, 'sql':'REAL'}}

        INPUT:

        - ``col_dict`` -- dictionary:

            - key -- column name

                - inner key -- one of the following:

                    - ``primary_key`` -- boolean, whether column has been set
                      as primary key
                    - ``index`` -- boolean, whether column has been set as
                      index
                    - ``unique`` -- boolean, whether column has been set as
                      unique
                    - ``sql`` -- one of ``'TEXT'``, ``'BOOLEAN'``,
                      ``'INTEGER'``, ``'REAL'``, or other user defined type

        EXAMPLES::

            sage: from collections import OrderedDict
            sage: MonicPolys = SQLDatabase()
            sage: MonicPolys.create_table('simon', OrderedDict([('n', {'sql':'INTEGER', 'index':True})]))
            sage: for n in range(20): MonicPolys.add_row('simon', (n,))
            sage: MonicPolys.add_column('simon', 'n_squared', {'sql':'INTEGER', 'index':False}, 0)
            sage: MonicPolys.show('simon')
            n                    n_squared
            ----------------------------------------
            0                    0
            1                    0
            2                    0
            3                    0
            4                    0
            5                    0
            6                    0
            7                    0
            8                    0
            9                    0
            10                   0
            11                   0
            12                   0
            13                   0
            14                   0
            15                   0
            16                   0
            17                   0
            18                   0
            19                   0
        """
    def drop_column(self, table_name, col_name) -> None:
        """
        Drop the column ``col_name`` from table ``table_name``.

        EXAMPLES::

            sage: MonicPolys = SQLDatabase()
            sage: MonicPolys.create_table('simon', {'n':{'sql':'INTEGER', 'index':True}})
            sage: for n in range(20): MonicPolys.add_row('simon', (n,))
            sage: MonicPolys.add_column('simon', 'n_squared', {'sql':'INTEGER'}, 0)
            sage: MonicPolys.drop_column('simon', 'n_squared')
            sage: MonicPolys.show('simon')
            n
            --------------------
            0
            1
            2
            3
            4
            5
            6
            7
            8
            9
            10
            11
            12
            13
            14
            15
            16
            17
            18
            19
        """
    def rename_table(self, table_name, new_name) -> None:
        """
        Rename the table ``table_name`` to ``new_name``.

        EXAMPLES::

            sage: D = SQLDatabase()
            sage: D.create_table('simon',{'col1':{'sql':'INTEGER'}})
            sage: D.show('simon')
            col1
            --------------------
            sage: D.rename_table('simon', 'lucy')
            sage: D.show('simon')
            Traceback (most recent call last):
            ...
            RuntimeError: Failure to fetch data.
            sage: D.show('lucy')
            col1
            --------------------
        """
    def drop_table(self, table_name) -> None:
        """
        Delete table ``table_name`` from database.

        INPUT:

        - ``table_name`` -- string

        EXAMPLES::

            sage: D = SQLDatabase()
            sage: D.create_table('simon',{'col1':{'sql':'INTEGER'}})
            sage: D.show('simon')
            col1
            --------------------
            sage: D.drop_table('simon')
            sage: D.get_skeleton()
            {}
        """
    def drop_data_from_table(self, table_name) -> None:
        """
        Remove all rows from ``table_name``.

        EXAMPLES::

            sage: D = SQLDatabase()
            sage: D.create_table('simon',{'col1':{'sql':'INTEGER'}})
            sage: D.add_row('simon',(9,))
            sage: D.show('simon')
            col1
            --------------------
            9
            sage: D.drop_data_from_table('simon')
            sage: D.show('simon')
            col1
            --------------------
        """
    def make_index(self, col_name, table_name, unique: bool = False) -> None:
        """
        Set the column ``col_name`` in table ``table_name`` to be an index,
        that is, a column set up to do quick searches on.

        INPUT:

        - ``col_name`` -- string
        - ``table_name`` -- string
        - ``unique`` -- requires that there are no multiple entries in the
          column, makes searching faster

        EXAMPLES::

            sage: MonicPolys = SQLDatabase()
            sage: MonicPolys.create_table('simon', {'n':{'sql':'INTEGER', 'index':True}, 'n2':{'sql':'INTEGER'}})
            sage: MonicPolys.make_index('n2','simon')
            sage: MonicPolys.get_skeleton()
            {'simon': {'n': {'index': True,
               'primary_key': False,
               'sql': 'INTEGER',
               'unique': False},
              'n2': {'index': True,
               'primary_key': False,
               'sql': 'INTEGER',
               'unique': False}}}
        """
    def drop_index(self, table_name, index_name) -> None:
        """
        Set the column ``index_name`` in table ``table_name`` to not be an
        index. See ``make_index()``

        EXAMPLES::

            sage: MonicPolys = SQLDatabase()
            sage: MonicPolys.create_table('simon', {'n':{'sql':'INTEGER', 'index':True}, 'n2':{'sql':'INTEGER'}})
            sage: MonicPolys.drop_index('simon', 'n')
            sage: MonicPolys.get_skeleton()
            {'simon': {'n': {'index': False,
               'primary_key': False,
               'sql': 'INTEGER',
               'unique': False},
              'n2': {'index': False,
               'primary_key': False,
               'sql': 'INTEGER',
               'unique': False}}}
        """
    def make_unique(self, table_name, col_name) -> None:
        """
        Set the column ``col_name`` in table ``table_name`` to store unique
        values.

        NOTE:

        This function only adds the requirement for entries in ``col_name`` to
        be unique, it does not change the values.

        EXAMPLES::

            sage: MonicPolys = SQLDatabase()
            sage: MonicPolys.create_table('simon', {'n':{'sql':'INTEGER', 'index':True}, 'n2':{'sql':'INTEGER'}})
            sage: MonicPolys.make_unique('simon', 'n2')
            sage: MonicPolys.get_skeleton()
            {'simon': {'n': {'index': True,
               'primary_key': False,
               'sql': 'INTEGER',
               'unique': False},
              'n2': {'index': False,
               'primary_key': False,
               'sql': 'INTEGER',
               'unique': True}}}
        """
    def drop_unique(self, table_name, col_name) -> None:
        """
        Set the column ``col_name`` in table ``table_name`` not store unique
        values.

        NOTE:

        This function only removes the requirement for entries in ``col_name``
        to be unique, it does not delete it.

        EXAMPLES::

            sage: MonicPolys = SQLDatabase()
            sage: MonicPolys.create_table('simon', {'n':{'sql':'INTEGER', 'index':True}, 'n2':{'sql':'INTEGER'}})
            sage: MonicPolys.make_unique('simon', 'n2')
            sage: MonicPolys.drop_unique('simon', 'n2')
            sage: MonicPolys.get_skeleton()
            {'simon': {'n': {'index': True,
               'primary_key': False,
               'sql': 'INTEGER',
               'unique': False},
              'n2': {'index': False,
               'primary_key': False,
               'sql': 'INTEGER',
               'unique': False}}}
        """
    def make_primary_key(self, table_name, col_name) -> None:
        """
        Set the column ``col_name`` in table ``table_name`` to be a primary key.

        A primary key is something like an index, but its main purpose is to
        link different tables together. This allows searches to be executed on
        multiple tables that represent maybe different data about the same
        objects.

        NOTE:

        Some SQL features, such as automatically incrementing primary key,
        require the full word ``'INTEGER'``, not just ``'INT'``.

        EXAMPLES::

            sage: MonicPolys = SQLDatabase()
            sage: MonicPolys.create_table('simon', {'n':{'sql':'INTEGER', 'index':True}, 'n2':{'sql':'INTEGER'}})
            sage: MonicPolys.make_primary_key('simon', 'n2')
            sage: MonicPolys.get_skeleton()
            {'simon': {'n': {'index': True,
               'primary_key': False,
               'sql': 'INTEGER',
               'unique': False},
              'n2': {'index': False,
               'primary_key': True,
               'sql': 'INTEGER',
               'unique': True}}}
        """
    def drop_primary_key(self, table_name, col_name) -> None:
        """
        Set the column ``col_name`` in table ``table_name`` not to be a primary
        key.

        A primary key is something like an index, but its main purpose is to
        link different tables together. This allows searches to be executed on
        multiple tables that represent maybe different data about the same
        objects.

        NOTE:

        This function only changes the column to be non-primary, it does not
        delete it.

        EXAMPLES::

            sage: MonicPolys = SQLDatabase()
            sage: MonicPolys.create_table('simon', {'n':{'sql':'INTEGER', 'index':True}, 'n2':{'sql':'INTEGER'}})
            sage: MonicPolys.make_primary_key('simon', 'n2')
            sage: MonicPolys.drop_primary_key('simon', 'n2')
            sage: MonicPolys.get_skeleton()
            {'simon': {'n': {'index': True,
               'primary_key': False,
               'sql': 'INTEGER',
               'unique': False},
              'n2': {'index': False,
               'primary_key': False,
               'sql': 'INTEGER',
               'unique': True}}}
        """
    def add_row(self, table_name, values, entry_order=None) -> None:
        """
        Add the row described by ``values`` to the table ``table_name``. Values
        should be a tuple, of same length and order as columns in given table.

        NOTE:

        If ``values`` is of length one, be sure to specify that it is a tuple of
        length one, by using a comma, e.g.::

            sage: values = (6,)

        EXAMPLES::

            sage: DB = SQLDatabase()
            sage: DB.create_table('simon',{'a1':{'sql':'bool'}, 'b2':{'sql':'int'}})
            sage: DB.add_row('simon',(0,1))
            sage: cur = DB.get_cursor()
            sage: (cur.execute('select * from simon')).fetchall()
            [(0, 1)]
        """
    def delete_rows(self, query) -> None:
        """
        Use a ``SQLQuery`` instance to modify (delete rows from) the
        database.

        ``SQLQuery`` must have no join statements.  (As of now, you can only
        delete from one table at a time -- ideas and patches are welcome).

        To remove all data that satisfies a ``SQLQuery``, send the query as an
        argument to ``delete_rows``.  Be careful, test your query first.

        Recommended use:  have some kind of row identification primary
        key column that you use as a parameter in the query.  (See example
        below).

        INPUT:

        - ``query`` -- a ``SQLQuery`` (Delete the rows returned when query is
          run)

        EXAMPLES::

            sage: from collections import OrderedDict
            sage: DB = SQLDatabase()
            sage: DB.create_table('lucy', OrderedDict([
            ....: ('id', {'sql':'INTEGER', 'primary_key':True, 'index':True}),
            ....: ('a1', {'sql':'bool'}),
            ....: ('b2', {'sql':'int'})]))
            sage: DB.add_rows('lucy', [(0,1,1),(1,1,4),(2,0,7),(3,1,384), (4,1,978932)],['id','a1','b2'])
            sage: DB.show('lucy')
            id                   a1                   b2
            ------------------------------------------------------------
            0                    1                    1
            1                    1                    4
            2                    0                    7
            3                    1                    384
            4                    1                    978932
            sage: Q = SQLQuery(DB, {'table_name':'lucy', 'display_cols':['id','a1','b2'], 'expression':['id','>=',3]})
            sage: DB.delete_rows(Q)
            sage: DB.show('lucy')
            id                   a1                   b2
            ------------------------------------------------------------
            0                    1                    1
            1                    1                    4
            2                    0                    7
        """
    def add_rows(self, table_name, rows, entry_order=None) -> None:
        """
        INPUT:

        - ``rows`` -- list of tuples that represent one row of data to add
          (types should match col types in order)
        - ``entry_order`` -- an ordered list or tuple overrides normal order
          with user defined order

        EXAMPLES::

            sage: DB = SQLDatabase()
            sage: DB.create_table('simon',{'a1':{'sql':'bool'}, 'b2':{'sql':'int'}})
            sage: DB.add_rows('simon',[(0,0),(1,1),(1,2)])
            sage: DB.add_rows('simon',[(0,0),(4,0),(5,1)], ['b2','a1'])
            sage: cur = DB.get_cursor()
            sage: (cur.execute('select * from simon')).fetchall()
            [(0, 0), (1, 1), (1, 2), (0, 0), (0, 4), (1, 5)]
        """
    add_data = add_rows
    def vacuum(self) -> None:
        """
        Clean the extra hard disk space used up by a database that has
        recently shrunk.

        EXAMPLES::

            sage: DB = SQLDatabase()
            sage: DB.create_table('simon',{'a1':{'sql':'bool'}, 'b2':{'sql':'int'}})
            sage: DB.add_row('simon',(0,1))
            sage: DB.add_data('simon',[(0,0),(1,1),(1,2)])
            sage: DB.add_data('simon',[(0,0),(4,0),(5,1)], ['b2','a1'])
            sage: DB.drop_column('simon','b2')
            sage: DB.commit()
            sage: DB.vacuum()
        """
    def commit(self) -> None:
        """
        Commit changes to file.

        EXAMPLES::

            sage: DB = SQLDatabase()
            sage: DB.create_table('simon',{'a1':{'sql':'bool'}, 'b2':{'sql':'int'}})
            sage: DB.add_row('simon',(0,1))
            sage: DB.add_data('simon',[(0,0),(1,1),(1,2)])
            sage: DB.add_data('simon',[(0,0),(4,0),(5,1)], ['b2','a1'])
            sage: DB.drop_column('simon','b2')
            sage: DB.commit()
            sage: DB.vacuum()
        """
