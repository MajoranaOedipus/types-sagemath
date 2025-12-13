from sage.misc.fast_methods import WithEqualityById as WithEqualityById
from sage.misc.verbose import verbose as verbose
from sage.structure.sage_object import SageObject as SageObject

class GraphicPrimitive(WithEqualityById, SageObject):
    """
    Base class for graphics primitives, e.g., things that knows how to draw
    themselves in 2D.

    EXAMPLES:

    We create an object that derives from GraphicPrimitive::

        sage: P = line([(-1,-2), (3,5)])
        sage: P[0]
        Line defined by 2 points
        sage: type(P[0])
        <class 'sage.plot.line.Line'>

    TESTS::

        sage: hash(circle((0,0),1))  # random
        42
    """
    def __init__(self, options) -> None:
        """
        Create a base class GraphicsPrimitive.  All this does is
        set the options.

        EXAMPLES:

        We indirectly test this function::

            sage: from sage.plot.primitive import GraphicPrimitive
            sage: GraphicPrimitive({})
            Graphics primitive
        """
    def plot3d(self, **kwds) -> None:
        """
        Plots 3D version of 2D graphics object.  Not implemented
        for base class.

        EXAMPLES::

            sage: from sage.plot.primitive import GraphicPrimitive
            sage: G=GraphicPrimitive({})
            sage: G.plot3d()
            Traceback (most recent call last):
            ...
            NotImplementedError: 3D plotting not implemented for Graphics primitive
        """
    def set_zorder(self, zorder) -> None:
        """
        Set the layer in which to draw the object.

        EXAMPLES::

            sage: P = line([(-2,-3), (3,4)], thickness=4)
            sage: p=P[0]
            sage: p.set_zorder(2)
            sage: p.options()['zorder']
            2
            sage: Q = line([(-2,-4), (3,5)], thickness=4,zorder=1,hue=.5)
            sage: P+Q # blue line on top
            Graphics object consisting of 2 graphics primitives
            sage: q=Q[0]
            sage: q.set_zorder(3)
            sage: P+Q # teal line on top
            Graphics object consisting of 2 graphics primitives
            sage: q.options()['zorder']
            3
        """
    def set_options(self, new_options) -> None:
        """
        Change the options to ``new_options``.

        EXAMPLES::

            sage: from sage.plot.circle import Circle
            sage: c = Circle(0,0,1,{})
            sage: c.set_options({'thickness': 0.6})
            sage: c.options()
            {'thickness': 0.6...}
        """
    def options(self):
        """
        Return the dictionary of options for this graphics primitive.

        By default this function verifies that the options are all
        valid; if any aren't, then a verbose message is printed with level 0.

        EXAMPLES::

            sage: from sage.plot.primitive import GraphicPrimitive
            sage: GraphicPrimitive({}).options()
            {}
        """

class GraphicPrimitive_xydata(GraphicPrimitive):
    def get_minmax_data(self):
        """
        Return a dictionary with the bounding box data.

        EXAMPLES::

            sage: d = polygon([[1,2], [5,6], [5,0]], rgbcolor=(1,0,1))[0].get_minmax_data()
            sage: d['ymin']
            0.0
            sage: d['xmin']
            1.0

        ::

            sage: d = point((3, 3), rgbcolor=hue(0.75))[0].get_minmax_data()
            sage: d['xmin']
            3.0
            sage: d['ymin']
            3.0

        ::

            sage: l = line([(100, 100), (120, 120)])[0]
            sage: d = l.get_minmax_data()
            sage: d['xmin']
            100.0
            sage: d['xmax']
            120.0
        """
