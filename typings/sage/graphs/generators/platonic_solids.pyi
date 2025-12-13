from sage.graphs.graph import Graph as Graph

def TetrahedralGraph():
    """
    Return a tetrahedral graph (with 4 nodes).

    A tetrahedron is a 4-sided triangular pyramid. The tetrahedral graph
    corresponds to the connectivity of the vertices of the tetrahedron. This
    graph is equivalent to a wheel graph with 4 nodes and also a complete graph
    on four nodes. (See examples below).

    PLOTTING: The Tetrahedral graph should be viewed in 3 dimensions. We choose
    to use a planar embedding of the graph. We hope to add rotatable,
    3-dimensional viewing in the future. In such a case, a argument will be
    added to select the desired layout.

    EXAMPLES:

    Construct and show a Tetrahedral graph::

        sage: g = graphs.TetrahedralGraph()
        sage: g.show()                          # long time                             # needs sage.plot

    The following example requires networkx::

        sage: import networkx as NX                                                     # needs networkx

    Compare this Tetrahedral, Wheel(4), Complete(4), and the Tetrahedral plotted
    with the spring-layout algorithm below in a Sage graphics array::

        sage: # needs networkx sage.plot
        sage: tetra_pos = graphs.TetrahedralGraph()
        sage: tetra_spring = Graph(NX.tetrahedral_graph())
        sage: wheel = graphs.WheelGraph(4)
        sage: complete = graphs.CompleteGraph(4)
        sage: g = [tetra_pos, tetra_spring, wheel, complete]
        sage: j = []
        sage: for i in range(2):
        ....:     n = []
        ....:     for m in range(2):
        ....:         n.append(g[i + m].plot(vertex_size=50, vertex_labels=False))
        ....:     j.append(n)
        sage: G = graphics_array(j)
        sage: G.show()                          # long time
    """
def HexahedralGraph():
    """
    Return a hexahedral graph (with 8 nodes).

    A regular hexahedron is a 6-sided cube. The hexahedral graph corresponds to
    the connectivity of the vertices of the hexahedron. This graph is
    equivalent to a 3-cube.

    PLOTTING: The Hexahedral graph should be viewed in 3 dimensions. We choose
    to use a planar embedding of the graph. We hope to add rotatable,
    3-dimensional viewing in the future. In such a case, a argument will be
    added to select the desired layout.

    EXAMPLES:

    Construct and show a Hexahedral graph::

        sage: g = graphs.HexahedralGraph()
        sage: g.show()                          # long time                             # needs sage.plot

    Create several hexahedral graphs in a Sage graphics array. They will be
    drawn differently due to the use of the spring-layout algorithm::

        sage: # needs sage.plot
        sage: g = []
        sage: j = []
        sage: for i in range(9):
        ....:     k = graphs.HexahedralGraph()
        ....:     g.append(k)
        sage: for i in range(3):
        ....:     n = []
        ....:     for m in range(3):
        ....:         n.append(g[3*i + m].plot(vertex_size=50, vertex_labels=False))
        ....:     j.append(n)
        sage: G = graphics_array(j)
        sage: G.show()                          # long time
    """
def OctahedralGraph():
    """
    Return an Octahedral graph (with 6 nodes).

    The regular octahedron is an 8-sided polyhedron with triangular faces. The
    octahedral graph corresponds to the connectivity of the vertices of the
    octahedron. It is the line graph of the tetrahedral graph. The octahedral is
    symmetric, so the spring-layout algorithm will be very effective for
    display.

    PLOTTING: The Octahedral graph should be viewed in 3 dimensions. We choose
    to use a planar embedding of the graph. We hope to add rotatable,
    3-dimensional viewing in the future. In such a case, a argument will be
    added to select the desired layout.

    EXAMPLES:

    Construct and show an Octahedral graph::

        sage: g = graphs.OctahedralGraph()
        sage: g.show()                          # long time                             # needs sage.plot

    Create several octahedral graphs in a Sage graphics array They will be drawn
    differently due to the use of the spring-layout algorithm::

        sage: # needs sage.plot
        sage: g = []
        sage: j = []
        sage: for i in range(9):
        ....:     k = graphs.OctahedralGraph()
        ....:     g.append(k)
        sage: for i in range(3):
        ....:     n = []
        ....:     for m in range(3):
        ....:         n.append(g[3*i + m].plot(vertex_size=50, vertex_labels=False))
        ....:     j.append(n)
        sage: G = graphics_array(j)
        sage: G.show()                          # long time
    """
def IcosahedralGraph():
    """
    Return an Icosahedral graph (with 12 nodes).

    The regular icosahedron is a 20-sided triangular polyhedron. The icosahedral
    graph corresponds to the connectivity of the vertices of the icosahedron. It
    is dual to the dodecahedral graph. The icosahedron is symmetric, so the
    spring-layout algorithm will be very effective for display.

    PLOTTING: The Icosahedral graph should be viewed in 3 dimensions. We choose
    to use a planar embedding of the graph. We hope to add rotatable,
    3-dimensional viewing in the future. In such a case, a argument will be
    added to select the desired layout.

    EXAMPLES:

    Construct and show an Octahedral graph::

        sage: g = graphs.IcosahedralGraph()
        sage: g.show()                          # long time                             # needs sage.plot

    Create several icosahedral graphs in a Sage graphics array. They will be
    drawn differently due to the use of the spring-layout algorithm::

        sage: # needs sage.plot
        sage: g = []
        sage: j = []
        sage: for i in range(9):
        ....:     k = graphs.IcosahedralGraph()
        ....:     g.append(k)
        sage: for i in range(3):
        ....:     n = []
        ....:     for m in range(3):
        ....:         n.append(g[3*i + m].plot(vertex_size=50, vertex_labels=False))
        ....:     j.append(n)
        sage: G = graphics_array(j)
        sage: G.show()                          # long time
    """
def DodecahedralGraph():
    """
    Return a Dodecahedral graph (with 20 nodes).

    The dodecahedral graph is cubic symmetric, so the spring-layout algorithm
    will be very effective for display. It is dual to the icosahedral graph.

    PLOTTING: The Dodecahedral graph should be viewed in 3 dimensions. We
    choose to use a planar embedding of the graph. We hope to add rotatable,
    3-dimensional viewing in the future. In such a case, a argument will be
    added to select the desired layout.

    EXAMPLES:

    Construct and show a Dodecahedral graph::

        sage: g = graphs.DodecahedralGraph()
        sage: g.show()                          # long time                             # needs sage.plot

    Create several dodecahedral graphs in a Sage graphics array They will be
    drawn differently due to the use of the spring-layout algorithm::

        sage: # needs sage.plot
        sage: g = []
        sage: j = []
        sage: for i in range(9):
        ....:     k = graphs.DodecahedralGraph()
        ....:     g.append(k)
        sage: for i in range(3):
        ....:     n = []
        ....:     for m in range(3):
        ....:         n.append(g[3*i + m].plot(vertex_size=50, vertex_labels=False))
        ....:     j.append(n)
        sage: G = graphics_array(j)
        sage: G.show()                          # long time
    """
