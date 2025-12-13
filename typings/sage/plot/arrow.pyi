from _typeshed import Incomplete
from sage.misc.decorators import options as options, rename_keyword as rename_keyword
from sage.plot.colors import to_mpl_color as to_mpl_color
from sage.plot.primitive import GraphicPrimitive as GraphicPrimitive

class CurveArrow(GraphicPrimitive):
    path: Incomplete
    codes: Incomplete
    vertices: Incomplete
    def __init__(self, path, options) -> None:
        """
        Return an arrow graphics primitive along the provided path (bezier curve).

        EXAMPLES::

            sage: from sage.plot.arrow import CurveArrow
            sage: b = CurveArrow(path=[[(0,0),(.5,.5),(1,0)],[(.5,1),(0,0)]],
            ....:                options={})
            sage: b
            CurveArrow from (0, 0) to (0, 0)
        """
    def get_minmax_data(self):
        '''
        Return a dictionary with the bounding box data.

        EXAMPLES::

            sage: import numpy  # to ensure numpy 2.0 compatibility
            sage: if int(numpy.version.short_version[0]) > 1:
            ....:     _ = numpy.set_printoptions(legacy="1.25")
            sage: from sage.plot.arrow import CurveArrow
            sage: b = CurveArrow(path=[[(0,0),(.5,.5),(1,0)],[(.5,1),(0,0)]],
            ....:                options={})
            sage: d = b.get_minmax_data()
            sage: d[\'xmin\']
            0.0
            sage: d[\'xmax\']
            1.0
        '''

class Arrow(GraphicPrimitive):
    """
    Primitive class that initializes the (line) arrow graphics type.

    EXAMPLES:

    We create an arrow graphics object, then take the 0th entry
    in it to get the actual Arrow graphics primitive::

        sage: P = arrow((0,1), (2,3))[0]
        sage: type(P)
        <class 'sage.plot.arrow.Arrow'>
        sage: P
        Arrow from (0.0,1.0) to (2.0,3.0)
    """
    xtail: Incomplete
    xhead: Incomplete
    ytail: Incomplete
    yhead: Incomplete
    def __init__(self, xtail, ytail, xhead, yhead, options) -> None:
        """
        Create an arrow graphics primitive.

        EXAMPLES::

            sage: from sage.plot.arrow import Arrow
            sage: Arrow(0,0,2,3,{})
            Arrow from (0.0,0.0) to (2.0,3.0)
        """
    def get_minmax_data(self):
        """
        Return a bounding box for this arrow.

        EXAMPLES::

            sage: d = arrow((1,1), (5,5)).get_minmax_data()
            sage: d['xmin']
            1.0
            sage: d['xmax']
            5.0
        """
    def plot3d(self, ztail: int = 0, zhead: int = 0, **kwds):
        """
        Take 2D plot and places it in 3D.

        EXAMPLES::

            sage: A = arrow((0,0),(1,1))[0].plot3d()
            sage: A.jmol_repr(A.testing_render_params())[0]
            'draw line_1 diameter 2 arrow {0.0 0.0 0.0}  {1.0 1.0 0.0} '

        Note that we had to index the arrow to get the Arrow graphics
        primitive.  We can also change the height via the :meth:`Graphics.plot3d`
        method, but only as a whole::

            sage: A = arrow((0,0),(1,1)).plot3d(3)
            sage: A.jmol_repr(A.testing_render_params())[0][0]
            'draw line_1 diameter 2 arrow {0.0 0.0 3.0}  {1.0 1.0 3.0} '

        Optional arguments place both the head and tail outside the
        `xy`-plane, but at different heights.  This must be done on
        the graphics primitive obtained by indexing::

            sage: A=arrow((0,0),(1,1))[0].plot3d(3,4)
            sage: A.jmol_repr(A.testing_render_params())[0]
            'draw line_1 diameter 2 arrow {0.0 0.0 3.0}  {1.0 1.0 4.0} '
        """

def arrow(tailpoint=None, headpoint=None, **kwds):
    """
    Return either a 2-dimensional or 3-dimensional arrow depending
    on value of points.

    For information regarding additional arguments, see either arrow2d?
    or arrow3d?.

    EXAMPLES::

        sage: arrow((0,0), (1,1))
        Graphics object consisting of 1 graphics primitive

    .. PLOT::

        sphinx_plot(arrow((0,0), (1,1)))

    ::

        sage: arrow((0,0,1), (1,1,1))
        Graphics3d Object

    .. PLOT::

        sphinx_plot(arrow((0,0,1), (1,1,1)))

    TESTS:

    Check that :issue:`35031` is fixed::

        sage: arrow((0,0), (0,0), linestyle='dashed')
        Graphics object consisting of 1 graphics primitive
    """
def arrow2d(tailpoint=None, headpoint=None, path=None, **options):
    """
    If ``tailpoint`` and ``headpoint`` are provided, returns an arrow from
    (xtail, ytail) to (xhead, yhead).  If ``tailpoint`` or ``headpoint`` is None and
    ``path`` is not None, returns an arrow along the path.  (See further info on
    paths in :class:`bezier_path`).

    INPUT:

    - ``tailpoint`` -- the starting point of the arrow

    - ``headpoint`` -- where the arrow is pointing to

    - ``path`` -- the list of points and control points (see bezier_path for
      detail) that the arrow will follow from source to destination

    - ``head`` -- 0, 1 or 2, whether to draw the head at the start (0), end (1)
      or both (2) of the path (using 0 will swap headpoint and tailpoint).
      This is ignored in 3D plotting.

    - ``linestyle`` -- (default: ``'solid'``) the style of the line, which is
      one of ``'dashed'``, ``'dotted'``, ``'solid'``, ``'dashdot'``,
      or ``'--'``, ``':'``, ``'-'``, ``'-.'``, respectively

    - ``width`` -- (default: 2) the width of the arrow shaft, in points

    - ``color`` -- (default: (0,0,1)) the color of the arrow (as an RGB tuple or
      a string)

    - ``hue`` -- the color of the arrow (as a number)

    - ``arrowsize`` -- the size of the arrowhead

    - ``arrowshorten`` -- the length in points to shorten the arrow (ignored if
      using path parameter)

    - ``legend_label`` -- the label for this item in the legend

    - ``legend_color`` -- the color for the legend label

    - ``zorder`` -- the layer level to draw the arrow-- note that this is
      ignored in 3D plotting

    EXAMPLES:

    A straight, blue arrow::

       sage: arrow2d((1,1), (3,3))
       Graphics object consisting of 1 graphics primitive

    .. PLOT::

        sphinx_plot(arrow2d((1,1), (3,3)))

    Make a red arrow::

       sage: arrow2d((-1,-1), (2,3), color=(1,0,0))
       Graphics object consisting of 1 graphics primitive

    .. PLOT::

        sphinx_plot(arrow2d((-1,-1), (2,3), color=(1,0,0)))

    ::

       sage: arrow2d((-1,-1), (2,3), color='red')
       Graphics object consisting of 1 graphics primitive

    .. PLOT::

        sphinx_plot(arrow2d((-1,-1), (2,3), color='red'))

    You can change the width of an arrow::

        sage: arrow2d((1,1), (3,3), width=5, arrowsize=15)
        Graphics object consisting of 1 graphics primitive

    .. PLOT::

        P = arrow2d((1,1), (3,3), width=5, arrowsize=15)
        sphinx_plot(P)

    Use a dashed line instead of a solid one for the arrow::

        sage: arrow2d((1,1), (3,3), linestyle='dashed')
        Graphics object consisting of 1 graphics primitive
        sage: arrow2d((1,1), (3,3), linestyle='--')
        Graphics object consisting of 1 graphics primitive

    .. PLOT::

        P = arrow2d((1,1), (3,3), linestyle='--')
        sphinx_plot(P)

    A pretty circle of arrows::

        sage: sum(arrow2d((0,0), (cos(x),sin(x)), hue=x/(2*pi))                         # needs sage.symbolic
        ....:     for x in [0..2*pi, step=0.1])
        Graphics object consisting of 63 graphics primitives

    .. PLOT::

        P = sum([arrow2d((0,0), (cos(x*0.1),sin(x*0.1)), hue=x/(20*pi)) for x in range(floor(20*pi)+1)])
        sphinx_plot(P)

    If we want to draw the arrow between objects, for example, the
    boundaries of two lines, we can use the ``arrowshorten`` option
    to make the arrow shorter by a certain number of points::

        sage: L1 = line([(0,0), (1,0)], thickness=10)
        sage: L2 = line([(0,1), (1,1)], thickness=10)
        sage: A = arrow2d((0.5,0), (0.5,1), arrowshorten=10, rgbcolor=(1,0,0))
        sage: L1 + L2 + A
        Graphics object consisting of 3 graphics primitives

    .. PLOT::

        L1 = line([(0,0), (1,0)],thickness=10)
        L2 = line([(0,1), (1,1)], thickness=10)
        A = arrow2d((0.5,0), (0.5,1), arrowshorten=10, rgbcolor=(1,0,0))
        sphinx_plot(L1 + L2 + A)

    If BOTH ``headpoint`` and ``tailpoint`` are None, then an empty plot is
    returned::

        sage: arrow2d(headpoint=None, tailpoint=None)
        Graphics object consisting of 0 graphics primitives

    We can also draw an arrow with a legend::

        sage: arrow((0,0), (0,2), legend_label='up', legend_color='purple')
        Graphics object consisting of 1 graphics primitive

    .. PLOT::

        P = arrow((0,0), (0,2), legend_label='up', legend_color='purple')
        sphinx_plot(P)

    Extra options will get passed on to :meth:`Graphics.show()`, as long as they are valid::

        sage: arrow2d((-2,2), (7,1), frame=True)
        Graphics object consisting of 1 graphics primitive

    .. PLOT::

        sphinx_plot(arrow2d((-2,2), (7,1), frame=True))

    ::

        sage: arrow2d((-2,2), (7,1)).show(frame=True)

    TESTS:

    Verify that :issue:`36153` is fixed::

        sage: A = arrow2d((-1,-1), (2,3), legend_label='test')
    """
