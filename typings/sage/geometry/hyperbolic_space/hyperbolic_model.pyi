from sage.categories.homset import Hom as Hom
from sage.functions.all import arccosh as arccosh
from sage.functions.other import imag as imag, real as real
from sage.geometry.hyperbolic_space.hyperbolic_coercion import CoercionHMtoKM as CoercionHMtoKM, CoercionHMtoPD as CoercionHMtoPD, CoercionHMtoUHP as CoercionHMtoUHP, CoercionKMtoHM as CoercionKMtoHM, CoercionKMtoPD as CoercionKMtoPD, CoercionKMtoUHP as CoercionKMtoUHP, CoercionPDtoHM as CoercionPDtoHM, CoercionPDtoKM as CoercionPDtoKM, CoercionPDtoUHP as CoercionPDtoUHP, CoercionUHPtoHM as CoercionUHPtoHM, CoercionUHPtoKM as CoercionUHPtoKM, CoercionUHPtoPD as CoercionUHPtoPD
from sage.geometry.hyperbolic_space.hyperbolic_constants import EPSILON as EPSILON, LORENTZ_GRAM as LORENTZ_GRAM
from sage.geometry.hyperbolic_space.hyperbolic_geodesic import HyperbolicGeodesic as HyperbolicGeodesic, HyperbolicGeodesicHM as HyperbolicGeodesicHM, HyperbolicGeodesicKM as HyperbolicGeodesicKM, HyperbolicGeodesicPD as HyperbolicGeodesicPD, HyperbolicGeodesicUHP as HyperbolicGeodesicUHP
from sage.geometry.hyperbolic_space.hyperbolic_isometry import HyperbolicIsometry as HyperbolicIsometry, HyperbolicIsometryKM as HyperbolicIsometryKM, HyperbolicIsometryPD as HyperbolicIsometryPD, HyperbolicIsometryUHP as HyperbolicIsometryUHP, moebius_transform as moebius_transform
from sage.geometry.hyperbolic_space.hyperbolic_point import HyperbolicPoint as HyperbolicPoint, HyperbolicPointUHP as HyperbolicPointUHP
from sage.matrix.constructor import matrix as matrix
from sage.misc.bindable_class import BindableClass as BindableClass
from sage.misc.functional import sqrt as sqrt
from sage.misc.lazy_import import lazy_import as lazy_import
from sage.rings.cc import CC as CC
from sage.rings.infinity import infinity as infinity
from sage.rings.real_double import RDF as RDF
from sage.rings.real_mpfr import RR as RR
from sage.structure.parent import Parent as Parent
from sage.structure.unique_representation import UniqueRepresentation as UniqueRepresentation
from sage.symbolic.constants import I as I

class HyperbolicModel(Parent, UniqueRepresentation, BindableClass):
    """
    Abstract base class for hyperbolic models.
    """
    Element = HyperbolicPoint
    def __init__(self, space, name, short_name, bounded, conformal, dimension, isometry_group, isometry_group_is_projective) -> None:
        """
        Initialize ``self``.

        EXAMPLES::

            sage: UHP = HyperbolicPlane().UHP()
            sage: TestSuite(UHP).run()
            sage: PD = HyperbolicPlane().PD()
            sage: TestSuite(PD).run()
            sage: KM = HyperbolicPlane().KM()
            sage: TestSuite(KM).run()
            sage: HM = HyperbolicPlane().HM()
            sage: TestSuite(HM).run()
        """
    def name(self):
        """
        Return the name of this model.

        EXAMPLES::

            sage: UHP = HyperbolicPlane().UHP()
            sage: UHP.name()
            'Upper Half Plane Model'
        """
    def short_name(self):
        """
        Return the short name of this model.

        EXAMPLES::

            sage: UHP = HyperbolicPlane().UHP()
            sage: UHP.short_name()
            'UHP'
        """
    def is_bounded(self):
        """
        Return ``True`` if ``self`` is a bounded model.

        EXAMPLES::

            sage: HyperbolicPlane().UHP().is_bounded()
            True
            sage: HyperbolicPlane().PD().is_bounded()
            True
            sage: HyperbolicPlane().KM().is_bounded()
            True
            sage: HyperbolicPlane().HM().is_bounded()
            False
        """
    def is_conformal(self):
        """
        Return ``True`` if ``self`` is a conformal model.

        EXAMPLES::

            sage: UHP = HyperbolicPlane().UHP()
            sage: UHP.is_conformal()
            True
        """
    def is_isometry_group_projective(self):
        """
        Return ``True`` if the isometry group of ``self`` is projective.

        EXAMPLES::

            sage: UHP = HyperbolicPlane().UHP()
            sage: UHP.is_isometry_group_projective()
            True
        """
    def point_in_model(self, p):
        """
        Return ``True`` if the point ``p`` is in the interior of the
        given model and ``False`` otherwise.

        INPUT:

        - any object that can converted into a complex number

        OUTPUT: boolean

        EXAMPLES::

            sage: HyperbolicPlane().UHP().point_in_model(I)
            True
            sage: HyperbolicPlane().UHP().point_in_model(-I)
            False
        """
    def point_test(self, p) -> None:
        """
        Test whether a point is in the model.  If the point is in the
        model, do nothing.  Otherwise, raise a :exc:`ValueError`.

        EXAMPLES::

            sage: from sage.geometry.hyperbolic_space.hyperbolic_model import HyperbolicModelUHP
            sage: HyperbolicPlane().UHP().point_test(2 + I)
            sage: HyperbolicPlane().UHP().point_test(2 - I)
            Traceback (most recent call last):
            ...
            ValueError: -I + 2 is not a valid point in the UHP model
        """
    def boundary_point_in_model(self, p):
        """
        Return ``True`` if the point is on the ideal boundary of hyperbolic
        space and ``False`` otherwise.

        INPUT:

        - any object that can converted into a complex number

        OUTPUT: boolean

        EXAMPLES::

            sage: HyperbolicPlane().UHP().boundary_point_in_model(I)
            False
        """
    def bdry_point_test(self, p) -> None:
        """
        Test whether a point is in the model.  If the point is in the
        model, do nothing; otherwise raise a :exc:`ValueError`.

        EXAMPLES::

            sage: HyperbolicPlane().UHP().bdry_point_test(2)
            sage: HyperbolicPlane().UHP().bdry_point_test(1 + I)
            Traceback (most recent call last):
            ...
            ValueError: I + 1 is not a valid boundary point in the UHP model
        """
    def isometry_in_model(self, A):
        """
        Return ``True`` if the input matrix represents an isometry of the
        given model and ``False`` otherwise.

        INPUT:

        - ``A`` -- a matrix that represents an isometry in the appropriate model

        OUTPUT: boolean

        EXAMPLES::

            sage: HyperbolicPlane().UHP().isometry_in_model(identity_matrix(2))
            True

            sage: HyperbolicPlane().UHP().isometry_in_model(identity_matrix(3))
            False
        """
    def isometry_test(self, A) -> None:
        """
        Test whether an isometry ``A`` is in the model.

        If the isometry is in the model, do nothing. Otherwise, raise
        a :exc:`ValueError`.

        EXAMPLES::

            sage: HyperbolicPlane().UHP().isometry_test(identity_matrix(2))
            sage: HyperbolicPlane().UHP().isometry_test(matrix(2, [I,1,2,1]))
            Traceback (most recent call last):
            ...
            ValueError:
            [I 1]
            [2 1] is not a valid isometry in the UHP model
        """
    def get_point(self, coordinates, is_boundary=None, **graphics_options):
        """
        Return a point in ``self``.

        Automatically determine the type of point to return given either:

        #. the coordinates of a point in the interior or ideal boundary
           of hyperbolic space, or
        #. a :class:`~sage.geometry.hyperbolic_space.hyperbolic_point.HyperbolicPoint` object.

        INPUT:

        - a point in hyperbolic space or on the ideal boundary

        OUTPUT: a :class:`~sage.geometry.hyperbolic_space.hyperbolic_point.HyperbolicPoint`

        EXAMPLES:

        We can create an interior point via the coordinates::

            sage: HyperbolicPlane().UHP().get_point(2*I)
            Point in UHP 2*I

        Or we can create a boundary point via the coordinates::

            sage: HyperbolicPlane().UHP().get_point(23)
            Boundary point in UHP 23

        However we cannot create points outside of our model::

            sage: HyperbolicPlane().UHP().get_point(12 - I)
            Traceback (most recent call last):
            ...
            ValueError: -I + 12 is not a valid point in the UHP model

        ::

            sage: HyperbolicPlane().UHP().get_point(2 + 3*I)
            Point in UHP 3*I + 2

            sage: HyperbolicPlane().PD().get_point(0)
            Point in PD 0

            sage: HyperbolicPlane().KM().get_point((0,0))
            Point in KM (0, 0)

            sage: HyperbolicPlane().HM().get_point((0,0,1))
            Point in HM (0, 0, 1)

            sage: p = HyperbolicPlane().UHP().get_point(I, color='red')
            sage: p.graphics_options()
            {'color': 'red'}

        ::

            sage: HyperbolicPlane().UHP().get_point(12)
            Boundary point in UHP 12

            sage: HyperbolicPlane().UHP().get_point(infinity)
            Boundary point in UHP +Infinity

            sage: HyperbolicPlane().PD().get_point(I)
            Boundary point in PD I

            sage: HyperbolicPlane().KM().get_point((0,-1))
            Boundary point in KM (0, -1)
        """
    def get_geodesic(self, start, end=None, **graphics_options):
        """
        Return a geodesic in the appropriate model.

        EXAMPLES::

            sage: HyperbolicPlane().UHP().get_geodesic(I, 2*I)
            Geodesic in UHP from I to 2*I

            sage: HyperbolicPlane().PD().get_geodesic(0, I/2)
            Geodesic in PD from 0 to 1/2*I

            sage: HyperbolicPlane().KM().get_geodesic((1/2, 1/2), (0,0))
            Geodesic in KM from (1/2, 1/2) to (0, 0)

            sage: HyperbolicPlane().HM().get_geodesic((0,0,1), (1,0, sqrt(2)))
            Geodesic in HM from (0, 0, 1) to (1, 0, sqrt(2))

        TESTS::

            sage: UHP = HyperbolicPlane().UHP()
            sage: g = UHP.get_geodesic(UHP.get_point(I), UHP.get_point(2 + I))
            sage: h = UHP.get_geodesic(I, 2 + I)
            sage: g == h
            True
        """
    def get_isometry(self, A):
        """
        Return an isometry in ``self`` from the matrix ``A`` in the
        isometry group of ``self``.

        EXAMPLES::

            sage: HyperbolicPlane().UHP().get_isometry(identity_matrix(2))
            Isometry in UHP
            [1 0]
            [0 1]

            sage: HyperbolicPlane().PD().get_isometry(identity_matrix(2))
            Isometry in PD
            [1 0]
            [0 1]

            sage: HyperbolicPlane().KM().get_isometry(identity_matrix(3))               # needs scipy
            Isometry in KM
            [1 0 0]
            [0 1 0]
            [0 0 1]

            sage: HyperbolicPlane().HM().get_isometry(identity_matrix(3))               # needs scipy
            Isometry in HM
            [1 0 0]
            [0 1 0]
            [0 0 1]
        """
    def random_element(self, **kwargs):
        """
        Return a random point in ``self``.

        The points are uniformly distributed over the rectangle
        `[-10, 10] \\times [0, 10 i]` in the upper half plane model.

        EXAMPLES::

            sage: p = HyperbolicPlane().UHP().random_element()
            sage: bool((p.coordinates().imag()) > 0)
            True

            sage: p = HyperbolicPlane().PD().random_element()
            sage: HyperbolicPlane().PD().point_in_model(p.coordinates())
            True

            sage: p = HyperbolicPlane().KM().random_element()
            sage: HyperbolicPlane().KM().point_in_model(p.coordinates())
            True

            sage: p = HyperbolicPlane().HM().random_element().coordinates()
            sage: bool((p[0]**2 + p[1]**2 - p[2]**2 - 1) < 10**-8)
            True
        """
    def random_point(self, **kwargs):
        """
        Return a random point of ``self``.

        The points are uniformly distributed over the rectangle
        `[-10, 10] \\times [0, 10 i]` in the upper half plane model.

        EXAMPLES::

            sage: p = HyperbolicPlane().UHP().random_point()
            sage: bool((p.coordinates().imag()) > 0)
            True

            sage: PD = HyperbolicPlane().PD()
            sage: p = PD.random_point()
            sage: PD.point_in_model(p.coordinates())
            True
        """
    def random_geodesic(self, **kwargs):
        """
        Return a random hyperbolic geodesic.

        Return the geodesic between two random points.

        EXAMPLES::

            sage: h = HyperbolicPlane().PD().random_geodesic()
            sage: all( e.coordinates().abs() <= 1 for e in h.endpoints() )
            True
        """
    def random_isometry(self, preserve_orientation: bool = True, **kwargs):
        """
        Return a random isometry in the model of ``self``.

        INPUT:

        - ``preserve_orientation`` -- if ``True`` return an
          orientation-preserving isometry

        OUTPUT: a hyperbolic isometry

        EXAMPLES::

            sage: # needs scipy
            sage: A = HyperbolicPlane().PD().random_isometry()
            sage: A.preserves_orientation()
            True
            sage: B = HyperbolicPlane().PD().random_isometry(preserve_orientation=False)
            sage: B.preserves_orientation()
            False
        """
    def dist(self, a, b):
        """
        Calculate the hyperbolic distance between ``a`` and ``b``.

        INPUT:

        - ``a``, ``b`` -- a point or geodesic

        OUTPUT: the hyperbolic distance

        EXAMPLES::

            sage: UHP = HyperbolicPlane().UHP()
            sage: p1 = UHP.get_point(5 + 7*I)
            sage: p2 = UHP.get_point(1.0 + I)
            sage: UHP.dist(p1, p2)
            2.23230104635820

            sage: PD = HyperbolicPlane().PD()
            sage: p1 = PD.get_point(0)
            sage: p2 = PD.get_point(I/2)
            sage: PD.dist(p1, p2)
            arccosh(5/3)

            sage: UHP(p1).dist(UHP(p2))
            arccosh(5/3)

            sage: KM = HyperbolicPlane().KM()
            sage: p1 = KM.get_point((0, 0))
            sage: p2 = KM.get_point((1/2, 1/2))
            sage: numerical_approx(KM.dist(p1, p2))
            0.881373587019543

            sage: HM = HyperbolicPlane().HM()
            sage: p1 = HM.get_point((0,0,1))
            sage: p2 = HM.get_point((1,0,sqrt(2)))
            sage: numerical_approx(HM.dist(p1, p2))
            0.881373587019543

        Distance between a point and itself is 0::

            sage: p = UHP.get_point(47 + I)
            sage: UHP.dist(p, p)
            0

        Points on the boundary are infinitely far from interior points::

            sage: UHP.get_point(3).dist(UHP.get_point(I))
            +Infinity

        TESTS::

            sage: UHP.dist(UHP.get_point(I), UHP.get_point(2*I))
            arccosh(5/4)
            sage: UHP.dist(I, 2*I)
            arccosh(5/4)
        """
    def isometry_from_fixed_points(self, repel, attract):
        """
        Given two fixed points ``repel`` and ``attract`` as hyperbolic
        points return a hyperbolic isometry with ``repel`` as repelling
        fixed point and ``attract`` as attracting fixed point.

        EXAMPLES::

            sage: UHP = HyperbolicPlane().UHP()
            sage: PD = HyperbolicPlane().PD()
            sage: PD.isometry_from_fixed_points(-i, i)
            Isometry in PD
            [   3/4  1/4*I]
            [-1/4*I    3/4]

        ::

            sage: p, q = PD.get_point(1/2 + I/2), PD.get_point(6/13 + 9/13*I)
            sage: PD.isometry_from_fixed_points(p, q)
            Traceback (most recent call last):
            ...
            ValueError: fixed points of hyperbolic elements must be ideal

            sage: p, q = PD.get_point(4/5 + 3/5*I), PD.get_point(-I)
            sage: PD.isometry_from_fixed_points(p, q)
            Isometry in PD
            [ 1/6*I - 2/3 -1/3*I - 1/6]
            [ 1/3*I - 1/6 -1/6*I - 2/3]
        """

class HyperbolicModelUHP(HyperbolicModel):
    """
    Upper Half Plane model.
    """
    Element = HyperbolicPointUHP
    def __init__(self, space) -> None:
        """
        Initialize ``self``.

        EXAMPLES::

            sage: UHP = HyperbolicPlane().UHP()
            sage: TestSuite(UHP).run()
        """
    def point_in_model(self, p):
        """
        Check whether a complex number lies in the open upper half plane.

        EXAMPLES::

            sage: UHP = HyperbolicPlane().UHP()
            sage: UHP.point_in_model(1 + I)
            True
            sage: UHP.point_in_model(infinity)
            False
            sage: UHP.point_in_model(CC(infinity))
            False
            sage: UHP.point_in_model(RR(infinity))
            False
            sage: UHP.point_in_model(1)
            False
            sage: UHP.point_in_model(12)
            False
            sage: UHP.point_in_model(1 - I)
            False
            sage: UHP.point_in_model(-2*I)
            False
            sage: UHP.point_in_model(I)
            True
            sage: UHP.point_in_model(0) # Not interior point
            False
        """
    def boundary_point_in_model(self, p):
        """
        Check whether a complex number is a real number or ``\\infty``.
        In the ``UHP.model_name_name``, this is the ideal boundary of
        hyperbolic space.

        EXAMPLES::

            sage: UHP = HyperbolicPlane().UHP()
            sage: UHP.boundary_point_in_model(1 + I)
            False
            sage: UHP.boundary_point_in_model(infinity)
            True
            sage: UHP.boundary_point_in_model(CC(infinity))
            True
            sage: UHP.boundary_point_in_model(RR(infinity))
            True
            sage: UHP.boundary_point_in_model(1)
            True
            sage: UHP.boundary_point_in_model(12)
            True
            sage: UHP.boundary_point_in_model(1 - I)
            False
            sage: UHP.boundary_point_in_model(-2*I)
            False
            sage: UHP.boundary_point_in_model(0)
            True
            sage: UHP.boundary_point_in_model(I)
            False
        """
    def isometry_in_model(self, A):
        """
        Check that ``A`` acts as an isometry on the upper half plane.
        That is, ``A`` must be an invertible `2 \\times 2` matrix with real
        entries.

        EXAMPLES::

            sage: UHP = HyperbolicPlane().UHP()
            sage: A = matrix(2,[1,2,3,4])
            sage: UHP.isometry_in_model(A)
            True
            sage: B = matrix(2,[I,2,4,1])
            sage: UHP.isometry_in_model(B)
            False

        An example of a matrix `A` such that `\\det(A) \\neq 1`, but the `A`
        acts isometrically::

            sage: C = matrix(2,[10,0,0,10])
            sage: UHP.isometry_in_model(C)
            True
        """
    def get_background_graphic(self, **bdry_options):
        """
        Return a graphic object that makes the model easier to visualize.
        For the upper half space, the background object is the ideal boundary.

        EXAMPLES::

            sage: hp = HyperbolicPlane().UHP().get_background_graphic()                 # needs sage.plot
        """
    def random_point(self, **kwargs):
        """
        Return a random point in the upper half plane. The points are
        uniformly distributed over the rectangle `[-10, 10] \\times [0, 10i]`.

        EXAMPLES::

            sage: p = HyperbolicPlane().UHP().random_point().coordinates()
            sage: bool((p.imag()) > 0)
            True
        """
    def isometry_from_fixed_points(self, repel, attract):
        """
        Given two fixed points ``repel`` and ``attract`` as complex
        numbers return a hyperbolic isometry with ``repel`` as repelling
        fixed point and ``attract`` as attracting fixed point.

        EXAMPLES::

            sage: UHP = HyperbolicPlane().UHP()
            sage: UHP.isometry_from_fixed_points(2 + I, 3 + I)
            Traceback (most recent call last):
            ...
            ValueError: fixed points of hyperbolic elements must be ideal

            sage: UHP.isometry_from_fixed_points(2, 0)
            Isometry in UHP
            [  -1    0]
            [-1/3 -1/3]

        TESTS::

            sage: UHP = HyperbolicPlane().UHP()
            sage: UHP.isometry_from_fixed_points(0, 4)
            Isometry in UHP
            [  -1    0]
            [-1/5 -1/5]
            sage: UHP.isometry_from_fixed_points(UHP.get_point(0), UHP.get_point(4))
            Isometry in UHP
            [  -1    0]
            [-1/5 -1/5]
        """
    def random_isometry(self, preserve_orientation: bool = True, **kwargs):
        """
        Return a random isometry in the Upper Half Plane model.

        INPUT:

        - ``preserve_orientation`` -- if ``True`` return an
          orientation-preserving isometry

        OUTPUT: a hyperbolic isometry

        EXAMPLES::

            sage: A = HyperbolicPlane().UHP().random_isometry()                         # needs scipy
            sage: B = HyperbolicPlane().UHP().random_isometry(preserve_orientation=False)           # needs scipy
            sage: B.preserves_orientation()                                             # needs scipy
            False
        """

class HyperbolicModelPD(HyperbolicModel):
    """
    Poincaré Disk Model.
    """
    def __init__(self, space) -> None:
        """
        Initialize ``self``.

        EXAMPLES::

            sage: PD = HyperbolicPlane().PD()
            sage: TestSuite(PD).run()
        """
    def point_in_model(self, p):
        """
        Check whether a complex number lies in the open unit disk.

        EXAMPLES::

            sage: PD = HyperbolicPlane().PD()
            sage: PD.point_in_model(1.00)
            False
            sage: PD.point_in_model(1/2 + I/2)
            True
            sage: PD.point_in_model(1 + .2*I)
            False
        """
    def boundary_point_in_model(self, p):
        """
        Check whether a complex number lies in the open unit disk.

        EXAMPLES::

            sage: PD = HyperbolicPlane().PD()
            sage: PD.boundary_point_in_model(1.00)
            True
            sage: PD.boundary_point_in_model(1/2 + I/2)
            False
            sage: PD.boundary_point_in_model(1 + .2*I)
            False
        """
    def isometry_in_model(self, A):
        """
        Check if the given matrix ``A`` is in the group `U(1,1)`.

        EXAMPLES::

            sage: z = [CC.random_element() for k in range(2)]; z.sort(key=abs)
            sage: A = matrix(2,[z[1], z[0],z[0].conjugate(),z[1].conjugate()])
            sage: HyperbolicPlane().PD().isometry_in_model(A)
            True
        """
    def get_background_graphic(self, **bdry_options):
        """
        Return a graphic object that makes the model easier to visualize.

        For the Poincaré disk, the background object is the ideal boundary.

        EXAMPLES::

            sage: circ = HyperbolicPlane().PD().get_background_graphic()                # needs sage.plot
        """

class HyperbolicModelKM(HyperbolicModel):
    """
    Klein Model.
    """
    def __init__(self, space) -> None:
        """
        Initialize ``self``.

        EXAMPLES::

            sage: KM = HyperbolicPlane().KM()
            sage: TestSuite(KM).run()
        """
    def point_in_model(self, p):
        """
        Check whether a point lies in the open unit disk.

        EXAMPLES::

            sage: KM = HyperbolicPlane().KM()
            sage: KM.point_in_model((1, 0))
            False
            sage: KM.point_in_model((1/2, 1/2))
            True
            sage: KM.point_in_model((1, .2))
            False
        """
    def boundary_point_in_model(self, p):
        """
        Check whether a point lies in the unit circle, which corresponds
        to the ideal boundary of the hyperbolic plane in the Klein model.

        EXAMPLES::

            sage: KM = HyperbolicPlane().KM()
            sage: KM.boundary_point_in_model((1, 0))
            True
            sage: KM.boundary_point_in_model((1/2, 1/2))
            False
            sage: KM.boundary_point_in_model((1, .2))
            False
        """
    def isometry_in_model(self, A):
        """
        Check if the given matrix ``A`` is in the group `SO(2,1)`.

        EXAMPLES::

            sage: A = matrix(3, [[1, 0, 0], [0, 17/8, 15/8], [0, 15/8, 17/8]])
            sage: HyperbolicPlane().KM().isometry_in_model(A)                           # needs scipy
            True
        """
    def get_background_graphic(self, **bdry_options):
        """
        Return a graphic object that makes the model easier to visualize.

        For the Klein model, the background object is the ideal boundary.

        EXAMPLES::

            sage: circ = HyperbolicPlane().KM().get_background_graphic()                # needs sage.plot
        """

class HyperbolicModelHM(HyperbolicModel):
    """
    Hyperboloid Model.
    """
    def __init__(self, space) -> None:
        """
        Initialize ``self``.

        EXAMPLES::

            sage: HM = HyperbolicPlane().HM()
            sage: TestSuite(HM).run()
        """
    def point_in_model(self, p):
        """
        Check whether a complex number lies in the hyperboloid.

        EXAMPLES::

            sage: HM = HyperbolicPlane().HM()
            sage: HM.point_in_model((0,0,1))
            True
            sage: HM.point_in_model((1,0,sqrt(2)))
            True
            sage: HM.point_in_model((1,2,1))
            False
        """
    def boundary_point_in_model(self, p):
        """
        Return ``False`` since the Hyperboloid model has no boundary points.

        EXAMPLES::

            sage: HM = HyperbolicPlane().HM()
            sage: HM.boundary_point_in_model((0,0,1))
            False
            sage: HM.boundary_point_in_model((1,0,sqrt(2)))
            False
            sage: HM.boundary_point_in_model((1,2,1))
            False
        """
    def isometry_in_model(self, A):
        """
        Test that the matrix ``A`` is in the group `SO(2,1)^+`.

        EXAMPLES::

           sage: A = diagonal_matrix([1,1,-1])
           sage: HyperbolicPlane().HM().isometry_in_model(A)                            # needs scipy
           True
        """
    def get_background_graphic(self, **bdry_options):
        """
        Return a graphic object that makes the model easier to visualize.
        For the hyperboloid model, the background object is the hyperboloid
        itself.

        EXAMPLES::

            sage: H = HyperbolicPlane().HM().get_background_graphic()                   # needs sage.plot
        """
