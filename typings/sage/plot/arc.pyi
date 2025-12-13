from _typeshed import Incomplete
from sage.misc.decorators import options as options, rename_keyword as rename_keyword
from sage.plot.colors import to_mpl_color as to_mpl_color
from sage.plot.primitive import GraphicPrimitive as GraphicPrimitive

class Arc(GraphicPrimitive):
    """
    Primitive class for the Arc graphics type.  See ``arc?`` for information
    about actually plotting an arc of a circle or an ellipse.

    INPUT:

    - ``x``, ``y`` -- coordinates of the center of the arc

    - ``r1``, ``r2`` -- lengths of the two radii

    - ``angle`` -- angle of the horizontal with width

    - ``sector`` -- sector of angle

    - ``options`` -- dictionary of valid plot options to pass to constructor

    EXAMPLES:

    Note that the construction should be done using ``arc``::

        sage: from math import pi
        sage: from sage.plot.arc import Arc
        sage: print(Arc(0,0,1,1,pi/4,pi/4,pi/2,{}))
        Arc with center (0.0,0.0) radii (1.0,1.0) angle 0.78539816339... inside the sector (0.78539816339...,1.5707963267...)
    """
    x: Incomplete
    y: Incomplete
    r1: Incomplete
    r2: Incomplete
    angle: Incomplete
    s1: Incomplete
    s2: Incomplete
    def __init__(self, x, y, r1, r2, angle, s1, s2, options) -> None:
        """
        Initialize base class ``Arc``.

        EXAMPLES::

            sage: # needs sage.symbolic
            sage: A = arc((2,3),1,1,pi/4,(0,pi))
            sage: A[0].x == 2
            True
            sage: A[0].y == 3
            True
            sage: A[0].r1 == 1
            True
            sage: A[0].r2 == 1
            True
            sage: A[0].angle
            0.7853981633974483
            sage: bool(A[0].s1 == 0)
            True
            sage: A[0].s2
            3.141592653589793

        TESTS::

            sage: from sage.plot.arc import Arc
            sage: a = Arc(0,0,1,1,0,0,1,{})
            sage: print(loads(dumps(a)))
            Arc with center (0.0,0.0) radii (1.0,1.0) angle 0.0 inside the sector (0.0,1.0)
        """
    def get_minmax_data(self):
        """
        Return a dictionary with the bounding box data.

        The bounding box is computed as minimal as possible.

        EXAMPLES:

        An example without angle::

            sage: p = arc((-2, 3), 1, 2)
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
            sage: p = arc((-2, 3), 1, 2, pi/2)
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
    def bezier_path(self):
        """
        Return ``self`` as a Bezier path.

        This is needed to concatenate arcs, in order to
        create hyperbolic polygons.

        EXAMPLES::

            sage: from sage.plot.arc import Arc
            sage: op = {'alpha':1,'thickness':1,'rgbcolor':'blue','zorder':0,
            ....:     'linestyle':'--'}
            sage: Arc(2,3,2.2,2.2,0,2,3,op).bezier_path()
            Graphics object consisting of 1 graphics primitive

            sage: from math import pi
            sage: a = arc((0,0),2,1,0,(pi/5,pi/2+pi/12), linestyle='--', color='red')
            sage: b = a[0].bezier_path()
            sage: b[0]
            Bezier path from (1.133..., 0.8237...) to (-0.2655..., 0.9911...)
        """
    def plot3d(self) -> None:
        """
        TESTS::

            sage: from sage.plot.arc import Arc
            sage: Arc(0,0,1,1,0,0,1,{}).plot3d()
            Traceback (most recent call last):
            ...
            NotImplementedError
        """

def arc(center, r1, r2=None, angle: float = 0.0, sector=..., **options):
    """
    An arc (that is a portion of a circle or an ellipse).

    Type ``arc.options`` to see all options.

    INPUT:

    - ``center`` -- 2-tuple of real numbers; position of the center

    - ``r1``, ``r2`` -- positive real numbers; radii of the ellipse. If only ``r1``
      is set, then the two radii are supposed to be equal and this function returns
      an arc of circle.

    - ``angle`` -- real number; angle between the horizontal and the axis that
      corresponds to ``r1``

    - ``sector`` -- 2-tuple (default: (0,2*pi)); angles sector in which the arc will
      be drawn

    OPTIONS:

    - ``alpha`` -- float (default: 1) -- transparency

    - ``thickness`` -- float (default: 1) -- thickness of the arc

    - ``color``, ``rgbcolor`` -- string or 2-tuple (default: ``'blue'``); the
      color of the arc

    - ``linestyle`` -- string (default: ``'solid'``); the style of the line,
      which is one of ``'dashed'``, ``'dotted'``, ``'solid'``, ``'dashdot'``,
      or ``'--'``, ``':'``, ``'-'``, ``'-.'``, respectively

    EXAMPLES:

    Plot an arc of circle centered at (0,0) with radius 1 in the sector
    `(\\pi/4,3*\\pi/4)`::

        sage: from math import pi
        sage: arc((0,0), 1, sector=(pi/4,3*pi/4))
        Graphics object consisting of 1 graphics primitive

    .. PLOT::

        sphinx_plot(arc((0,0), 1, sector=(pi/4,3*pi/4)))

    Plot an arc of an ellipse between the angles 0 and `\\pi/2`::

        sage: arc((2,3), 2, 1, sector=(0,pi/2))
        Graphics object consisting of 1 graphics primitive

    .. PLOT::

        sphinx_plot(arc((2,3), 2, 1, sector=(0,pi/2)))

    Plot an arc of a rotated ellipse between the angles 0 and `\\pi/2`::

        sage: arc((2,3), 2, 1, angle=pi/5, sector=(0,pi/2))
        Graphics object consisting of 1 graphics primitive

    .. PLOT::

        sphinx_plot(arc((2,3), 2, 1, angle=pi/5, sector=(0,pi/2)))

    Plot an arc of an ellipse in red with a dashed linestyle::

        sage: arc((0,0), 2, 1, 0, (0,pi/2), linestyle='dashed', color='red')
        Graphics object consisting of 1 graphics primitive
        sage: arc((0,0), 2, 1, 0, (0,pi/2), linestyle='--', color='red')
        Graphics object consisting of 1 graphics primitive

    .. PLOT::

        sphinx_plot(arc((0,0), 2, 1, 0, (0,pi/2), linestyle='dashed', color='red'))

    The default aspect ratio for arcs is 1.0::

        sage: arc((0,0), 1, sector=(pi/4,3*pi/4)).aspect_ratio()
        1.0

    It is not possible to draw arcs in 3D::

        sage: A = arc((0,0,0), 1)
        Traceback (most recent call last):
        ...
        NotImplementedError
    """
