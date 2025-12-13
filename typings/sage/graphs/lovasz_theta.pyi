def lovasz_theta(graph):
    """
    Return the value of Lovász theta-function of graph.

    For a graph `G` this function is denoted by `\\theta(G)`, and it can be
    computed in polynomial time. Mathematically, its most important property is
    the following:

    .. MATH::

        \\alpha(G)\\leq\\theta(G)\\leq\\chi(\\overline{G})

    with `\\alpha(G)` and `\\chi(\\overline{G})` being, respectively, the maximum
    size of an :meth:`independent set <sage.graphs.graph.Graph.independent_set>`
    set of `G` and the :meth:`chromatic number
    <sage.graphs.graph.Graph.chromatic_number>` of the :meth:`complement
    <sage.graphs.generic_graph.GenericGraph.complement>` `\\overline{G}` of `G`.

    For more information, see the :wikipedia:`Lovász_number`.

    .. NOTE::

        - Implemented for undirected graphs only. Use ``to_undirected``
          to convert a digraph to an undirected graph.

        - This function requires the optional package ``csdp``, which you can
          install with ``sage -i csdp``.

    EXAMPLES::

          sage: C = graphs.PetersenGraph()
          sage: C.lovasz_theta()                             # optional - csdp
          4.0
          sage: graphs.CycleGraph(5).lovasz_theta()          # optional - csdp
          2.236068

    TESTS::

        sage: g = Graph()
        sage: g.lovasz_theta() # indirect doctest
        0
    """
