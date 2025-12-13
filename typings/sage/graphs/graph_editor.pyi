from sage.features.phitigra import Phitigra as Phitigra
from sage.misc.lazy_import import lazy_import as lazy_import

def graph_editor(graph=None, **display_options):
    """
    Return a graph editor widget.

    The graph editor widget can be displayed with Jupyter or JupyterLab.
    It is provided by the ``phitigra`` optional package, see
    https://github.com/jfraymond/phitigra for details about the
    possible options (changing the width/height of the canvas, the
    default size and color of vertices, etc.).

    INPUT:

    - ``graph`` -- a graph to edit (default: ``None``)

    - ``display_options`` -- options for the widget

    EXAMPLES::

        sage: e = graph_editor()            # optional - phitigra
        sage: e.show()                      # not tested

    Opening an existing graph::

        sage: G = graphs.RandomGNP(10, 0.5)
        sage: e = graph_editor(G)           # optional - phitigra
        sage: e.show()                      # not tested

    Retrieving a copy of the drawn graph::

        sage: G = graphs.RandomGNP(10, 0.5)
        sage: e = graph_editor(G)           # optional - phitigra
        sage: H = e.get_graph()             # optional - phitigra
        sage: H == G and not H is G         # optional - phitigra
        True

    Using different display options::

        sage: e = graph_editor(graphs.PetersenGraph(), width=300, height=300,       # optional - phitigra
        ....:                  default_radius=12, default_vertex_color='orange',
        ....:                  default_edge_color='#666', show_vertex_labels=False)
        sage: e.show()                                                              # not tested

    .. NOTE::

        The editor does not support multigraphs.
    """
