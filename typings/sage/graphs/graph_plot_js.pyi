from sage.misc.lazy_import import lazy_import as lazy_import
from sage.misc.temporary_file import tmp_filename as tmp_filename

def gen_html_code(G, vertex_labels: bool = True, edge_labels: bool = False, vertex_partition=[], vertex_colors=None, edge_partition=[], force_spring_layout: bool = False, charge: int = -120, link_distance: int = 30, link_strength: int = 2, gravity: float = 0.04, vertex_size: int = 7, edge_thickness: int = 4):
    '''
    Create a .html file showing the graph using `d3.js <https://d3js.org/>`_.

    This function returns the name of the .html file. If you want to visualize
    the actual graph use :meth:`~sage.graphs.generic_graph.GenericGraph.show`.

    INPUT:

    - ``G`` -- the graph

    - ``vertex_labels`` -- boolean (default: ``False``); whether to display
      vertex labels

    - ``edge_labels`` -- boolean (default: ``False``); whether to display edge
      labels

    - ``vertex_partition`` -- list (default: ``[]``); a list of lists
      representing a partition of the vertex set. Vertices are then colored in
      the graph according to the partition.

    - ``vertex_colors`` -- dictionary (default: ``None``); a dictionary
      representing a partition of the vertex set. Keys are colors (ignored) and
      values are lists of vertices. Vertices are then colored in the graph
      according to the partition.

    - ``edge_partition`` -- list (default: ``[]``); same as
      ``vertex_partition``, with edges instead

    - ``force_spring_layout`` -- boolean (default: ``False``); whether to take
      previously computed position of nodes into account if there is one, or to
      compute a spring layout

    - ``vertex_size`` -- integer (default: 7); the size of a vertex\' circle

    - ``edge_thickness`` -- integer (default: 4); thickness of an edge

    - ``charge`` -- integer (default: -120); the vertices\' charge. Defines
      how they repulse each other. See
      `<https://github.com/mbostock/d3/wiki/Force-Layout>`_ for more
      information

    - ``link_distance`` -- integer (default: 30); see
      `<https://github.com/mbostock/d3/wiki/Force-Layout>`_ for more
      information

    - ``link_strength`` -- integer (default: 2); see
      `<https://github.com/mbostock/d3/wiki/Force-Layout>`_ for more
      information

    - ``gravity`` -- float (default: 0.04); see
      `<https://github.com/mbostock/d3/wiki/Force-Layout>`_ for more
      information

    .. WARNING::

        Since the d3js package is not standard yet, the javascript is fetched
        from d3js.org website by the browser. If you want to avoid that (e.g.
        to protect your privacy or by lack of internet connection), you can
        install the d3js package for offline use by running ``sage -i d3js``
        from the command line.

    EXAMPLES::

        sage: graphs.RandomTree(50).show(method=\'js\')                           # optional - internet

        sage: g = graphs.PetersenGraph()
        sage: g.show(method=\'js\', vertex_partition=g.coloring())                # optional - internet

        sage: graphs.DodecahedralGraph().show(method=\'js\',                      # optional - internet
        ....:                                 force_spring_layout=True)

        sage: graphs.DodecahedralGraph().show(method=\'js\')                      # optional - internet

        sage: # needs sage.combinat
        sage: g = digraphs.DeBruijn(2, 2)
        sage: g.allow_multiple_edges(True)
        sage: g.add_edge("10", "10", "a")
        sage: g.add_edge("10", "10", "b")
        sage: g.add_edge("10", "10", "c")
        sage: g.add_edge("10", "10", "d")
        sage: g.add_edge("01", "11", "1")
        sage: g.show(method=\'js\', vertex_labels=True, edge_labels=True,         # optional - internet
        ....:        link_distance=200, gravity=.05, charge=-500,
        ....:        edge_partition=[[("11", "12", "2"), ("21", "21", "a")]],
        ....:        edge_thickness=4)

    TESTS::

        sage: from sage.graphs.graph_plot_js import gen_html_code
        sage: filename = gen_html_code(graphs.PetersenGraph())

    :issue:`17370`::

        sage: filename = gen_html_code(graphs.CompleteBipartiteGraph(4, 5))

    In the generated html code, the source (resp. target) of a link is the index
    of the node in the list defining the names of the nodes. We check that the
    order is correct (:issue:`27460`)::

        sage: filename = gen_html_code(DiGraph({1: [10]}))
        sage: with open(filename, \'r\') as f:
        ....:     data = f.read()
        sage: nodes = data.partition(\'"nodes":\')[2]; nodes
        ...[{..."name": "10"...}, {..."name": "1"...}]...
        sage: links = data.partition(\'"links":\')[2]
        sage: \'"source": 1\' in links and \'"target": 0\' in links
        True
    '''
