from _typeshed import Incomplete
from sage.misc.decorators import options as options, rename_keyword as rename_keyword
from sage.plot.colors import to_mpl_color as to_mpl_color
from sage.plot.primitive import GraphicPrimitive_xydata as GraphicPrimitive_xydata

class Point(GraphicPrimitive_xydata):
    """
    Primitive class for the point graphics type.  See point?, point2d?
    or point3d? for information about actually plotting points.

    INPUT:

    - ``xdata`` -- list of x values for points in Point object

    - ``ydata`` -- list of y values for points in Point object

    - ``options`` -- dictionary of valid plot options to pass to constructor

    EXAMPLES:

    Note this should normally be used indirectly via :func:`point` and friends::

        sage: from sage.plot.point import Point
        sage: P = Point([1,2],[2,3],{'alpha':.5})
        sage: P
        Point set defined by 2 point(s)
        sage: P.options()['alpha']
        0.500000000000000
        sage: P.xdata
        [1, 2]

    TESTS:

    We test creating a point::

        sage: point((3,3))
        Graphics object consisting of 1 graphics primitive
    """
    xdata: Incomplete
    ydata: Incomplete
    def __init__(self, xdata, ydata, options) -> None:
        """
        Initialize base class Point.

        EXAMPLES::

            sage: P = point((3,4))
            sage: P[0].xdata
            [3.0]
            sage: P[0].options()['alpha']
            1
        """
    def plot3d(self, z: int = 0, **kwds):
        """
        Plots a two-dimensional point in 3-D, with default height zero.

        INPUT:

        - ``z`` -- (optional) 3D height above `xy`-plane; may be a list
          if ``self`` is a list of points

        EXAMPLES:

        One point::

            sage: A = point((1, 1))
            sage: a = A[0]; a
            Point set defined by 1 point(s)
            sage: b = a.plot3d()

        .. PLOT::

            A = point((1, 1))
            a = A[0]
            sphinx_plot(a.plot3d())

        One point with a height::

            sage: A = point((1, 1))
            sage: a = A[0]; a
            Point set defined by 1 point(s)
            sage: b = a.plot3d(z=3)
            sage: b.loc[2]
            3.0

        .. PLOT::

            A = point((1, 1))
            a = A[0]
            sphinx_plot(a.plot3d(z=3))

        Multiple points::

            sage: P = point([(0, 0), (1, 1)])
            sage: p = P[0]; p
            Point set defined by 2 point(s)
            sage: q = p.plot3d(size=22)

        .. PLOT::

            P = point([(0, 0), (1, 1)])
            p = P[0]
            sphinx_plot(p.plot3d(size=22))

        Multiple points with different heights::

            sage: P = point([(0, 0), (1, 1)])
            sage: p = P[0]
            sage: q = p.plot3d(z=[2,3])
            sage: q.all[0].loc[2]
            2.0
            sage: q.all[1].loc[2]
            3.0

        .. PLOT::

            P = point([(0, 0), (1, 1)])
            p = P[0]
            sphinx_plot(p.plot3d(z=[2,3]))

        Note that keywords passed must be valid point3d options::

            sage: A = point((1, 1), size=22)
            sage: a = A[0]; a
            Point set defined by 1 point(s)
            sage: b = a.plot3d()
            sage: b.size
            22
            sage: b = a.plot3d(pointsize=23)  # only 2D valid option
            sage: b.size
            22
            sage: b = a.plot3d(size=23) # correct keyword
            sage: b.size
            23

        TESTS:

        Heights passed as a list should have same length as
        number of points::

            sage: P = point([(0, 0), (1, 1), (2, 3)])
            sage: p = P[0]
            sage: q = p.plot3d(z=2)
            sage: q.all[1].loc[2]
            2.0
            sage: q = p.plot3d(z=[2,-2])
            Traceback (most recent call last):
            ...
            ValueError: incorrect number of heights given
        """
    def __getitem__(self, i):
        """
        Return tuple of coordinates of point.

        EXAMPLES::

            sage: P = point([(0, 0), (1, 1), (2, 3)])
            sage: p = P[0]; p
            Point set defined by 3 point(s)
            sage: p[1]
            (1.0, 1.0)
        """

def point(points, **kwds):
    """
    Return either a 2-dimensional or 3-dimensional point or sum of points.

    INPUT:

    - ``points`` -- either a single point (as a tuple), a list of
      points, a single complex number, or a list of complex numbers

    For information regarding additional arguments, see either point2d?
    or point3d?.

    .. SEEALSO::

        :func:`sage.plot.point.point2d`, :func:`sage.plot.plot3d.shapes2.point3d`

    EXAMPLES::

        sage: point((1, 2))
        Graphics object consisting of 1 graphics primitive

    .. PLOT::

        sphinx_plot(point((1, 2)))

    ::

        sage: point((1, 2, 3))
        Graphics3d Object

    .. PLOT::

        sphinx_plot(point((1, 2, 3)))

    ::

        sage: point([(0, 0), (1, 1)])
        Graphics object consisting of 1 graphics primitive

    .. PLOT::

        sphinx_plot(point([(0, 0), (1, 1)]))

    ::

        sage: point([(0, 0, 1), (1, 1, 1)])
        Graphics3d Object

    .. PLOT::

        sphinx_plot(point([(0, 0, 1), (1, 1, 1)]))

    Extra options will get passed on to show(), as long as they are valid::

        sage: point([(cos(theta), sin(theta))                                           # needs sage.symbolic
        ....:        for theta in srange(0, 2*pi, pi/8)], frame=True)
        Graphics object consisting of 1 graphics primitive
        sage: point([(cos(theta), sin(theta))               # These are equivalent      # needs sage.symbolic
        ....:        for theta in srange(0, 2*pi, pi/8)]).show(frame=True)

    TESTS:

    One can now use iterators (:issue:`13890`)::

        sage: point(iter([(1, 1, 1)]))
        Graphics3d Object
        sage: point(iter([(1, 2), (3, 5)]))
        Graphics object consisting of 1 graphics primitive
    """
def point2d(points, **options):
    """
    A point of size ``size`` defined by point = `(x, y)`.

    INPUT:

    - ``points`` -- either a single point (as a tuple), a list of
      points, a single complex number, or a list of complex numbers

    - ``alpha`` -- how transparent the point is

    - ``faceted`` -- if ``True``, color the edge of the point (only for 2D plots)

    - ``hue`` -- the color given as a hue

    - ``legend_color`` -- the color of the legend text

    - ``legend_label`` -- the label for this item in the legend

    - ``marker`` -- the marker symbol for 2D plots only (see documentation of
      :func:`plot` for details)

    - ``markeredgecolor`` -- the color of the marker edge (only for 2D plots)

    - ``rgbcolor`` -- the color as an RGB tuple

    - ``size`` -- how big the point is (i.e., area in points^2=(1/72 inch)^2)

    - ``zorder`` -- the layer level in which to draw

    EXAMPLES:

    A purple point from a single tuple of coordinates::

        sage: point((0.5, 0.5), rgbcolor=hue(0.75))
        Graphics object consisting of 1 graphics primitive

    .. PLOT::

        sphinx_plot(point((0.5, 0.5), rgbcolor=hue(0.75)))

    Points with customized markers and edge colors::

        sage: r = [(random(), random()) for _ in range(10)]
        sage: point(r, marker='d', markeredgecolor='red', size=20)
        Graphics object consisting of 1 graphics primitive

    .. PLOT::

        r = [(random(), random()) for _ in range(10)]
        sphinx_plot(point(r, marker='d', markeredgecolor='red', size=20))

    Passing an empty list returns an empty plot::

        sage: point([])
        Graphics object consisting of 0 graphics primitives
        sage: import numpy; point(numpy.array([]))
        Graphics object consisting of 0 graphics primitives

    If you need a 2D point to live in 3-space later, this is possible::

        sage: A = point((1, 1))
        sage: a = A[0]; a
        Point set defined by 1 point(s)
        sage: b = a.plot3d(z=3)

    .. PLOT::

        A = point((1, 1))
        a = A[0]
        b = a.plot3d(z=3)
        sphinx_plot(b)

    This is also true with multiple points::

        sage: P = point([(0, 0), (1, 1)])
        sage: p = P[0]
        sage: q = p.plot3d(z=[2,3])

    .. PLOT::

        P = point([(0, 0), (1, 1)])
        p = P[0]
        q = p.plot3d(z=[2,3])
        sphinx_plot(q)

    Here are some random larger red points, given as a list of tuples::

        sage: point(((0.5, 0.5), (1, 2), (0.5, 0.9), (-1, -1)), rgbcolor=hue(1), size=30)
        Graphics object consisting of 1 graphics primitive

    .. PLOT::

        sphinx_plot(point(((0.5, 0.5), (1, 2), (0.5, 0.9), (-1, -1)), rgbcolor=hue(1), size=30))

    And an example with a legend::

        sage: point((0, 0), rgbcolor='black', pointsize=40, legend_label='origin')
        Graphics object consisting of 1 graphics primitive

    .. PLOT::

        sphinx_plot(point((0, 0), rgbcolor='black', pointsize=40, legend_label='origin'))

    The legend can be colored::

        sage: P = points([(0, 0), (1, 0)], pointsize=40,
        ....:            legend_label='origin', legend_color='red')
        sage: P + plot(x^2, (x, 0, 1), legend_label='plot', legend_color='green')       # needs sage.symbolic
        Graphics object consisting of 2 graphics primitives

    .. PLOT::

        P = points([(0, 0), (1, 0)], pointsize=40, legend_label='origin', legend_color='red')
        Q = P + plot(x**2, (x, 0, 1), legend_label='plot', legend_color='green')
        sphinx_plot(Q)

    Extra options will get passed on to show(), as long as they are valid::

        sage: point([(cos(theta), sin(theta))                                           # needs sage.symbolic
        ....:        for theta in srange(0, 2*pi, pi/8)], frame=True)
        Graphics object consisting of 1 graphics primitive
        sage: point([(cos(theta), sin(theta))               # These are equivalent      # needs sage.symbolic
        ....:        for theta in srange(0, 2*pi, pi/8)]).show(frame=True)

    .. PLOT::

        sphinx_plot(point([(cos(theta), sin(theta)) for theta in srange(0, 2*pi, pi/8)], frame=True))

    For plotting data, we can use a logarithmic scale, as long as we are sure
    not to include any nonpositive points in the logarithmic direction::

        sage: point([(1, 2),(2, 4),(3, 4),(4, 8),(4.5, 32)], scale='semilogy', base=2)
        Graphics object consisting of 1 graphics primitive

    .. PLOT::

        sphinx_plot(point([(1, 2),(2, 4),(3, 4),(4, 8),(4.5, 32)], scale='semilogy', base=2))

    Since Sage Version 4.4 (:issue:`8599`), the size of a 2d point can be
    given by the argument ``size`` instead of ``pointsize``. The argument
    ``pointsize`` is still supported::

        sage: point((3, 4), size=100)
        Graphics object consisting of 1 graphics primitive

    ::

        sage: point((3, 4), pointsize=100)
        Graphics object consisting of 1 graphics primitive

    We can plot a single complex number::

        sage: point(1 + I, pointsize=100)                                               # needs sage.symbolic
        Graphics object consisting of 1 graphics primitive
        sage: point(sqrt(2) + I, pointsize=100)                                         # needs sage.symbolic
        Graphics object consisting of 1 graphics primitive

    .. PLOT::

        sphinx_plot(point(1 + I, pointsize=100))

    .. PLOT::

        sphinx_plot(point(sqrt(2) + I, pointsize=100))

    We can also plot a list of complex numbers::

        sage: point([I, 1 + I, 2 + 2*I], pointsize=100)                                 # needs sage.symbolic
        Graphics object consisting of 1 graphics primitive

    .. PLOT::

        sphinx_plot(point([I, 1 + I, 2 + 2*I], pointsize=100))

    TESTS::

       sage: point2d(iter([]))
       Graphics object consisting of 0 graphics primitives

    Verify that :issue:`36153` does not arise::

        sage: P = point((0.5, 0.5), legend_label='test')
    """
points = point
