import _cython_3_2_1
import sage.plot.plot3d.base
from sage.categories.category import RDF as RDF
from sage.cpython.string import bytes_to_str as bytes_to_str, str_to_bytes as str_to_bytes
from sage.modules.free_module_element import vector as vector
from sage.plot.colors import Color as Color, float_to_integer as float_to_integer
from sage.plot.plot3d.base import Graphics3dGroup as Graphics3dGroup
from sage.plot.plot3d.texture import Texture as Texture
from typing import Any, ClassVar, overload

cut_edge_by_bisection: _cython_3_2_1.cython_function_or_method
midpoint: _cython_3_2_1.cython_function_or_method
sticker: _cython_3_2_1.cython_function_or_method

class EdgeIter:
    """EdgeIter(face_set)

    File: /build/sagemath/src/sage/src/sage/plot/plot3d/index_face_set.pyx (starting at line 1774)

    A class for iteration over edges

    EXAMPLES::

        sage: from sage.plot.plot3d.shapes import *
        sage: S = Box(1,2,3)
        sage: len(list(S.edges())) == 12   # indirect doctest
        True"""
    def __init__(self, face_set) -> Any:
        """File: /build/sagemath/src/sage/src/sage/plot/plot3d/index_face_set.pyx (starting at line 1785)"""
    def __iter__(self) -> Any:
        """EdgeIter.__iter__(self)

        File: /build/sagemath/src/sage/src/sage/plot/plot3d/index_face_set.pyx (starting at line 1793)"""
    def __next__(self) -> Any:
        """EdgeIter.__next__(self)

        File: /build/sagemath/src/sage/src/sage/plot/plot3d/index_face_set.pyx (starting at line 1796)"""

class FaceIter:
    """FaceIter(face_set)

    File: /build/sagemath/src/sage/src/sage/plot/plot3d/index_face_set.pyx (starting at line 1743)

    A class for iteration over faces

    EXAMPLES::

        sage: from sage.plot.plot3d.shapes import *
        sage: S = Box(1,2,3)
        sage: len(list(S.faces())) == 6   # indirect doctest
        True"""
    def __init__(self, face_set) -> Any:
        """File: /build/sagemath/src/sage/src/sage/plot/plot3d/index_face_set.pyx (starting at line 1754)"""
    def __iter__(self) -> Any:
        """FaceIter.__iter__(self)

        File: /build/sagemath/src/sage/src/sage/plot/plot3d/index_face_set.pyx (starting at line 1758)"""
    def __next__(self) -> Any:
        """FaceIter.__next__(self)

        File: /build/sagemath/src/sage/src/sage/plot/plot3d/index_face_set.pyx (starting at line 1761)"""

class IndexFaceSet(sage.plot.plot3d.base.PrimitiveObject):
    """IndexFaceSet(faces, point_list=None, enclosed=False, texture_list=None, **kwds)

    File: /build/sagemath/src/sage/src/sage/plot/plot3d/index_face_set.pyx (starting at line 285)

    Graphics3D object that consists of a list of polygons, also used for
    triangulations of other objects.

    Polygons (mostly triangles and quadrilaterals) are stored in the
    c struct ``face_c`` (see transform.pyx). Rather than storing
    the points directly for each polygon, each face consists a list
    of pointers into a common list of points which are basically triples
    of doubles in a ``point_c``.

    Moreover, each face has an attribute ``color`` which is used to
    store color information when faces are colored. The red/green/blue
    components are then available as floats between 0 and 1 using
    ``color.r,color.g,color.b``.

    Usually these objects are not created directly by users.

    EXAMPLES::

        sage: from sage.plot.plot3d.index_face_set import IndexFaceSet
        sage: S = IndexFaceSet([[(1,0,0),(0,1,0),(0,0,1)], [(1,0,0),(0,1,0),(0,0,0)]])
        sage: S.face_list()
        [[(1.0, 0.0, 0.0), (0.0, 1.0, 0.0), (0.0, 0.0, 1.0)],
         [(1.0, 0.0, 0.0), (0.0, 1.0, 0.0), (0.0, 0.0, 0.0)]]
        sage: S.vertex_list()
        [(1.0, 0.0, 0.0), (0.0, 1.0, 0.0), (0.0, 0.0, 1.0), (0.0, 0.0, 0.0)]

        sage: def make_face(n): return [(0,0,n),(0,1,n),(1,1,n),(1,0,n)]
        sage: S = IndexFaceSet([make_face(n) for n in range(10)])
        sage: S.show()

        sage: point_list = [(1,0,0),(0,1,0)] + [(0,0,n) for n in range(10)]
        sage: face_list = [[0,1,n] for n in range(2,10)]
        sage: S = IndexFaceSet(face_list, point_list, color='red')
        sage: S.face_list()
        [[(1.0, 0.0, 0.0), (0.0, 1.0, 0.0), (0.0, 0.0, 0.0)],
         [(1.0, 0.0, 0.0), (0.0, 1.0, 0.0), (0.0, 0.0, 1.0)],
         [(1.0, 0.0, 0.0), (0.0, 1.0, 0.0), (0.0, 0.0, 2.0)],
         [(1.0, 0.0, 0.0), (0.0, 1.0, 0.0), (0.0, 0.0, 3.0)],
         [(1.0, 0.0, 0.0), (0.0, 1.0, 0.0), (0.0, 0.0, 4.0)],
         [(1.0, 0.0, 0.0), (0.0, 1.0, 0.0), (0.0, 0.0, 5.0)],
         [(1.0, 0.0, 0.0), (0.0, 1.0, 0.0), (0.0, 0.0, 6.0)],
         [(1.0, 0.0, 0.0), (0.0, 1.0, 0.0), (0.0, 0.0, 7.0)]]
        sage: S.show()

    A simple example of colored IndexFaceSet (:issue:`12212`)::

        sage: from sage.plot.plot3d.index_face_set import IndexFaceSet
        sage: from sage.plot.plot3d.texture import Texture
        sage: point_list = [(2,0,0),(0,2,0),(0,0,2),(0,1,1),(1,0,1),(1,1,0)]
        sage: face_list = [[0,4,5],[3,4,5],[2,3,4],[1,3,5]]
        sage: col = rainbow(10, 'rgbtuple')
        sage: t_list = [Texture(col[i]) for i in range(10)]
        sage: S = IndexFaceSet(face_list, point_list, texture_list=t_list)
        sage: S.show(viewer='tachyon')"""
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    @overload
    def __init__(self, faces, point_list=..., enclosed=..., texture_list=..., **kwds) -> Any:
        """File: /build/sagemath/src/sage/src/sage/plot/plot3d/index_face_set.pyx (starting at line 343)"""
    @overload
    def __init__(self, face_list, point_list, color=...) -> Any:
        """File: /build/sagemath/src/sage/src/sage/plot/plot3d/index_face_set.pyx (starting at line 343)"""
    @overload
    def __init__(self) -> Any:
        """File: /build/sagemath/src/sage/src/sage/plot/plot3d/index_face_set.pyx (starting at line 343)"""
    @overload
    def __init__(self, face_list, point_list, texture_list=...) -> Any:
        """File: /build/sagemath/src/sage/src/sage/plot/plot3d/index_face_set.pyx (starting at line 343)"""
    @overload
    def add_condition(self, condition, N=..., eps=...) -> Any:
        '''IndexFaceSet.add_condition(self, condition, N=100, eps=1.0E-6)

        File: /build/sagemath/src/sage/src/sage/plot/plot3d/index_face_set.pyx (starting at line 987)

        Cut the surface according to the given condition.

        This allows to take the intersection of the surface
        with a domain in 3-space, in such a way that the result
        has a smooth boundary.

        INPUT:

        - ``condition`` -- boolean function on ambient space, that
          defines the domain

        - ``N`` -- max number of steps used by the bisection method
          (default: 100) to cut the boundary triangles that are not
          entirely within the domain.

        - ``eps`` -- target accuracy in the intersection (default: 1.0e-6)

        OUTPUT: an ``IndexFaceSet``

        This will contain both triangular and quadrilateral faces.

        EXAMPLES::

            sage: var(\'x,y,z\')                                                          # needs sage.symbolic
            (x, y, z)
            sage: P = implicit_plot3d(z-x*y,(-2,2),(-2,2),(-2,2))                       # needs sage.symbolic
            sage: def condi(x, y, z):
            ....:     return bool(x*x+y*y+z*z <= Integer(1))
            sage: R = P.add_condition(condi, 20); R                                     # needs sage.symbolic
            Graphics3d Object

        .. PLOT::

            x,y,z = var(\'x,y,z\')
            P = implicit_plot3d(z-x*y,(-2,2),(-2,2),(-2,2))
            def condi(x, y, z):
                return bool(x*x+y*y+z*z <= Integer(1))
            sphinx_plot(P.add_condition(condi,40))

        An example with colors::

            sage: def condi(x, y, z):
            ....:     return bool(x*x+y*y <= 1.1)
            sage: cm = colormaps.hsv
            sage: cf = lambda x,y,z: float(x+y) % 1
            sage: P = implicit_plot3d(x**2+y**2+z**2-1-x**2*z+y**2*z,                   # needs sage.symbolic
            ....:                     (-2,2),(-2,2),(-2,2),color=(cm,cf))
            sage: R = P.add_condition(condi,40); R                                      # needs sage.symbolic
            Graphics3d Object

        .. PLOT::

            x,y,z = var(\'x,y,z\')
            def condi(x, y, z):
                return bool(x*x+y*y <= 1.1)
            cm = colormaps.hsv
            cf = lambda x,y,z: float(x+y) % 1
            P = implicit_plot3d(x**2+y**2+z**2-1-x**2*z+y**2*z,(-2,2),(-2,2),(-2,2),color=(cm,cf))
            sphinx_plot(P.add_condition(condi,40))

        An example with transparency::

            sage: P = implicit_plot3d(x**4+y**4+z**2-4, (x,-2,2), (y,-2,2), (z,-2,2),   # needs sage.symbolic
            ....:                     alpha=0.3)
            sage: def cut(a, b, c):
            ....:     return a*a+c*c > 2
            sage: Q = P.add_condition(cut,40); Q                                        # needs sage.symbolic
            Graphics3d Object

        .. PLOT::

            x,y,z = var(\'x,y,z\')
            P = implicit_plot3d(x**4+y**4+z**2-4,(x,-2,2),(y,-2,2),(z,-2,2),alpha=0.3)
            def cut(a, b, c):
                return a*a+c*c > 2
            sphinx_plot(P.add_condition(cut,40))

        A sombrero with quadrilaterals::

            sage: P = plot3d(-sin(2*x*x+2*y*y)*exp(-x*x-y*y), (x,-2,2), (y,-2,2),       # needs sage.symbolic
            ....:            color=\'gold\')
            sage: def cut(x, y, z):
            ....:     return x*x+y*y < 1
            sage: Q = P.add_condition(cut);Q                                            # needs sage.symbolic
            Graphics3d Object

        .. PLOT::

            x,y,z = var(\'x,y,z\')
            P = plot3d(-sin(2*x*x+2*y*y)*exp(-x*x-y*y),(x,-2,2),(y,-2,2),color=\'gold\')
            def cut(x, y, z):
                return x*x+y*y < 1
            sphinx_plot(P.add_condition(cut))

        TESTS:

        One test for preservation of transparency :issue:`28783`::

            sage: # needs sage.symbolic
            sage: x,y,z = var(\'x,y,z\')
            sage: P = plot3d(cos(x*y),(x,-2,2),(y,-2,2),color=\'red\',opacity=0.1)
            sage: def condi(x, y, z):
            ....:     return not(x*x+y*y <= 1)
            sage: Q = P.add_condition(condi, 40)
            sage: L = Q.json_repr(Q.default_render_params())
            sage: \'"opacity":0.1\' in L[-1]
            True

        A test that this works with polygons::

            sage: p = polygon3d([[2,0,0], [0,2,0], [0,0,3]])
            sage: def f(x, y, z):
            ....:     return bool(x*x+y*y+z*z<=5)
            sage: cut = p.add_condition(f,60,1.0e-12); cut.face_list()                  # needs sage.symbolic
            [[(0.556128491210302, 0.0, 2.165807263184547),
            (2.0, 0.0, 0.0),
            (0.0, 2.0, 0.0),
            (0.0, 0.556128491210302, 2.165807263184547)]]

        .. TODO::

            - Use a dichotomy to search for the place where to cut,
            - Compute the cut only once for each edge.'''
    @overload
    def add_condition(self, cut) -> Any:
        '''IndexFaceSet.add_condition(self, condition, N=100, eps=1.0E-6)

        File: /build/sagemath/src/sage/src/sage/plot/plot3d/index_face_set.pyx (starting at line 987)

        Cut the surface according to the given condition.

        This allows to take the intersection of the surface
        with a domain in 3-space, in such a way that the result
        has a smooth boundary.

        INPUT:

        - ``condition`` -- boolean function on ambient space, that
          defines the domain

        - ``N`` -- max number of steps used by the bisection method
          (default: 100) to cut the boundary triangles that are not
          entirely within the domain.

        - ``eps`` -- target accuracy in the intersection (default: 1.0e-6)

        OUTPUT: an ``IndexFaceSet``

        This will contain both triangular and quadrilateral faces.

        EXAMPLES::

            sage: var(\'x,y,z\')                                                          # needs sage.symbolic
            (x, y, z)
            sage: P = implicit_plot3d(z-x*y,(-2,2),(-2,2),(-2,2))                       # needs sage.symbolic
            sage: def condi(x, y, z):
            ....:     return bool(x*x+y*y+z*z <= Integer(1))
            sage: R = P.add_condition(condi, 20); R                                     # needs sage.symbolic
            Graphics3d Object

        .. PLOT::

            x,y,z = var(\'x,y,z\')
            P = implicit_plot3d(z-x*y,(-2,2),(-2,2),(-2,2))
            def condi(x, y, z):
                return bool(x*x+y*y+z*z <= Integer(1))
            sphinx_plot(P.add_condition(condi,40))

        An example with colors::

            sage: def condi(x, y, z):
            ....:     return bool(x*x+y*y <= 1.1)
            sage: cm = colormaps.hsv
            sage: cf = lambda x,y,z: float(x+y) % 1
            sage: P = implicit_plot3d(x**2+y**2+z**2-1-x**2*z+y**2*z,                   # needs sage.symbolic
            ....:                     (-2,2),(-2,2),(-2,2),color=(cm,cf))
            sage: R = P.add_condition(condi,40); R                                      # needs sage.symbolic
            Graphics3d Object

        .. PLOT::

            x,y,z = var(\'x,y,z\')
            def condi(x, y, z):
                return bool(x*x+y*y <= 1.1)
            cm = colormaps.hsv
            cf = lambda x,y,z: float(x+y) % 1
            P = implicit_plot3d(x**2+y**2+z**2-1-x**2*z+y**2*z,(-2,2),(-2,2),(-2,2),color=(cm,cf))
            sphinx_plot(P.add_condition(condi,40))

        An example with transparency::

            sage: P = implicit_plot3d(x**4+y**4+z**2-4, (x,-2,2), (y,-2,2), (z,-2,2),   # needs sage.symbolic
            ....:                     alpha=0.3)
            sage: def cut(a, b, c):
            ....:     return a*a+c*c > 2
            sage: Q = P.add_condition(cut,40); Q                                        # needs sage.symbolic
            Graphics3d Object

        .. PLOT::

            x,y,z = var(\'x,y,z\')
            P = implicit_plot3d(x**4+y**4+z**2-4,(x,-2,2),(y,-2,2),(z,-2,2),alpha=0.3)
            def cut(a, b, c):
                return a*a+c*c > 2
            sphinx_plot(P.add_condition(cut,40))

        A sombrero with quadrilaterals::

            sage: P = plot3d(-sin(2*x*x+2*y*y)*exp(-x*x-y*y), (x,-2,2), (y,-2,2),       # needs sage.symbolic
            ....:            color=\'gold\')
            sage: def cut(x, y, z):
            ....:     return x*x+y*y < 1
            sage: Q = P.add_condition(cut);Q                                            # needs sage.symbolic
            Graphics3d Object

        .. PLOT::

            x,y,z = var(\'x,y,z\')
            P = plot3d(-sin(2*x*x+2*y*y)*exp(-x*x-y*y),(x,-2,2),(y,-2,2),color=\'gold\')
            def cut(x, y, z):
                return x*x+y*y < 1
            sphinx_plot(P.add_condition(cut))

        TESTS:

        One test for preservation of transparency :issue:`28783`::

            sage: # needs sage.symbolic
            sage: x,y,z = var(\'x,y,z\')
            sage: P = plot3d(cos(x*y),(x,-2,2),(y,-2,2),color=\'red\',opacity=0.1)
            sage: def condi(x, y, z):
            ....:     return not(x*x+y*y <= 1)
            sage: Q = P.add_condition(condi, 40)
            sage: L = Q.json_repr(Q.default_render_params())
            sage: \'"opacity":0.1\' in L[-1]
            True

        A test that this works with polygons::

            sage: p = polygon3d([[2,0,0], [0,2,0], [0,0,3]])
            sage: def f(x, y, z):
            ....:     return bool(x*x+y*y+z*z<=5)
            sage: cut = p.add_condition(f,60,1.0e-12); cut.face_list()                  # needs sage.symbolic
            [[(0.556128491210302, 0.0, 2.165807263184547),
            (2.0, 0.0, 0.0),
            (0.0, 2.0, 0.0),
            (0.0, 0.556128491210302, 2.165807263184547)]]

        .. TODO::

            - Use a dichotomy to search for the place where to cut,
            - Compute the cut only once for each edge.'''
    @overload
    def add_condition(self, cut) -> Any:
        '''IndexFaceSet.add_condition(self, condition, N=100, eps=1.0E-6)

        File: /build/sagemath/src/sage/src/sage/plot/plot3d/index_face_set.pyx (starting at line 987)

        Cut the surface according to the given condition.

        This allows to take the intersection of the surface
        with a domain in 3-space, in such a way that the result
        has a smooth boundary.

        INPUT:

        - ``condition`` -- boolean function on ambient space, that
          defines the domain

        - ``N`` -- max number of steps used by the bisection method
          (default: 100) to cut the boundary triangles that are not
          entirely within the domain.

        - ``eps`` -- target accuracy in the intersection (default: 1.0e-6)

        OUTPUT: an ``IndexFaceSet``

        This will contain both triangular and quadrilateral faces.

        EXAMPLES::

            sage: var(\'x,y,z\')                                                          # needs sage.symbolic
            (x, y, z)
            sage: P = implicit_plot3d(z-x*y,(-2,2),(-2,2),(-2,2))                       # needs sage.symbolic
            sage: def condi(x, y, z):
            ....:     return bool(x*x+y*y+z*z <= Integer(1))
            sage: R = P.add_condition(condi, 20); R                                     # needs sage.symbolic
            Graphics3d Object

        .. PLOT::

            x,y,z = var(\'x,y,z\')
            P = implicit_plot3d(z-x*y,(-2,2),(-2,2),(-2,2))
            def condi(x, y, z):
                return bool(x*x+y*y+z*z <= Integer(1))
            sphinx_plot(P.add_condition(condi,40))

        An example with colors::

            sage: def condi(x, y, z):
            ....:     return bool(x*x+y*y <= 1.1)
            sage: cm = colormaps.hsv
            sage: cf = lambda x,y,z: float(x+y) % 1
            sage: P = implicit_plot3d(x**2+y**2+z**2-1-x**2*z+y**2*z,                   # needs sage.symbolic
            ....:                     (-2,2),(-2,2),(-2,2),color=(cm,cf))
            sage: R = P.add_condition(condi,40); R                                      # needs sage.symbolic
            Graphics3d Object

        .. PLOT::

            x,y,z = var(\'x,y,z\')
            def condi(x, y, z):
                return bool(x*x+y*y <= 1.1)
            cm = colormaps.hsv
            cf = lambda x,y,z: float(x+y) % 1
            P = implicit_plot3d(x**2+y**2+z**2-1-x**2*z+y**2*z,(-2,2),(-2,2),(-2,2),color=(cm,cf))
            sphinx_plot(P.add_condition(condi,40))

        An example with transparency::

            sage: P = implicit_plot3d(x**4+y**4+z**2-4, (x,-2,2), (y,-2,2), (z,-2,2),   # needs sage.symbolic
            ....:                     alpha=0.3)
            sage: def cut(a, b, c):
            ....:     return a*a+c*c > 2
            sage: Q = P.add_condition(cut,40); Q                                        # needs sage.symbolic
            Graphics3d Object

        .. PLOT::

            x,y,z = var(\'x,y,z\')
            P = implicit_plot3d(x**4+y**4+z**2-4,(x,-2,2),(y,-2,2),(z,-2,2),alpha=0.3)
            def cut(a, b, c):
                return a*a+c*c > 2
            sphinx_plot(P.add_condition(cut,40))

        A sombrero with quadrilaterals::

            sage: P = plot3d(-sin(2*x*x+2*y*y)*exp(-x*x-y*y), (x,-2,2), (y,-2,2),       # needs sage.symbolic
            ....:            color=\'gold\')
            sage: def cut(x, y, z):
            ....:     return x*x+y*y < 1
            sage: Q = P.add_condition(cut);Q                                            # needs sage.symbolic
            Graphics3d Object

        .. PLOT::

            x,y,z = var(\'x,y,z\')
            P = plot3d(-sin(2*x*x+2*y*y)*exp(-x*x-y*y),(x,-2,2),(y,-2,2),color=\'gold\')
            def cut(x, y, z):
                return x*x+y*y < 1
            sphinx_plot(P.add_condition(cut))

        TESTS:

        One test for preservation of transparency :issue:`28783`::

            sage: # needs sage.symbolic
            sage: x,y,z = var(\'x,y,z\')
            sage: P = plot3d(cos(x*y),(x,-2,2),(y,-2,2),color=\'red\',opacity=0.1)
            sage: def condi(x, y, z):
            ....:     return not(x*x+y*y <= 1)
            sage: Q = P.add_condition(condi, 40)
            sage: L = Q.json_repr(Q.default_render_params())
            sage: \'"opacity":0.1\' in L[-1]
            True

        A test that this works with polygons::

            sage: p = polygon3d([[2,0,0], [0,2,0], [0,0,3]])
            sage: def f(x, y, z):
            ....:     return bool(x*x+y*y+z*z<=5)
            sage: cut = p.add_condition(f,60,1.0e-12); cut.face_list()                  # needs sage.symbolic
            [[(0.556128491210302, 0.0, 2.165807263184547),
            (2.0, 0.0, 0.0),
            (0.0, 2.0, 0.0),
            (0.0, 0.556128491210302, 2.165807263184547)]]

        .. TODO::

            - Use a dichotomy to search for the place where to cut,
            - Compute the cut only once for each edge.'''
    @overload
    def bounding_box(self) -> Any:
        """IndexFaceSet.bounding_box(self)

        File: /build/sagemath/src/sage/src/sage/plot/plot3d/index_face_set.pyx (starting at line 891)

        Calculate the bounding box for the vertices in this object
        (ignoring infinite or NaN coordinates).

        OUTPUT:

        a tuple ( (low_x, low_y, low_z), (high_x, high_y, high_z)),
        which gives the coordinates of opposite corners of the
        bounding box.

        EXAMPLES::

            sage: x,y = var('x,y')                                                      # needs sage.symbolic
            sage: p = plot3d(sqrt(sin(x)*sin(y)), (x,0,2*pi), (y,0,2*pi))               # needs sage.symbolic
            sage: p.bounding_box()                                                      # needs sage.symbolic
            ((0.0, 0.0, 0.0), (6.283185307179586, 6.283185307179586, 0.9991889981715697))"""
    @overload
    def bounding_box(self) -> Any:
        """IndexFaceSet.bounding_box(self)

        File: /build/sagemath/src/sage/src/sage/plot/plot3d/index_face_set.pyx (starting at line 891)

        Calculate the bounding box for the vertices in this object
        (ignoring infinite or NaN coordinates).

        OUTPUT:

        a tuple ( (low_x, low_y, low_z), (high_x, high_y, high_z)),
        which gives the coordinates of opposite corners of the
        bounding box.

        EXAMPLES::

            sage: x,y = var('x,y')                                                      # needs sage.symbolic
            sage: p = plot3d(sqrt(sin(x)*sin(y)), (x,0,2*pi), (y,0,2*pi))               # needs sage.symbolic
            sage: p.bounding_box()                                                      # needs sage.symbolic
            ((0.0, 0.0, 0.0), (6.283185307179586, 6.283185307179586, 0.9991889981715697))"""
    @overload
    def dual(self, **kwds) -> Any:
        """IndexFaceSet.dual(self, **kwds)

        File: /build/sagemath/src/sage/src/sage/plot/plot3d/index_face_set.pyx (starting at line 1629)

        Return the dual.

        EXAMPLES::

            sage: S = cube()
            sage: T = S.dual()
            sage: len(T.vertex_list())
            6"""
    @overload
    def dual(self) -> Any:
        """IndexFaceSet.dual(self, **kwds)

        File: /build/sagemath/src/sage/src/sage/plot/plot3d/index_face_set.pyx (starting at line 1629)

        Return the dual.

        EXAMPLES::

            sage: S = cube()
            sage: T = S.dual()
            sage: len(T.vertex_list())
            6"""
    @overload
    def edge_list(self) -> Any:
        """IndexFaceSet.edge_list(self)

        File: /build/sagemath/src/sage/src/sage/plot/plot3d/index_face_set.pyx (starting at line 792)

        Return the list of edges.

        EXAMPLES::

            sage: from sage.plot.plot3d.shapes import *
            sage: S = Box(1,2,3)
            sage: S.edge_list()[0]
            ((1.0, -2.0, 3.0), (1.0, 2.0, 3.0))"""
    @overload
    def edge_list(self) -> Any:
        """IndexFaceSet.edge_list(self)

        File: /build/sagemath/src/sage/src/sage/plot/plot3d/index_face_set.pyx (starting at line 792)

        Return the list of edges.

        EXAMPLES::

            sage: from sage.plot.plot3d.shapes import *
            sage: S = Box(1,2,3)
            sage: S.edge_list()[0]
            ((1.0, -2.0, 3.0), (1.0, 2.0, 3.0))"""
    @overload
    def edges(self) -> Any:
        """IndexFaceSet.edges(self)

        File: /build/sagemath/src/sage/src/sage/plot/plot3d/index_face_set.pyx (starting at line 779)

        An iterator over the edges.

        EXAMPLES::

            sage: from sage.plot.plot3d.shapes import *
            sage: S = Box(1,2,3)
            sage: list(S.edges())[0]
            ((1.0, -2.0, 3.0), (1.0, 2.0, 3.0))"""
    @overload
    def edges(self) -> Any:
        """IndexFaceSet.edges(self)

        File: /build/sagemath/src/sage/src/sage/plot/plot3d/index_face_set.pyx (starting at line 779)

        An iterator over the edges.

        EXAMPLES::

            sage: from sage.plot.plot3d.shapes import *
            sage: S = Box(1,2,3)
            sage: list(S.edges())[0]
            ((1.0, -2.0, 3.0), (1.0, 2.0, 3.0))"""
    def face_list(self, render_params=...) -> Any:
        """IndexFaceSet.face_list(self, render_params=None)

        File: /build/sagemath/src/sage/src/sage/plot/plot3d/index_face_set.pyx (starting at line 746)

        Return the list of faces.

        Every face is given as a tuple of vertices.

        EXAMPLES::

            sage: from sage.plot.plot3d.shapes import *
            sage: S = Box(1,2,3)
            sage: S.face_list(S.default_render_params())[0]
            [(1.0, 2.0, 3.0), (-1.0, 2.0, 3.0), (-1.0, -2.0, 3.0), (1.0, -2.0, 3.0)]"""
    @overload
    def faces(self) -> Any:
        """IndexFaceSet.faces(self)

        File: /build/sagemath/src/sage/src/sage/plot/plot3d/index_face_set.pyx (starting at line 733)

        An iterator over the faces.

        EXAMPLES::

            sage: from sage.plot.plot3d.shapes import *
            sage: S = Box(1,2,3)
            sage: list(S.faces()) == S.face_list()
            True"""
    @overload
    def faces(self) -> Any:
        """IndexFaceSet.faces(self)

        File: /build/sagemath/src/sage/src/sage/plot/plot3d/index_face_set.pyx (starting at line 733)

        An iterator over the faces.

        EXAMPLES::

            sage: from sage.plot.plot3d.shapes import *
            sage: S = Box(1,2,3)
            sage: list(S.faces()) == S.face_list()
            True"""
    @overload
    def has_local_colors(self) -> bool:
        """IndexFaceSet.has_local_colors(self) -> bool

        File: /build/sagemath/src/sage/src/sage/plot/plot3d/index_face_set.pyx (starting at line 664)

        Return ``True`` if and only if every face has an individual color.

        EXAMPLES::

            sage: from sage.plot.plot3d.index_face_set import IndexFaceSet
            sage: from sage.plot.plot3d.texture import Texture
            sage: point_list = [(2,0,0),(0,2,0),(0,0,2),(0,1,1),(1,0,1),(1,1,0)]
            sage: face_list = [[0,4,5],[3,4,5],[2,3,4],[1,3,5]]
            sage: col = rainbow(10, 'rgbtuple')
            sage: t_list=[Texture(col[i]) for i in range(10)]
            sage: S = IndexFaceSet(face_list, point_list, texture_list=t_list)
            sage: S.has_local_colors()
            True

            sage: from sage.plot.plot3d.shapes import *
            sage: S = Box(1,2,3)
            sage: S.has_local_colors()
            False"""
    @overload
    def has_local_colors(self) -> Any:
        """IndexFaceSet.has_local_colors(self) -> bool

        File: /build/sagemath/src/sage/src/sage/plot/plot3d/index_face_set.pyx (starting at line 664)

        Return ``True`` if and only if every face has an individual color.

        EXAMPLES::

            sage: from sage.plot.plot3d.index_face_set import IndexFaceSet
            sage: from sage.plot.plot3d.texture import Texture
            sage: point_list = [(2,0,0),(0,2,0),(0,0,2),(0,1,1),(1,0,1),(1,1,0)]
            sage: face_list = [[0,4,5],[3,4,5],[2,3,4],[1,3,5]]
            sage: col = rainbow(10, 'rgbtuple')
            sage: t_list=[Texture(col[i]) for i in range(10)]
            sage: S = IndexFaceSet(face_list, point_list, texture_list=t_list)
            sage: S.has_local_colors()
            True

            sage: from sage.plot.plot3d.shapes import *
            sage: S = Box(1,2,3)
            sage: S.has_local_colors()
            False"""
    @overload
    def has_local_colors(self) -> Any:
        """IndexFaceSet.has_local_colors(self) -> bool

        File: /build/sagemath/src/sage/src/sage/plot/plot3d/index_face_set.pyx (starting at line 664)

        Return ``True`` if and only if every face has an individual color.

        EXAMPLES::

            sage: from sage.plot.plot3d.index_face_set import IndexFaceSet
            sage: from sage.plot.plot3d.texture import Texture
            sage: point_list = [(2,0,0),(0,2,0),(0,0,2),(0,1,1),(1,0,1),(1,1,0)]
            sage: face_list = [[0,4,5],[3,4,5],[2,3,4],[1,3,5]]
            sage: col = rainbow(10, 'rgbtuple')
            sage: t_list=[Texture(col[i]) for i in range(10)]
            sage: S = IndexFaceSet(face_list, point_list, texture_list=t_list)
            sage: S.has_local_colors()
            True

            sage: from sage.plot.plot3d.shapes import *
            sage: S = Box(1,2,3)
            sage: S.has_local_colors()
            False"""
    @overload
    def index_faces(self) -> Any:
        """IndexFaceSet.index_faces(self)

        File: /build/sagemath/src/sage/src/sage/plot/plot3d/index_face_set.pyx (starting at line 643)

        Return the list over all faces of the indices of the vertices.

        EXAMPLES::

            sage: from sage.plot.plot3d.shapes import *
            sage: S = Box(1,2,3)
            sage: S.index_faces()
            [[0, 1, 2, 3],
             [0, 4, 5, 1],
             [0, 3, 6, 4],
             [5, 4, 6, 7],
             [6, 3, 2, 7],
             [2, 1, 5, 7]]"""
    @overload
    def index_faces(self) -> Any:
        """IndexFaceSet.index_faces(self)

        File: /build/sagemath/src/sage/src/sage/plot/plot3d/index_face_set.pyx (starting at line 643)

        Return the list over all faces of the indices of the vertices.

        EXAMPLES::

            sage: from sage.plot.plot3d.shapes import *
            sage: S = Box(1,2,3)
            sage: S.index_faces()
            [[0, 1, 2, 3],
             [0, 4, 5, 1],
             [0, 3, 6, 4],
             [5, 4, 6, 7],
             [6, 3, 2, 7],
             [2, 1, 5, 7]]"""
    @overload
    def index_faces_with_colors(self) -> Any:
        """IndexFaceSet.index_faces_with_colors(self)

        File: /build/sagemath/src/sage/src/sage/plot/plot3d/index_face_set.pyx (starting at line 687)

        Return the list over all faces of (indices of the vertices, color).

        This only works if every face has its own color.

        .. SEEALSO::

            :meth:`has_local_colors`

        EXAMPLES:

        A simple colored one::

            sage: from sage.plot.plot3d.index_face_set import IndexFaceSet
            sage: from sage.plot.plot3d.texture import Texture
            sage: point_list = [(2,0,0),(0,2,0),(0,0,2),(0,1,1),(1,0,1),(1,1,0)]
            sage: face_list = [[0,4,5],[3,4,5],[2,3,4],[1,3,5]]
            sage: col = rainbow(10, 'rgbtuple')
            sage: t_list = [Texture(col[i]) for i in range(10)]
            sage: S = IndexFaceSet(face_list, point_list, texture_list=t_list)
            sage: S.index_faces_with_colors()
            [([0, 4, 5], '#ff0000'),
             ([3, 4, 5], '#ff9900'),
             ([2, 3, 4], '#cbff00'),
             ([1, 3, 5], '#33ff00')]

        When the texture is global, an error is raised::

            sage: from sage.plot.plot3d.shapes import *
            sage: S = Box(1,2,3)
            sage: S.index_faces_with_colors()
            Traceback (most recent call last):
            ...
            ValueError: the texture is global"""
    @overload
    def index_faces_with_colors(self) -> Any:
        """IndexFaceSet.index_faces_with_colors(self)

        File: /build/sagemath/src/sage/src/sage/plot/plot3d/index_face_set.pyx (starting at line 687)

        Return the list over all faces of (indices of the vertices, color).

        This only works if every face has its own color.

        .. SEEALSO::

            :meth:`has_local_colors`

        EXAMPLES:

        A simple colored one::

            sage: from sage.plot.plot3d.index_face_set import IndexFaceSet
            sage: from sage.plot.plot3d.texture import Texture
            sage: point_list = [(2,0,0),(0,2,0),(0,0,2),(0,1,1),(1,0,1),(1,1,0)]
            sage: face_list = [[0,4,5],[3,4,5],[2,3,4],[1,3,5]]
            sage: col = rainbow(10, 'rgbtuple')
            sage: t_list = [Texture(col[i]) for i in range(10)]
            sage: S = IndexFaceSet(face_list, point_list, texture_list=t_list)
            sage: S.index_faces_with_colors()
            [([0, 4, 5], '#ff0000'),
             ([3, 4, 5], '#ff9900'),
             ([2, 3, 4], '#cbff00'),
             ([1, 3, 5], '#33ff00')]

        When the texture is global, an error is raised::

            sage: from sage.plot.plot3d.shapes import *
            sage: S = Box(1,2,3)
            sage: S.index_faces_with_colors()
            Traceback (most recent call last):
            ...
            ValueError: the texture is global"""
    @overload
    def index_faces_with_colors(self) -> Any:
        """IndexFaceSet.index_faces_with_colors(self)

        File: /build/sagemath/src/sage/src/sage/plot/plot3d/index_face_set.pyx (starting at line 687)

        Return the list over all faces of (indices of the vertices, color).

        This only works if every face has its own color.

        .. SEEALSO::

            :meth:`has_local_colors`

        EXAMPLES:

        A simple colored one::

            sage: from sage.plot.plot3d.index_face_set import IndexFaceSet
            sage: from sage.plot.plot3d.texture import Texture
            sage: point_list = [(2,0,0),(0,2,0),(0,0,2),(0,1,1),(1,0,1),(1,1,0)]
            sage: face_list = [[0,4,5],[3,4,5],[2,3,4],[1,3,5]]
            sage: col = rainbow(10, 'rgbtuple')
            sage: t_list = [Texture(col[i]) for i in range(10)]
            sage: S = IndexFaceSet(face_list, point_list, texture_list=t_list)
            sage: S.index_faces_with_colors()
            [([0, 4, 5], '#ff0000'),
             ([3, 4, 5], '#ff9900'),
             ([2, 3, 4], '#cbff00'),
             ([1, 3, 5], '#33ff00')]

        When the texture is global, an error is raised::

            sage: from sage.plot.plot3d.shapes import *
            sage: S = Box(1,2,3)
            sage: S.index_faces_with_colors()
            Traceback (most recent call last):
            ...
            ValueError: the texture is global"""
    @overload
    def is_enclosed(self) -> Any:
        """IndexFaceSet.is_enclosed(self)

        File: /build/sagemath/src/sage/src/sage/plot/plot3d/index_face_set.pyx (starting at line 623)

        Whether or not it is necessary to render the back sides of the polygons.

        One is assuming, of course, that they have the correct orientation.

        This is may be passed in on construction. It is also
        calculated in
        :class:`sage.plot.plot3d.parametric_surface.ParametricSurface`
        by verifying the opposite edges of the rendered domain either
        line up or are pinched together.

        EXAMPLES::

            sage: from sage.plot.plot3d.index_face_set import IndexFaceSet
            sage: IndexFaceSet([[(0,0,1),(0,1,0),(1,0,0)]]).is_enclosed()
            False"""
    @overload
    def is_enclosed(self) -> Any:
        """IndexFaceSet.is_enclosed(self)

        File: /build/sagemath/src/sage/src/sage/plot/plot3d/index_face_set.pyx (starting at line 623)

        Whether or not it is necessary to render the back sides of the polygons.

        One is assuming, of course, that they have the correct orientation.

        This is may be passed in on construction. It is also
        calculated in
        :class:`sage.plot.plot3d.parametric_surface.ParametricSurface`
        by verifying the opposite edges of the rendered domain either
        line up or are pinched together.

        EXAMPLES::

            sage: from sage.plot.plot3d.index_face_set import IndexFaceSet
            sage: IndexFaceSet([[(0,0,1),(0,1,0),(1,0,0)]]).is_enclosed()
            False"""
    def jmol_repr(self, render_params) -> Any:
        """IndexFaceSet.jmol_repr(self, render_params)

        File: /build/sagemath/src/sage/src/sage/plot/plot3d/index_face_set.pyx (starting at line 1502)

        Return a jmol representation for ``self``.

        TESTS::

            sage: from sage.plot.plot3d.shapes import *
            sage: S = Cylinder(1,1)
            sage: S.show(viewer='jmol')   # indirect doctest"""
    def json_repr(self, render_params) -> Any:
        '''IndexFaceSet.json_repr(self, render_params)

        File: /build/sagemath/src/sage/src/sage/plot/plot3d/index_face_set.pyx (starting at line 1266)

        Return a json representation for ``self``.

        TESTS:

        A basic test with a triangle::

            sage: G = polygon([(0,0,1), (1,1,1), (2,0,1)])
            sage: G.json_repr(G.default_render_params())
            [\'{"vertices":[{"x":0,"y":0,"z":1},{"x":1,"y":1,"z":1},{"x":2,"y":0,"z":1}], "faces":[[0,1,2]], "color":"#0000ff", "opacity":1.0}\']

        A simple colored one::

            sage: from sage.plot.plot3d.index_face_set import IndexFaceSet
            sage: from sage.plot.plot3d.texture import Texture
            sage: point_list = [(2,0,0),(0,2,0),(0,0,2),(0,1,1),(1,0,1),(1,1,0)]
            sage: face_list = [[0,4,5],[3,4,5],[2,3,4],[1,3,5]]
            sage: col = rainbow(10, \'rgbtuple\')
            sage: t_list=[Texture(col[i]) for i in range(10)]
            sage: S = IndexFaceSet(face_list, point_list, texture_list=t_list)
            sage: S.json_repr(S.default_render_params())
            [\'{"vertices":[{"x":2,"y":0,"z":0},..., "faceColors":["#ff0000","#ff9900","#cbff00","#33ff00"], "opacity":1.0}\']'''
    def obj_repr(self, render_params) -> Any:
        """IndexFaceSet.obj_repr(self, render_params)

        File: /build/sagemath/src/sage/src/sage/plot/plot3d/index_face_set.pyx (starting at line 1463)

        Return an obj representation for ``self``.

        TESTS::

            sage: from sage.plot.plot3d.shapes import *
            sage: S = Cylinder(1,1)
            sage: s = S.obj_repr(S.default_render_params())"""
    def partition(self, f) -> Any:
        """IndexFaceSet.partition(self, f)

        File: /build/sagemath/src/sage/src/sage/plot/plot3d/index_face_set.pyx (starting at line 924)

        Partition the faces of ``self``.

        The partition is done according to the value of a map
        `f: \\RR^3 \\rightarrow \\ZZ` applied to the center of each face.

        INPUT:

        - ``f`` -- a function from `\\RR^3` to `\\ZZ`

        EXAMPLES::

            sage: from sage.plot.plot3d.shapes import *
            sage: S = Box(1,2,3)
            sage: len(S.partition(lambda x,y,z: floor(x+y+z)))
            6"""
    def sticker(self, face_list, width, hover, **kwds) -> Any:
        """IndexFaceSet.sticker(self, face_list, width, hover, **kwds)

        File: /build/sagemath/src/sage/src/sage/plot/plot3d/index_face_set.pyx (starting at line 1730)

        Return a sticker on the chosen faces."""
    def stickers(self, colors, width, hover) -> Any:
        """IndexFaceSet.stickers(self, colors, width, hover)

        File: /build/sagemath/src/sage/src/sage/plot/plot3d/index_face_set.pyx (starting at line 1696)

        Return a group of IndexFaceSets.

        INPUT:

        - ``colors`` -- list of colors/textures to use (in cyclic order)

        - ``width`` -- offset perpendicular into the edge (to create a border)
          may also be negative

        - ``hover`` -- offset normal to the face (usually have to float above
          the original surface so it shows, typically this value is very
          small compared to the actual object

        OUTPUT: Graphics3dGroup of stickers

        EXAMPLES::

            sage: from sage.plot.plot3d.shapes import Box
            sage: B = Box(.5,.4,.3, color='black')
            sage: S = B.stickers(['red','yellow','blue'], 0.1, 0.05)
            sage: S.show()
            sage: (S+B).show()"""
    def stl_binary_repr(self, render_params) -> Any:
        """IndexFaceSet.stl_binary_repr(self, render_params)

        File: /build/sagemath/src/sage/src/sage/plot/plot3d/index_face_set.pyx (starting at line 1577)

        Return data for STL (STereoLithography) representation of the surface.

        The STL binary representation is a list of binary strings,
        one for each triangle.

        EXAMPLES::

            sage: G = sphere()
            sage: data = G.stl_binary_repr(G.default_render_params()); len(data)
            1368"""
    def tachyon_repr(self, render_params) -> Any:
        """IndexFaceSet.tachyon_repr(self, render_params)

        File: /build/sagemath/src/sage/src/sage/plot/plot3d/index_face_set.pyx (starting at line 1204)

        Return a tachyon object for ``self``.

        EXAMPLES:

        A basic test with a triangle::

            sage: G = polygon([(0,0,1), (1,1,1), (2,0,1)])
            sage: s = G.tachyon_repr(G.default_render_params()); s
            ['TRI V0 0 0 1 V1 1 1 1 V2 2 0 1', ...]

        A simple colored one::

            sage: from sage.plot.plot3d.index_face_set import IndexFaceSet
            sage: from sage.plot.plot3d.texture import Texture
            sage: point_list = [(2,0,0),(0,2,0),(0,0,2),(0,1,1),(1,0,1),(1,1,0)]
            sage: face_list = [[0,4,5],[3,4,5],[2,3,4],[1,3,5]]
            sage: col = rainbow(10, 'rgbtuple')
            sage: t_list = [Texture(col[i]) for i in range(10)]
            sage: S = IndexFaceSet(face_list, point_list, texture_list=t_list)
            sage: S.tachyon_repr(S.default_render_params())
            ['TRI V0 2 0 0 V1 1 0 1 V2 1 1 0',
            'TEXTURE... AMBIENT 0.3 DIFFUSE 0.7 SPECULAR 0 OPACITY 1.0... COLOR 1 0 0 ... TEXFUNC 0',...]"""
    def threejs_repr(self, render_params) -> Any:
        """IndexFaceSet.threejs_repr(self, render_params)

        File: /build/sagemath/src/sage/src/sage/plot/plot3d/index_face_set.pyx (starting at line 1338)

        Return representation of the surface suitable for plotting with three.js.

        EXAMPLES:

        A simple triangle::

            sage: G = polygon([(0,0,1), (1,1,1), (2,0,1)])
            sage: G.threejs_repr(G.default_render_params())
            [('surface',
              {'color': '#0000ff',
               'faces': [[0, 1, 2]],
               'opacity': 1.0,
               'vertices': [{'x': 0.0, 'y': 0.0, 'z': 1.0},
                {'x': 1.0, 'y': 1.0, 'z': 1.0},
                {'x': 2.0, 'y': 0.0, 'z': 1.0}]})]

        The same but with more options applied::

            sage: G = polygon([(0,0,1), (1,1,1), (2,0,1)], color='red', opacity=0.5,
            ....:             render_order=2, threejs_flat_shading=True,
            ....:             single_side=True, mesh=True, thickness=10, depth_write=True)
            sage: G.threejs_repr(G.default_render_params())
            [('surface',
              {'color': '#ff0000',
               'depthWrite': True,
               'faces': [[0, 1, 2]],
               'linewidth': 10.0,
               'opacity': 0.5,
               'renderOrder': 2.0,
               'showMeshGrid': True,
               'singleSide': True,
               'useFlatShading': True,
               'vertices': [{'x': 0.0, 'y': 0.0, 'z': 1.0},
                {'x': 1.0, 'y': 1.0, 'z': 1.0},
                {'x': 2.0, 'y': 0.0, 'z': 1.0}]})]

        TESTS:

        Transformations apply to the surface's vertices::

            sage: G = polygon([(0,0,1), (1,1,1), (2,0,1)]).scale(2,1,-1)
            sage: G.threejs_repr(G.default_render_params())
            [('surface',
              {'color': '#0000ff',
               'faces': [[0, 1, 2]],
               'opacity': 1.0,
               'vertices': [{'x': 0.0, 'y': 0.0, 'z': -1.0},
                {'x': 2.0, 'y': 1.0, 'z': -1.0},
                {'x': 4.0, 'y': 0.0, 'z': -1.0}]})]

        Per-face colors::

            sage: from sage.plot.plot3d.index_face_set import IndexFaceSet
            sage: from sage.plot.plot3d.texture import Texture
            sage: point_list = [(2,0,0),(0,2,0),(0,0,2),(0,1,1),(1,0,1),(1,1,0)]
            sage: face_list = [[0,4,5],[3,4,5],[2,3,4],[1,3,5]]
            sage: col = rainbow(10, 'rgbtuple')
            sage: t_list=[Texture(col[i]) for i in range(10)]
            sage: S = IndexFaceSet(face_list, point_list, texture_list=t_list)
            sage: S.threejs_repr(S.default_render_params())
            [('surface',
              {'faceColors': ['#ff0000', '#ff9900', '#cbff00', '#33ff00'],
               'faces': [[0, 4, 5], [3, 4, 5], [2, 3, 4], [1, 3, 5]],
               'opacity': 1.0,
               'vertices': [{'x': 2.0, 'y': 0.0, 'z': 0.0},
                {'x': 0.0, 'y': 2.0, 'z': 0.0},
                {'x': 0.0, 'y': 0.0, 'z': 2.0},
                {'x': 0.0, 'y': 1.0, 'z': 1.0},
                {'x': 1.0, 'y': 0.0, 'z': 1.0},
                {'x': 1.0, 'y': 1.0, 'z': 0.0}]})]"""
    @overload
    def vertex_list(self) -> Any:
        """IndexFaceSet.vertex_list(self)

        File: /build/sagemath/src/sage/src/sage/plot/plot3d/index_face_set.pyx (starting at line 818)

        Return the list of vertices.

        EXAMPLES::

            sage: from sage.plot.plot3d.shapes import *
            sage: S = polygon([(0,0,1), (1,1,1), (2,0,1)])
            sage: S.vertex_list()[0]
            (0.0, 0.0, 1.0)"""
    @overload
    def vertex_list(self) -> Any:
        """IndexFaceSet.vertex_list(self)

        File: /build/sagemath/src/sage/src/sage/plot/plot3d/index_face_set.pyx (starting at line 818)

        Return the list of vertices.

        EXAMPLES::

            sage: from sage.plot.plot3d.shapes import *
            sage: S = polygon([(0,0,1), (1,1,1), (2,0,1)])
            sage: S.vertex_list()[0]
            (0.0, 0.0, 1.0)"""
    @overload
    def vertices(self) -> Any:
        """IndexFaceSet.vertices(self)

        File: /build/sagemath/src/sage/src/sage/plot/plot3d/index_face_set.pyx (starting at line 805)

        An iterator over the vertices.

        EXAMPLES::

            sage: from sage.plot.plot3d.shapes import *
            sage: S = Cone(1,1)
            sage: list(S.vertices()) == S.vertex_list()
            True"""
    @overload
    def vertices(self) -> Any:
        """IndexFaceSet.vertices(self)

        File: /build/sagemath/src/sage/src/sage/plot/plot3d/index_face_set.pyx (starting at line 805)

        An iterator over the vertices.

        EXAMPLES::

            sage: from sage.plot.plot3d.shapes import *
            sage: S = Cone(1,1)
            sage: list(S.vertices()) == S.vertex_list()
            True"""
    @overload
    def x3d_geometry(self) -> Any:
        """IndexFaceSet.x3d_geometry(self)

        File: /build/sagemath/src/sage/src/sage/plot/plot3d/index_face_set.pyx (starting at line 832)

        Return the x3d data.

        EXAMPLES:

        A basic test with a triangle::

            sage: G = polygon([(0,0,1), (1,1,1), (2,0,1)])
            sage: print(G.x3d_geometry())
            <BLANKLINE>
            <IndexedFaceSet coordIndex='0,1,2,-1'>
              <Coordinate point='0.0 0.0 1.0,1.0 1.0 1.0,2.0 0.0 1.0'/>
            </IndexedFaceSet>
            <BLANKLINE>

        A simple colored one::

            sage: from sage.plot.plot3d.index_face_set import IndexFaceSet
            sage: from sage.plot.plot3d.texture import Texture
            sage: point_list = [(2,0,0),(0,2,0),(0,0,2),(0,1,1),(1,0,1),(1,1,0)]
            sage: face_list = [[0,4,5],[3,4,5],[2,3,4],[1,3,5]]
            sage: col = rainbow(10, 'rgbtuple')
            sage: t_list = [Texture(col[i]) for i in range(10)]
            sage: S = IndexFaceSet(face_list, point_list, texture_list=t_list)
            sage: print(S.x3d_geometry())
            <BLANKLINE>
            <IndexedFaceSet solid='False' colorPerVertex='False' coordIndex='0,4,5,-1,3,4,5,-1,2,3,4,-1,1,3,5,-1'>
              <Coordinate point='2.0 0.0 0.0,0.0 2.0 0.0,0.0 0.0 2.0,0.0 1.0 1.0,1.0 0.0 1.0,1.0 1.0 0.0'/>
              <Color color='1.0 0.0 0.0,1.0 0.6000000000000001 0.0,0.7999999999999998 1.0 0.0,0.20000000000000018 1.0 0.0' />
            </IndexedFaceSet>
            <BLANKLINE>"""
    @overload
    def x3d_geometry(self) -> Any:
        """IndexFaceSet.x3d_geometry(self)

        File: /build/sagemath/src/sage/src/sage/plot/plot3d/index_face_set.pyx (starting at line 832)

        Return the x3d data.

        EXAMPLES:

        A basic test with a triangle::

            sage: G = polygon([(0,0,1), (1,1,1), (2,0,1)])
            sage: print(G.x3d_geometry())
            <BLANKLINE>
            <IndexedFaceSet coordIndex='0,1,2,-1'>
              <Coordinate point='0.0 0.0 1.0,1.0 1.0 1.0,2.0 0.0 1.0'/>
            </IndexedFaceSet>
            <BLANKLINE>

        A simple colored one::

            sage: from sage.plot.plot3d.index_face_set import IndexFaceSet
            sage: from sage.plot.plot3d.texture import Texture
            sage: point_list = [(2,0,0),(0,2,0),(0,0,2),(0,1,1),(1,0,1),(1,1,0)]
            sage: face_list = [[0,4,5],[3,4,5],[2,3,4],[1,3,5]]
            sage: col = rainbow(10, 'rgbtuple')
            sage: t_list = [Texture(col[i]) for i in range(10)]
            sage: S = IndexFaceSet(face_list, point_list, texture_list=t_list)
            sage: print(S.x3d_geometry())
            <BLANKLINE>
            <IndexedFaceSet solid='False' colorPerVertex='False' coordIndex='0,4,5,-1,3,4,5,-1,2,3,4,-1,1,3,5,-1'>
              <Coordinate point='2.0 0.0 0.0,0.0 2.0 0.0,0.0 0.0 2.0,0.0 1.0 1.0,1.0 0.0 1.0,1.0 1.0 0.0'/>
              <Color color='1.0 0.0 0.0,1.0 0.6000000000000001 0.0,0.7999999999999998 1.0 0.0,0.20000000000000018 1.0 0.0' />
            </IndexedFaceSet>
            <BLANKLINE>"""
    @overload
    def x3d_geometry(self) -> Any:
        """IndexFaceSet.x3d_geometry(self)

        File: /build/sagemath/src/sage/src/sage/plot/plot3d/index_face_set.pyx (starting at line 832)

        Return the x3d data.

        EXAMPLES:

        A basic test with a triangle::

            sage: G = polygon([(0,0,1), (1,1,1), (2,0,1)])
            sage: print(G.x3d_geometry())
            <BLANKLINE>
            <IndexedFaceSet coordIndex='0,1,2,-1'>
              <Coordinate point='0.0 0.0 1.0,1.0 1.0 1.0,2.0 0.0 1.0'/>
            </IndexedFaceSet>
            <BLANKLINE>

        A simple colored one::

            sage: from sage.plot.plot3d.index_face_set import IndexFaceSet
            sage: from sage.plot.plot3d.texture import Texture
            sage: point_list = [(2,0,0),(0,2,0),(0,0,2),(0,1,1),(1,0,1),(1,1,0)]
            sage: face_list = [[0,4,5],[3,4,5],[2,3,4],[1,3,5]]
            sage: col = rainbow(10, 'rgbtuple')
            sage: t_list = [Texture(col[i]) for i in range(10)]
            sage: S = IndexFaceSet(face_list, point_list, texture_list=t_list)
            sage: print(S.x3d_geometry())
            <BLANKLINE>
            <IndexedFaceSet solid='False' colorPerVertex='False' coordIndex='0,4,5,-1,3,4,5,-1,2,3,4,-1,1,3,5,-1'>
              <Coordinate point='2.0 0.0 0.0,0.0 2.0 0.0,0.0 0.0 2.0,0.0 1.0 1.0,1.0 0.0 1.0,1.0 1.0 0.0'/>
              <Color color='1.0 0.0 0.0,1.0 0.6000000000000001 0.0,0.7999999999999998 1.0 0.0,0.20000000000000018 1.0 0.0' />
            </IndexedFaceSet>
            <BLANKLINE>"""

class VertexIter:
    """VertexIter(face_set)

    File: /build/sagemath/src/sage/src/sage/plot/plot3d/index_face_set.pyx (starting at line 1825)

    A class for iteration over vertices

    EXAMPLES::

        sage: from sage.plot.plot3d.shapes import *
        sage: S = Box(1,2,3)
        sage: len(list(S.vertices())) == 8   # indirect doctest
        True"""
    def __init__(self, face_set) -> Any:
        """File: /build/sagemath/src/sage/src/sage/plot/plot3d/index_face_set.pyx (starting at line 1836)"""
    def __iter__(self) -> Any:
        """VertexIter.__iter__(self)

        File: /build/sagemath/src/sage/src/sage/plot/plot3d/index_face_set.pyx (starting at line 1840)"""
    def __next__(self) -> Any:
        """VertexIter.__next__(self)

        File: /build/sagemath/src/sage/src/sage/plot/plot3d/index_face_set.pyx (starting at line 1843)"""
