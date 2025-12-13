from .primitive import GraphicPrimitive as GraphicPrimitive
from _typeshed import Incomplete
from sage.misc.decorators import options as options, rename_keyword as rename_keyword
from sage.plot.colors import to_mpl_color as to_mpl_color

class Circle(GraphicPrimitive):
    """
    Primitive class for the :class:`Circle` graphics type.  See ``circle?`` for information
    about actually plotting circles.

    INPUT:

    - ``x`` -- `x`-coordinate of center of Circle

    - ``y`` -- `y`-coordinate of center of Circle

    - ``r`` -- radius of Circle object

    - ``options`` -- dictionary of valid plot options to pass to constructor

    EXAMPLES:

    Note this should normally be used indirectly via ``circle``::

        sage: from sage.plot.circle import Circle
        sage: C = Circle(2,3,5,{'zorder':2})
        sage: C
        Circle defined by (2.0,3.0) with r=5.0
        sage: C.options()['zorder']
        2
        sage: C.r
        5.0

    TESTS:

    We test creating a circle::

        sage: C = circle((2,3), 5)
    """
    x: Incomplete
    y: Incomplete
    r: Incomplete
    def __init__(self, x, y, r, options) -> None:
        """
        Initialize base class Circle.

        EXAMPLES::

            sage: C = circle((2,3), 5, edgecolor='red', alpha=.5, fill=True)
            sage: C[0].x
            2.0
            sage: C[0].r
            5.0
            sage: C[0].options()['edgecolor']
            'red'
            sage: C[0].options()['alpha']
            0.500000000000000
        """
    def get_minmax_data(self):
        """
        Return a dictionary with the bounding box data.

        EXAMPLES::

            sage: p = circle((3, 3), 1)
            sage: d = p.get_minmax_data()
            sage: d['xmin']
            2.0
            sage: d['ymin']
            2.0
        """
    def plot3d(self, z: int = 0, **kwds):
        """
        Plots a 2D circle (actually a 50-gon) in 3D,
        with default height zero.

        INPUT:

        - ``z`` -- (optional) 3D height above `xy`-plane

        EXAMPLES::

            sage: circle((0,0), 1).plot3d()
            Graphics3d Object

        This example uses this method implicitly, but does not pass
        the optional parameter z to this method::

            sage: sum(circle((random(),random()), random()).plot3d(z=random())
            ....:     for _ in range(20))
            Graphics3d Object

        .. PLOT::

            P = sum([circle((random(),random()), random()).plot3d(z=random()) for _ in range(20)])
            sphinx_plot(P)

        These examples are explicit, and pass z to this method::

            sage: from math import pi
            sage: C = circle((2,pi), 2, hue=.8, alpha=.3, fill=True)
            sage: c = C[0]
            sage: d = c.plot3d(z=2)
            sage: d.texture.opacity
            0.3

        ::

            sage: C = circle((2,pi), 2, hue=.8, alpha=.3, linestyle='dotted')
            sage: c = C[0]
            sage: d = c.plot3d(z=2)
            sage: d.jmol_repr(d.testing_render_params())[0][-1]
            'color $line_1 translucent 0.7 [204,0,255]'
        """

def circle(center, radius, **options):
    """
    Return a circle at a point center = `(x,y)` (or `(x,y,z)` and
    parallel to the `xy`-plane) with radius = `r`.  Type
    ``circle.options`` to see all options.

    OPTIONS:

    - ``alpha`` -- (default: 1)

    - ``fill`` -- (default: ``False``)

    - ``thickness`` -- (default: 1)

    - ``linestyle`` -- (default: ``'solid'``) (2D plotting only) the style of the
      line, which is one of ``'dashed'``, ``'dotted'``, ``'solid'``, ``'dashdot'``,
      or ``'--'``, ``':'``, ``'-'``, ``'-.'``, respectively

    - ``edgecolor`` -- (default: ``'blue'``) 2D plotting only

    - ``facecolor`` -- (default: ``'blue'``) 2D plotting only, useful only
      if ``fill=True``

    - ``rgbcolor`` -- 2D or 3D plotting.  This option overrides
      ``edgecolor`` and ``facecolor`` for 2D plotting

    - ``legend_label`` -- the label for this item in the legend

    - ``legend_color`` -- the color for the legend label

    EXAMPLES:

    The default color is blue, the default linestyle is solid, but this is easy to change::

        sage: c = circle((1,1), 1)
        sage: c
        Graphics object consisting of 1 graphics primitive

    .. PLOT::

        sphinx_plot(circle((1,1), 1))

    ::

        sage: c = circle((1,1), 1, rgbcolor=(1,0,0), linestyle='-.')
        sage: c
        Graphics object consisting of 1 graphics primitive

    .. PLOT::

        c = circle((1,1), 1, rgbcolor=(1,0,0), linestyle='-.')
        sphinx_plot(c)

    We can also use this command to plot three-dimensional circles parallel
    to the `xy`-plane::

        sage: c = circle((1,1,3), 1, rgbcolor=(1,0,0))
        sage: c
        Graphics3d Object
        sage: type(c)
        <class 'sage.plot.plot3d.base.TransformGroup'>

    .. PLOT::

        c = circle((1,1,3), 1, rgbcolor=(1,0,0))
        sphinx_plot(c)

    To correct the aspect ratio of certain graphics, it is necessary
    to show with a ``figsize`` of square dimensions::

        sage: c.show(figsize=[5,5],xmin=-1,xmax=3,ymin=-1,ymax=3)

    Here we make a more complicated plot, with many circles of different colors::

        sage: g = Graphics()
        sage: step = 6; ocur = 1/5; paths = 16
        sage: PI = math.pi    # numerical for speed -- fine for graphics
        sage: for r in range(1,paths+1):
        ....:     for x,y in [((r+ocur)*math.cos(n), (r+ocur)*math.sin(n))
        ....:                 for n in srange(0, 2*PI+PI/step, PI/step)]:
        ....:         g += circle((x,y), ocur, rgbcolor=hue(r/paths))
        ....:     rnext = (r+1)^2
        ....:     ocur = (rnext-r)-ocur
        sage: g.show(xmin=-(paths+1)^2, xmax=(paths+1)^2,
        ....:        ymin=-(paths+1)^2, ymax=(paths+1)^2, figsize=[6,6])

    .. PLOT::

        g = Graphics()
        step=6; ocur=1/5; paths=16;
        PI = math.pi    # numerical for speed -- fine for graphics
        for r in range(1,paths+1):
             for x,y in [((r+ocur)*math.cos(n), (r+ocur)*math.sin(n)) for n in srange(0, 2*PI+PI/step, PI/step)]:
                 g += circle((x,y), ocur, rgbcolor=hue(r*1.0/paths))
             rnext = (r+1)**2
             ocur = (rnext-r)-ocur
        g.set_axes_range(-(paths+1)**2,(paths+1)**2,-(paths+1)**2,(paths+1)**2)
        sphinx_plot(g)

    Note that the ``rgbcolor`` option overrides the other coloring options.
    This produces red fill in a blue circle::

        sage: circle((2,3), 1, fill=True, edgecolor='blue', facecolor='red')
        Graphics object consisting of 1 graphics primitive

    .. PLOT::

        sphinx_plot(circle((2,3), 1, fill=True, edgecolor='blue', facecolor='red'))

    This produces an all-green filled circle::

        sage: circle((2,3), 1, fill=True, edgecolor='blue', rgbcolor='green')
        Graphics object consisting of 1 graphics primitive

    .. PLOT::

        sphinx_plot(circle((2,3), 1, fill=True, edgecolor='blue', rgbcolor='green'))

    The option ``hue`` overrides *all* other options, so be careful with its use.
    This produces a purplish filled circle::

        sage: circle((2,3), 1, fill=True, edgecolor='blue', rgbcolor='green', hue=.8)
        Graphics object consisting of 1 graphics primitive

    .. PLOT::

        C = circle((2,3), 1, fill=True, edgecolor='blue', rgbcolor='green', hue=.8)
        sphinx_plot(C)

    And circles with legends::

        sage: circle((4,5), 1, rgbcolor='yellow', fill=True,
        ....:        legend_label='the sun').show(xmin=0, ymin=0)

    .. PLOT::

        C = circle((4,5), 1, rgbcolor='yellow', fill=True, legend_label='the sun')
        C.set_axes_range(xmin=0, ymin=0)
        sphinx_plot(C)

    ::

        sage: circle((4,5), 1,
        ....:        legend_label='the sun', legend_color='yellow').show(xmin=0, ymin=0)

    .. PLOT::

        C = circle((4,5), 1, legend_label='the sun', legend_color='yellow')
        C.set_axes_range(xmin=0, ymin=0)
        sphinx_plot(C)

    Extra options will get passed on to show(), as long as they are valid::

        sage: circle((0, 0), 2, figsize=[10,10])  # That circle is huge!
        Graphics object consisting of 1 graphics primitive

    ::

        sage: circle((0, 0), 2).show(figsize=[10,10])  # These are equivalent

    TESTS:

    We cannot currently plot circles in more than three dimensions::

        sage: circle((1,1,1,1), 1, rgbcolor=(1,0,0))
        Traceback (most recent call last):
        ...
        ValueError: the center of a plotted circle should have two or three coordinates

    The default aspect ratio for a circle is 1.0::

        sage: P = circle((1,1), 1)
        sage: P.aspect_ratio()
        1.0

    Verify that :issue:`36153` does not arise::

        sage: C = circle((1,1), 1, legend_label='test')
    """
