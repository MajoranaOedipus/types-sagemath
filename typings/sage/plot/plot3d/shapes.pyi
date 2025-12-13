import _cython_3_2_1
import sage.plot.plot3d.base
import sage.plot.plot3d.index_face_set
import sage.plot.plot3d.parametric_surface
from sage.categories.category import RDF as RDF
from sage.misc.decorators import rename_keyword as rename_keyword
from sage.modules.free_module_element import vector as vector
from sage.plot.plot3d.base import Graphics3dGroup as Graphics3dGroup
from typing import Any, Callable, ClassVar, overload

ColorCube: Callable
LineSegment: Callable
arrow3d: _cython_3_2_1.cython_function_or_method
validate_frame_size: _cython_3_2_1.cython_function_or_method

class Box(sage.plot.plot3d.index_face_set.IndexFaceSet):
    """File: /build/sagemath/src/sage/src/sage/plot/plot3d/shapes.pyx (starting at line 101)

        Return a box.

        EXAMPLES::

            sage: from sage.plot.plot3d.shapes import Box

        A square black box::

            sage: show(Box([1,1,1]), color='black')

        .. PLOT::

            from sage.plot.plot3d.shapes import Box
            sphinx_plot(Box([1,1,1], color='black'))

        A red rectangular box::

            sage: show(Box([2,3,4], color='red'))

        .. PLOT::

            from sage.plot.plot3d.shapes import Box
            sphinx_plot(Box([2,3,4], color='red'))

        A stack of boxes::

            sage: show(sum(Box([2,3,1], color='red').translate((0,0,6*i))
            ....:          for i in [0..3]))

        .. PLOT::

            from sage.plot.plot3d.shapes import Box
            P = sum([Box([2,3,1], color='red').translate((0,0,6*i)) for i in range(0,4)])
            sphinx_plot(P)

        A sinusoidal stack of multicolored boxes::

            sage: B = sum(Box([2,4,1/4],                                                    # needs sage.symbolic
            ....:             color=(i/4,i/5,1)).translate((sin(i),0,5-i))
            ....:         for i in [0..20])
            sage: show(B, figsize=6)                                                        # needs sage.symbolic

        .. PLOT::

            from sage.plot.plot3d.shapes import Box
            B = sum([Box([2,4,1/4], color=(i/4.0,i/5.0,1)).translate((sin(i),0,5-i)) for i in range(0,21)])
            sphinx_plot(B)
    """
    def __init__(self, *size, **kwds) -> Any:
        """Box.__init__(self, *size, **kwds)

        File: /build/sagemath/src/sage/src/sage/plot/plot3d/shapes.pyx (starting at line 151)

        EXAMPLES::

            sage: from sage.plot.plot3d.shapes import Box
            sage: Box(10, 1, 1) + Box(1, 10, 1) + Box(1, 1, 10)
            Graphics3d Object"""
    @overload
    def bounding_box(self) -> Any:
        """Box.bounding_box(self)

        File: /build/sagemath/src/sage/src/sage/plot/plot3d/shapes.pyx (starting at line 169)

        EXAMPLES::

            sage: from sage.plot.plot3d.shapes import Box
            sage: Box([1,2,3]).bounding_box()
            ((-1.0, -2.0, -3.0), (1.0, 2.0, 3.0))"""
    @overload
    def bounding_box(self) -> Any:
        """Box.bounding_box(self)

        File: /build/sagemath/src/sage/src/sage/plot/plot3d/shapes.pyx (starting at line 169)

        EXAMPLES::

            sage: from sage.plot.plot3d.shapes import Box
            sage: Box([1,2,3]).bounding_box()
            ((-1.0, -2.0, -3.0), (1.0, 2.0, 3.0))"""
    @overload
    def x3d_geometry(self) -> Any:
        '''Box.x3d_geometry(self)

        File: /build/sagemath/src/sage/src/sage/plot/plot3d/shapes.pyx (starting at line 179)

        EXAMPLES::

            sage: from sage.plot.plot3d.shapes import Box
            sage: Box([1,2,1/4]).x3d_geometry()
            "<Box size=\'1.0 2.0 0.25\'/>"'''
    @overload
    def x3d_geometry(self) -> Any:
        '''Box.x3d_geometry(self)

        File: /build/sagemath/src/sage/src/sage/plot/plot3d/shapes.pyx (starting at line 179)

        EXAMPLES::

            sage: from sage.plot.plot3d.shapes import Box
            sage: Box([1,2,1/4]).x3d_geometry()
            "<Box size=\'1.0 2.0 0.25\'/>"'''

class Cone(sage.plot.plot3d.parametric_surface.ParametricSurface):
    """Cone(radius, height, closed=True, **kwds)

    File: /build/sagemath/src/sage/src/sage/plot/plot3d/shapes.pyx (starting at line 251)

    A cone, with base in the xy-plane pointing up the z-axis.

    INPUT:

    - ``radius`` -- positive real number

    - ``height`` -- positive real number

    - ``closed`` -- whether or not to include the base (default: ``True``)

    - ``**kwds`` -- passed to the ParametricSurface constructor

    EXAMPLES::

        sage: from sage.plot.plot3d.shapes import Cone
        sage: c = Cone(3/2, 1, color='red')
        sage: c += Cone(1, 2, color='yellow').translate(3, 0, 0)
        sage: c.show(aspect_ratio=1)

    .. PLOT::

        from sage.plot.plot3d.shapes import Cone
        c = Cone(3/2, 1, color='red') + Cone(1, 2, color='yellow').translate(3, 0, 0)
        sphinx_plot(c)

    We may omit the base::

        sage: Cone(1, 1, closed=False)
        Graphics3d Object

    .. PLOT::

        from sage.plot.plot3d.shapes import Cone
        sphinx_plot(Cone(1, 1, closed=False))

    A spiky plot of the sine function::

        sage: sum(Cone(.1, sin(n), color='yellow').translate(n, sin(n), 0)              # needs sage.symbolic
        ....:     for n in [0..10, step=.1])
        Graphics3d Object

    .. PLOT::

        from sage.plot.plot3d.shapes import Cone
        sphinx_plot(sum(Cone(.1, sin(n/10.0), color='yellow').translate(n/10.0, sin(n/10.0), 0) for n in range(0,100)))

    A Christmas tree::

        sage: T = sum(Cone(exp(-n/5), 4/3*exp(-n/5),                                    # needs sage.symbolic
        ....:              color=(0, .5, 0)).translate(0, 0, -3*exp(-n/5))
        ....:         for n in [1..7])
        sage: T += Cone(1/8, 1, color='brown').translate(0, 0, -3)                      # needs sage.symbolic
        sage: T.show(aspect_ratio=1, frame=False)                                       # needs sage.symbolic

    .. PLOT::

        from sage.plot.plot3d.shapes import Cone
        T = sum(Cone(exp(-n/5.0), 4/3*exp(-n/5.0), color=(0, .5, 0)).translate(0, 0, -3*exp(-n/5.0)) for n in range(8))
        T += Cone(1/8, 1, color='brown').translate(0, 0, -3)
        sphinx_plot(T)"""
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    def __init__(self, radius, height, closed=..., **kwds) -> Any:
        """File: /build/sagemath/src/sage/src/sage/plot/plot3d/shapes.pyx (starting at line 314)

                TESTS::

                    sage: from sage.plot.plot3d.shapes import Cone
                    sage: c = Cone(1/2, 1, opacity=.5)
        """
    def get_grid(self, ds) -> Any:
        """Cone.get_grid(self, ds)

        File: /build/sagemath/src/sage/src/sage/plot/plot3d/shapes.pyx (starting at line 337)

        Return the grid on which to evaluate this parametric surface.

        EXAMPLES::

            sage: from sage.plot.plot3d.shapes import Cone
            sage: Cone(1, 3, closed=True).get_grid(100)
            ([1, 0, -1], [0.0, 1.2566..., 2.5132..., 3.7699..., 5.0265..., 0.0])
            sage: Cone(1, 3, closed=False).get_grid(100)
            ([1, 0], [0.0, 1.2566..., 2.5132..., 3.7699..., 5.0265..., 0.0])
            sage: len(Cone(1, 3).get_grid(.001)[1])
            38"""
    @overload
    def x3d_geometry(self) -> Any:
        '''Cone.x3d_geometry(self)

        File: /build/sagemath/src/sage/src/sage/plot/plot3d/shapes.pyx (starting at line 326)

        EXAMPLES::

            sage: from sage.plot.plot3d.shapes import Cone
            sage: Cone(1, 3).x3d_geometry()
            "<Cone bottomRadius=\'1.0\' height=\'3.0\'/>"'''
    @overload
    def x3d_geometry(self) -> Any:
        '''Cone.x3d_geometry(self)

        File: /build/sagemath/src/sage/src/sage/plot/plot3d/shapes.pyx (starting at line 326)

        EXAMPLES::

            sage: from sage.plot.plot3d.shapes import Cone
            sage: Cone(1, 3).x3d_geometry()
            "<Cone bottomRadius=\'1.0\' height=\'3.0\'/>"'''

class Cylinder(sage.plot.plot3d.parametric_surface.ParametricSurface):
    """Cylinder(radius, height, closed=True, **kwds)

    File: /build/sagemath/src/sage/src/sage/plot/plot3d/shapes.pyx (starting at line 370)

    A cone, with base in the xy-plane pointing up the z-axis.

    INPUT:

    - ``radius`` -- positive real number

    - ``height`` -- positive real number

    - ``closed`` -- whether or not to include the ends (default: ``True``)

    - ``**kwds`` -- passed to the :class:`ParametricSurface` constructor

    EXAMPLES::

        sage: from sage.plot.plot3d.shapes import Cylinder
        sage: c = Cylinder(3/2, 1, color='red')
        sage: c += Cylinder(1, 2, color='yellow').translate(3, 0, 0)
        sage: c.show(aspect_ratio=1)

    .. PLOT::

        from sage.plot.plot3d.shapes import Cylinder
        c = Cylinder(3/2, 1, color='red') + Cylinder(1, 2, color='yellow').translate(3, 0, 0)
        sphinx_plot(c)

    We may omit the base::

        sage: Cylinder(1, 1, closed=False)
        Graphics3d Object

    .. PLOT::

        from sage.plot.plot3d.shapes import Cylinder
        sphinx_plot(Cylinder(1, 1, closed=False))

    Some gears::

        sage: # needs sage.symbolic
        sage: G = Cylinder(1, .5) + Cylinder(.25, 3).translate(0, 0, -3)
        sage: G += sum(Cylinder(.2, 1).translate(cos(2*pi*n/9), sin(2*pi*n/9), 0)
        ....:          for n in [1..9])
        sage: G += G.translate(2.3, 0, -.5)
        sage: G += G.translate(3.5, 2, -1)
        sage: G.show(aspect_ratio=1, frame=False)

    .. PLOT::

        from sage.plot.plot3d.shapes import Cylinder
        G = Cylinder(1, .5) + Cylinder(.25, 3).translate(0, 0, -3)
        G += sum(Cylinder(.2, 1).translate(cos(2*pi*n/9.0), sin(2*pi*n/9.0), 0) for n in range(10))
        G += G.translate(2.3, 0, -.5)
        G += G.translate(3.5, 2, -1)
        sphinx_plot(G)"""
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    def __init__(self, radius, height, closed=..., **kwds) -> Any:
        """File: /build/sagemath/src/sage/src/sage/plot/plot3d/shapes.pyx (starting at line 426)

                TESTS::

                    sage: from sage.plot.plot3d.shapes import Cylinder
                    sage: Cylinder(1, 1, color='red')
                    Graphics3d Object
        """
    @overload
    def bounding_box(self) -> Any:
        """Cylinder.bounding_box(self)

        File: /build/sagemath/src/sage/src/sage/plot/plot3d/shapes.pyx (starting at line 439)

        EXAMPLES::

            sage: from sage.plot.plot3d.shapes import Cylinder
            sage: Cylinder(1, 2).bounding_box()
            ((-1.0, -1.0, 0), (1.0, 1.0, 2.0))"""
    @overload
    def bounding_box(self) -> Any:
        """Cylinder.bounding_box(self)

        File: /build/sagemath/src/sage/src/sage/plot/plot3d/shapes.pyx (starting at line 439)

        EXAMPLES::

            sage: from sage.plot.plot3d.shapes import Cylinder
            sage: Cylinder(1, 2).bounding_box()
            ((-1.0, -1.0, 0), (1.0, 1.0, 2.0))"""
    @overload
    def get_endpoints(self, transform=...) -> Any:
        """Cylinder.get_endpoints(self, transform=None)

        File: /build/sagemath/src/sage/src/sage/plot/plot3d/shapes.pyx (starting at line 536)

        EXAMPLES::

            sage: from sage.plot.plot3d.shapes import Cylinder
            sage: from sage.plot.plot3d.transform import Transformation
            sage: Cylinder(1, 5).get_endpoints()
            ((0, 0, 0), (0, 0, 5.0))
            sage: Cylinder(1, 5).get_endpoints(Transformation(trans=(1,2,3),
            ....:                                             scale=(2,2,2)))
            ((1.0, 2.0, 3.0), (1.0, 2.0, 13.0))"""
    @overload
    def get_endpoints(self) -> Any:
        """Cylinder.get_endpoints(self, transform=None)

        File: /build/sagemath/src/sage/src/sage/plot/plot3d/shapes.pyx (starting at line 536)

        EXAMPLES::

            sage: from sage.plot.plot3d.shapes import Cylinder
            sage: from sage.plot.plot3d.transform import Transformation
            sage: Cylinder(1, 5).get_endpoints()
            ((0, 0, 0), (0, 0, 5.0))
            sage: Cylinder(1, 5).get_endpoints(Transformation(trans=(1,2,3),
            ....:                                             scale=(2,2,2)))
            ((1.0, 2.0, 3.0), (1.0, 2.0, 13.0))"""
    def get_grid(self, ds) -> Any:
        """Cylinder.get_grid(self, ds)

        File: /build/sagemath/src/sage/src/sage/plot/plot3d/shapes.pyx (starting at line 570)

        Return the grid on which to evaluate this parametric surface.

        EXAMPLES::

            sage: from sage.plot.plot3d.shapes import Cylinder
            sage: Cylinder(1, 3, closed=True).get_grid(100)
            ([2, 1, -1, -2], [0.0, 1.2566..., 2.5132..., 3.7699..., 5.0265..., 0.0])
            sage: Cylinder(1, 3, closed=False).get_grid(100)
            ([1, -1], [0.0, 1.2566..., 2.5132..., 3.7699..., 5.0265..., 0.0])
            sage: len(Cylinder(1, 3).get_grid(.001)[1])
            38"""
    @overload
    def get_radius(self, transform=...) -> Any:
        """Cylinder.get_radius(self, transform=None)

        File: /build/sagemath/src/sage/src/sage/plot/plot3d/shapes.pyx (starting at line 553)

        EXAMPLES::

            sage: from sage.plot.plot3d.shapes import Cylinder
            sage: from sage.plot.plot3d.transform import Transformation
            sage: Cylinder(3, 1).get_radius()
            3.0
            sage: Cylinder(3, 1).get_radius(Transformation(trans=(1,2,3),
            ....:                                          scale=(2,2,2)))
            6.0"""
    @overload
    def get_radius(self) -> Any:
        """Cylinder.get_radius(self, transform=None)

        File: /build/sagemath/src/sage/src/sage/plot/plot3d/shapes.pyx (starting at line 553)

        EXAMPLES::

            sage: from sage.plot.plot3d.shapes import Cylinder
            sage: from sage.plot.plot3d.transform import Transformation
            sage: Cylinder(3, 1).get_radius()
            3.0
            sage: Cylinder(3, 1).get_radius(Transformation(trans=(1,2,3),
            ....:                                          scale=(2,2,2)))
            6.0"""
    def jmol_repr(self, render_params) -> Any:
        '''Cylinder.jmol_repr(self, render_params)

        File: /build/sagemath/src/sage/src/sage/plot/plot3d/shapes.pyx (starting at line 499)

        EXAMPLES::

            sage: from sage.plot.plot3d.shapes import Cylinder

        For thin cylinders, lines are used::

            sage: C = Cylinder(.1, 4)
            sage: C.jmol_repr(C.default_render_params())
            [\'\\ndraw line_1 width 0.1 {0 0 0} {0 0 4.0}\\ncolor $line_1  [102,102,255]\\n\']

        For anything larger, we use a pmesh::

            sage: C = Cylinder(3, 1, closed=False)
            sage: C.jmol_repr(C.testing_render_params())
            [\'pmesh obj_1 "obj_1.pmesh"\\ncolor pmesh  [102,102,255]\']'''
    def tachyon_repr(self, render_params) -> Any:
        """Cylinder.tachyon_repr(self, render_params)

        File: /build/sagemath/src/sage/src/sage/plot/plot3d/shapes.pyx (starting at line 461)

        EXAMPLES::

            sage: from sage.plot.plot3d.shapes import Cylinder
            sage: C = Cylinder(1/2, 4, closed=False)
            sage: C.tachyon_repr(C.default_render_params())
            'FCylinder\\n   Base 0 0 0\\n   Apex 0 0 4.0\\n   Rad 0.5\\n   texture...     '
            sage: C = Cylinder(1, 2)
            sage: C.tachyon_repr(C.default_render_params())
                ['Ring Center 0 0 0 Normal 0 0 1 Inner 0 Outer 1.0 texture...',
                 'FCylinder\\n   Base 0 0 0\\n   Apex 0 0 2.0\\n   Rad 1.0\\n   texture...     ',
                 'Ring Center 0 0 2.0 Normal 0 0 1 Inner 0 Outer 1.0 texture...']"""
    @overload
    def x3d_geometry(self) -> Any:
        '''Cylinder.x3d_geometry(self)

        File: /build/sagemath/src/sage/src/sage/plot/plot3d/shapes.pyx (starting at line 450)

        EXAMPLES::

            sage: from sage.plot.plot3d.shapes import Cylinder
            sage: Cylinder(1, 2).x3d_geometry()
            "<Cylinder radius=\'1.0\' height=\'2.0\'/>"'''
    @overload
    def x3d_geometry(self) -> Any:
        '''Cylinder.x3d_geometry(self)

        File: /build/sagemath/src/sage/src/sage/plot/plot3d/shapes.pyx (starting at line 450)

        EXAMPLES::

            sage: from sage.plot.plot3d.shapes import Cylinder
            sage: Cylinder(1, 2).x3d_geometry()
            "<Cylinder radius=\'1.0\' height=\'2.0\'/>"'''

class Sphere(sage.plot.plot3d.parametric_surface.ParametricSurface):
    """Sphere(radius, **kwds)

    File: /build/sagemath/src/sage/src/sage/plot/plot3d/shapes.pyx (starting at line 800)

    This class represents a sphere centered at the origin.

    EXAMPLES::

        sage: from sage.plot.plot3d.shapes import Sphere
        sage: Sphere(3)
        Graphics3d Object

    .. PLOT::

        from sage.plot.plot3d.shapes import Sphere
        sphinx_plot(Sphere(3))

    Plot with ``aspect_ratio=1`` to see it unsquashed::

        sage: S = Sphere(3, color='blue') + Sphere(2, color='red').translate(0,3,0)
        sage: S.show(aspect_ratio=1)

    .. PLOT::

        from sage.plot.plot3d.shapes import Sphere
        S = Sphere(3, color='blue') + Sphere(2, color='red').translate(0,3,0)
        sphinx_plot(S)

    Scale to get an ellipsoid::

        sage: S = Sphere(1).scale(1,2,1/2)
        sage: S.show(aspect_ratio=1)

    .. PLOT::

        from sage.plot.plot3d.shapes import Sphere
        S = Sphere(1).scale(1,2,1/2)
        sphinx_plot(S)"""
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    def __init__(self, radius, **kwds) -> Any:
        """File: /build/sagemath/src/sage/src/sage/plot/plot3d/shapes.pyx (starting at line 837)

                TESTS::

                    sage: from sage.plot.plot3d.shapes import Sphere
                    sage: Sphere(3)
                    Graphics3d Object
        """
    @overload
    def bounding_box(self) -> Any:
        """Sphere.bounding_box(self)

        File: /build/sagemath/src/sage/src/sage/plot/plot3d/shapes.pyx (starting at line 848)

        Return the bounding box that contains this sphere.

        EXAMPLES::

            sage: from sage.plot.plot3d.shapes import Sphere
            sage: Sphere(3).bounding_box()
            ((-3.0, -3.0, -3.0), (3.0, 3.0, 3.0))"""
    @overload
    def bounding_box(self) -> Any:
        """Sphere.bounding_box(self)

        File: /build/sagemath/src/sage/src/sage/plot/plot3d/shapes.pyx (starting at line 848)

        Return the bounding box that contains this sphere.

        EXAMPLES::

            sage: from sage.plot.plot3d.shapes import Sphere
            sage: Sphere(3).bounding_box()
            ((-3.0, -3.0, -3.0), (3.0, 3.0, 3.0))"""
    def get_grid(self, doubleds) -> Any:
        """Sphere.get_grid(self, double ds)

        File: /build/sagemath/src/sage/src/sage/plot/plot3d/shapes.pyx (starting at line 946)

        Return the range of variables to be evaluated on to render as a
        parametric surface.

        EXAMPLES::

            sage: from sage.plot.plot3d.shapes import Sphere
            sage: Sphere(1).get_grid(100)
            ([-10.0, ..., 10.0],
             [0.0, ..., 3.141592653589793, ..., 0.0])"""
    def jmol_repr(self, render_params) -> Any:
        '''Sphere.jmol_repr(self, render_params)

        File: /build/sagemath/src/sage/src/sage/plot/plot3d/shapes.pyx (starting at line 904)

        EXAMPLES::

            sage: from sage.plot.plot3d.shapes import Sphere

        Jmol has native code for handling spheres::

            sage: S = Sphere(2)
            sage: S.jmol_repr(S.default_render_params())
            [\'isosurface sphere_1  center {0 0 0} sphere 2.0\\ncolor isosurface  [102,102,255]\']
            sage: S.translate(10, 100, 1000).jmol_repr(S.default_render_params())
            [[\'isosurface sphere_1  center {10.0 100.0 1000.0} sphere 2.0\\ncolor isosurface  [102,102,255]\']]

        It cannot natively handle ellipsoids::

            sage: Sphere(1).scale(2, 3, 4).jmol_repr(S.testing_render_params())
            [[\'pmesh obj_2 "obj_2.pmesh"\\ncolor pmesh  [102,102,255]\']]

        Small spheres need extra hints to render well::

            sage: Sphere(.01).jmol_repr(S.default_render_params())
            [\'isosurface sphere_1 resolution 100 center {0 0 0} sphere 0.01\\ncolor isosurface  [102,102,255]\']'''
    def tachyon_repr(self, render_params) -> Any:
        """Sphere.tachyon_repr(self, render_params)

        File: /build/sagemath/src/sage/src/sage/plot/plot3d/shapes.pyx (starting at line 871)

        Tachyon can natively handle spheres. Ellipsoids rendering is done
        as a parametric surface.

        EXAMPLES::

            sage: from sage.plot.plot3d.shapes import Sphere
            sage: S = Sphere(2)
            sage: S.tachyon_repr(S.default_render_params())
            'Sphere center 0 0 0 Rad 2.0 texture...'
            sage: S.translate(1, 2, 3).scale(3).tachyon_repr(S.default_render_params())
            [['Sphere center 3.0 6.0 9.0 Rad 6.0 texture...']]
            sage: S.scale(1,1/2,1/4).tachyon_repr(S.default_render_params())
            [['TRI V0 0 0 -0.5 V1 0.308116 0.0271646 -0.493844 V2 0.312869 0 -0.493844',
              'texture...',
               ...
              'TRI V0 0.308116 -0.0271646 0.493844 V1 0.312869 0 0.493844 V2 0 0 0.5',
              'texture...']]"""
    @overload
    def x3d_geometry(self) -> Any:
        '''Sphere.x3d_geometry(self)

        File: /build/sagemath/src/sage/src/sage/plot/plot3d/shapes.pyx (starting at line 861)

        EXAMPLES::

            sage: from sage.plot.plot3d.shapes import Sphere
            sage: Sphere(12).x3d_geometry()
            "<Sphere radius=\'12.0\'/>"'''
    @overload
    def x3d_geometry(self) -> Any:
        '''Sphere.x3d_geometry(self)

        File: /build/sagemath/src/sage/src/sage/plot/plot3d/shapes.pyx (starting at line 861)

        EXAMPLES::

            sage: from sage.plot.plot3d.shapes import Sphere
            sage: Sphere(12).x3d_geometry()
            "<Sphere radius=\'12.0\'/>"'''

class Text(sage.plot.plot3d.base.PrimitiveObject):
    '''File: /build/sagemath/src/sage/src/sage/plot/plot3d/shapes.pyx (starting at line 1067)

        A text label attached to a point in 3d space. It always starts at the
        origin, translate it to move it elsewhere.

        EXAMPLES::

            sage: from sage.plot.plot3d.shapes import Text
            sage: Text("Just a lonely label.")
            Graphics3d Object

        .. PLOT::

            from sage.plot.plot3d.shapes import Text
            sphinx_plot(Text("Just a lonely label. "))

        ::

            sage: pts = [(RealField(10)^3).random_element() for k in range(20)]
            sage: sum(Text(str(P)).translate(P) for P in pts)
            Graphics3d Object

        .. PLOT::

            from sage.plot.plot3d.shapes import Text
            pts = [(RealField(10)**3).random_element() for k in range(20)]
            sphinx_plot(sum(Text(str(P)).translate(P) for P in pts))
    '''
    def __init__(self, string, **kwds) -> Any:
        '''Text.__init__(self, string, **kwds)

        File: /build/sagemath/src/sage/src/sage/plot/plot3d/shapes.pyx (starting at line 1095)

        TESTS::

            sage: from sage.plot.plot3d.shapes import Text
            sage: T = Text("Hi")'''
    @overload
    def bounding_box(self) -> Any:
        '''Text.bounding_box(self)

        File: /build/sagemath/src/sage/src/sage/plot/plot3d/shapes.pyx (starting at line 1225)

        Text labels have no extent::

            sage: from sage.plot.plot3d.shapes import Text
            sage: Text("Hi").bounding_box()
            ((0, 0, 0), (0, 0, 0))'''
    @overload
    def bounding_box(self) -> Any:
        '''Text.bounding_box(self)

        File: /build/sagemath/src/sage/src/sage/plot/plot3d/shapes.pyx (starting at line 1225)

        Text labels have no extent::

            sage: from sage.plot.plot3d.shapes import Text
            sage: Text("Hi").bounding_box()
            ((0, 0, 0), (0, 0, 0))'''
    def jmol_repr(self, render_params) -> Any:
        '''Text.jmol_repr(self, render_params)

        File: /build/sagemath/src/sage/src/sage/plot/plot3d/shapes.pyx (starting at line 1150)

        Labels in jmol must be attached to atoms.

        EXAMPLES::

            sage: from sage.plot.plot3d.shapes import Text
            sage: T = Text("Hi")
            sage: T.jmol_repr(T.testing_render_params())
            [\'select atomno = 1\', \'color atom  [102,102,255]\', \'label "Hi"\']
            sage: T = Text("Hi").translate(-1, 0, 0) + Text("Bye").translate(1, 0, 0)
            sage: T.jmol_repr(T.testing_render_params())
            [[[\'select atomno = 1\', \'color atom  [102,102,255]\', \'label "Hi"\']],
             [[\'select atomno = 2\', \'color atom  [102,102,255]\', \'label "Bye"\']]]'''
    @overload
    def obj_repr(self, render_params) -> Any:
        '''Text.obj_repr(self, render_params)

        File: /build/sagemath/src/sage/src/sage/plot/plot3d/shapes.pyx (starting at line 1116)

        The obj file format does not support text strings::

            sage: from sage.plot.plot3d.shapes import Text
            sage: Text("Hi").obj_repr(None)
            \'\''''
    @overload
    def obj_repr(self, _None) -> Any:
        '''Text.obj_repr(self, render_params)

        File: /build/sagemath/src/sage/src/sage/plot/plot3d/shapes.pyx (starting at line 1116)

        The obj file format does not support text strings::

            sage: from sage.plot.plot3d.shapes import Text
            sage: Text("Hi").obj_repr(None)
            \'\''''
    @overload
    def tachyon_repr(self, render_params) -> Any:
        '''Text.tachyon_repr(self, render_params)

        File: /build/sagemath/src/sage/src/sage/plot/plot3d/shapes.pyx (starting at line 1126)

        Strings are not yet supported in Tachyon, so we ignore them for now::

            sage: from sage.plot.plot3d.shapes import Text
            sage: Text("Hi").tachyon_repr(None)
            \'\''''
    @overload
    def tachyon_repr(self, _None) -> Any:
        '''Text.tachyon_repr(self, render_params)

        File: /build/sagemath/src/sage/src/sage/plot/plot3d/shapes.pyx (starting at line 1126)

        Strings are not yet supported in Tachyon, so we ignore them for now::

            sage: from sage.plot.plot3d.shapes import Text
            sage: Text("Hi").tachyon_repr(None)
            \'\''''
    def threejs_repr(self, render_params) -> Any:
        '''Text.threejs_repr(self, render_params)

        File: /build/sagemath/src/sage/src/sage/plot/plot3d/shapes.pyx (starting at line 1174)

        Return representation of the text suitable for plotting in three.js.

        EXAMPLES::

            sage: T = text3d("Hi", (1, 2, 3), color=\'red\', fontfamily=\'serif\',
            ....:            fontweight=\'bold\', fontstyle=\'italic\', fontsize=20,
            ....:            opacity=0.5)
            sage: T.threejs_repr(T.default_render_params())
            [(\'text\',
              {\'color\': \'#ff0000\',
               \'fontFamily\': [\'serif\'],
               \'fontSize\': 20.0,
               \'fontStyle\': \'italic\',
               \'fontWeight\': \'bold\',
               \'opacity\': 0.5,
               \'text\': \'Hi\',
               \'x\': 1.0,
               \'y\': 2.0,
               \'z\': 3.0})]

        TESTS:

        When created directly via the ``Text`` constructor instead of ``text3d``,
        the text is located at the origin::

            sage: from sage.plot.plot3d.shapes import Text
            sage: T = Text("Hi")
            sage: T.threejs_repr(T.default_render_params())
            [(\'text\',
              {\'color\': \'#6666ff\',
               \'fontFamily\': [\'monospace\'],
               \'fontSize\': 14.0,
               \'fontStyle\': \'normal\',
               \'fontWeight\': \'normal\',
               \'opacity\': 1.0,
               \'text\': \'Hi\',
               \'x\': 0.0,
               \'y\': 0.0,
               \'z\': 0.0})]'''
    @overload
    def x3d_geometry(self) -> Any:
        '''Text.x3d_geometry(self)

        File: /build/sagemath/src/sage/src/sage/plot/plot3d/shapes.pyx (starting at line 1106)

        EXAMPLES::

            sage: from sage.plot.plot3d.shapes import Text
            sage: Text("Hi").x3d_geometry()
            "<Text string=\'Hi\' solid=\'true\'/>"'''
    @overload
    def x3d_geometry(self) -> Any:
        '''Text.x3d_geometry(self)

        File: /build/sagemath/src/sage/src/sage/plot/plot3d/shapes.pyx (starting at line 1106)

        EXAMPLES::

            sage: from sage.plot.plot3d.shapes import Text
            sage: Text("Hi").x3d_geometry()
            "<Text string=\'Hi\' solid=\'true\'/>"'''

class Torus(sage.plot.plot3d.parametric_surface.ParametricSurface):
    """Torus(R=1, r=.3, **kwds)

    File: /build/sagemath/src/sage/src/sage/plot/plot3d/shapes.pyx (starting at line 976)

    INPUT:

    - ``R`` -- (default: ``1``) outer radius
    - ``r`` -- (default: ``.3``) inner radius

    OUTPUT: a 3d torus

    EXAMPLES::

        sage: from sage.plot.plot3d.shapes import Torus
        sage: Torus(1, .2).show(aspect_ratio=1)

    .. PLOT::

        from sage.plot.plot3d.shapes import Torus
        sphinx_plot(Torus(1, .2))

    ::

        sage: Torus(1, .7, color='red').show(aspect_ratio=1)

    .. PLOT::

        from sage.plot.plot3d.shapes import Torus
        sphinx_plot(Torus(1, .7, color='red'))

    A rubberband ball::

        sage: show(sum(Torus(1, .03, color=(1, t/30.0, 0)).rotate((1,1,1), t)
        ....:          for t in range(30)))

    .. PLOT::

        from sage.plot.plot3d.shapes import Torus
        sphinx_plot(sum([Torus(1, .03, color=(1, t/30.0, 0)).rotate((1,1,1),t) for t in range(30)]))

    Mmm... doughnuts::

        sage: D = Torus(1, .4, color=(.5, .3, .2))
        sage: D += Torus(1, .3, color='yellow').translate(0, 0, .15)
        sage: G = sum(D.translate(RDF.random_element(-.2, .2),
        ....:                     RDF.random_element(-.2, .2),
        ....:                     .8*t)
        ....:         for t in range(10))
        sage: G.show(aspect_ratio=1, frame=False)

    .. PLOT::

        from sage.plot.plot3d.shapes import Torus
        D = Torus(1, .4, color=(.5, .3, .2)) + Torus(1, .3, color='yellow').translate(0, 0, .15)
        G = sum(D.translate(RDF.random_element(-.2, .2), RDF.random_element(-.2, .2), .8*t) for t in range(10))
        sphinx_plot(G)"""
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    def __init__(self, R=..., r=..., **kwds) -> Any:
        """File: /build/sagemath/src/sage/src/sage/plot/plot3d/shapes.pyx (starting at line 1031)

                TESTS::

                    sage: from sage.plot.plot3d.shapes import Torus
                    sage: T = Torus(1, .5)
        """
    def get_grid(self, ds) -> Any:
        """Torus.get_grid(self, ds)

        File: /build/sagemath/src/sage/src/sage/plot/plot3d/shapes.pyx (starting at line 1042)

        Return the range of variables to be evaluated on to render as a
        parametric surface.

        EXAMPLES::

            sage: from sage.plot.plot3d.shapes import Torus
            sage: Torus(2, 1).get_grid(100)
            ([0.0, -1.047..., -3.141592653589793, ..., 0.0],
             [0.0, 1.047..., 3.141592653589793, ..., 0.0])"""
