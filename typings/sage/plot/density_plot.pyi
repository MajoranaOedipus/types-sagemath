from _typeshed import Incomplete
from sage.arith.srange import xsrange as xsrange
from sage.misc.decorators import options as options
from sage.plot.colors import get_cmap as get_cmap
from sage.plot.primitive import GraphicPrimitive as GraphicPrimitive

class DensityPlot(GraphicPrimitive):
    """
    Primitive class for the density plot graphics type.  See
    ``density_plot?`` for help actually doing density plots.

    INPUT:

    - ``xy_data_array`` -- list of lists giving evaluated values of the
      function on the grid

    - ``xrange`` -- tuple of 2 floats indicating range for horizontal direction

    - ``yrange`` -- tuple of 2 floats indicating range for vertical direction

    - ``options`` -- dictionary of valid plot options to pass to constructor

    EXAMPLES:

    Note this should normally be used indirectly via ``density_plot``::

        sage: from sage.plot.density_plot import DensityPlot
        sage: D = DensityPlot([[1,3],[2,4]], (1,2), (2,3),options={})
        sage: D
        DensityPlot defined by a 2 x 2 data grid
        sage: D.yrange
        (2, 3)
        sage: D.options()
        {}

    TESTS:

    We test creating a density plot::

        sage: x,y = var('x,y')
        sage: density_plot(x^2 - y^3 + 10*sin(x*y), (x,-4,4), (y,-4,4), plot_points=121, cmap='hsv')
        Graphics object consisting of 1 graphics primitive
    """
    xrange: Incomplete
    yrange: Incomplete
    xy_data_array: Incomplete
    xy_array_row: Incomplete
    xy_array_col: Incomplete
    def __init__(self, xy_data_array, xrange, yrange, options) -> None:
        """
        Initialize base class ``DensityPlot``.

        EXAMPLES::

            sage: x,y = var('x,y')
            sage: D = density_plot(x^2 - y^3 + 10*sin(x*y), (x,-4,4), (y,-4,4), plot_points=121, cmap='hsv')
            sage: D[0].xrange
            (-4.0, 4.0)
            sage: D[0].options()['plot_points']
            121
        """
    def get_minmax_data(self):
        """
        Return a dictionary with the bounding box data.

        EXAMPLES::

            sage: x,y = var('x,y')
            sage: f(x, y) = x^2 + y^2
            sage: d = density_plot(f, (3,6), (3,6))[0].get_minmax_data()
            sage: d['xmin']
            3.0
            sage: d['ymin']
            3.0
        """

def density_plot(f, xrange, yrange, **options):
    '''
    ``density_plot`` takes a function of two variables, `f(x,y)`
    and plots the height of the function over the specified
    ``xrange`` and ``yrange`` as demonstrated below.

    ``density_plot(f, (xmin,xmax), (ymin,ymax), ...)``

    INPUT:

    - ``f`` -- a function of two variables

    - ``(xmin, xmax)`` -- 2-tuple, the range of ``x`` values OR 3-tuple
      ``(x,xmin,xmax)``

    - ``(ymin, ymax)`` -- 2-tuple, the range of ``y`` values OR 3-tuple
      ``(y,ymin,ymax)``

    The following inputs must all be passed in as named parameters:

    - ``plot_points`` -- integer (default: 25); number of points to plot
      in each direction of the grid

    - ``cmap`` -- a colormap (default: ``\'gray\'``), the name of
      a predefined colormap, a list of colors or an instance of a matplotlib
      Colormap. Type: ``import matplotlib.cm; matplotlib.cm.datad.keys()``
      for available colormap names.

    - ``interpolation`` -- string (default: ``\'catrom\'``); the interpolation
      method to use: ``\'bilinear\'``, ``\'bicubic\'``, ``\'spline16\'``,
      ``\'spline36\'``, ``\'quadric\'``, ``\'gaussian\'``, ``\'sinc\'``,
      ``\'bessel\'``, ``\'mitchell\'``, ``\'lanczos\'``, ``\'catrom\'``,
      ``\'hermite\'``, ``\'hanning\'``, ``\'hamming\'``, ``\'kaiser\'``

    EXAMPLES:

    Here we plot a simple function of two variables.  Note that
    since the input function is an expression, we need to explicitly
    declare the variables in 3-tuples for the range::

        sage: x,y = var(\'x,y\')
        sage: density_plot(sin(x) * sin(y), (x,-2,2), (y,-2,2))
        Graphics object consisting of 1 graphics primitive

    .. PLOT::

        x,y = var(\'x,y\')
        g = density_plot(sin(x) * sin(y), (x,-2,2), (y,-2,2))
        sphinx_plot(g)

    Here we change the ranges and add some options; note that here
    ``f`` is callable (has variables declared), so we can use 2-tuple ranges::

        sage: x,y = var(\'x,y\')
        sage: f(x,y) = x^2 * cos(x*y)
        sage: density_plot(f, (x,-10,5), (y,-5,5), interpolation=\'sinc\', plot_points=100)
        Graphics object consisting of 1 graphics primitive

    .. PLOT::

        x,y = var(\'x,y\')
        def f(x, y): return x**2 * cos(x*y)
        g = density_plot(f, (x,-10,5), (y,-5,5), interpolation=\'sinc\', plot_points=100)
        sphinx_plot(g)

    An even more complicated plot::

        sage: x,y = var(\'x,y\')
        sage: density_plot(sin(x^2+y^2) * cos(x) * sin(y), (x,-4,4), (y,-4,4), cmap=\'jet\', plot_points=100)
        Graphics object consisting of 1 graphics primitive

    .. PLOT::

        x,y = var(\'x,y\')
        g = density_plot(sin(x**2 + y**2)*cos(x)*sin(y), (x,-4,4), (y,-4,4), cmap=\'jet\', plot_points=100)
        sphinx_plot(g)

    This should show a "spotlight" right on the origin::

        sage: x,y = var(\'x,y\')
        sage: density_plot(1/(x^10 + y^10), (x,-10,10), (y,-10,10))
        Graphics object consisting of 1 graphics primitive

    .. PLOT::

        x,y = var(\'x,y\')
        g = density_plot(1/(x**10 + y**10), (x,-10,10), (y,-10,10))
        sphinx_plot(g)

    Some elliptic curves, but with symbolic endpoints.  In the first
    example, the plot is rotated 90 degrees because we switch the
    variables `x`, `y`::

        sage: density_plot(y^2 + 1 - x^3 - x, (y,-pi,pi), (x,-pi,pi))
        Graphics object consisting of 1 graphics primitive

    .. PLOT::

        x,y = var(\'x,y\')
        g = density_plot(y**2 + 1 - x**3 - x, (y,-pi,pi), (x,-pi,pi))
        sphinx_plot(g)

    ::

        sage: density_plot(y^2 + 1 - x^3 - x, (x,-pi,pi), (y,-pi,pi))
        Graphics object consisting of 1 graphics primitive

    .. PLOT::

        x,y = var(\'x,y\')
        g = density_plot(y**2 + 1 - x**3 - x, (x,-pi,pi), (y,-pi,pi))
        sphinx_plot(g)

    Extra options will get passed on to show(), as long as they are valid::

        sage: density_plot(log(x) + log(y), (x,1,10), (y,1,10), aspect_ratio=1)
        Graphics object consisting of 1 graphics primitive

    .. PLOT::

        x,y = var(\'x,y\')
        g = density_plot(log(x) + log(y), (x,1,10), (y,1,10), aspect_ratio=1)
        sphinx_plot(g)

    ::

        sage: density_plot(log(x) + log(y), (x,1,10), (y,1,10)).show(aspect_ratio=1) # These are equivalent

    TESTS:

    Check that :issue:`15315` is fixed, i.e., density_plot respects the
    ``aspect_ratio`` parameter. Without the fix, it looks like a thin line
    of width a few mm. With the fix it should look like a nice fat layered
    image::

        sage: density_plot((x*y)^(1/2), (x,0,3), (y,0,500), aspect_ratio=.01)
        Graphics object consisting of 1 graphics primitive

    Default ``aspect_ratio`` is ``\'automatic\'``, and that should work too::

        sage: density_plot((x*y)^(1/2), (x,0,3), (y,0,500))
        Graphics object consisting of 1 graphics primitive

    Check that :issue:`17684` is fixed, i.e., symbolic values can be plotted::

        sage: def f(x, y):
        ....:     return SR(x)
        sage: density_plot(f, (0,1), (0,1))
        Graphics object consisting of 1 graphics primitive
    '''
