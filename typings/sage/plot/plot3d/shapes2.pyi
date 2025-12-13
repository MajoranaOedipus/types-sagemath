from . import shapes as shapes
from .base import PrimitiveObject as PrimitiveObject, point_list_bounding_box as point_list_bounding_box
from .shapes import Sphere as Sphere, Text as Text
from .texture import Texture as Texture
from _typeshed import Incomplete
from sage.arith.srange import srange as srange
from sage.misc.decorators import options as options, rename_keyword as rename_keyword
from sage.modules.free_module_element import vector as vector
from sage.rings.real_double import RDF as RDF

TACHYON_PIXEL: Incomplete

def line3d(points, thickness: int = 1, radius=None, arrow_head: bool = False, **kwds):
    """
    Draw a 3d line joining a sequence of points.

    One may specify either a thickness or radius. If a thickness is
    specified, this line will have a constant diameter regardless of
    scaling and zooming. If a radius is specified, it will behave as a
    series of cylinders.

    INPUT:

    - ``points`` -- list of at least 2 points

    - ``thickness`` -- (default: 1)

    - ``radius`` -- (default: ``None``)

    - ``arrow_head`` -- (default: ``False``)

    - ``color`` -- string (``'red'``, ``'green'`` etc)
      or a tuple (r, g, b) with r, g, b numbers between 0 and 1

    - ``opacity`` -- (default: 1) if less than 1 then is
      transparent

    EXAMPLES:

    A line in 3-space::

        sage: line3d([(1,2,3), (1,0,-2), (3,1,4), (2,1,-2)])
        Graphics3d Object

    .. PLOT::

        sphinx_plot(line3d([(1,2,3), (1,0,-2), (3,1,4), (2,1,-2)]))

    The same line but red::

        sage: line3d([(1,2,3), (1,0,-2), (3,1,4), (2,1,-2)], color='red')
        Graphics3d Object

    .. PLOT::

        sphinx_plot(line3d([(1,2,3), (1,0,-2), (3,1,4), (2,1,-2)], color='red'))

    The points of the line provided as a numpy array::

        sage: import numpy
        sage: line3d(numpy.array([(1,2,3), (1,0,-2), (3,1,4), (2,1,-2)]))
        Graphics3d Object

    .. PLOT::

        import numpy
        sphinx_plot(line3d(numpy.array([(1,2,3), (1,0,-2), (3,1,4), (2,1,-2)])))

    A transparent thick green line and a little blue line::

        sage: line3d([(0,0,0), (1,1,1), (1,0,2)], opacity=0.5, radius=0.1,
        ....:        color='green') + line3d([(0,1,0), (1,0,2)])
        Graphics3d Object

    .. PLOT::

        sphinx_plot(line3d([(0,0,0), (1,1,1), (1,0,2)], opacity=0.5, radius=0.1, color='green') + line3d([(0,1,0), (1,0,2)]))

    A Dodecahedral complex of 5 tetrahedra (a more elaborate example
    from Peter Jipsen)::

        sage: def tetra(col):
        ....:     return line3d([(0,0,1), (2*sqrt(2.)/3,0,-1./3), (-sqrt(2.)/3, sqrt(6.)/3,-1./3),\\\n        ....:            (-sqrt(2.)/3,-sqrt(6.)/3,-1./3), (0,0,1), (-sqrt(2.)/3, sqrt(6.)/3,-1./3),\\\n        ....:            (-sqrt(2.)/3,-sqrt(6.)/3,-1./3), (2*sqrt(2.)/3,0,-1./3)],\\\n        ....:            color=col, thickness=10, aspect_ratio=[1,1,1])

        sage: from math import pi
        sage: v  = (sqrt(5.)/2-5/6, 5/6*sqrt(3.)-sqrt(15.)/2, sqrt(5.)/3)
        sage: t  = acos(sqrt(5.)/3)/2
        sage: t1 = tetra('blue').rotateZ(t)
        sage: t2 = tetra('red').rotateZ(t).rotate(v,2*pi/5)
        sage: t3 = tetra('green').rotateZ(t).rotate(v,4*pi/5)
        sage: t4 = tetra('yellow').rotateZ(t).rotate(v,6*pi/5)
        sage: t5 = tetra('orange').rotateZ(t).rotate(v,8*pi/5)
        sage: show(t1+t2+t3+t4+t5, frame=False)

    .. PLOT::

        def tetra(col):
            return line3d([(0,0,1), (2*sqrt(2.)/3,0,-1./3), (-sqrt(2.)/3, sqrt(6.)/3,-1./3),\\\n                    (-sqrt(2.)/3,-sqrt(6.)/3,-1./3), (0,0,1), (-sqrt(2.)/3, sqrt(6.)/3,-1./3),\\\n                    (-sqrt(2.)/3,-sqrt(6.)/3,-1./3), (2*sqrt(2.)/3,0,-1./3)],\\\n                    color=col, thickness=10, aspect_ratio=[1,1,1])
        v  = (sqrt(5.)/2-5/6, 5/6*sqrt(3.)-sqrt(15.)/2, sqrt(5.)/3)
        t  = acos(sqrt(5.)/3)/2
        t1 = tetra('blue').rotateZ(t)
        t2 = tetra('red').rotateZ(t).rotate(v,2*pi/5)
        t3 = tetra('green').rotateZ(t).rotate(v,4*pi/5)
        t4 = tetra('yellow').rotateZ(t).rotate(v,6*pi/5)
        t5 = tetra('orange').rotateZ(t).rotate(v,8*pi/5)
        sphinx_plot(t1+t2+t3+t4+t5)

    TESTS:

    Copies are made of the input list, so the input list does not change::

        sage: mypoints = [vector([1,2,3]), vector([4,5,6])]
        sage: type(mypoints[0])
        <... 'sage.modules.vector_integer_dense.Vector_integer_dense'>
        sage: L = line3d(mypoints)
        sage: type(mypoints[0])
        <... 'sage.modules.vector_integer_dense.Vector_integer_dense'>

    The copies are converted to a list, so we can pass in immutable objects too::

        sage: L = line3d(((0,0,0),(1,2,3)))

    This function should work for anything than can be turned into a
    list, such as iterators and such (see :issue:`10478`)::

        sage: line3d(iter([(0,0,0), (sqrt(3), 2, 4)]))                                  # needs sage.symbolic
        Graphics3d Object
        sage: line3d((x, x^2, x^3) for x in range(5))
        Graphics3d Object
        sage: from builtins import zip
        sage: line3d(zip([2,3,5,7], [11, 13, 17, 19], [-1, -2, -3, -4]))
        Graphics3d Object
    """
def bezier3d(path, **options):
    """
    Draw a 3-dimensional bezier path.

    Input is similar to bezier_path, but each point in the path and
    each control point is required to have 3 coordinates.

    INPUT:

    - ``path`` -- list of curves, which each is a list of points. See further
        detail below

    - ``thickness`` -- (default: 2)

    - ``color`` -- string (``'red'``, ``'green'`` etc)
      or a tuple (r, g, b) with r, g, b numbers between 0 and 1

    - ``opacity`` -- (default: 1) if less than 1 then is
      transparent

    - ``aspect_ratio`` -- (default: [1,1,1])

    The path is a list of curves, and each curve is a list of points.
    Each point is a tuple (x,y,z).

    The first curve contains the endpoints as the first and last point
    in the list.  All other curves assume a starting point given by the
    last entry in the preceding list, and take the last point in the list
    as their opposite endpoint.  A curve can have 0, 1 or 2 control points
    listed between the endpoints.  In the input example for path below,
    the first and second curves have 2 control points, the third has one,
    and the fourth has no control points::

        path = [[p1, c1, c2, p2], [c3, c4, p3], [c5, p4], [p5], ...]

    In the case of no control points, a straight line will be drawn
    between the two endpoints.  If one control point is supplied, then
    the curve at each of the endpoints will be tangent to the line from
    that endpoint to the control point.  Similarly, in the case of two
    control points, at each endpoint the curve will be tangent to the line
    connecting that endpoint with the control point immediately after or
    immediately preceding it in the list.

    So in our example above, the curve between p1 and p2 is tangent to the
    line through p1 and c1 at p1, and tangent to the line through p2 and c2
    at p2.  Similarly, the curve between p2 and p3 is tangent to line(p2,c3)
    at p2 and tangent to line(p3,c4) at p3.  Curve(p3,p4) is tangent to
    line(p3,c5) at p3 and tangent to line(p4,c5) at p4.  Curve(p4,p5) is a
    straight line.

    EXAMPLES::

        sage: path = [[(0,0,0),(.5,.1,.2),(.75,3,-1),(1,1,0)],
        ....:         [(.5,1,.2),(1,.5,0)], [(.7,.2,.5)]]
        sage: b = bezier3d(path, color='green'); b                                      # needs sage.symbolic
        Graphics3d Object

    .. PLOT::

        path = [[(0,0,0),(.5,.1,.2),(.75,3,-1),(1,1,0)],[(.5,1,.2),(1,.5,0)],[(.7,.2,.5)]]
        sphinx_plot(bezier3d(path, color='green'))

    To construct a simple curve, create a list containing a single list::

        sage: path = [[(0,0,0),(1,0,0),(0,1,0),(0,1,1)]]
        sage: curve = bezier3d(path, thickness=5, color='blue'); curve                  # needs sage.symbolic
        Graphics3d Object

    .. PLOT::

        path = [[(0,0,0),(1,0,0),(0,1,0),(0,1,1)]]
        sphinx_plot(bezier3d(path, thickness=5, color='blue'))

    TESTS:

    Check for :issue:`31640`::

        sage: p2d = [[(3,0.0),(3,0.13),(2,0.2),(2,0.3)],
        ....:        [(2.7,0.4),(2.6,0.5),(2.5,0.5)], [(2.3,0.5),(2.2,0.4),(2.1,0.3)]]
        sage: bp = bezier_path(p2d)                                                     # needs sage.symbolic
        sage: bp.plot3d()                                                               # needs sage.symbolic
        Graphics3d Object

        sage: p3d = [[(3,0,0),(3,0.1,0),(2.9,0.2,0),(2.8,0.3,0)],
        ....:        [(2.7,0.4,0),(2,0.5,0),(2.5,0.5,0)],
        ....:        [(2.3,0.5,0),(2.2,0.4,0),(2.1,0.3,0)]]
        sage: bezier3d(p3d)                                                             # needs sage.symbolic
        Graphics3d Object
    """
def polygon3d(points, **options):
    """
    Draw a polygon in 3d.

    INPUT:

    - ``points`` -- the vertices of the polygon

    Type ``polygon3d.options`` for a dictionary of the default
    options for polygons.  You can change this to change
    the defaults for all future polygons.  Use ``polygon3d.reset()``
    to reset to the default options.

    EXAMPLES:

    A simple triangle::

        sage: polygon3d([[0,2,0], [1.5,1,3], [3,0,0]])
        Graphics3d Object

    .. PLOT::

        sphinx_plot(polygon3d([[0,2,0], [1.5,1,3], [3,0,0]]))

    Some modern art -- a random polygon::

        sage: v = [(randrange(-5,5), randrange(-5,5), randrange(-5, 5))
        ....:      for _ in range(10)]
        sage: polygon3d(v)
        Graphics3d Object

    .. PLOT::

        v = [(randrange(-5,5), randrange(-5,5), randrange(-5, 5)) for _ in range(10)]
        sphinx_plot(polygon3d(v))

    A bent transparent green triangle::

        sage: polygon3d([[1, 2, 3], [0,1,0], [1,0,1], [3,0,0]],
        ....:           color=(0,1,0), opacity=0.7)
        Graphics3d Object

    .. PLOT::

        sphinx_plot(polygon3d([[1, 2, 3], [0,1,0], [1,0,1], [3,0,0]], color=(0,1,0), opacity=0.7))

    This is the same as using ``alpha=0.7``::

        sage: polygon3d([[1, 2, 3], [0,1,0], [1,0,1], [3,0,0]],
        ....:           color=(0,1,0), alpha=0.7)
        Graphics3d Object

    .. PLOT::

        sphinx_plot(polygon3d([[1, 2, 3], [0,1,0], [1,0,1], [3,0,0]], color=(0,1,0), alpha=0.7))
    """
def polygons3d(faces, points, **options):
    """
    Draw the union of several polygons in 3d.

    Useful to plot a polyhedron as just one :class:`IndexFaceSet`.

    INPUT:

    - ``faces`` -- list of faces, every face given by the list
      of indices of its vertices

    - ``points`` -- coordinates of the vertices in the union

    EXAMPLES:

    Two adjacent triangles::

        sage: f = [[0,1,2],[1,2,3]]
        sage: v = [(-1,0,0),(0,1,1),(0,-1,1),(1,0,0)]
        sage: polygons3d(f, v, color='red')
        Graphics3d Object

    .. PLOT::

        f = [[0,1,2],[1,2,3]]
        v = [(-1,0,0),(0,1,1),(0,-1,1),(1,0,0)]
        sphinx_plot(polygons3d(f, v, color='red'))
    """
def frame3d(lower_left, upper_right, **kwds):
    """
    Draw a frame in 3-D.

    Primarily used as a helper function for creating frames for 3-D
    graphics viewing.

    INPUT:

    - ``lower_left`` -- the lower left corner of the frame, as a
      list, tuple, or vector

    - ``upper_right`` -- the upper right corner of the frame, as a
      list, tuple, or vector

    EXAMPLES:

    A frame::

        sage: from sage.plot.plot3d.shapes2 import frame3d
        sage: frame3d([1,3,2],vector([2,5,4]),color='red')
        Graphics3d Object

    This is usually used for making an actual plot::

        sage: y = var('y')                                                              # needs sage.symbolic
        sage: plot3d(sin(x^2+y^2), (x,0,pi), (y,0,pi))                                  # needs sage.symbolic
        Graphics3d Object
    """
def frame_labels(lower_left, upper_right, label_lower_left, label_upper_right, eps: int = 1, **kwds):
    '''
    Draw correct labels for a given frame in 3-D.

    Primarily used as a helper function for creating frames for 3-D
    graphics viewing - do not use directly unless you know what you
    are doing!

    INPUT:

    - ``lower_left`` -- the lower left corner of the frame, as a
      list, tuple, or vector

    - ``upper_right`` -- the upper right corner of the frame, as a
      list, tuple, or vector

    - ``label_lower_left`` -- the label for the lower left corner
      of the frame, as a list, tuple, or vector.  This label must actually
      have all coordinates less than the coordinates of the other label.

    - ``label_upper_right`` -- the label for the upper right corner
      of the frame, as a list, tuple, or vector.  This label must actually
      have all coordinates greater than the coordinates of the other label.

    - ``eps`` -- (default: 1) a parameter for how far away from the frame
      to put the labels

    EXAMPLES:

    We can use it directly::

        sage: from sage.plot.plot3d.shapes2 import frame_labels
        sage: frame_labels([1,2,3],[4,5,6],[1,2,3],[4,5,6])
        Graphics3d Object

    This is usually used for making an actual plot::

        sage: # needs sage.symbolic
        sage: y = var(\'y\')
        sage: P = plot3d(sin(x^2+y^2), (x,0,pi), (y,0,pi))
        sage: a,b = P._rescale_for_frame_aspect_ratio_and_zoom(1.0,[1,1,1],1)
        sage: F = frame_labels(a, b, *P._box_for_aspect_ratio("automatic",a,b))
        sage: F.jmol_repr(F.default_render_params())[0]
        [[\'select atomno = 1\', \'color atom  [76,76,76]\', \'label "0.0"\']]

    TESTS::

        sage: frame_labels([1,2,3],[4,5,6],[1,2,3],[1,3,4])
        Traceback (most recent call last):
        ...
        ValueError: ensure the upper right labels are above and to the right of the lower left labels
    '''
def ruler(start, end, ticks: int = 4, sub_ticks: int = 4, absolute: bool = False, snap: bool = False, **kwds):
    """
    Draw a ruler in 3-D, with major and minor ticks.

    INPUT:

    - ``start`` -- the beginning of the ruler, as a list,
      tuple, or vector

    - ``end`` -- the end of the ruler, as a list, tuple,
      or vector

    - ``ticks`` -- (default: 4) the number of major ticks
      shown on the ruler

    - ``sub_ticks`` -- (default: 4) the number of shown
      subdivisions between each major tick

    - ``absolute`` -- boolean (default: ``False``); if ``True``, makes a huge ruler
      in the direction of an axis

    - ``snap`` -- boolean (default: ``False``); if ``True``, snaps to an implied
      grid

    EXAMPLES:

    A ruler::

        sage: from sage.plot.plot3d.shapes2 import ruler
        sage: R = ruler([4, 2, 1],vector([3, 3, 2])); R
        Graphics3d Object

    .. PLOT::

        from sage.plot.plot3d.shapes2 import ruler
        sphinx_plot(ruler([4, 2, 1],vector([3, 3, 2])))

    A ruler with some options::

        sage: R = ruler([4, 2, 1],vector([3, 3, 2]),ticks=6, sub_ticks=2, color='red'); R
        Graphics3d Object

    .. PLOT::

        from sage.plot.plot3d.shapes2 import ruler
        sphinx_plot(ruler([4, 2, 1],vector([3, 3, 2]),ticks=6, sub_ticks=2, color='red'))

    The keyword ``snap`` makes the ticks not necessarily coincide
    with the ruler::

        sage: ruler([4, 2, 1],vector([3, 3, 2]),snap=True)
        Graphics3d Object

    .. PLOT::

        from sage.plot.plot3d.shapes2 import ruler
        sphinx_plot(ruler([4, 2, 1],vector([3, 3, 2]), snap=True))

    The keyword ``absolute`` makes a huge ruler in one of the axis
    directions::

        sage: ruler([1,2,3],vector([1,2,4]),absolute=True)
        Graphics3d Object

    .. PLOT::

        from sage.plot.plot3d.shapes2 import ruler
        sphinx_plot(ruler([1,2,3],vector([1,2,4]), absolute=True))

    TESTS::

        sage: ruler([1,2,3],vector([1,3,4]),absolute=True)
        Traceback (most recent call last):
        ...
        ValueError: absolute rulers only valid for axis-aligned paths
    """
def ruler_frame(lower_left, upper_right, ticks: int = 4, sub_ticks: int = 4, **kwds):
    """
    Draw a frame made of 3-D rulers, with major and minor ticks.

    INPUT:

    - ``lower_left`` -- the lower left corner of the frame, as a
      list, tuple, or vector

    - ``upper_right`` -- the upper right corner of the frame, as a
      list, tuple, or vector

    - ``ticks`` -- (default: 4) the number of major ticks
      shown on each ruler

    - ``sub_ticks`` -- (default: 4) the number of shown
      subdivisions between each major tick

    EXAMPLES:

    A ruler frame::

        sage: from sage.plot.plot3d.shapes2 import ruler_frame
        sage: F = ruler_frame([1,2,3],vector([2,3,4])); F
        Graphics3d Object

    .. PLOT::

        from sage.plot.plot3d.shapes2 import ruler_frame
        sphinx_plot(ruler_frame([1,2,3],vector([2,3,4])))

    A ruler frame with some options::

        sage: F = ruler_frame([1,2,3],vector([2,3,4]),ticks=6, sub_ticks=2, color='red'); F
        Graphics3d Object

    .. PLOT::

        from sage.plot.plot3d.shapes2 import ruler_frame
        sphinx_plot(ruler_frame([1,2,3],vector([2,3,4]),ticks=6, sub_ticks=2, color='red'))
    """
def sphere(center=(0, 0, 0), size: int = 1, **kwds):
    """
    Return a plot of a sphere of radius ``size`` centered at
    `(x,y,z)`.

    INPUT:

    -  `(x,y,z)` -- center (default: (0,0,0))

    - ``size`` -- the radius (default: 1)

    EXAMPLES: A simple sphere::

        sage: sphere()
        Graphics3d Object

    Two spheres touching::

        sage: sphere(center=(-1,0,0)) + sphere(center=(1,0,0), aspect_ratio=[1,1,1])
        Graphics3d Object

    .. PLOT::

        sphinx_plot(sphere(center=(-1,0,0)) + sphere(center=(1,0,0), aspect_ratio=[1,1,1]))

    Spheres of radii 1 and 2 one stuck into the other::

        sage: sphere(color='orange') + sphere(color=(0,0,0.3),
        ....:                                 center=(0,0,-2), size=2, opacity=0.9)
        Graphics3d Object

    .. PLOT::

        sphinx_plot(sphere(color='orange') + sphere(color=(0,0,0.3), center=(0,0,-2),size=2,opacity=0.9))

    We draw a transparent sphere on a saddle. ::

        sage: u,v = var('u v')                                                          # needs sage.symbolic
        sage: saddle = plot3d(u^2 - v^2, (u,-2,2), (v,-2,2))                            # needs sage.symbolic
        sage: sphere((0,0,1), color='red', opacity=0.5, aspect_ratio=[1,1,1]) + saddle  # needs sage.symbolic
        Graphics3d Object

    .. PLOT::

        u,v = var('u v')
        saddle = plot3d(u**2 - v**2, (u,-2,2), (v,-2,2))
        sphinx_plot(sphere((0,0,1), color='red', opacity=0.5, aspect_ratio=[1,1,1]) + saddle)

    TESTS::

        sage: T = sage.plot.plot3d.texture.Texture('red')
        sage: S = sphere(texture=T)
        sage: T in S.texture_set()
        True
    """
def text3d(txt, x_y_z, **kwds):
    '''
    Display 3d text.

    INPUT:

    - ``txt`` -- some text

    - ``x_y_z`` -- position tuple `(x,y,z)`

    - ``**kwds`` -- standard 3d graphics options

    EXAMPLES:

    We write the word Sage in red at position (1,2,3)::

        sage: text3d("Sage", (1,2,3), color=(0.5,0,0))
        Graphics3d Object

    .. PLOT::

        sphinx_plot(text3d("Sage", (1,2,3), color=(0.5,0,0)))

    We draw a multicolor spiral of numbers::

        sage: sum([text3d(\'%.1f\'%n, (cos(n),sin(n),n), color=(n/2,1-n/2,0))
        ....:     for n in [0,0.2,..,8]])
        Graphics3d Object

    .. PLOT::

        import numpy
        sphinx_plot(sum([text3d(\'%.1f\'%n, (cos(n),sin(n),n), color=(n/2,1-n/2,0))  for n in numpy.linspace(0,8,40)]))

    Another example::

        sage: text3d("Sage is really neat!!",(2,12,1))
        Graphics3d Object

    .. PLOT::

        sphinx_plot(text3d("Sage is really neat!!",(2,12,1)))

    And in 3d in two places::

        sage: text3d("Sage is...",(2,12,1), color=(1,0,0)) + text3d("quite powerful!!",(4,10,0), color=(0,0,1))
        Graphics3d Object

    .. PLOT::

        sphinx_plot(text3d("Sage is...",(2,12,1), color=(1,0,0)) + text3d("quite powerful!!",(4,10,0), color=(0,0,1)))

    Adjust the font size, family, style, and weight (Three.js viewer only)::

        sage: t0 = text3d("Pixel size", (0, 0, 0), fontsize=20)
        sage: t1 = text3d("Percentage size", (0, 0, 1), fontsize=\'300%\')
        sage: t2 = text3d("Keyword size", (0, 0, 2), fontsize=\'x-small\')
        sage: t3 = text3d("Single family", (0, 0, 3), fontfamily=\'serif\')
        sage: t4 = text3d("Family fallback", (0, 0, 4), fontfamily=[\'Consolas\', \'Lucida Console\', \'monospace\'])
        sage: t5 = text3d("Another way", (0, 0, 5), fontfamily=\'Consolas, Lucida Console, monospace\')
        sage: t6 = text3d("Style", (0, 0, 6), fontstyle=\'italic\')
        sage: t7 = text3d("Keyword weight", (0, 0, 7), fontweight=\'bold\')
        sage: t8 = text3d("Integer weight (1-1000)", (0, 0, 8), fontweight=800) # \'extra bold\'
        sage: sum([t0, t1, t2, t3, t4, t5, t6, t7, t8]).show(viewer=\'threejs\', frame=False)

    Adjust the text\'s opacity (Three.js viewer only)::

        sage: def echo(o):
        ....:     return text3d("Echo!", (0, 0, o), opacity=o)
        sage: show(sum([echo(o) for o in (0.1, 0.2, .., 1)]), viewer=\'threejs\')
    '''

class Point(PrimitiveObject):
    """
    Create a position in 3-space, represented by a sphere of fixed
    size.

    INPUT:

    - ``center`` -- point (3-tuple)

    - ``size`` -- (default: 1)

    EXAMPLES:

    We normally access this via the ``point3d`` function.  Note that extra
    keywords are correctly used::

        sage: point3d((4,3,2),size=2,color='red',opacity=.5)
        Graphics3d Object
    """
    loc: Incomplete
    size: Incomplete
    def __init__(self, center, size: int = 1, **kwds) -> None:
        """
        Create the graphics primitive :class:`Point` in 3-D.

        See the docstring of this class for full documentation.

        EXAMPLES::

            sage: from sage.plot.plot3d.shapes2 import Point
            sage: P = Point((1,2,3),2)
            sage: P.loc
            (1.0, 2.0, 3.0)
        """
    def bounding_box(self):
        """
        Return the lower and upper corners of a 3-D bounding box for ``self``.

        This is used for rendering and ``self`` should fit entirely within this
        box.  In this case, we simply return the center of the point.

        TESTS::

            sage: P = point3d((-3,2,10),size=7)
            sage: P.bounding_box()
            ((-3.0, 2.0, 10.0), (-3.0, 2.0, 10.0))
        """
    def tachyon_repr(self, render_params):
        """
        Return representation of the point suitable for plotting
        using the Tachyon ray tracer.

        TESTS::

            sage: P = point3d((1,2,3),size=3,color='purple')
            sage: P.tachyon_repr(P.default_render_params())
            'Sphere center 1.0 2.0 3.0 Rad 0.015 texture...'
        """
    def obj_repr(self, render_params):
        """
        Return complete representation of the point as a sphere.

        TESTS::

            sage: P = point3d((1,2,3),size=3,color='purple')
            sage: P.obj_repr(P.default_render_params())[0][0:2]
            ['g obj_1', 'usemtl texture...']
        """
    def jmol_repr(self, render_params):
        """
        Return representation of the object suitable for plotting
        using Jmol.

        TESTS::

            sage: P = point3d((1,2,3),size=3,color='purple')
            sage: P.jmol_repr(P.default_render_params())
            ['draw point_1 DIAMETER 3 {1.0 2.0 3.0}\\ncolor $point_1  [128,0,128]']
        """
    def threejs_repr(self, render_params):
        """
        Return representation of the point suitable for plotting with three.js.

        EXAMPLES::

            sage: P = point3d((1,2,3), color=(0,1,0), opacity=0.5, size=10)
            sage: P.threejs_repr(P.default_render_params())
            [('point',
              {'color': '#00ff00', 'opacity': 0.5, 'point': (1.0, 2.0, 3.0), 'size': 10.0})]

        TESTS:

        Transformations apply to the point's location::

            sage: P = point3d((1,2,3)).translate(-1, -2, -3)
            sage: P.threejs_repr(P.default_render_params())
            [('point',
              {'color': '#6666ff', 'opacity': 1.0, 'point': (0.0, 0.0, 0.0), 'size': 5.0})]
        """
    def stl_binary_repr(self, render_params):
        """
        Return an empty list, as this is not useful for STL export.

        EXAMPLES::

            sage: P = point3d((1,2,3)).translate(-1, -2, -3)
            sage: P.stl_binary_repr(P.default_render_params())
            []
        """

class Line(PrimitiveObject):
    """
    Draw a 3d line joining a sequence of points.

    This line has a fixed diameter unaffected by transformations and
    zooming. It may be smoothed if ``corner_cutoff < 1``.

    INPUT:

    - ``points`` -- list of points to pass through

    - ``thickness`` -- (default: 5) diameter of the line

    - ``corner_cutoff`` -- (default: 0.5) threshold for
      smoothing (see :meth:`corners`)

    - ``arrow_head`` -- boolean (default: ``False``); if ``True`` make
      this curve into an arrow

    The parameter ``corner_cutoff`` is a bound for the cosine of the
    angle made by two successive segments. This angle is close to `0`
    (and the cosine close to 1) if the two successive segments are
    almost aligned and close to `\\pi` (and the cosine close to -1) if
    the path has a strong peak. If the cosine is smaller than the
    bound (which means a sharper peak) then no smoothing is done.

    EXAMPLES::

        sage: from sage.plot.plot3d.shapes2 import Line
        sage: Line([(i*math.sin(i), i*math.cos(i), i/3) for i in range(30)],
        ....:      arrow_head=True)
        Graphics3d Object

    Smooth angles less than 90 degrees::

        sage: Line([(0,0,0),(1,0,0),(2,1,0),(0,1,0)], corner_cutoff=0)
        Graphics3d Object

    Make sure that the ``corner_cutoff`` keyword works (:issue:`3859`)::

        sage: N = 11
        sage: c = 0.4
        sage: sum(Line([(i,1,0), (i,0,0), (i,cos(2*pi*i/N), sin(2*pi*i/N))],            # needs sage.symbolic
        ....:          corner_cutoff=c,
        ....:          color='red' if -cos(2*pi*i/N)<=c else 'blue')
        ....:     for i in range(N+1))
        Graphics3d Object
    """
    points: Incomplete
    thickness: Incomplete
    corner_cutoff: Incomplete
    arrow_head: Incomplete
    def __init__(self, points, thickness: int = 5, corner_cutoff: float = 0.5, arrow_head: bool = False, **kwds) -> None:
        """
        Create the graphics primitive :class:`Line` in 3-D.

        See the docstring of this class for full documentation.

        EXAMPLES::

            sage: from sage.plot.plot3d.shapes2 import Line
            sage: P = Line([(1,2,3),(1,2,2),(-1,2,2),(-1,3,2)],thickness=6,corner_cutoff=.2)
            sage: P.points, P.arrow_head
            ([(1, 2, 3), (1, 2, 2), (-1, 2, 2), (-1, 3, 2)], False)
        """
    def bounding_box(self):
        """
        Return the lower and upper corners of a 3-D bounding box for ``self``.

        This is used for rendering and ``self`` should fit entirely within this
        box. In this case, we return the highest and lowest values of each
        coordinate among all points.

        TESTS::

            sage: from sage.plot.plot3d.shapes2 import Line
            sage: L = Line([(i, i^2 - 1, -2*ln(i)) for i in [10,20,30]])                # needs sage.symbolic
            sage: L.bounding_box()                                                      # needs sage.symbolic
            ((10.0, 99.0, -6.802394763324311),
             (30.0, 899.0, -4.605170185988092))
        """
    def tachyon_repr(self, render_params):
        """
        Return representation of the line suitable for plotting
        using the Tachyon ray tracer.

        TESTS::

            sage: L = line3d([(cos(i),sin(i),i^2) for i in srange(0,10,.01)],           # needs sage.symbolic
            ....:            color='red')
            sage: L.tachyon_repr(L.default_render_params())[0]                          # needs sage.symbolic
            'FCylinder base 1.0 0.0 0.0 apex 0.9999500004166653 0.009999833334166664 0.0001 rad 0.005 texture...'
        """
    def obj_repr(self, render_params):
        """
        Return complete representation of the line as an object.

        TESTS::

            sage: from sage.plot.plot3d.shapes2 import Line
            sage: L = Line([(cos(i),sin(i),i^2) for i in srange(0,10,.01)],             # needs sage.symbolic
            ....:          color='red')
            sage: L.obj_repr(L.default_render_params())[0][0][0][2][:3]                 # needs sage.symbolic
            ['v 0.99995 0.00999983 0.0001',
             'v 1.02376 0.010195 -0.00750607',
             'v 1.00007 0.0102504 -0.0248984']
        """
    def jmol_repr(self, render_params):
        """
        Return representation of the object suitable for plotting
        using Jmol.

        TESTS::

            sage: L = line3d([(cos(i),sin(i),i^2) for i in srange(0,10,.01)],           # needs sage.symbolic
            ....:            color='red')
            sage: L.jmol_repr(L.default_render_params())[0][:42]                        # needs sage.symbolic
            'draw line_1 diameter 1 curve {1.0 0.0 0.0}'
        """
    def corners(self, corner_cutoff=None, max_len=None):
        """
        Figure out where the curve turns too sharply to pretend it is
        smooth.

        INPUT:

        - ``corner_cutoff`` -- (default: ``None``) if the
          cosine of the angle between adjacent line segments is smaller than
          this bound, then there will be a sharp corner in the path.
          Otherwise, the path is smoothed. If ``None``,
          then the default value 0.5 is used.

        - ``max_len`` -- (default: ``None``) maximum number
          of points allowed in a single path. If this is set, this
          creates corners at smooth points in order to break the path
          into smaller pieces.

        The parameter ``corner_cutoff`` is a bound for the cosine of the
        angle made by two successive segments. This angle is close to `0`
        (and the cosine close to 1) if the two successive segments are
        almost aligned and close to `\\pi` (and the cosine close to -1) if
        the path has a strong peak. If the cosine is smaller than the
        bound (which means a sharper peak) then there must be a corner.

        OUTPUT:

        List of points at which to start a new line. This always
        includes the first point, and never the last.

        EXAMPLES:

        No corners, always smooth::

            sage: from sage.plot.plot3d.shapes2 import Line
            sage: Line([(0,0,0),(1,0,0),(2,1,0),(0,1,0)], corner_cutoff=-1).corners()
            [(0, 0, 0)]

        Smooth if the angle is greater than 90 degrees::

            sage: Line([(0,0,0),(1,0,0),(2,1,0),(0,1,0)], corner_cutoff=0).corners()
            [(0, 0, 0), (2, 1, 0)]

        Every point (corners everywhere)::

            sage: Line([(0,0,0),(1,0,0),(2,1,0),(0,1,0)], corner_cutoff=1).corners()
            [(0, 0, 0), (1, 0, 0), (2, 1, 0)]
        """
    def threejs_repr(self, render_params):
        """
        Return representation of the line suitable for plotting with three.js.

        EXAMPLES::

            sage: L = line3d([(1,2,3), (4,5,6)], thickness=10, color=(1,0,0), opacity=0.5)
            sage: L.threejs_repr(L.default_render_params())
            [('line',
              {'color': '#ff0000',
               'linewidth': 10.0,
               'opacity': 0.5,
               'points': [(1.0, 2.0, 3.0), (4.0, 5.0, 6.0)]})]

        TESTS:

        Transformations apply to the line's vertices::

            sage: L = line3d([(1,2,3), (4,5,6)]).translate(-1, -2, -3)
            sage: L.threejs_repr(L.default_render_params())
            [('line',
              {'color': '#6666ff',
               'linewidth': 1.0,
               'opacity': 1.0,
               'points': [(0.0, 0.0, 0.0), (3.0, 3.0, 3.0)]})]

        When setting ``arrow_head=True``, the last line segment is replaced by
        an arrow with a width half the thickness of the line::

            sage: L = line3d([(0,0,0), (1,1,1), (2,2,2)], thickness=4, arrow_head=True)
            sage: L_repr = L.threejs_repr(L.default_render_params())
            sage: L_repr[-1]
            ('line',
              {'color': '#6666ff',
               'linewidth': 4.0,
               'opacity': 1.0,
               'points': [(0.0, 0.0, 0.0), (1.0, 1.0, 1.0)]})
            sage: A = arrow3d((1,1,1), (2,2,2), width=2)
            sage: A_repr = A.threejs_repr(A.default_render_params())
            sage: A_repr == L_repr[:-1]
            True

        The arrow shares the transformation, color, and opacity of the line::

            sage: L = line3d([(0,0,0), (1,1,1), (2,2,2)], thickness=4,
            ....:            arrow_head=True, color=(1,0,0), opacity=0.5)
            sage: L = L.translate(-1, -1, -1)
            sage: L_repr = L.threejs_repr(L.default_render_params())
            sage: L_repr[-1]
            ('line',
              {'color': '#ff0000',
               'linewidth': 4.0,
               'opacity': 0.5,
               'points': [(-1.0, -1.0, -1.0), (0.0, 0.0, 0.0)]})
            sage: A = arrow3d((1,1,1), (2,2,2), width=2, color=(1,0,0), opacity=0.5)
            sage: A = A.translate(-1, -1, -1)
            sage: A_repr = A.threejs_repr(A.default_render_params())
            sage: A_repr == L_repr[:-1]
            True

        If there were only two points to begin with, only the arrow head's
        representation is returned::

            sage: L = line3d([(0,0,0), (1,1,1)], thickness=2, arrow_head=True)
            sage: L_repr = L.threejs_repr(L.default_render_params())
            sage: A = arrow3d((0,0,0), (1,1,1), width=1)
            sage: A_repr = A.threejs_repr(A.default_render_params())
            sage: A_repr == L_repr
            True
        """
    def stl_binary_repr(self, render_params):
        """
        Return an empty list, as this is not useful for STL export.

        EXAMPLES::

            sage: L = line3d([(1,2,3), (4,5,6)]).translate(-1, -2, -3)
            sage: L.stl_binary_repr(L.default_render_params())
            []
        """

def point3d(v, size: int = 5, **kwds):
    """
    Plot a point or list of points in 3d space.

    INPUT:

    - ``v`` -- a point or list of points

    - ``size`` -- (default: 5) size of the point (or
      points)

    - ``color`` -- string (``'red'``, ``'green'`` etc)
      or a tuple (r, g, b) with r, g, b numbers between 0 and 1

    - ``opacity`` -- (default: 1) if less than 1 then is
      transparent

    EXAMPLES::

        sage: sum(point3d((i,i^2,i^3), size=5) for i in range(10))
        Graphics3d Object

    .. PLOT::

        sphinx_plot(sum([point3d((i,i^2,i^3), size=5) for i in range(10)]))

    We check to make sure this works with vectors and other iterables::

        sage: pl = point3d([vector(ZZ,(1, 0, 0)), vector(ZZ,(0, 1, 0)), (-1, -1, 0)])
        sage: print(point(vector((2,3,4))))
        Graphics3d Object

        sage: c = polytopes.hypercube(3)                                                # needs sage.geometry.polyhedron
        sage: v = c.vertices()[0];  v                                                   # needs sage.geometry.polyhedron
        A vertex at (1, -1, -1)
        sage: print(point(v))                                                           # needs sage.geometry.polyhedron
        Graphics3d Object

    We check to make sure the options work::

        sage: point3d((4,3,2), size=20, color='red', opacity=.5)
        Graphics3d Object

    .. PLOT::

        sphinx_plot(point3d((4,3,2),size=20,color='red',opacity=.5))

    numpy arrays can be provided as input::

        sage: import numpy
        sage: point3d(numpy.array([1,2,3]))
        Graphics3d Object

    .. PLOT::

        import numpy
        sphinx_plot(point3d(numpy.array([1,2,3])))

    ::

        sage: point3d(numpy.array([[1,2,3], [4,5,6], [7,8,9]]))
        Graphics3d Object

    .. PLOT::

        import numpy
        sphinx_plot(point3d(numpy.array([[1,2,3], [4,5,6], [7,8,9]])))

    We check that iterators of points are accepted (:issue:`13890`)::

        sage: point3d(iter([(1,1,2),(2,3,4),(3,5,8)]), size=20, color='red')
        Graphics3d Object

    TESTS::

        sage: point3d([])
        Graphics3d Object
    """
