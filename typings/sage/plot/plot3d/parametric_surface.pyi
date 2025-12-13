import sage.plot.plot3d.index_face_set
from sage.categories.category import RDF as RDF
from sage.plot.colors import check_color_data as check_color_data
from sage.plot.plot3d.base import RenderParams as RenderParams
from typing import Any, ClassVar, overload

class MoebiusStrip(ParametricSurface):
    """File: /build/sagemath/src/sage/src/sage/plot/plot3d/parametric_surface.pyx (starting at line 790)

        Base class for the :class:`MoebiusStrip` graphics type. This sets the
        basic parameters of the object.

        INPUT:

        - ``r`` -- a number which can be coerced to a float, serving roughly
          as the radius of the object

        - ``width`` -- a number which can be coerced to a float, which gives the
          width of the object

        - ``twists`` -- (default: 1) an integer, giving the number of twists in the
          object (where one twist is the 'traditional' Möbius strip)

        EXAMPLES::

            sage: from sage.plot.plot3d.parametric_surface import MoebiusStrip
            sage: M = MoebiusStrip(3,3)
            sage: M.show()

        .. PLOT::

            from sage.plot.plot3d.parametric_surface import MoebiusStrip
            sphinx_plot(MoebiusStrip(3,3))
    """
    def __init__(self, r, width, twists=..., **kwds) -> Any:
        """MoebiusStrip.__init__(self, r, width, twists=1, **kwds)

        File: /build/sagemath/src/sage/src/sage/plot/plot3d/parametric_surface.pyx (starting at line 818)

        Create the graphics primitive MoebiusStrip. See the docstring of
        this class for full documentation.

        EXAMPLES:

        ::

            sage: from sage.plot.plot3d.parametric_surface import MoebiusStrip
            sage: M = MoebiusStrip(3,3); M # Same width and radius, roughly
            Graphics3d Object
            sage: N = MoebiusStrip(7,3,2); N # two twists, lots of open area in the middle
            Graphics3d Object
            sage: O = MoebiusStrip(5,1,plot_points=200,color='red'); O # keywords get passed to plot3d
            Graphics3d Object"""
    def eval(self, u, v) -> Any:
        """MoebiusStrip.eval(self, u, v)

        File: /build/sagemath/src/sage/src/sage/plot/plot3d/parametric_surface.pyx (starting at line 866)

        Return a tuple for `x,y,z` coordinates for the given ``u`` and ``v``
        for this MoebiusStrip instance.

        EXAMPLES::

            sage: from sage.plot.plot3d.parametric_surface import MoebiusStrip
            sage: N = MoebiusStrip(7,3,2) # two twists
            sage: N.eval(-1,0)
            (4.0, 0.0, -0.0)"""
    def get_grid(self, ds) -> Any:
        """MoebiusStrip.get_grid(self, ds)

        File: /build/sagemath/src/sage/src/sage/plot/plot3d/parametric_surface.pyx (starting at line 840)

        Return appropriate `u` and `v` ranges for this MoebiusStrip instance.

        This is intended for internal use in creating an actual plot.

        INPUT:

        - ``ds`` -- a number, typically coming from a RenderParams object,
          which helps determine the increment for the `v` range for the
          MoebiusStrip object

        EXAMPLES::

            sage: from sage.plot.plot3d.parametric_surface import MoebiusStrip
            sage: N = MoebiusStrip(7,3,2) # two twists
            sage: N.get_grid(N.default_render_params().ds)
            ([-1, 1], [0.0, 0.12566370614359174, 0.25132741228718347, 0.37699111843077515, ...])"""

class ParametricSurface(sage.plot.plot3d.index_face_set.IndexFaceSet):
    """ParametricSurface(f=None, domain=None, **kwds)

    File: /build/sagemath/src/sage/src/sage/plot/plot3d/parametric_surface.pyx (starting at line 140)

    Base class that initializes the ParametricSurface
    graphics type. This sets options, the function to be plotted, and the
    plotting array as attributes.

    INPUT:

    - ``f`` -- (default: ``None``) the defining function. Either a tuple of
      three functions, or a single function which returns a tuple, taking
      two python floats as input. To subclass, pass ``None`` for ``f`` and
      override ``eval_c`` or ``eval`` instead.

    - ``domain`` -- (default: ``None``) a tuple of two lists, defining the
      grid of `u,v` values. If ``None``, this will be calculated automatically.

    - ``color`` -- (default: ``None``) a pair `(h,c)` where `h` is
      a function with values in `[0,1]` and `c` is a colormap. The
      color of a point `p` is then defined as the composition
      `c(h(p))`

    EXAMPLES::

        sage: from sage.plot.plot3d.parametric_surface import ParametricSurface
        sage: def f(x, y): return cos(x)*sin(y), sin(x)*sin(y), cos(y)+log(tan(y/2))+0.2*x
        sage: S = ParametricSurface(f, (srange(0,12.4,0.1), srange(0.1,2,0.1)))
        sage: show(S)

        sage: len(S.face_list())
        2214

    .. PLOT::

        from sage.plot.plot3d.parametric_surface import ParametricSurface
        def f(x, y): return cos(x)*sin(y), sin(x)*sin(y), cos(y)+log(tan(y/2))+0.2*x
        sphinx_plot(ParametricSurface(f, (srange(0,12.4,0.1), srange(0.1,2,0.1))))

    The Hessenberg surface:

    ::

        sage: def f(u, v):
        ....:     a = 1
        ....:     from math import cos, sin, sinh, cosh
        ....:     x = cos(a)*(cos(u)*sinh(v)-cos(3*u)*sinh(3*v)/3) + sin(a)*(
        ....:         sin(u)*cosh(v)-sin(3*u)*cosh(3*v)/3)
        ....:     y = cos(a)*(sin(u)*sinh(v)+sin(3*u)*sinh(3*v)/3) + sin(a)*(
        ....:         -cos(u)*cosh(v)-cos(3*u)*cosh(3*v)/3)
        ....:     z = cos(a)*cos(2*u)*cosh(2*v)+sin(a)*sin(2*u)*sinh(2*v)
        ....:     return (x,y,z)
        sage: v = srange(float(0),float((3/2)*pi),float(0.1))
        sage: S = ParametricSurface(f, (srange(float(0),float(pi),float(0.1)),
        ....:                srange(float(-1),float(1),float(0.1))), color='blue')
        sage: show(S)

    .. PLOT::

        def f(u, v):
            a = 1
            from math import cos, sin, sinh, cosh
            x = cos(a)*(cos(u)*sinh(v)-cos(3*u)*sinh(3*v)/3) + sin(a)*(sin(u)*cosh(v)-sin(3*u)*cosh(3*v)/3)
            y = cos(a)*(sin(u)*sinh(v)+sin(3*u)*sinh(3*v)/3) + sin(a)*(-cos(u)*cosh(v)-cos(3*u)*cosh(3*v)/3)
            z = cos(a)*cos(2*u)*cosh(2*v)+sin(a)*sin(2*u)*sinh(2*v)
            return (x,y,z)
        from sage.plot.plot3d.parametric_surface import ParametricSurface
        v = srange(float(0),float((3/2)*pi),float(0.1))
        sphinx_plot(ParametricSurface(f, (srange(float(0),float(pi),float(0.1)),srange(float(-1),float(1),float(0.1))), color='blue'))

    A colored example using the ``color`` keyword::

        sage: def g(x, y): return x, y, - x**2 + y**2
        sage: def c(x, y): return sin((x-y/2)*y/4)**2
        sage: cm = colormaps.gist_rainbow
        sage: P = ParametricSurface(g, (srange(-10,10,0.1),
        ....:   srange(-5,5.0,0.1)),color=(c,cm))
        sage: P.show(viewer='tachyon')

    .. PLOT::

        from sage.plot.plot3d.parametric_surface import ParametricSurface
        def g(x, y): return x, y, - x**2 + y**2
        def c(x, y): return sin((x-y/2)*y/4)**2
        cm = colormaps.gist_rainbow
        sphinx_plot(ParametricSurface(g, (srange(-10,10,0.1), srange(-5,5.0,0.1)),color=(c,cm)))"""
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    def __init__(self, f=..., domain=..., **kwds) -> Any:
        """File: /build/sagemath/src/sage/src/sage/plot/plot3d/parametric_surface.pyx (starting at line 226)

                Create the graphics primitive :class:`ParametricSurface`.  See the
                docstring of this class for full documentation.

                EXAMPLES::

                    sage: from sage.plot.plot3d.parametric_surface import ParametricSurface
                    sage: def f(x, y): return x+y, sin(x)*sin(y), x*y
                    sage: S = ParametricSurface(f, (srange(0,12.4,0.1), srange(0.1,2,0.1)))
        """
    @overload
    def bounding_box(self) -> Any:
        """ParametricSurface.bounding_box(self)

        File: /build/sagemath/src/sage/src/sage/plot/plot3d/parametric_surface.pyx (starting at line 453)

        Return the lower and upper corners of a 3D bounding box for ``self``.

        This is used for rendering and ``self`` should fit entirely within this
        box.

        Specifically, the first point returned should have x, y, and z
        coordinates should be the respective infimum over all points in
        ``self``, and the second point is the supremum.

        EXAMPLES::

            sage: from sage.plot.plot3d.parametric_surface import MoebiusStrip
            sage: M = MoebiusStrip(7,3,2)
            sage: M.bounding_box()
            ((-10.0, -7.53907349250478..., -2.9940801852848145),
             (10.0, 7.53907349250478..., 2.9940801852848145))"""
    @overload
    def bounding_box(self) -> Any:
        """ParametricSurface.bounding_box(self)

        File: /build/sagemath/src/sage/src/sage/plot/plot3d/parametric_surface.pyx (starting at line 453)

        Return the lower and upper corners of a 3D bounding box for ``self``.

        This is used for rendering and ``self`` should fit entirely within this
        box.

        Specifically, the first point returned should have x, y, and z
        coordinates should be the respective infimum over all points in
        ``self``, and the second point is the supremum.

        EXAMPLES::

            sage: from sage.plot.plot3d.parametric_surface import MoebiusStrip
            sage: M = MoebiusStrip(7,3,2)
            sage: M.bounding_box()
            ((-10.0, -7.53907349250478..., -2.9940801852848145),
             (10.0, 7.53907349250478..., 2.9940801852848145))"""
    @overload
    def default_render_params(self) -> Any:
        """ParametricSurface.default_render_params(self)

        File: /build/sagemath/src/sage/src/sage/plot/plot3d/parametric_surface.pyx (starting at line 261)

        Return an instance of RenderParams suitable for plotting this object.

        TESTS::

            sage: from sage.plot.plot3d.parametric_surface import MoebiusStrip
            sage: type(MoebiusStrip(3,3).default_render_params())
            <class 'sage.plot.plot3d.base.RenderParams'>"""
    @overload
    def default_render_params(self) -> Any:
        """ParametricSurface.default_render_params(self)

        File: /build/sagemath/src/sage/src/sage/plot/plot3d/parametric_surface.pyx (starting at line 261)

        Return an instance of RenderParams suitable for plotting this object.

        TESTS::

            sage: from sage.plot.plot3d.parametric_surface import MoebiusStrip
            sage: type(MoebiusStrip(3,3).default_render_params())
            <class 'sage.plot.plot3d.base.RenderParams'>"""
    @overload
    def dual(self) -> Any:
        """ParametricSurface.dual(self)

        File: /build/sagemath/src/sage/src/sage/plot/plot3d/parametric_surface.pyx (starting at line 413)

        Return an ``IndexFaceSet`` which is the dual of the
        :class:`ParametricSurface` object as a triangulated surface.

        EXAMPLES:

        As one might expect, this gives an icosahedron::

            sage: D = dodecahedron()
            sage: D.dual()
            Graphics3d Object

        But any enclosed surface should work::

            sage: from sage.plot.plot3d.shapes import Torus
            sage: T =  Torus(1, .2)
            sage: T.dual()
            Graphics3d Object
            sage: T.is_enclosed()
            True

        Surfaces which are not enclosed, though, should raise an exception::

            sage: from sage.plot.plot3d.parametric_surface import MoebiusStrip
            sage: M = MoebiusStrip(3,1)
            sage: M.is_enclosed()
            False
            sage: M.dual()
            Traceback (most recent call last):
            ...
            NotImplementedError: this is only implemented for enclosed surfaces"""
    @overload
    def dual(self) -> Any:
        """ParametricSurface.dual(self)

        File: /build/sagemath/src/sage/src/sage/plot/plot3d/parametric_surface.pyx (starting at line 413)

        Return an ``IndexFaceSet`` which is the dual of the
        :class:`ParametricSurface` object as a triangulated surface.

        EXAMPLES:

        As one might expect, this gives an icosahedron::

            sage: D = dodecahedron()
            sage: D.dual()
            Graphics3d Object

        But any enclosed surface should work::

            sage: from sage.plot.plot3d.shapes import Torus
            sage: T =  Torus(1, .2)
            sage: T.dual()
            Graphics3d Object
            sage: T.is_enclosed()
            True

        Surfaces which are not enclosed, though, should raise an exception::

            sage: from sage.plot.plot3d.parametric_surface import MoebiusStrip
            sage: M = MoebiusStrip(3,1)
            sage: M.is_enclosed()
            False
            sage: M.dual()
            Traceback (most recent call last):
            ...
            NotImplementedError: this is only implemented for enclosed surfaces"""
    @overload
    def dual(self) -> Any:
        """ParametricSurface.dual(self)

        File: /build/sagemath/src/sage/src/sage/plot/plot3d/parametric_surface.pyx (starting at line 413)

        Return an ``IndexFaceSet`` which is the dual of the
        :class:`ParametricSurface` object as a triangulated surface.

        EXAMPLES:

        As one might expect, this gives an icosahedron::

            sage: D = dodecahedron()
            sage: D.dual()
            Graphics3d Object

        But any enclosed surface should work::

            sage: from sage.plot.plot3d.shapes import Torus
            sage: T =  Torus(1, .2)
            sage: T.dual()
            Graphics3d Object
            sage: T.is_enclosed()
            True

        Surfaces which are not enclosed, though, should raise an exception::

            sage: from sage.plot.plot3d.parametric_surface import MoebiusStrip
            sage: M = MoebiusStrip(3,1)
            sage: M.is_enclosed()
            False
            sage: M.dual()
            Traceback (most recent call last):
            ...
            NotImplementedError: this is only implemented for enclosed surfaces"""
    @overload
    def dual(self) -> Any:
        """ParametricSurface.dual(self)

        File: /build/sagemath/src/sage/src/sage/plot/plot3d/parametric_surface.pyx (starting at line 413)

        Return an ``IndexFaceSet`` which is the dual of the
        :class:`ParametricSurface` object as a triangulated surface.

        EXAMPLES:

        As one might expect, this gives an icosahedron::

            sage: D = dodecahedron()
            sage: D.dual()
            Graphics3d Object

        But any enclosed surface should work::

            sage: from sage.plot.plot3d.shapes import Torus
            sage: T =  Torus(1, .2)
            sage: T.dual()
            Graphics3d Object
            sage: T.is_enclosed()
            True

        Surfaces which are not enclosed, though, should raise an exception::

            sage: from sage.plot.plot3d.parametric_surface import MoebiusStrip
            sage: M = MoebiusStrip(3,1)
            sage: M.is_enclosed()
            False
            sage: M.dual()
            Traceback (most recent call last):
            ...
            NotImplementedError: this is only implemented for enclosed surfaces"""
    def eval(self, doubleu, doublev) -> Any:
        """ParametricSurface.eval(self, double u, double v)

        File: /build/sagemath/src/sage/src/sage/plot/plot3d/parametric_surface.pyx (starting at line 761)

        TESTS::

            sage: from sage.plot.plot3d.parametric_surface import ParametricSurface
            sage: def f(x, y): return x+y,x-y,x*y
            sage: P = ParametricSurface(f,(srange(0,1,0.1),srange(0,1,0.1)))
            sage: P.eval(0,0)
            Traceback (most recent call last):
            ...
            NotImplementedError"""
    def get_grid(self, ds) -> Any:
        """ParametricSurface.get_grid(self, ds)

        File: /build/sagemath/src/sage/src/sage/plot/plot3d/parametric_surface.pyx (starting at line 636)

        TESTS::

            sage: from sage.plot.plot3d.parametric_surface import ParametricSurface
            sage: def f(x, y): return x+y,x-y,x*y
            sage: P = ParametricSurface(f)
            sage: P.get_grid(.1)
            Traceback (most recent call last):
            ...
            NotImplementedError: you must override the get_grid method"""
    @overload
    def is_enclosed(self) -> Any:
        """ParametricSurface.is_enclosed(self)

        File: /build/sagemath/src/sage/src/sage/plot/plot3d/parametric_surface.pyx (starting at line 390)

        Return a boolean telling whether or not it is necessary to
        render the back sides of the polygons (assuming, of course,
        that they have the correct orientation).

        This is calculated in by verifying the opposite edges
        of the rendered domain either line up or are pinched together.

        EXAMPLES::

            sage: from sage.plot.plot3d.shapes import Sphere
            sage: Sphere(1).is_enclosed()
            True

            sage: from sage.plot.plot3d.parametric_surface import MoebiusStrip
            sage: MoebiusStrip(1,0.2).is_enclosed()
            False"""
    @overload
    def is_enclosed(self) -> Any:
        """ParametricSurface.is_enclosed(self)

        File: /build/sagemath/src/sage/src/sage/plot/plot3d/parametric_surface.pyx (starting at line 390)

        Return a boolean telling whether or not it is necessary to
        render the back sides of the polygons (assuming, of course,
        that they have the correct orientation).

        This is calculated in by verifying the opposite edges
        of the rendered domain either line up or are pinched together.

        EXAMPLES::

            sage: from sage.plot.plot3d.shapes import Sphere
            sage: Sphere(1).is_enclosed()
            True

            sage: from sage.plot.plot3d.parametric_surface import MoebiusStrip
            sage: MoebiusStrip(1,0.2).is_enclosed()
            False"""
    @overload
    def is_enclosed(self) -> Any:
        """ParametricSurface.is_enclosed(self)

        File: /build/sagemath/src/sage/src/sage/plot/plot3d/parametric_surface.pyx (starting at line 390)

        Return a boolean telling whether or not it is necessary to
        render the back sides of the polygons (assuming, of course,
        that they have the correct orientation).

        This is calculated in by verifying the opposite edges
        of the rendered domain either line up or are pinched together.

        EXAMPLES::

            sage: from sage.plot.plot3d.shapes import Sphere
            sage: Sphere(1).is_enclosed()
            True

            sage: from sage.plot.plot3d.parametric_surface import MoebiusStrip
            sage: MoebiusStrip(1,0.2).is_enclosed()
            False"""
    def jmol_repr(self, render_params) -> Any:
        '''ParametricSurface.jmol_repr(self, render_params)

        File: /build/sagemath/src/sage/src/sage/plot/plot3d/parametric_surface.pyx (starting at line 329)

        Return a representation of the object suitable for plotting
        using Jmol.

        TESTS::

            sage: _ = var(\'x,y\')
            sage: P = plot3d(x^2-y^2, (x, -2, 2), (y, -2, 2))
            sage: s = P.jmol_repr(P.testing_render_params())
            sage: s[:10]
            [\'pmesh obj_1 "obj_1.pmesh"\\ncolor pmesh  [102,102,255]\']'''
    def json_repr(self, render_params) -> Any:
        '''ParametricSurface.json_repr(self, render_params)

        File: /build/sagemath/src/sage/src/sage/plot/plot3d/parametric_surface.pyx (starting at line 345)

        Return a representation of the object in JSON format as
        a list with one element, which is a string of a dictionary
        listing vertices, faces and colors.

        TESTS::

            sage: _ = var(\'x,y\')
            sage: P = plot3d(x^2-y^2, (x, -2, 2), (y, -2, 2))
            sage: s = P.json_repr(P.default_render_params())
            sage: print(s[0][:100])
            {"vertices":[{"x":-2,"y":-2,"z":0},{"x":-2,"y":-1.89744,"z":0.399737},{"x":-1.89744,"y":-1.89744,"z"

        One test for :issue:`22688`::

            sage: P = spherical_plot3d(sqrt(x-pi/2),(x,0,pi),(y,0,2*pi))
            sage: s = P.json_repr(P.default_render_params())
            sage: \'nan\' in s or \'NaN\' in s
            False'''
    def obj_repr(self, render_params) -> Any:
        """ParametricSurface.obj_repr(self, render_params)

        File: /build/sagemath/src/sage/src/sage/plot/plot3d/parametric_surface.pyx (starting at line 306)

        Return a complete representation of object with name, texture, and
        lists of vertices, faces, and back-faces.

        TESTS::

            sage: _ = var('x,y')
            sage: P = plot3d(x^2-y^2, (x, -2, 2), (y, -2, 2))
            sage: s = P.obj_repr(P.default_render_params())
            sage: s[:2]+s[2][:3]+s[3][:3]
            ['g obj_1',
             'usemtl texture...',
             'v -2 -2 0',
             'v -2 -1.89744 0.399737',
             'v -1.89744 -1.89744 0',
             'f 1 2 3 4',
             'f 2 5 6 3',
             'f 5 7 8 6']"""
    @overload
    def plot(self) -> Any:
        """ParametricSurface.plot(self)

        File: /build/sagemath/src/sage/src/sage/plot/plot3d/parametric_surface.pyx (starting at line 775)

        Draw a 3D plot of this graphics object, which just returns this
        object since this is already a 3D graphics object.
        Needed to support PLOT in doctrings, see :issue:`17498`

        EXAMPLES::

            sage: S = parametric_plot3d( (sin, cos, lambda u: u/10), (0, 20))
            sage: S.plot() is S
            True"""
    @overload
    def plot(self) -> Any:
        """ParametricSurface.plot(self)

        File: /build/sagemath/src/sage/src/sage/plot/plot3d/parametric_surface.pyx (starting at line 775)

        Draw a 3D plot of this graphics object, which just returns this
        object since this is already a 3D graphics object.
        Needed to support PLOT in doctrings, see :issue:`17498`

        EXAMPLES::

            sage: S = parametric_plot3d( (sin, cos, lambda u: u/10), (0, 20))
            sage: S.plot() is S
            True"""
    def tachyon_repr(self, render_params) -> Any:
        """ParametricSurface.tachyon_repr(self, render_params)

        File: /build/sagemath/src/sage/src/sage/plot/plot3d/parametric_surface.pyx (starting at line 290)

        Return representation of the object suitable for plotting
        using Tachyon ray tracer.

        TESTS::

            sage: _ = var('x,y')
            sage: P = plot3d(x^2-y^2, (x, -2, 2), (y, -2, 2))
            sage: s = P.tachyon_repr(P.default_render_params())
            sage: s[:2]
            ['TRI V0 -2 -2 0 V1 -2 -1.89744 0.399737 V2 -1.89744 -1.89744 0', 'texture...']"""
    def threejs_repr(self, render_params) -> Any:
        """ParametricSurface.threejs_repr(self, render_params)

        File: /build/sagemath/src/sage/src/sage/plot/plot3d/parametric_surface.pyx (starting at line 369)

        Return a representation of the surface suitable for plotting with three.js.

        EXAMPLES::

            sage: _ = var('x,y')
            sage: P = plot3d(x^2-y^2, (x, -2, 2), (y, -2, 2))
            sage: P.threejs_repr(P.default_render_params())
            [('surface',
              {'color': '#6666ff',
               'faces': [[0, 1, 2, 3],
                ...
               'opacity': 1.0,
               'vertices': [{'x': -2.0, 'y': -2.0, 'z': 0.0},
                ...
                {'x': 2.0, 'y': 2.0, 'z': 0.0}]})]"""
    def triangulate(self, render_params=...) -> Any:
        """ParametricSurface.triangulate(self, render_params=None)

        File: /build/sagemath/src/sage/src/sage/plot/plot3d/parametric_surface.pyx (starting at line 479)

        Call self.eval_grid() for all `(u,v)` in
        `\\text{urange} \\times \\text{vrange}` to construct this surface.

        The most complicated part of this code is identifying shared
        vertices and shrinking trivial edges. This is not done so much
        to save memory, rather it is needed so normals of the triangles
        can be calculated correctly.

        TESTS::

            sage: from sage.plot.plot3d.parametric_surface import ParametricSurface, MoebiusStrip
            sage: def f(x, y): return x+y, sin(x)*sin(y), x*y                        # indirect doctests
            sage: P = ParametricSurface(f, (srange(0,10,0.1), srange(-5,5.0,0.1)))  # indirect doctests
            sage: P.show()                                                          # indirect doctests
            sage: S = MoebiusStrip(1, .2)                                           # indirect doctests
            sage: S.show()                                                          # indirect doctests"""
    def x3d_geometry(self) -> Any:
        '''ParametricSurface.x3d_geometry(self)

        File: /build/sagemath/src/sage/src/sage/plot/plot3d/parametric_surface.pyx (starting at line 273)

        Return XML-like representation of the coordinates of all points
        in a triangulation of the object along with an indexing of those
        points.

        TESTS::

            sage: _ = var(\'x,y\')
            sage: P = plot3d(x^2-y^2, (x, -2, 2), (y, -2, 2))
            sage: s = P.x3d_str()    # indirect doctest
            sage: s[:100]
            "<Shape>\\n<IndexedFaceSet coordIndex=\'0,1,..."'''
