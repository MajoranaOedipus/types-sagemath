from .tri_plot import SmoothTriangle as SmoothTriangle, Triangle as Triangle, TriangleFactory as TriangleFactory, TrianglePlot as TrianglePlot
from sage.interfaces.tachyon import tachyon_rt as tachyon_rt
from sage.misc.fast_methods import WithEqualityById as WithEqualityById
from sage.misc.temporary_file import tmp_filename as tmp_filename
from sage.misc.verbose import get_verbose as get_verbose
from sage.structure.sage_object import SageObject as SageObject

class Tachyon(WithEqualityById, SageObject):
    """
    Create a scene the can be rendered using the Tachyon ray tracer.

    INPUT:

    - ``xres`` -- (default: 350)
    - ``yres`` -- (default: 350)
    - ``zoom`` -- (default: 1.0)
    - ``antialiasing`` -- (default: ``False``)
    - ``aspectratio`` -- (default: 1.0)
    - ``raydepth`` -- (default: 8)
    - ``camera_position`` -- (default: (-3, 0, 0))
    - ``updir`` -- (default: (0, 0, 1))
    - ``look_at`` -- (default: (0,0,0))
    - ``viewdir`` -- (default: ``None``) otherwise list of three numbers
    - ``projection`` -- ``'PERSPECTIVE'`` (default) ``'perspective_dof'``
      or ``'fisheye'``
    - ``frustum`` -- (default: ``''``) otherwise list of four numbers. Only
      used with ``projection='fisheye'``.
    - ``focallength`` -- (default: ``''``) otherwise a number. Only used
      with ``projection='perspective_dof'``.
    - ``aperture`` -- (default: ``''``) otherwise a number.  Only used
      with ``projection='perspective_dof'``.

    OUTPUT: a Tachyon 3d scene

    Note that the coordinates are by default such that `z` is
    up, positive `y` is to the {left} and `x` is toward
    you. This is not oriented according to the right hand rule.

    EXAMPLES: Spheres along the twisted cubic.

    ::

        sage: t = Tachyon(xres=512,yres=512, camera_position=(3,0.3,0))
        sage: t.light((4,3,2), 0.2, (1,1,1))
        sage: t.texture('t0', ambient=0.1, diffuse=0.9, specular=0.5, opacity=1.0, color=(1.0,0,0))
        sage: t.texture('t1', ambient=0.1, diffuse=0.9, specular=0.3, opacity=1.0, color=(0,1.0,0))
        sage: t.texture('t2', ambient=0.2, diffuse=0.7, specular=0.5, opacity=0.7, color=(0,0,1.0))
        sage: k=0
        sage: for i in srange(-1,1,0.05):
        ....:    k += 1
        ....:    t.sphere((i,i^2-0.5,i^3), 0.1, 't%s'%(k%3))
        sage: t.show()

    Another twisted cubic, but with a white background, got by putting
    infinite planes around the scene.

    ::

        sage: t = Tachyon(xres=512,yres=512, camera_position=(3,0.3,0), raydepth=8)
        sage: t.light((4,3,2), 0.2, (1,1,1))
        sage: t.texture('t0', ambient=0.1, diffuse=0.9, specular=0.5, opacity=1.0, color=(1.0,0,0))
        sage: t.texture('t1', ambient=0.1, diffuse=0.9, specular=0.3, opacity=1.0, color=(0,1.0,0))
        sage: t.texture('t2', ambient=0.2,diffuse=0.7, specular=0.5, opacity=0.7, color=(0,0,1.0))
        sage: t.texture('white', color=(1,1,1))
        sage: t.plane((0,0,-1), (0,0,1), 'white')
        sage: t.plane((0,-20,0), (0,1,0), 'white')
        sage: t.plane((-20,0,0), (1,0,0), 'white')

    ::

        sage: k=0
        sage: for i in srange(-1,1,0.05):
        ....:    k += 1
        ....:    t.sphere((i,i^2 - 0.5,i^3), 0.1, 't%s'%(k%3))
        ....:    t.cylinder((0,0,0), (0,0,1), 0.05,'t1')
        sage: t.show()

    Many random spheres::

        sage: t = Tachyon(xres=512,yres=512, camera_position=(2,0.5,0.5), look_at=(0.5,0.5,0.5), raydepth=4)
        sage: t.light((4,3,2), 0.2, (1,1,1))
        sage: t.texture('t0', ambient=0.1, diffuse=0.9, specular=0.5, opacity=1.0, color=(1.0,0,0))
        sage: t.texture('t1', ambient=0.1, diffuse=0.9, specular=0.3, opacity=1.0, color=(0,1.0,0))
        sage: t.texture('t2', ambient=0.2, diffuse=0.7, specular=0.5, opacity=0.7, color=(0,0,1.0))
        sage: k=0
        sage: for i in range(100):
        ....:    k += 1
        ....:    t.sphere((random(),random(), random()), random()/10, 't%s'%(k%3))
        sage: t.show()

    Points on an elliptic curve, their height indicated by their height
    above the axis::

        sage: # needs sage.schemes
        sage: t = Tachyon(camera_position=(5,2,2), look_at=(0,1,0))
        sage: t.light((10,3,2), 0.2, (1,1,1))
        sage: t.texture('t0', ambient=0.1, diffuse=0.9, specular=0.5, opacity=1.0, color=(1,0,0))
        sage: t.texture('t1', ambient=0.1, diffuse=0.9, specular=0.5, opacity=1.0, color=(0,1,0))
        sage: t.texture('t2', ambient=0.1, diffuse=0.9, specular=0.5, opacity=1.0, color=(0,0,1))
        sage: E = EllipticCurve('37a')                                                  # needs sage.schemes
        sage: P = E([0,0])                                                              # needs sage.schemes
        sage: Q = P                                                                     # needs sage.schemes
        sage: n = 100
        sage: for i in range(n):   # increase 20 for a better plot                      # needs sage.schemes
        ....:    Q = Q + P
        ....:    t.sphere((Q[1], Q[0], ZZ(i)/n), 0.1, 't%s'%(i%3))
        sage: t.show()                                                                  # needs sage.schemes

    A beautiful picture of rational points on a rank 1 elliptic curve.

    ::

        sage: # needs sage.schemes
        sage: t = Tachyon(xres=1000, yres=800, camera_position=(2,7,4),
        ....:             look_at=(2,0,0), raydepth=4)
        sage: t.light((10,3,2), 1, (1,1,1))
        sage: t.light((10,-3,2), 1, (1,1,1))
        sage: t.texture('black', color=(0,0,0))
        sage: t.texture('red', color=(1,0,0))
        sage: t.texture('grey', color=(.9,.9,.9))
        sage: t.plane((0,0,0),(0,0,1),'grey')
        sage: t.cylinder((0,0,0),(1,0,0),.01,'black')
        sage: t.cylinder((0,0,0),(0,1,0),.01,'black')
        sage: E = EllipticCurve('37a')                                                  # needs sage.schemes
        sage: P = E([0,0])                                                              # needs sage.schemes
        sage: Q = P                                                                     # needs sage.schemes
        sage: n = 100
        sage: for i in range(n):                                                        # needs sage.schemes
        ....:    Q = Q + P
        ....:    c = i/n + .1
        ....:    t.texture('r%s'%i,color=(float(i/n),0,0))
        ....:    t.sphere((Q[0], -Q[1], .01), .04, 'r%s'%i)
        sage: t.show()                          # long time                             # needs sage.schemes

    A beautiful spiral.

    ::

        sage: t = Tachyon(xres=800, yres=800, camera_position=(2,5,2), look_at=(2.5,0,0))
        sage: t.light((0,0,100), 1, (1,1,1))
        sage: t.texture('r', ambient=0.1, diffuse=0.9, specular=0.5,
        ....:           opacity=1.0, color=(1,0,0))
        sage: for i in srange(0,50,0.1):
        ....:    t.sphere((i/10.0,sin(i),cos(i)), 0.05, 'r')
        sage: t.texture('white', color=(1,1,1), opacity=1, specular=1, diffuse=1)
        sage: t.plane((0,0,-100), (0,0,-100), 'white')
        sage: t.show()

    If the optional parameter ``viewdir`` is not set, the camera
    center should not coincide with the point which
    is looked at (see :issue:`7232`)::

        sage: t = Tachyon(xres=80,yres=80, camera_position=(2,5,2), look_at=(2,5,2))
        Traceback (most recent call last):
        ...
        ValueError: camera_position and look_at coincide

    Use of a fisheye lens perspective. ::

        sage: T = Tachyon(xres=800, yres=600, camera_position=(-1.5,-1.5,.3),
        ....:             projection='fisheye', frustum=(-1.0, 1.0, -1.0, 1.0))
        sage: T.texture('t1', color=(0,0,1))
        sage: cedges = [[[1, 1, 1], [-1, 1, 1]], [[1, 1, 1], [1, -1, 1]],
        ....:           [[1, 1, 1], [1, 1, -1]], [[-1, 1, 1], [-1, -1, 1]],
        ....:           [[-1, 1, 1], [-1, 1, -1]], [[1, -1, 1], [-1, -1, 1]],
        ....:           [[1, -1, 1], [1, -1, -1]], [[-1, -1, 1], [-1, -1, -1]],
        ....:           [[1, 1, -1], [-1, 1, -1]], [[1, 1, -1], [1, -1, -1]],
        ....:           [[-1, 1, -1], [-1, -1, -1]], [[1, -1, -1], [-1, -1, -1]]]
        sage: for ed in cedges:
        ....:     T.fcylinder(ed[0], ed[1], .05, 't1')
        sage: T.light((-4,-4,4), .1, (1,1,1))
        sage: T.show()

    Use of the ``projection='perspective_dof'`` option.  This may not be
    implemented correctly. ::

        sage: T = Tachyon(xres=800, antialiasing=4, raydepth=10,
        ....:             projection='perspective_dof', focallength='1.0', aperture='.0025')
        sage: T.light((0,5,7), 1.0, (1,1,1))
        sage: T.texture('t1', opacity=1, specular=.3)
        sage: T.texture('t2', opacity=1, specular=.3, color=(0,0,1))
        sage: T.texture('t3', opacity=1, specular=1, color=(1,.8,1), diffuse=0.2)
        sage: T.plane((0,0,-1), (0,0,1), 't3')
        sage: ttlist = ['t1', 't2']
        sage: tt = 't1'
        sage: T.cylinder((0,0,.1), (1,1/3,0), .05, 't3')
        sage: for q in srange(-3, 100, .15):
        ....:     if tt == 't1':
        ....:         tt = 't2'
        ....:     else:
        ....:         tt = 't1'
        ....:     T.sphere((q, q/3+.3*sin(3*q), .1+.3*cos(3*q)), .1, tt)
        sage: T.show()

    TESTS::

        sage: hash(Tachyon()) # random
        140658972348064
    """
    def __init__(self, xres: int = 350, yres: int = 350, zoom: float = 1.0, antialiasing: bool = False, aspectratio: float = 1.0, raydepth: int = 8, camera_position=None, camera_center=None, updir=[0, 0, 1], look_at=[0, 0, 0], viewdir=None, projection: str = 'PERSPECTIVE', focallength: str = '', aperture: str = '', frustum: str = '') -> None:
        """
        Create an instance of the Tachyon class.

        EXAMPLES::

            sage: t = Tachyon()
            sage: t._xres
            350
        """
    def save_image(self, filename=None, *args, **kwds) -> None:
        """
        Save an image representation of ``self``.

        The image type is
        determined by the extension of the filename.  For example,
        this could be ``.png``, ``.jpg``, ``.gif``, ``.pdf``,
        ``.svg``.  Currently this is implemented by calling the
        :meth:`save` method of self, passing along all arguments and
        keywords.

        .. NOTE::

            Not all image types are necessarily implemented for all
            graphics types.  See :meth:`save` for more details.

        EXAMPLES::

            sage: q = Tachyon()
            sage: q.light((1,1,11), 1,(1,1,1))
            sage: q.texture('s')
            sage: q.sphere((0,-1,1),1,'s')
            sage: tempname = tmp_filename()
            sage: q.save_image(tempname)

        TESTS:

        :meth:`save_image` is used for generating animations::

            sage: def tw_cubic(t):
            ....:     q = Tachyon()
            ....:     q.light((1,1,11), 1,(1,1,1))
            ....:     q.texture('s')
            ....:     for i in srange(-1,t,0.05):
            ....:         q.sphere((i,i^2-0.5,i^3), 0.1, 's')
            ....:     return q

            sage: a = animate([tw_cubic(t) for t in srange(-1,1,.3)])
            sage: a        # optional -- ImageMagick
            Animation with 7 frames
            sage: a.show() # optional -- ImageMagick
        """
    def save(self, filename: str = 'sage.png', verbose=None, extra_opts: str = '') -> None:
        """
        Save rendering of the tachyon scene.

        INPUT:

        - ``filename`` -- (default: ``'sage.png'``) output
          filename; the extension of the filename determines the type.
          Supported types include:

        - ``tga`` -- 24-bit (uncompressed)

        - ``bmp`` -- 24-bit Windows BMP (uncompressed)

        - ``ppm`` -- 24-bit PPM (uncompressed)

        - ``rgb`` -- 24-bit SGI RGB (uncompressed)

        - ``png`` -- 24-bit PNG (compressed, lossless)

        - ``verbose`` -- integer (default: ``None``); if no verbosity setting
          is supplied, the verbosity level set by
          ``sage.misc.verbose.set_verbose`` is used.

        - ``0`` -- silent

        - ``1`` -- some output

        - ``2`` -- very verbose output

        - ``extra_opts`` -- passed directly to tachyon command
          line. Use ``tachyon_rt.usage()`` to see some of the possibilities.

        EXAMPLES::

            sage: q = Tachyon()
            sage: q.light((1,1,11), 1,(1,1,1))
            sage: q.texture('s')
            sage: q.sphere((0,0,0),1,'s')
            sage: tempname = tmp_filename()
            sage: q.save(tempname)
        """
    def show(self, **kwds) -> None:
        '''
        Create a PNG file of the scene.

        This method attempts to display the graphics immediately,
        without waiting for the currently running code (if any) to
        return to the command line. Be careful, calling it from within
        a loop will potentially launch a large number of external
        viewer programs.

        OUTPUT:

        This method does not return anything. Use :meth:`save` if you
        want to save the figure as an image.

        EXAMPLES:

        This example demonstrates how the global Sage verbosity setting
        is used if none is supplied. Firstly, using a global verbosity
        setting of 0 means no extra technical information is displayed,
        and we are simply shown the plot.

        ::

            sage: h = Tachyon(xres=512, yres=512, camera_position=(4,-4,3),
            ....:             viewdir=(-4,4,-3), raydepth=4)
            sage: h.light((4.4,-4.4,4.4), 0.2, (1,1,1))
            sage: def f(x, y): return float(sin(x*y))
            sage: h.texture(\'t0\', ambient=0.1, diffuse=0.9, specular=0.1,
            ....:           opacity=1.0, color=(1.0,0,0))
            sage: h.plot(f, (-4,4), (-4,4), "t0", max_depth=5, initial_depth=3,         # needs sage.symbolic
            ....:        num_colors=60)  # increase min_depth for better picture
            sage: from sage.misc.verbose import set_verbose, get_verbose
            sage: set_verbose(0)
            sage: h.show()                                                              # needs sage.symbolic

        This second example, using a "medium" global verbosity
        setting of 1, displays some extra technical information then
        displays our graph.

        ::

            sage: s = Tachyon(xres=512, yres=512, camera_position=(4,-4,3),
            ....:             viewdir=(-4,4,-3), raydepth=4)
            sage: s.light((4.4,-4.4,4.4), 0.2, (1,1,1))
            sage: def f(x, y): return float(sin(x*y))
            sage: s.texture(\'t0\', ambient=0.1, diffuse=0.9, specular=0.1,
            ....:           opacity=1.0, color=(1.0,0,0))
            sage: s.plot(f, (-4,4), (-4,4), "t0", max_depth=5, initial_depth=3,         # needs sage.symbolic
            ....:        num_colors=60)  # increase min_depth for better picture
            sage: set_verbose(1)
            sage: s.show()                                                              # needs sage.symbolic
            tachyon ...
            Scene contains 2713 objects.
            ...

        The last example shows how you can override the global Sage
        verbosity setting, my supplying a setting level as an argument.
        In this case we chose the highest verbosity setting level, 2,
        so much more extra technical information is shown, along with
        the plot.

        ::

            sage: set_verbose(0)
            sage: d = Tachyon(xres=512, yres=512, camera_position=(4,-4,3),
            ....:             viewdir=(-4,4,-3), raydepth=4)
            sage: d.light((4.4,-4.4,4.4), 0.2, (1,1,1))
            sage: def f(x, y): return float(sin(x*y))
            sage: d.texture(\'t0\', ambient=0.1, diffuse=0.9, specular=0.1,
            ....:           opacity=1.0, color=(1.0,0,0))
            sage: d.plot(f,(-4,4),(-4,4),"t0",max_depth=5,initial_depth=3,              # needs sage.symbolic
            ....:        num_colors=60)  # increase min_depth for better picture
            sage: get_verbose()
            0
            sage: d.show(verbose=2)                                                     # needs sage.symbolic
            tachyon ...
            Scene contains 2713 objects.
            ...
            Scene contains 1 non-gridded objects
            ...
        '''
    def str(self):
        """
        Return the complete tachyon scene file as a string.

        EXAMPLES::

            sage: t = Tachyon(xres=500,yres=500, camera_position=(2,0,0))
            sage: t.light((4,3,2), 0.2, (1,1,1))
            sage: t.texture('t2', ambient=0.1, diffuse=0.9, specular=0.5, opacity=1.0, color=(1,0,0))
            sage: t.texture('t3', ambient=0.1, diffuse=0.9, specular=0.5, opacity=1.0, color=(0,1,0))
            sage: t.texture('t4', ambient=0.1, diffuse=0.9, specular=0.5, opacity=1.0, color=(0,0,1))
            sage: t.sphere((0,0.5,0), 0.2, 't2')
            sage: t.sphere((0.5,0,0), 0.2, 't3')
            sage: t.sphere((0,0,0.5), 0.2, 't4')
            sage: 'PLASTIC' in t.str()
            True
        """
    def light(self, center, radius, color) -> None:
        """
        Create a light source of the given center, radius, and color.

        EXAMPLES::

            sage: q = Tachyon()
            sage: q.light((1,1,1),1.0,(.2,0,.8))
            sage: q.str().split('\\n')[17]
            '        light center  1.0 1.0 1.0 '
        """
    def texfunc(self, type: int = 0, center=(0, 0, 0), rotate=(0, 0, 0), scale=(1, 1, 1), imagefile: str = ''):
        """
        INPUT:

        - ``type`` -- (default: 0)

           0. No special texture, plain shading
           1. 3D checkerboard function, like a rubik's cube
           2. Grit Texture, randomized surface color
           3. 3D marble texture, uses object's base color
           4. 3D wood texture, light and dark brown, not very good yet
           5. 3D gradient noise function (can't remember what it looks
              like)
           6. Don't remember
           7. Cylindrical Image Map, requires ppm filename (with path)
           8. Spherical Image Map, requires ppm filename (with path)
           9. Planar Image Map, requires ppm filename (with path)

        - ``center`` -- (default: (0,0,0))
        - ``rotate`` -- (default: (0,0,0))
        - ``scale`` -- (default: (1,1,1))

        EXAMPLES: We draw an infinite checkerboard::

            sage: t = Tachyon(camera_position=(2,7,4), look_at=(2,0,0))
            sage: t.texture('black', color=(0,0,0), texfunc=1)
            sage: t.plane((0,0,0),(0,0,1),'black')
            sage: t.show()
        """
    def texture(self, name, ambient: float = 0.2, diffuse: float = 0.8, specular: float = 0.0, opacity: float = 1.0, color=(1.0, 0.0, 0.5), texfunc: int = 0, phong: int = 0, phongsize: float = 0.5, phongtype: str = 'PLASTIC', imagefile: str = '') -> None:
        """
        INPUT:

        - ``name`` -- string; the name of the texture (to be
          used later)

        - ``ambient`` -- (default: 0.2)

        - ``diffuse`` -- (default: 0.8)

        - ``specular`` -- (default: 0.0)

        - ``opacity`` -- (default: 1.0)

        - ``color`` -- (default: (1.0,0.0,0.5))

        - ``texfunc`` -- (default: 0) a texture function; this
          is either the output of self.texfunc, or a number between 0 and 9,
          inclusive. See the docs for self.texfunc.

        - ``phong`` -- (default: 0)

        - ``phongsize`` -- (default: 0.5)

        - ``phongtype`` -- (default: ``'PLASTIC'``)

        EXAMPLES:

        We draw a scene with 4 spheres that illustrates various uses of
        the texture command::

            sage: t = Tachyon(camera_position=(2,5,4), look_at=(2,0,0), raydepth=6)
            sage: t.light((10,3,4), 1, (1,1,1))
            sage: t.texture('mirror', ambient=0.05, diffuse=0.05, specular=.9,
            ....:           opacity=0.9, color=(.8,.8,.8))
            sage: t.texture('grey', color=(.8,.8,.8), texfunc=3)
            sage: t.plane((0,0,0),(0,0,1),'grey')
            sage: t.sphere((4,-1,1), 1, 'mirror')
            sage: t.sphere((0,-1,1), 1, 'mirror')
            sage: t.sphere((2,-1,1), 0.5, 'mirror')
            sage: t.sphere((2,1,1), 0.5, 'mirror')
            sage: show(t)  # known bug (trac #7232)
        """
    def texture_recolor(self, name, colors):
        """
        Recolor default textures.

        EXAMPLES::

            sage: t = Tachyon()
            sage: t.texture('s')
            sage: q = t.texture_recolor('s',[(0,0,1)])
            sage: t._objects[1]._color
            (0.0, 0.0, 1.0)
        """
    def sphere(self, center, radius, texture) -> None:
        """
        Create the scene information for a sphere with the given
        center, radius, and texture.

        EXAMPLES::

            sage: t = Tachyon()
            sage: t.texture('sphere_texture')
            sage: t.sphere((1,2,3), .1, 'sphere_texture')
            sage: t._objects[1].str()
            '\\n        sphere center  1.0 2.0 3.0  rad 0.1 sphere_texture\\n        '
        """
    def ring(self, center, normal, inner, outer, texture) -> None:
        """
        Create the scene information for a ring with the given parameters.

        EXAMPLES::

            sage: t = Tachyon()
            sage: t.ring([0,0,0], [0,0,1], 1.0, 2.0, 's')
            sage: t._objects[0]._center
            (0.0, 0.0, 0.0)
        """
    def cylinder(self, center, axis, radius, texture) -> None:
        """
        Create the scene information for a infinite cylinder with the
        given center, axis direction, radius, and texture.

        EXAMPLES::

            sage: t = Tachyon()
            sage: t.texture('c')
            sage: t.cylinder((0,0,0),(-1,-1,-1),.1,'c')
        """
    def plane(self, center, normal, texture) -> None:
        """
        Create an infinite plane with the given center and normal.

        TESTS::

            sage: t = Tachyon()
            sage: t.plane((0,0,0),(1,1,1),'s')
            sage: plane_pos = t.str().index('plane')
            sage: t.str()[plane_pos:plane_pos+42]
            'plane center  0.0 0.0 0.0  normal  1.0 1.0'
        """
    def axis_aligned_box(self, min_p, max_p, texture) -> None:
        """
        Create an axis-aligned box with minimal point ``min_p`` and
        maximum point ``max_p``.

        EXAMPLES::

            sage: t = Tachyon()
            sage: t.axis_aligned_box((0,0,0),(2,2,2),'s')
        """
    def fcylinder(self, base, apex, radius, texture) -> None:
        """
        Finite cylinders are almost the same as infinite ones, but the
        center and length of the axis determine the extents of the
        cylinder.

        The finite cylinder is also really a shell, it
        does not have any caps. If you need to close off the ends of
        the cylinder, use two ring objects, with the inner radius set
        to 0.0 and the normal set to be the axis of the cylinder.
        Finite cylinders are built this way to enhance speed.

        EXAMPLES::

            sage: t = Tachyon()
            sage: t.fcylinder((1,1,1),(1,2,3),.01,'s')
            sage: len(t.str())
            451
        """
    def triangle(self, vertex_1, vertex_2, vertex_3, texture) -> None:
        """
        Create a triangle with the given vertices and texture.

        EXAMPLES::

            sage: t = Tachyon()
            sage: t.texture('s')
            sage: t.triangle([1,2,3],[4,5,6],[7,8,10],'s')
            sage: t._objects[1].get_vertices()
            ([1, 2, 3], [4, 5, 6], [7, 8, 10])
        """
    def smooth_triangle(self, vertex_1, vertex_2, vertex_3, normal_1, normal_2, normal_3, texture) -> None:
        """
        Create a triangle along with a normal vector for smoothing.

        EXAMPLES::

            sage: t = Tachyon()
            sage: t.light((1,1,1),.1,(1,1,1))
            sage: t.texture('s')
            sage: t.smooth_triangle([0,0,0],[0,0,1],[0,1,0],[0,1,1],[-1,1,2],[3,0,0],'s')
            sage: t._objects[2].get_vertices()
            ([0, 0, 0], [0, 0, 1], [0, 1, 0])
            sage: t._objects[2].get_normals()
            ([0, 1, 1], [-1, 1, 2], [3, 0, 0])
        """
    def fractal_landscape(self, res, scale, center, texture) -> None:
        """
        Axis-aligned fractal landscape.

        Not very useful at the moment.

        EXAMPLES::

            sage: t = Tachyon()
            sage: t.texture('s')
            sage: t.fractal_landscape([30,30],[80,80],[0,0,0],'s')
            sage: len(t._objects)
            2
        """
    def plot(self, f, xmin_xmax, ymin_ymax, texture, grad_f=None, max_bend: float = 0.7, max_depth: int = 5, initial_depth: int = 3, num_colors=None) -> None:
        '''
        INPUT:

        - ``f`` -- function of two variables, which returns a
          float (or coercible to a float) (xmin,xmax)

        - ``(ymin,ymax)`` -- defines the rectangle to plot over
          texture: Name of texture to be used Optional arguments:

        - ``grad_f`` -- gradient function. If specified,
          smooth triangles will be used

        - ``max_bend`` -- cosine of the threshold angle
          between triangles used to determine whether or not to recurse after
          the minimum depth

        - ``max_depth`` -- maximum recursion depth. Maximum
          triangles plotted = `2^{2*max_depth}`

        - ``initial_depth`` -- minimum recursion depth. No
          error-tolerance checking is performed below this depth. Minimum
          triangles plotted: `2^{2*min_depth}`

        - ``num_colors`` -- number of rainbow bands to color
          the plot with. Texture supplied will be cloned (with different
          colors) using the texture_recolor method of the Tachyon object.


        Plots a function by constructing a mesh with nonstandard sampling
        density without gaps. At very high resolutions (depths 10) it
        becomes very slow. Cython may help. Complexity is approx.
        `O(2^{2*maxdepth})`. This algorithm has been optimized for
        speed, not memory - values from f(x,y) are recycled rather than
        calling the function multiple times. At high recursion depth, this
        may cause problems for some machines.

        Flat Triangles::

            sage: t = Tachyon(xres=512, yres=512, camera_position=(4,-4,3),
            ....:             viewdir=(-4,4,-3), raydepth=4)
            sage: t.light((4.4,-4.4,4.4), 0.2, (1,1,1))
            sage: def f(x, y): return float(sin(x*y))
            sage: t.texture(\'t0\', ambient=0.1, diffuse=0.9, specular=0.1,
            ....:           opacity=1.0, color=(1.0,0,0))
            sage: t.plot(f, (-4,4), (-4,4), "t0", max_depth=5, initial_depth=3,         # needs sage.symbolic
            ....:        num_colors=60)  # increase min_depth for better picture
            sage: t.show(verbose=1)                                                     # needs sage.symbolic
            tachyon ...
            Scene contains 2713 objects.
            ...

        Plotting with Smooth Triangles (requires explicit gradient
        function)::

            sage: t = Tachyon(xres=512, yres=512, camera_position=(4,-4,3),
            ....:             viewdir=(-4,4,-3), raydepth=4)
            sage: t.light((4.4,-4.4,4.4), 0.2, (1,1,1))
            sage: def f(x, y): return float(sin(x*y))
            sage: def g(x, y): return (float(y*cos(x*y)), float(x*cos(x*y)), 1)
            sage: t.texture(\'t0\', ambient=0.1, diffuse=0.9, specular=0.1,
            ....:           opacity=1.0, color=(1.0,0,0))
            sage: t.plot(f, (-4,4), (-4,4), "t0", max_depth=5, initial_depth=3,         # needs sage.symbolic
            ....:        grad_f=g)  # increase min_depth for better picture
            sage: t.show(verbose=1)                                                     # needs sage.symbolic
            tachyon ...
            Scene contains 2713 objects.
            ...

        Preconditions: f is a scalar function of two variables, grad_f is
        None or a triple-valued function of two variables, min_x !=
        max_x, min_y != max_y

        ::

            sage: f = lambda x,y: x*y
            sage: t = Tachyon()
            sage: t.plot(f,(2.,2.),(-2.,2.),\'\')
            Traceback (most recent call last):
            ...
            ValueError: plot rectangle is really a line; make sure min_x != max_x and min_y != max_y
        '''
    def parametric_plot(self, f, t_0, t_f, tex, r: float = 0.1, cylinders: bool = True, min_depth: int = 4, max_depth: int = 8, e_rel: float = 0.01, e_abs: float = 0.01) -> None:
        """
        Plot a space curve as a series of spheres and finite cylinders.

        Example (twisted cubic) ::

            sage: f = lambda t: (t,t^2,t^3)
            sage: t = Tachyon(camera_position=(5,0,4))
            sage: t.texture('t')
            sage: t.light((-20,-20,40), 0.2, (1,1,1))
            sage: t.parametric_plot(f,-5,5,'t',min_depth=6)
            sage: t.show(verbose=1)
            tachyon ...
            Scene contains 482 objects.
            ...
        """

class Light:
    """
    Represent lighting objects.

    EXAMPLES::

        sage: from sage.plot.plot3d.tachyon import Light
        sage: q = Light((1,1,1), 1, (1,1,1))
        sage: q._center
        (1.0, 1.0, 1.0)
    """
    def __init__(self, center, radius, color) -> None:
        """
        Store the center, radius and color.

        EXAMPLES::

            sage: from sage.plot.plot3d.tachyon import Light
            sage: q = Light((1,1,1), 1, (1,1,1))
            sage: print(q._center, q._color, q._radius)
            (1.0, 1.0, 1.0) (1.0, 1.0, 1.0) 1.0
        """
    def str(self):
        """
        Return the tachyon string defining the light source.

        EXAMPLES::

            sage: from sage.plot.plot3d.tachyon import Light
            sage: q = Light((1,1,1), 1, (1,1,1))
            sage: print(q.str())
                    light center  1.0 1.0 1.0
                          rad 1.0
                          color  1.0 1.0 1.0
        """

class Texfunc:
    def __init__(self, ttype: int = 0, center=(0, 0, 0), rotate=(0, 0, 0), scale=(1, 1, 1), imagefile: str = '') -> None:
        """
        Create a texture function.

        EXAMPLES::

            sage: from sage.plot.plot3d.tachyon import Texfunc
            sage: t = Texfunc()
            sage: t._ttype
            0
        """
    def str(self):
        """
        Return the scene string for this texture function.

        EXAMPLES::

            sage: from sage.plot.plot3d.tachyon import Texfunc
            sage: t = Texfunc()
            sage: t.str()
            '0'
        """

class Texture:
    def __init__(self, name, ambient: float = 0.2, diffuse: float = 0.8, specular: float = 0.0, opacity: float = 1.0, color=(1.0, 0.0, 0.5), texfunc: int = 0, phong: int = 0, phongsize: int = 0, phongtype: str = 'PLASTIC', imagefile: str = '') -> None:
        """
        Store texture information.

        EXAMPLES::

            sage: from sage.plot.plot3d.tachyon import Texture
            sage: t = Texture('w')
            sage: t.str().split()[2:6]
            ['ambient', '0.2', 'diffuse', '0.8']
        """
    def recolor(self, name, color):
        """
        Return a texture with the new given color.

        EXAMPLES::

            sage: from sage.plot.plot3d.tachyon import Texture
            sage: t2 = Texture('w')
            sage: t2w = t2.recolor('w2', (.1,.2,.3))
            sage: t2ws = t2w.str()
            sage: color_index = t2ws.find('color')
            sage: t2ws[color_index:color_index+20]
            'color  0.1 0.2 0.3  '
        """
    def str(self):
        """
        Return the scene string for this texture.

        EXAMPLES::

            sage: from sage.plot.plot3d.tachyon import Texture
            sage: t = Texture('w')
            sage: t.str().split()[2:6]
            ['ambient', '0.2', 'diffuse', '0.8']
        """

class Sphere:
    """
    A class for creating spheres in tachyon.
    """
    def __init__(self, center, radius, texture) -> None:
        """
        Store the center, radius, and texture information in a class.

        EXAMPLES::

            sage: t = Tachyon()
            sage: from sage.plot.plot3d.tachyon import Sphere
            sage: t.texture('r', color=(.8,0,0), ambient=.1)
            sage: s = Sphere((1,1,1), 1, 'r')
            sage: s._radius
            1.0
        """
    def str(self):
        """
        Return the scene string for the sphere.

        EXAMPLES::

            sage: t = Tachyon()
            sage: from sage.plot.plot3d.tachyon import Sphere
            sage: t.texture('r', color=(.8,0,0), ambient = .1)
            sage: s = Sphere((1,1,1), 1, 'r')
            sage: s.str()
            '\\n        sphere center  1.0 1.0 1.0  rad 1.0 r\\n        '
        """

class Ring:
    """
    An annulus of zero thickness.
    """
    def __init__(self, center, normal, inner, outer, texture) -> None:
        """
        Create a ring with the given center, normal, inner radius,
        outer radius, and texture.

        EXAMPLES::

            sage: from sage.plot.plot3d.tachyon import Ring
            sage: r = Ring((1,1,1), (1,1,0), 1.0, 2.0, 's')
            sage: r._center
            (1.0, 1.0, 1.0)
        """
    def str(self):
        """
        Return the scene string of the ring.

        EXAMPLES::

            sage: from sage.plot.plot3d.tachyon import Ring
            sage: r = Ring((0,0,0), (1,1,0), 1.0, 2.0, 's')
            sage: r.str()
            '\\n        ring center  0.0 0.0 0.0  normal  1.0 1.0 0.0  inner 1.0 outer 2.0 s\\n        '
        """

class FractalLandscape:
    """
    Axis-aligned fractal landscape.

    Does not seem very useful at the moment, but perhaps will be improved in the future.
    """
    def __init__(self, res, scale, center, texture) -> None:
        """
        Create a fractal landscape in tachyon.

        EXAMPLES::

            sage: from sage.plot.plot3d.tachyon import FractalLandscape
            sage: fl = FractalLandscape([20,20],[30,30],[1,2,3],'s')
            sage: fl._center
            (1.0, 2.0, 3.0)
        """
    def str(self):
        """
        Return the scene string of the fractal landscape.

        EXAMPLES::

            sage: from sage.plot.plot3d.tachyon import FractalLandscape
            sage: fl = FractalLandscape([20,20],[30,30],[1,2,3],'s')
            sage: fl.str()
            '\\n        scape res  20 20  scale  30 30  center  1.0 2.0 3.0  s\\n        '
        """

class Cylinder:
    """
    An infinite cylinder.
    """
    def __init__(self, center, axis, radius, texture) -> None:
        """
        Create a cylinder with the given parameters.

        EXAMPLES::

            sage: t = Tachyon()
            sage: from sage.plot.plot3d.tachyon import Cylinder
            sage: c = Cylinder((0,0,0),(1,1,1),.1,'s')
            sage: c.str()
            '\\n        cylinder center  0.0 0.0 0.0  axis  1.0 1.0 1.0  rad 0.1 s\\n        '
        """
    def str(self):
        """
        Return the scene string of the cylinder.

        EXAMPLES::

            sage: t = Tachyon()
            sage: from sage.plot.plot3d.tachyon import Cylinder
            sage: c = Cylinder((0,0,0),(1,1,1),.1,'s')
            sage: c.str()
            '\\n        cylinder center  0.0 0.0 0.0  axis  1.0 1.0 1.0  rad 0.1 s\\n        '
        """

class Plane:
    """
    An infinite plane.
    """
    def __init__(self, center, normal, texture) -> None:
        """
        Create the plane object.

        EXAMPLES::

            sage: from sage.plot.plot3d.tachyon import Plane
            sage: p = Plane((1,2,3), (1,2,4), 's')
            sage: p.str()
            '\\n        plane center  1.0 2.0 3.0  normal  1.0 2.0 4.0  s\\n        '
        """
    def str(self):
        """
        Return the scene string of the plane.

        EXAMPLES::

            sage: from sage.plot.plot3d.tachyon import Plane
            sage: p = Plane((1,2,3),(1,2,4),'s')
            sage: p.str()
            '\\n        plane center  1.0 2.0 3.0  normal  1.0 2.0 4.0  s\\n        '
        """

class FCylinder:
    """
    A finite cylinder.
    """
    def __init__(self, base, apex, radius, texture) -> None:
        """
        Create a finite cylinder object.

        EXAMPLES::

            sage: from sage.plot.plot3d.tachyon import FCylinder
            sage: fc = FCylinder((0,0,0),(1,1,1),.1,'s')
            sage: fc.str()
            '\\n        fcylinder base  0.0 0.0 0.0  apex  1.0 1.0 1.0  rad 0.1 s\\n        '
        """
    def str(self):
        """
        Return the scene string of the finite cylinder.

        EXAMPLES::

            sage: from sage.plot.plot3d.tachyon import FCylinder
            sage: fc = FCylinder((0,0,0),(1,1,1),.1,'s')
            sage: fc.str()
            '\\n        fcylinder base  0.0 0.0 0.0  apex  1.0 1.0 1.0  rad 0.1 s\\n        '
        """

class Axis_aligned_box:
    """
    Box with axis-aligned edges with the given min and max coordinates.
    """
    def __init__(self, min_p, max_p, texture) -> None:
        """
        Create the axis-aligned box object.

        EXAMPLES::

            sage: from sage.plot.plot3d.tachyon import Axis_aligned_box
            sage: aab = Axis_aligned_box((0,0,0),(1,1,1),'s')
            sage: aab.str()
            '\\n        box min  0.0 0.0 0.0  max  1.0 1.0 1.0  s\\n        '
        """
    def str(self):
        """
        Return the scene string of the axis-aligned box.

        EXAMPLES::

            sage: from sage.plot.plot3d.tachyon import Axis_aligned_box
            sage: aab = Axis_aligned_box((0,0,0),(1,1,1),'s')
            sage: aab.str()
            '\\n        box min  0.0 0.0 0.0  max  1.0 1.0 1.0  s\\n        '
        """

class TachyonTriangle(Triangle):
    """
    Basic triangle class.
    """
    def str(self):
        """
        Return the scene string for a triangle.

        EXAMPLES::

            sage: from sage.plot.plot3d.tachyon import TachyonTriangle
            sage: t = TachyonTriangle([-1,-1,-1],[0,0,0],[1,2,3])
            sage: t.str()
            '\\n        TRI V0  -1.0 -1.0 -1.0   V1  0.0 0.0 0.0    V2  1.0 2.0 3.0 \\n            0\\n        '
        """

class TachyonSmoothTriangle(SmoothTriangle):
    """
    A triangle along with a normal vector, which is used for smoothing.
    """
    def str(self):
        """
        Return the scene string for a smoothed triangle.

        EXAMPLES::

            sage: from sage.plot.plot3d.tachyon import TachyonSmoothTriangle
            sage: t = TachyonSmoothTriangle([-1,-1,-1],[0,0,0],[1,2,3],[1,0,0],[0,1,0],[0,0,1])
            sage: t.str()
            '\\n        STRI V0  ...  1.0 0.0 0.0  N1  0.0 1.0 0.0   N2  0.0 0.0 1.0 \\n             0\\n        '
        """

class TachyonTriangleFactory(TriangleFactory):
    """
    A class to produce triangles of various rendering types.
    """
    def __init__(self, tach, tex) -> None:
        """
        Initialize with tachyon instance and texture.

        EXAMPLES::

            sage: from sage.plot.plot3d.tachyon import TachyonTriangleFactory
            sage: t = Tachyon()
            sage: t.texture('s')
            sage: ttf = TachyonTriangleFactory(t, 's')
            sage: ttf._texture
            's'
        """
    def triangle(self, a, b, c, color=None):
        """
        Create a TachyonTriangle with vertices a, b, and c.

        EXAMPLES::

            sage: from sage.plot.plot3d.tachyon import TachyonTriangleFactory
            sage: t = Tachyon()
            sage: t.texture('s')
            sage: ttf = TachyonTriangleFactory(t, 's')
            sage: ttft = ttf.triangle([1,2,3],[3,2,1],[0,2,1])
            sage: ttft.str()
            '\\n        TRI V0  1.0 2.0 3.0   V1  3.0 2.0 1.0    V2  0.0 2.0 1.0 \\n            s\\n        '
        """
    def smooth_triangle(self, a, b, c, da, db, dc, color=None):
        """
        Create a TachyonSmoothTriangle.

        EXAMPLES::

            sage: from sage.plot.plot3d.tachyon import TachyonTriangleFactory
            sage: t = Tachyon()
            sage: t.texture('s')
            sage: ttf = TachyonTriangleFactory(t, 's')
            sage: ttfst = ttf.smooth_triangle([0,0,0],[1,0,0],[0,0,1],[1,1,1],[1,2,3],[-1,-1,2])
            sage: ttfst.str()
            '\\n        STRI V0  0.0 0.0 0.0  ...'
        """
    def get_colors(self, list):
        """
        Return a list of color labels.

        EXAMPLES::

            sage: from sage.plot.plot3d.tachyon import TachyonTriangleFactory
            sage: t = Tachyon()
            sage: t.texture('s')
            sage: ttf = TachyonTriangleFactory(t, 's')
            sage: ttf.get_colors([(1,1,1)])
            ['SAGETEX1_0']
        """

class ParametricPlot:
    """
    Parametric plotting routines.
    """
    def str(self):
        """
        Return the tachyon string representation of the parameterized curve.

        EXAMPLES::

            sage: from sage.plot.plot3d.tachyon import ParametricPlot
            sage: f = lambda t: (t,t^2,t^3)
            sage: q = ParametricPlot(f,0,1,'s')
            sage: q.str()[9:69]
            'sphere center  0.0 0.0 0.0  rad 0.1 s\\n        \\n        fcyli'
        """
    def __init__(self, f, t_0, t_f, tex, r: float = 0.1, cylinders: bool = True, min_depth: int = 4, max_depth: int = 8, e_rel: float = 0.01, e_abs: float = 0.01) -> None:
        """
        Create the parametric plotting class.

        EXAMPLES::

            sage: from sage.plot.plot3d.tachyon import ParametricPlot
            sage: f = lambda t: (t,t^2,t^3)
            sage: q = ParametricPlot(f,0,1,'s')
            sage: q._e_rel
            0.01
        """
    def tol(self, est, val):
        """
        Check relative, then absolute tolerance.

        If both fail, return ``False``.

        This is a zero-safe error checker.

        EXAMPLES::

            sage: from sage.plot.plot3d.tachyon import ParametricPlot
            sage: f = lambda t: (t,t^2,t^3)
            sage: q = ParametricPlot(f,0,1,'s')
            sage: q.tol([0,0,0],[1,0,0])
            False
            sage: q.tol([0,0,0],[.0001,0,0])
            True
        """

def tostr(s, length: int = 3, out_type=...):
    """
    Convert vector information to a space-separated string.

    EXAMPLES::

        sage: from sage.plot.plot3d.tachyon import tostr
        sage: tostr((1,1,1))
        ' 1.0 1.0 1.0 '
        sage: tostr('2 3 2')
        '2 3 2'
    """
