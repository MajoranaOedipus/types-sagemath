from .primitive import GraphicPrimitive as GraphicPrimitive
from _typeshed import Incomplete
from sage.misc.decorators import options as options, rename_keyword as rename_keyword
from sage.plot.colors import to_mpl_color as to_mpl_color

class Ellipse(GraphicPrimitive):
    """
    Primitive class for the ``Ellipse`` graphics type.  See ``ellipse?`` for
    information about actually plotting ellipses.

    INPUT:

    - ``x``, ``y`` -- coordinates of the center of the ellipse

    - ``r1``, ``r2`` -- radii of the ellipse

    - ``angle`` -- angle

    - ``options`` -- dictionary of options

    EXAMPLES:

    Note that this construction should be done using ``ellipse``::

        sage: from math import pi
        sage: from sage.plot.ellipse import Ellipse
        sage: Ellipse(0, 0, 2, 1, pi/4, {})
        Ellipse centered at (0.0, 0.0) with radii (2.0, 1.0) and angle 0.78539816339...
    """
    x: Incomplete
    y: Incomplete
    r1: Incomplete
    r2: Incomplete
    angle: Incomplete
    def __init__(self, x, y, r1, r2, angle, options) -> None:
        """
        Initialize base class ``Ellipse``.

        TESTS::

            sage: from sage.plot.ellipse import Ellipse
            sage: e = Ellipse(0, 0, 1, 1, 0, {})
            sage: print(loads(dumps(e)))
            Ellipse centered at (0.0, 0.0) with radii (1.0, 1.0) and angle 0.0
            sage: ellipse((0,0),0,1)
            Traceback (most recent call last):
            ...
            ValueError: both radii must be positive
        """
    def get_minmax_data(self):
        """
        Return a dictionary with the bounding box data.

        The bounding box is computed to be as minimal as possible.

        EXAMPLES:

        An example without an angle::

            sage: p = ellipse((-2, 3), 1, 2)
            sage: d = p.get_minmax_data()
            sage: d['xmin']
            -3.0
            sage: d['xmax']
            -1.0
            sage: d['ymin']
            1.0
            sage: d['ymax']
            5.0

        The same example with a rotation of angle `\\pi/2`::

            sage: from math import pi
            sage: p = ellipse((-2, 3), 1, 2, pi/2)
            sage: d = p.get_minmax_data()
            sage: d['xmin']
            -4.0
            sage: d['xmax']
            0.0
            sage: d['ymin']
            2.0
            sage: d['ymax']
            4.0
        """
    def plot3d(self) -> None:
        """
        Plotting in 3D is not implemented.

        TESTS::

            sage: from sage.plot.ellipse import Ellipse
            sage: Ellipse(0,0,2,1,pi/4,{}).plot3d()                                     # needs sage.symbolic
            Traceback (most recent call last):
            ...
            NotImplementedError
        """

def ellipse(center, r1, r2, angle: int = 0, **options):
    '''
    Return an ellipse centered at a point center = ``(x,y)`` with radii =
    ``r1,r2`` and angle ``angle``.  Type ``ellipse.options`` to see all
    options.

    INPUT:

    - ``center`` -- 2-tuple of real numbers; coordinates of the center

    - ``r1``, ``r2`` -- positive real numbers; the radii of the ellipse

    - ``angle`` -- real number (default: 0) -- the angle between the first axis
      and the horizontal

    OPTIONS:

    - ``alpha`` -- (default: 1) transparency

    - ``fill`` -- (default: ``False``) whether to fill the ellipse or not

    - ``thickness`` -- (default: 1) thickness of the line

    - ``linestyle`` -- (default: ``\'solid\'``) the style of the line, which is one
      of ``\'dashed\'``, ``\'dotted\'``, ``\'solid\'``, ``\'dashdot\'``, or ``\'--\'``,
      ``\':\'``, ``\'-\'``, ``\'-.\'``,  respectively

    - ``edgecolor`` -- (default: ``\'black\'``) color of the contour

    - ``facecolor`` -- (default: ``\'red\'``) color of the filling

    - ``rgbcolor`` -- 2D or 3D plotting.  This option overrides
      ``edgecolor`` and ``facecolor`` for 2D plotting

    - ``legend_label`` -- the label for this item in the legend

    - ``legend_color`` -- the color for the legend label

    EXAMPLES:

    An ellipse centered at (0,0) with major and minor axes of lengths 2 and 1.
    Note that the default color is blue::

        sage: ellipse((0,0),2,1)
        Graphics object consisting of 1 graphics primitive

    .. PLOT::

        E=ellipse((0,0),2,1)
        sphinx_plot(E)

    More complicated examples with tilted axes and drawing options::

        sage: from math import pi
        sage: ellipse((0,0), 3, 1, pi/6, fill=True, alpha=0.3, linestyle=\'dashed\')
        Graphics object consisting of 1 graphics primitive

    .. PLOT::

        E = ellipse((0,0),3,1,pi/6,fill=True,alpha=0.3,linestyle=\'dashed\')
        sphinx_plot(E)

    other way to indicate dashed linestyle::

        sage: ellipse((0,0),3,1,pi/6,fill=True,alpha=0.3,linestyle=\'--\')
        Graphics object consisting of 1 graphics primitive

    .. PLOT::

        E =ellipse((0,0),3,1,pi/6,fill=True,alpha=0.3,linestyle=\'--\')
        sphinx_plot(E)

    with colors ::

        sage: ellipse((0,0),3,1,pi/6,fill=True,edgecolor=\'black\',facecolor=\'red\')
        Graphics object consisting of 1 graphics primitive

    .. PLOT::

        E=ellipse((0,0),3,1,pi/6,fill=True,edgecolor=\'black\',facecolor=\'red\')
        sphinx_plot(E)

    We see that ``rgbcolor`` overrides these other options, as this plot
    is green::

        sage: ellipse((0,0),3,1,pi/6,fill=True,edgecolor=\'black\',facecolor=\'red\',rgbcolor=\'green\')
        Graphics object consisting of 1 graphics primitive

    .. PLOT::

        E=ellipse((0,0),3,1,pi/6,fill=True,edgecolor=\'black\',facecolor=\'red\',rgbcolor=\'green\')
        sphinx_plot(E)

    The default aspect ratio for ellipses is 1.0::

        sage: ellipse((0,0),2,1).aspect_ratio()
        1.0

    One cannot yet plot ellipses in 3D::

        sage: ellipse((0,0,0),2,1)
        Traceback (most recent call last):
        ...
        NotImplementedError: plotting ellipse in 3D is not implemented

    We can also give ellipses a legend::

        sage: ellipse((0,0),2,1,legend_label="My ellipse", legend_color=\'green\')
        Graphics object consisting of 1 graphics primitive

    .. PLOT::

        E=ellipse((0,0),2,1,legend_label="My ellipse", legend_color=\'green\')
        sphinx_plot(E)

    TESTS:

    Verify that :issue:`36153` does not arise::

        sage: E = ellipse((0,0), 2, 1, legend_label=\'test\')
    '''
