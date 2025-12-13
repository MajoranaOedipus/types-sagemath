from _typeshed import Incomplete
from sage.misc.decorators import options as options, rename_keyword as rename_keyword
from sage.plot.bezier_path import BezierPath as BezierPath
from sage.plot.circle import circle as circle
from sage.plot.hyperbolic_arc import HyperbolicArcCore as HyperbolicArcCore
from sage.rings.cc import CC as CC

class HyperbolicPolygon(HyperbolicArcCore):
    '''
    Primitive class for hyperbolic polygon type.

    See ``hyperbolic_polygon?`` for information about plotting a hyperbolic
    polygon in the complex plane.

    INPUT:

    - ``pts`` -- coordinates of the polygon (as complex numbers)

    - ``options`` -- dictionary of valid plot options to pass to constructor

    EXAMPLES:

    Note that constructions should use :func:`hyperbolic_polygon` or
    :func:`hyperbolic_triangle`::

         sage: from sage.plot.hyperbolic_polygon import HyperbolicPolygon
         sage: print(HyperbolicPolygon([0, 1/2, I], "UHP", {}))
         Hyperbolic polygon (0.000000000000000, 0.500000000000000, 1.00000000000000*I)
    '''
    path: Incomplete
    def __init__(self, pts, model, options) -> None:
        '''
        Initialize HyperbolicPolygon.

        EXAMPLES::

            sage: from sage.plot.hyperbolic_polygon import HyperbolicPolygon
            sage: HP = HyperbolicPolygon([0, 1/2, I], "UHP", {})
            sage: TestSuite(HP).run(skip =\'_test_pickling\')
        '''

def hyperbolic_polygon(pts, model: str = 'UHP', resolution: int = 200, **options):
    """
    Return a hyperbolic polygon in the hyperbolic plane with vertices ``pts``.

    Type ``?hyperbolic_polygon`` to see all options.

    INPUT:

    - ``pts`` -- list or tuple of complex numbers

    OPTIONS:

    - ``model`` -- (default: ``UHP``) Model used for hyperbolic plane

    - ``alpha`` -- (default: 1)

    - ``fill`` -- (default: ``False``)

    - ``thickness`` -- (default: 1)

    - ``rgbcolor`` -- (default: ``'blue'``)

    - ``linestyle`` -- (default: ``'solid'``) the style of the line, which is
      one of ``'dashed'``, ``'dotted'``, ``'solid'``, ``'dashdot'``, or
      ``'--'``, ``':'``, ``'-'``, ``'-.'``, respectively

    EXAMPLES:

    Show a hyperbolic polygon with coordinates `-1`, `3i`, `2+2i`, `1+i`::

        sage: hyperbolic_polygon([-1,3*I,2+2*I,1+I])
        Graphics object consisting of 1 graphics primitive

    .. PLOT::

        P = hyperbolic_polygon([-1,3*I,2+2*I,1+I])
        sphinx_plot(P)

    With more options::

        sage: hyperbolic_polygon([-1,3*I,2+2*I,1+I], fill=True, color='red')
        Graphics object consisting of 1 graphics primitive

    .. PLOT::

        sphinx_plot(hyperbolic_polygon([-1,3*I,2+2*I,1+I], fill=True, color='red'))

    With a vertex at `\\infty`::

        sage: hyperbolic_polygon([-1,0,1,Infinity], color='green')
        Graphics object consisting of 1 graphics primitive

    .. PLOT::

        from sage.rings.infinity import infinity
        sphinx_plot(hyperbolic_polygon([-1,0,1,infinity], color='green'))

    Poincare disc model is supported via the parameter ``model``.
    Show a hyperbolic polygon in the Poincare disc model with coordinates
    `1`, `i`, `-1`, `-i`::

        sage: hyperbolic_polygon([1,I,-1,-I], model='PD', color='green')
        Graphics object consisting of 2 graphics primitives

    .. PLOT::

        sphinx_plot(hyperbolic_polygon([1,I,-1,-I], model='PD', color='green'))

    With more options::

        sage: hyperbolic_polygon([1,I,-1,-I], model='PD', color='green', fill=True, linestyle='-')
        Graphics object consisting of 2 graphics primitives

    .. PLOT::

        P = hyperbolic_polygon([1,I,-1,-I], model='PD', color='green', fill=True, linestyle='-')
        sphinx_plot(P)

    Klein model is also supported via the parameter ``model``.
    Show a hyperbolic polygon in the Klein model with coordinates
    `1`, `e^{i\\pi/3}`, `e^{i2\\pi/3}`, `-1`, `e^{i4\\pi/3}`, `e^{i5\\pi/3}`::

        sage: p1 = 1
        sage: p2 = (cos(pi/3), sin(pi/3))
        sage: p3 = (cos(2*pi/3), sin(2*pi/3))
        sage: p4 = -1
        sage: p5 = (cos(4*pi/3), sin(4*pi/3))
        sage: p6 = (cos(5*pi/3), sin(5*pi/3))
        sage: hyperbolic_polygon([p1,p2,p3,p4,p5,p6], model='KM', fill=True, color='purple')
        Graphics object consisting of 2 graphics primitives

    .. PLOT::

        p1=1
        p2=(cos(pi/3),sin(pi/3))
        p3=(cos(2*pi/3),sin(2*pi/3))
        p4=-1
        p5=(cos(4*pi/3),sin(4*pi/3))
        p6=(cos(5*pi/3),sin(5*pi/3))
        P = hyperbolic_polygon([p1,p2,p3,p4,p5,p6], model='KM', fill=True, color='purple')
        sphinx_plot(P)

    Hyperboloid model is supported partially,  via the parameter ``model``.
    Show a hyperbolic polygon in the hyperboloid model with coordinates
    `(3,3,\\sqrt(19))`, `(3,-3,\\sqrt(19))`, `(-3,-3,\\sqrt(19))`,
    `(-3,3,\\sqrt(19))`::

        sage: pts = [(3,3,sqrt(19)),(3,-3,sqrt(19)),(-3,-3,sqrt(19)),(-3,3,sqrt(19))]
        sage: hyperbolic_polygon(pts, model='HM')
        Graphics3d Object

    .. PLOT::

        pts = [(3,3,sqrt(19)),(3,-3,sqrt(19)),(-3,-3,sqrt(19)),(-3,3,sqrt(19))]
        P = hyperbolic_polygon(pts, model='HM')
        sphinx_plot(P)

    Filling a hyperbolic_polygon in hyperboloid model is possible although
    jaggy. We show a filled hyperbolic polygon in the hyperboloid model
    with coordinates `(1,1,\\sqrt(3))`, `(0,2,\\sqrt(5))`, `(2,0,\\sqrt(5))`.
    (The doctest is done at lower resolution than the picture below to
    give a faster result.) ::

        sage: pts = [(1,1,sqrt(3)), (0,2,sqrt(5)), (2,0,sqrt(5))]
        sage: hyperbolic_polygon(pts, model='HM', resolution=50,
        ....:                    color='yellow', fill=True)
        Graphics3d Object

    .. PLOT::

        pts = [(1,1,sqrt(3)),(0,2,sqrt(5)),(2,0,sqrt(5))]
        P = hyperbolic_polygon(pts, model='HM', color='yellow', fill=True)
        sphinx_plot(P)
    """
def hyperbolic_triangle(a, b, c, model: str = 'UHP', **options):
    """
    Return a hyperbolic triangle in the hyperbolic plane with
    vertices ``(a,b,c)``.

    Type ``?hyperbolic_polygon`` to see all options.

    INPUT:

    - ``a``, ``b``, ``c`` -- complex numbers in the upper half complex plane

    OPTIONS:

    - ``alpha`` -- (default: 1)

    - ``fill`` -- (default: ``False``)

    - ``thickness`` -- (default: 1)

    - ``rgbcolor`` -- (default: ``'blue'``)

    - ``linestyle`` -- (default: ``'solid'``) the style of the line, which is
      one of ``'dashed'``, ``'dotted'``, ``'solid'``, ``'dashdot'``, or
      ``'--'``, ``':'``, ``'-'``, ``'-.'``, respectively

    EXAMPLES:

    Show a hyperbolic triangle with coordinates `0`, `1/2 + i\\sqrt{3}/2` and
    `-1/2 + i\\sqrt{3}/2`::

         sage: hyperbolic_triangle(0, -1/2+I*sqrt(3)/2, 1/2+I*sqrt(3)/2)
         Graphics object consisting of 1 graphics primitive

    .. PLOT::

        P = hyperbolic_triangle(0, 0.5*(-1+I*sqrt(3)), 0.5*(1+I*sqrt(3)))
        sphinx_plot(P)

    A hyperbolic triangle with coordinates `0`, `1` and `2+i` and a dashed line::

         sage: hyperbolic_triangle(0, 1, 2+i, fill=true, rgbcolor='red', linestyle='--')
         Graphics object consisting of 1 graphics primitive

    .. PLOT::

        P = hyperbolic_triangle(0, 1, 2+i, fill=true, rgbcolor='red', linestyle='--')
        sphinx_plot(P)

    A hyperbolic triangle with a vertex at `\\infty`::

        sage: hyperbolic_triangle(-5,Infinity,5)
        Graphics object consisting of 1 graphics primitive

    .. PLOT::

        from sage.rings.infinity import infinity
        sphinx_plot(hyperbolic_triangle(-5,infinity,5))

    It can also plot a hyperbolic triangle in the Poincaré disk model::

        sage: z1 = CC((cos(pi/3),sin(pi/3)))
        sage: z2 = CC((0.6*cos(3*pi/4),0.6*sin(3*pi/4)))
        sage: z3 = 1
        sage: hyperbolic_triangle(z1, z2, z3, model='PD', color='red')
        Graphics object consisting of 2 graphics primitives

    .. PLOT::

        z1 = CC((cos(pi/3),sin(pi/3)))
        z2 = CC((0.6*cos(3*pi/4),0.6*sin(3*pi/4)))
        z3 = 1
        P = hyperbolic_triangle(z1, z2, z3, model='PD', color='red')
        sphinx_plot(P)

    ::

        sage: hyperbolic_triangle(0.3+0.3*I, 0.8*I, -0.5-0.5*I, model='PD', color='magenta')
        Graphics object consisting of 2 graphics primitives

    .. PLOT::

        P = hyperbolic_triangle(0.3+0.3*I, 0.8*I, -0.5-0.5*I, model='PD', color='magenta')
        sphinx_plot(P)
    """
