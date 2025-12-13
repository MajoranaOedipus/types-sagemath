from _typeshed import Incomplete
from sage.misc.decorators import options as options, rename_keyword as rename_keyword
from sage.plot.colors import to_mpl_color as to_mpl_color
from sage.plot.primitive import GraphicPrimitive as GraphicPrimitive

class Disk(GraphicPrimitive):
    """
    Primitive class for the ``Disk`` graphics type.  See ``disk?`` for
    information about actually plotting a disk (the Sage term for a sector
    or wedge of a circle).

    INPUT:

    - ``point`` -- coordinates of center of disk

    - ``r`` -- radius of disk

    - ``angle`` -- beginning and ending angles of disk (i.e.
      angle extent of sector/wedge)

    - ``options`` -- dictionary of valid plot options to pass to constructor

    EXAMPLES:

    Note this should normally be used indirectly via ``disk``::

        sage: from math import pi
        sage: from sage.plot.disk import Disk
        sage: D = Disk((1,2), 2, (pi/2,pi), {'zorder':3})
        sage: D
        Disk defined by (1.0,2.0) with r=2.0
         spanning (1.5707963267..., 3.1415926535...) radians
        sage: D.options()['zorder']
        3
        sage: D.x
        1.0

    TESTS:

    We test creating a disk::

        sage: disk((2,3), 2, (0,pi/2))
        Graphics object consisting of 1 graphics primitive
    """
    x: Incomplete
    y: Incomplete
    r: Incomplete
    rad1: Incomplete
    rad2: Incomplete
    def __init__(self, point, r, angle, options) -> None:
        """
        Initialize base class ``Disk``.

        EXAMPLES::

            sage: from math import pi
            sage: D = disk((2,3), 1, (pi/2, pi), fill=False, color='red', thickness=1, alpha=.5)
            sage: D[0].x
            2.0
            sage: D[0].r
            1.0
            sage: D[0].rad1
            1.5707963267948966
            sage: D[0].options()['rgbcolor']
            'red'
            sage: D[0].options()['alpha']
            0.500000000000000
            sage: print(loads(dumps(D)))
            Graphics object consisting of 1 graphics primitive
        """
    def get_minmax_data(self):
        """
        Return a dictionary with the bounding box data.

        EXAMPLES::

            sage: from math import pi
            sage: D = disk((5,4), 1, (pi/2, pi))
            sage: d = D.get_minmax_data()
            sage: d['xmin']
            4.0
            sage: d['ymin']
            3.0
            sage: d['xmax']
            6.0
            sage: d['ymax']
            5.0
        """
    def plot3d(self, z: int = 0, **kwds):
        """
        Plots a 2D disk (actually a 52-gon) in 3D,
        with default height zero.

        INPUT:

        - ``z`` -- (optional) 3D height above `xy`-plane

        AUTHORS:

        - Karl-Dieter Crisman (05-09)

        EXAMPLES::

            sage: from math import pi
            sage: disk((0,0), 1, (0, pi/2)).plot3d()
            Graphics3d Object
            sage: disk((0,0), 1, (0, pi/2)).plot3d(z=2)
            Graphics3d Object
            sage: disk((0,0), 1, (pi/2, 0), fill=False).plot3d(3)
            Graphics3d Object


        These examples show that the appropriate options are passed::

            sage: D = disk((2,3), 1, (pi/4,pi/3), hue=.8, alpha=.3, fill=True)
            sage: d = D[0]
            sage: d.plot3d(z=2).texture.opacity
            0.3

        ::

            sage: D = disk((2,3), 1, (pi/4,pi/3), hue=.8, alpha=.3, fill=False)
            sage: d = D[0]
            sage: dd = d.plot3d(z=2)
            sage: dd.jmol_repr(dd.testing_render_params())[0][-1]
            'color $line_4 translucent 0.7 [204,0,255]'
        """

def disk(point, radius, angle, **options):
    """
    A disk (that is, a sector or wedge of a circle) with center
    at a point = `(x,y)` (or `(x,y,z)` and parallel to the
    `xy`-plane) with radius = `r` spanning (in radians)
    angle=`(rad1, rad2)`.

    Type ``disk.options`` to see all options.

    EXAMPLES:

    Make some dangerous disks::

        sage: from math import pi
        sage: bl = disk((0.0,0.0), 1, (pi, 3*pi/2), color='yellow')
        sage: tr = disk((0.0,0.0), 1, (0, pi/2), color='yellow')
        sage: tl = disk((0.0,0.0), 1, (pi/2, pi), color='black')
        sage: br = disk((0.0,0.0), 1, (3*pi/2, 2*pi), color='black')
        sage: P  = tl + tr + bl + br
        sage: P.show(xmin=-2, xmax=2, ymin=-2, ymax=2)

    .. PLOT::

        from sage.plot.disk import Disk
        bl = disk((0.0,0.0), 1, (pi, 3*pi/2), color='yellow')
        tr = disk((0.0,0.0), 1, (0, pi/2), color='yellow')
        tl = disk((0.0,0.0), 1, (pi/2, pi), color='black')
        br = disk((0.0,0.0), 1, (3*pi/2, 2*pi), color='black')
        P  = tl+tr+bl+br
        sphinx_plot(P)

    The default aspect ratio is 1.0::

        sage: disk((0.0,0.0), 1, (pi, 3*pi/2)).aspect_ratio()
        1.0

    Another example of a disk::

        sage: bl = disk((0.0,0.0), 1, (pi, 3*pi/2), rgbcolor=(1,1,0))
        sage: bl.show(figsize=[5,5])

    .. PLOT::

        from sage.plot.disk import Disk
        bl = disk((0.0,0.0), 1, (pi, 3*pi/2), rgbcolor=(1,1,0))
        sphinx_plot(bl)

    Note that since ``thickness`` defaults to zero, it is best to change
    that option when using ``fill=False``::

        sage: disk((2,3), 1, (pi/4,pi/3), hue=.8, alpha=.3, fill=False, thickness=2)
        Graphics object consisting of 1 graphics primitive

    .. PLOT::

        from sage.plot.disk import Disk
        D = disk((2,3), 1, (pi/4,pi/3), hue=.8, alpha=.3, fill=False, thickness=2)
        sphinx_plot(D)

    The previous two examples also illustrate using ``hue`` and ``rgbcolor``
    as ways of specifying the color of the graphic.

    We can also use this command to plot three-dimensional disks parallel
    to the `xy`-plane::

        sage: d = disk((1,1,3), 1, (pi,3*pi/2), rgbcolor=(1,0,0))
        sage: d
        Graphics3d Object
        sage: type(d)
        <... 'sage.plot.plot3d.index_face_set.IndexFaceSet'>

    .. PLOT::

        from sage.plot.disk import Disk
        d = disk((1,1,3), 1, (pi,3*pi/2), rgbcolor=(1,0,0))
        sphinx_plot(d)

    Extra options will get passed on to ``show()``, as long as they are valid::

        sage: disk((0, 0), 5, (0, pi/2), rgbcolor=(1, 0, 1),
        ....:      xmin=0, xmax=5, ymin=0, ymax=5, figsize=(2,2))
        Graphics object consisting of 1 graphics primitive
        sage: disk((0, 0), 5, (0, pi/2), rgbcolor=(1, 0, 1)).show(  # These are equivalent
        ....:     xmin=0, xmax=5, ymin=0, ymax=5, figsize=(2,2))

    TESTS:

    Testing that legend labels work right::

        sage: disk((2,4), 3, (pi/8, pi/4), hue=1, legend_label='disk', legend_color='blue')
        Graphics object consisting of 1 graphics primitive

    We cannot currently plot disks in more than three dimensions::

        sage: d = disk((1,1,1,1), 1, (0,pi))
        Traceback (most recent call last):
        ...
        ValueError: the center point of a plotted disk should have two or three coordinates

    Verify that :issue:`36153` is fixed::

        sage: D = disk((0, 0), 5, (0, pi/2), legend_label='test')
    """
