from _typeshed import Incomplete
from sage.arith.srange import xsrange as xsrange
from sage.misc.decorators import options as options
from sage.plot.primitive import GraphicPrimitive as GraphicPrimitive

class StreamlinePlot(GraphicPrimitive):
    """
    Primitive class that initializes the StreamlinePlot graphics type
    """
    xpos_array: Incomplete
    ypos_array: Incomplete
    xvec_array: Incomplete
    yvec_array: Incomplete
    def __init__(self, xpos_array, ypos_array, xvec_array, yvec_array, options) -> None:
        """
        Create the graphics primitive StreamlinePlot. This sets options
        and the array to be plotted as attributes.

        EXAMPLES::

            sage: x, y = var('x y')
            sage: R = streamline_plot((sin(x), cos(y)), (x,0,1), (y,0,1), plot_points=2)
            sage: r = R[0]
            sage: r.options()['plot_points']
            2
            sage: r.xpos_array
            array([0., 1.])
            sage: r.yvec_array
            masked_array(
              data=[[1.0, 1.0],
                    [0.5403023058681398, 0.5403023058681398]],
              mask=[[False, False],
                    [False, False]],
              fill_value=1e+20)

        TESTS:

        We test dumping and loading a plot::

            sage: x, y = var('x y')
            sage: P = streamline_plot((sin(x), cos(y)), (x,-3,3), (y,-3,3))
            sage: Q = loads(dumps(P))
        """
    def get_minmax_data(self):
        '''
        Return a dictionary with the bounding box data.

        EXAMPLES::

            sage: x, y = var(\'x y\')
            sage: import numpy  # to ensure numpy 2.0 compatibility
            sage: if int(numpy.version.short_version[0]) > 1:
            ....:     _ = numpy.set_printoptions(legacy="1.25")
            sage: d = streamline_plot((.01*x, x+y), (x,10,20), (y,10,20))[0].get_minmax_data()
            sage: d[\'xmin\']
            10.0
            sage: d[\'ymin\']
            10.0
        '''

def streamline_plot(f_g, xrange, yrange, **options):
    """
    Return a streamline plot in a vector field.

    ``streamline_plot`` can take either one or two functions. Consider
    two variables `x` and `y`.

    If given two functions `(f(x,y), g(x,y))`, then this function plots
    streamlines in the vector field over the specified ranges with ``xrange``
    being of `x`, denoted by ``xvar`` below, between ``xmin`` and ``xmax``,
    and ``yrange`` similarly (see below). ::

        streamline_plot((f, g), (xvar, xmin, xmax), (yvar, ymin, ymax))

    Similarly, if given one function `f(x, y)`, then this function plots
    streamlines in the slope field `dy/dx = f(x,y)` over the specified
    ranges as given above.

    PLOT OPTIONS:

    - ``plot_points`` -- (default: 200) the minimal number of plot points

    - ``density`` -- float (default: 1.); controls the closeness of
      streamlines

    - ``start_points`` -- (optional) list of coordinates of starting
      points for the streamlines; coordinate pairs can be tuples or lists

    EXAMPLES:

    Plot some vector fields involving `\\sin` and `\\cos`::

        sage: x, y = var('x y')
        sage: streamline_plot((sin(x), cos(y)), (x,-3,3), (y,-3,3))
        Graphics object consisting of 1 graphics primitive

    .. PLOT::

        x, y = var('x y')
        g = streamline_plot((sin(x), cos(y)), (x,-3,3), (y,-3,3))
        sphinx_plot(g)

    ::

        sage: streamline_plot((y, (cos(x)-2) * sin(x)), (x,-pi,pi), (y,-pi,pi))
        Graphics object consisting of 1 graphics primitive

    .. PLOT::

        x, y = var('x y')
        g = streamline_plot((y, (cos(x)-2) * sin(x)), (x,-pi,pi), (y,-pi,pi))
        sphinx_plot(g)

    We increase the density of the plot::

        sage: streamline_plot((y, (cos(x)-2) * sin(x)),
        ....:                 (x,-pi,pi), (y,-pi,pi), density=2)
        Graphics object consisting of 1 graphics primitive

    .. PLOT::

        x, y = var('x y')
        g = streamline_plot((y, (cos(x)-2) * sin(x)), (x,-pi,pi), (y,-pi,pi), density=2)
        sphinx_plot(g)

    We ignore function values that are infinite or NaN::

        sage: x, y = var('x y')
        sage: streamline_plot((-x/sqrt(x^2+y^2), -y/sqrt(x^2+y^2)),
        ....:                 (x,-10,10), (y,-10,10))
        Graphics object consisting of 1 graphics primitive

    .. PLOT::

        x, y = var('x y')
        g = streamline_plot((-x/sqrt(x**2+y**2), -y/sqrt(x**2+y**2)), (x,-10,10), (y,-10,10))
        sphinx_plot(g)

    Extra options will get passed on to :func:`show()`, as long as they
    are valid::

        sage: streamline_plot((x, y), (x,-2,2), (y,-2,2), xmax=10)
        Graphics object consisting of 1 graphics primitive
        sage: streamline_plot((x, y), (x,-2,2), (y,-2,2)).show(xmax=10)  # These are equivalent

    .. PLOT::

        x, y = var('x y')
        g = streamline_plot((x, y), (x,-2,2), (y,-2,2), xmax=10)
        sphinx_plot(g)

    We can also construct streamlines in a slope field::

        sage: x, y = var('x y')
        sage: streamline_plot((x + y) / sqrt(x^2 + y^2), (x,-3,3), (y,-3,3))
        Graphics object consisting of 1 graphics primitive

    .. PLOT::

        x, y = var('x y')
        g = streamline_plot((x + y) / sqrt(x**2 + y**2), (x,-3,3), (y,-3,3))
        sphinx_plot(g)

    We choose some particular points the streamlines pass through::

        sage: pts = [[1, 1], [-2, 2], [1, -3/2]]
        sage: g = streamline_plot((x + y) / sqrt(x^2 + y^2),
        ....:                     (x,-3,3), (y,-3,3), start_points=pts)
        sage: g += point(pts, color='red')
        sage: g
        Graphics object consisting of 2 graphics primitives

    .. PLOT::

        x, y = var('x y')
        pts = [[1, 1], [-2, 2], [1, -3/2]]
        g = streamline_plot((x + y) / sqrt(x**2 + y**2), (x,-3,3), (y,-3,3), start_points=pts)
        g += point(pts, color='red')
        sphinx_plot(g)

    .. NOTE::

        Streamlines currently pass close to ``start_points`` but do
        not necessarily pass directly through them. That is part of
        the behavior of matplotlib, not an error on your part.
    """
