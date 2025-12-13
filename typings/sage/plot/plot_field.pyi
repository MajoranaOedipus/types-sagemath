from _typeshed import Incomplete
from sage.arith.srange import xsrange as xsrange
from sage.misc.decorators import options as options
from sage.plot.primitive import GraphicPrimitive as GraphicPrimitive

class PlotField(GraphicPrimitive):
    """
    Primitive class that initializes the
    PlotField graphics type
    """
    xpos_array: Incomplete
    ypos_array: Incomplete
    xvec_array: Incomplete
    yvec_array: Incomplete
    def __init__(self, xpos_array, ypos_array, xvec_array, yvec_array, options) -> None:
        """
        Create the graphics primitive PlotField.  This sets options
        and the array to be plotted as attributes.

        EXAMPLES::

            sage: x,y = var('x,y')
            sage: R=plot_slope_field(x + y, (x,0,1), (y,0,1), plot_points=2)
            sage: r=R[0]
            sage: r.options()['headaxislength']
            0
            sage: r.xpos_array
            [0.0, 0.0, 1.0, 1.0]
            sage: r.yvec_array
            masked_array(data=[0.0, 0.70710678118..., 0.70710678118...,
                               0.89442719...],
                         mask=[False, False, False, False],
                   fill_value=1e+20)

        TESTS:

        We test dumping and loading a plot::

            sage: x,y = var('x,y')
            sage: P = plot_vector_field((sin(x),cos(y)), (x,-3,3), (y,-3,3))
            sage: Q = loads(dumps(P))
        """
    def get_minmax_data(self):
        """
        Return a dictionary with the bounding box data.

        EXAMPLES::

            sage: x,y = var('x,y')
            sage: d = plot_vector_field((.01*x,x+y), (x,10,20), (y,10,20))[0].get_minmax_data()
            sage: d['xmin']
            10.0
            sage: d['ymin']
            10.0
        """

def plot_vector_field(f_g, xrange, yrange, **options):
    """
    ``plot_vector_field`` takes two functions of two variables xvar and yvar
    (for instance, if the variables are `x` and `y`, take `(f(x,y), g(x,y))`)
    and plots vector arrows of the function over the specified ranges, with
    xrange being of xvar between xmin and xmax, and yrange similarly
    (see below).

    ``plot_vector_field((f,g), (xvar,xmin,xmax), (yvar,ymin,ymax))``

    EXAMPLES:

    Plot some vector fields involving sin and cos::

        sage: x,y = var('x y')
        sage: plot_vector_field((sin(x),cos(y)), (x,-3,3), (y,-3,3))
        Graphics object consisting of 1 graphics primitive

    .. PLOT::

        x, y = var('x y')
        g = plot_vector_field((sin(x),cos(y)), (x,-3,3), (y,-3,3))
        sphinx_plot(g)

    ::

        sage: plot_vector_field((y,(cos(x)-2) * sin(x)), (x,-pi,pi), (y,-pi,pi))
        Graphics object consisting of 1 graphics primitive

    .. PLOT::

        x, y = var('x y')
        g = plot_vector_field((y,(cos(x)-2) * sin(x)), (x,-pi,pi), (y,-pi,pi))
        sphinx_plot(g)

    Plot a gradient field::

        sage: u, v = var('u v')
        sage: f = exp(-(u^2 + v^2))
        sage: plot_vector_field(f.gradient(), (u,-2,2), (v,-2,2), color='blue')
        Graphics object consisting of 1 graphics primitive

    .. PLOT::

        u, v = var('u v')
        f = exp(-(u**2 + v**2))
        g = plot_vector_field(f.gradient(), (u,-2,2), (v,-2,2), color='blue')
        sphinx_plot(g)

    Plot two orthogonal vector fields::

        sage: x,y = var('x,y')
        sage: a = plot_vector_field((x,y), (x,-3,3), (y,-3,3), color='blue')
        sage: b = plot_vector_field((y,-x), (x,-3,3), (y,-3,3), color='red')
        sage: show(a + b)

    .. PLOT::

        x,y = var('x,y')
        a = plot_vector_field((x,y), (x,-3,3), (y,-3,3), color='blue')
        b = plot_vector_field((y,-x), (x,-3,3), (y,-3,3), color='red')
        sphinx_plot(a + b)

    We ignore function values that are infinite or NaN::

        sage: x,y = var('x,y')
        sage: plot_vector_field((-x/sqrt(x^2+y^2),-y/sqrt(x^2+y^2)), (x,-10,10), (y,-10,10))
        Graphics object consisting of 1 graphics primitive

    .. PLOT::

        x,y = var('x,y')
        g = plot_vector_field((-x/sqrt(x**2+y**2),-y/sqrt(x**2+y**2)), (x,-10,10), (y,-10,10))
        sphinx_plot(g)

    ::

        sage: x,y = var('x,y')
        sage: plot_vector_field((-x/sqrt(x+y),-y/sqrt(x+y)), (x,-10, 10), (y,-10,10))
        Graphics object consisting of 1 graphics primitive

    .. PLOT::

        x,y = var('x,y')
        g = plot_vector_field((-x/sqrt(x+y),-y/sqrt(x+y)), (x,-10,10), (y,-10,10))
        sphinx_plot(g)

    Extra options will get passed on to show(), as long as they are valid::

        sage: plot_vector_field((x,y), (x,-2,2), (y,-2,2), xmax=10)
        Graphics object consisting of 1 graphics primitive
        sage: plot_vector_field((x,y), (x,-2,2), (y,-2,2)).show(xmax=10) # These are equivalent

    .. PLOT::

        x,y = var('x,y')
        g = plot_vector_field((x,y), (x,-2,2), (y,-2,2), xmax=10)
        sphinx_plot(g)
    """
def plot_slope_field(f, xrange, yrange, **kwds):
    """
    ``plot_slope_field`` takes a function of two variables xvar and yvar
    (for instance, if the variables are `x` and `y`, take `f(x,y)`), and at
    representative points `(x_i,y_i)` between xmin, xmax, and ymin, ymax
    respectively, plots a line with slope `f(x_i,y_i)` (see below).

    ``plot_slope_field(f, (xvar,xmin,xmax), (yvar,ymin,ymax))``

    EXAMPLES:

    A logistic function modeling population growth::

        sage: x,y = var('x y')
        sage: capacity = 3 # thousand
        sage: growth_rate = 0.7 # population increases by 70% per unit of time
        sage: plot_slope_field(growth_rate * (1-y/capacity) * y, (x,0,5), (y,0,capacity*2))
        Graphics object consisting of 1 graphics primitive

    .. PLOT::

        x,y = var('x y')
        capacity = 3 # thousand
        growth_rate = 0.7 # population increases by 70% per unit of time
        g = plot_slope_field(growth_rate * (1-y/capacity) * y, (x,0,5), (y,0,capacity*2))
        sphinx_plot(g)

    Plot a slope field involving sin and cos::

        sage: x,y = var('x y')
        sage: plot_slope_field(sin(x+y) + cos(x+y), (x,-3,3), (y,-3,3))
        Graphics object consisting of 1 graphics primitive

    .. PLOT::

        x,y = var('x y')
        g = plot_slope_field(sin(x+y)+cos(x+y), (x,-3,3), (y,-3,3))
        sphinx_plot(g)

    Plot a slope field using a lambda function::

        sage: plot_slope_field(lambda x,y: x + y, (-2,2), (-2,2))
        Graphics object consisting of 1 graphics primitive

    .. PLOT::

        x,y = var('x y')
        g = plot_slope_field(lambda x,y: x + y, (-2,2), (-2,2))
        sphinx_plot(g)

    TESTS:

    Verify that we're not getting warnings due to use of headless quivers
    (:issue:`11208`)::

        sage: x,y = var('x y')
        sage: import numpy # bump warnings up to errors for testing purposes
        sage: old_err = numpy.seterr('raise')
        sage: plot_slope_field(sin(x+y) + cos(x+y), (x,-3,3), (y,-3,3))
        Graphics object consisting of 1 graphics primitive
        sage: dummy_err = numpy.seterr(**old_err)
    """
