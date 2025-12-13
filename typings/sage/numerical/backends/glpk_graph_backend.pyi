from sage.cpython.string import bytes_to_str as bytes_to_str, str_to_bytes as str_to_bytes
from sage.numerical.mip import MIPSolverException as MIPSolverException
from typing import Any, ClassVar, overload

FS_ENCODING: str

class GLPKGraphBackend:
    '''File: /build/sagemath/src/sage/src/sage/numerical/backends/glpk_graph_backend.pyx (starting at line 80)

        GLPK Backend for access to GLPK graph functions.

        The constructor can either be called without arguments (which results in an
        empty graph) or with arguments to read graph data from a file.

        INPUT:

        - ``data`` -- a filename or a :class:`Graph` object

        - ``format`` -- when ``data`` is a filename, specifies the format of the
          data read from a file.  The ``format`` parameter is a string and can take
          values as described in the table below.

        **Format parameters:**

        .. list-table::
         :widths: 10 70

         * - ``plain``

           - Read data from a plain text file containing the following information:

               | nv na
               | i[1] j[1]
               | i[2] j[2]
               | . . .
               | i[na] j[na]

             where:

             * nv is the number of vertices (nodes);

             * na is the number of arcs;

             * i[k], k = 1, . . . , na, is the index of tail vertex of arc k;

             * j[k], k = 1, . . . , na, is the index of head vertex of arc k.


         * - ``dimacs``

           - Read data from a plain ASCII text file in DIMACS format.
             A description of the DIMACS format can be found at
             http://dimacs.rutgers.edu/Challenges/.

         * - ``mincost``

           - Reads the mincost flow problem data from a text file in DIMACS format

         * - ``maxflow``

           - Reads the maximum flow problem data from a text file in DIMACS format

        .. NOTE::

            When ``data`` is a :class:`Graph`, the following restrictions are
            applied.

                * vertices -- the value of the demand of each vertex (see
                  :meth:`set_vertex_demand`) is obtained from the numerical
                  value associated with the key "rhs" if it is a dictionary.

                * edges -- The edge values used in the algorithms are read from the
                  edges labels (and left undefined if the edge labels are equal to
                  ``None``). To be defined, the labels must be dictionary objects with
                  keys "low", "cap" and "cost". See :meth:`get_edge` for details.

        EXAMPLES:

        The following example creates an empty graph::

            sage: from sage.numerical.backends.glpk_graph_backend import GLPKGraphBackend
            sage: gbe = GLPKGraphBackend()

        The following example creates an empty graph, adds some data, saves the data
        to a file and loads it::

            sage: from sage.numerical.backends.glpk_graph_backend import GLPKGraphBackend
            sage: gbe = GLPKGraphBackend()
            sage: gbe.add_vertices([None, None])
            [\'0\', \'1\']
            sage: a = gbe.add_edge(\'0\', \'1\')
            sage: import tempfile
            sage: with tempfile.NamedTemporaryFile() as f:
            ....:     _ = gbe.write_graph(f.name)
            ....:     gbe1 = GLPKGraphBackend(f.name, "plain")
            Writing graph to ...
            4 lines were written
            Reading graph from ...
            Graph has 2 vertices and 1 edge
            3 lines were read

        The following example imports a Sage ``Graph`` and then uses it to solve a
        maxflow problem::

            sage: from sage.numerical.backends.glpk_graph_backend import GLPKGraphBackend
            sage: g = graphs.PappusGraph()
            sage: for ed in g.edges(sort=False):
            ....:     g.set_edge_label(ed[0], ed[1], {"cap":1})
            sage: gbe = GLPKGraphBackend(g)
            sage: gbe.maxflow_ffalg(\'1\', \'2\')
            3.0
    '''
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    @classmethod
    def __init__(cls, *args, **kwargs) -> None:
        """Create and return a new object.  See help(type) for accurate signature."""
    def add_edge(self, u, v, dictparams=...) -> Any:
        '''GLPKGraphBackend.add_edge(self, u, v, dict params=None)

        File: /build/sagemath/src/sage/src/sage/numerical/backends/glpk_graph_backend.pyx (starting at line 555)

        Add an edge between vertices ``u`` and ``v``.

        Allows adding an edge and optionally providing parameters used by the
        algorithms. If a vertex does not exist it is created.

        INPUT:

        - ``u`` -- the name (as string) of the tail vertex

        - ``v`` -- the name (as string) of the head vertex

        - ``params`` -- an optional dictionary containing the edge parameters used
          for the algorithms. The following keys are used:

            * ``low`` -- the minimum flow through the edge

            * ``cap`` -- the maximum capacity of the edge

            * ``cost`` -- the cost of transporting one unit through the edge

        EXAMPLES::

            sage: from sage.numerical.backends.glpk_graph_backend import GLPKGraphBackend
            sage: gbe = GLPKGraphBackend()
            sage: gbe.add_edge("A", "B", {"low":0.0, "cap":10.0, "cost":5})
            sage: gbe.vertices()
            [\'A\', \'B\']
            sage: for ed in gbe.edges():
            ....:     print((ed[0], ed[1], ed[2][\'cap\'], ed[2][\'cost\'], ed[2][\'low\']))
            (\'A\', \'B\', 10.0, 5.0, 0.0)
            sage: gbe.add_edge("B", "C", {"low":0.0, "cap":10.0, "cost":\'5\'})
            Traceback (most recent call last):
            ...
            TypeError: Invalid edge parameter.'''
    @overload
    def add_edges(self, edges) -> list:
        '''GLPKGraphBackend.add_edges(self, edges) -> list

        File: /build/sagemath/src/sage/src/sage/numerical/backends/glpk_graph_backend.pyx (starting at line 619)

        Add edges to the graph.

        INPUT:

        - ``edges`` -- an iterable container of pairs of the form ``(u, v)``,
          where ``u`` is name (as string) of the tail vertex and ``v`` is the
          name (as string) of the head vertex or an iterable container of
          triples of the form ``(u, v, params)`` where params is a dictionary as
          described in ``add_edge``.

        EXAMPLES::

            sage: from sage.numerical.backends.glpk_graph_backend import GLPKGraphBackend
            sage: gbe = GLPKGraphBackend()
            sage: edges = [("A", "B", {"low":0.0, "cap":10.0, "cost":5})]
            sage: edges.append(("B", "C"))
            sage: gbe.add_edges(edges)
            sage: for ed in gbe.edges():
            ....:     print((ed[0], ed[1], ed[2][\'cap\'], ed[2][\'cost\'], ed[2][\'low\']))
            (\'A\', \'B\', 10.0, 5.0, 0.0)
            (\'B\', \'C\', 0.0, 0.0, 0.0)
            sage: edges = [("C", "D", {"low":0.0, "cap":10.0, "cost":5})]
            sage: edges.append(("C", "E", 5))
            sage: gbe.add_edges(edges)
            Traceback (most recent call last):
            ...
            TypeError: Argument \'params\' has incorrect type ...
            sage: for ed in gbe.edges():
            ....:     print((ed[0], ed[1], ed[2][\'cap\'], ed[2][\'cost\'], ed[2][\'low\']))
            (\'A\', \'B\', 10.0, 5.0, 0.0)
            (\'B\', \'C\', 0.0, 0.0, 0.0)
            (\'C\', \'D\', 10.0, 5.0, 0.0)'''
    @overload
    def add_edges(self, edges) -> Any:
        '''GLPKGraphBackend.add_edges(self, edges) -> list

        File: /build/sagemath/src/sage/src/sage/numerical/backends/glpk_graph_backend.pyx (starting at line 619)

        Add edges to the graph.

        INPUT:

        - ``edges`` -- an iterable container of pairs of the form ``(u, v)``,
          where ``u`` is name (as string) of the tail vertex and ``v`` is the
          name (as string) of the head vertex or an iterable container of
          triples of the form ``(u, v, params)`` where params is a dictionary as
          described in ``add_edge``.

        EXAMPLES::

            sage: from sage.numerical.backends.glpk_graph_backend import GLPKGraphBackend
            sage: gbe = GLPKGraphBackend()
            sage: edges = [("A", "B", {"low":0.0, "cap":10.0, "cost":5})]
            sage: edges.append(("B", "C"))
            sage: gbe.add_edges(edges)
            sage: for ed in gbe.edges():
            ....:     print((ed[0], ed[1], ed[2][\'cap\'], ed[2][\'cost\'], ed[2][\'low\']))
            (\'A\', \'B\', 10.0, 5.0, 0.0)
            (\'B\', \'C\', 0.0, 0.0, 0.0)
            sage: edges = [("C", "D", {"low":0.0, "cap":10.0, "cost":5})]
            sage: edges.append(("C", "E", 5))
            sage: gbe.add_edges(edges)
            Traceback (most recent call last):
            ...
            TypeError: Argument \'params\' has incorrect type ...
            sage: for ed in gbe.edges():
            ....:     print((ed[0], ed[1], ed[2][\'cap\'], ed[2][\'cost\'], ed[2][\'low\']))
            (\'A\', \'B\', 10.0, 5.0, 0.0)
            (\'B\', \'C\', 0.0, 0.0, 0.0)
            (\'C\', \'D\', 10.0, 5.0, 0.0)'''
    @overload
    def add_edges(self, edges) -> Any:
        '''GLPKGraphBackend.add_edges(self, edges) -> list

        File: /build/sagemath/src/sage/src/sage/numerical/backends/glpk_graph_backend.pyx (starting at line 619)

        Add edges to the graph.

        INPUT:

        - ``edges`` -- an iterable container of pairs of the form ``(u, v)``,
          where ``u`` is name (as string) of the tail vertex and ``v`` is the
          name (as string) of the head vertex or an iterable container of
          triples of the form ``(u, v, params)`` where params is a dictionary as
          described in ``add_edge``.

        EXAMPLES::

            sage: from sage.numerical.backends.glpk_graph_backend import GLPKGraphBackend
            sage: gbe = GLPKGraphBackend()
            sage: edges = [("A", "B", {"low":0.0, "cap":10.0, "cost":5})]
            sage: edges.append(("B", "C"))
            sage: gbe.add_edges(edges)
            sage: for ed in gbe.edges():
            ....:     print((ed[0], ed[1], ed[2][\'cap\'], ed[2][\'cost\'], ed[2][\'low\']))
            (\'A\', \'B\', 10.0, 5.0, 0.0)
            (\'B\', \'C\', 0.0, 0.0, 0.0)
            sage: edges = [("C", "D", {"low":0.0, "cap":10.0, "cost":5})]
            sage: edges.append(("C", "E", 5))
            sage: gbe.add_edges(edges)
            Traceback (most recent call last):
            ...
            TypeError: Argument \'params\' has incorrect type ...
            sage: for ed in gbe.edges():
            ....:     print((ed[0], ed[1], ed[2][\'cap\'], ed[2][\'cost\'], ed[2][\'low\']))
            (\'A\', \'B\', 10.0, 5.0, 0.0)
            (\'B\', \'C\', 0.0, 0.0, 0.0)
            (\'C\', \'D\', 10.0, 5.0, 0.0)'''
    @overload
    def add_vertex(self, name=...) -> Any:
        '''GLPKGraphBackend.add_vertex(self, name=None)

        File: /build/sagemath/src/sage/src/sage/numerical/backends/glpk_graph_backend.pyx (starting at line 234)

        Add an isolated vertex to the graph.

        If the vertex already exists, nothing is done.

        INPUT:

        - ``name`` -- string of max 255 chars length. If no name is
          specified, then the vertex will be represented by the string
          representation of the ID of the vertex or - if this already exists -
          a string representation of the least integer not already representing
          a vertex.

        OUTPUT:

        If no ``name`` is passed as an argument, the new vertex name is
        returned. ``None`` otherwise.

        EXAMPLES::

            sage: from sage.numerical.backends.glpk_graph_backend import GLPKGraphBackend
            sage: gbe = GLPKGraphBackend()
            sage: gbe.add_vertex()
            \'0\'
            sage: gbe.add_vertex("2")
            sage: gbe.add_vertex()
            \'1\''''
    @overload
    def add_vertex(self) -> Any:
        '''GLPKGraphBackend.add_vertex(self, name=None)

        File: /build/sagemath/src/sage/src/sage/numerical/backends/glpk_graph_backend.pyx (starting at line 234)

        Add an isolated vertex to the graph.

        If the vertex already exists, nothing is done.

        INPUT:

        - ``name`` -- string of max 255 chars length. If no name is
          specified, then the vertex will be represented by the string
          representation of the ID of the vertex or - if this already exists -
          a string representation of the least integer not already representing
          a vertex.

        OUTPUT:

        If no ``name`` is passed as an argument, the new vertex name is
        returned. ``None`` otherwise.

        EXAMPLES::

            sage: from sage.numerical.backends.glpk_graph_backend import GLPKGraphBackend
            sage: gbe = GLPKGraphBackend()
            sage: gbe.add_vertex()
            \'0\'
            sage: gbe.add_vertex("2")
            sage: gbe.add_vertex()
            \'1\''''
    @overload
    def add_vertex(self) -> Any:
        '''GLPKGraphBackend.add_vertex(self, name=None)

        File: /build/sagemath/src/sage/src/sage/numerical/backends/glpk_graph_backend.pyx (starting at line 234)

        Add an isolated vertex to the graph.

        If the vertex already exists, nothing is done.

        INPUT:

        - ``name`` -- string of max 255 chars length. If no name is
          specified, then the vertex will be represented by the string
          representation of the ID of the vertex or - if this already exists -
          a string representation of the least integer not already representing
          a vertex.

        OUTPUT:

        If no ``name`` is passed as an argument, the new vertex name is
        returned. ``None`` otherwise.

        EXAMPLES::

            sage: from sage.numerical.backends.glpk_graph_backend import GLPKGraphBackend
            sage: gbe = GLPKGraphBackend()
            sage: gbe.add_vertex()
            \'0\'
            sage: gbe.add_vertex("2")
            sage: gbe.add_vertex()
            \'1\''''
    @overload
    def add_vertices(self, vertices) -> list:
        """GLPKGraphBackend.add_vertices(self, vertices) -> list

        File: /build/sagemath/src/sage/src/sage/numerical/backends/glpk_graph_backend.pyx (starting at line 330)

        Add vertices from an iterable container of vertices.

        Vertices that already exist in the graph will not be added again.

        INPUT:

        - ``vertices`` -- iterator of vertex labels (string); a label can be
          ``None``

        OUTPUT:

        Generated names of new vertices if there is at least one ``None`` value
        present in ``vertices``. ``None`` otherwise.

        EXAMPLES::

            sage: from sage.numerical.backends.glpk_graph_backend import GLPKGraphBackend
            sage: gbe = GLPKGraphBackend()
            sage: vertices = [None for i in range(3)]
            sage: gbe.add_vertices(vertices)
            ['0', '1', '2']
            sage: gbe.add_vertices(['A', 'B', None])
            ['5']
            sage: gbe.add_vertices(['A', 'B', 'C'])
            sage: gbe.vertices()
            ['0', '1', '2', 'A', 'B', '5', 'C']

        TESTS::

            sage: from sage.numerical.backends.glpk_graph_backend import GLPKGraphBackend
            sage: gbe = GLPKGraphBackend()
            sage: gbe.add_vertices([None, None, None, '1'])
            ['0', '2', '3']"""
    @overload
    def add_vertices(self, vertices) -> Any:
        """GLPKGraphBackend.add_vertices(self, vertices) -> list

        File: /build/sagemath/src/sage/src/sage/numerical/backends/glpk_graph_backend.pyx (starting at line 330)

        Add vertices from an iterable container of vertices.

        Vertices that already exist in the graph will not be added again.

        INPUT:

        - ``vertices`` -- iterator of vertex labels (string); a label can be
          ``None``

        OUTPUT:

        Generated names of new vertices if there is at least one ``None`` value
        present in ``vertices``. ``None`` otherwise.

        EXAMPLES::

            sage: from sage.numerical.backends.glpk_graph_backend import GLPKGraphBackend
            sage: gbe = GLPKGraphBackend()
            sage: vertices = [None for i in range(3)]
            sage: gbe.add_vertices(vertices)
            ['0', '1', '2']
            sage: gbe.add_vertices(['A', 'B', None])
            ['5']
            sage: gbe.add_vertices(['A', 'B', 'C'])
            sage: gbe.vertices()
            ['0', '1', '2', 'A', 'B', '5', 'C']

        TESTS::

            sage: from sage.numerical.backends.glpk_graph_backend import GLPKGraphBackend
            sage: gbe = GLPKGraphBackend()
            sage: gbe.add_vertices([None, None, None, '1'])
            ['0', '2', '3']"""
    @overload
    def cpp(self) -> double:
        '''GLPKGraphBackend.cpp(self) -> double

        File: /build/sagemath/src/sage/src/sage/numerical/backends/glpk_graph_backend.pyx (starting at line 1312)

        Solve the critical path problem of a project network.

        OUTPUT: the length of the critical path of the network

        EXAMPLES::

            sage: from sage.numerical.backends.glpk_graph_backend import GLPKGraphBackend
            sage: gbe = GLPKGraphBackend()
            sage: gbe.add_vertices([None for i in range(3)])
            [\'0\', \'1\', \'2\']
            sage: gbe.set_vertex_demand(\'0\', 3)
            sage: gbe.set_vertex_demand(\'1\', 1)
            sage: gbe.set_vertex_demand(\'2\', 4)
            sage: a = gbe.add_edge(\'0\', \'2\')
            sage: a = gbe.add_edge(\'1\', \'2\')
            sage: gbe.cpp()
            7.0
            sage: v = gbe.get_vertex(\'1\')
            sage: 1, v["rhs"], v["es"], v["ls"] # abs tol 1e-6
            (1, 1.0, 0.0, 2.0)'''
    @overload
    def cpp(self) -> Any:
        '''GLPKGraphBackend.cpp(self) -> double

        File: /build/sagemath/src/sage/src/sage/numerical/backends/glpk_graph_backend.pyx (starting at line 1312)

        Solve the critical path problem of a project network.

        OUTPUT: the length of the critical path of the network

        EXAMPLES::

            sage: from sage.numerical.backends.glpk_graph_backend import GLPKGraphBackend
            sage: gbe = GLPKGraphBackend()
            sage: gbe.add_vertices([None for i in range(3)])
            [\'0\', \'1\', \'2\']
            sage: gbe.set_vertex_demand(\'0\', 3)
            sage: gbe.set_vertex_demand(\'1\', 1)
            sage: gbe.set_vertex_demand(\'2\', 4)
            sage: a = gbe.add_edge(\'0\', \'2\')
            sage: a = gbe.add_edge(\'1\', \'2\')
            sage: gbe.cpp()
            7.0
            sage: v = gbe.get_vertex(\'1\')
            sage: 1, v["rhs"], v["es"], v["ls"] # abs tol 1e-6
            (1, 1.0, 0.0, 2.0)'''
    def delete_edge(self, u, v, dictparams=...) -> Any:
        '''GLPKGraphBackend.delete_edge(self, u, v, dict params=None)

        File: /build/sagemath/src/sage/src/sage/numerical/backends/glpk_graph_backend.pyx (starting at line 895)

        Delete an edge from the graph.

        If an edge does not exist it is ignored.

        INPUT:

        - ``u`` -- the name (as string) of the tail vertex of the edge
        - ``v`` -- the name (as string) of the tail vertex of the edge
        - ``params`` -- an optional dictionary containing the edge
          parameters (see :meth:`add_edge`). If this parameter
          is not provided, all edges connecting ``u`` and ``v`` are deleted.
          Otherwise only edges with matching parameters are deleted.

        .. SEEALSO::

            :meth:`delete_edges`

        EXAMPLES::

            sage: from sage.numerical.backends.glpk_graph_backend import GLPKGraphBackend
            sage: gbe = GLPKGraphBackend()
            sage: edges = [("A", "B", {"low":0.0, "cap":10.0, "cost":5})]
            sage: edges.append(("A", "B", {"low":0.0, "cap":15.0, "cost":10}))
            sage: edges.append(("B", "C", {"low":0.0, "cap":20.0, "cost":1}))
            sage: edges.append(("B", "C", {"low":0.0, "cap":10.0, "cost":20}))
            sage: gbe.add_edges(edges)
            sage: gbe.delete_edge("A", "B")
            sage: gbe.delete_edge("B", "C", {"low":0.0, "cap":10.0, "cost":20})
            sage: gbe.edges()[0][0], gbe.edges()[0][1], gbe.edges()[0][2][\'cost\']
            (\'B\', \'C\', 1.0)'''
    def delete_edges(self, edges) -> Any:
        '''GLPKGraphBackend.delete_edges(self, edges)

        File: /build/sagemath/src/sage/src/sage/numerical/backends/glpk_graph_backend.pyx (starting at line 974)

        Delete edges from the graph.

        Non existing edges are ignored.

        INPUT:

        - ``edges`` -- an iterable container of edges

        .. SEEALSO::

            :meth:`delete_edge`

        EXAMPLES::

            sage: from sage.numerical.backends.glpk_graph_backend import GLPKGraphBackend
            sage: gbe = GLPKGraphBackend()
            sage: edges = [("A", "B", {"low":0.0, "cap":10.0, "cost":5})]
            sage: edges.append(("A", "B", {"low":0.0, "cap":15.0, "cost":10}))
            sage: edges.append(("B", "C", {"low":0.0, "cap":20.0, "cost":1}))
            sage: edges.append(("B", "C", {"low":0.0, "cap":10.0, "cost":20}))
            sage: gbe.add_edges(edges)
            sage: gbe.delete_edges(edges[1:])
            sage: len(gbe.edges())
            1
            sage: gbe.edges()[0][0], gbe.edges()[0][1], gbe.edges()[0][2][\'cap\']
            (\'A\', \'B\', 10.0)'''
    def delete_vertex(self, vert) -> Any:
        '''GLPKGraphBackend.delete_vertex(self, vert)

        File: /build/sagemath/src/sage/src/sage/numerical/backends/glpk_graph_backend.pyx (starting at line 815)

        Removes a vertex from the graph.

        Trying to delete a non existing vertex will raise an exception.

        INPUT:

        - ``vert`` -- the name (as string) of the vertex to delete

        EXAMPLES::

            sage: from sage.numerical.backends.glpk_graph_backend import GLPKGraphBackend
            sage: gbe = GLPKGraphBackend()
            sage: verts = ["A", "D"]
            sage: gbe.add_vertices(verts)
            sage: gbe.delete_vertex("A")
            sage: gbe.vertices()
            [\'D\']
            sage: gbe.delete_vertex("A")
            Traceback (most recent call last):
            ...
            RuntimeError: Vertex A does not exist.'''
    @overload
    def delete_vertices(self, listverts) -> Any:
        '''GLPKGraphBackend.delete_vertices(self, list verts)

        File: /build/sagemath/src/sage/src/sage/numerical/backends/glpk_graph_backend.pyx (starting at line 851)

        Removes vertices from the graph.

        Trying to delete a non existing vertex will raise an exception.

        INPUT:

        - ``verts`` -- iterable container containing names (as string) of the
          vertices to delete

        EXAMPLES::

            sage: from sage.numerical.backends.glpk_graph_backend import GLPKGraphBackend
            sage: gbe = GLPKGraphBackend()
            sage: verts = ["A", "B", "C", "D"]
            sage: gbe.add_vertices(verts)
            sage: v_d = ["A", "B"]
            sage: gbe.delete_vertices(v_d)
            sage: gbe.vertices()
            [\'C\', \'D\']
            sage: gbe.delete_vertices(["C", "A"])
            Traceback (most recent call last):
            ...
            RuntimeError: Vertex A does not exist.
            sage: gbe.vertices()
            [\'C\', \'D\']'''
    @overload
    def delete_vertices(self, v_d) -> Any:
        '''GLPKGraphBackend.delete_vertices(self, list verts)

        File: /build/sagemath/src/sage/src/sage/numerical/backends/glpk_graph_backend.pyx (starting at line 851)

        Removes vertices from the graph.

        Trying to delete a non existing vertex will raise an exception.

        INPUT:

        - ``verts`` -- iterable container containing names (as string) of the
          vertices to delete

        EXAMPLES::

            sage: from sage.numerical.backends.glpk_graph_backend import GLPKGraphBackend
            sage: gbe = GLPKGraphBackend()
            sage: verts = ["A", "B", "C", "D"]
            sage: gbe.add_vertices(verts)
            sage: v_d = ["A", "B"]
            sage: gbe.delete_vertices(v_d)
            sage: gbe.vertices()
            [\'C\', \'D\']
            sage: gbe.delete_vertices(["C", "A"])
            Traceback (most recent call last):
            ...
            RuntimeError: Vertex A does not exist.
            sage: gbe.vertices()
            [\'C\', \'D\']'''
    @overload
    def edges(self) -> list:
        '''GLPKGraphBackend.edges(self) -> list

        File: /build/sagemath/src/sage/src/sage/numerical/backends/glpk_graph_backend.pyx (starting at line 768)

        Return a ``list`` of all edges in the graph.

        OUTPUT: a ``list`` of ``triples`` representing the edges of the graph

        EXAMPLES::

            sage: from sage.numerical.backends.glpk_graph_backend import GLPKGraphBackend
            sage: gbe = GLPKGraphBackend()
            sage: edges = [("A", "B", {"low":0.0, "cap":10.0, "cost":5})]
            sage: edges.append(("B", "C"))
            sage: gbe.add_edges(edges)
            sage: for ed in gbe.edges():
            ....:     print((ed[0], ed[1], ed[2][\'cost\']))
            (\'A\', \'B\', 5.0)
            (\'B\', \'C\', 0.0)'''
    @overload
    def edges(self) -> Any:
        '''GLPKGraphBackend.edges(self) -> list

        File: /build/sagemath/src/sage/src/sage/numerical/backends/glpk_graph_backend.pyx (starting at line 768)

        Return a ``list`` of all edges in the graph.

        OUTPUT: a ``list`` of ``triples`` representing the edges of the graph

        EXAMPLES::

            sage: from sage.numerical.backends.glpk_graph_backend import GLPKGraphBackend
            sage: gbe = GLPKGraphBackend()
            sage: edges = [("A", "B", {"low":0.0, "cap":10.0, "cost":5})]
            sage: edges.append(("B", "C"))
            sage: gbe.add_edges(edges)
            sage: for ed in gbe.edges():
            ....:     print((ed[0], ed[1], ed[2][\'cost\']))
            (\'A\', \'B\', 5.0)
            (\'B\', \'C\', 0.0)'''
    def get_edge(self, u, v) -> tuple:
        '''GLPKGraphBackend.get_edge(self, u, v) -> tuple

        File: /build/sagemath/src/sage/src/sage/numerical/backends/glpk_graph_backend.pyx (starting at line 712)

        Return an edge connecting two vertices.

        .. NOTE::

           If multiple edges connect the two vertices only the first edge
           found is returned.

        INPUT:

        - ``u`` -- name (as string) of the tail vertex
        - ``v`` -- name (as string) of the head vertex

        OUTPUT:

        A ``triple`` describing if edge was found or ``None`` if not. The third
        value of the triple is a dictionary containing the following edge
        parameters:

            * ``low`` -- the minimum flow through the edge
            * ``cap`` -- the maximum capacity of the edge
            * ``cost`` -- the cost of transporting one unit through the edge
            * ``x`` -- the actual flow through the edge after solving

        EXAMPLES::

            sage: from sage.numerical.backends.glpk_graph_backend import GLPKGraphBackend
            sage: gbe = GLPKGraphBackend()
            sage: edges = [("A", "B"), ("A", "C"), ("B", "C")]
            sage: gbe.add_edges(edges)
            sage: ed = gbe.get_edge("A", "B")
            sage: ed[0], ed[1], ed[2][\'x\']
            (\'A\', \'B\', 0.0)
            sage: gbe.get_edge("A", "F") is None
            True'''
    def get_vertex(self, vertex) -> dict:
        '''GLPKGraphBackend.get_vertex(self, vertex) -> dict

        File: /build/sagemath/src/sage/src/sage/numerical/backends/glpk_graph_backend.pyx (starting at line 447)

        Return a specific vertex as a dictionary Object.

        INPUT:

        - ``vertex`` -- the vertex label as string

        OUTPUT:

        The vertex as a dictionary object or ``None`` if the vertex does not
        exist. The dictionary contains the values used or created by the different
        algorithms. The values associated with the keys following keys contain:

            * "rhs"  -- The supply / demand value the vertex (mincost alg)
            * "pi"   -- The node potential (mincost alg)
            * "cut"  -- The cut flag of the vertex (maxflow alg)
            * "es"   -- The earliest start of task (cpp alg)
            * "ls"   -- The latest start of task (cpp alg)

        EXAMPLES::

            sage: from sage.numerical.backends.glpk_graph_backend import GLPKGraphBackend
            sage: gbe = GLPKGraphBackend()
            sage: verts = ["A", "B", "C", "D"]
            sage: gbe.add_vertices(verts)
            sage: sorted(gbe.get_vertex("A").items())
            [(\'cut\', 0), (\'es\', 0.0), (\'ls\', 0.0), (\'pi\', 0.0), (\'rhs\', 0.0)]
            sage: gbe.get_vertex("F") is None
            True'''
    @overload
    def get_vertices(self, verts) -> dict:
        '''GLPKGraphBackend.get_vertices(self, verts) -> dict

        File: /build/sagemath/src/sage/src/sage/numerical/backends/glpk_graph_backend.pyx (starting at line 494)

        Return a dictionary of the dictionaries associated to each vertex.

        INPUT:

        - ``verts`` -- iterable container of vertices

        OUTPUT:

        A list of pairs ``(vertex, properties)`` where ``properties`` is a
        dictionary containing the numerical values associated with a vertex. For
        more information, see the documentation of
        :meth:`GLPKGraphBackend.get_vertex`.

        EXAMPLES::

            sage: from sage.numerical.backends.glpk_graph_backend import GLPKGraphBackend
            sage: gbe = GLPKGraphBackend()
            sage: verts = [\'A\', \'B\']
            sage: gbe.add_vertices(verts)
            sage: sorted(gbe.get_vertices(verts)[\'B\'].items())
            [(\'cut\', 0), (\'es\', 0.0), (\'ls\', 0.0), (\'pi\', 0.0), (\'rhs\', 0.0)]
            sage: gbe.get_vertices(["C", "D"])
            {}'''
    @overload
    def get_vertices(self, verts) -> Any:
        '''GLPKGraphBackend.get_vertices(self, verts) -> dict

        File: /build/sagemath/src/sage/src/sage/numerical/backends/glpk_graph_backend.pyx (starting at line 494)

        Return a dictionary of the dictionaries associated to each vertex.

        INPUT:

        - ``verts`` -- iterable container of vertices

        OUTPUT:

        A list of pairs ``(vertex, properties)`` where ``properties`` is a
        dictionary containing the numerical values associated with a vertex. For
        more information, see the documentation of
        :meth:`GLPKGraphBackend.get_vertex`.

        EXAMPLES::

            sage: from sage.numerical.backends.glpk_graph_backend import GLPKGraphBackend
            sage: gbe = GLPKGraphBackend()
            sage: verts = [\'A\', \'B\']
            sage: gbe.add_vertices(verts)
            sage: sorted(gbe.get_vertices(verts)[\'B\'].items())
            [(\'cut\', 0), (\'es\', 0.0), (\'ls\', 0.0), (\'pi\', 0.0), (\'rhs\', 0.0)]
            sage: gbe.get_vertices(["C", "D"])
            {}'''
    @overload
    def maxflow_ffalg(self, u=..., v=...) -> double:
        '''GLPKGraphBackend.maxflow_ffalg(self, u=None, v=None) -> double

        File: /build/sagemath/src/sage/src/sage/numerical/backends/glpk_graph_backend.pyx (starting at line 1226)

        Finds solution to the maxflow problem with Ford-Fulkerson algorithm.

        INPUT:

        - ``u`` -- name (as string) of the tail vertex; default is ``None``
        - ``v`` -- name (as string) of the head vertex; default is ``None``

        If ``u`` or ``v`` are ``None``, the currently stored values for the
        head or tail vertex are used. This behavior is useful when reading
        maxflow data from a file. When calling this function with values for
        ``u`` and ``v``, the head and tail vertex are stored for
        later use.

        OUTPUT: the solution to the maxflow problem, i.e. the maximum flow

        .. NOTE::

            * If the source or sink vertex does not exist, an :exc:`IndexError` is
              raised.

            * If the source and sink are identical, a :exc:`ValueError` is raised.

            * This method raises ``MIPSolverException`` exceptions when the
              solution cannot be computed for any reason (none exists, or the
              LP solver was not able to find it, etc...)

        EXAMPLES::

            sage: from sage.numerical.backends.glpk_graph_backend import GLPKGraphBackend
            sage: gbe = GLPKGraphBackend()
            sage: v = gbe.add_vertices([None for i in range(5)])
            sage: edges = ((0, 1, 2), (0, 2, 3), (1, 2, 3), (1, 3, 4),
            ....:         (3, 4, 1), (2, 4, 2))
            sage: for a in edges:
            ....:     edge = gbe.add_edge(str(a[0]), str(a[1]), {"cap":a[2]})
            sage: gbe.maxflow_ffalg(\'0\', \'4\')
            3.0
            sage: gbe.maxflow_ffalg()
            3.0
            sage: gbe.maxflow_ffalg(\'0\', \'8\')
            Traceback (most recent call last):
            ...
            IndexError: Source or sink vertex does not exist'''
    @overload
    def maxflow_ffalg(self) -> Any:
        '''GLPKGraphBackend.maxflow_ffalg(self, u=None, v=None) -> double

        File: /build/sagemath/src/sage/src/sage/numerical/backends/glpk_graph_backend.pyx (starting at line 1226)

        Finds solution to the maxflow problem with Ford-Fulkerson algorithm.

        INPUT:

        - ``u`` -- name (as string) of the tail vertex; default is ``None``
        - ``v`` -- name (as string) of the head vertex; default is ``None``

        If ``u`` or ``v`` are ``None``, the currently stored values for the
        head or tail vertex are used. This behavior is useful when reading
        maxflow data from a file. When calling this function with values for
        ``u`` and ``v``, the head and tail vertex are stored for
        later use.

        OUTPUT: the solution to the maxflow problem, i.e. the maximum flow

        .. NOTE::

            * If the source or sink vertex does not exist, an :exc:`IndexError` is
              raised.

            * If the source and sink are identical, a :exc:`ValueError` is raised.

            * This method raises ``MIPSolverException`` exceptions when the
              solution cannot be computed for any reason (none exists, or the
              LP solver was not able to find it, etc...)

        EXAMPLES::

            sage: from sage.numerical.backends.glpk_graph_backend import GLPKGraphBackend
            sage: gbe = GLPKGraphBackend()
            sage: v = gbe.add_vertices([None for i in range(5)])
            sage: edges = ((0, 1, 2), (0, 2, 3), (1, 2, 3), (1, 3, 4),
            ....:         (3, 4, 1), (2, 4, 2))
            sage: for a in edges:
            ....:     edge = gbe.add_edge(str(a[0]), str(a[1]), {"cap":a[2]})
            sage: gbe.maxflow_ffalg(\'0\', \'4\')
            3.0
            sage: gbe.maxflow_ffalg()
            3.0
            sage: gbe.maxflow_ffalg(\'0\', \'8\')
            Traceback (most recent call last):
            ...
            IndexError: Source or sink vertex does not exist'''
    @overload
    def mincost_okalg(self) -> double:
        '''GLPKGraphBackend.mincost_okalg(self) -> double

        File: /build/sagemath/src/sage/src/sage/numerical/backends/glpk_graph_backend.pyx (starting at line 1115)

        Finds solution to the mincost problem with the out-of-kilter algorithm.

        The out-of-kilter algorithm requires all problem data to be integer
        valued.

        OUTPUT:

        The solution to the mincost problem, i.e. the total cost, if operation
        was successful.

        .. NOTE::

           This method raises ``MIPSolverException`` exceptions when
           the solution cannot be computed for any reason (none
           exists, or the LP solver was not able to find it, etc...)

        EXAMPLES::

            sage: from sage.numerical.backends.glpk_graph_backend import GLPKGraphBackend
            sage: gbe = GLPKGraphBackend()
            sage: vertices = (35, 50, 40, -45, -20, -30, -30)
            sage: vs = gbe.add_vertices([None for i in range(len(vertices))])
            sage: v_dict = {}
            sage: for i, v in enumerate(vs):
            ....:     v_dict[v] = vertices[i]
            sage: gbe.set_vertices_demand(list(v_dict.items()))
            sage: cost = ((8, 6, 10, 9), (9, 12, 13, 7), (14, 9, 16, 5))

            sage: for i in range(len(cost)):
            ....:     for j in range(len(cost[0])):
            ....:         gbe.add_edge(str(i), str(j + len(cost)), {"cost":cost[i][j], "cap":100})
            sage: gbe.mincost_okalg()
            1020.0
            sage: for ed in gbe.edges():
            ....:     print("{} -> {} {}".format(ed[0], ed[1], ed[2]["x"]))
            0 -> 6 0.0
            0 -> 5 25.0
            0 -> 4 10.0
            0 -> 3 0.0
            1 -> 6 0.0
            1 -> 5 5.0
            1 -> 4 0.0
            1 -> 3 45.0
            2 -> 6 30.0
            2 -> 5 0.0
            2 -> 4 10.0
            2 -> 3 0.0'''
    @overload
    def mincost_okalg(self) -> Any:
        '''GLPKGraphBackend.mincost_okalg(self) -> double

        File: /build/sagemath/src/sage/src/sage/numerical/backends/glpk_graph_backend.pyx (starting at line 1115)

        Finds solution to the mincost problem with the out-of-kilter algorithm.

        The out-of-kilter algorithm requires all problem data to be integer
        valued.

        OUTPUT:

        The solution to the mincost problem, i.e. the total cost, if operation
        was successful.

        .. NOTE::

           This method raises ``MIPSolverException`` exceptions when
           the solution cannot be computed for any reason (none
           exists, or the LP solver was not able to find it, etc...)

        EXAMPLES::

            sage: from sage.numerical.backends.glpk_graph_backend import GLPKGraphBackend
            sage: gbe = GLPKGraphBackend()
            sage: vertices = (35, 50, 40, -45, -20, -30, -30)
            sage: vs = gbe.add_vertices([None for i in range(len(vertices))])
            sage: v_dict = {}
            sage: for i, v in enumerate(vs):
            ....:     v_dict[v] = vertices[i]
            sage: gbe.set_vertices_demand(list(v_dict.items()))
            sage: cost = ((8, 6, 10, 9), (9, 12, 13, 7), (14, 9, 16, 5))

            sage: for i in range(len(cost)):
            ....:     for j in range(len(cost[0])):
            ....:         gbe.add_edge(str(i), str(j + len(cost)), {"cost":cost[i][j], "cap":100})
            sage: gbe.mincost_okalg()
            1020.0
            sage: for ed in gbe.edges():
            ....:     print("{} -> {} {}".format(ed[0], ed[1], ed[2]["x"]))
            0 -> 6 0.0
            0 -> 5 25.0
            0 -> 4 10.0
            0 -> 3 0.0
            1 -> 6 0.0
            1 -> 5 5.0
            1 -> 4 0.0
            1 -> 3 45.0
            2 -> 6 30.0
            2 -> 5 0.0
            2 -> 4 10.0
            2 -> 3 0.0'''
    def set_vertex_demand(self, vertex, demand) -> Any:
        """GLPKGraphBackend.set_vertex_demand(self, vertex, demand)

        File: /build/sagemath/src/sage/src/sage/numerical/backends/glpk_graph_backend.pyx (starting at line 382)

        Set the demand of the vertex in a mincost flow algorithm.

        INPUT:

        - ``vertex`` -- name of the vertex

        - ``demand`` -- the numerical value representing demand of the vertex in
          a mincost flow algorithm (it could be for instance `-1` to represent a
          sink, or `1` to represent a source and `0` for a neutral vertex). This
          can either be an ``int`` or ``float`` value.

        EXAMPLES::

            sage: from sage.numerical.backends.glpk_graph_backend import GLPKGraphBackend
            sage: gbe = GLPKGraphBackend()
            sage: vertices = [None for i in range(3)]
            sage: gbe.add_vertices(vertices)
            ['0', '1', '2']
            sage: gbe.set_vertex_demand('0', 2)
            sage: gbe.get_vertex('0')['rhs']
            2.0
            sage: gbe.set_vertex_demand('3', 2)
            Traceback (most recent call last):
            ...
            KeyError: 'Vertex 3 does not exist.'"""
    def set_vertices_demand(self, listpairs) -> Any:
        """GLPKGraphBackend.set_vertices_demand(self, list pairs)

        File: /build/sagemath/src/sage/src/sage/numerical/backends/glpk_graph_backend.pyx (starting at line 419)

        Set the parameters of selected vertices.

        INPUT:

        - ``pairs`` -- list of pairs ``(vertex, demand)`` associating a demand
          to each vertex. For more information, see the documentation of
          :meth:`set_vertex_demand`.

        EXAMPLES::

            sage: from sage.numerical.backends.glpk_graph_backend import GLPKGraphBackend
            sage: gbe = GLPKGraphBackend()
            sage: vertices = [None for i in range(3)]
            sage: gbe.add_vertices(vertices)
            ['0', '1', '2']
            sage: gbe.set_vertices_demand([('0', 2), ('1', 3), ('3', 4)])
            sage: sorted(gbe.get_vertex('1').items())
            [('cut', 0), ('es', 0.0), ('ls', 0.0), ('pi', 0.0), ('rhs', 3.0)]"""
    @overload
    def vertices(self) -> list:
        '''GLPKGraphBackend.vertices(self) -> list

        File: /build/sagemath/src/sage/src/sage/numerical/backends/glpk_graph_backend.pyx (starting at line 523)

        Return the list of all vertices.

        .. NOTE::

           Changing elements of the ``list`` will not change anything in the
           the graph.

        .. NOTE::

           If a vertex in the graph does not have a name / label it will appear
           as ``None`` in the resulting ``list``.

        EXAMPLES::

            sage: from sage.numerical.backends.glpk_graph_backend import GLPKGraphBackend
            sage: gbe = GLPKGraphBackend()
            sage: verts = ["A", "B", "C"]
            sage: gbe.add_vertices(verts)
            sage: a = gbe.vertices(); a
            [\'A\', \'B\', \'C\']
            sage: a.pop(0)
            \'A\'
            sage: gbe.vertices()
            [\'A\', \'B\', \'C\']'''
    @overload
    def vertices(self) -> Any:
        '''GLPKGraphBackend.vertices(self) -> list

        File: /build/sagemath/src/sage/src/sage/numerical/backends/glpk_graph_backend.pyx (starting at line 523)

        Return the list of all vertices.

        .. NOTE::

           Changing elements of the ``list`` will not change anything in the
           the graph.

        .. NOTE::

           If a vertex in the graph does not have a name / label it will appear
           as ``None`` in the resulting ``list``.

        EXAMPLES::

            sage: from sage.numerical.backends.glpk_graph_backend import GLPKGraphBackend
            sage: gbe = GLPKGraphBackend()
            sage: verts = ["A", "B", "C"]
            sage: gbe.add_vertices(verts)
            sage: a = gbe.vertices(); a
            [\'A\', \'B\', \'C\']
            sage: a.pop(0)
            \'A\'
            sage: gbe.vertices()
            [\'A\', \'B\', \'C\']'''
    @overload
    def vertices(self) -> Any:
        '''GLPKGraphBackend.vertices(self) -> list

        File: /build/sagemath/src/sage/src/sage/numerical/backends/glpk_graph_backend.pyx (starting at line 523)

        Return the list of all vertices.

        .. NOTE::

           Changing elements of the ``list`` will not change anything in the
           the graph.

        .. NOTE::

           If a vertex in the graph does not have a name / label it will appear
           as ``None`` in the resulting ``list``.

        EXAMPLES::

            sage: from sage.numerical.backends.glpk_graph_backend import GLPKGraphBackend
            sage: gbe = GLPKGraphBackend()
            sage: verts = ["A", "B", "C"]
            sage: gbe.add_vertices(verts)
            sage: a = gbe.vertices(); a
            [\'A\', \'B\', \'C\']
            sage: a.pop(0)
            \'A\'
            sage: gbe.vertices()
            [\'A\', \'B\', \'C\']'''
    def write_ccdata(self, fname) -> int:
        '''GLPKGraphBackend.write_ccdata(self, fname) -> int

        File: /build/sagemath/src/sage/src/sage/numerical/backends/glpk_graph_backend.pyx (starting at line 1058)

        Writes the graph to a text file in DIMACS format.

        Writes the data to plain ASCII text file in DIMACS format.
        A description of the DIMACS format can be found at
        http://dimacs.rutgers.edu/Challenges/.

        INPUT:

        - ``fname`` -- full name of the file

        OUTPUT: zero if the operations was successful otherwise nonzero

        EXAMPLES::

            sage: from sage.numerical.backends.glpk_graph_backend import GLPKGraphBackend
            sage: gbe = GLPKGraphBackend()
            sage: a = gbe.add_edge("0", "1")
            sage: import tempfile
            sage: with tempfile.NamedTemporaryFile() as f:
            ....:     gbe.write_ccdata(f.name)
            Writing graph to ...
            6 lines were written
            0'''
    def write_graph(self, fname) -> int:
        '''GLPKGraphBackend.write_graph(self, fname) -> int

        File: /build/sagemath/src/sage/src/sage/numerical/backends/glpk_graph_backend.pyx (starting at line 1032)

        Writes the graph to a plain text file

        INPUT:

        - ``fname`` -- full name of the file

        OUTPUT: zero if the operations was successful otherwise nonzero

        EXAMPLES::

            sage: from sage.numerical.backends.glpk_graph_backend import GLPKGraphBackend
            sage: gbe = GLPKGraphBackend()
            sage: a = gbe.add_edge("0", "1")
            sage: import tempfile
            sage: with tempfile.NamedTemporaryFile() as f:
            ....:     gbe.write_graph(f.name)
            Writing graph to ...
            4 lines were written
            0'''
    def write_maxflow(self, fname) -> int:
        """GLPKGraphBackend.write_maxflow(self, fname) -> int

        File: /build/sagemath/src/sage/src/sage/numerical/backends/glpk_graph_backend.pyx (starting at line 1185)

        Writes the maximum flow problem data to a text file in DIMACS format.

        INPUT:

        - ``fname`` -- full name of file

        OUTPUT:

        ``Zero`` if successful, otherwise ``nonzero``

        EXAMPLES::

            sage: from sage.numerical.backends.glpk_graph_backend import GLPKGraphBackend
            sage: gbe = GLPKGraphBackend()
            sage: import tempfile
            sage: with tempfile.NamedTemporaryFile() as f:
            ....:     gbe.write_maxflow(f.name)
            Traceback (most recent call last):
            ...
            OSError: Cannot write empty graph
            sage: gbe.add_vertices([None for i in range(2)])
            ['0', '1']
            sage: a = gbe.add_edge('0', '1')
            sage: gbe.maxflow_ffalg('0', '1')
            0.0
            sage: with tempfile.NamedTemporaryFile() as f:
            ....:     gbe.write_maxflow(f.name)
            Writing maximum flow problem data to ...
            6 lines were written
            0"""
    def write_mincost(self, fname) -> int:
        '''GLPKGraphBackend.write_mincost(self, fname) -> int

        File: /build/sagemath/src/sage/src/sage/numerical/backends/glpk_graph_backend.pyx (starting at line 1088)

        Writes the mincost flow problem data to a text file in DIMACS format

        INPUT:

        - ``fname`` -- full name of file

        OUTPUT: zero if successful, otherwise nonzero

        EXAMPLES::

            sage: from sage.numerical.backends.glpk_graph_backend import GLPKGraphBackend
            sage: gbe = GLPKGraphBackend()
            sage: a = gbe.add_edge("0", "1")
            sage: import tempfile
            sage: with tempfile.NamedTemporaryFile() as f:
            ....:     gbe.write_mincost(f.name)
            Writing min-cost flow problem data to ...
            4 lines were written
            0'''
