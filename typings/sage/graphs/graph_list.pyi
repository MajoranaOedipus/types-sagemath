from sage.misc.misc import try_read as try_read

def from_whatever(data, immutable: bool = False):
    """
    Return a list of Sage Graphs, given a list of whatever kind of data.

    INPUT:

    - ``data`` -- can be a string, a list/iterable of strings, or a readable
      file-like object

    - ``immutable`` -- boolean (default: ``False``); whether to return immutable
      or mutable graphs

    EXAMPLES::

        sage: l = ['N@@?N@UGAGG?gGlKCMO', ':P_`cBaC_ACd`C_@BC`ABDHaEH_@BF_@CHIK_@BCEHKL_BIKM_BFGHI']
        sage: graphs_list.from_whatever(l)
        [Graph on 15 vertices, Looped multi-graph on 17 vertices]
        sage: graphs_list.from_whatever('\\n'.join(l))
        [Graph on 15 vertices, Looped multi-graph on 17 vertices]

    This example happens to be a mix a sparse and non-sparse graphs, so we don't
    explicitly put a ``.g6`` or ``.s6`` extension, which implies just one or the
    other::

        sage: filename = tmp_filename()
        sage: with open(filename, 'w') as fobj:
        ....:     _ = fobj.write('\\n'.join(l))
        sage: with open(filename) as fobj:
        ....:     graphs_list.from_whatever(fobj)
        [Graph on 15 vertices, Looped multi-graph on 17 vertices]

    Check the behaviour of parameter ``immutable``::

        sage: with open(filename) as fobj:
        ....:     any(g.is_immutable() for g in graphs_list.from_whatever(fobj))
        False
        sage: with open(filename) as fobj:
        ....:     all(g.is_immutable() for g in graphs_list.from_whatever(fobj, immutable=True))
        True
    """
def from_graph6(data, immutable: bool = False):
    """
    Return a list of Sage Graphs, given a list of graph6 data.

    INPUT:

    - ``data`` -- can be a string, a list of strings, or a file stream

    - ``immutable`` -- boolean (default: ``False``); whether to return immutable
      or mutable graphs

    EXAMPLES::

        sage: l = ['N@@?N@UGAGG?gGlKCMO', 'XsGGWOW?CC?C@HQKHqOjYKC_uHWGX?P?~TqIKA`OA@SAOEcEA??']
        sage: graphs_list.from_graph6(l)
        [Graph on 15 vertices, Graph on 25 vertices]

    Check the behaviour of parameter ``immutable``::

        sage: any(g.is_immutable() for g in graphs_list.from_graph6(l))
        False
        sage: all(g.is_immutable() for g in graphs_list.from_graph6(l, immutable=True))
        True
    """
def from_sparse6(data, immutable: bool = False):
    """
    Return a list of Sage Graphs, given a list of sparse6 data.

    INPUT:

    - ``data`` -- can be a string, a list of strings, or a file stream

    - ``immutable`` -- boolean (default: ``False``); whether to return immutable
      or mutable graphs

    EXAMPLES::

        sage: g1 = ':P_`cBaC_ACd`C_@BC`ABDHaEH_@BF_@CHIK_@BCEHKL_BIKM_BFGHI'
        sage: g2 = ':f`??KO?B_OOSCGE_?OWONDBO?GOJBDO?_SSJdApcOIG`?og_UKEbg?_SKF'
        sage: g2 += 'q@[CCBA`p?oYMFp@gw]Qaa@xEMHDb@hMCBCbQ@ECHEcAKKQKFPOwo[PIDQ'
        sage: g2 += '{KIHEcQPOkVKEW_WMNKqPWwcRKOOWSKIGCqhWt??___WMJFCahWzEBa`xO'
        sage: g2 += 'u[MpPPKqYNoOOOKHHDBPs|??__gWMKEcAHKgTLErqA?A@a@G{kVLErs?GD'
        sage: g2 += 'BA@XCs\\NggWSOJIDbHh@?A@aF'
        sage: graphs_list.from_sparse6([g1, g2])
        [Looped multi-graph on 17 vertices, Looped multi-graph on 39 vertices]

    Check the behaviour of parameter ``immutable``::

        sage: any(g.is_immutable() for g in graphs_list.from_sparse6([g1, g2]))
        False
        sage: all(g.is_immutable() for g in graphs_list.from_sparse6([g1, g2], immutable=True))
        True
    """
def to_graph6(graphs, file=None, output_list: bool = False):
    """
    Convert a list of Sage graphs to a single string of graph6 graphs.

    If ``file`` is specified, then the string will be written quietly to the
    file.  If ``output_list`` is ``True``, then a list of strings will be
    returned, one string per graph.

    INPUT:

    - ``graphs`` -- a Python list of Sage Graphs

    - ``file`` -- (optional) a file stream to write to (must be in 'w' mode)

    - ``output_list`` -- boolean (default: ``False``); whether to return a
      string (when set to ``True``) or a list of strings. This parameter is
      ignored if file gets specified

    EXAMPLES::

        sage: l = [graphs.DodecahedralGraph(), graphs.PetersenGraph()]
        sage: graphs_list.to_graph6(l)
        'ShCHGD@?K?_@?@?C_GGG@??cG?G?GK_?C\\nIheA@GUAo\\n'
    """
def to_sparse6(graphs, file=None, output_list: bool = False):
    """
    Convert a list of Sage graphs to a single string of sparse6 graphs.

    If ``file`` is specified, then the string will be written quietly to the
    file.  If ``output_list`` is ``True``, then a list of strings will be
    returned, one string per graph.

    INPUT:

    - ``graphs`` -- a Python list of Sage Graphs

    - ``file`` -- (optional) a file stream to write to (must be in 'w' mode)

    - ``output_list`` -- boolean (default: ``False``); whether to return a
      string (when set to ``True``) or a list of strings. This parameter is
      ignored if file gets specified

    EXAMPLES::

        sage: l = [graphs.DodecahedralGraph(), graphs.PetersenGraph()]
        sage: graphs_list.to_sparse6(l)
        ':S_`abcaDe`Fg_HijhKfLdMkNcOjP_BQ\\n:I`ES@obGkqegW~\\n'
    """
def to_graphics_array(graph_list, **kwds):
    """
    Draw all graphs in a graphics array.

    INPUT:

    - ``graph_list`` -- a Python list of Sage Graphs

    GRAPH PLOTTING:

    Defaults to circular layout for graphs. This allows for a nicer display in a
    small area and takes much less time to compute than the spring- layout
    algorithm for many graphs.

    EXAMPLES::

        sage: glist = []
        sage: for i in range(999):
        ....:     glist.append(graphs.RandomGNP(6, .45))
        sage: garray = graphs_list.to_graphics_array(glist)                             # needs sage.plot
        sage: garray.nrows(), garray.ncols()                                            # needs sage.plot
        (250, 4)

    See the .plot() or .show() documentation for an individual graph for
    options, all of which are available from :func:`to_graphics_array`::

        sage: glist = []
        sage: for _ in range(10):                                                       # needs networkx
        ....:     glist.append(graphs.RandomLobster(41, .3, .4))
        sage: graphs_list.to_graphics_array(glist, layout='spring', vertex_size=20)     # needs networkx sage.plot
        Graphics Array of size 3 x 4
    """
def show_graphs(graph_list, **kwds) -> None:
    """
    Show a maximum of 20 graphs from ``graph_list`` in a sage graphics array.

    If more than 20 graphs are given in the list argument, then it will display
    one graphics array after another with each containing at most 20 graphs.

    Note that to save the image output from the notebook, you must save each
    graphics array individually. (There will be a small space between graphics
    arrays).

    INPUT:

    - ``graph_list`` -- a Python list of Sage Graphs

    GRAPH PLOTTING: Defaults to circular layout for graphs. This allows for a
    nicer display in a small area and takes much less time to compute than the
    spring-layout algorithm for many graphs.

    EXAMPLES: Create a list of graphs::

        sage: glist = []
        sage: glist.append(graphs.CompleteGraph(6))
        sage: glist.append(graphs.CompleteBipartiteGraph(4, 5))
        sage: glist.append(graphs.BarbellGraph(7, 4))
        sage: glist.append(graphs.CycleGraph(15))
        sage: glist.append(graphs.DiamondGraph())
        sage: glist.append(graphs.GemGraph())
        sage: glist.append(graphs.DartGraph())
        sage: glist.append(graphs.ForkGraph())
        sage: glist.append(graphs.HouseGraph())
        sage: glist.append(graphs.HouseXGraph())
        sage: glist.append(graphs.KrackhardtKiteGraph())
        sage: glist.append(graphs.LadderGraph(5))
        sage: glist.append(graphs.LollipopGraph(5, 6))
        sage: glist.append(graphs.PathGraph(15))
        sage: glist.append(graphs.PetersenGraph())
        sage: glist.append(graphs.StarGraph(17))
        sage: glist.append(graphs.WheelGraph(9))

    Check that length is <= 20::

        sage: len(glist)
        17

    Show the graphs in a graphics array::

        sage: graphs_list.show_graphs(glist)                                            # needs sage.plot

    Example where more than one graphics array is used::

        sage: gq = GraphQuery(display_cols=['graph6'], num_vertices=5)
        sage: g = gq.get_graphs_list()
        sage: len(g)
        34
        sage: graphs_list.show_graphs(g)                                                # needs sage.plot

    See the .plot() or .show() documentation for an individual graph for
    options, all of which are available from :func:`to_graphics_array`::

        sage: glist = []
        sage: for _ in range(10):                                                       # needs networkx
        ....:     glist.append(graphs.RandomLobster(41, .3, .4))
        sage: graphs_list.show_graphs(glist, layout='spring', vertex_size=20)           # needs sage.plot
    """
