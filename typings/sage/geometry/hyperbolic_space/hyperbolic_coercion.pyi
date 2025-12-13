from sage.categories.morphism import Morphism as Morphism
from sage.functions.other import imag as imag, real as real
from sage.geometry.hyperbolic_space.hyperbolic_constants import EPSILON as EPSILON
from sage.matrix.constructor import matrix as matrix
from sage.misc.functional import sqrt as sqrt
from sage.misc.lazy_import import lazy_import as lazy_import
from sage.modules.free_module_element import vector as vector
from sage.rings.infinity import infinity as infinity
from sage.rings.integer import Integer as Integer
from sage.symbolic.constants import I as I

class HyperbolicModelCoercion(Morphism):
    """
    Abstract base class for morphisms between the hyperbolic models.
    """
    def convert_geodesic(self, x):
        """
        Convert the geodesic ``x`` of the domain into a geodesic of
        the codomain.

        EXAMPLES::

            sage: UHP = HyperbolicPlane().UHP()
            sage: PD = HyperbolicPlane().PD()
            sage: phi = UHP.coerce_map_from(PD)
            sage: phi.convert_geodesic(PD.get_geodesic(0.5+0.5*I, -I))
            Geodesic in UHP from 2.00000000000000 + 1.00000000000000*I to 0
        """
    def convert_isometry(self, x):
        """
        Convert the hyperbolic isometry ``x`` of the domain into an
        isometry of the codomain.

        EXAMPLES::

            sage: UHP = HyperbolicPlane().UHP()
            sage: HM = HyperbolicPlane().HM()
            sage: phi = HM.coerce_map_from(UHP)
            sage: I2 = UHP.get_isometry(identity_matrix(2))
            sage: phi.convert_isometry(I2)
            Isometry in HM
            [1 0 0]
            [0 1 0]
            [0 0 1]
        """
    def __invert__(self):
        """
        Return the inverse coercion of ``self``.

        EXAMPLES::

            sage: UHP = HyperbolicPlane().UHP()
            sage: PD = HyperbolicPlane().PD()
            sage: phi = UHP.coerce_map_from(PD)
            sage: ~phi
            Coercion Isometry morphism:
              From: Hyperbolic plane in the Upper Half Plane Model
              To:   Hyperbolic plane in the Poincare Disk Model
        """

class CoercionUHPtoPD(HyperbolicModelCoercion):
    """
    Coercion from the UHP to PD model.
    """
    def image_coordinates(self, x):
        """
        Return the image of the coordinates of the hyperbolic point ``x``
        under ``self``.

        EXAMPLES::

            sage: UHP = HyperbolicPlane().UHP()
            sage: PD = HyperbolicPlane().PD()
            sage: phi = PD.coerce_map_from(UHP)
            sage: phi.image_coordinates(I)
            0
        """
    def image_isometry_matrix(self, x):
        """
        Return the image of the matrix of the hyperbolic isometry ``x``
        under ``self``.

        EXAMPLES::

            sage: UHP = HyperbolicPlane().UHP()
            sage: PD = HyperbolicPlane().PD()
            sage: phi = PD.coerce_map_from(UHP)
            sage: phi.image_isometry_matrix(identity_matrix(2))
            [1 0]
            [0 1]
        """

class CoercionUHPtoKM(HyperbolicModelCoercion):
    """
    Coercion from the UHP to KM model.
    """
    def image_coordinates(self, x):
        """
        Return the image of the coordinates of the hyperbolic point ``x``
        under ``self``.

        EXAMPLES::

            sage: UHP = HyperbolicPlane().UHP()
            sage: KM = HyperbolicPlane().KM()
            sage: phi = KM.coerce_map_from(UHP)
            sage: phi.image_coordinates(3 + I)
            (6/11, 9/11)
        """
    def image_isometry_matrix(self, x):
        """
        Return the image of the matrix of the hyperbolic isometry ``x``
        under ``self``.

        EXAMPLES::

            sage: UHP = HyperbolicPlane().UHP()
            sage: KM = HyperbolicPlane().KM()
            sage: phi = KM.coerce_map_from(UHP)
            sage: phi.image_isometry_matrix(identity_matrix(2))
            [1 0 0]
            [0 1 0]
            [0 0 1]
        """

class CoercionUHPtoHM(HyperbolicModelCoercion):
    """
    Coercion from the UHP to HM model.
    """
    def image_coordinates(self, x):
        """
        Return the image of the coordinates of the hyperbolic point ``x``
        under ``self``.

        EXAMPLES::

            sage: UHP = HyperbolicPlane().UHP()
            sage: HM = HyperbolicPlane().HM()
            sage: phi = HM.coerce_map_from(UHP)
            sage: phi.image_coordinates(3 + I)
            (3, 9/2, 11/2)
        """
    def image_isometry_matrix(self, x):
        """
        Return the image of the matrix of the hyperbolic isometry ``x``
        under ``self``.

        EXAMPLES::

            sage: UHP = HyperbolicPlane().UHP()
            sage: HM = HyperbolicPlane().HM()
            sage: phi = HM.coerce_map_from(UHP)
            sage: phi.image_isometry_matrix(identity_matrix(2))
            [1 0 0]
            [0 1 0]
            [0 0 1]
        """

class CoercionPDtoUHP(HyperbolicModelCoercion):
    """
    Coercion from the PD to UHP model.
    """
    def image_coordinates(self, x):
        """
        Return the image of the coordinates of the hyperbolic point ``x``
        under ``self``.

        EXAMPLES::

            sage: PD = HyperbolicPlane().PD()
            sage: UHP = HyperbolicPlane().UHP()
            sage: phi = UHP.coerce_map_from(PD)
            sage: phi.image_coordinates(0.5+0.5*I)
            2.00000000000000 + 1.00000000000000*I
            sage: phi.image_coordinates(0)
            I
            sage: phi.image_coordinates(I)
            +Infinity
            sage: phi.image_coordinates(-I)
            0

        TESTS:

        Check that the second bug discussed in :issue:`32362` is fixed::

            sage: PD = HyperbolicPlane().PD()
            sage: UHP = HyperbolicPlane().UHP()
            sage: r = exp((pi*I/2).n())
            sage: p = PD.get_point(r)
            sage: UHP(p)
            Boundary point in UHP +Infinity
        """
    def image_isometry_matrix(self, x):
        """
        Return the image of the matrix of the hyperbolic isometry ``x``
        under ``self``.

        EXAMPLES:

        We check that orientation-reversing isometries behave as they
        should::

            sage: PD = HyperbolicPlane().PD()
            sage: UHP = HyperbolicPlane().UHP()
            sage: phi = UHP.coerce_map_from(PD)
            sage: phi.image_isometry_matrix(matrix([[0,I],[I,0]]))
            [-1  0]
            [ 0 -1]
        """

class CoercionPDtoKM(HyperbolicModelCoercion):
    """
    Coercion from the PD to KM model.
    """
    def image_coordinates(self, x):
        """
        Return the image of the coordinates of the hyperbolic point ``x``
        under ``self``.

        EXAMPLES::

            sage: PD = HyperbolicPlane().PD()
            sage: KM = HyperbolicPlane().KM()
            sage: phi = KM.coerce_map_from(PD)
            sage: phi.image_coordinates(0.5+0.5*I)
            (0.666666666666667, 0.666666666666667)
        """
    def image_isometry_matrix(self, x):
        """
        Return the image of the matrix of the hyperbolic isometry ``x``
        under ``self``.

        EXAMPLES::

            sage: PD = HyperbolicPlane().PD()
            sage: KM = HyperbolicPlane().KM()
            sage: phi = KM.coerce_map_from(PD)
            sage: phi.image_isometry_matrix(matrix([[0,I],[I,0]]))
            [-1  0  0]
            [ 0  1  0]
            [ 0  0 -1]
        """

class CoercionPDtoHM(HyperbolicModelCoercion):
    """
    Coercion from the PD to HM model.
    """
    def image_coordinates(self, x):
        """
        Return the image of the coordinates of the hyperbolic point ``x``
        under ``self``.

        EXAMPLES::

            sage: PD = HyperbolicPlane().PD()
            sage: HM = HyperbolicPlane().HM()
            sage: phi = HM.coerce_map_from(PD)
            sage: phi.image_coordinates(0.5+0.5*I)
            (2.00000000000000, 2.00000000000000, 3.00000000000000)
        """
    def image_isometry_matrix(self, x):
        """
        Return the image of the matrix of the hyperbolic isometry ``x``
        under ``self``.

        EXAMPLES::

            sage: PD = HyperbolicPlane().PD()
            sage: HM = HyperbolicPlane().HM()
            sage: phi = HM.coerce_map_from(PD)
            sage: phi.image_isometry_matrix(matrix([[0,I],[I,0]]))
            [-1  0  0]
            [ 0  1  0]
            [ 0  0 -1]
        """

class CoercionKMtoUHP(HyperbolicModelCoercion):
    """
    Coercion from the KM to UHP model.
    """
    def image_coordinates(self, x):
        """
        Return the image of the coordinates of the hyperbolic point ``x``
        under ``self``.

        EXAMPLES::

            sage: KM = HyperbolicPlane().KM()
            sage: UHP = HyperbolicPlane().UHP()
            sage: phi = UHP.coerce_map_from(KM)
            sage: phi.image_coordinates((0, 0))
            I
            sage: phi.image_coordinates((0, 1))
            +Infinity
        """
    def image_isometry_matrix(self, x):
        """
        Return the image of the matrix of the hyperbolic isometry ``x``
        under ``self``.

        EXAMPLES::

            sage: KM = HyperbolicPlane().KM()
            sage: UHP = HyperbolicPlane().UHP()
            sage: phi = UHP.coerce_map_from(KM)
            sage: m = matrix([[5/3,0,4/3], [0,1,0], [4/3,0,5/3]])
            sage: phi.image_isometry_matrix(m)
            [2*sqrt(1/3)   sqrt(1/3)]
            [  sqrt(1/3) 2*sqrt(1/3)]
        """

class CoercionKMtoPD(HyperbolicModelCoercion):
    """
    Coercion from the KM to PD model.
    """
    def image_coordinates(self, x):
        """
        Return the image of the coordinates of the hyperbolic point ``x``
        under ``self``.

        EXAMPLES::

            sage: KM = HyperbolicPlane().KM()
            sage: PD = HyperbolicPlane().PD()
            sage: phi = PD.coerce_map_from(KM)
            sage: phi.image_coordinates((0, 0))
            0
        """
    def image_isometry_matrix(self, x):
        """
        Return the image of the matrix of the hyperbolic isometry ``x``
        under ``self``.

        EXAMPLES::

            sage: KM = HyperbolicPlane().KM()
            sage: PD = HyperbolicPlane().PD()
            sage: phi = PD.coerce_map_from(KM)
            sage: m = matrix([[5/3,0,4/3], [0,1,0], [4/3,0,5/3]])
            sage: phi.image_isometry_matrix(m)
            [2*sqrt(1/3)   sqrt(1/3)]
            [  sqrt(1/3) 2*sqrt(1/3)]
        """

class CoercionKMtoHM(HyperbolicModelCoercion):
    """
    Coercion from the KM to HM model.
    """
    def image_coordinates(self, x):
        """
        Return the image of the coordinates of the hyperbolic point ``x``
        under ``self``.

        EXAMPLES::

            sage: KM = HyperbolicPlane().KM()
            sage: HM = HyperbolicPlane().HM()
            sage: phi = HM.coerce_map_from(KM)
            sage: phi.image_coordinates((0, 0))
            (0, 0, 1)
        """
    def image_isometry_matrix(self, x):
        """
        Return the image of the matrix of the hyperbolic isometry ``x``
        under ``self``.

        EXAMPLES::

            sage: KM = HyperbolicPlane().KM()
            sage: HM = HyperbolicPlane().HM()
            sage: phi = HM.coerce_map_from(KM)
            sage: m = matrix([[5/3,0,4/3], [0,1,0], [4/3,0,5/3]])
            sage: phi.image_isometry_matrix(m)
            [5/3   0 4/3]
            [  0   1   0]
            [4/3   0 5/3]
        """

class CoercionHMtoUHP(HyperbolicModelCoercion):
    """
    Coercion from the HM to UHP model.
    """
    def image_coordinates(self, x):
        """
        Return the image of the coordinates of the hyperbolic point ``x``
        under ``self``.

        EXAMPLES::

            sage: HM = HyperbolicPlane().HM()
            sage: UHP = HyperbolicPlane().UHP()
            sage: phi = UHP.coerce_map_from(HM)
            sage: phi.image_coordinates( vector((0,0,1)) )
            I
        """
    def image_isometry_matrix(self, x):
        """
        Return the image of the matrix of the hyperbolic isometry ``x``
        under ``self``.

        EXAMPLES::

            sage: HM = HyperbolicPlane().HM()
            sage: UHP = HyperbolicPlane().UHP()
            sage: phi = UHP.coerce_map_from(HM)
            sage: phi.image_isometry_matrix(identity_matrix(3))
            [1 0]
            [0 1]
        """

class CoercionHMtoPD(HyperbolicModelCoercion):
    """
    Coercion from the HM to PD model.
    """
    def image_coordinates(self, x):
        """
        Return the image of the coordinates of the hyperbolic point ``x``
        under ``self``.

        EXAMPLES::

            sage: HM = HyperbolicPlane().HM()
            sage: PD = HyperbolicPlane().PD()
            sage: phi = PD.coerce_map_from(HM)
            sage: phi.image_coordinates( vector((0,0,1)) )
            0
        """
    def image_isometry_matrix(self, x):
        """
        Return the image of the matrix of the hyperbolic isometry ``x``
        under ``self``.

        EXAMPLES::

            sage: HM = HyperbolicPlane().HM()
            sage: PD = HyperbolicPlane().PD()
            sage: phi = PD.coerce_map_from(HM)
            sage: phi.image_isometry_matrix(identity_matrix(3))
            [1 0]
            [0 1]
        """

class CoercionHMtoKM(HyperbolicModelCoercion):
    """
    Coercion from the HM to KM model.
    """
    def image_coordinates(self, x):
        """
        Return the image of the coordinates of the hyperbolic point ``x``
        under ``self``.

        EXAMPLES::

            sage: HM = HyperbolicPlane().HM()
            sage: KM = HyperbolicPlane().KM()
            sage: phi = KM.coerce_map_from(HM)
            sage: phi.image_coordinates( vector((0,0,1)) )
            (0, 0)
        """
    def image_isometry_matrix(self, x):
        """
        Return the image of the matrix of the hyperbolic isometry ``x``
        under ``self``.

        EXAMPLES::

            sage: HM = HyperbolicPlane().HM()
            sage: KM = HyperbolicPlane().KM()
            sage: phi = KM.coerce_map_from(HM)
            sage: phi.image_isometry_matrix(identity_matrix(3))
            [1 0 0]
            [0 1 0]
            [0 0 1]
        """

def SL2R_to_SO21(A):
    """
    Given a matrix in `SL(2, \\RR)` return its irreducible representation in
    `O(2,1)`.

    Note that this is not the only homomorphism, but it is the only one
    that works in the context of the implemented 2D hyperbolic geometry
    models.

    EXAMPLES::

        sage: from sage.geometry.hyperbolic_space.hyperbolic_coercion import SL2R_to_SO21
        sage: A = SL2R_to_SO21(identity_matrix(2))
        sage: J = matrix([[1,0,0],[0,1,0],[0,0,-1]]) #Lorentzian Gram matrix
        sage: norm(A.transpose()*J*A - J) < 10**-4                                      # needs scipy
        True
    """
def SO21_to_SL2R(M):
    """
    A homomorphism from `SO(2, 1)` to `SL(2, \\RR)`.

    Note that this is not the only homomorphism, but it is the only one
    that works in the context of the implemented 2D hyperbolic geometry
    models.

    EXAMPLES::

        sage: from sage.geometry.hyperbolic_space.hyperbolic_coercion import SO21_to_SL2R
        sage: (SO21_to_SL2R(identity_matrix(3)) - identity_matrix(2)).norm() < 10**-4   # needs scipy
        True
    """
