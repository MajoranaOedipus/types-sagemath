from _typeshed import Incomplete
from sage.matrix.constructor import matrix as matrix
from sage.misc.decorators import options as options, rename_keyword as rename_keyword
from sage.misc.functional import is_odd as is_odd
from sage.misc.lazy_import import lazy_import as lazy_import
from sage.plot.hyperbolic_polygon import HyperbolicPolygon as HyperbolicPolygon
from sage.plot.plot import Graphics as Graphics
from sage.rings.cc import CC as CC
from sage.rings.integer import Integer as Integer

class HyperbolicRegularPolygon(HyperbolicPolygon):
    """
    Primitive class for regular hyperbolic polygon type.

    See ``hyperbolic_regular_polygon?`` for information about plotting
    a hyperbolic regular polygon in the upper complex halfplane.

    INPUT:

    - ``sides`` -- number of sides of the polygon

    - ``i_angle`` -- interior angle of the polygon

    - ``center`` -- center point as a complex number of the polygon

    EXAMPLES:

    Note that constructions should use :func:`hyperbolic_regular_polygon`::

         sage: from sage.plot.hyperbolic_regular_polygon import HyperbolicRegularPolygon
         sage: print(HyperbolicRegularPolygon(5,pi/2,I, {}))
         Hyperbolic regular polygon (sides=5, i_angle=1/2*pi, center=1.00000000000000*I)

    The code verifies is there exists a compact hyperbolic regular polygon
    with the given data, checking

    .. MATH::

        A(\\mathcal{P}) = \\pi(s-2) - s \\cdot \\alpha > 0,

    where `s` is ``sides`` and `\\alpha` is ``i_angle``. This raises an error if
    the ``i_angle`` is less than the minimum to generate a compact polygon::

        sage: from sage.plot.hyperbolic_regular_polygon import HyperbolicRegularPolygon
        sage: P = HyperbolicRegularPolygon(4, pi/2, I, {})
        Traceback (most recent call last):
        ...
        ValueError: there exists no hyperbolic regular compact polygon,
         for sides=4 the interior angle must be less than 1/2*pi

    It is an error to give a center outside the upper half plane in this model ::

         sage: from sage.plot.hyperbolic_regular_polygon import HyperbolicRegularPolygon
         sage: P = HyperbolicRegularPolygon(4, pi/4, 1-I, {})
         Traceback (most recent call last):
         ...
         ValueError: center: 1.00000000000000 - 1.00000000000000*I is not
          a valid point in the upper half plane model of the hyperbolic plane

    TESTS::

         sage: from sage.plot.hyperbolic_regular_polygon import HyperbolicRegularPolygon
         sage: P = HyperbolicRegularPolygon(4, -pi/4, I, {})
         Traceback (most recent call last):
         ...
         ValueError: interior angle -1/4*pi must be in (0, pi) interval

         sage: from sage.plot.hyperbolic_regular_polygon import HyperbolicRegularPolygon
         sage: P=HyperbolicRegularPolygon(16, 3*pi/2, I, {})
         Traceback (most recent call last):
         ...
         ValueError: interior angle 3/2*pi must be in (0, pi) interval

         sage: from sage.plot.hyperbolic_regular_polygon import HyperbolicRegularPolygon
         sage: P = HyperbolicRegularPolygon(2, pi/10, I, {})
         Traceback (most recent call last):
         ...
         ValueError: degenerated polygons (sides<=2) are not supported
    """
    center: Incomplete
    sides: Incomplete
    i_angle: Incomplete
    def __init__(self, sides, i_angle, center, options) -> None:
        """
        Initialize HyperbolicRegularPolygon.

        EXAMPLES::

            sage: from sage.plot.hyperbolic_regular_polygon import HyperbolicRegularPolygon
            sage: print(HyperbolicRegularPolygon(5,pi/2,I, {}))
            Hyperbolic regular polygon (sides=5, i_angle=1/2*pi, center=1.00000000000000*I)
        """

def hyperbolic_regular_polygon(sides, i_angle, center=..., **options):
    """
    Return a hyperbolic regular polygon in the upper half model of
    Hyperbolic plane given the number of sides, interior angle and
    possibly a center.

    Type ``?hyperbolic_regular_polygon`` to see all options.

    INPUT:

    - ``sides`` -- number of sides of the polygon

    - ``i_angle`` -- interior angle of the polygon

    - ``center`` -- (default: `i`) hyperbolic center point
      (complex number) of the polygon

    OPTIONS:

    - ``alpha`` -- (default: 1)

    - ``fill`` -- (default: ``False``)

    - ``thickness`` -- (default: 1)

    - ``rgbcolor`` -- (default: ``'blue'``)

    - ``linestyle`` -- (default: ``'solid'``) the style of the line,
      which can be one of the following:

      * ``'dashed'`` or ``'--'``
      * ``'dotted'`` or ``':'``
      * ``'solid'`` or ``'-'``
      * ``'dashdot'`` or ``'-.'``

    EXAMPLES:

    Show a hyperbolic regular polygon with 6 sides and square angles::

        sage: g = hyperbolic_regular_polygon(6, pi/2)
        sage: g.plot()
        Graphics object consisting of 1 graphics primitive

    .. PLOT::

         g = hyperbolic_regular_polygon(6, pi/2)
         sphinx_plot(g.plot())

    With more options::

        sage: g = hyperbolic_regular_polygon(6, pi/2, center=3+2*I, fill=True, color='red')
        sage: g.plot()
        Graphics object consisting of 1 graphics primitive

    .. PLOT::

         g = hyperbolic_regular_polygon(6, pi/2, center=3+2*I, fill=True, color='red')
         sphinx_plot(g.plot())

    The code verifies is there exists a hyperbolic regular polygon
    with the given data, checking

    .. MATH::

        A(\\mathcal{P}) = \\pi(s-2) - s \\cdot \\alpha > 0,

    where `s` is ``sides`` and `\\alpha` is ``i_angle``. This raises an error if
    the ``i_angle`` is less than the minimum to generate a compact polygon::

        sage: hyperbolic_regular_polygon(4, pi/2)
        Traceback (most recent call last):
        ...
        ValueError: there exists no hyperbolic regular compact polygon,
         for sides=4 the interior angle must be less than 1/2*pi

    It is an error to give a center outside the upper half plane in
    this model::

        sage: from sage.plot.hyperbolic_regular_polygon import hyperbolic_regular_polygon
        sage: hyperbolic_regular_polygon(4, pi/4, 1-I)
        Traceback (most recent call last):
        ...
        ValueError: center: 1.00000000000000 - 1.00000000000000*I is not
         a valid point in the upper half plane model of the hyperbolic plane
    """
