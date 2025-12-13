from sage.misc.cachefunc import cached_function as cached_function
from sage.misc.latex import latex as latex
from sage.structure.sage_object import SageObject as SageObject

def check_tkz_graph() -> None:
    """
    Check if the proper LaTeX packages for the ``tikzpicture`` environment are
    installed in the user's environment, and issue a warning otherwise.

    The warning is only issued on the first call to this function. So any
    doctest that illustrates the use of the tkz-graph packages should call this
    once as having random output to exhaust the warnings before testing output.

    See also :meth:`sage.misc.latex.Latex.check_file`

    TESTS::

        sage: from sage.graphs.graph_latex import check_tkz_graph
        sage: check_tkz_graph()  # random - depends on TeX installation
        sage: check_tkz_graph()  # at least the second time, so no output
    """
def have_tkz_graph() -> bool:
    """
    Return ``True`` if the proper LaTeX packages for the ``tikzpicture``
    environment are installed in the user's environment, namely ``tikz``,
    ``tkz-graph`` and ``tkz-berge``.

    The result is cached.

    See also :meth:`sage.misc.latex.Latex.has_file`

    TESTS::

        sage: from sage.graphs.graph_latex import have_tkz_graph
        sage: have_tkz_graph()  # random - depends on TeX installation
        sage: have_tkz_graph() in [True, False]
        True
    """
@cached_function
def setup_latex_preamble() -> None:
    '''
    Add appropriate ``\\usepackage{...}``, and other instructions to the latex
    preamble for the packages that are needed for processing graphs(``tikz``,
    ``tkz-graph``, ``tkz-berge``), if available in the ``LaTeX`` installation.

    See also :meth:`sage.misc.latex.Latex.add_package_to_preamble_if_available`.

    EXAMPLES::

        sage: sage.graphs.graph_latex.setup_latex_preamble()

    TESTS::

        sage: ("\\\\usepackage{tikz}" in latex.extra_preamble()) == latex.has_file("tikz.sty")
        True
    '''

class GraphLatex(SageObject):
    """
    A class to hold, manipulate and employ options for converting
    a graph to LaTeX.

    This class serves two purposes.  First it holds the values of various
    options designed to work with the ``tkz-graph`` LaTeX package for rendering
    graphs.  As such, a graph that uses this class will hold a reference to it.
    Second, this class contains the code to convert a graph into the
    corresponding LaTeX constructs, returning a string.

    EXAMPLES::

        sage: from sage.graphs.graph_latex import GraphLatex
        sage: opts = GraphLatex(graphs.PetersenGraph())
        sage: opts
        LaTeX options for Petersen graph: {}
        sage: g = graphs.PetersenGraph()
        sage: opts = g.latex_options()
        sage: g == loads(dumps(g))
        True
    """
    def __init__(self, graph, **options) -> None:
        """
        Return a GraphLatex object, which holds all the parameters needed for
        creating a LaTeX string that will be rendered as a picture of the graph.

        See :mod:`sage.graphs.graph_latex` for more documentation.

        EXAMPLES::

            sage: from sage.graphs.graph_latex import GraphLatex
            sage: GraphLatex(graphs.PetersenGraph())
            LaTeX options for Petersen graph: {}
        """
    def __eq__(self, other):
        """
        Two :class:`sage.graphs.graph_latex.GraphLatex` objects are equal if
        their options are equal.

        The graphs they are associated with are ignored in the comparison.

        TESTS::

            sage: from sage.graphs.graph_latex import GraphLatex
            sage: opts1 = GraphLatex(graphs.PetersenGraph())
            sage: opts2 = GraphLatex(graphs.CompleteGraph(10))
            sage: opts1.set_option('tkz_style', 'Art')
            sage: opts2.set_option('tkz_style', 'Art')
            sage: opts1 == opts2
            True
            sage: opts2.set_option('tkz_style', 'Normal')
            sage: opts1 == opts2
            False
        """
    def set_option(self, option_name, option_value=None) -> None:
        '''
        Set, modify, clear a LaTeX option for controlling the rendering of a
        graph.

        The possible options are documented here, because ultimately it is this
        routine that sets the values. However, the
        :meth:`sage.graphs.generic_graph.GenericGraph.set_latex_options` method
        is the easiest way to set options, and allows several to be set at once.

        INPUT:

        - ``option_name`` -- string for a latex option contained in the list
          ``sage.graphs.graph_latex.GraphLatex.__graphlatex_options``;
          a :exc:`ValueError` is raised if the option is not allowed

        - ``option_value`` -- a value for the option; if omitted, or set to
          ``None``, the option will use the default value

        The output can be either handled internally by ``Sage``, or delegated to
        the external software ``dot2tex`` and ``graphviz``. This is controlled
        by the option ``format``:

        - ``format`` -- string (default: ``\'tkz_graph\'``); either ``\'dot2tex\'``
          or ``\'tkz_graph\'``

        If format is ``\'dot2tex\'``, then all the LaTeX generation will be
        delegated to ``dot2tex`` (which must be installed).

        For ``tkz_graph``, the possible option names, and associated values are
        given below. This first group allows you to set a style for a graph and
        specify some sizes related to the eventual image. (For more information
        consult the documentation for the ``tkz-graph`` package.)

        - ``tkz_style`` -- string (default: ``\'Custom\'``); the name of a
          pre-defined ``tkz-graph`` style such as ``\'Shade\'``, ``\'Art\'``,
          ``\'Normal\'``, ``\'Dijkstra\'``, ``\'Welsh\'``, ``\'Classic\'``, and
          ``\'Simple\'``, or the string ``\'Custom\'``.  Using one of these styles
          alone will often give a reasonably good drawing with minimal
          effort. For a custom appearance set this to ``\'Custom\'`` and use the
          options described below to override the default values.

        - ``units`` -- string (default: ``\'cm\'``); a natural unit of
          measurement used for all dimensions.  Possible values are: ``\'in\'``,
          ``\'mm\'``, ``\'cm\'``, ``\'pt\'``, ``\'em\'``, ``\'ex\'``.

        - ``scale`` -- float (default: `1.0`); a dimensionless number that
          multiplies every linear dimension. So you can design at sizes you are
          accustomed to, then shrink or expand to meet other needs. Though fonts
          do not scale.

        - ``graphic_size`` -- tuple (default: ``(5, 5)``); overall dimensions
          (width, length) of the bounding box around the entire graphic image

        - ``margins`` -- 4-tuple (default: ``(0, 0, 0, 0)``); portion of graphic
          given over to a plain border as a tuple of four numbers: (left, right,
          top, bottom). These are subtracted from the ``graphic_size`` to
          create the area left for the vertices of the graph itself.  Note that
          the processing done by Sage will trim the graphic down to the minimum
          possible size, removing any border. So this is only useful if you use
          the latex string in a latex document.

        If not using a pre-built style the following options are used, so the
        following defaults will apply.  It is not possible to begin with a
        pre-built style and modify it (other than editing the latex string by
        hand after the fact).

        - ``vertex_color`` -- (default: ``\'black\'``) a single color to use as
          the default for outline of vertices. For the ``sphere`` shape this
          color is used for the entire vertex, which is drawn with a 3D shading.
          Colors must be specified as a string recognized by the matplotlib
          library: a standard color name like ``\'red\'``, or a hex string like
          ``\'#2D87A7\'``, or a single character from the choices ``\'rgbcmykw\'``.
          Additionally, a number between 0 and 1 will create a grayscale value.
          These color specifications are consistent throughout the options for
          a ``tikzpicture``.

        - ``vertex_colors`` -- dictionary whose keys are vertices of the graph
          and whose values are colors. These will be used to color the outline
          of vertices. See the explanation above for the ``vertex_color`` option
          to see possible values. These values need only be specified for a
          proper subset of the vertices. Specified values will supersede a
          default value.

        - ``vertex_fill_color`` -- (default: ``\'white\'``) a single color to use
          as the default for the fill color of vertices. See the explanation
          above for the ``vertex_color`` option to see possible values. This
          color is ignored for the ``sphere`` vertex shape.

        - ``vertex_fill_colors`` -- dictionary whose keys are vertices of the
          graph and whose values are colors. These will be used to fill the
          interior of vertices. See the explanation above for the
          ``vertex_color`` option to see possible values. These values need only
          be specified for a proper subset of the vertices. Specified values
          will supersede a default value.

        - ``vertex_shape`` -- string (default: ``\'circle\'``); specifies the
          shape of the vertices. Allowable values are ``\'circle\'``,
          ``\'sphere\'``, ``\'rectangle\'``, ``\'diamond\'``. The sphere shape has a
          3D look to its coloring and is uses only one color, that specified by
          ``vertex_color`` and ``vertex_colors``, which are normally used for
          the outline of the vertex.

        - ``vertex_shapes`` -- dictionary whose keys are vertices of the graph
          and whose values are shapes. See ``vertex_shape`` for the allowable
          possibilities.

        - ``vertex_size`` -- float (default: 1.0); the minimum size of a vertex
          as a number. Vertices will expand to contain their labels if the
          labels are placed inside the vertices. If you set this value to zero
          the vertex will be as small as possible (up to tkz-graph\'s "inner sep"
          parameter), while still containing labels. However, if labels are not
          of a uniform size, then the vertices will not be either.

        - ``vertex_sizes`` -- dictionary of sizes for some of the vertices

        - ``vertex_labels`` -- boolean (default: ``True``); determine whether or
          not to display the vertex labels.  If ``False`` subsequent options
          about vertex labels are ignored.

        - ``vertex_labels_math`` -- boolean (default: ``True``); when ``True``,
          if a label is a string that begins and ends with dollar signs, then
          the string will be rendered as a latex string.  Otherwise, the label
          will be automatically subjected to the ``latex()`` method and rendered
          accordingly. If ``False`` the label is rendered as its textual
          representation according to the ``_repr`` method. Support for
          arbitrarily-complicated mathematics is not especially robust.

        - ``vertex_label_color`` -- (default: ``\'black\'``) a single color to
          use as the default for labels of vertices. See the explanation above
          for the ``vertex_color`` option to see possible values.

        - ``vertex_label_colors`` -- dictionary whose keys are vertices of the
          graph and whose values are colors. These will be used for the text of
          the labels of vertices. See the explanation above for the
          ``vertex_color`` option to see possible values. These values need only
          be specified for a proper subset of the vertices. Specified values
          will supersede a default value.

        - ``vertex_label_placement`` -- (default: ``\'center\'``) if ``\'center\'``
          the label is centered in the interior of the vertex and the vertex
          will expand to contain the label. Giving instead a pair of numbers
          will place the label exterior to the vertex at a certain distance from
          the edge, and at an angle to the positive x-axis, similar in spirit to
          polar coordinates.

        - ``vertex_label_placements`` -- dictionary of placements indexed by
          the vertices. See the explanation for ``vertex_label_placement`` for
          the possible values.

        - ``edge_color`` -- (default: ``\'black\'``) a single color to use as the
          default for an edge. See the explanation above for the
          ``vertex_color`` option to see possible values.

        - ``edge_colors`` -- dictionary whose keys are edges of the graph and
          whose values are colors. These will be used to color the edges. See
          the explanation above for the ``vertex_color`` option to see possible
          values. These values need only be specified for a proper subset of the
          vertices. Specified values will supersede a default value.

        - ``edge_fills`` -- boolean (default: ``False``); whether an edge has a
          second color running down the middle. This can be a useful effect for
          highlighting edge crossings.

        - ``edge_fill_color`` -- (default: ``\'black\'``) a single color to use
          as the default for the fill color of an edge. The boolean switch
          ``edge_fills`` must be set to ``True`` for this to have an effect. See
          the explanation above for the ``vertex_color`` option to see possible
          values.

        - ``edge_fill_colors`` -- dictionary whose keys are edges of the graph
          and whose values are colors. See the explanation above for the
          ``vertex_color`` option to see possible values. These values need
          only be specified for a proper subset of the vertices. Specified
          values will supersede a default value.

        - ``edge_thickness`` -- float (default: 0.1); specifies the width of the
          edges. Note that ``tkz-graph`` does not interpret this number for
          loops.

        - ``edge_thicknesses`` -- dictionary of thicknesses for some of the
          edges of a graph. These values need only be specified for a proper
          subset of the vertices. Specified values will supersede a default
          value.

        - ``edge_labels`` -- boolean (default: ``False``); determine if edge
          labels are shown. If ``False`` subsequent options about edge labels
          are ignored.

        - ``edge_labels_math`` -- boolean (default: ``True``); control how edge
          labels are rendered. Read the explanation for the
          ``vertex_labels_math`` option, which behaves identically.  Support for
          arbitrarily-complicated mathematics is not especially robust.

        - ``edge_label_color`` -- (default: ``\'black\'``) a single color to use
          as the default for labels of edges. See the explanation above for the
          ``vertex_color`` option to see possible values.

        - ``edge_label_colors`` -- dictionary whose keys are edges of the
          graph and whose values are colors. These will be used for the text of
          the labels of edges. See the explanation above for the
          ``vertex_color`` option to see possible values. These values need only
          be specified for a proper subset of the vertices. Specified values
          will supersede a default value. Note that labels must be used for this
          to have any effect, and no care is taken to ensure that label and fill
          colors work well together.

        - ``edge_label_sloped`` -- boolean (default: ``True``); specifies how
          edge labels are place. ``False`` results in a horizontal label, while
          ``True`` means the label is rotated to follow the direction of the
          edge it labels.

        - ``edge_label_slopes`` -- dictionary of booleans, indexed by some
          subset of the edges.  See the ``edge_label_sloped`` option for a
          description of sloped edge labels.

        - ``edge_label_placement`` -- (default: 0.50) either a number between
          0.0 and 1.0, or one of: ``\'above\'``, ``\'below\'``, ``\'left\'``,
          ``\'right\'``. These adjust the location of an edge label along an
          edge. A number specifies how far along the edge the label is located.
          ``\'left\'`` and ``\'right\'`` are conveniences. ``\'above\'`` and
          ``\'below\'`` move the label off the edge itself while leaving it near
          the midpoint of the edge. The default value of ``0.50`` places the
          label on the midpoint of the edge.

        - ``edge_label_placements`` -- dictionary of edge placements, indexed
          by the edges.  See the ``edge_label_placement`` option for a
          description of the allowable values.

        - ``loop_placement`` -- (default: ``(3.0, \'NO\')``); determine how loops
          are rendered.  the first element of the pair is a distance, which
          determines how big the loop is and the second element is a string
          specifying a compass point (North, South, East, West) as one of
          ``\'NO\'``, ``\'SO\'``, ``\'EA\'``, ``\'WE\'``.

        - ``loop_placements`` -- dictionary of loop placements.  See the
          ``loop_placements`` option for the allowable values.  While loops are
          technically edges, this dictionary is indexed by vertices.

        For the ``\'dot2tex\'`` format, the possible option names and associated
        values are given below:

        - ``prog`` -- string; the program used for the layout. It must be a
          string corresponding to one of the software of the graphviz suite:
          ``\'dot\'``, ``\'neato\'``, ``\'twopi\'``, ``\'circo\'`` or ``\'fdp\'``.

        - ``edge_labels`` -- boolean (default: ``False)``; whether to display
          the labels on edges

        - ``edge_colors`` -- a color; can be used to set a global color to the
          edge of the graph

        - ``color_by_label`` -- boolean (default: ``False``); colors the edges
          according to their labels

        - ``subgraph_clusters`` -- (default: ``[]``) a list of lists of
          vertices, if supported by the layout engine, nodes belonging to the
          same cluster subgraph are drawn together, with the entire drawing of
          the cluster contained within a bounding rectangle.

        OUTPUT: none; success happens silently

        EXAMPLES:

        Set, then modify, then clear the ``tkz_style`` option, and finally show
        an error for an unrecognized option name::

            sage: g = graphs.PetersenGraph()
            sage: opts = g.latex_options()
            sage: opts
            LaTeX options for Petersen graph: {}
            sage: opts.set_option(\'tkz_style\', \'Art\')
            sage: opts
            LaTeX options for Petersen graph: {\'tkz_style\': \'Art\'}
            sage: opts.set_option(\'tkz_style\', \'Simple\')
            sage: opts
            LaTeX options for Petersen graph: {\'tkz_style\': \'Simple\'}
            sage: opts.set_option(\'tkz_style\')
            sage: opts
            LaTeX options for Petersen graph: {}
            sage: opts.set_option(\'bad_name\', \'nonsense\')
            Traceback (most recent call last):
            ...
            ValueError: bad_name is not a LaTeX option for a graph.

        See :meth:`sage.graphs.generic_graph.GenericGraph.layout_graphviz` for
        installation instructions for ``graphviz`` and ``dot2tex``. Furthermore,
        pgf >= 2.00 should be available inside LaTeX\'s tree for LaTeX
        compilation (e.g. when using ``view``). In case your LaTeX distribution
        does not provide it, here are short instructions:

           - download pgf from http://sourceforge.net/projects/pgf/
           - unpack it in ``/usr/share/texmf/tex/generic`` (depends on your system)
           - clean out remaining pgf files from older version
           - run texhash

        TESTS:

        These test all of the options and one example of each allowable proper
        input. They should all execute silently. ::

            sage: G = Graph()
            sage: G.add_edge((0,1))
            sage: opts = G.latex_options()
            sage: opts.set_option(\'tkz_style\', \'Custom\')
            sage: opts.set_option(\'tkz_style\', \'Art\')
            sage: opts.set_option(\'format\', \'tkz_graph\')
            sage: opts.set_option(\'layout\', \'acyclic\')
            sage: opts.set_option(\'prog\', \'dot\')
            sage: opts.set_option(\'units\', \'cm\')
            sage: opts.set_option(\'scale\', 1.0)
            sage: opts.set_option(\'graphic_size\', (5, 5))
            sage: opts.set_option(\'margins\', (0,0,0,0))
            sage: opts.set_option(\'vertex_color\', \'black\')
            sage: opts.set_option(\'vertex_colors\', {0:\'#ABCDEF\'})
            sage: opts.set_option(\'vertex_fill_color\', \'white\')
            sage: opts.set_option(\'vertex_fill_colors\', {0:\'c\'})
            sage: opts.set_option(\'vertex_shape\', \'circle\')
            sage: opts.set_option(\'vertex_shapes\', {0:\'sphere\'})
            sage: opts.set_option(\'vertex_size\', 1.0)
            sage: opts.set_option(\'vertex_sizes\', {0:3.4})
            sage: opts.set_option(\'vertex_labels\', True)
            sage: opts.set_option(\'vertex_labels_math\', True)
            sage: opts.set_option(\'vertex_label_color\', \'black\')
            sage: opts.set_option(\'vertex_label_colors\', {0:\'.23\'})
            sage: opts.set_option(\'vertex_label_placement\', \'center\')
            sage: opts.set_option(\'vertex_label_placement\', (3, 4.2))
            sage: opts.set_option(\'vertex_label_placements\', {0:\'center\'})
            sage: opts.set_option(\'vertex_label_placements\', {0:(4.7,1)})
            sage: opts.set_option(\'edge_color\', \'black\')
            sage: opts.set_option(\'edge_colors\', {(0,1):\'w\'})
            sage: opts.set_option(\'edge_fills\', False)
            sage: opts.set_option(\'edge_fill_color\', \'black\')
            sage: opts.set_option(\'edge_fill_colors\', {(0,1):"#123456"})
            sage: opts.set_option(\'edge_thickness\', 0.1)
            sage: opts.set_option(\'edge_thicknesses\', {(0,1):5.2})
            sage: opts.set_option(\'edge_labels\', False)
            sage: opts.set_option(\'edge_labels_math\', True)
            sage: opts.set_option(\'edge_label_color\', \'black\')
            sage: opts.set_option(\'edge_label_colors\', {(0,1):\'red\'})
            sage: opts.set_option(\'edge_label_sloped\', True)
            sage: opts.set_option(\'edge_label_slopes\', {(0,1): False})
            sage: opts.set_option(\'edge_label_placement\', \'left\')
            sage: opts.set_option(\'edge_label_placement\', 0.50)
            sage: opts.set_option(\'edge_label_placements\', {(0,1):\'above\'})
            sage: opts.set_option(\'edge_label_placements\', {(0,1):0.75})
            sage: opts.set_option(\'loop_placement\', (3.0, \'NO\'))
            sage: opts.set_option(\'loop_placements\', {0:(5.7,\'WE\')})
            sage: opts.set_option(\'subgraph_clusters\', [[0,1]])

        These test some of the logic of possible failures. Some tests, such as
        inputs of colors, are handled by somewhat general sections of code and
        are not tested for each possible option. ::

            sage: G=Graph()
            sage: G.add_edge((0,1))
            sage: opts = G.latex_options()
            sage: opts.set_option(\'tkz_style\', \'Crazed\')
            Traceback (most recent call last):
            ...
            ValueError: tkz_style is not "Custom", nor an implemented tkz-graph style
            sage: opts.set_option(\'format\', \'NonExistent\')
            Traceback (most recent call last):
            ...
            ValueError: format option must be one of: tkz_graph, dot2tex not NonExistent
            sage: opts.set_option(\'units\', \'furlongs\')
            Traceback (most recent call last):
            ...
            ValueError: units option must be one of: in, mm, cm, pt, em, ex, not furlongs
            sage: opts.set_option(\'graphic_size\', (1,2,3))
            Traceback (most recent call last):
            ...
            ValueError: graphic_size option must be an ordered pair, not (1, 2, 3)
            sage: opts.set_option(\'margins\', (1,2,3))
            Traceback (most recent call last):
            ...
            ValueError: margins option must be 4-tuple, not (1, 2, 3)
            sage: opts.set_option(\'vertex_color\', \'chartruse\')
            Traceback (most recent call last):
            ...
            ValueError: vertex_color option needs to be a matplotlib color (always as a string), not chartruse
            sage: opts.set_option(\'vertex_labels_math\', \'maybe\')
            Traceback (most recent call last):
            ...
            ValueError: vertex_labels_math option must be True or False, not maybe
            sage: opts.set_option(\'vertex_shape\', \'decagon\')
            Traceback (most recent call last):
            ...
            ValueError: vertex_shape option must be the shape of a vertex, not decagon
            sage: opts.set_option(\'scale\', \'big\')
            Traceback (most recent call last):
            ...
            ValueError: scale option must be a positive number, not big
            sage: opts.set_option(\'scale\', -6)
            Traceback (most recent call last):
            ...
            ValueError: scale option must be a positive number, not -6
            sage: opts.set_option(\'vertex_label_placement\', (2,-4))
            Traceback (most recent call last):
            ...
            ValueError: vertex_label_placement option must be None, or a pair of positive numbers, not (2, -4)
            sage: opts.set_option(\'edge_label_placement\', 3.6)
            Traceback (most recent call last):
            ...
            ValueError: edge_label_placement option must be a number between 0.0 and 1.0 or a place (like "above"), not 3.60000000000000
            sage: opts.set_option(\'loop_placement\', (5,\'SW\'))
            Traceback (most recent call last):
            ...
            ValueError: loop_placement option must be a pair that is a positive number followed by a compass point abbreviation, not (5, \'SW\')
            sage: opts.set_option(\'vertex_fill_colors\', {0:\'#GG0000\'})
            Traceback (most recent call last):
            ...
            ValueError: vertex_fill_colors option for 0 needs to be a matplotlib color (always as a string), not #GG0000
            sage: opts.set_option(\'vertex_sizes\', {0:-10})
            Traceback (most recent call last):
            ...
            ValueError: vertex_sizes option for 0 needs to be a positive number, not -10
            sage: opts.set_option(\'edge_label_slopes\', {(0,1):\'possibly\'})
            Traceback (most recent call last):
            ...
            ValueError: edge_label_slopes option for (0, 1) needs to be True or False, not possibly
            sage: opts.set_option(\'vertex_shapes\', {0:\'pentagon\'})
            Traceback (most recent call last):
            ...
            ValueError: vertex_shapes option for 0 needs to be a vertex shape, not pentagon
            sage: opts.set_option(\'vertex_label_placements\', {0:(1,2,3)})
            Traceback (most recent call last):
            ...
            ValueError: vertex_label_placements option for 0 needs to be None or a pair of positive numbers, not (1, 2, 3)
            sage: opts.set_option(\'edge_label_placements\', {(0,1):\'partway\'})
            Traceback (most recent call last):
            ...
            ValueError: edge_label_placements option for (0, 1) needs to be a number between 0.0 and 1.0 or a place (like "above"), not partway
            sage: opts.set_option(\'loop_placements\', {0:(-3,\'WE\')})
            Traceback (most recent call last):
            ...
            ValueError: loop_placements option for 0 needs to be a positive number and a compass point (like "EA"), not (-3, \'WE\')
            sage: opts.set_option(\'margins\', (1,2,3,-5))
            Traceback (most recent call last):
            ...
            ValueError: margins option of (1, 2, 3, -5) cannot contain -5
        '''
    def set_options(self, **kwds) -> None:
        """
        Set several LaTeX options for a graph all at once.

        INPUT:

        - ``kwds`` -- any number of option/value pairs to set many graph latex
          options at once (a variable number, in any order). Existing values are
          overwritten, new values are added.  Existing values can be cleared by
          setting the value to ``None``. Errors are raised in the
          :func:`set_option` method.

        EXAMPLES::

            sage: g = graphs.PetersenGraph()
            sage: opts = g.latex_options()
            sage: opts.set_options(tkz_style='Welsh')
            sage: opts.get_option('tkz_style')
            'Welsh'
        """
    def get_option(self, option_name):
        '''
        Return the current value of the named option.

        INPUT:

        - ``option_name`` -- the name of an option

        OUTPUT:

        If the name is not present in ``__graphlatex_options`` it is an error to
        ask for it. If an option has not been set then the default value is
        returned. Otherwise, the value of the option is returned.

        EXAMPLES::

            sage: g = graphs.PetersenGraph()
            sage: opts = g.latex_options()
            sage: opts.set_option(\'tkz_style\', \'Art\')
            sage: opts.get_option(\'tkz_style\')
            \'Art\'
            sage: opts.set_option(\'tkz_style\')
            sage: opts.get_option(\'tkz_style\') == "Custom"
            True
            sage: opts.get_option(\'bad_name\')
            Traceback (most recent call last):
            ...
            ValueError: bad_name is not a Latex option for a graph.
        '''
    def latex(self):
        """
        Return a string in LaTeX representing a graph.

        This is the command that is invoked by
        ``sage.graphs.generic_graph.GenericGraph._latex_`` for a graph, so it
        returns a string of LaTeX commands that can be incorporated into a LaTeX
        document unmodified. The exact contents of this string are influenced by
        the options set via the methods
        :meth:`sage.graphs.generic_graph.GenericGraph.set_latex_options`,
        :meth:`set_option`, and :meth:`set_options`.

        By setting the ``format`` option different packages can be used to
        create the latex version of a graph. Supported packages are
        ``tkz-graph`` and ``dot2tex``.

        EXAMPLES::

            sage: from sage.graphs.graph_latex import check_tkz_graph
            sage: check_tkz_graph()  # random - depends on TeX installation
            sage: g = graphs.CompleteGraph(2)
            sage: opts = g.latex_options()
            sage: print(opts.latex())
            \\begin{tikzpicture}
            \\definecolor{cv0}{rgb}{0.0,0.0,0.0}
            \\definecolor{cfv0}{rgb}{1.0,1.0,1.0}
            \\definecolor{clv0}{rgb}{0.0,0.0,0.0}
            \\definecolor{cv1}{rgb}{0.0,0.0,0.0}
            \\definecolor{cfv1}{rgb}{1.0,1.0,1.0}
            \\definecolor{clv1}{rgb}{0.0,0.0,0.0}
            \\definecolor{cv0v1}{rgb}{0.0,0.0,0.0}
            %
            \\Vertex[style={minimum size=1.0cm,draw=cv0,fill=cfv0,text=clv0,shape=circle},LabelOut=false,L=\\hbox{$0$},x=2.5cm,y=5.0cm]{v0}
            \\Vertex[style={minimum size=1.0cm,draw=cv1,fill=cfv1,text=clv1,shape=circle},LabelOut=false,L=\\hbox{$1$},x=2.5cm,y=0.0cm]{v1}
            %
            \\Edge[lw=0.1cm,style={color=cv0v1,},](v0)(v1)
            %
            \\end{tikzpicture}

        We check that :issue:`22070` is fixed::

            sage: edges = [(i,(i+1)%3,a) for i,a in enumerate('abc')]
            sage: G_with_labels = DiGraph(edges)
            sage: C = [[0,1], [2]]
            sage: kwds = dict(subgraph_clusters=C,color_by_label=True,prog='dot',format='dot2tex')
            sage: opts = G_with_labels.latex_options()
            sage: opts.set_options(edge_labels=True, **kwds)  # optional - dot2tex graphviz
            sage: latex(G_with_labels)                        # optional - dot2tex graphviz
            \\begin{tikzpicture}[>=latex,line join=bevel,]
            %%
            \\begin{scope}
              \\pgfsetstrokecolor{black}
              \\definecolor{strokecol}{rgb}{...};
              \\pgfsetstrokecolor{strokecol}
              \\definecolor{fillcol}{rgb}{...};
              \\pgfsetfillcolor{fillcol}
              \\filldraw ... cycle;
            \\end{scope}
            \\begin{scope}
              \\pgfsetstrokecolor{black}
              \\definecolor{strokecol}{rgb}{...};
              \\pgfsetstrokecolor{strokecol}
              \\definecolor{fillcol}{rgb}{...};
              \\pgfsetfillcolor{fillcol}
              \\filldraw ... cycle;
            \\end{scope}
            ...
            \\end{tikzpicture}
        """
    def dot2tex_picture(self):
        """
        Call ``dot2tex`` to construct a string of LaTeX commands representing a
        graph as a ``tikzpicture``.

        EXAMPLES::

            sage: g = digraphs.ButterflyGraph(1)
            sage: from sage.graphs.graph_latex import check_tkz_graph
            sage: check_tkz_graph()  # random - depends on TeX installation
            sage: print(g.latex_options().dot2tex_picture())  # optional - dot2tex graphviz
            \\begin{tikzpicture}[>=latex,line join=bevel,]
            %%
              \\node (node_...) at (...bp,...bp) [draw,draw=none] {$\\left(...\\right)$};
              \\node (node_...) at (...bp,...bp) [draw,draw=none] {$\\left(...\\right)$};
              \\node (node_...) at (...bp,...bp) [draw,draw=none] {$\\left(...\\right)$};
              \\node (node_...) at (...bp,...bp) [draw,draw=none] {$\\left(...\\right)$};
              \\draw [black,->] (node_...) ..controls (...bp,...bp) and (...bp,...bp)  .. (node_...);
              \\draw [black,->] (node_...) ..controls (...bp,...bp) and (...bp,...bp)  .. (node_...);
              \\draw [black,->] (node_...) ..controls (...bp,...bp) and (...bp,...bp)  .. (node_...);
              \\draw [black,->] (node_...) ..controls (...bp,...bp) and (...bp,...bp)  .. (node_...);
            %
            \\end{tikzpicture}

        We make sure :issue:`13624` is fixed::

            sage: G = DiGraph()
            sage: G.add_edge(3333, 88, 'my_label')
            sage: G.set_latex_options(edge_labels=True)
            sage: print(G.latex_options().dot2tex_picture())  # optional - dot2tex graphviz
            \\begin{tikzpicture}[>=latex,line join=bevel,]
            %%
            \\node (node_...) at (...bp,...bp) [draw,draw=none] {$...$};
              \\node (node_...) at (...bp,...bp) [draw,draw=none] {$...$};
              \\draw [black,->] (node_...) ..controls (...bp,...bp) and (...bp,...bp)  .. (node_...);
              \\definecolor{strokecol}{rgb}{0.0,0.0,0.0};
              \\pgfsetstrokecolor{strokecol}
              \\draw (...bp,...bp) node {$\\text{\\texttt{my{\\char`\\_}label}}$};
            %
            \\end{tikzpicture}

        Check that :issue:`25120` is fixed::

            sage: G = Graph([(0,1)])
            sage: G.set_latex_options(edge_colors = {(0,1): 'red'})
            sage: print(G.latex_options().dot2tex_picture())  # optional - dot2tex graphviz
            \\begin{tikzpicture}[>=latex,line join=bevel,]
            ...
            \\draw [red,] (node_0) ... (node_1);
            ...
            \\end{tikzpicture}

        .. NOTE::

            There is a lot of overlap between what ``tkz_picture`` and
            ``dot2tex`` do. It would be best to merge them! ``dot2tex`` probably
            can work without ``graphviz`` if layout information is provided.
        """
    def tkz_picture(self):
        '''
        Return a string of LaTeX commands representing a graph as a
        ``tikzpicture``.

        This routine interprets the graph\'s properties and the options in
        ``_options`` to render the graph with commands from the ``tkz-graph``
        LaTeX package.

        This requires that the LaTeX optional packages ``tkz-graph`` and
        ``tkz-berge`` be installed. You may also need a current version of the
        pgf package.  If the ``tkz-graph`` and ``tkz-berge`` packages are
        present in the system\'s TeX installation, the appropriate
        ``\\\\usepackage{}`` commands will be added to the LaTeX preamble as part
        of the initialization of the graph. If these two packages are not
        present, then this command will return a warning on its first use, but
        will return a string that could be used elsewhere, such as a LaTeX
        document.

        For more information about tkz-graph you can visit
        https://www.ctan.org/pkg/tkz-graph.

        EXAMPLES:

        With a pre-built ``tkz-graph`` style specified, the latex representation
        will be relatively simple. ::

            sage: from sage.graphs.graph_latex import check_tkz_graph
            sage: check_tkz_graph()  # random - depends on TeX installation
            sage: g = graphs.CompleteGraph(3)
            sage: opts = g.latex_options()
            sage: g.set_latex_options(tkz_style=\'Art\')
            sage: print(opts.tkz_picture())
            \\begin{tikzpicture}
            \\GraphInit[vstyle=Art]
            %
            \\Vertex[L=\\hbox{$0$},x=2.5cm,y=5.0cm]{v0}
            \\Vertex[L=\\hbox{$1$},x=0.0cm,y=0.0cm]{v1}
            \\Vertex[L=\\hbox{$2$},x=5.0cm,y=0.0cm]{v2}
            %
            \\Edge[](v0)(v1)
            \\Edge[](v0)(v2)
            \\Edge[](v1)(v2)
            %
            \\end{tikzpicture}

        Setting the style to "Custom" results in various configurable aspects
        set to the defaults, so the string is more involved. ::

            sage: from sage.graphs.graph_latex import check_tkz_graph
            sage: check_tkz_graph()  # random - depends on TeX installation
            sage: g = graphs.CompleteGraph(3)
            sage: opts = g.latex_options()
            sage: g.set_latex_options(tkz_style=\'Custom\')
            sage: print(opts.tkz_picture())
            \\begin{tikzpicture}
            \\definecolor{cv0}{rgb}{0.0,0.0,0.0}
            \\definecolor{cfv0}{rgb}{1.0,1.0,1.0}
            \\definecolor{clv0}{rgb}{0.0,0.0,0.0}
            \\definecolor{cv1}{rgb}{0.0,0.0,0.0}
            \\definecolor{cfv1}{rgb}{1.0,1.0,1.0}
            \\definecolor{clv1}{rgb}{0.0,0.0,0.0}
            \\definecolor{cv2}{rgb}{0.0,0.0,0.0}
            \\definecolor{cfv2}{rgb}{1.0,1.0,1.0}
            \\definecolor{clv2}{rgb}{0.0,0.0,0.0}
            \\definecolor{cv0v1}{rgb}{0.0,0.0,0.0}
            \\definecolor{cv0v2}{rgb}{0.0,0.0,0.0}
            \\definecolor{cv1v2}{rgb}{0.0,0.0,0.0}
            %
            \\Vertex[style={minimum size=1.0cm,draw=cv0,fill=cfv0,text=clv0,shape=circle},LabelOut=false,L=\\hbox{$0$},x=2.5cm,y=5.0cm]{v0}
            \\Vertex[style={minimum size=1.0cm,draw=cv1,fill=cfv1,text=clv1,shape=circle},LabelOut=false,L=\\hbox{$1$},x=0.0cm,y=0.0cm]{v1}
            \\Vertex[style={minimum size=1.0cm,draw=cv2,fill=cfv2,text=clv2,shape=circle},LabelOut=false,L=\\hbox{$2$},x=5.0cm,y=0.0cm]{v2}
            %
            \\Edge[lw=0.1cm,style={color=cv0v1,},](v0)(v1)
            \\Edge[lw=0.1cm,style={color=cv0v2,},](v0)(v2)
            \\Edge[lw=0.1cm,style={color=cv1v2,},](v1)(v2)
            %
            \\end{tikzpicture}

        See the introduction to the :mod:`~sage.graphs.graph_latex` module for
        more information on the use of this routine.

        TESTS:

        Graphs with preset layouts that are vertical or horizontal can cause
        problems. First test is a horizontal layout on a path with three
        vertices. ::

            sage: from sage.graphs.graph_latex import check_tkz_graph
            sage: check_tkz_graph()  # random - depends on TeX installation
            sage: g = graphs.PathGraph(3)
            sage: opts = g.latex_options()
            sage: print(opts.tkz_picture())
            \\begin{tikzpicture}
            ...
            \\end{tikzpicture}

        Scaling to a bounding box is problematic for graphs with just one
        vertex, or none. ::

            sage: from sage.graphs.graph_latex import check_tkz_graph
            sage: check_tkz_graph()  # random - depends on TeX installation
            sage: g = graphs.CompleteGraph(1)
            sage: opts = g.latex_options()
            sage: print(opts.tkz_picture())
            \\begin{tikzpicture}
            ...
            \\end{tikzpicture}

        With the empty graph, an empty tikzfigure is output. ::

            sage: from sage.graphs.graph_latex import check_tkz_graph
            sage: check_tkz_graph()  # random - depends on TeX installation
            sage: g = Graph()
            sage: opts = g.latex_options()
            sage: print(opts.tkz_picture())
            \\begin{tikzpicture}
            %
            %
            %
            \\end{tikzpicture}

        For a complicated vertex, a TeX box is used. ::

            sage: B = crystals.Tableaux([\'B\', 2], shape=[1])
            sage: latex(B)  # optional - !dot2tex
            \\begin{tikzpicture}
            ...
            \\newsavebox{\\vertex}
            \\sbox{\\vertex}{${\\def\\lr#1{\\multicolumn{1}{|@{\\hspace{.6ex}}c@{\\hspace{.6ex}}|}{\\raisebox{-.3ex}{$#1$}}}
            \\raisebox{-.6ex}{$\\begin{array}[b]{*{1}c}\\cline{1-1}
            \\lr{1}\\\\\\cline{1-1}
            \\end{array}$}
            }$}\\Vertex[style={minimum size=1.0cm,draw=cv0,fill=cfv0,text=clv0,shape=circle},LabelOut=false,L=\\usebox{\\vertex},x=...,y=...]{v0}
            ...
            \\end{tikzpicture}
        '''
