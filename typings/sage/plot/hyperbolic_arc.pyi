from _typeshed import Incomplete
from sage.geometry.hyperbolic_space.hyperbolic_constants import EPSILON as EPSILON
from sage.misc.decorators import options as options, rename_keyword as rename_keyword
from sage.plot.bezier_path import BezierPath as BezierPath
from sage.plot.circle import circle as circle
from sage.rings.cc import CC as CC

class HyperbolicArcCore(BezierPath):
    """
    Base class for Hyperbolic arcs and hyperbolic polygons in the
    hyperbolic plane.

    The Upper Half Model, Poincaré Disk Model, and Klein Disk model
    are supported.
    """

class HyperbolicArc(HyperbolicArcCore):
    '''
    Primitive class for hyberbolic arc type.

    See ``hyperbolic_arc?`` for information about plotting a hyperbolic
    arc in the complex plane.

    INPUT:

    - ``A``, ``B`` -- end points of the hyperbolic arc
    - ``model`` -- the hyperbolic model used, which is one of the following:

      * ``\'UHP\'`` -- upper half plane
      * ``\'PD\'`` -- Poincaré disk
      * ``\'KM\'`` -- Klein disk

    TESTS::

         sage: from sage.plot.hyperbolic_arc import HyperbolicArc
         sage: HyperbolicArc(0, 1/2+I*sqrt(3)/2, "UHP", {})
         Hyperbolic arc (0.000000000000000, 0.500000000000000 + 0.866025403784439*I)
    '''
    A: Incomplete
    B: Incomplete
    model: Incomplete
    path: Incomplete
    def __init__(self, A, B, model, options) -> None:
        '''
        Initialize ``self``.

        EXAMPLES::

            sage: from sage.plot.hyperbolic_arc import HyperbolicArc
            sage: arc = HyperbolicArc(0, 1/2+I*sqrt(3)/2, "UHP", {})
            sage: TestSuite(arc).run(skip=\'_test_pickling\')  # no equality implemented
        '''

def hyperbolic_arc(a, b, model: str = 'UHP', **options):
    """
    Plot an arc from ``a`` to ``b`` in hyperbolic plane.

    INPUT:

    - ``a``, ``b`` -- complex numbers connected by a hyperbolic arc

    - ``model`` -- (default: ``'UHP'``) hyperbolic model used,
      which is one of the following:

      * ``'UHP'`` -- upper half plane
      * ``'PD'`` -- Poincaré disk
      * ``'KM'`` -- Klein disk
      * ``'HM'`` -- hyperboloid model

    OPTIONS:

    - ``alpha`` -- (default: 1)

    - ``thickness`` -- (default: 1)

    - ``rgbcolor`` -- (default: ``'blue'``)

    - ``linestyle`` -- (default: ``'solid'``) the style of the line, which
      is one of ``'dashed'``, ``'dotted'``, ``'solid'``, ``'dashdot'``,
      or ``'--'``, ``':'``, ``'-'``, ``'-.'``, respectively

    EXAMPLES:

    Show a hyperbolic arc from `0` to `1`::

        sage: hyperbolic_arc(0, 1)
        Graphics object consisting of 1 graphics primitive

    .. PLOT::

        sphinx_plot(hyperbolic_arc(0,1))

    Show a hyperbolic arc from `1/2` to `i` with a red thick line::

        sage: hyperbolic_arc(0.5, I,color='red', thickness=2)
        Graphics object consisting of 1 graphics primitive

    .. PLOT::

        sphinx_plot(hyperbolic_arc(0.5, I, color='red', thickness=2))

    Show a hyperbolic arc from `1+i` to `1+2i` with dashed line::

        sage: hyperbolic_arc(1+I, 1+2*I, linestyle='dashed', color='green')
        Graphics object consisting of 1 graphics primitive

    .. PLOT::

        sphinx_plot(hyperbolic_arc(CC(1,1), CC(1,2), linestyle='dashed', color='green'))

    ::

         sage: hyperbolic_arc(-1+I, 1+2*I, linestyle='--', color='orange')
         Graphics object consisting of 1 graphics primitive

    .. PLOT::

        sphinx_plot(hyperbolic_arc(CC(-1,1), CC(1,2), linestyle='dashed'))

    Show a hyperbolic arc from a `1+i` to infinity::

        sage: hyperbolic_arc(1 + I, infinity, color='brown')
        Graphics object consisting of 1 graphics primitive

    .. PLOT::

        from sage.rings.infinity import infinity
        sphinx_plot(hyperbolic_arc(CC(1,1), infinity, color='brown'))

    We can also plot hyperbolic arcs in other models.

    We show a hyperbolic arc from `i` to `-1` in red, another hyperbolic arc
    from `e^{i\\pi/3}` to `0.6 \\cdot e^{i 3\\pi/4}` with dashed style in green,
    and finally a hyperbolic arc from `-0.5+0.5i` to `0.5-0.5i` together
    with the disk frontier in the Poincaré disk model::

        sage: z1 = CC(0,1)
        sage: z2 = CC(-1,0)
        sage: z3 = CC((cos(pi/3),sin(pi/3)))
        sage: z4 = CC((0.6*cos(3*pi/4),0.6*sin(3*pi/4)))
        sage: z5 = CC(-0.5,0.5)
        sage: z6 = CC(0.5,-0.5)
        sage: a1 = hyperbolic_arc(z1, z2, model='PD', color='red')
        sage: a2 = hyperbolic_arc(z3, z4, model='PD', color='green')
        sage: a3 = hyperbolic_arc(z5, z6, model='PD', linestyle='--')
        sage: a1 + a2 + a3
        Graphics object consisting of 6 graphics primitives

    .. PLOT::

        z1 = CC(0,1)
        z2 = CC(-1,0)
        z3 = CC((cos(pi/3),sin(pi/3)))
        z4 = CC((0.6*cos(3*pi/4),0.6*sin(3*pi/4)))
        z5 = CC(-0.5,0.5)
        z6 = CC(0.5,-0.5)
        a1 = hyperbolic_arc(z1, z2, model='PD', color='red')
        a2 = hyperbolic_arc(z3, z4, model='PD', color='green')
        a3 = hyperbolic_arc(z5, z6, model='PD', linestyle='--')
        P = a1 + a2 + a3
        sphinx_plot(P)

    We show the arcs defined by the same endpoints in the Klein disk
    model (note that these are *not* the image of those arcs when
    changing between the models)::

        sage: a1 = hyperbolic_arc(z1, z2, model='KM', color='red')
        sage: a2 = hyperbolic_arc(z3, z4, model='KM', color='green')
        sage: a3 = hyperbolic_arc(z5, z6, model='KM', linestyle='--')
        sage: a1 + a2 + a3
        Graphics object consisting of 6 graphics primitives

    .. PLOT::

        z1 = CC(0,1)
        z2 = CC(-1,0)
        z3 = CC((cos(pi/3),sin(pi/3)))
        z4 = CC((0.6*cos(3*pi/4),0.6*sin(3*pi/4)))
        z5 = CC(-0.5,0.5)
        z6 = CC(0.5,-0.5)
        a1 = hyperbolic_arc(z1, z2, model='KM', color='red')
        a2 = hyperbolic_arc(z3, z4, model='KM', color='green')
        a3 = hyperbolic_arc(z5, z6, model='KM', linestyle='--')
        P = a1 + a2 + a3
        sphinx_plot(P)

    Show a hyperbolic arc from `(1,2,\\sqrt(6))` to `(-2,-3,\\sqrt(14))`
    in the hyperboloid model::

        sage: a = (1,2,sqrt(6))
        sage: b = (-2,-3,sqrt(14))
        sage: hyperbolic_arc(a, b, model='HM')
        Graphics3d Object

    .. PLOT::

       a = (1,2,sqrt(6))
       b = (-2,-3,sqrt(14))
       sphinx_plot(hyperbolic_arc(a, b, model='HM'))
    """
