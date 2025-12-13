from sage.functions.hyperbolic import arcsinh as arcsinh, cosh as cosh, sinh as sinh
from sage.functions.log import exp as exp
from sage.functions.other import imag as imag, real as real
from sage.functions.trig import arccos as arccos
from sage.geometry.hyperbolic_space.hyperbolic_constants import EPSILON as EPSILON
from sage.matrix.constructor import matrix as matrix
from sage.misc.functional import sqrt as sqrt
from sage.misc.lazy_attribute import lazy_attribute as lazy_attribute
from sage.misc.lazy_import import lazy_import as lazy_import
from sage.modules.free_module_element import vector as vector
from sage.rings.cc import CC as CC
from sage.rings.infinity import infinity as infinity
from sage.rings.real_mpfr import RR as RR
from sage.structure.sage_object import SageObject as SageObject
from sage.symbolic.constants import I as I, pi as pi
from sage.symbolic.ring import SR as SR

class HyperbolicGeodesic(SageObject):
    """
    Abstract base class for oriented geodesics that are not necessarily
    complete.

    INPUT:

    - ``start`` -- a HyperbolicPoint or coordinates of a point in
      hyperbolic space representing the start of the geodesic

    - ``end`` -- a HyperbolicPoint or coordinates of a point in
      hyperbolic space representing the end of the geodesic

    EXAMPLES:

    We can construct a hyperbolic geodesic in any model::

        sage: HyperbolicPlane().UHP().get_geodesic(1, 0)
        Geodesic in UHP from 1 to 0
        sage: HyperbolicPlane().PD().get_geodesic(1, 0)
        Geodesic in PD from 1 to 0
        sage: HyperbolicPlane().KM().get_geodesic((0,1/2), (1/2, 0))
        Geodesic in KM from (0, 1/2) to (1/2, 0)
        sage: HyperbolicPlane().HM().get_geodesic((0,0,1), (0,1, sqrt(2)))
        Geodesic in HM from (0, 0, 1) to (0, 1, sqrt(2))
    """
    def __init__(self, model, start, end, **graphics_options) -> None:
        """
        See :class:`HyperbolicGeodesic` for full documentation.

        EXAMPLES::

            sage: HyperbolicPlane().UHP().get_geodesic(I, 2 + I)
            Geodesic in UHP from I to I + 2
        """
    def __eq__(self, other):
        """
        Return ``True`` if ``self`` is equal to other as an oriented geodesic.

        EXAMPLES::

            sage: g1 = HyperbolicPlane().UHP().get_geodesic(I, 2*I)
            sage: g2 = HyperbolicPlane().UHP().get_geodesic(2*I, I)
            sage: g1 == g2
            False
            sage: g1 == g1
            True
        """
    def __ne__(self, other):
        """
        Test unequality of ``self`` and ``other``.

        EXAMPLES::

            sage: g1 = HyperbolicPlane().UHP().get_geodesic(I, 2*I)
            sage: g2 = HyperbolicPlane().UHP().get_geodesic(2*I, I)
            sage: g1 != g2
            True
            sage: g1 != g1
            False
        """
    def start(self):
        """
        Return the starting point of the geodesic.

        EXAMPLES::

            sage: g = HyperbolicPlane().UHP().get_geodesic(I, 3*I)
            sage: g.start()
            Point in UHP I
        """
    def end(self):
        """
        Return the starting point of the geodesic.

        EXAMPLES::

            sage: g = HyperbolicPlane().UHP().get_geodesic(I, 3*I)
            sage: g.end()
            Point in UHP 3*I
        """
    def endpoints(self):
        """
        Return a list containing the start and endpoints.

        EXAMPLES::

            sage: g = HyperbolicPlane().UHP().get_geodesic(I, 3*I)
            sage: g.endpoints()
            [Point in UHP I, Point in UHP 3*I]
        """
    def model(self):
        """
        Return the model to which the :class:`HyperbolicGeodesic` belongs.

        EXAMPLES::

            sage: UHP = HyperbolicPlane().UHP()
            sage: UHP.get_geodesic(I, 2*I).model()
            Hyperbolic plane in the Upper Half Plane Model

            sage: PD = HyperbolicPlane().PD()
            sage: PD.get_geodesic(0, I/2).model()
            Hyperbolic plane in the Poincare Disk Model

            sage: KM = HyperbolicPlane().KM()
            sage: KM.get_geodesic((0, 0), (0, 1/2)).model()
            Hyperbolic plane in the Klein Disk Model

            sage: HM = HyperbolicPlane().HM()
            sage: HM.get_geodesic((0, 0, 1), (0, 1, sqrt(2))).model()
            Hyperbolic plane in the Hyperboloid Model
        """
    def to_model(self, model):
        """
        Convert the current object to image in another model.

        INPUT:

        - ``model`` -- the image model

        EXAMPLES::

            sage: UHP = HyperbolicPlane().UHP()
            sage: PD = HyperbolicPlane().PD()
            sage: UHP.get_geodesic(I, 2*I).to_model(PD)
            Geodesic in PD from 0 to 1/3*I
            sage: UHP.get_geodesic(I, 2*I).to_model('PD')
            Geodesic in PD from 0 to 1/3*I
        """
    def graphics_options(self):
        """
        Return the graphics options of ``self``.

        EXAMPLES::

            sage: g = HyperbolicPlane().UHP().get_geodesic(I, 2*I, color='red')
            sage: g.graphics_options()
            {'color': 'red'}
        """
    def update_graphics(self, update: bool = False, **options) -> None:
        '''
        Update the graphics options of ``self``.

        INPUT:

        - ``update`` -- if ``True``, the original option are updated
          rather than overwritten

        EXAMPLES::

            sage: g = HyperbolicPlane().UHP().get_geodesic(I, 2*I)
            sage: g.graphics_options()
            {}

            sage: g.update_graphics(color = "red"); g.graphics_options()
            {\'color\': \'red\'}

            sage: g.update_graphics(color = "blue"); g.graphics_options()
            {\'color\': \'blue\'}

            sage: g.update_graphics(True, size = 20); g.graphics_options()
            {\'color\': \'blue\', \'size\': 20}
        '''
    def is_complete(self):
        """
        Return ``True`` if ``self`` is a complete geodesic (that is, both
        endpoints are on the ideal boundary) and ``False`` otherwise.

        If we represent complete geodesics using green color and incomplete
        using red colors we have the following graphic:

        .. PLOT::

            UHP = HyperbolicPlane().UHP()
            g = UHP.get_geodesic(1.5*I, 2.5*I)
            h = UHP.get_geodesic(0, I)
            l = UHP.get_geodesic(2, 4)
            m = UHP.get_geodesic(3, infinity)
            G = g.plot(color='red') +\\\n                text('is_complete()=False',
                     (0, 2),
                     horizontal_alignement='left')
            H = h.plot(color='red') +\\\n                text('is_complete()=False',
                     (0, 0.5),
                     horizontal_alignement='left')
            L = l.plot(color='green') +\\\n                text('is_complete()=True',
                     (5, 1.5))
            M = m.plot(color='green') + text('is complete()=True',
                                             (5, 4),
                                             horizontal_alignement='left')
            sphinx_plot(G+H+L+M)

        Notice, that there is no visual indication that the *vertical* geodesic
        is complete

        EXAMPLES::

            sage: UHP = HyperbolicPlane().UHP()
            sage: UHP.get_geodesic(1.5*I, 2.5*I).is_complete()
            False
            sage: UHP.get_geodesic(0, I).is_complete()
            False
            sage: UHP.get_geodesic(3, infinity).is_complete()
            True
            sage: UHP.get_geodesic(2,5).is_complete()
            True
        """
    def is_asymptotically_parallel(self, other):
        """
        Return ``True`` if ``self`` and ``other`` are asymptotically
        parallel and ``False`` otherwise.

        INPUT:

        - ``other`` -- a hyperbolic geodesic

        EXAMPLES::

            sage: g = HyperbolicPlane().UHP().get_geodesic(-2,5)
            sage: h = HyperbolicPlane().UHP().get_geodesic(-2,4)
            sage: g.is_asymptotically_parallel(h)
            True

        .. PLOT::

             g = HyperbolicPlane().UHP().get_geodesic(-2.0,5.0)
             h = HyperbolicPlane().UHP().get_geodesic(-2.0,4.0)
             sphinx_plot(g.plot(color='green')+h.plot(color='green'))

        Ultraparallel geodesics are not asymptotically parallel::

            sage: g = HyperbolicPlane().UHP().get_geodesic(-2,5)
            sage: h = HyperbolicPlane().UHP().get_geodesic(-1,4)
            sage: g.is_asymptotically_parallel(h)
            False

        .. PLOT::

             g = HyperbolicPlane().UHP().get_geodesic(-2.0,5.0)
             h = HyperbolicPlane().UHP().get_geodesic(-1.0,4.0)
             sphinx_plot(g.plot(color='red')+h.plot(color='red'))


        No hyperbolic geodesic is asymptotically parallel to itself::

            sage: g = HyperbolicPlane().UHP().get_geodesic(-2,5)
            sage: g.is_asymptotically_parallel(g)
            False
        """
    def is_ultra_parallel(self, other):
        """
        Return ``True`` if ``self`` and ``other`` are ultra parallel
        and ``False`` otherwise.

        INPUT:

        - ``other`` -- a hyperbolic geodesic

        EXAMPLES::

            sage: from sage.geometry.hyperbolic_space.hyperbolic_geodesic \\\n            ....:   import *
            sage: g = HyperbolicPlane().UHP().get_geodesic(0,1)
            sage: h = HyperbolicPlane().UHP().get_geodesic(-3,-1)
            sage: g.is_ultra_parallel(h)
            True

        .. PLOT::

             g = HyperbolicPlane().UHP().get_geodesic(0.0,1.1)
             h = HyperbolicPlane().UHP().get_geodesic(-3.0,-1.0)
             sphinx_plot(g.plot(color='green')+h.plot(color='green'))

        ::

            sage: g = HyperbolicPlane().UHP().get_geodesic(-2,5)
            sage: h = HyperbolicPlane().UHP().get_geodesic(2,6)
            sage: g.is_ultra_parallel(h)
            False

        .. PLOT::

             g = HyperbolicPlane().UHP().get_geodesic(-2,5)
             h = HyperbolicPlane().UHP().get_geodesic(2,6)
             sphinx_plot(g.plot(color='red')+h.plot(color='red'))

        ::

            sage: g = HyperbolicPlane().UHP().get_geodesic(-2,5)
            sage: g.is_ultra_parallel(g)
            False
        """
    def is_parallel(self, other):
        """
        Return ``True`` if the two given hyperbolic geodesics are either
        ultra parallel or asymptotically parallel and ``False`` otherwise.

        INPUT:

        - ``other`` -- a hyperbolic geodesic in any model

        OUTPUT:

        ``True`` if the given geodesics are either ultra parallel or
        asymptotically parallel, ``False`` if not.

        EXAMPLES::

            sage: g = HyperbolicPlane().UHP().get_geodesic(-2,5)
            sage: h = HyperbolicPlane().UHP().get_geodesic(5,12)
            sage: g.is_parallel(h)
            True

        .. PLOT::

            g = HyperbolicPlane().UHP().get_geodesic(-2,5)
            h = HyperbolicPlane().UHP().get_geodesic(5,12)
            sphinx_plot(g.plot(color='green')+h.plot(color='green'))

        ::

            sage: g = HyperbolicPlane().UHP().get_geodesic(-2,5)
            sage: h = HyperbolicPlane().UHP().get_geodesic(-2,4)
            sage: g.is_parallel(h)
            True

        .. PLOT::

            g = HyperbolicPlane().UHP().get_geodesic(-2.0,5.0)
            h = HyperbolicPlane().UHP().get_geodesic(-2.0,4.0)
            sphinx_plot(g.plot(color='green')+h.plot(color='green'))

        ::

            sage: g = HyperbolicPlane().UHP().get_geodesic(-2,2)
            sage: h = HyperbolicPlane().UHP().get_geodesic(-1,4)
            sage: g.is_parallel(h)
            False

        .. PLOT::

            g = HyperbolicPlane().UHP().get_geodesic(-2,2)
            h = HyperbolicPlane().UHP().get_geodesic(-1,4)
            sphinx_plot(g.plot(color='red')+h.plot(color='red'))


        No hyperbolic geodesic is either ultra parallel or
        asymptotically parallel to itself::

            sage: g = HyperbolicPlane().UHP().get_geodesic(-2,5)
            sage: g.is_parallel(g)
            False
        """
    def ideal_endpoints(self):
        """
        Return the ideal endpoints in bounded models.  Raise a
        :exc:`NotImplementedError` in models that are not bounded.

        EXAMPLES::

            sage: H = HyperbolicPlane()
            sage: UHP = H.UHP()
            sage: UHP.get_geodesic(1 + I, 1 + 3*I).ideal_endpoints()
            [Boundary point in UHP 1, Boundary point in UHP +Infinity]

            sage: PD = H.PD()
            sage: PD.get_geodesic(0, I/2).ideal_endpoints()
            [Boundary point in PD -I, Boundary point in PD I]

            sage: KM = H.KM()
            sage: KM.get_geodesic((0,0), (0, 1/2)).ideal_endpoints()
            [Boundary point in KM (0, -1), Boundary point in KM (0, 1)]

            sage: HM = H.HM()
            sage: HM.get_geodesic((0,0,1), (1, 0, sqrt(2))).ideal_endpoints()
            Traceback (most recent call last):
            ...
            NotImplementedError: boundary points are not implemented in
             the HM model
        """
    def complete(self):
        """
        Return the geodesic with ideal endpoints in bounded models.  Raise a
        :exc:`NotImplementedError` in models that are not bounded.
        In the following examples we represent complete geodesics by a dashed
        line.

        EXAMPLES::

            sage: H = HyperbolicPlane()
            sage: UHP = H.UHP()
            sage: UHP.get_geodesic(1 + I, 1 + 3*I).complete()
            Geodesic in UHP from 1 to +Infinity

        .. PLOT::

             g = HyperbolicPlane().UHP().get_geodesic(1 + I, 1 + 3*I)
             h = g.complete()
             sphinx_plot(g.plot()+h.plot(linestyle='dashed'))

        ::

            sage: PD = H.PD()
            sage: PD.get_geodesic(0, I/2).complete()
            Geodesic in PD from -I to I
            sage: PD.get_geodesic(0.25*(-1-I),0.25*(1-I)).complete()
            Geodesic in PD from -0.895806416477617 - 0.444444444444444*I to 0.895806416477617 - 0.444444444444444*I

        .. PLOT::

            PD = HyperbolicPlane().PD()
            g = PD.get_geodesic(0, I/2)
            h = g. complete()
            m = PD.get_geodesic(0.25*(-1-I),0.25*(1-I))
            l = m.complete()
            sphinx_plot(g.plot()+h.plot(linestyle='dashed') +
                        m.plot()+l.plot(linestyle='dashed'))

        ::

            sage: KM = H.KM()
            sage: KM.get_geodesic((0,0), (0,1/2)).complete()
            Geodesic in KM from (0, -1) to (0, 1)

        .. PLOT::

            g = HyperbolicPlane().KM().get_geodesic(CC(0,0), CC(0, 0.5))
            h = g.complete()
            sphinx_plot(g.plot()+h.plot(linestyle='dashed'))

        ::

            sage: KM.get_geodesic(-I, 1).complete()
            Geodesic in KM from -I to 1

        .. PLOT::

            g = HyperbolicPlane().KM().get_geodesic(CC(0,-1), CC(1, 0))
            h = g.complete()
            sphinx_plot(g.plot()+h.plot(linestyle='dashed'))


        ::

            sage: HM = H.HM()
            sage: HM.get_geodesic((0,0,1), (1, 0, sqrt(2))).complete()
            Geodesic in HM from (0, 0, 1) to (1, 0, sqrt(2))

        .. PLOT::

            g = HyperbolicPlane().HM().get_geodesic((0,0,1), (1, 0, sqrt(2)))
            h = g.complete()
            sphinx_plot(g.plot(color='black')+h.plot(linestyle='dashed',color='black'))

        ::

            sage: g = HM.get_geodesic((0,0,1), (1, 0, sqrt(2))).complete()
            sage: g.is_complete()
            True

        TESTS:

        Check that floating points remain floating points through this method::

            sage: H = HyperbolicPlane()
            sage: g = H.UHP().get_geodesic(CC(0,1), CC(2,2))
            sage: gc = g.complete()
            sage: parent(gc.start().coordinates())
            Real Field with 53 bits of precision
        """
    def reflection_involution(self):
        """
        Return the involution fixing ``self``.

        EXAMPLES::

            sage: H = HyperbolicPlane()
            sage: gU = H.UHP().get_geodesic(2,4)
            sage: RU = gU.reflection_involution(); RU
            Isometry in UHP
            [ 3 -8]
            [ 1 -3]

            sage: RU*gU == gU
            True

            sage: gP = H.PD().get_geodesic(0, I)
            sage: RP = gP.reflection_involution(); RP
            Isometry in PD
            [ 1  0]
            [ 0 -1]

            sage: RP*gP == gP
            True

            sage: gK = H.KM().get_geodesic((0,0), (0,1))
            sage: RK = gK.reflection_involution(); RK
            Isometry in KM
            [-1  0  0]
            [ 0  1  0]
            [ 0  0  1]

            sage: RK*gK == gK
            True

            sage: HM = H.HM()
            sage: g = HM.get_geodesic((0,0,1), (1,0, n(sqrt(2))))
            sage: A = g.reflection_involution()
            sage: B = diagonal_matrix([1, -1, 1])
            sage: bool((B - A.matrix()).norm() < 10**-9)                                # needs scipy
            True

        The above tests go through the Upper Half Plane.  It remains to
        test that the matrices in the models do what we intend. ::

            sage: from sage.geometry.hyperbolic_space.hyperbolic_isometry \\\n            ....:   import moebius_transform
            sage: R = H.PD().get_geodesic(-1,1).reflection_involution()
            sage: bool(moebius_transform(R.matrix(), 0) == 0)
            True
        """
    def common_perpendicula(self, other):
        """
        Return the unique hyperbolic geodesic perpendicular to two given
        geodesics, if such a geodesic exists.  If none exists, raise a
        :exc:`ValueError`.

        INPUT:

        - ``other`` -- a hyperbolic geodesic in the same model as ``self``

        OUTPUT: a hyperbolic geodesic

        EXAMPLES::

            sage: g = HyperbolicPlane().UHP().get_geodesic(2,3)
            sage: h = HyperbolicPlane().UHP().get_geodesic(4,5)
            sage: g.common_perpendicular(h)
            Geodesic in UHP from 1/2*sqrt(3) + 7/2 to -1/2*sqrt(3) + 7/2

        .. PLOT::

            g = HyperbolicPlane().UHP().get_geodesic(2.0, 3.0)
            h = HyperbolicPlane().UHP().get_geodesic(4.0, 5.0)
            l = g.common_perpendicular(h)
            P = g.plot(color='blue') +\\\n                h.plot(color='blue') +\\\n                l.plot(color='orange')
            sphinx_plot(P)

        It is an error to ask for the common perpendicular of two
        intersecting geodesics::

            sage: g = HyperbolicPlane().UHP().get_geodesic(2,4)
            sage: h = HyperbolicPlane().UHP().get_geodesic(3, infinity)
            sage: g.common_perpendicular(h)
            Traceback (most recent call last):
            ...
            ValueError: geodesics intersect; no common perpendicular exists
        """
    def intersection(self, other):
        """
        Return the point of intersection of two geodesics (if such a
        point exists).

        INPUT:

        - ``other`` -- a hyperbolic geodesic in the same model as ``self``

        OUTPUT: a hyperbolic point or geodesic

        EXAMPLES::

            sage: PD = HyperbolicPlane().PD()
        """
    def perpendicular_bisector(self):
        """
        Return the perpendicular bisector of ``self`` if ``self`` has
        finite length.  Here distance is hyperbolic distance.

        EXAMPLES::

            sage: PD = HyperbolicPlane().PD()
            sage: g = PD.get_geodesic(-0.3+0.4*I,+0.7-0.1*I)
            sage: h = g.perpendicular_bisector().complete()
            sage: P = g.plot(color='blue')+h.plot(color='orange');P
            Graphics object consisting of 4 graphics primitives

        .. PLOT::

            g = HyperbolicPlane().PD().get_geodesic(-0.3+0.4*I,+0.7-0.1*I)
            h = g.perpendicular_bisector().complete()
            sphinx_plot(g.plot(color='blue')+h.plot(color='orange'))

        Complete geodesics cannot be bisected::

            sage: g = HyperbolicPlane().PD().get_geodesic(0, 1)
            sage: g.perpendicular_bisector()
            Traceback (most recent call last):
            ...
            ValueError: the length must be finite

        TESTS::

            sage: g = HyperbolicPlane().PD().random_geodesic()
            sage: h = g.perpendicular_bisector().complete()
            sage: bool(h.intersection(g)[0].coordinates() - g.midpoint().coordinates() < 10**-9)
            True

            sage: g = HyperbolicPlane().UHP().random_geodesic()
            sage: h = g.perpendicular_bisector().complete()
            sage: bool(h.intersection(g)[0].coordinates() - g.midpoint().coordinates() < 10**-9)
            True
        """
    def midpoint(self):
        """
        Return the (hyperbolic) midpoint of a hyperbolic line segment.

        EXAMPLES::

            sage: g = HyperbolicPlane().UHP().random_geodesic()
            sage: m = g.midpoint()
            sage: end1, end2 = g.endpoints()
            sage: bool(abs(m.dist(end1) - m.dist(end2)) < 10**-9)
            True

        Complete geodesics have no midpoint::

            sage: HyperbolicPlane().UHP().get_geodesic(0,2).midpoint()
            Traceback (most recent call last):
            ...
            ValueError: the length must be finite
        """
    def dist(self, other):
        """
        Return the hyperbolic distance from a given hyperbolic geodesic
        to another geodesic or point.

        INPUT:

        - ``other`` -- a hyperbolic geodesic or hyperbolic point in
          the same model

        OUTPUT: the hyperbolic distance

        EXAMPLES::

            sage: g = HyperbolicPlane().UHP().get_geodesic(2, 4.0)
            sage: h = HyperbolicPlane().UHP().get_geodesic(5, 7.0)
            sage: bool(abs(g.dist(h).n() - 1.92484730023841) < 10**-9)
            True

        If the second object is a geodesic ultraparallel to the first,
        or if it is a point on the boundary that is not one of the
        first object's endpoints, then return +infinity

        ::

            sage: g = HyperbolicPlane().UHP().get_geodesic(2, 2+I)
            sage: p = HyperbolicPlane().UHP().get_point(5)
            sage: g.dist(p)
            +Infinity

        TESTS:

        Check that floating points remain floating points in :meth:`dist` ::

            sage: UHP = HyperbolicPlane().UHP()
            sage: g = UHP.get_geodesic(CC(0,1), CC(2,2))
            sage: UHP.dist(g.start(), g.end())
            1.45057451382258
            sage: parent(_)
            Real Field with 53 bits of precision
        """
    def angle(self, other):
        """
        Return the angle  between any two given geodesics if they
        intersect.

        INPUT:

        - ``other`` -- a hyperbolic geodesic in the same model as ``self``

        OUTPUT: the angle in radians between the two given geodesics

        EXAMPLES::

            sage: PD = HyperbolicPlane().PD()
            sage: g = PD.get_geodesic(3/5*I + 4/5, 15/17*I + 8/17)
            sage: h = PD.get_geodesic(4/5*I + 3/5, I)
            sage: g.angle(h)
            1/2*pi

        .. PLOT::

            PD = HyperbolicPlane().PD()
            g = PD.get_geodesic(3.0/5.0*I + 4.0/5.0, 15.0/17.0*I + 8.0/17.0)
            h = PD.get_geodesic(4.0/5.0*I + 3.0/5.0, I)
            sphinx_plot(g.plot()+h.plot(color='orange'))
        """
    def length(self):
        """
        Return the Hyperbolic length of the hyperbolic line segment.

        EXAMPLES::

            sage: g = HyperbolicPlane().UHP().get_geodesic(2 + I, 3 + I/2)
            sage: g.length()
            arccosh(9/4)
        """

class HyperbolicGeodesicUHP(HyperbolicGeodesic):
    """
    Create a geodesic in the upper half plane model.

    The geodesics in this model are represented by circular arcs perpendicular
    to the real axis (half-circles whose origin is on the real axis) and
    straight vertical lines ending on the real axis.

    INPUT:

    - ``start`` -- a :class:`HyperbolicPoint` in hyperbolic space
      representing the start of the geodesic

    - ``end`` -- a :class:`HyperbolicPoint` in hyperbolic space
      representing the end of the geodesic

    EXAMPLES::

        sage: UHP = HyperbolicPlane().UHP()
        sage: g = UHP.get_geodesic(UHP.get_point(I), UHP.get_point(2 + I))
        sage: g = UHP.get_geodesic(I, 2 + I)
        sage: h = UHP.get_geodesic(-1, -1+2*I)

    .. PLOT::

        UHP = HyperbolicPlane().UHP()
        g = UHP.get_geodesic(I, 2 + I)
        h = UHP.get_geodesic(-1, -1+2*I)
        sphinx_plot(g.plot()+h.plot())
    """
    def reflection_involution(self):
        """
        Return the isometry of the involution fixing the geodesic ``self``.

        EXAMPLES::

            sage: UHP = HyperbolicPlane().UHP()
            sage: g1 = UHP.get_geodesic(0, 1)
            sage: g1.reflection_involution()
            Isometry in UHP
            [ 1  0]
            [ 2 -1]
            sage: UHP.get_geodesic(I, 2*I).reflection_involution()
            Isometry in UHP
            [ 1  0]
            [ 0 -1]
        """
    def plot(self, boundary: bool = True, **options):
        """
        Plot ``self``.

        EXAMPLES::

            sage: UHP = HyperbolicPlane().UHP()
            sage: UHP.get_geodesic(0, 1).plot()                                         # needs sage.plot
            Graphics object consisting of 2 graphics primitives

        .. PLOT::

            UHP = HyperbolicPlane().UHP()
            g = UHP.get_geodesic(0.0, 1.0).plot()
            sphinx_plot(g)

        ::

            sage: UHP.get_geodesic(I, 3+4*I).plot(linestyle='dashed', color='brown')    # needs sage.plot
            Graphics object consisting of 2 graphics primitives

        .. PLOT::

            UHP = HyperbolicPlane().UHP()
            g = UHP.get_geodesic(I, 3+4*I).plot(linestyle='dashed', color='brown')
            sphinx_plot(g)

        ::

            sage: UHP.get_geodesic(1, infinity).plot(color='orange')                    # needs sage.plot
            Graphics object consisting of 2 graphics primitives

        .. PLOT::

            UHP = HyperbolicPlane().UHP()
            g = UHP.get_geodesic(1, infinity).plot(color='orange')
            sphinx_plot(g)

        TESTS:

        Plotting a line with ``boundary=True``. ::

            sage: g = HyperbolicPlane().UHP().get_geodesic(0, I)
            sage: g.plot()                                                              # needs sage.plot
            Graphics object consisting of 2 graphics primitives

        Plotting a line with ``boundary=False``. ::

            sage: g = HyperbolicPlane().UHP().get_geodesic(0, I)
            sage: g.plot(boundary=False)                                                # needs sage.plot
            Graphics object consisting of 1 graphics primitive

        Plotting a circle with ``boundary=True``. ::

            sage: g = HyperbolicPlane().UHP().get_geodesic(-3, 19)
            sage: g.plot()                                                              # needs sage.plot
            Graphics object consisting of 2 graphics primitives

        Plotting a circle with ``boundary=False``. ::

            sage: g = HyperbolicPlane().UHP().get_geodesic(3, 4)
            sage: g.plot(boundary=False)                                                # needs sage.plot
            Graphics object consisting of 1 graphics primitive
        """
    def ideal_endpoints(self):
        """
        Determine the ideal (boundary) endpoints of the complete
        hyperbolic geodesic corresponding to ``self``.

        OUTPUT: list of 2 boundary points

        EXAMPLES::

            sage: UHP = HyperbolicPlane().UHP()
            sage: UHP.get_geodesic(I, 2*I).ideal_endpoints()
            [Boundary point in UHP 0,
             Boundary point in UHP +Infinity]
            sage: UHP.get_geodesic(1 + I, 2 + 4*I).ideal_endpoints()
            [Boundary point in UHP -sqrt(65) + 9,
             Boundary point in UHP sqrt(65) + 9]

        TESTS:

        Check that :issue:`32362` is fixed::

            sage: PD = HyperbolicPlane().PD()
            sage: z0 = CC(-0.0571909584179366 + 0.666666666666667*I)
            sage: z1 = CC(-1)
            sage: pts = PD.get_geodesic(z0, z1).ideal_endpoints()
            sage: pts[1]
            Boundary point in PD I
        """
    def common_perpendicular(self, other):
        """
        Return the unique hyperbolic geodesic perpendicular to ``self``
        and ``other``, if such a geodesic exists; otherwise raise a
        :exc:`ValueError`.

        INPUT:

        - ``other`` -- a hyperbolic geodesic in current model

        OUTPUT: a hyperbolic geodesic

        EXAMPLES::

            sage: UHP = HyperbolicPlane().UHP()
            sage: g = UHP.get_geodesic(2, 3)
            sage: h = UHP.get_geodesic(4, 5)
            sage: g.common_perpendicular(h)
            Geodesic in UHP from 1/2*sqrt(3) + 7/2 to -1/2*sqrt(3) + 7/2

        .. PLOT::

            UHP = HyperbolicPlane().UHP()
            g = UHP.get_geodesic(2.0, 3.0)
            h = UHP.get_geodesic(4.0, 5.0)
            p = g.common_perpendicular(h)
            sphinx_plot(g.plot(color='blue')+h.plot(color='blue')+p.plot(color='orange'))

        It is an error to ask for the common perpendicular of two
        intersecting geodesics::

            sage: g = UHP.get_geodesic(2, 4)
            sage: h = UHP.get_geodesic(3, infinity)
            sage: g.common_perpendicular(h)
            Traceback (most recent call last):
            ...
            ValueError: geodesics intersect; no common perpendicular exists
        """
    def intersection(self, other):
        """
        Return the point of intersection of ``self`` and ``other``
        (if such a point exists).

        INPUT:

        - ``other`` -- a hyperbolic geodesic in the current model

        OUTPUT: list of hyperbolic points or a hyperbolic geodesic

        EXAMPLES::

            sage: UHP = HyperbolicPlane().UHP()
            sage: g = UHP.get_geodesic(3, 5)
            sage: h = UHP.get_geodesic(4, 7)
            sage: g.intersection(h)
            [Point in UHP 2/3*sqrt(-2) + 13/3]

        .. PLOT::

            UHP = HyperbolicPlane().UHP()
            g = UHP.get_geodesic(3, 5)
            h = UHP.get_geodesic(4, 7)
            P = g.intersection(h)
            pict = g.plot(color='red')+h.plot(color='red')
            sphinx_plot(pict)

        If the given geodesics do not intersect, the function returns an
        empty list::

            sage: g = UHP.get_geodesic(4, 5)
            sage: h = UHP.get_geodesic(6, 7)
            sage: g.intersection(h)
            []

        .. PLOT::

            UHP = HyperbolicPlane().UHP()
            g = UHP.get_geodesic(4.0, 5.0)
            h = UHP.get_geodesic(6.0, 7.0)
            sphinx_plot(g.plot() + h.plot())

        If the given geodesics are asymptotically parallel, the function returns the common boundary point::

            sage: g = UHP.get_geodesic(4, 5)
            sage: h = UHP.get_geodesic(5, 7)
            sage: g.intersection(h)
            [Boundary point in UHP 5.00000000000000]

        .. PLOT::

            UHP = HyperbolicPlane().UHP()
            g = UHP.get_geodesic(4.0, 5.0)
            h = UHP.get_geodesic(6.0, 7.0)
            sphinx_plot(g.plot() + h.plot())

        If the given geodesics are identical, return that
        geodesic::

            sage: g = UHP.get_geodesic(4 + I, 18*I)
            sage: h = UHP.get_geodesic(4 + I, 18*I)
            sage: g.intersection(h)
            Geodesic in UHP from I + 4 to 18*I

        TESTS:

            sage: UHP = HyperbolicPlane().UHP()
            sage: g1 = UHP.get_geodesic(2*QQbar.gen(), 5)
            sage: g2 = UHP.get_geodesic(-1/2, Infinity)
            sage: g1.intersection(g2)
            []

            sage: UHP = HyperbolicPlane().UHP() #case Ia
            sage: UHP = HyperbolicPlane().UHP()
            sage: g1=UHP.get_geodesic(-1,I)
            sage: g2=UHP.get_geodesic(0,2)
            sage: g1.intersection(g2)
            []

            sage: UHP = HyperbolicPlane().UHP() #case Ib
            sage: g1=UHP.get_geodesic(-1,I)
            sage: g2=UHP.get_geodesic(1/2,1/2+2*I)
            sage: g1.intersection(g2)
            []

            sage: UHP = HyperbolicPlane().UHP() #case IIa
            sage: g1=UHP.get_geodesic(-1,+1)
            sage: g2=UHP.get_geodesic(-1,2)
            sage: g1.intersection(g2)
            [Boundary point in UHP -1.00000000000000]

            sage: UHP = HyperbolicPlane().UHP() #case IIb
            sage: g1=UHP.get_geodesic(-1,+Infinity)
            sage: g2=UHP.get_geodesic(+1,+Infinity)
            sage: g1.intersection(g2)
            [Boundary point in UHP +infinity]

            sage: UHP = HyperbolicPlane().UHP() #case IIc
            sage: g1=UHP.get_geodesic(-1,-1+I)
            sage: g2=UHP.get_geodesic(+1,+1+I)
            sage: g1.intersection(g2)
            []

            sage: UHP = HyperbolicPlane().UHP() #case IId
            sage: g1=UHP.get_geodesic(-1,+1)
            sage: g2=UHP.get_geodesic(-1,-1+2*I)
            sage: g1.intersection(g2)
            [Boundary point in UHP -1.00000000000000]

            sage: UHP = HyperbolicPlane().UHP() #case IIIa
            sage: g1=UHP.get_geodesic(-1,I)
            sage: g2=UHP.get_geodesic(+1,(+cos(pi/3)+I*sin(pi/3)))
            sage: g1.intersection(g2)
            []

            sage: UHP = HyperbolicPlane().UHP() #case IIIb
            sage: g1=UHP.get_geodesic(I,2*I)
            sage: g2=UHP.get_geodesic(3*I,4*I)
            sage: g1.intersection(g2)
            []

            sage: UHP = HyperbolicPlane().UHP() #case IVa
            sage: g1=UHP.get_geodesic(3*I,Infinity)
            sage: g2=UHP.get_geodesic(2*I,4*I)
            sage: g1.intersection(g2)
            Geodesic in UHP from 3.00000000000000*I to 4.00000000000000*I

            sage: UHP = HyperbolicPlane().UHP() #case IVb
            sage: g1=UHP.get_geodesic(I,3*I)
            sage: g2=UHP.get_geodesic(2*I,4*I)
            sage: g1.intersection(g2)
            Geodesic in UHP from 2.00000000000000*I to 3.00000000000000*I

            sage: UHP = HyperbolicPlane().UHP() #case IVc
            sage: g1=UHP.get_geodesic(2*I,infinity)
            sage: g2=UHP.get_geodesic(3*I,infinity)
            sage: g1.intersection(g2)
            Geodesic in UHP from 3.00000000000000*I to +infinity
        """
    def perpendicular_bisector(self):
        """
        Return the perpendicular bisector of the hyperbolic geodesic ``self``
        if that geodesic has finite length.

        EXAMPLES::

             sage: UHP = HyperbolicPlane().UHP()
             sage: g = UHP.random_geodesic()
             sage: h = g.perpendicular_bisector().complete()
             sage: c = lambda x: x.coordinates()
             sage: bool(c(g.intersection(h)[0]) - c(g.midpoint()) < 10**-9)
             True

        ::

            sage: UHP = HyperbolicPlane().UHP()
            sage: g = UHP.get_geodesic(1+I,2+0.5*I)
            sage: h = g.perpendicular_bisector().complete()
            sage: show(g.plot(color='blue')+h.plot(color='orange'))

        .. PLOT::

            UHP = HyperbolicPlane().UHP()
            g = UHP.get_geodesic(1+I,2+0.5*I)
            h = g.perpendicular_bisector().complete()
            sphinx_plot(g.plot(color='blue')+h.plot(color='orange'))

        Infinite geodesics cannot be bisected::

            sage: UHP.get_geodesic(0, 1).perpendicular_bisector()
            Traceback (most recent call last):
            ...
            ValueError: the length must be finite

        TESTS:

        Check the result is independent of the order (:issue:`29936`)::

            sage: def bisector_gets_midpoint(a, b):
            ....:     UHP = HyperbolicPlane().UHP()
            ....:     g = UHP.get_geodesic(a, b)
            ....:     p = g.perpendicular_bisector()
            ....:     x = g.intersection(p)[0]
            ....:     m = g.midpoint()
            ....:     return bool(x.dist(m) < 1e-9)
            sage: c, d, e = CC(1, 1), CC(2, 1), CC(2, 0.5)
            sage: pairs = [(c, d), (d, c), (c, e), (e, c), (d, e), (e, d)]
            sage: all(bisector_gets_midpoint(a, b) for a, b in pairs)                   # needs scipy
            True
        """
    def midpoint(self):
        """
        Return the (hyperbolic) midpoint of ``self`` if it exists.

        EXAMPLES::

            sage: UHP = HyperbolicPlane().UHP()
            sage: g = UHP.random_geodesic()
            sage: m = g.midpoint()
            sage: d1 = UHP.dist(m, g.start())
            sage: d2 = UHP.dist(m, g.end())
            sage: bool(abs(d1 - d2) < 10**-9)
            True

        Infinite geodesics have no midpoint::

            sage: UHP.get_geodesic(0, 2).midpoint()
            Traceback (most recent call last):
            ...
            ValueError: the length must be finite

        TESTS:

        This checks :issue:`20330` so that geodesics defined by symbolic
        expressions do not generate runtime errors. ::

            sage: g=HyperbolicPlane().UHP().get_geodesic(-1+I,1+I)
            sage: point = g.midpoint(); point
            Point in UHP -1/2*(sqrt(2)*...
            sage: QQbar(point.coordinates()).radical_expression()  # long time
            I*sqrt(2)

        Check that floating points remain floating points
        in :meth:`midpoint`::

            sage: UHP = HyperbolicPlane().UHP()
            sage: g = UHP.get_geodesic(CC(0,1), CC(2,2))
            sage: g.midpoint()
            Point in UHP 0.666666666666667 + 1.69967317119760*I
            sage: parent(g.midpoint().coordinates())
            Complex Field with 53 bits of precision

        Check that the midpoint is independent of the order (:issue:`29936`)::

            sage: g = UHP.get_geodesic(1+I, 2+0.5*I)
            sage: h = UHP.get_geodesic(2+0.5*I, 1+I)
            sage: abs(g.midpoint().coordinates() - h.midpoint().coordinates()) < 1e-9
            True

            sage: g = UHP.get_geodesic(2+I, 2+0.5*I)
            sage: h = UHP.get_geodesic(2+0.5*I, 2+I)
            sage: abs(g.midpoint().coordinates() - h.midpoint().coordinates()) < 1e-9
            True
        """
    def angle(self, other):
        """
        Return the angle between the completions of any two given
        geodesics if they intersect.

        INPUT:

        - ``other`` -- a hyperbolic geodesic in the UHP model

        OUTPUT: the angle in radians between the two given geodesics

        EXAMPLES::

            sage: UHP = HyperbolicPlane().UHP()
            sage: g = UHP.get_geodesic(2, 4)
            sage: h = UHP.get_geodesic(3, 3 + I)
            sage: g.angle(h)
            1/2*pi
            sage: numerical_approx(g.angle(h))
            1.57079632679490

        .. PLOT::

            UHP = HyperbolicPlane().UHP()
            g = UHP.get_geodesic(2, 4)
            h = UHP.get_geodesic(3, 3 + I)
            sphinx_plot(g.plot()+h.plot())

        If the geodesics are identical, return angle 0::

            sage: g.angle(g)
            0

        It is an error to ask for the angle of two geodesics that do not
        intersect::

            sage: g = UHP.get_geodesic(2, 4)
            sage: h = UHP.get_geodesic(5, 7)
            sage: g.angle(h)
            Traceback (most recent call last):
            ...
            ValueError: geodesics do not intersect

        TESTS:

        Points as parameters raise an error. ::

            sage: g = HyperbolicPlane().UHP().get_geodesic(I, I)
            sage: h = HyperbolicPlane().UHP().get_geodesic(-1, 1)
            sage: g.angle(h)
            Traceback (most recent call last):
            ...
            ValueError: intersecting geodesic is a point
            sage: h.angle(g)
            Traceback (most recent call last):
            ...
            ValueError: intersecting geodesic is a point

            sage: g = HyperbolicPlane().UHP().get_geodesic(I, I)
            sage: h = HyperbolicPlane().UHP().get_geodesic(0, infinity)
            sage: g.angle(h)
            Traceback (most recent call last):
            ...
            ValueError: intersecting geodesic is a point
            sage: h.angle(g)
            Traceback (most recent call last):
            ...
            ValueError: intersecting geodesic is a point

        Intersections in boundary points raise an error. ::

            sage: g = HyperbolicPlane().UHP().get_geodesic(1, 3)
            sage: h = HyperbolicPlane().UHP().get_geodesic(1, 2)
            sage: g.angle(h)
            Traceback (most recent call last):
            ...
            ValueError: geodesics do not intersect
            sage: h.angle(g)
            Traceback (most recent call last):
            ...
            ValueError: geodesics do not intersect

            sage: g = HyperbolicPlane().UHP().get_geodesic(1, 2)
            sage: h = HyperbolicPlane().UHP().get_geodesic(1, Infinity)
            sage: g.angle(h)
            Traceback (most recent call last):
            ...
            ValueError: geodesics do not intersect
            sage: h.angle(g)
            Traceback (most recent call last):
            ...
            ValueError: geodesics do not intersect

        Parallel lines raise an error. ::

            sage: g = HyperbolicPlane().UHP().get_geodesic(-2, -2 + 4*I)
            sage: h = HyperbolicPlane().UHP().get_geodesic(9, Infinity)
            sage: g.angle(h)
            Traceback (most recent call last):
            ...
            ValueError: geodesics do not intersect
            sage: h.angle(g)
            Traceback (most recent call last):
            ...
            ValueError: geodesics do not intersect

        Non-intersecting circles raise an error. ::

            sage: g = HyperbolicPlane().UHP().get_geodesic(-2, -1)
            sage: h = HyperbolicPlane().UHP().get_geodesic( 2,  1)
            sage: g.angle(h)
            Traceback (most recent call last):
            ...
            ValueError: geodesics do not intersect
            sage: h.angle(g)
            Traceback (most recent call last):
            ...
            ValueError: geodesics do not intersect

        Non-intersecting line and circle raise an error. ::

            sage: g = HyperbolicPlane().UHP().get_geodesic(-2, -2 + 4*I)
            sage: h = HyperbolicPlane().UHP().get_geodesic( 7, 9)
            sage: g.angle(h)
            Traceback (most recent call last):
            ...
            ValueError: geodesics do not intersect
            sage: h.angle(g)
            Traceback (most recent call last):
            ...
            ValueError: geodesics do not intersect

        Non-complete equal circles yield angle 0. ::

            sage: g = HyperbolicPlane().UHP().get_geodesic(-1, I)
            sage: h = HyperbolicPlane().UHP().get_geodesic(I, 1)
            sage: g.angle(h)
            0
            sage: h.angle(g)
            0

        Complete equal lines yield angle 0. ::

            sage: g = HyperbolicPlane().UHP().get_geodesic(4, Infinity)
            sage: h = HyperbolicPlane().UHP().get_geodesic(4, Infinity)
            sage: g.angle(h)
            0
            sage: h.angle(g)
            0

        Non-complete equal lines yield angle 0. ::

            sage: g = HyperbolicPlane().UHP().get_geodesic(1 +   I, 1 + 2*I)
            sage: h = HyperbolicPlane().UHP().get_geodesic(1 + 3*I, 1 + 4*I)
            sage: g.angle(h)
            0
            sage: h.angle(g)
            0

        Angle between two complete circles. ::

            sage: g = HyperbolicPlane().UHP().get_geodesic(0, 2)
            sage: h = HyperbolicPlane().UHP().get_geodesic(1, 3)
            sage: g.angle(h)
            1/3*pi
            sage: h.angle(g)
            1/3*pi

        Angle between two non-intersecting circles whose completion intersects. ::

            sage: g = HyperbolicPlane().UHP().get_geodesic(-2, 2*I)
            sage: h = HyperbolicPlane().UHP().get_geodesic(-1, 1 + 2*I)
            sage: g.angle(h)
            arccos(7/8)
            sage: h.angle(g)
            arccos(7/8)

        Angle between circle and line. Note that ``1/2*sqrt(2)`` equals
        ``1/4*pi``. ::

            sage: g = HyperbolicPlane().UHP().get_geodesic( 0, Infinity)
            sage: h = HyperbolicPlane().UHP().get_geodesic(-1, 1)
            sage: g.angle(h)
            1/2*pi
            sage: h.angle(g)
            1/2*pi

            sage: g = HyperbolicPlane().UHP().get_geodesic(1, 1 + I)
            sage: h = HyperbolicPlane().UHP().get_geodesic(-sqrt(2), sqrt(2))
            sage: g.angle(h)
            1/4*pi
            sage: h.angle(g)
            1/4*pi

        Angle is unoriented, as opposed to oriented. ::

            sage: g = HyperbolicPlane().UHP().get_geodesic(0, I)
            sage: h1 = HyperbolicPlane().UHP().get_geodesic(-1, 2)
            sage: h2 = HyperbolicPlane().UHP().get_geodesic(1, -2)
            sage: g.angle(h1)
            arccos(1/3)
            sage: h1.angle(g)
            arccos(1/3)
            sage: g.angle(h2)
            arccos(1/3)
            sage: h2.angle(g)
            arccos(1/3)
        """

class HyperbolicGeodesicPD(HyperbolicGeodesic):
    """
    A geodesic in the Poincaré disk model.

    Geodesics in this model are represented by segments of circles contained
    within the unit disk that are orthogonal to the boundary of the disk,
    plus all diameters of the disk.

    INPUT:

    - ``start`` -- a :class:`HyperbolicPoint` in hyperbolic space
      representing the start of the geodesic

    - ``end`` -- a :class:`HyperbolicPoint` in hyperbolic space
      representing the end of the geodesic

    EXAMPLES::

        sage: PD = HyperbolicPlane().PD()
        sage: g = PD.get_geodesic(PD.get_point(I), PD.get_point(-I/2))
        sage: g = PD.get_geodesic(I,-I/2)
        sage: h = PD.get_geodesic(-1/2+I/2,1/2+I/2)

    .. PLOT::

         PD = HyperbolicPlane().PD()
         g = PD.get_geodesic(I,-I/2)
         h = PD.get_geodesic(-0.5+I*0.5,0.5+I*0.5)
         sphinx_plot(g.plot()+h.plot(color='green'))
    """
    def plot(self, boundary: bool = True, **options):
        """
        Plot ``self``.

        EXAMPLES:

        First some lines::

            sage: PD = HyperbolicPlane().PD()
            sage: PD.get_geodesic(0, 1).plot()                                          # needs sage.plot
            Graphics object consisting of 2 graphics primitives

        .. PLOT::

            sphinx_plot(HyperbolicPlane().PD().get_geodesic(0, 1).plot())

        ::

            sage: PD.get_geodesic(0, 0.3+0.8*I).plot()                                  # needs sage.plot
            Graphics object consisting of 2 graphics primitives

        .. PLOT::

            PD = HyperbolicPlane().PD()
            sphinx_plot(PD.get_geodesic(0, 0.3+0.8*I).plot())

        Then some generic geodesics::

            sage: PD.get_geodesic(-0.5, 0.3+0.4*I).plot()                               # needs sage.plot
            Graphics object consisting of 2 graphics primitives
            sage: g = PD.get_geodesic(-1, exp(3*I*pi/7))
            sage: G = g.plot(linestyle='dashed',color='red'); G                         # needs sage.plot
            Graphics object consisting of 2 graphics primitives
            sage: h = PD.get_geodesic(exp(2*I*pi/11), exp(1*I*pi/11))
            sage: H = h.plot(thickness=6, color='orange'); H                            # needs sage.plot
            Graphics object consisting of 2 graphics primitives
            sage: show(G+H)                                                             # needs sage.plot

        .. PLOT::

            PD = HyperbolicPlane().PD()
            PD.get_geodesic(-0.5, 0.3+0.4*I).plot()
            g = PD.get_geodesic(-1, exp(3*I*pi/7))
            G = g.plot(linestyle='dashed',color='red')
            h = PD.get_geodesic(exp(2*I*pi/11), exp(1*I*pi/11))
            H = h.plot(thickness=6, color='orange')
            sphinx_plot(G+H)
        """

class HyperbolicGeodesicKM(HyperbolicGeodesic):
    """
    A geodesic in the Klein disk model.

    Geodesics are represented by the chords, straight line segments with ideal
    endpoints on the boundary circle.

    INPUT:

    - ``start`` -- a :class:`HyperbolicPoint` in hyperbolic space
      representing the start of the geodesic

    - ``end`` -- a :class:`HyperbolicPoint` in hyperbolic space
      representing the end of the geodesic

    EXAMPLES::

        sage: KM = HyperbolicPlane().KM()
        sage: g = KM.get_geodesic((0.1,0.9),(-0.1,-0.9))
        sage: h = KM.get_geodesic((-0.707106781,-0.707106781),(0.707106781,-0.707106781))
        sage: P = g.plot(color='orange')+h.plot(); P                                    # needs sage.plot
        Graphics object consisting of 4 graphics primitives

    .. PLOT::

        KM = HyperbolicPlane().KM()
        g = KM.get_geodesic(CC(0.1,0.9),
                            CC(-0.1,-0.9))
        h = KM.get_geodesic(CC(-0.707106781,-0.707106781),
                            CC(0.707106781,-0.707106781))
        sphinx_plot(g.plot(color='orange')+h.plot())
    """
    def plot(self, boundary: bool = True, **options):
        """
        Plot ``self``.

        EXAMPLES::

            sage: HyperbolicPlane().KM().get_geodesic(0, 1).plot()                      # needs sage.plot
            Graphics object consisting of 2 graphics primitives

        .. PLOT::

            KM = HyperbolicPlane().KM()
            sphinx_plot(KM.get_geodesic(CC(0,0), CC(1,0)).plot())
        """

class HyperbolicGeodesicHM(HyperbolicGeodesic):
    """
    A geodesic in the hyperboloid model.

    Valid points in the hyperboloid model satisfy :math:`x^2 + y^2 - z^2 = -1`

    INPUT:

    - ``start`` -- a :class:`HyperbolicPoint` in hyperbolic space
      representing the start of the geodesic

    - ``end`` -- a :class:`HyperbolicPoint` in hyperbolic space
      representing the end of the geodesic

    EXAMPLES::

        sage: HM = HyperbolicPlane().HM()
        sage: p1 = HM.get_point((4, -4, sqrt(33)))
        sage: p2 = HM.get_point((-3,-3,sqrt(19)))
        sage: g = HM.get_geodesic(p1, p2)
        sage: g = HM.get_geodesic((4, -4, sqrt(33)), (-3, -3, sqrt(19)))

    .. PLOT::

        HM = HyperbolicPlane().HM()
        p1 = HM.get_point((4, -4, sqrt(33)))
        p2 = HM.get_point((-3,-3,sqrt(19)))
        g = HM.get_geodesic(p1, p2)
        sphinx_plot(g.plot(color='blue'))
    """
    def plot(self, show_hyperboloid: bool = True, **graphics_options):
        """
        Plot ``self``.

        EXAMPLES::

            sage: from sage.geometry.hyperbolic_space.hyperbolic_geodesic \\\n            ....:    import *
            sage: g = HyperbolicPlane().HM().random_geodesic()
            sage: g.plot()                                                              # needs sage.plot
            Graphics3d Object

        .. PLOT::

            sphinx_plot(HyperbolicPlane().HM().random_geodesic().plot())
        """
