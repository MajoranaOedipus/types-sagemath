from _typeshed import Incomplete
from sage.misc.classcall_metaclass import ClasscallMetaclass as ClasscallMetaclass, typecall as typecall
from sage.misc.fast_methods import WithEqualityById as WithEqualityById
from sage.plot.colors import Color as Color, colors as colors
from sage.structure.sage_object import SageObject as SageObject

uniq_c: int

def is_Texture(x):
    """
    Deprecated. Use ``isinstance(x, Texture)`` instead.

    EXAMPLES::

        sage: from sage.plot.plot3d.texture import is_Texture, Texture
        sage: t = Texture(0.5)
        sage: is_Texture(t)
        doctest:...: DeprecationWarning: Please use isinstance(x, Texture)
        See https://github.com/sagemath/sage/issues/27593 for details.
        True
    """
def parse_color(info, base=None):
    """
    Parse the color.

    It transforms a valid color string into a color object and
    a color object into an RBG tuple of length 3. Otherwise,
    it multiplies the info by the base color.

    INPUT:

    - ``info`` -- color, valid color str or number
    - ``base`` -- tuple of length 3 (default: ``None``)

    OUTPUT: a tuple or color

    EXAMPLES:

    From a color::

        sage: from sage.plot.plot3d.texture import parse_color
        sage: c = Color('red')
        sage: parse_color(c)
        (1.0, 0.0, 0.0)

    From a valid color str::

        sage: parse_color('red')
        RGB color (1.0, 0.0, 0.0)
        sage: parse_color('#ff0000')
        RGB color (1.0, 0.0, 0.0)

    From a non valid color str::

        sage: parse_color('redd')
        Traceback (most recent call last):
        ...
        ValueError: unknown color 'redd'

    From an info and a base::

        sage: opacity = 10
        sage: parse_color(opacity, base=(.2,.3,.4))
        (2.0, 3.0, 4.0)
    """

class Texture(WithEqualityById, SageObject, metaclass=ClasscallMetaclass):
    '''
    Class representing a texture.

    See documentation of :meth:`Texture.__classcall__
    <sage.plot.plot3d.texture.Texture.__classcall__>` for more details and
    examples.

    EXAMPLES:

    We create a translucent texture::

        sage: from sage.plot.plot3d.texture import Texture
        sage: t = Texture(opacity=0.6)
        sage: t
        Texture(texture..., 6666ff)
        sage: t.opacity
        0.6
        sage: t.jmol_str(\'obj\')
        \'color obj translucent 0.4 [102,102,255]\'
        sage: t.mtl_str()
        \'newmtl texture...\\nKa 0.2 0.2 0.5\\nKd 0.4 0.4 1.0\\nKs 0.0 0.0 0.0\\nillum 1\\nNs 1.0\\nd 0.6\'
        sage: t.x3d_str()
        "<Appearance><Material diffuseColor=\'0.4 0.4 1.0\' shininess=\'1.0\' specularColor=\'0.0 0.0 0.0\'/></Appearance>"

    TESTS::

        sage: Texture(opacity=1/3).opacity
        0.3333333333333333

        sage: hash(Texture()) # random
        42
    '''
    @staticmethod
    def __classcall__(cls, id=None, **kwds):
        """
        Construct a new texture by id.

        INPUT:

        - ``id`` -- a texture (default: ``None``), a dictionary, a color, a
          string, a tuple, ``None`` or any other type acting as an ID. If ``id`` is
          ``None`` and keyword ``texture`` is empty, then it returns a unique texture object.
        - ``texture`` -- a texture
        - ``color`` -- tuple or string (default: (.4, .4, 1))
        - ``opacity`` -- number between 0 and 1 (default: 1)
        - ``ambient`` -- number (default: 0.5)
        - ``diffuse`` -- number (default: 1)
        - ``specular`` -- number (default: 0)
        - ``shininess`` -- number (default: 1)
        - ``name`` -- string (default: ``None``)
        - ``**kwds`` -- other valid keywords

        OUTPUT: a texture object

        EXAMPLES:

        Texture from integer ``id``::

            sage: from sage.plot.plot3d.texture import Texture
            sage: Texture(17)
            Texture(17, 6666ff)

        Texture from rational ``id``::

            sage: Texture(3/4)
            Texture(3/4, 6666ff)

        Texture from a dict::

            sage: Texture({'color':'orange','opacity':0.5})
            Texture(texture..., orange, ffa500)

        Texture from a color::

            sage: c = Color('red')
            sage: Texture(c)
            Texture(texture..., ff0000)

        Texture from a valid string color::

            sage: Texture('red')
            Texture(texture..., red, ff0000)

        Texture from a non valid string color::

            sage: Texture('redd')
            Texture(redd, 6666ff)

        Texture from a tuple::

            sage: Texture((.2,.3,.4))
            Texture(texture..., 334c66)

        Now accepting negative arguments, reduced modulo 1::

            sage: Texture((-3/8, 1/2, 3/8))
            Texture(texture..., 9f7f5f)

        Textures using other keywords::

            sage: Texture(specular=0.4)
            Texture(texture..., 6666ff)
            sage: Texture(diffuse=0.4)
            Texture(texture..., 6666ff)
            sage: Texture(shininess=0.3)
            Texture(texture..., 6666ff)
            sage: Texture(ambient=0.7)
            Texture(texture..., 6666ff)
        """
    id: Incomplete
    name: Incomplete
    color: Incomplete
    opacity: Incomplete
    shininess: Incomplete
    ambient: Incomplete
    diffuse: Incomplete
    specular: Incomplete
    def __init__(self, id, color=(0.4, 0.4, 1), opacity: int = 1, ambient: float = 0.5, diffuse: int = 1, specular: int = 0, shininess: int = 1, name=None, **kwds) -> None:
        """
        Construction of a texture.

        See documentation of :meth:`Texture.__classcall__
        <sage.plot.plot3d.texture.Texture.__classcall__>` for more details and
        examples.

        EXAMPLES::

            sage: from sage.plot.plot3d.texture import Texture
            sage: Texture(3, opacity=0.6)
            Texture(3, 6666ff)
        """
    def hex_rgb(self):
        """
        EXAMPLES::

            sage: from sage.plot.plot3d.texture import Texture
            sage: Texture('red').hex_rgb()
            'ff0000'
            sage: Texture((1, .5, 0)).hex_rgb()
            'ff7f00'
        """
    def tachyon_str(self):
        """
        Convert Texture object to string suitable for Tachyon ray tracer.

        EXAMPLES::

            sage: from sage.plot.plot3d.texture import Texture
            sage: t = Texture(opacity=0.6)
            sage: t.tachyon_str()
            'Texdef texture...\\n  Ambient 0.3333333333333333 Diffuse 0.6666666666666666 Specular 0.0 Opacity 0.6\\n   Color 0.4 0.4 1.0\\n   TexFunc 0'
        """
    def x3d_str(self):
        '''
        Convert Texture object to string suitable for x3d.

        EXAMPLES::

            sage: from sage.plot.plot3d.texture import Texture
            sage: t = Texture(opacity=0.6)
            sage: t.x3d_str()
            "<Appearance><Material diffuseColor=\'0.4 0.4 1.0\' shininess=\'1.0\' specularColor=\'0.0 0.0 0.0\'/></Appearance>"
        '''
    def mtl_str(self):
        """
        Convert Texture object to string suitable for mtl output.

        EXAMPLES::

            sage: from sage.plot.plot3d.texture import Texture
            sage: t = Texture(opacity=0.6)
            sage: t.mtl_str()
            'newmtl texture...\\nKa 0.2 0.2 0.5\\nKd 0.4 0.4 1.0\\nKs 0.0 0.0 0.0\\nillum 1\\nNs 1.0\\nd 0.6'
        """
    def jmol_str(self, obj):
        """
        Convert Texture object to string suitable for Jmol applet.

        INPUT:

        - ``obj`` -- str

        EXAMPLES::

            sage: from sage.plot.plot3d.texture import Texture
            sage: t = Texture(opacity=0.6)
            sage: t.jmol_str('obj')
            'color obj translucent 0.4 [102,102,255]'

        ::

            sage: sum([dodecahedron(center=[2.5*x, 0, 0], color=(1, 0, 0, x/10)) for x in range(11)]).show(aspect_ratio=[1,1,1], frame=False, zoom=2)
        """
