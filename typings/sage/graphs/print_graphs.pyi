def print_header_ps(s):
    """
    Give the header for a postscript file.

    EXAMPLES::

        sage: from sage.graphs.print_graphs import print_header_ps
        sage: print(print_header_ps(''))
        %% --- Auto-generated PostScript ---
        %% Generated on:
        %%...
    """
def print_header_eps(s, xmin, ymin, xmax, ymax):
    """
    Give the header for an encapsulated postscript file.

    EXAMPLES::

        sage: from sage.graphs.print_graphs import print_header_eps
        sage: print(print_header_eps('',0,0,1,1))
        %!PS-Adobe-3.0 EPSF-3.0
        %%BoundingBox: 0 0 1 1
    """
def print_functions(s):
    """
    Define edge and point drawing functions.

    EXAMPLES::

        sage: from sage.graphs.print_graphs import print_functions
        sage: print(print_functions(''))
        /point %% input: x y
        { moveto
          gsave
          currentpoint translate
          0 0 2 0 360 arc
          fill
          grestore
          } def
        /edge %% input: x1 y1 x2 y2
        { moveto
          lineto
          stroke
          } def
    """
def print_graph_ps(vert_ls, edge_iter, pos_dict):
    """
    Give postscript text for drawing a graph.

    EXAMPLES::

        sage: from sage.graphs.print_graphs import print_graph_ps
        sage: P = graphs.PetersenGraph()
        sage: print(print_graph_ps(P.vertices(sort=True), P.edges(sort=True), sage.graphs.generic_graph_pyx.spring_layout_fast(P)))
        %% --- Auto-generated PostScript ---
        %% Generated on:
        %%...
        /point %% input: x y
        { moveto
          gsave
          currentpoint translate
          0 0 2 0 360 arc
          fill
          grestore
          } def
        /edge %% input: x1 y1 x2 y2
        { moveto
          lineto
          stroke
          } def
        ... point
        ...
        ... point
        ... edge
        ...
        ... edge
    """
def print_graph_eps(vert_ls, edge_iter, pos_dict):
    """
    Give postscript text for drawing a graph.

    EXAMPLES::

        sage: from sage.graphs.print_graphs import print_graph_eps
        sage: P = graphs.PetersenGraph()
        sage: print(print_graph_eps(P.vertices(sort=True), P.edges(sort=True), sage.graphs.generic_graph_pyx.spring_layout_fast(P)))
        %!PS-Adobe-3.0 EPSF-3.0
        %%BoundingBox: 0 0 100 100
        /point %% input: x y
        { moveto
          gsave
          currentpoint translate
          0 0 2 0 360 arc
          fill
          grestore
          } def
        /edge %% input: x1 y1 x2 y2
        { moveto
          lineto
          stroke
          } def
        ... point
        ...
        ... point
        ... edge
        ...
        ... edge
    """
