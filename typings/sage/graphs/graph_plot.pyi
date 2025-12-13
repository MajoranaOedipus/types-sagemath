from _typeshed import Incomplete
from sage.misc.lazy_import import lazy_import as lazy_import
from sage.structure.sage_object import SageObject as SageObject

layout_options: Incomplete
graphplot_options: Incomplete
__doc__: Incomplete
DEFAULT_SHOW_OPTIONS: Incomplete
DEFAULT_PLOT_OPTIONS: Incomplete

class GraphPlot(SageObject):
    def __init__(self, graph, options) -> None:
        """
        Return a ``GraphPlot`` object, which stores all the parameters needed
        for plotting (Di)Graphs.

        A ``GraphPlot`` has a plot and show function, as well as some functions
        to set parameters for vertices and edges.  This constructor assumes
        default options are set.  Defaults are shown in the example below.

        EXAMPLES::

            sage: from sage.graphs.graph_plot import GraphPlot
            sage: options = {
            ....:     'vertex_size': 200,
            ....:     'vertex_labels': True,
            ....:     'layout': None,
            ....:     'edge_style': 'solid',
            ....:     'edge_color': 'black',
            ....:     'edge_colors': None,
            ....:     'edge_labels': False,
            ....:     'iterations': 50,
            ....:     'tree_orientation': 'down',
            ....:     'heights': None,
            ....:     'graph_border': False,
            ....:     'talk': False,
            ....:     'color_by_label': False,
            ....:     'partition': None,
            ....:     'dist': .075,
            ....:     'max_dist': 1.5,
            ....:     'loop_size': .075,
            ....:     'edge_labels_background': 'transparent'}
            sage: g = Graph({0: [1, 2], 2: [3], 4: [0, 1]})
            sage: GP = GraphPlot(g, options)
        """
    def set_pos(self) -> None:
        """
        Set the position plotting parameters for this GraphPlot.

        EXAMPLES:

        This function is called implicitly by the code below::

            sage: g = Graph({0: [1, 2], 2: [3], 4: [0, 1]})
            sage: g.graphplot(save_pos=True, layout='circular')  # indirect doctest
            GraphPlot object for Graph on 5 vertices

        The following illustrates the format of a position dictionary, but due
        to numerical noise we do not check the values themselves::

            sage: g.get_pos()
            {0: (0.0, 1.0),
             1: (-0.951..., 0.309...),
             2: (-0.587..., -0.809...),
             3: (0.587..., -0.809...),
             4: (0.951..., 0.309...)}

        ::

            sage: T = list(graphs.trees(7))
            sage: t = T[3]
            sage: t.plot(heights={0: [0], 1: [4, 5, 1], 2: [2], 3: [3, 6]})
            Graphics object consisting of 14 graphics primitives

        .. PLOT::

            g = Graph({0: [1, 2], 2: [3], 4: [0, 1]})
            g.graphplot(save_pos=True, layout='circular')  # indirect doctest
            T = list(graphs.trees(7))
            t = T[3]
            P = t.plot(heights={0: [0], 1: [4, 5, 1], 2: [2], 3: [3, 6]})
            sphinx_plot(P)

        TESTS:

        Make sure that vertex locations are floats.  Not being floats isn't
        a bug in itself but made it too easy to accidentally introduce a bug
        elsewhere, such as in :meth:`set_edges` (:issue:`10124`), via silent
        truncating division of Python 2 integers::

            sage: g = graphs.FruchtGraph()
            sage: gp = g.graphplot()
            sage: set(map(type, flatten(gp._pos.values())))
            {<... 'float'>}
            sage: g = graphs.BullGraph()
            sage: gp = g.graphplot(save_pos=True)
            sage: set(map(type, flatten(gp._pos.values())))
            {<... 'float'>}

        Non-ascii labels are also possible using unicode (:issue:`21008`)::

            sage: Graph({u'où': [u'là', u'ici']}).plot()
            Graphics object consisting of 6 graphics primitives
        """
    def set_vertices(self, **vertex_options):
        """
        Set the vertex plotting parameters for this ``GraphPlot``.

        This function is called by the constructor but can also be
        called to make updates to the vertex options of an existing
        ``GraphPlot`` object. Note that the changes are cumulative.

        EXAMPLES::

            sage: g = Graph({}, loops=True, multiedges=True, sparse=True)
            sage: g.add_edges([(0, 0, 'a'), (0, 0, 'b'), (0, 1, 'c'),
            ....:              (0, 1, 'd'), (0, 1, 'e'), (0, 1, 'f'),
            ....:              (0, 1, 'f'), (2, 1, 'g'), (2, 2, 'h')])
            sage: GP = g.graphplot(vertex_size=100, edge_labels=True,
            ....:                  color_by_label=True, edge_style='dashed')
            sage: GP.set_vertices(talk=True)
            sage: GP.plot()
            Graphics object consisting of 22 graphics primitives
            sage: GP.set_vertices(vertex_color='green', vertex_shape='^')
            sage: GP.plot()
            Graphics object consisting of 22 graphics primitives

        .. PLOT::

            g = Graph({}, loops=True, multiedges=True, sparse=True)
            g.add_edges([(0, 0, 'a'), (0, 0, 'b'), (0, 1, 'c'),
                         (0, 1, 'd'), (0, 1, 'e'), (0, 1, 'f'),
                         (0, 1, 'f'), (2, 1, 'g'), (2, 2, 'h')])
            GP = g.graphplot(vertex_size=100, edge_labels=True,
                             color_by_label=True, edge_style='dashed')
            GP.set_vertices(talk=True)
            sphinx_plot(GP)

        .. PLOT::

            g = Graph({}, loops=True, multiedges=True, sparse=True)
            g.add_edges([(0, 0, 'a'), (0, 0, 'b'), (0, 1, 'c'),
                         (0, 1, 'd'), (0, 1, 'e'), (0, 1, 'f'),
                         (0, 1, 'f'), (2, 1, 'g'), (2, 2, 'h')])
            GP = g.graphplot(vertex_size=100, edge_labels=True,
                             color_by_label=True, edge_style='dashed')
            GP.set_vertices(talk=True)
            GP.set_vertices(vertex_color='green', vertex_shape='^')
            sphinx_plot(GP)

        Vertex labels are flexible::

            sage: g = graphs.PathGraph(4)
            sage: g.plot(vertex_labels=False)
            Graphics object consisting of 4 graphics primitives

        .. PLOT::

            g = graphs.PathGraph(4)
            P = g.graphplot(vertex_labels=False)
            sphinx_plot(P)

        ::

            sage: g = graphs.PathGraph(4)
            sage: g.plot(vertex_labels=True)
            Graphics object consisting of 8 graphics primitives

        .. PLOT::

            g = graphs.PathGraph(4)
            P = g.graphplot(vertex_labels=True)
            sphinx_plot(P)

        ::

            sage: g = graphs.PathGraph(4)
            sage: g.plot(vertex_labels=dict(zip(g, ['+', '-', '/', '*'])))
            Graphics object consisting of 8 graphics primitives

        .. PLOT::

            g = graphs.PathGraph(4)
            P = g.graphplot(vertex_labels=dict(zip(g, ['+', '-', '/', '*'])))
            sphinx_plot(P)

        ::

            sage: g = graphs.PathGraph(4)
            sage: g.plot(vertex_labels=lambda x: str(x % 2))
            Graphics object consisting of 8 graphics primitives

        .. PLOT::

            g = graphs.PathGraph(4)
            P = g.graphplot(vertex_labels=lambda x: str(x % 2))
            sphinx_plot(P)
        """
    def set_edges(self, **edge_options):
        '''
        Set edge plotting parameters for the ``GraphPlot`` object.

        This function is called by the constructor but can also be called to
        update the edge options of an existing ``GraphPlot`` object.
        Note that the changes are cumulative.

        EXAMPLES::

            sage: g = Graph(loops=True, multiedges=True, sparse=True)
            sage: g.add_edges([(0, 0, \'a\'), (0, 0, \'b\'), (0, 1, \'c\'),
            ....:              (0, 1, \'d\'), (0, 1, \'e\'), (0, 1, \'f\'),
            ....:              (0, 1, \'f\'), (2, 1, \'g\'), (2, 2, \'h\')])
            sage: GP = g.graphplot(vertex_size=100, edge_labels=True,
            ....:                  color_by_label=True, edge_style=\'dashed\')
            sage: GP.set_edges(edge_style=\'solid\')
            sage: GP.plot()
            Graphics object consisting of 22 graphics primitives

        .. PLOT::

            g = Graph(loops=True, multiedges=True, sparse=True)
            g.add_edges([(0, 0, \'a\'), (0, 0, \'b\'), (0, 1, \'c\'),
                         (0, 1, \'d\'), (0, 1, \'e\'), (0, 1, \'f\'),
                         (0, 1, \'f\'), (2, 1, \'g\'), (2, 2, \'h\')])
            GP = g.graphplot(vertex_size=100, edge_labels=True,
                             color_by_label=True, edge_style=\'dashed\')
            GP.set_edges(edge_style=\'solid\')
            sphinx_plot(GP)

        ::

            sage: GP.set_edges(edge_color=\'black\')
            sage: GP.plot()
            Graphics object consisting of 22 graphics primitives

        .. PLOT::

            g = Graph(loops=True, multiedges=True, sparse=True)
            g.add_edges([(0, 0, \'a\'), (0, 0, \'b\'), (0, 1, \'c\'),
                         (0, 1, \'d\'), (0, 1, \'e\'), (0, 1, \'f\'),
                         (0, 1, \'f\'), (2, 1, \'g\'), (2, 2, \'h\')])
            GP = g.graphplot(vertex_size=100, edge_labels=True,
                             color_by_label=True, edge_style=\'dashed\')
            GP.set_edges(edge_style=\'solid\')
            GP.set_edges(edge_color=\'black\')
            sphinx_plot(GP)

        ::

            sage: d = DiGraph(loops=True, multiedges=True, sparse=True)
            sage: d.add_edges([(0, 0, \'a\'), (0, 0, \'b\'), (0, 1, \'c\'),
            ....:              (0, 1, \'d\'), (0, 1, \'e\'), (0, 1, \'f\'),
            ....:              (0, 1, \'f\'), (2, 1, \'g\'), (2, 2, \'h\')])
            sage: GP = d.graphplot(vertex_size=100, edge_labels=True,
            ....:                  color_by_label=True, edge_style=\'dashed\')
            sage: GP.set_edges(edge_style=\'solid\')
            sage: GP.plot()
            Graphics object consisting of 24 graphics primitives

        .. PLOT::

            d = DiGraph(loops=True, multiedges=True, sparse=True)
            d.add_edges([(0, 0, \'a\'), (0, 0, \'b\'), (0, 1, \'c\'),
                         (0, 1, \'d\'), (0, 1, \'e\'), (0, 1, \'f\'),
                         (0, 1, \'f\'), (2, 1, \'g\'), (2, 2, \'h\')])
            GP = d.graphplot(vertex_size=100, edge_labels=True,
                             color_by_label=True, edge_style=\'dashed\')
            GP.set_edges(edge_style=\'solid\')
            sphinx_plot(GP)

        ::

            sage: GP.set_edges(edge_color=\'black\')
            sage: GP.plot()
            Graphics object consisting of 24 graphics primitives

        .. PLOT::

            d = DiGraph(loops=True, multiedges=True, sparse=True)
            d.add_edges([(0, 0, \'a\'), (0, 0, \'b\'), (0, 1, \'c\'),
                         (0, 1, \'d\'), (0, 1, \'e\'), (0, 1, \'f\'),
                         (0, 1, \'f\'), (2, 1, \'g\'), (2, 2, \'h\')])
            GP = d.graphplot(vertex_size=100, edge_labels=True,
                             color_by_label=True, edge_style=\'dashed\')
            GP.set_edges(edge_style=\'solid\')
            GP.set_edges(edge_color=\'black\')
            sphinx_plot(GP)

        TESTS::

            sage: G = Graph("Fooba")
            sage: G.show(edge_colors={\'red\':[(3, 6), (2, 5)]})

        Check default edge labels are pretty close to halfway between
        the vertices in some cases where they weren\'t due to Python 2
        truncating division (:issue:`10124`)::

            sage: test_graphs = graphs.FruchtGraph(), graphs.BullGraph()
            sage: tol = 0.001
            sage: for G in test_graphs:
            ....:     E = G.edges(sort=True)
            ....:     for e0, e1, elab in E:
            ....:         G.set_edge_label(e0, e1, \'%d %d\' % (e0, e1))
            ....:     gp = G.graphplot(save_pos=True, edge_labels=True)
            ....:     vx = gp._plot_components[\'vertices\'][0].xdata
            ....:     vy = gp._plot_components[\'vertices\'][0].ydata
            ....:     for elab in gp._plot_components[\'edge_labels\']:
            ....:         textobj = elab[0]
            ....:         x, y, s = textobj.x, textobj.y, textobj.string
            ....:         v0, v1 = map(int, s.split())
            ....:         m = sum(vector((vx[v], vy[v])) for v in (v0, v1))/2
            ....:         assert (vector((x, y)) - m).norm() < tol

        Issue :issue:`24051` is fixed::

            sage: G = Graph([(0, 1), (0, 1)], multiedges=True)
            sage: G.plot(edge_colors={"red": [(1, 0)]})
            Graphics object consisting of 5 graphics primitives

        Issue :issue:`31542` is fixed::

            sage: s = \'ABCCCCDABCDABCDA\'
            sage: g = DiGraph({}, loops=True, multiedges=True)
            sage: for a, b in [(s[i], u) for i, u in enumerate(s[1:])]:
            ....:     g.add_edge(a, b, b)
            sage: g.plot(color_by_label=True, layout=\'circular\')
            Graphics object consisting of 23 graphics primitives
        '''
    def show(self, **kwds) -> None:
        """
        Show the (di)graph associated with this ``GraphPlot`` object.

        INPUT:

        This method accepts all parameters of
        :meth:`sage.plot.graphics.Graphics.show`.

        .. NOTE::

            - See :mod:`the module's documentation <sage.graphs.graph_plot>`
              for information on default values of this method.

            - Any options not used by plot will be passed on to the
              :meth:`~sage.plot.graphics.Graphics.show` method.

        EXAMPLES::

            sage: C = graphs.CubeGraph(8)
            sage: P = C.graphplot(vertex_labels=False, vertex_size=0,
            ....:                 graph_border=True)
            sage: P.show()

        .. PLOT::

            C = graphs.CubeGraph(8)
            P = C.graphplot(vertex_labels=False, vertex_size=0,
                            graph_border=True)
            sphinx_plot(P)
        """
    def plot(self, **kwds):
        '''
        Return a graphics object representing the (di)graph.

        INPUT:

        The options accepted by this method are to be found in the
        documentation of the :mod:`sage.graphs.graph_plot` module,
        and the :meth:`~sage.plot.graphics.Graphics.show` method.

        .. NOTE::

            See :mod:`the module\'s documentation <sage.graphs.graph_plot>` for
            information on default values of this method.

        We can specify some pretty precise plotting of familiar graphs::

            sage: from math import sin, cos, pi
            sage: P = graphs.PetersenGraph()
            sage: d = {\'#FF0000\': [0, 5], \'#FF9900\': [1, 6], \'#FFFF00\': [2, 7],
            ....:      \'#00FF00\': [3, 8], \'#0000FF\': [4,9]}
            sage: pos_dict = {}
            sage: for i in range(5):
            ....:  x = float(cos(pi/2 + ((2*pi)/5)*i))
            ....:  y = float(sin(pi/2 + ((2*pi)/5)*i))
            ....:  pos_dict[i] = [x,y]
            ...
            sage: for i in range(5, 10):
            ....:  x = float(0.5*cos(pi/2 + ((2*pi)/5)*i))
            ....:  y = float(0.5*sin(pi/2 + ((2*pi)/5)*i))
            ....:  pos_dict[i] = [x,y]
            ...
            sage: pl = P.graphplot(pos=pos_dict, vertex_colors=d)
            sage: pl.show()

        .. PLOT::

            from math import sin, cos, pi
            P = graphs.PetersenGraph()
            d = {\'#FF0000\': [0, 5], \'#FF9900\': [1, 6], \'#FFFF00\': [2, 7],
                 \'#00FF00\': [3, 8], \'#0000FF\': [4,9]}
            pos_dict = {}
            for i in range(5):
                x = float(cos(pi/2 + ((2*pi)/5)*i))
                y = float(sin(pi/2 + ((2*pi)/5)*i))
                pos_dict[i] = [x,y]

            for i in range(5, 10):
                x = float(0.5*cos(pi/2 + ((2*pi)/5)*i))
                y = float(0.5*sin(pi/2 + ((2*pi)/5)*i))
                pos_dict[i] = [x,y]

            pl = P.graphplot(pos=pos_dict, vertex_colors=d)
            sphinx_plot(pl)

        Here are some more common graphs with typical options::

            sage: C = graphs.CubeGraph(8)
            sage: P = C.graphplot(vertex_labels=False, vertex_size=0,
            ....:                 graph_border=True)
            sage: P.show()

        .. PLOT::

            C = graphs.CubeGraph(8)
            P = C.graphplot(vertex_labels=False, vertex_size=0,
                            graph_border=True)
            sphinx_plot(P)

        ::

            sage: G = graphs.HeawoodGraph().copy(sparse=True)
            sage: for u, v, l in G.edges(sort=True):
            ....:     G.set_edge_label(u, v, f\'({u},{v})\')
            sage: G.graphplot(edge_labels=True).show()

        .. PLOT::

            G = graphs.HeawoodGraph().copy(sparse=True)
            for u, v, l in G.edges(sort=True):
                G.set_edge_label(u, v, f\'({u},{v})\')
            sphinx_plot(G.graphplot(edge_labels=True))

        The options for plotting also work with directed graphs::

            sage: D = DiGraph({
            ....:     0: [1, 10, 19], 1: [8, 2], 2: [3, 6], 3: [19, 4],
            ....:     4: [17, 5], 5: [6, 15], 6: [7], 7: [8, 14], 8: [9],
            ....:     9: [10, 13], 10: [11], 11: [12, 18], 12: [16, 13],
            ....:     13: [14], 14: [15], 15: [16], 16: [17], 17: [18],
            ....:     18: [19], 19: []})
            sage: for u, v, l in D.edges(sort=True):
            ....:     D.set_edge_label(u, v, f\'({u},{v})\')
            sage: D.graphplot(edge_labels=True, layout=\'circular\').show()

        .. PLOT::

            D = DiGraph({
                0: [1, 10, 19], 1: [8, 2], 2: [3, 6], 3: [19, 4],
                4: [17, 5], 5: [6, 15], 6: [7], 7: [8, 14], 8: [9],
                9: [10, 13], 10: [11], 11: [12, 18], 12: [16, 13],
                13: [14], 14: [15], 15: [16], 16: [17], 17: [18],
                18: [19], 19: []})
            for u, v, l in D.edges(sort=True):
                D.set_edge_label(u, v, f\'({u},{v})\')
            sphinx_plot(D.graphplot(edge_labels=True, layout=\'circular\'))

        For graphs with ``circular`` layouts, one may shift the vertex labels by
        specifying coordinates to shift by::

            sage: D = DiGraph({
            ....:     0: [1, 10, 19], 1: [8, 2], 2: [3, 6], 3: [19, 4],
            ....:     4: [17, 5], 5: [6, 15], 6: [7], 7: [8, 14], 8: [9],
            ....:     9: [10, 13], 10: [11], 11: [12, 18], 12: [16, 13],
            ....:     13: [14], 14: [15], 15: [16], 16: [17], 17: [18],
            ....:     18: [19], 19: []})
            sage: for u, v, l in D.edges(sort=True):
            ....:     D.set_edge_label(u, v, f\'({u},{v})\')
            sage: D.graphplot(edge_labels=True, layout=\'circular\', vertex_label_shift=(15,10)).show()

        .. PLOT::

            D = DiGraph({
                0: [1, 10, 19], 1: [8, 2], 2: [3, 6], 3: [19, 4],
                4: [17, 5], 5: [6, 15], 6: [7], 7: [8, 14], 8: [9],
                9: [10, 13], 10: [11], 11: [12, 18], 12: [16, 13],
                13: [14], 14: [15], 15: [16], 16: [17], 17: [18],
                18: [19], 19: []})
            for u, v, l in D.edges(sort=True):
                D.set_edge_label(u, v, f\'({u},{v})\')
            sphinx_plot(D.graphplot(edge_labels=True, layout=\'circular\', vertex_label_shift=(15,10)))

        This example shows off the coloring of edges::

            sage: from sage.plot.colors import rainbow
            sage: C = graphs.CubeGraph(5)
            sage: R = rainbow(5)
            sage: edge_colors = {}
            sage: for i in range(5):
            ....:     edge_colors[R[i]] = []
            sage: for u, v, l in C.edges(sort=True):
            ....:     for i in range(5):
            ....:         if u[i] != v[i]:
            ....:             edge_colors[R[i]].append((u, v, l))
            sage: C.graphplot(vertex_labels=False, vertex_size=0,
            ....:             edge_colors=edge_colors).show()

        .. PLOT::

            from sage.plot.colors import rainbow
            C = graphs.CubeGraph(5)
            R = rainbow(5)
            edge_colors = {}
            for i in range(5):
                edge_colors[R[i]] = []
            for u, v, l in C.edges(sort=True):
                for i in range(5):
                    if u[i] != v[i]:
                        edge_colors[R[i]].append((u, v, l))
            sphinx_plot(C.graphplot(vertex_labels=False, vertex_size=0,
                                    edge_colors=edge_colors))

        With the ``partition`` option, we can separate out same-color groups
        of vertices::

            sage: D = graphs.DodecahedralGraph()
            sage: Pi = [[6, 5, 15, 14, 7], [16, 13, 8, 2, 4],
            ....:       [12, 17, 9, 3, 1], [0, 19, 18, 10, 11]]
            sage: D.show(partition=Pi)

        .. PLOT::

            D = graphs.DodecahedralGraph()
            Pi = [[6, 5, 15, 14, 7], [16, 13, 8, 2, 4],
                  [12, 17, 9, 3, 1], [0, 19, 18, 10, 11]]
            sphinx_plot(D.plot(partition=Pi))

        Loops are also plotted correctly::

            sage: G = graphs.PetersenGraph()
            sage: G.allow_loops(True)
            sage: G.add_edge(0,0)
            sage: G.show()

        .. PLOT::

            G = graphs.PetersenGraph()
            G.allow_loops(True)
            G.add_edge(0,0)
            sphinx_plot(G)

        ::

            sage: D = DiGraph({0:[0,1], 1:[2], 2:[3]}, loops=True)
            sage: D.show()
            sage: D.show(edge_colors={(0, 1, 0): [(0, 1, None), (1, 2, None)],
            ....:                     (0, 0, 0): [(2, 3, None)]})

        .. PLOT::

            D = DiGraph({0:[0,1], 1:[2], 2:[3]}, loops=True)
            P = D.plot(edge_colors={(0, 1, 0): [(0, 1, None), (1, 2, None)],
                                    (0, 0, 0): [(2, 3, None)]})
            sphinx_plot(P)

        More options::

            sage: pos = {0: [0.0, 1.5], 1: [-0.8, 0.3], 2: [-0.6, -0.8],
            ....:        3:[0.6, -0.8], 4:[0.8, 0.3]}
            sage: g = Graph({0: [1], 1: [2], 2: [3], 3: [4], 4: [0]})
            sage: g.graphplot(pos=pos, layout=\'spring\', iterations=0).plot()
            Graphics object consisting of 11 graphics primitives

        .. PLOT::

            pos = {0: [0.0, 1.5], 1: [-0.8, 0.3], 2: [-0.6, -0.8],
                   3: [0.6, -0.8], 4:[0.8, 0.3]}
            g = Graph({0: [1], 1: [2], 2: [3], 3: [4], 4: [0]})
            P = g.graphplot(pos=pos, layout=\'spring\', iterations=0).plot()
            sphinx_plot(P)

        ::

            sage: D = graphs.CubeGraph(3)
            sage: D.graphplot(layout=\'planar\').plot()
            Graphics object consisting of 21 graphics primitives

        .. PLOT::

            D = graphs.CubeGraph(3)
            sphinx_plot(D.graphplot(layout=\'planar\'))

        ::

            sage: G = Graph()
            sage: P = G.graphplot().plot()
            sage: P.axes()
            False
            sage: G = DiGraph()
            sage: P = G.graphplot().plot()
            sage: P.axes()
            False

        We can plot multiple graphs::

            sage: T = list(graphs.trees(7))
            sage: t = T[3]
            sage: t.graphplot(heights={0: [0], 1: [4, 5, 1],
            ....:                      2: [2], 3: [3, 6]}
            ....:            ).plot()
            Graphics object consisting of 14 graphics primitives

        .. PLOT::

            T = list(graphs.trees(7))
            t = T[3]
            sphinx_plot(t.graphplot(heights={0: [0], 1: [4, 5, 1],
                                             2: [2], 3: [3, 6]}))

        ::

            sage: T = list(graphs.trees(7))
            sage: t = T[3]
            sage: t.graphplot(heights={0: [0], 1: [4, 5, 1],
            ....:                      2: [2], 3: [3, 6]}
            ....:            ).plot()
            Graphics object consisting of 14 graphics primitives

        .. PLOT::

            T = list(graphs.trees(7))
            t = T[3]
            sphinx_plot(t.graphplot(heights={0: [0], 1: [4, 5, 1],
                                             2: [2], 3: [3, 6]}))

        ::

            sage: t.set_edge_label(0, 1, -7)
            sage: t.set_edge_label(0, 5, 3)
            sage: t.set_edge_label(0, 5, 99)
            sage: t.set_edge_label(1, 2, 1000)
            sage: t.set_edge_label(3, 2, \'spam\')
            sage: t.set_edge_label(2, 6, 3/2)
            sage: t.set_edge_label(0, 4, 66)
            sage: t.graphplot(heights={0: [0], 1: [4, 5, 1],
            ....:                      2: [2], 3: [3, 6]},
            ....:             edge_labels=True
            ....:            ).plot()
            Graphics object consisting of 20 graphics primitives

        .. PLOT::

            T = list(graphs.trees(7))
            t = T[3]
            t.set_edge_label(0, 1, -7)
            t.set_edge_label(0, 5, 3)
            t.set_edge_label(0, 5, 99)
            t.set_edge_label(1, 2, 1000)
            t.set_edge_label(3, 2, \'spam\')
            t.set_edge_label(2, 6, 3/2)
            t.set_edge_label(0, 4, 66)
            sphinx_plot(t.graphplot(heights={0: [0], 1: [4, 5, 1],
                                             2: [2], 3: [3, 6]},
                                    edge_labels=True))

        ::

            sage: T = list(graphs.trees(7))
            sage: t = T[3]
            sage: t.graphplot(layout=\'tree\').show()

        .. PLOT::

            T = list(graphs.trees(7))
            t = T[3]
            sphinx_plot(t.graphplot(layout=\'tree\'))

        The tree layout is also useful::

            sage: t = DiGraph(\'JCC???@A??GO??CO??GO??\')
            sage: t.graphplot(layout=\'tree\', tree_root=0,
            ....:             tree_orientation="up"
            ....:            ).show()

        .. PLOT::

            t = DiGraph(\'JCC???@A??GO??CO??GO??\')
            sphinx_plot(t.graphplot(layout=\'tree\', tree_root=0,
                                    tree_orientation=\'up\'))

        More examples::

            sage: D = DiGraph({0:[1,2,3], 2:[1,4], 3:[0]})
            sage: D.graphplot().show()

        .. PLOT::

            D = DiGraph({0:[1,2,3], 2:[1,4], 3:[0]})
            sphinx_plot(D.graphplot())

        ::

            sage: D = DiGraph({0:[1,2,3], 2:[1,4], 3:[0]})
            sage: D.graphplot(label_fontsize=20, arrowsize=10).show()

        .. PLOT::

            D = DiGraph({0:[1,2,3], 2:[1,4], 3:[0]})
            sphinx_plot(D.graphplot(label_fontsize=20, arrowsize=10))


        ::

            sage: D = DiGraph(multiedges=True, sparse=True)
            sage: for i in range(5):
            ....:   D.add_edge((i, i + 1, \'a\'))
            ....:   D.add_edge((i, i - 1, \'b\'))
            sage: D.graphplot(edge_labels=True,
            ....:             edge_colors=D._color_by_label()
            ....:            ).plot()
            Graphics object consisting of 34 graphics primitives

        .. PLOT::

            D = DiGraph(multiedges=True, sparse=True)
            for i in range(5):
                 D.add_edge((i, i + 1, \'a\'))
                 D.add_edge((i, i - 1, \'b\'))
            sphinx_plot(D.graphplot(edge_labels=True,
                                    edge_colors=D._color_by_label()))

        ::

            sage: g = Graph({}, loops=True, multiedges=True, sparse=True)
            sage: g.add_edges([(0, 0, \'a\'), (0, 0, \'b\'), (0, 1, \'c\'),
            ....:              (0, 1, \'d\'), (0, 1, \'e\'), (0, 1, \'f\'),
            ....:              (0, 1, \'f\'), (2, 1, \'g\'), (2, 2, \'h\')])
            sage: g.graphplot(edge_labels=True,
            ....:             color_by_label=True,
            ....:             edge_style=\'dashed\'
            ....:            ).plot()
            Graphics object consisting of 22 graphics primitives

        .. PLOT::

            g = Graph({}, loops=True, multiedges=True, sparse=True)
            g.add_edges([(0, 0, \'a\'), (0, 0, \'b\'), (0, 1, \'c\'),
                         (0, 1, \'d\'), (0, 1, \'e\'), (0, 1, \'f\'),
                         (0, 1, \'f\'), (2, 1, \'g\'), (2, 2, \'h\')])
            sphinx_plot(g.graphplot(edge_labels=True,
                                    color_by_label=True,
                                    edge_style=\'dashed\'))

        The ``edge_style`` option may be provided in the short format too::


            sage: g.graphplot(edge_labels=True,
            ....:             color_by_label=True,
            ....:             edge_style=\'--\'
            ....:            ).plot()
            Graphics object consisting of 22 graphics primitives

        The ``edge_styles`` option may be provided if you need only certain edges
        to have certain styles::

            sage: g = Graph(loops=True, multiedges=True, sparse=True)
            sage: g.add_edges([(0, 0, \'a\'), (0, 0, \'b\'), (0, 1, \'c\'),
            ....:              (0, 1, \'d\'), (0, 1, \'e\'), (0, 1, \'f\'),
            ....:              (0, 1, \'f\'), (2, 1, \'g\'), (2, 2, \'h\')])
            sage: GP = g.graphplot(vertex_size=100, edge_labels=True,
            ....:                  color_by_label=True, edge_style=\'dashed\')
            sage: GP.set_edges(edge_styles={\'a\':\'dashed\', \'g\':\'dotted\'})
            sage: GP.plot()
            Graphics object consisting of 22 graphics primitives

        .. PLOT::

            g = Graph(loops=True, multiedges=True, sparse=True)
            g.add_edges([(0, 0, \'a\'), (0, 0, \'b\'), (0, 1, \'c\'),
                         (0, 1, \'d\'), (0, 1, \'e\'), (0, 1, \'f\'),
                         (0, 1, \'f\'), (2, 1, \'g\'), (2, 2, \'h\')])
            GP = g.graphplot(vertex_size=100, edge_labels=True,
                             color_by_label=True, edge_style=\'dashed\')
            GP.set_edges(edge_style=\'solid\')
            GP.set_edges(edge_color=\'black\')
            GP.set_edges(edge_styles={\'a\':\'dashed\', \'g\':\'dotted\'})
            sphinx_plot(GP)

        ::

            sage: g = Graph(loops=True, multiedges=True, sparse=True)
            sage: g.add_edges([(0, 0, \'a\'), (0, 0, \'b\'), (0, 1, \'c\'),
            ....:              (0, 1, \'d\'), (0, 1, \'e\'), (0, 1, \'f\'),
            ....:              (0, 1, \'f\'), (2, 1, \'g\'), (2, 2, \'h\')])
            sage: GP = g.graphplot(vertex_size=100, edge_labels=True,
            ....:                  color_by_label=True, edge_thickness=3)
            sage: GP.set_edges(edge_thicknesses={\'a\':1, \'g\':5})
            sage: GP.plot()
            Graphics object consisting of 22 graphics primitives

        .. PLOT::

            g = Graph(loops=True, multiedges=True, sparse=True)
            g.add_edges([(0, 0, \'a\'), (0, 0, \'b\'), (0, 1, \'c\'),
                         (0, 1, \'d\'), (0, 1, \'e\'), (0, 1, \'f\'),
                         (0, 1, \'f\'), (2, 1, \'g\'), (2, 2, \'h\')])
            GP = g.graphplot(vertex_size=100, edge_labels=True,
                             color_by_label=True, edge_thickness=3)
            GP.set_edges(edge_style=\'solid\')
            GP.set_edges(edge_color=\'black\')
            GP.set_edges(edge_thicknesses={\'a\':1, \'g\':5})
            sphinx_plot(GP)

        TESTS:

        Make sure that show options work with plot also::

            sage: g = Graph({})
            sage: g.plot(title=\'empty graph\', axes=True)
            Graphics object consisting of 0 graphics primitives

        Check for invalid inputs::

            sage: p = graphs.PetersenGraph().plot(egabrag=\'garbage\')
            Traceback (most recent call last):
            ...
            ValueError: invalid input \'egabrag=garbage\'

        Make sure that no graphics primitive is clipped::

            sage: tadpole = Graph({0: [0, 1]}).plot()
            sage: bbox = tadpole.get_minmax_data()
            sage: for part in tadpole:
            ....:      part_bbox = part.get_minmax_data()
            ....:      assert (bbox[\'xmin\'] <= part_bbox[\'xmin\']
            ....:              <= part_bbox[\'xmax\'] <= bbox[\'xmax\'])
            ....:      assert (bbox[\'ymin\'] <= part_bbox[\'ymin\']
            ....:              <= part_bbox[\'ymax\'] <= bbox[\'ymax\'])

        Check that one can plot immutable graphs (:issue:`17340`)::

            sage: Graph({0: [0]}, immutable=True).plot()
            Graphics object consisting of 3 graphics primitives
        '''
    def layout_tree(self, root, orientation):
        '''
        Compute a nice layout of a tree.

        INPUT:

        - ``root`` -- the root vertex

        - ``orientation`` -- whether to place the root at the top or at the
          bottom:

          * ``orientation="down"`` -- children are placed below their parent
          * ``orientation="top"`` -- children are placed above their parent

        EXAMPLES::

            sage: from sage.graphs.graph_plot import GraphPlot
            sage: G = graphs.HoffmanSingletonGraph()
            sage: T = Graph()
            sage: T.add_edges(G.min_spanning_tree(starting_vertex=0))
            sage: T.show(layout=\'tree\', tree_root=0)  # indirect doctest
        '''
