import _cython_3_2_1
import sage.plot.plot3d.index_face_set
from sage.categories.category import RDF as RDF
from sage.plot.colors import check_color_data as check_color_data
from sage.plot.misc import setup_for_eval_on_grid as setup_for_eval_on_grid
from typing import Any, ClassVar, overload

DEFAULT_PLOT_POINTS: int
render_implicit: _cython_3_2_1.cython_function_or_method
triangle_table2: tuple

class ImplicitSurface(sage.plot.plot3d.index_face_set.IndexFaceSet):
    """ImplicitSurface(f, xrange, yrange, zrange, contour=0, plot_points='automatic', region=None, smooth=True, gradient=None, **kwds)"""
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    color_function: File
    colormap: File
    contours: File
    f: File
    gradient: File
    plot_points: File
    region: File
    smooth: File
    vars: File
    xrange: File
    yrange: File
    zrange: File
    def __init__(self, f, xrange, yrange, zrange, contour=..., plot_points=..., region=..., smooth=..., gradient=..., **kwds) -> Any:
        """File: /build/sagemath/src/sage/src/sage/plot/plot3d/implicit_surface.pyx (starting at line 949)

                TESTS::

                    sage: from sage.plot.plot3d.implicit_surface import ImplicitSurface
                    sage: var('x,y,z')
                    (x, y, z)
                    sage: G = ImplicitSurface(x^2 + y^2 + z^2, (x,-2, 2), (y,-2, 2), (z,-2, 2), contour=4)
                    sage: show(G)

                A colored case::

                    sage: t = (1-sin(2*x*y+3*z)**2).function(x,y,z)
                    sage: cm = colormaps.autumn
                    sage: G = ImplicitSurface(x^2 + y^2 + z^2, (x,-2, 2), (y,-2, 2), (z,-2, 2), contour=4, color=(t,cm))
                    sage: G.show(viewer='tachyon')
        """
    @overload
    def bounding_box(self) -> Any:
        """ImplicitSurface.bounding_box(self)

        File: /build/sagemath/src/sage/src/sage/plot/plot3d/implicit_surface.pyx (starting at line 1051)

        Return a bounding box for the ``ImplicitSurface``, as a tuple of two
        3-dimensional points.

        EXAMPLES:

        Note that the bounding box corresponds exactly to the x-, y-, and z- range::

            sage: from sage.plot.plot3d.implicit_surface import ImplicitSurface
            sage: G = ImplicitSurface(0, (0, 1), (0, 1), (0, 1))
            sage: G.bounding_box()
            ((0.0, 0.0, 0.0), (1.0, 1.0, 1.0))"""
    @overload
    def bounding_box(self) -> Any:
        """ImplicitSurface.bounding_box(self)

        File: /build/sagemath/src/sage/src/sage/plot/plot3d/implicit_surface.pyx (starting at line 1051)

        Return a bounding box for the ``ImplicitSurface``, as a tuple of two
        3-dimensional points.

        EXAMPLES:

        Note that the bounding box corresponds exactly to the x-, y-, and z- range::

            sage: from sage.plot.plot3d.implicit_surface import ImplicitSurface
            sage: G = ImplicitSurface(0, (0, 1), (0, 1), (0, 1))
            sage: G.bounding_box()
            ((0.0, 0.0, 0.0), (1.0, 1.0, 1.0))"""
    def jmol_repr(self, render_params) -> Any:
        """ImplicitSurface.jmol_repr(self, render_params)

        File: /build/sagemath/src/sage/src/sage/plot/plot3d/implicit_surface.pyx (starting at line 1123)

        Return a representation of this object suitable for use with the Jmol
        renderer.

        TESTS::

            sage: from sage.plot.plot3d.implicit_surface import ImplicitSurface
            sage: var('x,y,z')
            (x, y, z)
            sage: G = ImplicitSurface(x + y + z, (x,-1, 1), (y,-1, 1), (z,-1, 1))
            sage: show(G, viewer='jmol')   # indirect doctest"""
    def json_repr(self, render_params) -> Any:
        '''ImplicitSurface.json_repr(self, render_params)

        File: /build/sagemath/src/sage/src/sage/plot/plot3d/implicit_surface.pyx (starting at line 1139)

        Return a representation of this object in JavaScript Object Notation (JSON).

        TESTS::

            sage: from sage.plot.plot3d.implicit_surface import ImplicitSurface
            sage: var(\'x,y,z\')
            (x, y, z)
            sage: G = ImplicitSurface(x + y + z, (x,-1, 1), (y,-1, 1), (z,-1, 1))
            sage: G.json_repr(G.default_render_params())[0].startswith(\'{"vertices":\')
            True'''
    def obj_repr(self, render_params) -> Any:
        """ImplicitSurface.obj_repr(self, render_params)

        File: /build/sagemath/src/sage/src/sage/plot/plot3d/implicit_surface.pyx (starting at line 1068)

        Return a representation of this object in the .obj format.

        TESTS:

        We graph a simple plane::

            sage: from sage.plot.plot3d.implicit_surface import ImplicitSurface
            sage: var('x,y,z')
            (x, y, z)
            sage: G = ImplicitSurface(x + y + z, (x,-1, 1), (y,-1, 1), (z,-1, 1))
            sage: obj = G.obj_repr(G.default_render_params())
            sage: vertices = obj[2]

        The number of vertices in the OBJ representation should equal the number
        of vertices in the face set::

            sage: len(vertices) == len(G.vertex_list())
            True

        The vertices in the OBJ representation should also be approximately equal
        to the vertices in the face set -- the small error is due to rounding
        which occurs during output (we test only the first 20 points for the
        sake of speed)::

            sage: def points_equal(a, b, epsilon=(1e-5)):
            ....:     return all(abs(x0-x1) < epsilon for x0, x1 in zip(a, b))
            sage: checklist = []
            sage: assert len(vertices) >= 20 # I should hope so, we're rendering at the default resolution!
            sage: for vertex, surf_vertex in list(zip(vertices, G.vertex_list()))[0:20]:
            ....:     checklist.append(points_equal(map(float, vertex.split(' ')[1:]), surf_vertex))
            sage: all(checklist)
            True"""
    def tachyon_repr(self, render_params) -> Any:
        """ImplicitSurface.tachyon_repr(self, render_params)

        File: /build/sagemath/src/sage/src/sage/plot/plot3d/implicit_surface.pyx (starting at line 1106)

        Return a representation of this object suitable for use with the Tachyon
        renderer.

        TESTS::

            sage: from sage.plot.plot3d.implicit_surface import ImplicitSurface
            sage: var('x,y,z')
            (x, y, z)
            sage: G = ImplicitSurface(x + y + z, (x,-1, 1), (y,-1, 1), (z,-1, 1))
            sage: G.tachyon_repr(G.default_render_params())[0].startswith('TRI')
            True"""
    def threejs_repr(self, render_params) -> Any:
        """ImplicitSurface.threejs_repr(self, render_params)

        File: /build/sagemath/src/sage/src/sage/plot/plot3d/implicit_surface.pyx (starting at line 1155)

        Return a representation of the surface suitable for plotting with three.js.

        EXAMPLES::

            sage: from sage.plot.plot3d.implicit_surface import ImplicitSurface
            sage: _ = var('x,y,z')
            sage: G = ImplicitSurface(x + y + z, (x,-1, 1), (y,-1, 1), (z,-1, 1))
            sage: G.threejs_repr(G.default_render_params())
            [('surface',
              {'color': '#6666ff',
               'faces': [[0, 1, 2],
                ...
               'opacity': 1.0,
               'vertices': [{'x': ...,
                 'y': -0.9743589743589...,
                 'z': -0.02564102564102...},
                ...
                {'x': -1.0, 'y': 0.9487179487179..., 'z': 0.05128205128205...}]})]"""
    @overload
    def triangulate(self, force=...) -> Any:
        """ImplicitSurface.triangulate(self, force=False)

        File: /build/sagemath/src/sage/src/sage/plot/plot3d/implicit_surface.pyx (starting at line 1179)

        The IndexFaceSet will be empty until you call this method,
        which generates the faces and vertices according to the
        parameters specified in the constructor for ImplicitSurface.

        Note that if you call this method more than once, subsequent
        invocations will have no effect (this is an optimization to
        avoid repeated work) unless you specify ``force=True`` in the
        keywords.

        EXAMPLES::

            sage: from sage.plot.plot3d.implicit_surface import ImplicitSurface
            sage: var('x,y,z')
            (x, y, z)
            sage: G = ImplicitSurface(x + y + z, (x,-1, 1), (y,-1, 1), (z,-1, 1))
            sage: len(G.vertex_list()), len(G.face_list())
            (0, 0)
            sage: G.triangulate()
            sage: len(G.vertex_list()) > 0, len(G.face_list()) > 0
            (True, True)
            sage: G.show() # This should be fast, since the mesh is already triangulated."""
    @overload
    def triangulate(self) -> Any:
        """ImplicitSurface.triangulate(self, force=False)

        File: /build/sagemath/src/sage/src/sage/plot/plot3d/implicit_surface.pyx (starting at line 1179)

        The IndexFaceSet will be empty until you call this method,
        which generates the faces and vertices according to the
        parameters specified in the constructor for ImplicitSurface.

        Note that if you call this method more than once, subsequent
        invocations will have no effect (this is an optimization to
        avoid repeated work) unless you specify ``force=True`` in the
        keywords.

        EXAMPLES::

            sage: from sage.plot.plot3d.implicit_surface import ImplicitSurface
            sage: var('x,y,z')
            (x, y, z)
            sage: G = ImplicitSurface(x + y + z, (x,-1, 1), (y,-1, 1), (z,-1, 1))
            sage: len(G.vertex_list()), len(G.face_list())
            (0, 0)
            sage: G.triangulate()
            sage: len(G.vertex_list()) > 0, len(G.face_list()) > 0
            (True, True)
            sage: G.show() # This should be fast, since the mesh is already triangulated."""

class MarchingCubes:
    """MarchingCubes(xrange, yrange, zrange, contour, plot_points, transform=None, region=None, gradient=None, smooth=True, color_function=None, colormap=None)

    File: /build/sagemath/src/sage/src/sage/plot/plot3d/implicit_surface.pyx (starting at line 168)

    Handles marching cube rendering.

    Protocol:

    1. Create the class.
    2. Call ``process_slice`` once for each X slice, from self.nx > x >= 0.
    3. Call ``finish()``, which returns a list of strings.

    .. NOTE::

        Actually, only 4 slices ever exist; the caller will re-use old
        storage."""
    color_function: File
    colormap: File
    contour: File
    gradient: File
    nx: File
    ny: File
    nz: File
    region: File
    results: File
    smooth: File
    transform: File
    xrange: File
    yrange: File
    zrange: File
    def __init__(self, xrange, yrange, zrange, contour, plot_points, transform=..., region=..., gradient=..., smooth=..., color_function=..., colormap=...) -> Any:
        """File: /build/sagemath/src/sage/src/sage/plot/plot3d/implicit_surface.pyx (starting at line 219)

                TESTS:

                Marching cubes is an abstract base class, you can't do anything with it::

                    sage: from sage.plot.plot3d.implicit_surface import MarchingCubes
                    sage: cube_marcher = MarchingCubes((0, 1), (0, 1), (0, 1), 1, (10, 10, 10))
        """
    @overload
    def finish(self) -> Any:
        """MarchingCubes.finish(self)

        File: /build/sagemath/src/sage/src/sage/plot/plot3d/implicit_surface.pyx (starting at line 279)

        Return the results of the marching cubes algorithm as a list.

        The format is specific to the subclass implementing this
        method.

        TESTS:

        By default, it returns an empty list::

            sage: from sage.plot.plot3d.implicit_surface import MarchingCubes
            sage: cube_marcher = MarchingCubes((0, 1), (0, 1), (0, 1), 1, (10, 10, 10), None)
            sage: cube_marcher.finish()
            []"""
    @overload
    def finish(self) -> Any:
        """MarchingCubes.finish(self)

        File: /build/sagemath/src/sage/src/sage/plot/plot3d/implicit_surface.pyx (starting at line 279)

        Return the results of the marching cubes algorithm as a list.

        The format is specific to the subclass implementing this
        method.

        TESTS:

        By default, it returns an empty list::

            sage: from sage.plot.plot3d.implicit_surface import MarchingCubes
            sage: cube_marcher = MarchingCubes((0, 1), (0, 1), (0, 1), 1, (10, 10, 10), None)
            sage: cube_marcher.finish()
            []"""

class MarchingCubesTriangles(MarchingCubes):
    """MarchingCubesTriangles(*args, **kwargs)

    File: /build/sagemath/src/sage/src/sage/plot/plot3d/implicit_surface.pyx (starting at line 298)

    A subclass of MarchingCubes that returns its results as a list of triangles,
    including their vertices and normals (if ``smooth=True``).

    And also their vertex colors if a vertex coloring function is given."""
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    slices: File
    x_vertices: File
    y_vertices: File
    y_vertices_swapped: File
    z_vertices: File
    z_vertices_swapped: File
    def __init__(self, *args, **kwargs) -> Any:
        """File: /build/sagemath/src/sage/src/sage/plot/plot3d/implicit_surface.pyx (starting at line 315)

                TESTS::

                    sage: from sage.plot.plot3d.implicit_surface import MarchingCubesTriangles
                    sage: cube_marcher = MarchingCubesTriangles((0, 1), (0, 1), (0, 1), 1, (10, 10, 10))
        """
    def add_triangle(self, VertexInfov1, VertexInfov2, VertexInfov3) -> Any:
        """MarchingCubesTriangles.add_triangle(self, VertexInfo v1, VertexInfo v2, VertexInfo v3)

        File: /build/sagemath/src/sage/src/sage/plot/plot3d/implicit_surface.pyx (starting at line 793)

        Called when a new triangle is generated by the marching cubes algorithm
        to update the results array.

        TESTS::

            sage: from sage.plot.plot3d.implicit_surface import MarchingCubesTriangles, VertexInfo
            sage: cube_marcher = MarchingCubesTriangles((0, 1), (0, 1), (0, 1), 0, (10,)*3, smooth=False)
            sage: cube_marcher.add_triangle(VertexInfo(), VertexInfo(), VertexInfo())
            sage: cube_marcher.finish()
            [({'x': 0.0, 'y': 0.0, 'z': 0.0},
              {'x': 0.0, 'y': 0.0, 'z': 0.0},
              {'x': 0.0, 'y': 0.0, 'z': 0.0})]"""
    def process_cubes(self, ndarray_left, ndarray_right) -> Any:
        """MarchingCubesTriangles.process_cubes(self, ndarray _left, ndarray _right)

        File: /build/sagemath/src/sage/src/sage/plot/plot3d/implicit_surface.pyx (starting at line 689)

        TESTS::

            sage: from sage.plot.plot3d.implicit_surface import MarchingCubesTriangles
            sage: import numpy as np
            sage: cube_marcher = MarchingCubesTriangles((0, 1), (0, 1), (0, 1), 0, (3, 2, 2), smooth=False)
            sage: slices = [np.ones((2, 2), dtype=np.double) for i in range(3)]
            sage: slices[0][1, 1] = -1
            sage: cube_marcher._update_yz_vertices(0, None, slices[0], slices[1])
            sage: cube_marcher._update_x_vertices(0, None, slices[0], slices[1], slices[2])
            sage: cube_marcher.process_cubes(slices[0], slices[1])
            sage: cube_marcher.finish()
            [({'x': 0.0, 'y': 1.0, 'z': 0.5},
              {'x': 0.25, 'y': 1.0, 'z': 1.0},
              {'x': 0.0, 'y': 0.5, 'z': 1.0})]"""
    def process_slice(self, unsignedintx, ndarrayslice) -> Any:
        """MarchingCubesTriangles.process_slice(self, unsigned int x, ndarray slice)

        File: /build/sagemath/src/sage/src/sage/plot/plot3d/implicit_surface.pyx (starting at line 336)

        Process a single slice of function evaluations at the specified `x`
        coordinate.

        EXAMPLES::

            sage: from sage.plot.plot3d.implicit_surface import MarchingCubesTriangles
            sage: import numpy as np
            sage: cube_marcher = MarchingCubesTriangles((-2, 2), (-2, 2), (-2, 2), 4, (10,)*3, smooth=False)
            sage: f = lambda x, y, z: x^2 + y^2 + z^2
            sage: slices = np.zeros((10, 10, 10), dtype=np.double)
            sage: for x in reversed(range(0, 10)):
            ....:     for y in range(0, 10):
            ....:         for z in range(0, 10):
            ....:             slices[x, y, z] = f(*[a * (4 / 9) -2 for a in (x, y, z)])
            ....:     cube_marcher.process_slice(x, slices[x, :, :])
            sage: faces = cube_marcher.finish()
            sage: faces[0][0]
            {'x': 1.555555555555..., 'y': -1.111111111111..., 'z': -0.555555555555...}

        We render the isosurface using IndexFaceSet::

            sage: from sage.plot.plot3d.index_face_set import IndexFaceSet
            sage: IndexFaceSet([tuple((p['x'], p['y'], p['z']) for p in face) for face in faces])
            Graphics3d Object"""

class VertexInfo:
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    @classmethod
    def __init__(cls, *args, **kwargs) -> None:
        """Create and return a new object.  See help(type) for accurate signature."""
