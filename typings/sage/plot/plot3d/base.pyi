import _cython_3_2_1
import sage.structure.sage_object
from sage.categories.category import RDF as RDF, pi as pi
from sage.interfaces.tachyon import tachyon_rt as tachyon_rt
from sage.misc.temporary_file import tmp_filename as tmp_filename
from sage.modules.free_module_element import vector as vector
from sage.plot.plot3d.texture import Texture as Texture, default_texture as default_texture
from typing import Any, ClassVar, overload

SHOW_DEFAULTS: dict
flatten_list: _cython_3_2_1.cython_function_or_method
max3: _cython_3_2_1.cython_function_or_method
min3: _cython_3_2_1.cython_function_or_method
optimal_aspect_ratios: _cython_3_2_1.cython_function_or_method
optimal_extra_kwds: _cython_3_2_1.cython_function_or_method
point_list_bounding_box: _cython_3_2_1.cython_function_or_method

class BoundingSphere(sage.structure.sage_object.SageObject):
    """File: /build/sagemath/src/sage/src/sage/plot/plot3d/base.pyx (starting at line 3016)

        A bounding sphere is like a bounding box, but is simpler to deal with and
        behaves better under rotations.
    """
    def __init__(self, cen, r) -> Any:
        """BoundingSphere.__init__(self, cen, r)

        File: /build/sagemath/src/sage/src/sage/plot/plot3d/base.pyx (starting at line 3021)

        EXAMPLES::

            sage: from sage.plot.plot3d.base import BoundingSphere
            sage: BoundingSphere((0,0,0), 1)
            Center (0.0, 0.0, 0.0) radius 1
            sage: BoundingSphere((0,-1,5), 2)
            Center (0.0, -1.0, 5.0) radius 2
    """
    def transform(self, T) -> Any:
        """BoundingSphere.transform(self, T)

        File: /build/sagemath/src/sage/src/sage/plot/plot3d/base.pyx (starting at line 3075)

        Return the bounding sphere of this sphere acted on by T. This always
        returns a new sphere, even if the resulting object is an ellipsoid.

        EXAMPLES::

            sage: from sage.plot.plot3d.transform import Transformation
            sage: from sage.plot.plot3d.base import BoundingSphere
            sage: BoundingSphere((0,0,0), 10).transform(Transformation(trans=(1,2,3)))
            Center (1.0, 2.0, 3.0) radius 10.0
            sage: BoundingSphere((0,0,0), 10).transform(Transformation(scale=(1/2, 1, 2)))
            Center (0.0, 0.0, 0.0) radius 20.0
            sage: BoundingSphere((0,0,3), 10).transform(Transformation(scale=(2, 2, 2)))
            Center (0.0, 0.0, 6.0) radius 20.0"""
    def __add__(self, other) -> Any:
        """BoundingSphere.__add__(self, other)

        File: /build/sagemath/src/sage/src/sage/plot/plot3d/base.pyx (starting at line 3044)

        Return the bounding sphere containing both terms.

        EXAMPLES::

            sage: from sage.plot.plot3d.base import BoundingSphere
            sage: BoundingSphere((0,0,0), 1) + BoundingSphere((0,0,0), 2)
            Center (0.0, 0.0, 0.0) radius 2
            sage: BoundingSphere((0,0,0), 1) + BoundingSphere((0,0,100), 1)
            Center (0.0, 0.0, 50.0) radius 51.0
            sage: BoundingSphere((0,0,0), 1) + BoundingSphere((1,1,1), 2)
            Center (0.7886751345948128, 0.7886751345948128, 0.7886751345948128) radius 2.3660254037844384

        Treat None and 0 as the identity::

            sage: BoundingSphere((1,2,3), 10) + None + 0
            Center (1.0, 2.0, 3.0) radius 10"""

class Graphics3d(sage.structure.sage_object.SageObject):
    """File: /build/sagemath/src/sage/src/sage/plot/plot3d/base.pyx (starting at line 78)

        This is the baseclass for all 3d graphics objects.

        .. automethod:: __add__
        .. automethod:: _rich_repr_
    """
    tachyon_keywords: ClassVar[tuple] = ...
    texture: texture
    @classmethod
    def __init__(cls, *args, **kwargs) -> None:
        """Create and return a new object.  See help(type) for accurate signature."""
    @overload
    def amf_ascii_string(self, name=...) -> Any:
        '''Graphics3d.amf_ascii_string(self, name=\'surface\')

        File: /build/sagemath/src/sage/src/sage/plot/plot3d/base.pyx (starting at line 2169)

        Return an AMF (Additive Manufacturing File Format) representation of
        the surface.

        .. WARNING::

            This only works for triangulated surfaces!

        INPUT:

        - ``name`` -- string (default: ``\'surface\'``); name of the surface

        OUTPUT: string that represents the surface in the AMF format

        See :wikipedia:`Additive_Manufacturing_File_Format`.

        .. TODO::

            This should rather be saved as a ZIP archive to save space.

        EXAMPLES::

            sage: # needs sage.symbolic
            sage: x,y,z = var(\'x,y,z\')
            sage: a = implicit_plot3d(x^2+y^2+z^2-9,[x,-5,5],[y,-5,5],[z,-5,5])
            sage: a_amf = a.amf_ascii_string()
            sage: a_amf[:160]
            \'<?xml version="1.0" encoding="utf-8"?><amf><object id="surface"><mesh><vertices><vertex><coordinates><x>2.948717948717948</x><y>-0.384615384615385</y><z>-0.3935\'

            sage: p = polygon3d([[0,0,0], [1,2,3], [3,0,0]])
            sage: print(p.amf_ascii_string(name=\'triangle\'))
            <?xml version="1.0" encoding="utf-8"?><amf><object id="triangle"><mesh><vertices><vertex><coordinates><x>0.0</x><y>0.0</y><z>0.0</z></coordinates></vertex><vertex><coordinates><x>1.0</x><y>2.0</y><z>3.0</z></coordinates></vertex><vertex><coordinates><x>3.0</x><y>0.0</y><z>0.0</z></coordinates></vertex></vertices><volume><triangle><v1>0</v1><v2>1</v2><v3>2</v3></triangle></volume></mesh></object></amf>'''
    @overload
    def amf_ascii_string(self) -> Any:
        '''Graphics3d.amf_ascii_string(self, name=\'surface\')

        File: /build/sagemath/src/sage/src/sage/plot/plot3d/base.pyx (starting at line 2169)

        Return an AMF (Additive Manufacturing File Format) representation of
        the surface.

        .. WARNING::

            This only works for triangulated surfaces!

        INPUT:

        - ``name`` -- string (default: ``\'surface\'``); name of the surface

        OUTPUT: string that represents the surface in the AMF format

        See :wikipedia:`Additive_Manufacturing_File_Format`.

        .. TODO::

            This should rather be saved as a ZIP archive to save space.

        EXAMPLES::

            sage: # needs sage.symbolic
            sage: x,y,z = var(\'x,y,z\')
            sage: a = implicit_plot3d(x^2+y^2+z^2-9,[x,-5,5],[y,-5,5],[z,-5,5])
            sage: a_amf = a.amf_ascii_string()
            sage: a_amf[:160]
            \'<?xml version="1.0" encoding="utf-8"?><amf><object id="surface"><mesh><vertices><vertex><coordinates><x>2.948717948717948</x><y>-0.384615384615385</y><z>-0.3935\'

            sage: p = polygon3d([[0,0,0], [1,2,3], [3,0,0]])
            sage: print(p.amf_ascii_string(name=\'triangle\'))
            <?xml version="1.0" encoding="utf-8"?><amf><object id="triangle"><mesh><vertices><vertex><coordinates><x>0.0</x><y>0.0</y><z>0.0</z></coordinates></vertex><vertex><coordinates><x>1.0</x><y>2.0</y><z>3.0</z></coordinates></vertex><vertex><coordinates><x>3.0</x><y>0.0</y><z>0.0</z></coordinates></vertex></vertices><volume><triangle><v1>0</v1><v2>1</v2><v3>2</v3></triangle></volume></mesh></object></amf>'''
    @overload
    def amf_ascii_string(self, name=...) -> Any:
        '''Graphics3d.amf_ascii_string(self, name=\'surface\')

        File: /build/sagemath/src/sage/src/sage/plot/plot3d/base.pyx (starting at line 2169)

        Return an AMF (Additive Manufacturing File Format) representation of
        the surface.

        .. WARNING::

            This only works for triangulated surfaces!

        INPUT:

        - ``name`` -- string (default: ``\'surface\'``); name of the surface

        OUTPUT: string that represents the surface in the AMF format

        See :wikipedia:`Additive_Manufacturing_File_Format`.

        .. TODO::

            This should rather be saved as a ZIP archive to save space.

        EXAMPLES::

            sage: # needs sage.symbolic
            sage: x,y,z = var(\'x,y,z\')
            sage: a = implicit_plot3d(x^2+y^2+z^2-9,[x,-5,5],[y,-5,5],[z,-5,5])
            sage: a_amf = a.amf_ascii_string()
            sage: a_amf[:160]
            \'<?xml version="1.0" encoding="utf-8"?><amf><object id="surface"><mesh><vertices><vertex><coordinates><x>2.948717948717948</x><y>-0.384615384615385</y><z>-0.3935\'

            sage: p = polygon3d([[0,0,0], [1,2,3], [3,0,0]])
            sage: print(p.amf_ascii_string(name=\'triangle\'))
            <?xml version="1.0" encoding="utf-8"?><amf><object id="triangle"><mesh><vertices><vertex><coordinates><x>0.0</x><y>0.0</y><z>0.0</z></coordinates></vertex><vertex><coordinates><x>1.0</x><y>2.0</y><z>3.0</z></coordinates></vertex><vertex><coordinates><x>3.0</x><y>0.0</y><z>0.0</z></coordinates></vertex></vertices><volume><triangle><v1>0</v1><v2>1</v2><v3>2</v3></triangle></volume></mesh></object></amf>'''
    @overload
    def aspect_ratio(self, v=...) -> Any:
        """Graphics3d.aspect_ratio(self, v=None)

        File: /build/sagemath/src/sage/src/sage/plot/plot3d/base.pyx (starting at line 644)

        Set or get the preferred aspect ratio.

        INPUT:

        - ``v`` -- (default: ``None``) must be a list or tuple of length three,
          or the integer ``1``. If no arguments are provided then the
          default aspect ratio is returned.

        EXAMPLES::

            sage: D = dodecahedron()
            sage: D.aspect_ratio()
            [1.0, 1.0, 1.0]
            sage: D.aspect_ratio([1,2,3])
            sage: D.aspect_ratio()
            [1.0, 2.0, 3.0]
            sage: D.aspect_ratio(1)
            sage: D.aspect_ratio()
            [1.0, 1.0, 1.0]"""
    @overload
    def aspect_ratio(self) -> Any:
        """Graphics3d.aspect_ratio(self, v=None)

        File: /build/sagemath/src/sage/src/sage/plot/plot3d/base.pyx (starting at line 644)

        Set or get the preferred aspect ratio.

        INPUT:

        - ``v`` -- (default: ``None``) must be a list or tuple of length three,
          or the integer ``1``. If no arguments are provided then the
          default aspect ratio is returned.

        EXAMPLES::

            sage: D = dodecahedron()
            sage: D.aspect_ratio()
            [1.0, 1.0, 1.0]
            sage: D.aspect_ratio([1,2,3])
            sage: D.aspect_ratio()
            [1.0, 2.0, 3.0]
            sage: D.aspect_ratio(1)
            sage: D.aspect_ratio()
            [1.0, 1.0, 1.0]"""
    @overload
    def aspect_ratio(self) -> Any:
        """Graphics3d.aspect_ratio(self, v=None)

        File: /build/sagemath/src/sage/src/sage/plot/plot3d/base.pyx (starting at line 644)

        Set or get the preferred aspect ratio.

        INPUT:

        - ``v`` -- (default: ``None``) must be a list or tuple of length three,
          or the integer ``1``. If no arguments are provided then the
          default aspect ratio is returned.

        EXAMPLES::

            sage: D = dodecahedron()
            sage: D.aspect_ratio()
            [1.0, 1.0, 1.0]
            sage: D.aspect_ratio([1,2,3])
            sage: D.aspect_ratio()
            [1.0, 2.0, 3.0]
            sage: D.aspect_ratio(1)
            sage: D.aspect_ratio()
            [1.0, 1.0, 1.0]"""
    @overload
    def aspect_ratio(self) -> Any:
        """Graphics3d.aspect_ratio(self, v=None)

        File: /build/sagemath/src/sage/src/sage/plot/plot3d/base.pyx (starting at line 644)

        Set or get the preferred aspect ratio.

        INPUT:

        - ``v`` -- (default: ``None``) must be a list or tuple of length three,
          or the integer ``1``. If no arguments are provided then the
          default aspect ratio is returned.

        EXAMPLES::

            sage: D = dodecahedron()
            sage: D.aspect_ratio()
            [1.0, 1.0, 1.0]
            sage: D.aspect_ratio([1,2,3])
            sage: D.aspect_ratio()
            [1.0, 2.0, 3.0]
            sage: D.aspect_ratio(1)
            sage: D.aspect_ratio()
            [1.0, 1.0, 1.0]"""
    @overload
    def bounding_box(self) -> Any:
        """Graphics3d.bounding_box(self)

        File: /build/sagemath/src/sage/src/sage/plot/plot3d/base.pyx (starting at line 740)

        Return the lower and upper corners of a 3d bounding box.

        This is used for rendering, and the scene should fit entirely
        within this box.

        Specifically, the first point returned has x, y, and z
        coordinates that are the respective minimum over all points
        in the graphics, and the second point is the maximum.

        The default return value is simply the box containing the origin.

        EXAMPLES::

            sage: sphere((1,1,1), 2).bounding_box()
            ((-1.0, -1.0, -1.0), (3.0, 3.0, 3.0))
            sage: G = line3d([(1, 2, 3), (-1,-2,-3)])
            sage: G.bounding_box()
            ((-1.0, -2.0, -3.0), (1.0, 2.0, 3.0))"""
    @overload
    def bounding_box(self) -> Any:
        """Graphics3d.bounding_box(self)

        File: /build/sagemath/src/sage/src/sage/plot/plot3d/base.pyx (starting at line 740)

        Return the lower and upper corners of a 3d bounding box.

        This is used for rendering, and the scene should fit entirely
        within this box.

        Specifically, the first point returned has x, y, and z
        coordinates that are the respective minimum over all points
        in the graphics, and the second point is the maximum.

        The default return value is simply the box containing the origin.

        EXAMPLES::

            sage: sphere((1,1,1), 2).bounding_box()
            ((-1.0, -1.0, -1.0), (3.0, 3.0, 3.0))
            sage: G = line3d([(1, 2, 3), (-1,-2,-3)])
            sage: G.bounding_box()
            ((-1.0, -2.0, -3.0), (1.0, 2.0, 3.0))"""
    @overload
    def bounding_box(self) -> Any:
        """Graphics3d.bounding_box(self)

        File: /build/sagemath/src/sage/src/sage/plot/plot3d/base.pyx (starting at line 740)

        Return the lower and upper corners of a 3d bounding box.

        This is used for rendering, and the scene should fit entirely
        within this box.

        Specifically, the first point returned has x, y, and z
        coordinates that are the respective minimum over all points
        in the graphics, and the second point is the maximum.

        The default return value is simply the box containing the origin.

        EXAMPLES::

            sage: sphere((1,1,1), 2).bounding_box()
            ((-1.0, -1.0, -1.0), (3.0, 3.0, 3.0))
            sage: G = line3d([(1, 2, 3), (-1,-2,-3)])
            sage: G.bounding_box()
            ((-1.0, -2.0, -3.0), (1.0, 2.0, 3.0))"""
    @overload
    def default_render_params(self) -> Any:
        """Graphics3d.default_render_params(self)

        File: /build/sagemath/src/sage/src/sage/plot/plot3d/base.pyx (starting at line 902)

        Return an instance of RenderParams suitable for plotting this object.

        EXAMPLES::

            sage: type(dodecahedron().default_render_params())
            <class 'sage.plot.plot3d.base.RenderParams'>"""
    @overload
    def default_render_params(self) -> Any:
        """Graphics3d.default_render_params(self)

        File: /build/sagemath/src/sage/src/sage/plot/plot3d/base.pyx (starting at line 902)

        Return an instance of RenderParams suitable for plotting this object.

        EXAMPLES::

            sage: type(dodecahedron().default_render_params())
            <class 'sage.plot.plot3d.base.RenderParams'>"""
    @overload
    def export_jmol(self, filename=..., force_reload=..., zoom=..., spin=..., background=..., stereo=..., mesh=..., dots=..., perspective_depth=..., orientation=..., **ignored_kwds) -> Any:
        '''Graphics3d.export_jmol(self, filename=\'jmol_shape.jmol\', force_reload=False, zoom=1, spin=False, background=(1, 1, 1), stereo=False, mesh=False, dots=False, perspective_depth=True, orientation=(-764, -346, -545, 76.39), **ignored_kwds)

        File: /build/sagemath/src/sage/src/sage/plot/plot3d/base.pyx (starting at line 1169)

        A jmol scene consists of a script which refers to external files.
        Fortunately, we are able to put all of them in a single zip archive,
        which is the output of this call.

        EXAMPLES::

            sage: out_file = tmp_filename(ext=\'.jmol\')
            sage: G = sphere((1, 2, 3), 5) + cube() + sage.plot.plot3d.shapes.Text("hi")
            sage: G.export_jmol(out_file)
            sage: import zipfile
            sage: z = zipfile.ZipFile(out_file)
            sage: z.namelist()
            [\'obj_...pmesh\', \'SCRIPT\']

            sage: print(z.read(\'SCRIPT\').decode(\'ascii\'))
            data "model list"
            2
            empty
            Xx 0 0 0
            Xx 5.5 5.5 5.5
            end "model list"; show data
            select *
            wireframe off; spacefill off
            set labelOffset 0 0
            background [255,255,255]
            spin OFF
            moveto 0 -764 -346 -545 76.39
            centerAt absolute {0 0 0}
            zoom 100
            frank OFF
            set perspectivedepth ON
            isosurface sphere_1  center {1.0 2.0 3.0} sphere 5.0
            color isosurface  [102,102,255]
            pmesh obj_... "obj_...pmesh"
            color pmesh  [102,102,255]
            select atomno = 1
            color atom  [102,102,255]
            label "hi"
            isosurface fullylit; pmesh o* fullylit; set antialiasdisplay on;

            sage: print(z.read(z.namelist()[0]).decode(\'ascii\'))
            24
            0.5 0.5 0.5
            -0.5 0.5 0.5
            ...
            -0.5 -0.5 -0.5
            6
            5
            0
            1
            ...'''
    @overload
    def export_jmol(self, out_file) -> Any:
        '''Graphics3d.export_jmol(self, filename=\'jmol_shape.jmol\', force_reload=False, zoom=1, spin=False, background=(1, 1, 1), stereo=False, mesh=False, dots=False, perspective_depth=True, orientation=(-764, -346, -545, 76.39), **ignored_kwds)

        File: /build/sagemath/src/sage/src/sage/plot/plot3d/base.pyx (starting at line 1169)

        A jmol scene consists of a script which refers to external files.
        Fortunately, we are able to put all of them in a single zip archive,
        which is the output of this call.

        EXAMPLES::

            sage: out_file = tmp_filename(ext=\'.jmol\')
            sage: G = sphere((1, 2, 3), 5) + cube() + sage.plot.plot3d.shapes.Text("hi")
            sage: G.export_jmol(out_file)
            sage: import zipfile
            sage: z = zipfile.ZipFile(out_file)
            sage: z.namelist()
            [\'obj_...pmesh\', \'SCRIPT\']

            sage: print(z.read(\'SCRIPT\').decode(\'ascii\'))
            data "model list"
            2
            empty
            Xx 0 0 0
            Xx 5.5 5.5 5.5
            end "model list"; show data
            select *
            wireframe off; spacefill off
            set labelOffset 0 0
            background [255,255,255]
            spin OFF
            moveto 0 -764 -346 -545 76.39
            centerAt absolute {0 0 0}
            zoom 100
            frank OFF
            set perspectivedepth ON
            isosurface sphere_1  center {1.0 2.0 3.0} sphere 5.0
            color isosurface  [102,102,255]
            pmesh obj_... "obj_...pmesh"
            color pmesh  [102,102,255]
            select atomno = 1
            color atom  [102,102,255]
            label "hi"
            isosurface fullylit; pmesh o* fullylit; set antialiasdisplay on;

            sage: print(z.read(z.namelist()[0]).decode(\'ascii\'))
            24
            0.5 0.5 0.5
            -0.5 0.5 0.5
            ...
            -0.5 -0.5 -0.5
            6
            5
            0
            1
            ...'''
    @overload
    def flatten(self) -> Any:
        """Graphics3d.flatten(self)

        File: /build/sagemath/src/sage/src/sage/plot/plot3d/base.pyx (starting at line 1435)

        Try to reduce the depth of the scene tree by consolidating groups
        and transformations.

        The generic Graphics3d object cannot be made flatter.

        EXAMPLES::

            sage: G = sage.plot.plot3d.base.Graphics3d()
            sage: G.flatten() is G
            True"""
    @overload
    def flatten(self) -> Any:
        """Graphics3d.flatten(self)

        File: /build/sagemath/src/sage/src/sage/plot/plot3d/base.pyx (starting at line 1435)

        Try to reduce the depth of the scene tree by consolidating groups
        and transformations.

        The generic Graphics3d object cannot be made flatter.

        EXAMPLES::

            sage: G = sage.plot.plot3d.base.Graphics3d()
            sage: G.flatten() is G
            True"""
    @overload
    def frame_aspect_ratio(self, v=...) -> Any:
        """Graphics3d.frame_aspect_ratio(self, v=None)

        File: /build/sagemath/src/sage/src/sage/plot/plot3d/base.pyx (starting at line 678)

        Set or get the preferred frame aspect ratio.

        INPUT:

        - ``v`` -- (default: ``None``) must be a list or tuple of
          length three, or the integer ``1``. If no arguments are
          provided then the default frame aspect ratio is returned.

        EXAMPLES::

            sage: D = dodecahedron()
            sage: D.frame_aspect_ratio()
            [1.0, 1.0, 1.0]
            sage: D.frame_aspect_ratio([2,2,1])
            sage: D.frame_aspect_ratio()
            [2.0, 2.0, 1.0]
            sage: D.frame_aspect_ratio(1)
            sage: D.frame_aspect_ratio()
            [1.0, 1.0, 1.0]"""
    @overload
    def frame_aspect_ratio(self) -> Any:
        """Graphics3d.frame_aspect_ratio(self, v=None)

        File: /build/sagemath/src/sage/src/sage/plot/plot3d/base.pyx (starting at line 678)

        Set or get the preferred frame aspect ratio.

        INPUT:

        - ``v`` -- (default: ``None``) must be a list or tuple of
          length three, or the integer ``1``. If no arguments are
          provided then the default frame aspect ratio is returned.

        EXAMPLES::

            sage: D = dodecahedron()
            sage: D.frame_aspect_ratio()
            [1.0, 1.0, 1.0]
            sage: D.frame_aspect_ratio([2,2,1])
            sage: D.frame_aspect_ratio()
            [2.0, 2.0, 1.0]
            sage: D.frame_aspect_ratio(1)
            sage: D.frame_aspect_ratio()
            [1.0, 1.0, 1.0]"""
    @overload
    def frame_aspect_ratio(self) -> Any:
        """Graphics3d.frame_aspect_ratio(self, v=None)

        File: /build/sagemath/src/sage/src/sage/plot/plot3d/base.pyx (starting at line 678)

        Set or get the preferred frame aspect ratio.

        INPUT:

        - ``v`` -- (default: ``None``) must be a list or tuple of
          length three, or the integer ``1``. If no arguments are
          provided then the default frame aspect ratio is returned.

        EXAMPLES::

            sage: D = dodecahedron()
            sage: D.frame_aspect_ratio()
            [1.0, 1.0, 1.0]
            sage: D.frame_aspect_ratio([2,2,1])
            sage: D.frame_aspect_ratio()
            [2.0, 2.0, 1.0]
            sage: D.frame_aspect_ratio(1)
            sage: D.frame_aspect_ratio()
            [1.0, 1.0, 1.0]"""
    @overload
    def frame_aspect_ratio(self) -> Any:
        """Graphics3d.frame_aspect_ratio(self, v=None)

        File: /build/sagemath/src/sage/src/sage/plot/plot3d/base.pyx (starting at line 678)

        Set or get the preferred frame aspect ratio.

        INPUT:

        - ``v`` -- (default: ``None``) must be a list or tuple of
          length three, or the integer ``1``. If no arguments are
          provided then the default frame aspect ratio is returned.

        EXAMPLES::

            sage: D = dodecahedron()
            sage: D.frame_aspect_ratio()
            [1.0, 1.0, 1.0]
            sage: D.frame_aspect_ratio([2,2,1])
            sage: D.frame_aspect_ratio()
            [2.0, 2.0, 1.0]
            sage: D.frame_aspect_ratio(1)
            sage: D.frame_aspect_ratio()
            [1.0, 1.0, 1.0]"""
    def jmol_repr(self, render_params) -> Any:
        """Graphics3d.jmol_repr(self, render_params)

        File: /build/sagemath/src/sage/src/sage/plot/plot3d/base.pyx (starting at line 1297)

        A (possibly nested) list of strings which will be concatenated and
        used by jmol to render the object.

        (Nested lists of strings are used because otherwise all the
        intermediate concatenations can kill performance). This may
        refer to several remove files, which are stored in
        render_parames.output_archive.

        EXAMPLES::

            sage: G = sage.plot.plot3d.base.Graphics3d()
            sage: G.jmol_repr(G.default_render_params())
            []
            sage: G = sphere((1, 2, 3))
            sage: G.jmol_repr(G.default_render_params())
            [['isosurface sphere_1  center {1.0 2.0 3.0} sphere 1.0\\ncolor isosurface  [102,102,255]']]"""
    def json_repr(self, render_params) -> Any:
        """Graphics3d.json_repr(self, render_params)

        File: /build/sagemath/src/sage/src/sage/plot/plot3d/base.pyx (starting at line 1281)

        A (possibly nested) list of strings. Each entry is formatted
        as JSON, so that a JavaScript client could eval it and get an
        object. Each object has fields to encapsulate the faces and
        vertices of the object. This representation is intended to be
        consumed by the canvas3d viewer backend.

        EXAMPLES::

            sage: G = sage.plot.plot3d.base.Graphics3d()
            sage: G.json_repr(G.default_render_params())
            []"""
    @overload
    def mtl_str(self) -> Any:
        """Graphics3d.mtl_str(self)

        File: /build/sagemath/src/sage/src/sage/plot/plot3d/base.pyx (starting at line 1409)

        Return the contents of a .mtl file, to be used to provide coloring
        information for an .obj file.

        EXAMPLES::

            sage: G = tetrahedron(color='red') + tetrahedron(color='yellow', opacity=0.5)
            sage: print(G.mtl_str())
            newmtl ...
            Ka 0.5 5e-06 5e-06
            Kd 1.0 1e-05 1e-05
            Ks 0.0 0.0 0.0
            illum 1
            Ns 1.0
            d 1.0
            newmtl ...
            Ka 0.5 0.5 5e-06
            Kd 1.0 1.0 1e-05
            Ks 0.0 0.0 0.0
            illum 1
            Ns 1.0
            d 0.5"""
    @overload
    def mtl_str(self) -> Any:
        """Graphics3d.mtl_str(self)

        File: /build/sagemath/src/sage/src/sage/plot/plot3d/base.pyx (starting at line 1409)

        Return the contents of a .mtl file, to be used to provide coloring
        information for an .obj file.

        EXAMPLES::

            sage: G = tetrahedron(color='red') + tetrahedron(color='yellow', opacity=0.5)
            sage: print(G.mtl_str())
            newmtl ...
            Ka 0.5 5e-06 5e-06
            Kd 1.0 1e-05 1e-05
            Ks 0.0 0.0 0.0
            illum 1
            Ns 1.0
            d 1.0
            newmtl ...
            Ka 0.5 0.5 5e-06
            Kd 1.0 1.0 1e-05
            Ks 0.0 0.0 0.0
            illum 1
            Ns 1.0
            d 0.5"""
    @overload
    def obj(self) -> Any:
        """Graphics3d.obj(self)

        File: /build/sagemath/src/sage/src/sage/plot/plot3d/base.pyx (starting at line 1128)

        An .obj scene file (as a string) containing the this object.

        A .mtl file of the same name must also be produced for
        coloring.

        EXAMPLES::

            sage: from sage.plot.plot3d.shapes import ColorCube
            sage: print(ColorCube(1, ['red', 'yellow', 'blue']).obj())
            g obj_1
            usemtl ...
            v 1 1 1
            v -1 1 1
            v -1 -1 1
            v 1 -1 1
            f 1 2 3 4
            ...
            g obj_6
            usemtl ...
            v -1 -1 1
            v -1 1 1
            v -1 1 -1
            v -1 -1 -1
            f 21 22 23 24"""
    @overload
    def obj(self) -> Any:
        """Graphics3d.obj(self)

        File: /build/sagemath/src/sage/src/sage/plot/plot3d/base.pyx (starting at line 1128)

        An .obj scene file (as a string) containing the this object.

        A .mtl file of the same name must also be produced for
        coloring.

        EXAMPLES::

            sage: from sage.plot.plot3d.shapes import ColorCube
            sage: print(ColorCube(1, ['red', 'yellow', 'blue']).obj())
            g obj_1
            usemtl ...
            v 1 1 1
            v -1 1 1
            v -1 -1 1
            v 1 -1 1
            f 1 2 3 4
            ...
            g obj_6
            usemtl ...
            v -1 -1 1
            v -1 1 1
            v -1 1 -1
            v -1 -1 -1
            f 21 22 23 24"""
    def obj_repr(self, render_params) -> Any:
        """Graphics3d.obj_repr(self, render_params)

        File: /build/sagemath/src/sage/src/sage/plot/plot3d/base.pyx (starting at line 1339)

        A (possibly nested) list of strings which will be concatenated and
        used to construct an .obj file of the object.

        (Nested lists of strings are used because otherwise all the
        intermediate concatenations can kill performance). This may
        include a reference to color information which is stored
        elsewhere.

        EXAMPLES::

            sage: G = sage.plot.plot3d.base.Graphics3d()
            sage: G.obj_repr(G.default_render_params())
            []
            sage: G = cube()
            sage: G.obj_repr(G.default_render_params())
            ['g obj_1',
             'usemtl ...',
             ['v 0.5 0.5 0.5',
              'v -0.5 0.5 0.5',
              'v -0.5 -0.5 0.5',
              'v 0.5 -0.5 0.5',
              'v 0.5 0.5 -0.5',
              'v -0.5 0.5 -0.5',
              'v 0.5 -0.5 -0.5',
              'v -0.5 -0.5 -0.5'],
             ['f 1 2 3 4',
              'f 1 5 6 2',
              'f 1 4 7 5',
              'f 6 5 7 8',
              'f 7 4 3 8',
              'f 3 2 6 8'],
             []]"""
    @overload
    def plot(self) -> Any:
        """Graphics3d.plot(self)

        File: /build/sagemath/src/sage/src/sage/plot/plot3d/base.pyx (starting at line 2226)

        Draw a 3D plot of this graphics object, which just returns this
        object since this is already a 3D graphics object.
        Needed to support PLOT in docstrings, see :issue:`17498`

        EXAMPLES::

            sage: S = sphere((0,0,0), 2)
            sage: S.plot() is S
            True"""
    @overload
    def plot(self) -> Any:
        """Graphics3d.plot(self)

        File: /build/sagemath/src/sage/src/sage/plot/plot3d/base.pyx (starting at line 2226)

        Draw a 3D plot of this graphics object, which just returns this
        object since this is already a 3D graphics object.
        Needed to support PLOT in docstrings, see :issue:`17498`

        EXAMPLES::

            sage: S = sphere((0,0,0), 2)
            sage: S.plot() is S
            True"""
    @overload
    def ply_ascii_string(self, name=...) -> Any:
        """Graphics3d.ply_ascii_string(self, name='surface')

        File: /build/sagemath/src/sage/src/sage/plot/plot3d/base.pyx (starting at line 2105)

        Return a PLY (Polygon File Format) representation of the surface.

        INPUT:

        - ``name`` -- string (default: ``'surface'``); name of the surface

        OUTPUT: string that represents the surface in the PLY format

        See :wikipedia:`PLY_(file_format)`.

        EXAMPLES::

            sage: # needs sage.symbolic
            sage: x,y,z = var('x,y,z')
            sage: a = implicit_plot3d(x^2+y^2+z^2-9,[x,-5,5],[y,-5,5],[z,-5,5])
            sage: astl = a.ply_ascii_string()
            sage: astl.splitlines()[:10]
            ['ply',
            'format ascii 1.0',
            'comment surface',
            'element vertex 15540',
            'property float x',
            'property float y',
            'property float z',
            'element face 5180',
            'property list uchar int vertex_indices',
            'end_header']

            sage: p = polygon3d([[0,0,0], [1,2,3], [3,0,0]])
            sage: print(p.ply_ascii_string(name='triangle'))
            ply
            format ascii 1.0
            comment triangle
            element vertex 3
            property float x
            property float y
            property float z
            element face 1
            property list uchar int vertex_indices
            end_header
            0.0 0.0 0.0
            1.0 2.0 3.0
            3.0 0.0 0.0
            3 0 1 2"""
    @overload
    def ply_ascii_string(self) -> Any:
        """Graphics3d.ply_ascii_string(self, name='surface')

        File: /build/sagemath/src/sage/src/sage/plot/plot3d/base.pyx (starting at line 2105)

        Return a PLY (Polygon File Format) representation of the surface.

        INPUT:

        - ``name`` -- string (default: ``'surface'``); name of the surface

        OUTPUT: string that represents the surface in the PLY format

        See :wikipedia:`PLY_(file_format)`.

        EXAMPLES::

            sage: # needs sage.symbolic
            sage: x,y,z = var('x,y,z')
            sage: a = implicit_plot3d(x^2+y^2+z^2-9,[x,-5,5],[y,-5,5],[z,-5,5])
            sage: astl = a.ply_ascii_string()
            sage: astl.splitlines()[:10]
            ['ply',
            'format ascii 1.0',
            'comment surface',
            'element vertex 15540',
            'property float x',
            'property float y',
            'property float z',
            'element face 5180',
            'property list uchar int vertex_indices',
            'end_header']

            sage: p = polygon3d([[0,0,0], [1,2,3], [3,0,0]])
            sage: print(p.ply_ascii_string(name='triangle'))
            ply
            format ascii 1.0
            comment triangle
            element vertex 3
            property float x
            property float y
            property float z
            element face 1
            property list uchar int vertex_indices
            end_header
            0.0 0.0 0.0
            1.0 2.0 3.0
            3.0 0.0 0.0
            3 0 1 2"""
    @overload
    def ply_ascii_string(self, name=...) -> Any:
        """Graphics3d.ply_ascii_string(self, name='surface')

        File: /build/sagemath/src/sage/src/sage/plot/plot3d/base.pyx (starting at line 2105)

        Return a PLY (Polygon File Format) representation of the surface.

        INPUT:

        - ``name`` -- string (default: ``'surface'``); name of the surface

        OUTPUT: string that represents the surface in the PLY format

        See :wikipedia:`PLY_(file_format)`.

        EXAMPLES::

            sage: # needs sage.symbolic
            sage: x,y,z = var('x,y,z')
            sage: a = implicit_plot3d(x^2+y^2+z^2-9,[x,-5,5],[y,-5,5],[z,-5,5])
            sage: astl = a.ply_ascii_string()
            sage: astl.splitlines()[:10]
            ['ply',
            'format ascii 1.0',
            'comment surface',
            'element vertex 15540',
            'property float x',
            'property float y',
            'property float z',
            'element face 5180',
            'property list uchar int vertex_indices',
            'end_header']

            sage: p = polygon3d([[0,0,0], [1,2,3], [3,0,0]])
            sage: print(p.ply_ascii_string(name='triangle'))
            ply
            format ascii 1.0
            comment triangle
            element vertex 3
            property float x
            property float y
            property float z
            element face 1
            property list uchar int vertex_indices
            end_header
            0.0 0.0 0.0
            1.0 2.0 3.0
            3.0 0.0 0.0
            3 0 1 2"""
    def rotate(self, v, theta) -> Any:
        """Graphics3d.rotate(self, v, theta)

        File: /build/sagemath/src/sage/src/sage/plot/plot3d/base.pyx (starting at line 828)

        Return the object rotated about the vector `v` by `\\theta` radians.

        EXAMPLES::

            sage: from math import pi
            sage: from sage.plot.plot3d.shapes import Cone
            sage: v = (1,2,3)
            sage: G = arrow3d((0, 0, 0), v)
            sage: G += Cone(1/5, 1).translate((0, 0, 2))
            sage: C = Cone(1/5, 1, opacity=.25).translate((0, 0, 2))
            sage: G += sum(C.rotate(v, pi*t/4) for t in [1..7])
            sage: G.show(aspect_ratio=1)

            sage: from sage.plot.plot3d.shapes import Box
            sage: Box(1/3, 1/5, 1/7).rotate((1, 1, 1), pi/3).show(aspect_ratio=1)"""
    def rotateX(self, theta) -> Any:
        """Graphics3d.rotateX(self, theta)

        File: /build/sagemath/src/sage/src/sage/plot/plot3d/base.pyx (starting at line 849)

        Return the object rotated about the `x`-axis by the given angle.

        EXAMPLES::

            sage: from math import pi
            sage: from sage.plot.plot3d.shapes import Cone
            sage: G = Cone(1/5, 1) + Cone(1/5, 1, opacity=.25).rotateX(pi/2)
            sage: G.show(aspect_ratio=1)"""
    def rotateY(self, theta) -> Any:
        """Graphics3d.rotateY(self, theta)

        File: /build/sagemath/src/sage/src/sage/plot/plot3d/base.pyx (starting at line 862)

        Return the object rotated about the `y`-axis by the given angle.

        EXAMPLES::

            sage: from math import pi
            sage: from sage.plot.plot3d.shapes import Cone
            sage: G = Cone(1/5, 1) + Cone(1/5, 1, opacity=.25).rotateY(pi/3)
            sage: G.show(aspect_ratio=1)"""
    def rotateZ(self, theta) -> Any:
        """Graphics3d.rotateZ(self, theta)

        File: /build/sagemath/src/sage/src/sage/plot/plot3d/base.pyx (starting at line 875)

        Return the object rotated about the `z`-axis by the given angle.

        EXAMPLES::

            sage: from math import pi
            sage: from sage.plot.plot3d.shapes import Box
            sage: G = Box(1/2, 1/3, 1/5) + Box(1/2, 1/3, 1/5, opacity=.25).rotateZ(pi/5)
            sage: G.show(aspect_ratio=1)"""
    @overload
    def save(self, filename, **kwds) -> Any:
        '''Graphics3d.save(self, filename, **kwds)

        File: /build/sagemath/src/sage/src/sage/plot/plot3d/base.pyx (starting at line 1867)

        Save the graphic in a file.

        The file type depends on the file extension you give in the
        filename. This can be either:

        - an image file (of type: PNG, BMP, GIF, PPM, or TIFF) rendered
          using Jmol (default) or Tachyon,

        - a Sage object file (of type ``.sobj``) that you can load back later
          (a pickle),

        - an HTML file depicting the graphic using the Three.js viewer,

        - a data file (of type: X3D, STL, AMF, PLY) for export and use in
          other software.

        For data files, the support is only partial. For instance STL and
        AMF only works for triangulated surfaces. The prefered format is X3D.

        INPUT:

        - ``filename`` -- string; where to save the image or object

        - ``**kwds`` -- when specifying an image file to be rendered by Tachyon
          or Jmol, any of the viewing options accepted by :meth:`show` are valid as
          keyword arguments to this function and they will behave in the same
          way. Accepted keywords include: ``viewer``, ``verbosity``,
          ``figsize``, ``aspect_ratio``, ``frame_aspect_ratio``, ``zoom``,
          ``frame``, and ``axes``. Default values are provided.

        EXAMPLES::

            sage: f = tmp_filename(ext=\'.png\')
            sage: G = sphere()
            sage: G.save(f)

        We demonstrate using keyword arguments to control the appearance of the
        output image::

            sage: G.save(f, zoom=2, figsize=[5, 10])

        Using Tachyon instead of the default viewer (Jmol) to create the
        image::

            sage: G.save(f, viewer=\'tachyon\')

        Since Tachyon only outputs PNG images, PIL will be used to convert to
        alternate formats::

            sage: cube().save(tmp_filename(ext=\'.gif\'), viewer=\'tachyon\')

        Here is how to save in one of the data formats::

            sage: f = tmp_filename(ext=\'.x3d\')
            sage: cube().save(f)

            sage: open(f).read().splitlines()[7]
            "<Shape><Box size=\'0.5 0.5 0.5\'/><Appearance><Material diffuseColor=\'0.4 0.4 1.0\' shininess=\'1.0\' specularColor=\'0.0 0.0 0.0\'/></Appearance></Shape>"

        Producing a Three.js-based HTML file::

            sage: f = tmp_filename(ext=\'.html\')
            sage: G.save(f, frame=False, online=True)'''
    @overload
    def save(self, f) -> Any:
        '''Graphics3d.save(self, filename, **kwds)

        File: /build/sagemath/src/sage/src/sage/plot/plot3d/base.pyx (starting at line 1867)

        Save the graphic in a file.

        The file type depends on the file extension you give in the
        filename. This can be either:

        - an image file (of type: PNG, BMP, GIF, PPM, or TIFF) rendered
          using Jmol (default) or Tachyon,

        - a Sage object file (of type ``.sobj``) that you can load back later
          (a pickle),

        - an HTML file depicting the graphic using the Three.js viewer,

        - a data file (of type: X3D, STL, AMF, PLY) for export and use in
          other software.

        For data files, the support is only partial. For instance STL and
        AMF only works for triangulated surfaces. The prefered format is X3D.

        INPUT:

        - ``filename`` -- string; where to save the image or object

        - ``**kwds`` -- when specifying an image file to be rendered by Tachyon
          or Jmol, any of the viewing options accepted by :meth:`show` are valid as
          keyword arguments to this function and they will behave in the same
          way. Accepted keywords include: ``viewer``, ``verbosity``,
          ``figsize``, ``aspect_ratio``, ``frame_aspect_ratio``, ``zoom``,
          ``frame``, and ``axes``. Default values are provided.

        EXAMPLES::

            sage: f = tmp_filename(ext=\'.png\')
            sage: G = sphere()
            sage: G.save(f)

        We demonstrate using keyword arguments to control the appearance of the
        output image::

            sage: G.save(f, zoom=2, figsize=[5, 10])

        Using Tachyon instead of the default viewer (Jmol) to create the
        image::

            sage: G.save(f, viewer=\'tachyon\')

        Since Tachyon only outputs PNG images, PIL will be used to convert to
        alternate formats::

            sage: cube().save(tmp_filename(ext=\'.gif\'), viewer=\'tachyon\')

        Here is how to save in one of the data formats::

            sage: f = tmp_filename(ext=\'.x3d\')
            sage: cube().save(f)

            sage: open(f).read().splitlines()[7]
            "<Shape><Box size=\'0.5 0.5 0.5\'/><Appearance><Material diffuseColor=\'0.4 0.4 1.0\' shininess=\'1.0\' specularColor=\'0.0 0.0 0.0\'/></Appearance></Shape>"

        Producing a Three.js-based HTML file::

            sage: f = tmp_filename(ext=\'.html\')
            sage: G.save(f, frame=False, online=True)'''
    @overload
    def save(self, f, zoom=..., figsize=...) -> Any:
        '''Graphics3d.save(self, filename, **kwds)

        File: /build/sagemath/src/sage/src/sage/plot/plot3d/base.pyx (starting at line 1867)

        Save the graphic in a file.

        The file type depends on the file extension you give in the
        filename. This can be either:

        - an image file (of type: PNG, BMP, GIF, PPM, or TIFF) rendered
          using Jmol (default) or Tachyon,

        - a Sage object file (of type ``.sobj``) that you can load back later
          (a pickle),

        - an HTML file depicting the graphic using the Three.js viewer,

        - a data file (of type: X3D, STL, AMF, PLY) for export and use in
          other software.

        For data files, the support is only partial. For instance STL and
        AMF only works for triangulated surfaces. The prefered format is X3D.

        INPUT:

        - ``filename`` -- string; where to save the image or object

        - ``**kwds`` -- when specifying an image file to be rendered by Tachyon
          or Jmol, any of the viewing options accepted by :meth:`show` are valid as
          keyword arguments to this function and they will behave in the same
          way. Accepted keywords include: ``viewer``, ``verbosity``,
          ``figsize``, ``aspect_ratio``, ``frame_aspect_ratio``, ``zoom``,
          ``frame``, and ``axes``. Default values are provided.

        EXAMPLES::

            sage: f = tmp_filename(ext=\'.png\')
            sage: G = sphere()
            sage: G.save(f)

        We demonstrate using keyword arguments to control the appearance of the
        output image::

            sage: G.save(f, zoom=2, figsize=[5, 10])

        Using Tachyon instead of the default viewer (Jmol) to create the
        image::

            sage: G.save(f, viewer=\'tachyon\')

        Since Tachyon only outputs PNG images, PIL will be used to convert to
        alternate formats::

            sage: cube().save(tmp_filename(ext=\'.gif\'), viewer=\'tachyon\')

        Here is how to save in one of the data formats::

            sage: f = tmp_filename(ext=\'.x3d\')
            sage: cube().save(f)

            sage: open(f).read().splitlines()[7]
            "<Shape><Box size=\'0.5 0.5 0.5\'/><Appearance><Material diffuseColor=\'0.4 0.4 1.0\' shininess=\'1.0\' specularColor=\'0.0 0.0 0.0\'/></Appearance></Shape>"

        Producing a Three.js-based HTML file::

            sage: f = tmp_filename(ext=\'.html\')
            sage: G.save(f, frame=False, online=True)'''
    @overload
    def save(self, f, viewer=...) -> Any:
        '''Graphics3d.save(self, filename, **kwds)

        File: /build/sagemath/src/sage/src/sage/plot/plot3d/base.pyx (starting at line 1867)

        Save the graphic in a file.

        The file type depends on the file extension you give in the
        filename. This can be either:

        - an image file (of type: PNG, BMP, GIF, PPM, or TIFF) rendered
          using Jmol (default) or Tachyon,

        - a Sage object file (of type ``.sobj``) that you can load back later
          (a pickle),

        - an HTML file depicting the graphic using the Three.js viewer,

        - a data file (of type: X3D, STL, AMF, PLY) for export and use in
          other software.

        For data files, the support is only partial. For instance STL and
        AMF only works for triangulated surfaces. The prefered format is X3D.

        INPUT:

        - ``filename`` -- string; where to save the image or object

        - ``**kwds`` -- when specifying an image file to be rendered by Tachyon
          or Jmol, any of the viewing options accepted by :meth:`show` are valid as
          keyword arguments to this function and they will behave in the same
          way. Accepted keywords include: ``viewer``, ``verbosity``,
          ``figsize``, ``aspect_ratio``, ``frame_aspect_ratio``, ``zoom``,
          ``frame``, and ``axes``. Default values are provided.

        EXAMPLES::

            sage: f = tmp_filename(ext=\'.png\')
            sage: G = sphere()
            sage: G.save(f)

        We demonstrate using keyword arguments to control the appearance of the
        output image::

            sage: G.save(f, zoom=2, figsize=[5, 10])

        Using Tachyon instead of the default viewer (Jmol) to create the
        image::

            sage: G.save(f, viewer=\'tachyon\')

        Since Tachyon only outputs PNG images, PIL will be used to convert to
        alternate formats::

            sage: cube().save(tmp_filename(ext=\'.gif\'), viewer=\'tachyon\')

        Here is how to save in one of the data formats::

            sage: f = tmp_filename(ext=\'.x3d\')
            sage: cube().save(f)

            sage: open(f).read().splitlines()[7]
            "<Shape><Box size=\'0.5 0.5 0.5\'/><Appearance><Material diffuseColor=\'0.4 0.4 1.0\' shininess=\'1.0\' specularColor=\'0.0 0.0 0.0\'/></Appearance></Shape>"

        Producing a Three.js-based HTML file::

            sage: f = tmp_filename(ext=\'.html\')
            sage: G.save(f, frame=False, online=True)'''
    @overload
    def save(self, f) -> Any:
        '''Graphics3d.save(self, filename, **kwds)

        File: /build/sagemath/src/sage/src/sage/plot/plot3d/base.pyx (starting at line 1867)

        Save the graphic in a file.

        The file type depends on the file extension you give in the
        filename. This can be either:

        - an image file (of type: PNG, BMP, GIF, PPM, or TIFF) rendered
          using Jmol (default) or Tachyon,

        - a Sage object file (of type ``.sobj``) that you can load back later
          (a pickle),

        - an HTML file depicting the graphic using the Three.js viewer,

        - a data file (of type: X3D, STL, AMF, PLY) for export and use in
          other software.

        For data files, the support is only partial. For instance STL and
        AMF only works for triangulated surfaces. The prefered format is X3D.

        INPUT:

        - ``filename`` -- string; where to save the image or object

        - ``**kwds`` -- when specifying an image file to be rendered by Tachyon
          or Jmol, any of the viewing options accepted by :meth:`show` are valid as
          keyword arguments to this function and they will behave in the same
          way. Accepted keywords include: ``viewer``, ``verbosity``,
          ``figsize``, ``aspect_ratio``, ``frame_aspect_ratio``, ``zoom``,
          ``frame``, and ``axes``. Default values are provided.

        EXAMPLES::

            sage: f = tmp_filename(ext=\'.png\')
            sage: G = sphere()
            sage: G.save(f)

        We demonstrate using keyword arguments to control the appearance of the
        output image::

            sage: G.save(f, zoom=2, figsize=[5, 10])

        Using Tachyon instead of the default viewer (Jmol) to create the
        image::

            sage: G.save(f, viewer=\'tachyon\')

        Since Tachyon only outputs PNG images, PIL will be used to convert to
        alternate formats::

            sage: cube().save(tmp_filename(ext=\'.gif\'), viewer=\'tachyon\')

        Here is how to save in one of the data formats::

            sage: f = tmp_filename(ext=\'.x3d\')
            sage: cube().save(f)

            sage: open(f).read().splitlines()[7]
            "<Shape><Box size=\'0.5 0.5 0.5\'/><Appearance><Material diffuseColor=\'0.4 0.4 1.0\' shininess=\'1.0\' specularColor=\'0.0 0.0 0.0\'/></Appearance></Shape>"

        Producing a Three.js-based HTML file::

            sage: f = tmp_filename(ext=\'.html\')
            sage: G.save(f, frame=False, online=True)'''
    @overload
    def save(self, f, frame=..., online=...) -> Any:
        '''Graphics3d.save(self, filename, **kwds)

        File: /build/sagemath/src/sage/src/sage/plot/plot3d/base.pyx (starting at line 1867)

        Save the graphic in a file.

        The file type depends on the file extension you give in the
        filename. This can be either:

        - an image file (of type: PNG, BMP, GIF, PPM, or TIFF) rendered
          using Jmol (default) or Tachyon,

        - a Sage object file (of type ``.sobj``) that you can load back later
          (a pickle),

        - an HTML file depicting the graphic using the Three.js viewer,

        - a data file (of type: X3D, STL, AMF, PLY) for export and use in
          other software.

        For data files, the support is only partial. For instance STL and
        AMF only works for triangulated surfaces. The prefered format is X3D.

        INPUT:

        - ``filename`` -- string; where to save the image or object

        - ``**kwds`` -- when specifying an image file to be rendered by Tachyon
          or Jmol, any of the viewing options accepted by :meth:`show` are valid as
          keyword arguments to this function and they will behave in the same
          way. Accepted keywords include: ``viewer``, ``verbosity``,
          ``figsize``, ``aspect_ratio``, ``frame_aspect_ratio``, ``zoom``,
          ``frame``, and ``axes``. Default values are provided.

        EXAMPLES::

            sage: f = tmp_filename(ext=\'.png\')
            sage: G = sphere()
            sage: G.save(f)

        We demonstrate using keyword arguments to control the appearance of the
        output image::

            sage: G.save(f, zoom=2, figsize=[5, 10])

        Using Tachyon instead of the default viewer (Jmol) to create the
        image::

            sage: G.save(f, viewer=\'tachyon\')

        Since Tachyon only outputs PNG images, PIL will be used to convert to
        alternate formats::

            sage: cube().save(tmp_filename(ext=\'.gif\'), viewer=\'tachyon\')

        Here is how to save in one of the data formats::

            sage: f = tmp_filename(ext=\'.x3d\')
            sage: cube().save(f)

            sage: open(f).read().splitlines()[7]
            "<Shape><Box size=\'0.5 0.5 0.5\'/><Appearance><Material diffuseColor=\'0.4 0.4 1.0\' shininess=\'1.0\' specularColor=\'0.0 0.0 0.0\'/></Appearance></Shape>"

        Producing a Three.js-based HTML file::

            sage: f = tmp_filename(ext=\'.html\')
            sage: G.save(f, frame=False, online=True)'''
    @overload
    def save_image(self, filename, **kwds) -> Any:
        """Graphics3d.save_image(self, filename, **kwds)

        File: /build/sagemath/src/sage/src/sage/plot/plot3d/base.pyx (starting at line 1827)

        Save a 2-D image rendering.

        The image type is determined by the extension of the filename.
        For example, this could be ``.png``, ``.jpg``, ``.gif``,
        ``.pdf``, ``.svg``.

        INPUT:

        - ``filename`` -- string; the file name under which to save
          the image

        Any further keyword arguments are passed to the renderer.

        EXAMPLES::

            sage: G = sphere()
            sage: png = tmp_filename(ext='.png')
            sage: G.save_image(png)
            sage: with open(png, 'rb') as fobj:
            ....:     assert fobj.read().startswith(b'\\x89PNG')

            sage: gif = tmp_filename(ext='.gif')
            sage: G.save_image(gif)
            sage: with open(gif, 'rb') as fobj:
            ....:     assert fobj.read().startswith(b'GIF')"""
    @overload
    def save_image(self, png) -> Any:
        """Graphics3d.save_image(self, filename, **kwds)

        File: /build/sagemath/src/sage/src/sage/plot/plot3d/base.pyx (starting at line 1827)

        Save a 2-D image rendering.

        The image type is determined by the extension of the filename.
        For example, this could be ``.png``, ``.jpg``, ``.gif``,
        ``.pdf``, ``.svg``.

        INPUT:

        - ``filename`` -- string; the file name under which to save
          the image

        Any further keyword arguments are passed to the renderer.

        EXAMPLES::

            sage: G = sphere()
            sage: png = tmp_filename(ext='.png')
            sage: G.save_image(png)
            sage: with open(png, 'rb') as fobj:
            ....:     assert fobj.read().startswith(b'\\x89PNG')

            sage: gif = tmp_filename(ext='.gif')
            sage: G.save_image(gif)
            sage: with open(gif, 'rb') as fobj:
            ....:     assert fobj.read().startswith(b'GIF')"""
    @overload
    def save_image(self, gif) -> Any:
        """Graphics3d.save_image(self, filename, **kwds)

        File: /build/sagemath/src/sage/src/sage/plot/plot3d/base.pyx (starting at line 1827)

        Save a 2-D image rendering.

        The image type is determined by the extension of the filename.
        For example, this could be ``.png``, ``.jpg``, ``.gif``,
        ``.pdf``, ``.svg``.

        INPUT:

        - ``filename`` -- string; the file name under which to save
          the image

        Any further keyword arguments are passed to the renderer.

        EXAMPLES::

            sage: G = sphere()
            sage: png = tmp_filename(ext='.png')
            sage: G.save_image(png)
            sage: with open(png, 'rb') as fobj:
            ....:     assert fobj.read().startswith(b'\\x89PNG')

            sage: gif = tmp_filename(ext='.gif')
            sage: G.save_image(gif)
            sage: with open(gif, 'rb') as fobj:
            ....:     assert fobj.read().startswith(b'GIF')"""
    def scale(self, *x) -> Any:
        """Graphics3d.scale(self, *x)

        File: /build/sagemath/src/sage/src/sage/plot/plot3d/base.pyx (starting at line 804)

        Return the object scaled in the x, y, and z directions.

        EXAMPLES::

            sage: G = dodecahedron() + dodecahedron(opacity=.5).scale(2)
            sage: G.show(aspect_ratio=1)
            sage: G = icosahedron() + icosahedron(opacity=.5).scale([1, 1/2, 2])
            sage: G.show(aspect_ratio=1)

        TESTS::

            sage: G = sphere((0, 0, 0), 1)
            sage: G.scale(2)
            Graphics3d Object
            sage: G.scale(1, 2, 1/2).show(aspect_ratio=1)
            sage: G.scale(2).bounding_box()
            ((-2.0, -2.0, -2.0), (2.0, 2.0, 2.0))"""
    def show(self, **kwds) -> Any:
        '''Graphics3d.show(self, **kwds)

        File: /build/sagemath/src/sage/src/sage/plot/plot3d/base.pyx (starting at line 1621)

        Display graphics immediately.

        This method attempts to display the graphics immediately,
        without waiting for the currently running code (if any) to
        return to the command line. Be careful, calling it from within
        a loop will potentially launch a large number of external
        viewer programs.

        INPUT:

        - ``viewer`` -- string (default: ``\'threejs\'``); how to view the plot.
          Admissible values are

           * ``\'threejs\'``: interactive web-based 3D viewer using JavaScript
             and a WebGL renderer

           * ``\'jmol\'``: interactive 3D viewer using Java

           * ``\'tachyon\'``: ray tracer generating a static PNG image;
             can produce high-resolution graphics, but does
             not show any text labels

           * ``\'canvas3d\'``: web-based 3D viewer using JavaScript
             and a canvas renderer (Sage notebook only)

        - ``verbosity`` -- display information about rendering
          the figure

        - ``figsize`` -- (default: 5) x or pair [x,y] for
          numbers, e.g., [5,5]; controls the size of the output figure.
          With \'tachyon\', the resolution (in number of pixels) is 100 times
          ``figsize``. This is ignored for the jmol embedded renderer.

        - ``aspect_ratio`` -- (default: ``\'automatic\'``) aspect
          ratio of the coordinate system itself; give [1,1,1] or 1 to make
          spheres look round

        - ``frame_aspect_ratio`` -- (default: ``\'automatic\'``)
          aspect ratio of frame that contains the 3d scene

        - ``zoom`` -- (default: 1) how zoomed in

        - ``frame`` -- boolean (default: ``True``); if ``True``, draw a
          bounding frame with labels

        - ``axes`` -- boolean (default: ``False``); if ``True``, draw coordinate
          axes

        - ``camera_position`` -- (for tachyon) (default: (2.3, 2.4, 2.0))
          the viewpoint, with respect to the cube
          $[-1,1]\\\\times[-1,1]\\\\times[-1,1]$,
          into which the bounding box of the scene
          is scaled and centered.
          The default viewing direction is towards the origin.

        - ``viewdir`` -- (for tachyon) (default: ``None``) three coordinates
          specifying the viewing direction

        - ``updir`` -- (for tachyon) (default: (0,0,1)) the "upward"
          direction of the camera

        - ``light_position`` -- (for tachyon) (default: (4,3,2)) the position
          of the single light source in the scene (in addition to ambient light)

        - ``antialiasing`` -- (for tachyon) (default: ``False``)

        - ``raydepth`` -- (for tachyon) (default: 8)
          see the :class:`sage.plot.plot3d.tachyon.Tachyon` class

        - ``shade`` -- (for tachyon) string (default: ``\'full\'``);
          shading options. Admissible values are

           * ``\'full\'``: best quality rendering (and slowest).
             Sets tachyon command line flag ``-fullshade``.

           * ``\'medium``: good quality rendering, but no shadows.
             Sets tachyon command line flag ``-mediumshade``.

           * ``\'low\'``: low quality rendering, preview (and fast).
             Sets tachyon command line flag ``-lowshade``.

           * ``\'lowest\'``: worst quality rendering, preview (and fastest).
             Sets tachyon command line flag ``-lowestshade``.

        - ``extra_opts`` -- (for tachyon) string (default: empty string);
          extra options that will be appended to the tachyon command line

        - ``**kwds`` -- other options, which make sense for particular
          rendering engines

        OUTPUT:

        This method does not return anything. Use :meth:`save` if you
        want to save the figure as an image file.

        .. WARNING::

            By default, the jmol and tachyon viewers perform
            some non-uniform scaling of the axes.

        If this is not desired, one can set ``aspect_ratio=1``::

            sage: p = plot3d(lambda u,v:(cos(u)-cos(v)), (-0.2,0.2),(-0.2,0.2))
            sage: p.show(viewer=\'threejs\')
            sage: p.show(viewer=\'jmol\')
            sage: p.show(viewer=\'jmol\',aspect_ratio=1)
            sage: p.show(viewer=\'tachyon\',camera_position=(4,0,0))
            sage: p.show(viewer=\'tachyon\',camera_position=(2,2,0.3),aspect_ratio=1)

        CHANGING DEFAULTS: Defaults can be uniformly changed by importing a
        dictionary and changing it. For example, here we change the default
        so images display without a frame instead of with one::

            sage: from sage.plot.plot3d.base import SHOW_DEFAULTS
            sage: SHOW_DEFAULTS[\'frame\'] = False

        This sphere will not have a frame around it::

            sage: sphere((0,0,0))
            Graphics3d Object

        We change the default back::

            sage: SHOW_DEFAULTS[\'frame\'] = True

        Now this sphere is enclosed in a frame::

            sage: sphere((0,0,0))
            Graphics3d Object

        EXAMPLES: We illustrate use of the ``aspect_ratio`` option::

            sage: x, y = var(\'x,y\')                                                     # needs sage.symbolic
            sage: p = plot3d(2*sin(x*y), (x, -pi, pi), (y, -pi, pi))                    # needs sage.symbolic
            sage: p.show(aspect_ratio=[1,1,1])                                          # needs sage.symbolic

        This looks flattened, but filled with the plot::

            sage: p.show(frame_aspect_ratio=[1,1,1/16])                                 # needs sage.symbolic

        This looks flattened, but the plot is square and smaller::

            sage: p.show(aspect_ratio=[1,1,1], frame_aspect_ratio=[1,1,1/8])            # needs sage.symbolic

        This example shows indirectly that the defaults
        from :func:`~sage.plot.plot.plot` are dealt with properly::

            sage: plot(vector([1,2,3]))
            Graphics3d Object

        We use the \'canvas3d\' backend from inside the notebook to get a view of
        the plot rendered inline using HTML canvas::

            sage: p.show(viewer=\'canvas3d\')                                             # needs sage.symbolic

        Sometimes shadows in Tachyon-produced images can lead to confusing
        plots. To remove them::

            sage: p.show(viewer=\'tachyon\', shade=\'medium\')                              # needs sage.symbolic

        One can also pass Tachyon command line flags directly. For example,
        the following line produces the same result as the previous one::

            sage: p.show(viewer=\'tachyon\', extra_opts=\'-mediumshade\')                   # needs sage.symbolic'''
    @overload
    def stl_ascii_string(self, name=...) -> Any:
        """Graphics3d.stl_ascii_string(self, name='surface')

        File: /build/sagemath/src/sage/src/sage/plot/plot3d/base.pyx (starting at line 2004)

        Return an STL (STereoLithography) representation of the surface.

        .. WARNING::

            This only works for surfaces, not for general plot objects!

        INPUT:

        - ``name`` -- string (default: ``'surface'``); name of the surface

        OUTPUT: string that represents the surface in the STL format

        See :wikipedia:`STL_(file_format)`

        .. SEEALSO:: :meth:`stl_binary`

        EXAMPLES::

            sage: # needs sage.symbolic
            sage: x,y,z = var('x,y,z')
            sage: a = implicit_plot3d(x^2+y^2+z^2-9,[x,-5,5],[y,-5,5],[z,-5,5])
            sage: astl = a.stl_ascii_string()
            sage: astl.splitlines()[:7]  # abs tol 1e-10
            ['solid surface',
            'facet normal 0.9733285267845754 -0.16222142113076257 -0.16222142113076257',
            '    outer loop',
            '        vertex 2.94871794872 -0.384615384615 -0.39358974359',
            '        vertex 2.95021367521 -0.384615384615 -0.384615384615',
            '        vertex 2.94871794872 -0.39358974359 -0.384615384615',
            '    endloop']

            sage: p = polygon3d([[0,0,0], [1,2,3], [3,0,0]])
            sage: print(p.stl_ascii_string(name='triangle'))
            solid triangle
            facet normal 0.0 0.8320502943378436 -0.5547001962252291
                outer loop
                    vertex 0.0 0.0 0.0
                    vertex 1.0 2.0 3.0
                    vertex 3.0 0.0 0.0
                endloop
            endfacet
            endsolid triangle

        Now works when faces have more then 3 sides::

            sage: # needs sage.geometry.polyhedron sage.groups
            sage: P = polytopes.dodecahedron()
            sage: Q = P.plot().all[-1]
            sage: print(Q.stl_ascii_string().splitlines()[:7])
            ['solid surface',
             'facet normal 0.0 0.5257311121191338 0.8506508083520399',
             '    outer loop',
             '        vertex -0.7639320225002102 0.7639320225002102 0.7639320225002102',
             '        vertex -0.4721359549995796 0.0 1.2360679774997898',
             '        vertex 0.4721359549995796 0.0 1.2360679774997898',
             '    endloop']"""
    @overload
    def stl_ascii_string(self) -> Any:
        """Graphics3d.stl_ascii_string(self, name='surface')

        File: /build/sagemath/src/sage/src/sage/plot/plot3d/base.pyx (starting at line 2004)

        Return an STL (STereoLithography) representation of the surface.

        .. WARNING::

            This only works for surfaces, not for general plot objects!

        INPUT:

        - ``name`` -- string (default: ``'surface'``); name of the surface

        OUTPUT: string that represents the surface in the STL format

        See :wikipedia:`STL_(file_format)`

        .. SEEALSO:: :meth:`stl_binary`

        EXAMPLES::

            sage: # needs sage.symbolic
            sage: x,y,z = var('x,y,z')
            sage: a = implicit_plot3d(x^2+y^2+z^2-9,[x,-5,5],[y,-5,5],[z,-5,5])
            sage: astl = a.stl_ascii_string()
            sage: astl.splitlines()[:7]  # abs tol 1e-10
            ['solid surface',
            'facet normal 0.9733285267845754 -0.16222142113076257 -0.16222142113076257',
            '    outer loop',
            '        vertex 2.94871794872 -0.384615384615 -0.39358974359',
            '        vertex 2.95021367521 -0.384615384615 -0.384615384615',
            '        vertex 2.94871794872 -0.39358974359 -0.384615384615',
            '    endloop']

            sage: p = polygon3d([[0,0,0], [1,2,3], [3,0,0]])
            sage: print(p.stl_ascii_string(name='triangle'))
            solid triangle
            facet normal 0.0 0.8320502943378436 -0.5547001962252291
                outer loop
                    vertex 0.0 0.0 0.0
                    vertex 1.0 2.0 3.0
                    vertex 3.0 0.0 0.0
                endloop
            endfacet
            endsolid triangle

        Now works when faces have more then 3 sides::

            sage: # needs sage.geometry.polyhedron sage.groups
            sage: P = polytopes.dodecahedron()
            sage: Q = P.plot().all[-1]
            sage: print(Q.stl_ascii_string().splitlines()[:7])
            ['solid surface',
             'facet normal 0.0 0.5257311121191338 0.8506508083520399',
             '    outer loop',
             '        vertex -0.7639320225002102 0.7639320225002102 0.7639320225002102',
             '        vertex -0.4721359549995796 0.0 1.2360679774997898',
             '        vertex 0.4721359549995796 0.0 1.2360679774997898',
             '    endloop']"""
    @overload
    def stl_ascii_string(self, name=...) -> Any:
        """Graphics3d.stl_ascii_string(self, name='surface')

        File: /build/sagemath/src/sage/src/sage/plot/plot3d/base.pyx (starting at line 2004)

        Return an STL (STereoLithography) representation of the surface.

        .. WARNING::

            This only works for surfaces, not for general plot objects!

        INPUT:

        - ``name`` -- string (default: ``'surface'``); name of the surface

        OUTPUT: string that represents the surface in the STL format

        See :wikipedia:`STL_(file_format)`

        .. SEEALSO:: :meth:`stl_binary`

        EXAMPLES::

            sage: # needs sage.symbolic
            sage: x,y,z = var('x,y,z')
            sage: a = implicit_plot3d(x^2+y^2+z^2-9,[x,-5,5],[y,-5,5],[z,-5,5])
            sage: astl = a.stl_ascii_string()
            sage: astl.splitlines()[:7]  # abs tol 1e-10
            ['solid surface',
            'facet normal 0.9733285267845754 -0.16222142113076257 -0.16222142113076257',
            '    outer loop',
            '        vertex 2.94871794872 -0.384615384615 -0.39358974359',
            '        vertex 2.95021367521 -0.384615384615 -0.384615384615',
            '        vertex 2.94871794872 -0.39358974359 -0.384615384615',
            '    endloop']

            sage: p = polygon3d([[0,0,0], [1,2,3], [3,0,0]])
            sage: print(p.stl_ascii_string(name='triangle'))
            solid triangle
            facet normal 0.0 0.8320502943378436 -0.5547001962252291
                outer loop
                    vertex 0.0 0.0 0.0
                    vertex 1.0 2.0 3.0
                    vertex 3.0 0.0 0.0
                endloop
            endfacet
            endsolid triangle

        Now works when faces have more then 3 sides::

            sage: # needs sage.geometry.polyhedron sage.groups
            sage: P = polytopes.dodecahedron()
            sage: Q = P.plot().all[-1]
            sage: print(Q.stl_ascii_string().splitlines()[:7])
            ['solid surface',
             'facet normal 0.0 0.5257311121191338 0.8506508083520399',
             '    outer loop',
             '        vertex -0.7639320225002102 0.7639320225002102 0.7639320225002102',
             '        vertex -0.4721359549995796 0.0 1.2360679774997898',
             '        vertex 0.4721359549995796 0.0 1.2360679774997898',
             '    endloop']"""
    @overload
    def stl_ascii_string(self) -> Any:
        """Graphics3d.stl_ascii_string(self, name='surface')

        File: /build/sagemath/src/sage/src/sage/plot/plot3d/base.pyx (starting at line 2004)

        Return an STL (STereoLithography) representation of the surface.

        .. WARNING::

            This only works for surfaces, not for general plot objects!

        INPUT:

        - ``name`` -- string (default: ``'surface'``); name of the surface

        OUTPUT: string that represents the surface in the STL format

        See :wikipedia:`STL_(file_format)`

        .. SEEALSO:: :meth:`stl_binary`

        EXAMPLES::

            sage: # needs sage.symbolic
            sage: x,y,z = var('x,y,z')
            sage: a = implicit_plot3d(x^2+y^2+z^2-9,[x,-5,5],[y,-5,5],[z,-5,5])
            sage: astl = a.stl_ascii_string()
            sage: astl.splitlines()[:7]  # abs tol 1e-10
            ['solid surface',
            'facet normal 0.9733285267845754 -0.16222142113076257 -0.16222142113076257',
            '    outer loop',
            '        vertex 2.94871794872 -0.384615384615 -0.39358974359',
            '        vertex 2.95021367521 -0.384615384615 -0.384615384615',
            '        vertex 2.94871794872 -0.39358974359 -0.384615384615',
            '    endloop']

            sage: p = polygon3d([[0,0,0], [1,2,3], [3,0,0]])
            sage: print(p.stl_ascii_string(name='triangle'))
            solid triangle
            facet normal 0.0 0.8320502943378436 -0.5547001962252291
                outer loop
                    vertex 0.0 0.0 0.0
                    vertex 1.0 2.0 3.0
                    vertex 3.0 0.0 0.0
                endloop
            endfacet
            endsolid triangle

        Now works when faces have more then 3 sides::

            sage: # needs sage.geometry.polyhedron sage.groups
            sage: P = polytopes.dodecahedron()
            sage: Q = P.plot().all[-1]
            sage: print(Q.stl_ascii_string().splitlines()[:7])
            ['solid surface',
             'facet normal 0.0 0.5257311121191338 0.8506508083520399',
             '    outer loop',
             '        vertex -0.7639320225002102 0.7639320225002102 0.7639320225002102',
             '        vertex -0.4721359549995796 0.0 1.2360679774997898',
             '        vertex 0.4721359549995796 0.0 1.2360679774997898',
             '    endloop']"""
    @overload
    def stl_binary(self) -> Any:
        """Graphics3d.stl_binary(self)

        File: /build/sagemath/src/sage/src/sage/plot/plot3d/base.pyx (starting at line 1960)

        Return an STL (STereoLithography) binary representation of the surface.

        .. WARNING::

            This only works for surfaces, transforms and unions of surfaces,
            but not for general plot objects!

        OUTPUT: a binary string that represents the surface in the binary STL format

        See :wikipedia:`STL_(file_format)`

        .. SEEALSO:: :meth:`stl_ascii_string`

        EXAMPLES::

            sage: # needs sage.symbolic
            sage: x,y,z = var('x,y,z')
            sage: a = implicit_plot3d(x^2+y^2+z^2-9,[x,-5,5],[y,-5,5],[z,-5,5])
            sage: astl = a.stl_binary()
            sage: print(astl[:40].decode('ascii'))
            STL binary file / made by SageMath / ###

            sage: p = polygon3d([[0,0,0], [1,2,3], [3,0,0]])
            sage: print(p.stl_binary()[:40].decode('ascii'))
            STL binary file / made by SageMath / ###

        This works when faces have more then 3 sides::

            sage: # needs sage.geometry.polyhedron sage.groups
            sage: P = polytopes.dodecahedron()
            sage: Q = P.plot().all[-1]
            sage: print(Q.stl_binary()[:40].decode('ascii'))
            STL binary file / made by SageMath / ###"""
    @overload
    def stl_binary(self) -> Any:
        """Graphics3d.stl_binary(self)

        File: /build/sagemath/src/sage/src/sage/plot/plot3d/base.pyx (starting at line 1960)

        Return an STL (STereoLithography) binary representation of the surface.

        .. WARNING::

            This only works for surfaces, transforms and unions of surfaces,
            but not for general plot objects!

        OUTPUT: a binary string that represents the surface in the binary STL format

        See :wikipedia:`STL_(file_format)`

        .. SEEALSO:: :meth:`stl_ascii_string`

        EXAMPLES::

            sage: # needs sage.symbolic
            sage: x,y,z = var('x,y,z')
            sage: a = implicit_plot3d(x^2+y^2+z^2-9,[x,-5,5],[y,-5,5],[z,-5,5])
            sage: astl = a.stl_binary()
            sage: print(astl[:40].decode('ascii'))
            STL binary file / made by SageMath / ###

            sage: p = polygon3d([[0,0,0], [1,2,3], [3,0,0]])
            sage: print(p.stl_binary()[:40].decode('ascii'))
            STL binary file / made by SageMath / ###

        This works when faces have more then 3 sides::

            sage: # needs sage.geometry.polyhedron sage.groups
            sage: P = polytopes.dodecahedron()
            sage: Q = P.plot().all[-1]
            sage: print(Q.stl_binary()[:40].decode('ascii'))
            STL binary file / made by SageMath / ###"""
    @overload
    def stl_binary(self) -> Any:
        """Graphics3d.stl_binary(self)

        File: /build/sagemath/src/sage/src/sage/plot/plot3d/base.pyx (starting at line 1960)

        Return an STL (STereoLithography) binary representation of the surface.

        .. WARNING::

            This only works for surfaces, transforms and unions of surfaces,
            but not for general plot objects!

        OUTPUT: a binary string that represents the surface in the binary STL format

        See :wikipedia:`STL_(file_format)`

        .. SEEALSO:: :meth:`stl_ascii_string`

        EXAMPLES::

            sage: # needs sage.symbolic
            sage: x,y,z = var('x,y,z')
            sage: a = implicit_plot3d(x^2+y^2+z^2-9,[x,-5,5],[y,-5,5],[z,-5,5])
            sage: astl = a.stl_binary()
            sage: print(astl[:40].decode('ascii'))
            STL binary file / made by SageMath / ###

            sage: p = polygon3d([[0,0,0], [1,2,3], [3,0,0]])
            sage: print(p.stl_binary()[:40].decode('ascii'))
            STL binary file / made by SageMath / ###

        This works when faces have more then 3 sides::

            sage: # needs sage.geometry.polyhedron sage.groups
            sage: P = polytopes.dodecahedron()
            sage: Q = P.plot().all[-1]
            sage: print(Q.stl_binary()[:40].decode('ascii'))
            STL binary file / made by SageMath / ###"""
    @overload
    def stl_binary(self) -> Any:
        """Graphics3d.stl_binary(self)

        File: /build/sagemath/src/sage/src/sage/plot/plot3d/base.pyx (starting at line 1960)

        Return an STL (STereoLithography) binary representation of the surface.

        .. WARNING::

            This only works for surfaces, transforms and unions of surfaces,
            but not for general plot objects!

        OUTPUT: a binary string that represents the surface in the binary STL format

        See :wikipedia:`STL_(file_format)`

        .. SEEALSO:: :meth:`stl_ascii_string`

        EXAMPLES::

            sage: # needs sage.symbolic
            sage: x,y,z = var('x,y,z')
            sage: a = implicit_plot3d(x^2+y^2+z^2-9,[x,-5,5],[y,-5,5],[z,-5,5])
            sage: astl = a.stl_binary()
            sage: print(astl[:40].decode('ascii'))
            STL binary file / made by SageMath / ###

            sage: p = polygon3d([[0,0,0], [1,2,3], [3,0,0]])
            sage: print(p.stl_binary()[:40].decode('ascii'))
            STL binary file / made by SageMath / ###

        This works when faces have more then 3 sides::

            sage: # needs sage.geometry.polyhedron sage.groups
            sage: P = polytopes.dodecahedron()
            sage: Q = P.plot().all[-1]
            sage: print(Q.stl_binary()[:40].decode('ascii'))
            STL binary file / made by SageMath / ###"""
    def tachyon(self, *args, **kwargs):
        """Graphics3d.tachyon(self, zoom=1.0, antialiasing=False, figsize=[5, 5], raydepth=8, camera_position=[2.3, 2.4, 2.0], updir=[0, 0, 1], light_position=[4.0, 3.0, 2.0], viewdir=None)

        File: /build/sagemath/src/sage/src/sage/plot/plot3d/base.pyx (starting at line 1009)

        A tachyon input file (as a string) containing the this object.

        EXAMPLES::

            sage: print(sphere((1, 2, 3), 5, color='yellow').tachyon())
            <BLANKLINE>
            begin_scene
            resolution 500 500
            <BLANKLINE>
                     camera
                    ...
                  plane
                    center -592.870151560437 618.647114671761 -515.539262226467
                    normal -2.3 2.4 -2.0
                    TEXTURE
                        AMBIENT 1.0 DIFFUSE 0.0 SPECULAR 0.0 OPACITY 1.0
                        COLOR 1.0 1.0 1.0
                        TEXFUNC 0
            <BLANKLINE>
                Texdef texture...
              Ambient 0.3333333333333333 Diffuse 0.6666666666666666 Specular 0.0 Opacity 1.0
              Color 1.0 1.0 0.0
              TexFunc 0
            <BLANKLINE>
                Sphere center 1.0 -2.0 3.0 Rad 5.0 texture...
            <BLANKLINE>
            end_scene

            sage: G = icosahedron(color='red') + sphere((1,2,3), 0.5, color='yellow')
            sage: G.show(viewer='tachyon', frame=false)
            sage: print(G.tachyon())
            begin_scene
            ...
            Texdef texture...
              Ambient 0.3333333333333333 Diffuse 0.6666666666666666 Specular 0.0 Opacity 1.0
               Color 1.0 1.0 0.0
               TexFunc 0
            TRI V0 ...
            Sphere center 1.0 -2.0 3.0 Rad 0.5 texture...
            end_scene"""
    def tachyon_repr(self, render_params) -> Any:
        """Graphics3d.tachyon_repr(self, render_params)

        File: /build/sagemath/src/sage/src/sage/plot/plot3d/base.pyx (starting at line 1318)

        A (possibly nested) list of strings which will be concatenated and
        used by tachyon to render the object.

        (Nested lists of strings are used because otherwise all the
        intermediate concatenations can kill performance). This may
        include a reference to color information which is stored
        elsewhere.

        EXAMPLES::

            sage: G = sage.plot.plot3d.base.Graphics3d()
            sage: G.tachyon_repr(G.default_render_params())
            []
            sage: G = sphere((1, 2, 3))
            sage: G.tachyon_repr(G.default_render_params())
            ['Sphere center 1.0 2.0 3.0 Rad 1.0 texture...']"""
    @overload
    def testing_render_params(self) -> Any:
        """Graphics3d.testing_render_params(self)

        File: /build/sagemath/src/sage/src/sage/plot/plot3d/base.pyx (starting at line 913)

        Return an instance of RenderParams suitable for testing this object.

        In particular, it opens up a temporary file as an auxiliary zip
        file for jmol.

        EXAMPLES::

            sage: type(dodecahedron().testing_render_params())
            <class 'sage.plot.plot3d.base.RenderParams'>"""
    @overload
    def testing_render_params(self) -> Any:
        """Graphics3d.testing_render_params(self)

        File: /build/sagemath/src/sage/src/sage/plot/plot3d/base.pyx (starting at line 913)

        Return an instance of RenderParams suitable for testing this object.

        In particular, it opens up a temporary file as an auxiliary zip
        file for jmol.

        EXAMPLES::

            sage: type(dodecahedron().testing_render_params())
            <class 'sage.plot.plot3d.base.RenderParams'>"""
    @overload
    def texture_set(self) -> Any:
        """Graphics3d.texture_set(self)

        File: /build/sagemath/src/sage/src/sage/plot/plot3d/base.pyx (starting at line 1390)

        Often the textures of a 3d file format are kept separate from the
        objects themselves. This function returns the set of textures used,
        so they can be defined in a preamble or separate file.

        EXAMPLES::

            sage: sage.plot.plot3d.base.Graphics3d().texture_set()
            set()

            sage: G = tetrahedron(color='red') + tetrahedron(color='yellow') + tetrahedron(color='red', opacity=0.5)
            sage: [t for t in G.texture_set() if t.color == colors.red] # we should have two red textures
            [Texture(texture..., red, ff0000), Texture(texture..., red, ff0000)]
            sage: [t for t in G.texture_set() if t.color == colors.yellow] # ...and one yellow
            [Texture(texture..., yellow, ffff00)]"""
    @overload
    def texture_set(self) -> Any:
        """Graphics3d.texture_set(self)

        File: /build/sagemath/src/sage/src/sage/plot/plot3d/base.pyx (starting at line 1390)

        Often the textures of a 3d file format are kept separate from the
        objects themselves. This function returns the set of textures used,
        so they can be defined in a preamble or separate file.

        EXAMPLES::

            sage: sage.plot.plot3d.base.Graphics3d().texture_set()
            set()

            sage: G = tetrahedron(color='red') + tetrahedron(color='yellow') + tetrahedron(color='red', opacity=0.5)
            sage: [t for t in G.texture_set() if t.color == colors.red] # we should have two red textures
            [Texture(texture..., red, ff0000), Texture(texture..., red, ff0000)]
            sage: [t for t in G.texture_set() if t.color == colors.yellow] # ...and one yellow
            [Texture(texture..., yellow, ffff00)]"""
    @overload
    def texture_set(self) -> Any:
        """Graphics3d.texture_set(self)

        File: /build/sagemath/src/sage/src/sage/plot/plot3d/base.pyx (starting at line 1390)

        Often the textures of a 3d file format are kept separate from the
        objects themselves. This function returns the set of textures used,
        so they can be defined in a preamble or separate file.

        EXAMPLES::

            sage: sage.plot.plot3d.base.Graphics3d().texture_set()
            set()

            sage: G = tetrahedron(color='red') + tetrahedron(color='yellow') + tetrahedron(color='red', opacity=0.5)
            sage: [t for t in G.texture_set() if t.color == colors.red] # we should have two red textures
            [Texture(texture..., red, ff0000), Texture(texture..., red, ff0000)]
            sage: [t for t in G.texture_set() if t.color == colors.yellow] # ...and one yellow
            [Texture(texture..., yellow, ffff00)]"""
    @overload
    def texture_set(self) -> Any:
        """Graphics3d.texture_set(self)

        File: /build/sagemath/src/sage/src/sage/plot/plot3d/base.pyx (starting at line 1390)

        Often the textures of a 3d file format are kept separate from the
        objects themselves. This function returns the set of textures used,
        so they can be defined in a preamble or separate file.

        EXAMPLES::

            sage: sage.plot.plot3d.base.Graphics3d().texture_set()
            set()

            sage: G = tetrahedron(color='red') + tetrahedron(color='yellow') + tetrahedron(color='red', opacity=0.5)
            sage: [t for t in G.texture_set() if t.color == colors.red] # we should have two red textures
            [Texture(texture..., red, ff0000), Texture(texture..., red, ff0000)]
            sage: [t for t in G.texture_set() if t.color == colors.yellow] # ...and one yellow
            [Texture(texture..., yellow, ffff00)]"""
    def threejs_repr(self, render_params) -> Any:
        """Graphics3d.threejs_repr(self, render_params)

        File: /build/sagemath/src/sage/src/sage/plot/plot3d/base.pyx (starting at line 1376)

        A flat list of ``(kind, desc)`` tuples where ``kind`` is one of:
        'point', 'line', 'text', or 'surface'; and where ``desc`` is a dictionary
        describing a point, line, text, or surface.

        EXAMPLES::

            sage: G = sage.plot.plot3d.base.Graphics3d()
            sage: G.threejs_repr(G.default_render_params())
            []"""
    @overload
    def transform(self, **kwds) -> Any:
        """Graphics3d.transform(self, **kwds)

        File: /build/sagemath/src/sage/src/sage/plot/plot3d/base.pyx (starting at line 763)

        Apply a transformation, where the inputs are
        passed onto a TransformGroup object.

        Mostly for internal use; see the translate, scale, and rotate
        methods for more details.

        EXAMPLES::

            sage: sphere((0,0,0), 1).transform(trans=(1, 0, 0), scale=(2,3,4)).bounding_box()
            ((-1.0, -3.0, -4.0), (3.0, 3.0, 4.0))"""
    @overload
    def transform(self, trans=..., scale=...) -> Any:
        """Graphics3d.transform(self, **kwds)

        File: /build/sagemath/src/sage/src/sage/plot/plot3d/base.pyx (starting at line 763)

        Apply a transformation, where the inputs are
        passed onto a TransformGroup object.

        Mostly for internal use; see the translate, scale, and rotate
        methods for more details.

        EXAMPLES::

            sage: sphere((0,0,0), 1).transform(trans=(1, 0, 0), scale=(2,3,4)).bounding_box()
            ((-1.0, -3.0, -4.0), (3.0, 3.0, 4.0))"""
    def translate(self, *x) -> Any:
        """Graphics3d.translate(self, *x)

        File: /build/sagemath/src/sage/src/sage/plot/plot3d/base.pyx (starting at line 778)

        Return the object translated by the given vector (which can be
        given either as a 3-iterable or via positional arguments).

        EXAMPLES::

            sage: icosahedron() + sum(icosahedron(opacity=0.25).translate(2*n, 0, 0) for n in [1..4])
            Graphics3d Object
            sage: icosahedron() + sum(icosahedron(opacity=0.25).translate([-2*n, n, n^2]) for n in [1..4])
            Graphics3d Object

        TESTS::

            sage: G = sphere((0, 0, 0), 1)
            sage: G.bounding_box()
            ((-1.0, -1.0, -1.0), (1.0, 1.0, 1.0))
            sage: G.translate(0, 0, 1).bounding_box()
            ((-1.0, -1.0, 0.0), (1.0, 1.0, 2.0))
            sage: G.translate(-1, 5, 0).bounding_box()
            ((-2.0, 4.0, -1.0), (0.0, 6.0, 1.0))"""
    @overload
    def viewpoint(self) -> Any:
        """Graphics3d.viewpoint(self)

        File: /build/sagemath/src/sage/src/sage/plot/plot3d/base.pyx (starting at line 888)

        Return the viewpoint of this plot.

        Currently only a stub for x3d.

        EXAMPLES::

            sage: type(dodecahedron().viewpoint())
            <class 'sage.plot.plot3d.base.Viewpoint'>"""
    @overload
    def viewpoint(self) -> Any:
        """Graphics3d.viewpoint(self)

        File: /build/sagemath/src/sage/src/sage/plot/plot3d/base.pyx (starting at line 888)

        Return the viewpoint of this plot.

        Currently only a stub for x3d.

        EXAMPLES::

            sage: type(dodecahedron().viewpoint())
            <class 'sage.plot.plot3d.base.Viewpoint'>"""
    @overload
    def x3d(self) -> Any:
        """Graphics3d.x3d(self)

        File: /build/sagemath/src/sage/src/sage/plot/plot3d/base.pyx (starting at line 930)

        An x3d scene file (as a string) containing the this object.

        EXAMPLES::

            sage: print(sphere((1, 2, 3), 5).x3d())
            <X3D version='3.0' profile='Immersive' xmlns:xsd='http://www.w3.org/2001/XMLSchema-instance' xsd:noNamespaceSchemaLocation=' http://www.web3d.org/specifications/x3d-3.0.xsd '>
            <head>
            <meta name='title' content='sage3d'/>
            </head>
            <Scene>
            <Viewpoint position='0 0 6'/>
            <Transform translation='1 2 3'>
            <Shape><Sphere radius='5.0'/><Appearance><Material diffuseColor='0.4 0.4 1.0' shininess='1.0' specularColor='0.0 0.0 0.0'/></Appearance></Shape>
            </Transform>
            </Scene>
            </X3D>

            sage: G = icosahedron() + sphere((0,0,0), 0.5, color='red')
            sage: print(G.x3d())
            <X3D version='3.0' profile='Immersive' xmlns:xsd='http://www.w3.org/2001/XMLSchema-instance' xsd:noNamespaceSchemaLocation=' http://www.web3d.org/specifications/x3d-3.0.xsd '>
            <head>
            <meta name='title' content='sage3d'/>
            </head>
            <Scene>
            <Viewpoint position='0 0 6'/>
            <Shape>
            <IndexedFaceSet coordIndex='...'>
              <Coordinate point='...'/>
            </IndexedFaceSet>
            <Appearance><Material diffuseColor='0.4 0.4 1.0' shininess='1.0' specularColor='0.0 0.0 0.0'/></Appearance></Shape>
            <Transform translation='0 0 0'>
            <Shape><Sphere radius='0.5'/><Appearance><Material diffuseColor='1.0 0.0 0.0' shininess='1.0' specularColor='0.0 0.0 0.0'/></Appearance></Shape>
            </Transform>
            </Scene>
            </X3D>"""
    @overload
    def x3d(self) -> Any:
        """Graphics3d.x3d(self)

        File: /build/sagemath/src/sage/src/sage/plot/plot3d/base.pyx (starting at line 930)

        An x3d scene file (as a string) containing the this object.

        EXAMPLES::

            sage: print(sphere((1, 2, 3), 5).x3d())
            <X3D version='3.0' profile='Immersive' xmlns:xsd='http://www.w3.org/2001/XMLSchema-instance' xsd:noNamespaceSchemaLocation=' http://www.web3d.org/specifications/x3d-3.0.xsd '>
            <head>
            <meta name='title' content='sage3d'/>
            </head>
            <Scene>
            <Viewpoint position='0 0 6'/>
            <Transform translation='1 2 3'>
            <Shape><Sphere radius='5.0'/><Appearance><Material diffuseColor='0.4 0.4 1.0' shininess='1.0' specularColor='0.0 0.0 0.0'/></Appearance></Shape>
            </Transform>
            </Scene>
            </X3D>

            sage: G = icosahedron() + sphere((0,0,0), 0.5, color='red')
            sage: print(G.x3d())
            <X3D version='3.0' profile='Immersive' xmlns:xsd='http://www.w3.org/2001/XMLSchema-instance' xsd:noNamespaceSchemaLocation=' http://www.web3d.org/specifications/x3d-3.0.xsd '>
            <head>
            <meta name='title' content='sage3d'/>
            </head>
            <Scene>
            <Viewpoint position='0 0 6'/>
            <Shape>
            <IndexedFaceSet coordIndex='...'>
              <Coordinate point='...'/>
            </IndexedFaceSet>
            <Appearance><Material diffuseColor='0.4 0.4 1.0' shininess='1.0' specularColor='0.0 0.0 0.0'/></Appearance></Shape>
            <Transform translation='0 0 0'>
            <Shape><Sphere radius='0.5'/><Appearance><Material diffuseColor='1.0 0.0 0.0' shininess='1.0' specularColor='0.0 0.0 0.0'/></Appearance></Shape>
            </Transform>
            </Scene>
            </X3D>"""
    @overload
    def x3d(self) -> Any:
        """Graphics3d.x3d(self)

        File: /build/sagemath/src/sage/src/sage/plot/plot3d/base.pyx (starting at line 930)

        An x3d scene file (as a string) containing the this object.

        EXAMPLES::

            sage: print(sphere((1, 2, 3), 5).x3d())
            <X3D version='3.0' profile='Immersive' xmlns:xsd='http://www.w3.org/2001/XMLSchema-instance' xsd:noNamespaceSchemaLocation=' http://www.web3d.org/specifications/x3d-3.0.xsd '>
            <head>
            <meta name='title' content='sage3d'/>
            </head>
            <Scene>
            <Viewpoint position='0 0 6'/>
            <Transform translation='1 2 3'>
            <Shape><Sphere radius='5.0'/><Appearance><Material diffuseColor='0.4 0.4 1.0' shininess='1.0' specularColor='0.0 0.0 0.0'/></Appearance></Shape>
            </Transform>
            </Scene>
            </X3D>

            sage: G = icosahedron() + sphere((0,0,0), 0.5, color='red')
            sage: print(G.x3d())
            <X3D version='3.0' profile='Immersive' xmlns:xsd='http://www.w3.org/2001/XMLSchema-instance' xsd:noNamespaceSchemaLocation=' http://www.web3d.org/specifications/x3d-3.0.xsd '>
            <head>
            <meta name='title' content='sage3d'/>
            </head>
            <Scene>
            <Viewpoint position='0 0 6'/>
            <Shape>
            <IndexedFaceSet coordIndex='...'>
              <Coordinate point='...'/>
            </IndexedFaceSet>
            <Appearance><Material diffuseColor='0.4 0.4 1.0' shininess='1.0' specularColor='0.0 0.0 0.0'/></Appearance></Shape>
            <Transform translation='0 0 0'>
            <Shape><Sphere radius='0.5'/><Appearance><Material diffuseColor='1.0 0.0 0.0' shininess='1.0' specularColor='0.0 0.0 0.0'/></Appearance></Shape>
            </Transform>
            </Scene>
            </X3D>"""
    def __add__(self, left, right) -> Any:
        """Graphics3d.__add__(left, right)

        File: /build/sagemath/src/sage/src/sage/plot/plot3d/base.pyx (starting at line 591)

        Addition of objects adds them to the same scene.

        EXAMPLES::

            sage: A = sphere((0,0,0), 1, color='red')
            sage: B = dodecahedron((2, 0, 0), color='yellow')
            sage: A+B
            Graphics3d Object

        For convenience, we take 0 and ``None`` to be the additive identity::

            sage: A + 0 is A
            True
            sage: A + None is A, 0 + A is A, None + A is A
            (True, True, True)

        In particular, this allows us to use the sum() function without
        having to provide an empty starting object::

            sage: sum(point3d((cos(n), sin(n), n)) for n in [0..10, step=.1])
            Graphics3d Object

        A Graphics 3d object and a 2d object can also be added::

            sage: A = sphere((0, 0, 0), 1) + circle((0, 0), 1.5)
            sage: A.show(aspect_ratio=1)"""
    def __hash__(self) -> Any:
        """Graphics3d.__hash__(self)

        File: /build/sagemath/src/sage/src/sage/plot/plot3d/base.pyx (starting at line 97)

        TESTS::

            sage: from sage.plot.plot3d.base import Graphics3d
            sage: hash(Graphics3d()) # random
            140658972348064"""
    def __radd__(self, other):
        """Return value+self."""

class Graphics3dGroup(Graphics3d):
    """File: /build/sagemath/src/sage/src/sage/plot/plot3d/base.pyx (starting at line 2251)

        This class represents a collection of 3d objects. Usually they are formed
        implicitly by summing.
    """
    def __init__(self, all=..., rot=..., trans=..., scale=..., T=...) -> Any:
        """Graphics3dGroup.__init__(self, all=(), rot=None, trans=None, scale=None, T=None)

        File: /build/sagemath/src/sage/src/sage/plot/plot3d/base.pyx (starting at line 2256)

        EXAMPLES::

            sage: sage.plot.plot3d.base.Graphics3dGroup([icosahedron(), dodecahedron(opacity=.5)])
            Graphics3d Object
            sage: type(icosahedron() + dodecahedron(opacity=.5))
            <class 'sage.plot.plot3d.base.Graphics3dGroup'>"""
    @overload
    def bounding_box(self) -> Any:
        """Graphics3dGroup.bounding_box(self)

        File: /build/sagemath/src/sage/src/sage/plot/plot3d/base.pyx (starting at line 2300)

        Box that contains the bounding boxes of
        the objects.

        EXAMPLES::

            sage: A = sphere((0,0,0), 5)
            sage: B = sphere((1, 5, 10), 1)
            sage: A.bounding_box()
            ((-5.0, -5.0, -5.0), (5.0, 5.0, 5.0))
            sage: B.bounding_box()
            ((0.0, 4.0, 9.0), (2.0, 6.0, 11.0))
            sage: (A+B).bounding_box()
            ((-5.0, -5.0, -5.0), (5.0, 6.0, 11.0))
            sage: (A+B).show(aspect_ratio=1, frame=True)

            sage: sage.plot.plot3d.base.Graphics3dGroup([]).bounding_box()
            ((0.0, 0.0, 0.0), (0.0, 0.0, 0.0))"""
    @overload
    def bounding_box(self) -> Any:
        """Graphics3dGroup.bounding_box(self)

        File: /build/sagemath/src/sage/src/sage/plot/plot3d/base.pyx (starting at line 2300)

        Box that contains the bounding boxes of
        the objects.

        EXAMPLES::

            sage: A = sphere((0,0,0), 5)
            sage: B = sphere((1, 5, 10), 1)
            sage: A.bounding_box()
            ((-5.0, -5.0, -5.0), (5.0, 5.0, 5.0))
            sage: B.bounding_box()
            ((0.0, 4.0, 9.0), (2.0, 6.0, 11.0))
            sage: (A+B).bounding_box()
            ((-5.0, -5.0, -5.0), (5.0, 6.0, 11.0))
            sage: (A+B).show(aspect_ratio=1, frame=True)

            sage: sage.plot.plot3d.base.Graphics3dGroup([]).bounding_box()
            ((0.0, 0.0, 0.0), (0.0, 0.0, 0.0))"""
    @overload
    def bounding_box(self) -> Any:
        """Graphics3dGroup.bounding_box(self)

        File: /build/sagemath/src/sage/src/sage/plot/plot3d/base.pyx (starting at line 2300)

        Box that contains the bounding boxes of
        the objects.

        EXAMPLES::

            sage: A = sphere((0,0,0), 5)
            sage: B = sphere((1, 5, 10), 1)
            sage: A.bounding_box()
            ((-5.0, -5.0, -5.0), (5.0, 5.0, 5.0))
            sage: B.bounding_box()
            ((0.0, 4.0, 9.0), (2.0, 6.0, 11.0))
            sage: (A+B).bounding_box()
            ((-5.0, -5.0, -5.0), (5.0, 6.0, 11.0))
            sage: (A+B).show(aspect_ratio=1, frame=True)

            sage: sage.plot.plot3d.base.Graphics3dGroup([]).bounding_box()
            ((0.0, 0.0, 0.0), (0.0, 0.0, 0.0))"""
    @overload
    def bounding_box(self) -> Any:
        """Graphics3dGroup.bounding_box(self)

        File: /build/sagemath/src/sage/src/sage/plot/plot3d/base.pyx (starting at line 2300)

        Box that contains the bounding boxes of
        the objects.

        EXAMPLES::

            sage: A = sphere((0,0,0), 5)
            sage: B = sphere((1, 5, 10), 1)
            sage: A.bounding_box()
            ((-5.0, -5.0, -5.0), (5.0, 5.0, 5.0))
            sage: B.bounding_box()
            ((0.0, 4.0, 9.0), (2.0, 6.0, 11.0))
            sage: (A+B).bounding_box()
            ((-5.0, -5.0, -5.0), (5.0, 6.0, 11.0))
            sage: (A+B).show(aspect_ratio=1, frame=True)

            sage: sage.plot.plot3d.base.Graphics3dGroup([]).bounding_box()
            ((0.0, 0.0, 0.0), (0.0, 0.0, 0.0))"""
    @overload
    def bounding_box(self) -> Any:
        """Graphics3dGroup.bounding_box(self)

        File: /build/sagemath/src/sage/src/sage/plot/plot3d/base.pyx (starting at line 2300)

        Box that contains the bounding boxes of
        the objects.

        EXAMPLES::

            sage: A = sphere((0,0,0), 5)
            sage: B = sphere((1, 5, 10), 1)
            sage: A.bounding_box()
            ((-5.0, -5.0, -5.0), (5.0, 5.0, 5.0))
            sage: B.bounding_box()
            ((0.0, 4.0, 9.0), (2.0, 6.0, 11.0))
            sage: (A+B).bounding_box()
            ((-5.0, -5.0, -5.0), (5.0, 6.0, 11.0))
            sage: (A+B).show(aspect_ratio=1, frame=True)

            sage: sage.plot.plot3d.base.Graphics3dGroup([]).bounding_box()
            ((0.0, 0.0, 0.0), (0.0, 0.0, 0.0))"""
    @overload
    def flatten(self) -> Any:
        """Graphics3dGroup.flatten(self)

        File: /build/sagemath/src/sage/src/sage/plot/plot3d/base.pyx (starting at line 2519)

        Try to reduce the depth of the scene tree by consolidating groups
        and transformations.

        EXAMPLES::

            sage: G = sum([circle((0, 0), t) for t in [1..10]], sphere()); G
            Graphics3d Object
            sage: G.flatten()
            Graphics3d Object
            sage: len(G.all)
            2
            sage: len(G.flatten().all)
            11"""
    @overload
    def flatten(self) -> Any:
        """Graphics3dGroup.flatten(self)

        File: /build/sagemath/src/sage/src/sage/plot/plot3d/base.pyx (starting at line 2519)

        Try to reduce the depth of the scene tree by consolidating groups
        and transformations.

        EXAMPLES::

            sage: G = sum([circle((0, 0), t) for t in [1..10]], sphere()); G
            Graphics3d Object
            sage: G.flatten()
            Graphics3d Object
            sage: len(G.all)
            2
            sage: len(G.flatten().all)
            11"""
    @overload
    def flatten(self) -> Any:
        """Graphics3dGroup.flatten(self)

        File: /build/sagemath/src/sage/src/sage/plot/plot3d/base.pyx (starting at line 2519)

        Try to reduce the depth of the scene tree by consolidating groups
        and transformations.

        EXAMPLES::

            sage: G = sum([circle((0, 0), t) for t in [1..10]], sphere()); G
            Graphics3d Object
            sage: G.flatten()
            Graphics3d Object
            sage: len(G.all)
            2
            sage: len(G.flatten().all)
            11"""
    def jmol_repr(self, render_params) -> Any:
        """Graphics3dGroup.jmol_repr(self, render_params)

        File: /build/sagemath/src/sage/src/sage/plot/plot3d/base.pyx (starting at line 2431)

        The jmol representation of a group is simply the concatenation of
        the representation of its objects.

        EXAMPLES::

            sage: G = sphere() + sphere((1,2,3))
            sage: G.jmol_repr(G.default_render_params())
            [[['isosurface sphere_1  center {0.0 0.0 0.0} sphere 1.0\\ncolor isosurface  [102,102,255]']],
             [['isosurface sphere_2  center {1.0 2.0 3.0} sphere 1.0\\ncolor isosurface  [102,102,255]']]]"""
    def json_repr(self, render_params) -> Any:
        '''Graphics3dGroup.json_repr(self, render_params)

        File: /build/sagemath/src/sage/src/sage/plot/plot3d/base.pyx (starting at line 2358)

        The JSON representation of a group is simply the concatenation of the
        representations of its objects.

        EXAMPLES::

            sage: G = sphere() + sphere((1, 2, 3))
            sage: G.json_repr(G.default_render_params())
            [[[\'{"vertices":...\']], [[\'{"vertices":...\']]]'''
    def obj_repr(self, render_params) -> Any:
        """Graphics3dGroup.obj_repr(self, render_params)

        File: /build/sagemath/src/sage/src/sage/plot/plot3d/base.pyx (starting at line 2403)

        The obj representation of a group is simply the concatenation of
        the representation of its objects.

        EXAMPLES::

            sage: G = tetrahedron() + tetrahedron().translate(10, 10, 10)
            sage: G.obj_repr(G.default_render_params())
            [['g obj_1',
              'usemtl ...',
              ['v 0 0 1',
               'v 0.942809 0 -0.333333',
               'v -0.471405 0.816497 -0.333333',
               'v -0.471405 -0.816497 -0.333333'],
              ['f 1 2 3', 'f 2 4 3', 'f 1 3 4', 'f 1 4 2'],
              []],
             [['g obj_2',
               'usemtl ...',
               ['v 10 10 11',
                'v 10.9428 10 9.66667',
                'v 9.5286 10.8165 9.66667',
                'v 9.5286 9.1835 9.66667'],
               ['f 5 6 7', 'f 6 8 7', 'f 5 7 8', 'f 5 8 6'],
               []]]]"""
    def plot(self) -> Any:
        """Graphics3dGroup.plot(self)

        File: /build/sagemath/src/sage/src/sage/plot/plot3d/base.pyx (starting at line 2546)"""
    @overload
    def set_texture(self, **kwds) -> Any:
        """Graphics3dGroup.set_texture(self, **kwds)

        File: /build/sagemath/src/sage/src/sage/plot/plot3d/base.pyx (starting at line 2344)

        EXAMPLES::

            sage: G = dodecahedron(color='red', opacity=.5) + icosahedron((3, 0, 0), color='blue')
            sage: G
            Graphics3d Object
            sage: G.set_texture(color='yellow')
            sage: G
            Graphics3d Object"""
    @overload
    def set_texture(self, color=...) -> Any:
        """Graphics3dGroup.set_texture(self, **kwds)

        File: /build/sagemath/src/sage/src/sage/plot/plot3d/base.pyx (starting at line 2344)

        EXAMPLES::

            sage: G = dodecahedron(color='red', opacity=.5) + icosahedron((3, 0, 0), color='blue')
            sage: G
            Graphics3d Object
            sage: G.set_texture(color='yellow')
            sage: G
            Graphics3d Object"""
    def stl_binary_repr(self, render_params) -> Any:
        """Graphics3dGroup.stl_binary_repr(self, render_params)

        File: /build/sagemath/src/sage/src/sage/plot/plot3d/base.pyx (starting at line 2469)

        The stl binary representation of a group is simply the
        concatenation of the representation of its objects.

        The STL binary representation is a list of binary strings,
        one for each triangle.

        EXAMPLES::

            sage: G = sphere() + sphere((1,2,3))
            sage: len(G.stl_binary_repr(G.default_render_params()))
            2736"""
    def tachyon_repr(self, render_params) -> Any:
        """Graphics3dGroup.tachyon_repr(self, render_params)

        File: /build/sagemath/src/sage/src/sage/plot/plot3d/base.pyx (starting at line 2371)

        The tachyon representation of a group is simply the concatenation of
        the representations of its objects.

        EXAMPLES::

            sage: G = sphere() + sphere((1,2,3))
            sage: G.tachyon_repr(G.default_render_params())
            [['Sphere center 0.0 0.0 0.0 Rad 1.0 texture...'],
             ['Sphere center 1.0 2.0 3.0 Rad 1.0 texture...']]"""
    @overload
    def texture_set(self) -> Any:
        """Graphics3dGroup.texture_set(self)

        File: /build/sagemath/src/sage/src/sage/plot/plot3d/base.pyx (starting at line 2488)

        The texture set of a group is simply the union of the textures of
        all its objects.

        EXAMPLES::

            sage: G = sphere(color='red') + sphere(color='yellow')
            sage: [t for t in G.texture_set() if t.color == colors.red] # one red texture
            [Texture(texture..., red, ff0000)]
            sage: [t for t in G.texture_set() if t.color == colors.yellow] # one yellow texture
            [Texture(texture..., yellow, ffff00)]

            sage: T = sage.plot.plot3d.texture.Texture('blue'); T
            Texture(texture..., blue, 0000ff)
            sage: G = sphere(texture=T) + sphere((1, 1, 1), texture=T)
            sage: len(G.texture_set())
            1

        TESTS:

        Check that :issue:`23200` is fixed::

            sage: G = sage.plot.plot3d.base.Graphics3dGroup()
            sage: G.texture_set()
            set()"""
    @overload
    def texture_set(self) -> Any:
        """Graphics3dGroup.texture_set(self)

        File: /build/sagemath/src/sage/src/sage/plot/plot3d/base.pyx (starting at line 2488)

        The texture set of a group is simply the union of the textures of
        all its objects.

        EXAMPLES::

            sage: G = sphere(color='red') + sphere(color='yellow')
            sage: [t for t in G.texture_set() if t.color == colors.red] # one red texture
            [Texture(texture..., red, ff0000)]
            sage: [t for t in G.texture_set() if t.color == colors.yellow] # one yellow texture
            [Texture(texture..., yellow, ffff00)]

            sage: T = sage.plot.plot3d.texture.Texture('blue'); T
            Texture(texture..., blue, 0000ff)
            sage: G = sphere(texture=T) + sphere((1, 1, 1), texture=T)
            sage: len(G.texture_set())
            1

        TESTS:

        Check that :issue:`23200` is fixed::

            sage: G = sage.plot.plot3d.base.Graphics3dGroup()
            sage: G.texture_set()
            set()"""
    @overload
    def texture_set(self) -> Any:
        """Graphics3dGroup.texture_set(self)

        File: /build/sagemath/src/sage/src/sage/plot/plot3d/base.pyx (starting at line 2488)

        The texture set of a group is simply the union of the textures of
        all its objects.

        EXAMPLES::

            sage: G = sphere(color='red') + sphere(color='yellow')
            sage: [t for t in G.texture_set() if t.color == colors.red] # one red texture
            [Texture(texture..., red, ff0000)]
            sage: [t for t in G.texture_set() if t.color == colors.yellow] # one yellow texture
            [Texture(texture..., yellow, ffff00)]

            sage: T = sage.plot.plot3d.texture.Texture('blue'); T
            Texture(texture..., blue, 0000ff)
            sage: G = sphere(texture=T) + sphere((1, 1, 1), texture=T)
            sage: len(G.texture_set())
            1

        TESTS:

        Check that :issue:`23200` is fixed::

            sage: G = sage.plot.plot3d.base.Graphics3dGroup()
            sage: G.texture_set()
            set()"""
    @overload
    def texture_set(self) -> Any:
        """Graphics3dGroup.texture_set(self)

        File: /build/sagemath/src/sage/src/sage/plot/plot3d/base.pyx (starting at line 2488)

        The texture set of a group is simply the union of the textures of
        all its objects.

        EXAMPLES::

            sage: G = sphere(color='red') + sphere(color='yellow')
            sage: [t for t in G.texture_set() if t.color == colors.red] # one red texture
            [Texture(texture..., red, ff0000)]
            sage: [t for t in G.texture_set() if t.color == colors.yellow] # one yellow texture
            [Texture(texture..., yellow, ffff00)]

            sage: T = sage.plot.plot3d.texture.Texture('blue'); T
            Texture(texture..., blue, 0000ff)
            sage: G = sphere(texture=T) + sphere((1, 1, 1), texture=T)
            sage: len(G.texture_set())
            1

        TESTS:

        Check that :issue:`23200` is fixed::

            sage: G = sage.plot.plot3d.base.Graphics3dGroup()
            sage: G.texture_set()
            set()"""
    @overload
    def texture_set(self) -> Any:
        """Graphics3dGroup.texture_set(self)

        File: /build/sagemath/src/sage/src/sage/plot/plot3d/base.pyx (starting at line 2488)

        The texture set of a group is simply the union of the textures of
        all its objects.

        EXAMPLES::

            sage: G = sphere(color='red') + sphere(color='yellow')
            sage: [t for t in G.texture_set() if t.color == colors.red] # one red texture
            [Texture(texture..., red, ff0000)]
            sage: [t for t in G.texture_set() if t.color == colors.yellow] # one yellow texture
            [Texture(texture..., yellow, ffff00)]

            sage: T = sage.plot.plot3d.texture.Texture('blue'); T
            Texture(texture..., blue, 0000ff)
            sage: G = sphere(texture=T) + sphere((1, 1, 1), texture=T)
            sage: len(G.texture_set())
            1

        TESTS:

        Check that :issue:`23200` is fixed::

            sage: G = sage.plot.plot3d.base.Graphics3dGroup()
            sage: G.texture_set()
            set()"""
    def threejs_repr(self, render_params) -> Any:
        """Graphics3dGroup.threejs_repr(self, render_params)

        File: /build/sagemath/src/sage/src/sage/plot/plot3d/base.pyx (starting at line 2445)

        The three.js representation of a group is the concatenation of the
        representations of its objects.

        EXAMPLES::

            sage: G = point3d((1,2,3)) + point3d((4,5,6)) + line3d([(1,2,3), (4,5,6)])
            sage: G.threejs_repr(G.default_render_params())
            [('point',
              {'color': '#6666ff', 'opacity': 1.0, 'point': (1.0, 2.0, 3.0), 'size': 5.0}),
             ('point',
              {'color': '#6666ff', 'opacity': 1.0, 'point': (4.0, 5.0, 6.0), 'size': 5.0}),
             ('line',
              {'color': '#6666ff',
               'linewidth': 1.0,
               'opacity': 1.0,
               'points': [(1.0, 2.0, 3.0), (4.0, 5.0, 6.0)]})]"""
    @overload
    def transform(self, **kwds) -> Any:
        """Graphics3dGroup.transform(self, **kwds)

        File: /build/sagemath/src/sage/src/sage/plot/plot3d/base.pyx (starting at line 2325)

        Transforming this entire group simply makes a transform group with
        the same contents.

        EXAMPLES::

            sage: G = dodecahedron(color='red', opacity=.5) + icosahedron(color='blue')
            sage: G
            Graphics3d Object
            sage: G.transform(scale=(2,1/2,1))
            Graphics3d Object
            sage: G.transform(trans=(1,1,3))
            Graphics3d Object"""
    @overload
    def transform(self, scale=...) -> Any:
        """Graphics3dGroup.transform(self, **kwds)

        File: /build/sagemath/src/sage/src/sage/plot/plot3d/base.pyx (starting at line 2325)

        Transforming this entire group simply makes a transform group with
        the same contents.

        EXAMPLES::

            sage: G = dodecahedron(color='red', opacity=.5) + icosahedron(color='blue')
            sage: G
            Graphics3d Object
            sage: G.transform(scale=(2,1/2,1))
            Graphics3d Object
            sage: G.transform(trans=(1,1,3))
            Graphics3d Object"""
    @overload
    def transform(self, trans=...) -> Any:
        """Graphics3dGroup.transform(self, **kwds)

        File: /build/sagemath/src/sage/src/sage/plot/plot3d/base.pyx (starting at line 2325)

        Transforming this entire group simply makes a transform group with
        the same contents.

        EXAMPLES::

            sage: G = dodecahedron(color='red', opacity=.5) + icosahedron(color='blue')
            sage: G
            Graphics3d Object
            sage: G.transform(scale=(2,1/2,1))
            Graphics3d Object
            sage: G.transform(trans=(1,1,3))
            Graphics3d Object"""
    @overload
    def x3d_str(self) -> Any:
        """Graphics3dGroup.x3d_str(self)

        File: /build/sagemath/src/sage/src/sage/plot/plot3d/base.pyx (starting at line 2385)

        The x3d representation of a group is simply the concatenation of
        the representation of its objects.

        EXAMPLES::

            sage: G = sphere() + sphere((1,2,3))
            sage: print(G.x3d_str())
            <Transform translation='0 0 0'>
            <Shape><Sphere radius='1.0'/><Appearance><Material diffuseColor='0.4 0.4 1.0' shininess='1.0' specularColor='0.0 0.0 0.0'/></Appearance></Shape>
            </Transform>
            <Transform translation='1 2 3'>
            <Shape><Sphere radius='1.0'/><Appearance><Material diffuseColor='0.4 0.4 1.0' shininess='1.0' specularColor='0.0 0.0 0.0'/></Appearance></Shape>
            </Transform>"""
    @overload
    def x3d_str(self) -> Any:
        """Graphics3dGroup.x3d_str(self)

        File: /build/sagemath/src/sage/src/sage/plot/plot3d/base.pyx (starting at line 2385)

        The x3d representation of a group is simply the concatenation of
        the representation of its objects.

        EXAMPLES::

            sage: G = sphere() + sphere((1,2,3))
            sage: print(G.x3d_str())
            <Transform translation='0 0 0'>
            <Shape><Sphere radius='1.0'/><Appearance><Material diffuseColor='0.4 0.4 1.0' shininess='1.0' specularColor='0.0 0.0 0.0'/></Appearance></Shape>
            </Transform>
            <Transform translation='1 2 3'>
            <Shape><Sphere radius='1.0'/><Appearance><Material diffuseColor='0.4 0.4 1.0' shininess='1.0' specularColor='0.0 0.0 0.0'/></Appearance></Shape>
            </Transform>"""
    def __add__(self, other) -> Any:
        """Graphics3dGroup.__add__(self, other)

        File: /build/sagemath/src/sage/src/sage/plot/plot3d/base.pyx (starting at line 2270)

        We override this here to make large sums more efficient.

        EXAMPLES::

            sage: G = sum(tetrahedron(opacity=1-t/11).translate(t, 0, 0) for t in range(10))
            sage: G
            Graphics3d Object
            sage: len(G.all)
            10

        We check that :issue:`17258` is solved::

            sage: g = point3d([0,-2,-2]); g += point3d([2,-2,-2])
            sage: len(g.all)
            2
            sage: h = g + arrow([0,-2,-2], [2,-2,-2])
            sage: len(g.all)
            2
            sage: g == h
            False"""

class KeyframeAnimationGroup(Graphics3dGroup):
    """File: /build/sagemath/src/sage/src/sage/plot/plot3d/base.pyx (starting at line 2814)
    A group of objects, each depicting a single frame of animation"""
    def __init__(self, all=..., **kwds) -> Any:
        """KeyframeAnimationGroup.__init__(self, all=(), **kwds)

        File: /build/sagemath/src/sage/src/sage/plot/plot3d/base.pyx (starting at line 2816)

        EXAMPLES::

            sage: frames = [dodecahedron(), icosahedron(), tetrahedron()]
            sage: sage.plot.plot3d.base.KeyframeAnimationGroup(frames)
            Graphics3d Object

        They are usually constructed from an class:`~sage.plot.animate.Animation`::

            sage: type(animate(frames).interactive())
            <class 'sage.plot.plot3d.base.KeyframeAnimationGroup'>"""
    def threejs_repr(self, render_params) -> Any:
        """KeyframeAnimationGroup.threejs_repr(self, render_params)

        File: /build/sagemath/src/sage/src/sage/plot/plot3d/base.pyx (starting at line 2832)

        Add keyframe information to the representations of the group's contents.

        EXAMPLES::

            sage: a = point3d((0, 0, 1))
            sage: b = point3d((0, 1, 0))
            sage: c = point3d((1, 0, 0))
            sage: g = sage.plot.plot3d.base.KeyframeAnimationGroup([a, b, c])
            sage: g.threejs_repr(g.default_render_params())
            [('point', {..., 'keyframe': 0, ..., 'point': (0.0, 0.0, 1.0), ...}),
             ('point', {..., 'keyframe': 1, ..., 'point': (0.0, 1.0, 0.0), ...}),
             ('point', {..., 'keyframe': 2, ..., 'point': (1.0, 0.0, 0.0), ...})]

        Only top-level objects get a unique keyframe. Nested objects share the
        same keyframe::

            sage: g = sage.plot.plot3d.base.KeyframeAnimationGroup([a + b, c])
            sage: g.threejs_repr(g.default_render_params())
            [('point', {..., 'keyframe': 0, ..., 'point': (0.0, 0.0, 1.0), ...}),
             ('point', {..., 'keyframe': 0, ..., 'point': (0.0, 1.0, 0.0), ...}),
             ('point', {..., 'keyframe': 1, ..., 'point': (1.0, 0.0, 0.0), ...})]"""

class PrimitiveObject(Graphics3d):
    """PrimitiveObject(**kwds)

    File: /build/sagemath/src/sage/src/sage/plot/plot3d/base.pyx (starting at line 2892)

    This is the base class for the non-container 3d objects."""
    def __init__(self, **kwds) -> Any:
        """File: /build/sagemath/src/sage/src/sage/plot/plot3d/base.pyx (starting at line 2896)"""
    @overload
    def get_texture(self) -> Any:
        """PrimitiveObject.get_texture(self)

        File: /build/sagemath/src/sage/src/sage/plot/plot3d/base.pyx (starting at line 2917)

        EXAMPLES::

            sage: G = dodecahedron(color='red')
            sage: G.get_texture()
            Texture(texture..., red, ff0000)"""
    @overload
    def get_texture(self) -> Any:
        """PrimitiveObject.get_texture(self)

        File: /build/sagemath/src/sage/src/sage/plot/plot3d/base.pyx (starting at line 2917)

        EXAMPLES::

            sage: G = dodecahedron(color='red')
            sage: G.get_texture()
            Texture(texture..., red, ff0000)"""
    def jmol_repr(self, render_params) -> Any:
        '''PrimitiveObject.jmol_repr(self, render_params)

        File: /build/sagemath/src/sage/src/sage/plot/plot3d/base.pyx (starting at line 2979)

        Default behavior is to render the triangulation. The actual polygon
        data is stored in a separate file.

        EXAMPLES::

            sage: from sage.plot.plot3d.shapes import Torus
            sage: G = Torus(1, .5)
            sage: G.jmol_repr(G.testing_render_params())
            [\'pmesh obj_1 "obj_1.pmesh"\\ncolor pmesh  [102,102,255]\']'''
    def obj_repr(self, render_params) -> Any:
        """PrimitiveObject.obj_repr(self, render_params)

        File: /build/sagemath/src/sage/src/sage/plot/plot3d/base.pyx (starting at line 2961)

        Default behavior is to render the triangulation.

        EXAMPLES::

            sage: from sage.plot.plot3d.shapes import Torus
            sage: G = Torus(1, .5)
            sage: G.obj_repr(G.default_render_params())
            ['g obj_1',
             'usemtl ...',
             ['v 0 1 0.5',
             ...
              'f ...'],
             []]"""
    @overload
    def set_texture(self, texture=..., **kwds) -> Any:
        """PrimitiveObject.set_texture(self, texture=None, **kwds)

        File: /build/sagemath/src/sage/src/sage/plot/plot3d/base.pyx (starting at line 2904)

        EXAMPLES::

            sage: G = dodecahedron(color='red'); G
            Graphics3d Object
            sage: G.set_texture(color='yellow'); G
            Graphics3d Object"""
    @overload
    def set_texture(self, color=...) -> Any:
        """PrimitiveObject.set_texture(self, texture=None, **kwds)

        File: /build/sagemath/src/sage/src/sage/plot/plot3d/base.pyx (starting at line 2904)

        EXAMPLES::

            sage: G = dodecahedron(color='red'); G
            Graphics3d Object
            sage: G.set_texture(color='yellow'); G
            Graphics3d Object"""
    def tachyon_repr(self, render_params) -> Any:
        """PrimitiveObject.tachyon_repr(self, render_params)

        File: /build/sagemath/src/sage/src/sage/plot/plot3d/base.pyx (starting at line 2946)

        Default behavior is to render the triangulation.

        EXAMPLES::

            sage: from sage.plot.plot3d.shapes import Torus
            sage: G = Torus(1, .5)
            sage: G.tachyon_repr(G.default_render_params())
            ['TRI V0 0 1 0.5
            ...
            'texture...']"""
    @overload
    def texture_set(self) -> Any:
        """PrimitiveObject.texture_set(self)

        File: /build/sagemath/src/sage/src/sage/plot/plot3d/base.pyx (starting at line 2927)

        EXAMPLES::

            sage: G = dodecahedron(color='red')
            sage: G.texture_set()
            {Texture(texture..., red, ff0000)}"""
    @overload
    def texture_set(self) -> Any:
        """PrimitiveObject.texture_set(self)

        File: /build/sagemath/src/sage/src/sage/plot/plot3d/base.pyx (starting at line 2927)

        EXAMPLES::

            sage: G = dodecahedron(color='red')
            sage: G.texture_set()
            {Texture(texture..., red, ff0000)}"""
    def threejs_repr(self, render_params) -> Any:
        """PrimitiveObject.threejs_repr(self, render_params)

        File: /build/sagemath/src/sage/src/sage/plot/plot3d/base.pyx (starting at line 2993)

        Default behavior is to render the triangulation.

        EXAMPLES::

            sage: from sage.plot.plot3d.base import PrimitiveObject
            sage: class SimpleTriangle(PrimitiveObject):
            ....:     def triangulation(self):
            ....:         return polygon3d([(0,0,0), (1,0,0), (0,1,0)])
            sage: G = SimpleTriangle()
            sage: G.threejs_repr(G.default_render_params())
            [('surface',
              {'color': '#0000ff',
               'faces': [[0, 1, 2]],
               'opacity': 1.0,
               'vertices': [{'x': 0.0, 'y': 0.0, 'z': 0.0},
                {'x': 1.0, 'y': 0.0, 'z': 0.0},
                {'x': 0.0, 'y': 1.0, 'z': 0.0}]})]"""
    @overload
    def x3d_str(self) -> Any:
        '''PrimitiveObject.x3d_str(self)

        File: /build/sagemath/src/sage/src/sage/plot/plot3d/base.pyx (starting at line 2937)

        EXAMPLES::

            sage: sphere().flatten().x3d_str()
            "<Transform>\\n<Shape><Sphere radius=\'1.0\'/><Appearance><Material diffuseColor=\'0.4 0.4 1.0\' shininess=\'1.0\' specularColor=\'0.0 0.0 0.0\'/></Appearance></Shape>\\n\\n</Transform>"'''
    @overload
    def x3d_str(self) -> Any:
        '''PrimitiveObject.x3d_str(self)

        File: /build/sagemath/src/sage/src/sage/plot/plot3d/base.pyx (starting at line 2937)

        EXAMPLES::

            sage: sphere().flatten().x3d_str()
            "<Transform>\\n<Shape><Sphere radius=\'1.0\'/><Appearance><Material diffuseColor=\'0.4 0.4 1.0\' shininess=\'1.0\' specularColor=\'0.0 0.0 0.0\'/></Appearance></Shape>\\n\\n</Transform>"'''

class RenderParams(sage.structure.sage_object.SageObject):
    """File: /build/sagemath/src/sage/src/sage/plot/plot3d/base.pyx (starting at line 3094)

        This class is a container for all parameters that may be needed to
        render triangulate/render an object to a certain format. It can
        contain both cumulative and global parameters.

        Of particular note is the transformation object, which holds the
        cumulative transformation from the root of the scene graph to this
        node in the tree.
    """
    _uniq_counter: ClassVar[int] = ...
    antialiasing: ClassVar[int] = ...
    dots: ClassVar[bool] = ...
    force_reload: ClassVar[bool] = ...
    mesh: ClassVar[bool] = ...
    randomize_counter: ClassVar[int] = ...
    def __init__(self, **kwds) -> Any:
        """RenderParams.__init__(self, **kwds)

        File: /build/sagemath/src/sage/src/sage/plot/plot3d/base.pyx (starting at line 3112)

        EXAMPLES::

            sage: params = sage.plot.plot3d.base.RenderParams(foo='x')
            sage: params.transform_list
            []
            sage: params.foo
            'x'"""
    @overload
    def pop_transform(self) -> Any:
        """RenderParams.pop_transform(self)

        File: /build/sagemath/src/sage/src/sage/plot/plot3d/base.pyx (starting at line 3162)

        Remove the last transformation off the stack, resetting self.transform
        to the previous value.

        EXAMPLES::

            sage: from sage.plot.plot3d.transform import Transformation
            sage: params = sage.plot.plot3d.base.RenderParams()
            sage: T = Transformation(trans=(100, 500, 0))
            sage: params.push_transform(T)
            sage: params.transform.get_matrix()
            [  1.0   0.0   0.0 100.0]
            [  0.0   1.0   0.0 500.0]
            [  0.0   0.0   1.0   0.0]
            [  0.0   0.0   0.0   1.0]
            sage: params.push_transform(Transformation(trans=(-100, 500, 200)))
            sage: params.transform.get_matrix()
            [   1.0    0.0    0.0    0.0]
            [   0.0    1.0    0.0 1000.0]
            [   0.0    0.0    1.0  200.0]
            [   0.0    0.0    0.0    1.0]
            sage: params.pop_transform()
            sage: params.transform.get_matrix()
            [  1.0   0.0   0.0 100.0]
            [  0.0   1.0   0.0 500.0]
            [  0.0   0.0   1.0   0.0]
            [  0.0   0.0   0.0   1.0]"""
    @overload
    def pop_transform(self) -> Any:
        """RenderParams.pop_transform(self)

        File: /build/sagemath/src/sage/src/sage/plot/plot3d/base.pyx (starting at line 3162)

        Remove the last transformation off the stack, resetting self.transform
        to the previous value.

        EXAMPLES::

            sage: from sage.plot.plot3d.transform import Transformation
            sage: params = sage.plot.plot3d.base.RenderParams()
            sage: T = Transformation(trans=(100, 500, 0))
            sage: params.push_transform(T)
            sage: params.transform.get_matrix()
            [  1.0   0.0   0.0 100.0]
            [  0.0   1.0   0.0 500.0]
            [  0.0   0.0   1.0   0.0]
            [  0.0   0.0   0.0   1.0]
            sage: params.push_transform(Transformation(trans=(-100, 500, 200)))
            sage: params.transform.get_matrix()
            [   1.0    0.0    0.0    0.0]
            [   0.0    1.0    0.0 1000.0]
            [   0.0    0.0    1.0  200.0]
            [   0.0    0.0    0.0    1.0]
            sage: params.pop_transform()
            sage: params.transform.get_matrix()
            [  1.0   0.0   0.0 100.0]
            [  0.0   1.0   0.0 500.0]
            [  0.0   0.0   1.0   0.0]
            [  0.0   0.0   0.0   1.0]"""
    @overload
    def push_transform(self, T) -> Any:
        """RenderParams.push_transform(self, T)

        File: /build/sagemath/src/sage/src/sage/plot/plot3d/base.pyx (starting at line 3132)

        Push a transformation onto the stack, updating self.transform.

        EXAMPLES::

            sage: from sage.plot.plot3d.transform import Transformation
            sage: params = sage.plot.plot3d.base.RenderParams()
            sage: params.transform is None
            True
            sage: T = Transformation(scale=(10,20,30))
            sage: params.push_transform(T)
            sage: params.transform.get_matrix()
            [10.0  0.0  0.0  0.0]
            [ 0.0 20.0  0.0  0.0]
            [ 0.0  0.0 30.0  0.0]
            [ 0.0  0.0  0.0  1.0]
            sage: params.push_transform(T)  # scale again
            sage: params.transform.get_matrix()
            [100.0   0.0   0.0   0.0]
            [  0.0 400.0   0.0   0.0]
            [  0.0   0.0 900.0   0.0]
            [  0.0   0.0   0.0   1.0]"""
    @overload
    def push_transform(self, T) -> Any:
        """RenderParams.push_transform(self, T)

        File: /build/sagemath/src/sage/src/sage/plot/plot3d/base.pyx (starting at line 3132)

        Push a transformation onto the stack, updating self.transform.

        EXAMPLES::

            sage: from sage.plot.plot3d.transform import Transformation
            sage: params = sage.plot.plot3d.base.RenderParams()
            sage: params.transform is None
            True
            sage: T = Transformation(scale=(10,20,30))
            sage: params.push_transform(T)
            sage: params.transform.get_matrix()
            [10.0  0.0  0.0  0.0]
            [ 0.0 20.0  0.0  0.0]
            [ 0.0  0.0 30.0  0.0]
            [ 0.0  0.0  0.0  1.0]
            sage: params.push_transform(T)  # scale again
            sage: params.transform.get_matrix()
            [100.0   0.0   0.0   0.0]
            [  0.0 400.0   0.0   0.0]
            [  0.0   0.0 900.0   0.0]
            [  0.0   0.0   0.0   1.0]"""
    @overload
    def push_transform(self, T) -> Any:
        """RenderParams.push_transform(self, T)

        File: /build/sagemath/src/sage/src/sage/plot/plot3d/base.pyx (starting at line 3132)

        Push a transformation onto the stack, updating self.transform.

        EXAMPLES::

            sage: from sage.plot.plot3d.transform import Transformation
            sage: params = sage.plot.plot3d.base.RenderParams()
            sage: params.transform is None
            True
            sage: T = Transformation(scale=(10,20,30))
            sage: params.push_transform(T)
            sage: params.transform.get_matrix()
            [10.0  0.0  0.0  0.0]
            [ 0.0 20.0  0.0  0.0]
            [ 0.0  0.0 30.0  0.0]
            [ 0.0  0.0  0.0  1.0]
            sage: params.push_transform(T)  # scale again
            sage: params.transform.get_matrix()
            [100.0   0.0   0.0   0.0]
            [  0.0 400.0   0.0   0.0]
            [  0.0   0.0 900.0   0.0]
            [  0.0   0.0   0.0   1.0]"""
    @overload
    def unique_name(self, desc=...) -> Any:
        """RenderParams.unique_name(self, desc='name')

        File: /build/sagemath/src/sage/src/sage/plot/plot3d/base.pyx (starting at line 3193)

        Return a unique identifier starting with ``desc``.

        INPUT:

        - ``desc`` -- string (default: ``'name'``); the prefix of the names

        EXAMPLES::

            sage: params = sage.plot.plot3d.base.RenderParams()
            sage: params.unique_name()
            'name_1'
            sage: params.unique_name()
            'name_2'
            sage: params.unique_name('texture')
            'texture_3'"""
    @overload
    def unique_name(self) -> Any:
        """RenderParams.unique_name(self, desc='name')

        File: /build/sagemath/src/sage/src/sage/plot/plot3d/base.pyx (starting at line 3193)

        Return a unique identifier starting with ``desc``.

        INPUT:

        - ``desc`` -- string (default: ``'name'``); the prefix of the names

        EXAMPLES::

            sage: params = sage.plot.plot3d.base.RenderParams()
            sage: params.unique_name()
            'name_1'
            sage: params.unique_name()
            'name_2'
            sage: params.unique_name('texture')
            'texture_3'"""
    @overload
    def unique_name(self) -> Any:
        """RenderParams.unique_name(self, desc='name')

        File: /build/sagemath/src/sage/src/sage/plot/plot3d/base.pyx (starting at line 3193)

        Return a unique identifier starting with ``desc``.

        INPUT:

        - ``desc`` -- string (default: ``'name'``); the prefix of the names

        EXAMPLES::

            sage: params = sage.plot.plot3d.base.RenderParams()
            sage: params.unique_name()
            'name_1'
            sage: params.unique_name()
            'name_2'
            sage: params.unique_name('texture')
            'texture_3'"""

class TransformGroup(Graphics3dGroup):
    """File: /build/sagemath/src/sage/src/sage/plot/plot3d/base.pyx (starting at line 2550)

        This class is a container for a group of objects with a common
        transformation.
    """
    def __init__(self, all=..., rot=..., trans=..., scale=..., T=...) -> Any:
        """TransformGroup.__init__(self, all=[], rot=None, trans=None, scale=None, T=None)

        File: /build/sagemath/src/sage/src/sage/plot/plot3d/base.pyx (starting at line 2555)

        EXAMPLES::

            sage: sage.plot.plot3d.base.TransformGroup([sphere()], trans=(1,2,3)) + point3d((0,0,0))
            Graphics3d Object

        The are usually constructed implicitly::

            sage: type(sphere((1,2,3)))
            <class 'sage.plot.plot3d.base.TransformGroup'>
            sage: type(dodecahedron().scale(2))
            <class 'sage.plot.plot3d.base.TransformGroup'>"""
    @overload
    def bounding_box(self) -> Any:
        """TransformGroup.bounding_box(self)

        File: /build/sagemath/src/sage/src/sage/plot/plot3d/base.pyx (starting at line 2583)

        Return the bounding box, i.e., the box containing the
        contents of the object after applying the transformation.

        EXAMPLES::

            sage: from math import pi
            sage: G = cube()
            sage: G.bounding_box()
            ((-0.5, -0.5, -0.5), (0.5, 0.5, 0.5))
            sage: G.scale(4).bounding_box()
            ((-2.0, -2.0, -2.0), (2.0, 2.0, 2.0))
            sage: G.rotateZ(pi/4).bounding_box()
            ((-0.7071067811865475, -0.7071067811865475, -0.5),
             (0.7071067811865475, 0.7071067811865475, 0.5))"""
    @overload
    def bounding_box(self) -> Any:
        """TransformGroup.bounding_box(self)

        File: /build/sagemath/src/sage/src/sage/plot/plot3d/base.pyx (starting at line 2583)

        Return the bounding box, i.e., the box containing the
        contents of the object after applying the transformation.

        EXAMPLES::

            sage: from math import pi
            sage: G = cube()
            sage: G.bounding_box()
            ((-0.5, -0.5, -0.5), (0.5, 0.5, 0.5))
            sage: G.scale(4).bounding_box()
            ((-2.0, -2.0, -2.0), (2.0, 2.0, 2.0))
            sage: G.rotateZ(pi/4).bounding_box()
            ((-0.7071067811865475, -0.7071067811865475, -0.5),
             (0.7071067811865475, 0.7071067811865475, 0.5))"""
    @overload
    def bounding_box(self) -> Any:
        """TransformGroup.bounding_box(self)

        File: /build/sagemath/src/sage/src/sage/plot/plot3d/base.pyx (starting at line 2583)

        Return the bounding box, i.e., the box containing the
        contents of the object after applying the transformation.

        EXAMPLES::

            sage: from math import pi
            sage: G = cube()
            sage: G.bounding_box()
            ((-0.5, -0.5, -0.5), (0.5, 0.5, 0.5))
            sage: G.scale(4).bounding_box()
            ((-2.0, -2.0, -2.0), (2.0, 2.0, 2.0))
            sage: G.rotateZ(pi/4).bounding_box()
            ((-0.7071067811865475, -0.7071067811865475, -0.5),
             (0.7071067811865475, 0.7071067811865475, 0.5))"""
    @overload
    def bounding_box(self) -> Any:
        """TransformGroup.bounding_box(self)

        File: /build/sagemath/src/sage/src/sage/plot/plot3d/base.pyx (starting at line 2583)

        Return the bounding box, i.e., the box containing the
        contents of the object after applying the transformation.

        EXAMPLES::

            sage: from math import pi
            sage: G = cube()
            sage: G.bounding_box()
            ((-0.5, -0.5, -0.5), (0.5, 0.5, 0.5))
            sage: G.scale(4).bounding_box()
            ((-2.0, -2.0, -2.0), (2.0, 2.0, 2.0))
            sage: G.rotateZ(pi/4).bounding_box()
            ((-0.7071067811865475, -0.7071067811865475, -0.5),
             (0.7071067811865475, 0.7071067811865475, 0.5))"""
    @overload
    def flatten(self) -> Any:
        """TransformGroup.flatten(self)

        File: /build/sagemath/src/sage/src/sage/plot/plot3d/base.pyx (starting at line 2768)

        Try to reduce the depth of the scene tree by consolidating groups
        and transformations.

        EXAMPLES::

            sage: G = sphere((1,2,3)).scale(100)
            sage: T = G.get_transformation()
            sage: T.get_matrix()
            [100.0   0.0   0.0   0.0]
            [  0.0 100.0   0.0   0.0]
            [  0.0   0.0 100.0   0.0]
            [  0.0   0.0   0.0   1.0]

            sage: G.flatten().get_transformation().get_matrix()
            [100.0   0.0   0.0 100.0]
            [  0.0 100.0   0.0 200.0]
            [  0.0   0.0 100.0 300.0]
            [  0.0   0.0   0.0   1.0]"""
    @overload
    def flatten(self) -> Any:
        """TransformGroup.flatten(self)

        File: /build/sagemath/src/sage/src/sage/plot/plot3d/base.pyx (starting at line 2768)

        Try to reduce the depth of the scene tree by consolidating groups
        and transformations.

        EXAMPLES::

            sage: G = sphere((1,2,3)).scale(100)
            sage: T = G.get_transformation()
            sage: T.get_matrix()
            [100.0   0.0   0.0   0.0]
            [  0.0 100.0   0.0   0.0]
            [  0.0   0.0 100.0   0.0]
            [  0.0   0.0   0.0   1.0]

            sage: G.flatten().get_transformation().get_matrix()
            [100.0   0.0   0.0 100.0]
            [  0.0 100.0   0.0 200.0]
            [  0.0   0.0 100.0 300.0]
            [  0.0   0.0   0.0   1.0]"""
    @overload
    def get_transformation(self) -> Any:
        """TransformGroup.get_transformation(self)

        File: /build/sagemath/src/sage/src/sage/plot/plot3d/base.pyx (starting at line 2748)

        Return the current transformation object.

        EXAMPLES::

            sage: G = sphere().scale(100)
            sage: T = G.get_transformation()
            sage: T.get_matrix()
            [100.0   0.0   0.0   0.0]
            [  0.0 100.0   0.0   0.0]
            [  0.0   0.0 100.0   0.0]
            [  0.0   0.0   0.0   1.0]"""
    @overload
    def get_transformation(self) -> Any:
        """TransformGroup.get_transformation(self)

        File: /build/sagemath/src/sage/src/sage/plot/plot3d/base.pyx (starting at line 2748)

        Return the current transformation object.

        EXAMPLES::

            sage: G = sphere().scale(100)
            sage: T = G.get_transformation()
            sage: T.get_matrix()
            [100.0   0.0   0.0   0.0]
            [  0.0 100.0   0.0   0.0]
            [  0.0   0.0 100.0   0.0]
            [  0.0   0.0   0.0   1.0]"""
    def jmol_repr(self, render_params) -> Any:
        """TransformGroup.jmol_repr(self, render_params)

        File: /build/sagemath/src/sage/src/sage/plot/plot3d/base.pyx (starting at line 2711)

        Transformations for jmol are applied at the leaf nodes.

        EXAMPLES::

            sage: G = sphere((1,2,3)).scale(2)
            sage: G.jmol_repr(G.default_render_params())
            [[['isosurface sphere_1  center {2.0 4.0 6.0} sphere 2.0\\ncolor isosurface  [102,102,255]']]]"""
    def json_repr(self, render_params) -> Any:
        '''TransformGroup.json_repr(self, render_params)

        File: /build/sagemath/src/sage/src/sage/plot/plot3d/base.pyx (starting at line 2632)

        Transformations are applied at the leaf nodes.

        EXAMPLES::

            sage: G = cube().rotateX(0.2)
            sage: G.json_repr(G.default_render_params())
            [[\'{"vertices":[{"x":0.5,"y":0.589368,"z":0.390699},...\']]'''
    def obj_repr(self, render_params) -> Any:
        """TransformGroup.obj_repr(self, render_params)

        File: /build/sagemath/src/sage/src/sage/plot/plot3d/base.pyx (starting at line 2680)

        Transformations for .obj files are applied at the leaf nodes.

        EXAMPLES::

            sage: G = cube().scale(4).translate(1, 2, 3)
            sage: G.obj_repr(G.default_render_params())
            [[['g obj_1',
               'usemtl ...',
               ['v 3 4 5',
                'v -1 4 5',
                'v -1 0 5',
                'v 3 0 5',
                'v 3 4 1',
                'v -1 4 1',
                'v 3 0 1',
                'v -1 0 1'],
               ['f 1 2 3 4',
                'f 1 5 6 2',
                'f 1 4 7 5',
                'f 6 5 7 8',
                'f 7 4 3 8',
                'f 3 2 6 8'],
               []]]]"""
    def stl_binary_repr(self, render_params) -> Any:
        """TransformGroup.stl_binary_repr(self, render_params)

        File: /build/sagemath/src/sage/src/sage/plot/plot3d/base.pyx (starting at line 2647)

        Transformations are applied at the leaf nodes.

        The STL binary representation is a list of binary strings,
        one for each triangle.

        EXAMPLES::

            sage: G = sphere().translate((1,2,0))
            sage: len(G.stl_binary_repr(G.default_render_params()))
            1368"""
    def tachyon_repr(self, render_params) -> Any:
        """TransformGroup.tachyon_repr(self, render_params)

        File: /build/sagemath/src/sage/src/sage/plot/plot3d/base.pyx (starting at line 2665)

        Transformations for Tachyon are applied at the leaf nodes.

        EXAMPLES::

            sage: G = sphere((1,2,3)).scale(2)
            sage: G.tachyon_repr(G.default_render_params())
            [['Sphere center 2.0 4.0 6.0 Rad 2.0 texture...']]"""
    def threejs_repr(self, render_params) -> Any:
        """TransformGroup.threejs_repr(self, render_params)

        File: /build/sagemath/src/sage/src/sage/plot/plot3d/base.pyx (starting at line 2726)

        Transformations for three.js are applied at the leaf nodes.

        EXAMPLES::

            sage: G = point3d((1,2,3)) + point3d((4,5,6))
            sage: G = G.translate(-1, -2, -3).scale(10)
            sage: G.threejs_repr(G.default_render_params())
            [('point',
              {'color': '#6666ff', 'opacity': 1.0, 'point': (0.0, 0.0, 0.0), 'size': 5.0}),
             ('point',
              {'color': '#6666ff',
               'opacity': 1.0,
               'point': (30.0, 30.0, 30.0),
               'size': 5.0})]"""
    @overload
    def transform(self, **kwds) -> Any:
        """TransformGroup.transform(self, **kwds)

        File: /build/sagemath/src/sage/src/sage/plot/plot3d/base.pyx (starting at line 2797)

        Transforming this entire group can be done by composing transformations.

        EXAMPLES::

            sage: G = dodecahedron(color='red', opacity=.5) + icosahedron(color='blue')
            sage: G
            Graphics3d Object
            sage: G.transform(scale=(2,1/2,1))
            Graphics3d Object
            sage: G.transform(trans=(1,1,3))
            Graphics3d Object"""
    @overload
    def transform(self, scale=...) -> Any:
        """TransformGroup.transform(self, **kwds)

        File: /build/sagemath/src/sage/src/sage/plot/plot3d/base.pyx (starting at line 2797)

        Transforming this entire group can be done by composing transformations.

        EXAMPLES::

            sage: G = dodecahedron(color='red', opacity=.5) + icosahedron(color='blue')
            sage: G
            Graphics3d Object
            sage: G.transform(scale=(2,1/2,1))
            Graphics3d Object
            sage: G.transform(trans=(1,1,3))
            Graphics3d Object"""
    @overload
    def transform(self, trans=...) -> Any:
        """TransformGroup.transform(self, **kwds)

        File: /build/sagemath/src/sage/src/sage/plot/plot3d/base.pyx (starting at line 2797)

        Transforming this entire group can be done by composing transformations.

        EXAMPLES::

            sage: G = dodecahedron(color='red', opacity=.5) + icosahedron(color='blue')
            sage: G
            Graphics3d Object
            sage: G.transform(scale=(2,1/2,1))
            Graphics3d Object
            sage: G.transform(trans=(1,1,3))
            Graphics3d Object"""
    @overload
    def x3d_str(self) -> Any:
        '''TransformGroup.x3d_str(self)

        File: /build/sagemath/src/sage/src/sage/plot/plot3d/base.pyx (starting at line 2610)

        To apply a transformation to a set of objects in x3d, simply make them
        all children of an x3d Transform node.

        EXAMPLES::

            sage: sphere((1,2,3)).x3d_str()
            "<Transform translation=\'1 2 3\'>\\n<Shape><Sphere radius=\'1.0\'/><Appearance><Material diffuseColor=\'0.4 0.4 1.0\' shininess=\'1.0\' specularColor=\'0.0 0.0 0.0\'/></Appearance></Shape>\\n\\n</Transform>"'''
    @overload
    def x3d_str(self) -> Any:
        '''TransformGroup.x3d_str(self)

        File: /build/sagemath/src/sage/src/sage/plot/plot3d/base.pyx (starting at line 2610)

        To apply a transformation to a set of objects in x3d, simply make them
        all children of an x3d Transform node.

        EXAMPLES::

            sage: sphere((1,2,3)).x3d_str()
            "<Transform translation=\'1 2 3\'>\\n<Shape><Sphere radius=\'1.0\'/><Appearance><Material diffuseColor=\'0.4 0.4 1.0\' shininess=\'1.0\' specularColor=\'0.0 0.0 0.0\'/></Appearance></Shape>\\n\\n</Transform>"'''

class Viewpoint(Graphics3d):
    """File: /build/sagemath/src/sage/src/sage/plot/plot3d/base.pyx (starting at line 2864)

        This class represents a viewpoint, necessary for x3d.

        In the future, there could be multiple viewpoints, and they could have
        more properties. (Currently they only hold a position).
    """
    def __init__(self, *x) -> Any:
        '''Viewpoint.__init__(self, *x)

        File: /build/sagemath/src/sage/src/sage/plot/plot3d/base.pyx (starting at line 2871)

        EXAMPLES::

            sage: sage.plot.plot3d.base.Viewpoint(1, 2, 4).x3d_str()
            "<Viewpoint position=\'1 2 4\'/>"'''
    @overload
    def x3d_str(self) -> Any:
        '''Viewpoint.x3d_str(self)

        File: /build/sagemath/src/sage/src/sage/plot/plot3d/base.pyx (starting at line 2882)

        EXAMPLES::

            sage: sphere((0,0,0), 100).viewpoint().x3d_str()
            "<Viewpoint position=\'0 0 6\'/>"'''
    @overload
    def x3d_str(self) -> Any:
        '''Viewpoint.x3d_str(self)

        File: /build/sagemath/src/sage/src/sage/plot/plot3d/base.pyx (starting at line 2882)

        EXAMPLES::

            sage: sphere((0,0,0), 100).viewpoint().x3d_str()
            "<Viewpoint position=\'0 0 6\'/>"'''
