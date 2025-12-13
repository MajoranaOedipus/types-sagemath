from sage.categories.homset import Hom as Hom
from sage.categories.morphism import Morphism as Morphism
from sage.functions.all import arccosh as arccosh, sign as sign
from sage.functions.other import imag as imag
from sage.geometry.hyperbolic_space.hyperbolic_constants import EPSILON as EPSILON
from sage.geometry.hyperbolic_space.hyperbolic_geodesic import HyperbolicGeodesic as HyperbolicGeodesic
from sage.matrix.constructor import matrix as matrix
from sage.misc.functional import sqrt as sqrt
from sage.misc.latex import latex as latex
from sage.misc.lazy_attribute import lazy_attribute as lazy_attribute
from sage.modules.free_module_element import vector as vector
from sage.rings.infinity import infinity as infinity
from sage.rings.real_double import RDF as RDF

class HyperbolicIsometry(Morphism):
    """
    Abstract base class for hyperbolic isometries.  This class should
    never be instantiated.

    INPUT:

    - ``A`` -- a matrix representing a hyperbolic isometry in the
      appropriate model

    EXAMPLES::

        sage: HyperbolicPlane().HM().get_isometry(identity_matrix(3))
        Isometry in HM
        [1 0 0]
        [0 1 0]
        [0 0 1]
    """
    def __init__(self, model, A, check: bool = True) -> None:
        """
        See :class:`HyperbolicIsometry` for full documentation.

        EXAMPLES::

            sage: A = HyperbolicPlane().UHP().get_isometry(matrix(2, [0,1,-1,0]))
            sage: TestSuite(A).run(skip='_test_category')
        """
    def __eq__(self, other):
        """
        Return ``True`` if the isometries are the same and ``False`` otherwise.

        EXAMPLES::

            sage: UHP = HyperbolicPlane().UHP()
            sage: A = UHP.get_isometry(identity_matrix(2))
            sage: B = UHP.get_isometry(-identity_matrix(2))
            sage: A == B
            True

            sage: HM = HyperbolicPlane().HM()
            sage: A = HM.random_isometry()
            sage: A == A
            True
        """
    def __hash__(self):
        """
        Return the hash of ``self``.

        EXAMPLES::

            sage: UHP = HyperbolicPlane().UHP()
            sage: A = UHP.get_isometry(identity_matrix(2))
            sage: B = UHP.get_isometry(-identity_matrix(2))
            sage: hash(A) == hash(B)
            True

            sage: HM = HyperbolicPlane().HM()
            sage: A = HM.random_isometry()
            sage: hash(A) == hash(A)
            True
        """
    def __pow__(self, n):
        """
        EXAMPLES::

            sage: A = HyperbolicPlane().UHP().get_isometry(matrix(2,[3,1,2,1]))
            sage: A**3
            Isometry in UHP
            [41 15]
            [30 11]
        """
    def __mul__(self, other):
        """
        EXAMPLES::

            sage: UHP = HyperbolicPlane().UHP()
            sage: A = UHP.get_isometry(Matrix(2,[5,2,1,2]))
            sage: B = UHP.get_isometry(Matrix(2,[3,1,1,2]))
            sage: B * A
            Isometry in UHP
            [16  8]
            [ 7  6]
            sage: A = UHP.get_isometry(Matrix(2,[5,2,1,2]))
            sage: p = UHP.get_point(2 + I)
            sage: A * p
            Point in UHP 8/17*I + 53/17

            sage: g = UHP.get_geodesic(2 + I, 4 + I)
            sage: A * g
            Geodesic in UHP from 8/17*I + 53/17 to 8/37*I + 137/37

            sage: A = diagonal_matrix([1, -1, 1])
            sage: A = HyperbolicPlane().HM().get_isometry(A)
            sage: A.preserves_orientation()
            False
            sage: p = HyperbolicPlane().HM().get_point((0, 1, sqrt(2)))
            sage: A * p
            Point in HM (0, -1, sqrt(2))
        """
    def matrix(self):
        """
        Return the matrix of the isometry.

        .. NOTE::

            We do not allow the ``matrix`` constructor to work as these may
            be elements of a projective group (ex. `PSL(n, \\RR)`), so these
            isometries aren't true matrices.

        EXAMPLES::

            sage: UHP = HyperbolicPlane().UHP()
            sage: UHP.get_isometry(-identity_matrix(2)).matrix()
            [-1  0]
            [ 0 -1]
        """
    def __invert__(self):
        """
        Return the inverse of the isometry ``self``.

        EXAMPLES::

            sage: UHP = HyperbolicPlane().UHP()
            sage: A = UHP.get_isometry(matrix(2,[4,1,3,2]))
            sage: B = A.inverse()   # indirect doctest
            sage: A*B == UHP.get_isometry(identity_matrix(2))
            True
        """
    def is_identity(self):
        """
        Return ``True`` if ``self`` is the identity isometry.

        EXAMPLES::

            sage: UHP = HyperbolicPlane().UHP()
            sage: UHP.get_isometry(matrix(2,[4,1,3,2])).is_identity()
            False
            sage: UHP.get_isometry(identity_matrix(2)).is_identity()
            True
        """
    def model(self):
        """
        Return the model to which ``self`` belongs.

        EXAMPLES::

            sage: HyperbolicPlane().UHP().get_isometry(identity_matrix(2)).model()
            Hyperbolic plane in the Upper Half Plane Model

            sage: HyperbolicPlane().PD().get_isometry(identity_matrix(2)).model()
            Hyperbolic plane in the Poincare Disk Model

            sage: HyperbolicPlane().KM().get_isometry(identity_matrix(3)).model()
            Hyperbolic plane in the Klein Disk Model

            sage: HyperbolicPlane().HM().get_isometry(identity_matrix(3)).model()
            Hyperbolic plane in the Hyperboloid Model
        """
    def to_model(self, other):
        """
        Convert the current object to image in another model.

        INPUT:

        - ``other`` -- (a string representing) the image model

        EXAMPLES::

            sage: H = HyperbolicPlane()
            sage: UHP = H.UHP()
            sage: PD = H.PD()
            sage: KM = H.KM()
            sage: HM = H.HM()

            sage: A = UHP.get_isometry(identity_matrix(2))
            sage: A.to_model(HM)
            Isometry in HM
            [1 0 0]
            [0 1 0]
            [0 0 1]
            sage: A.to_model('HM')
            Isometry in HM
            [1 0 0]
            [0 1 0]
            [0 0 1]

            sage: A = PD.get_isometry(matrix([[I, 0], [0, -I]]))
            sage: A.to_model(UHP)
            Isometry in UHP
            [ 0  1]
            [-1  0]
            sage: A.to_model(HM)
            Isometry in HM
            [-1  0  0]
            [ 0 -1  0]
            [ 0  0  1]
            sage: A.to_model(KM)
            Isometry in KM
            [-1  0  0]
            [ 0 -1  0]
            [ 0  0  1]

            sage: A = HM.get_isometry(diagonal_matrix([-1, -1, 1]))
            sage: A.to_model('UHP')
            Isometry in UHP
            [ 0 -1]
            [ 1  0]
            sage: A.to_model('PD')
            Isometry in PD
            [-I  0]
            [ 0  I]
            sage: A.to_model('KM')
            Isometry in KM
            [-1  0  0]
            [ 0 -1  0]
            [ 0  0  1]
        """
    def preserves_orientation(self):
        """
        Return ``True`` if ``self`` is orientation-preserving and ``False``
        otherwise.

        EXAMPLES::

            sage: UHP = HyperbolicPlane().UHP()
            sage: A = UHP.get_isometry(identity_matrix(2))
            sage: A.preserves_orientation()
            True
            sage: B = UHP.get_isometry(matrix(2,[0,1,1,0]))
            sage: B.preserves_orientation()
            False
        """
    def classification(self):
        """
        Classify the hyperbolic isometry as elliptic, parabolic,
        hyperbolic or a reflection.

        A hyperbolic isometry fixes two points on the boundary of
        hyperbolic space, a parabolic isometry fixes one point on the
        boundary of hyperbolic space, and an elliptic isometry fixes no
        points.

        EXAMPLES::

            sage: UHP = HyperbolicPlane().UHP()
            sage: H = UHP.get_isometry(matrix(2,[2,0,0,1/2]))
            sage: H.classification()
            'hyperbolic'

            sage: P = UHP.get_isometry(matrix(2,[1,1,0,1]))
            sage: P.classification()
            'parabolic'

            sage: E = UHP.get_isometry(matrix(2,[-1,0,0,1]))
            sage: E.classification()
            'reflection'
        """
    def translation_length(self):
        """
        For hyperbolic elements, return the translation length;
        otherwise, raise a :exc:`ValueError`.

        EXAMPLES::

            sage: UHP = HyperbolicPlane().UHP()
            sage: H = UHP.get_isometry(matrix(2,[2,0,0,1/2]))
            sage: H.translation_length()
            2*arccosh(5/4)

        ::

            sage: f_1 = UHP.get_point(-1)
            sage: f_2 = UHP.get_point(1)
            sage: H = UHP.isometry_from_fixed_points(f_1, f_2)
            sage: p = UHP.get_point(exp(i*7*pi/8))
            sage: bool((p.dist(H*p) - H.translation_length()) < 10**-9)
            True
        """
    def axis(self):
        """
        For a hyperbolic isometry, return the axis of the
        transformation; otherwise raise a :exc:`ValueError`.

        EXAMPLES::

            sage: UHP = HyperbolicPlane().UHP()
            sage: H = UHP.get_isometry(matrix(2,[2,0,0,1/2]))
            sage: H.axis()
            Geodesic in UHP from 0 to +Infinity

        It is an error to call this function on an isometry that is
        not hyperbolic::

            sage: P = UHP.get_isometry(matrix(2,[1,4,0,1]))
            sage: P.axis()
            Traceback (most recent call last):
            ...
            ValueError: the isometry is not hyperbolic: axis is undefined
        """
    def fixed_point_set(self):
        """
        Return a list containing the fixed point set of
        orientation-preserving isometries.

        OUTPUT: list of hyperbolic points or a hyperbolic geodesic

        EXAMPLES::

            sage: KM = HyperbolicPlane().KM()
            sage: H = KM.get_isometry(matrix([[5/3,0,4/3], [0,1,0], [4/3,0,5/3]]))
            sage: g = H.fixed_point_set(); g
            Geodesic in KM from (1, 0) to (-1, 0)
            sage: H(g.start()) == g.start()
            True
            sage: H(g.end()) == g.end()
            True
            sage: A = KM.get_isometry(matrix([[1,0,0], [0,-1,0], [0,0,1]]))
            sage: A.preserves_orientation()
            False
            sage: A.fixed_point_set()
            Geodesic in KM from (1, 0) to (-1, 0)

        ::

            sage: B = KM.get_isometry(identity_matrix(3))
            sage: B.fixed_point_set()
            Traceback (most recent call last):
            ...
            ValueError: the identity transformation fixes the entire hyperbolic plane
        """
    def fixed_geodesic(self):
        """
        If ``self`` is a reflection in a geodesic, return that geodesic.

        EXAMPLES::

            sage: A = HyperbolicPlane().PD().get_isometry(matrix([[0, 1], [1, 0]]))
            sage: A.fixed_geodesic()
            Geodesic in PD from -1 to 1
        """
    def repelling_fixed_point(self):
        """
        For a hyperbolic isometry, return the attracting fixed point;
        otherwise raise a :exc:`ValueError`.

        OUTPUT: a hyperbolic point

        EXAMPLES::

            sage: UHP = HyperbolicPlane().UHP()
            sage: A = UHP.get_isometry(Matrix(2,[4,0,0,1/4]))
            sage: A.repelling_fixed_point()
            Boundary point in UHP 0
        """
    def attracting_fixed_point(self):
        """
        For a hyperbolic isometry, return the attracting fixed point;
        otherwise raise a :exc:`ValueError`.

        OUTPUT: a hyperbolic point

        EXAMPLES::

            sage: UHP = HyperbolicPlane().UHP()
            sage: A = UHP.get_isometry(Matrix(2,[4,0,0,1/4]))
            sage: A.attracting_fixed_point()
            Boundary point in UHP +Infinity
        """

class HyperbolicIsometryUHP(HyperbolicIsometry):
    """
    Create a hyperbolic isometry in the UHP model.

    INPUT:

    - a matrix in `GL(2, \\RR)`

    EXAMPLES::

        sage: HyperbolicPlane().UHP().get_isometry(identity_matrix(2))
        Isometry in UHP
        [1 0]
        [0 1]
    """
    def preserves_orientation(self):
        """
        Return ``True`` if ``self`` is orientation-preserving and ``False``
        otherwise.

        EXAMPLES::

            sage: UHP = HyperbolicPlane().UHP()
            sage: A = identity_matrix(2)
            sage: UHP.get_isometry(A).preserves_orientation()
            True
            sage: B = matrix(2,[0,1,1,0])
            sage: UHP.get_isometry(B).preserves_orientation()
            False
        """
    def classification(self):
        """
        Classify the hyperbolic isometry as elliptic, parabolic, or
        hyperbolic.

        A hyperbolic isometry fixes two points on the boundary of
        hyperbolic space, a parabolic isometry fixes one point on the
        boundary of hyperbolic space, and an elliptic isometry fixes
        no points.

        EXAMPLES::

            sage: UHP = HyperbolicPlane().UHP()
            sage: UHP.get_isometry(identity_matrix(2)).classification()
            'identity'

            sage: UHP.get_isometry(4*identity_matrix(2)).classification()
            'identity'

            sage: UHP.get_isometry(matrix(2,[2,0,0,1/2])).classification()
            'hyperbolic'

            sage: UHP.get_isometry(matrix(2, [0, 3, -1/3, 6])).classification()
            'hyperbolic'

            sage: UHP.get_isometry(matrix(2,[1,1,0,1])).classification()
            'parabolic'

            sage: UHP.get_isometry(matrix(2,[-1,0,0,1])).classification()
            'reflection'
        """
    def translation_length(self):
        """
        For hyperbolic elements, return the translation length;
        otherwise, raise a :exc:`ValueError`.

        EXAMPLES::

            sage: UHP = HyperbolicPlane().UHP()
            sage: UHP.get_isometry(matrix(2,[2,0,0,1/2])).translation_length()
            2*arccosh(5/4)

        ::

            sage: H = UHP.isometry_from_fixed_points(-1,1)
            sage: p = UHP.get_point(exp(i*7*pi/8))
            sage: Hp = H(p)
            sage: bool((UHP.dist(p, Hp) - H.translation_length()) < 10**-9)
            True
        """
    def fixed_point_set(self):
        """
        Return a list or geodesic containing the fixed point set of
        orientation-preserving isometries.

        OUTPUT: list of hyperbolic points or a hyperbolic geodesic

        EXAMPLES::

            sage: UHP = HyperbolicPlane().UHP()
            sage: H = UHP.get_isometry(matrix(2, [-2/3,-1/3,-1/3,-2/3]))
            sage: g = H.fixed_point_set(); g
            Geodesic in UHP from -1 to 1
            sage: H(g.start()) == g.start()
            True
            sage: H(g.end()) == g.end()
            True
            sage: A = UHP.get_isometry(matrix(2,[0,1,1,0]))
            sage: A.preserves_orientation()
            False
            sage: A.fixed_point_set()
            Geodesic in UHP from 1 to -1

        ::

            sage: B = UHP.get_isometry(identity_matrix(2))
            sage: B.fixed_point_set()
            Traceback (most recent call last):
            ...
            ValueError: the identity transformation fixes the entire hyperbolic plane
        """
    def repelling_fixed_point(self):
        """
        Return the repelling fixed point.

        Otherwise, this raises a :exc:`ValueError`.

        OUTPUT: a hyperbolic point

        EXAMPLES::

            sage: UHP = HyperbolicPlane().UHP()
            sage: A = matrix(2,[4,0,0,1/4])
            sage: UHP.get_isometry(A).repelling_fixed_point()
            Boundary point in UHP 0
        """
    def attracting_fixed_point(self):
        """
        Return the attracting fixed point.

        Otherwise, this raises a :exc:`ValueError`.

        OUTPUT: a hyperbolic point

        EXAMPLES::

            sage: UHP = HyperbolicPlane().UHP()
            sage: A = matrix(2,[4,0,0,1/4])
            sage: UHP.get_isometry(A).attracting_fixed_point()
            Boundary point in UHP +Infinity
        """

class HyperbolicIsometryPD(HyperbolicIsometry):
    """
    Create a hyperbolic isometry in the PD model.

    INPUT:

    - a matrix in `PU(1,1)`

    EXAMPLES::

        sage: HyperbolicPlane().PD().get_isometry(identity_matrix(2))
        Isometry in PD
        [1 0]
        [0 1]
    """
    def __mul__(self, other):
        """
        Return image of ``p`` under the action of ``self``.

        EXAMPLES::

            sage: PD = HyperbolicPlane().PD()
            sage: X = PD.get_isometry(matrix([[3/4, -I/4], [-I/4, -3/4]]))
            sage: X*X
            Isometry in PD
            [   5/8  3/8*I]
            [-3/8*I    5/8]
        """
    def __pow__(self, n):
        """
        EXAMPLES::

            sage: PD = HyperbolicPlane().PD()
            sage: X = PD.get_isometry(matrix([[3/4, -I/4], [-I/4, -3/4]]))
            sage: X^2
            Isometry in PD
            [   5/8  3/8*I]
            [-3/8*I    5/8]
        """
    def preserves_orientation(self):
        """
        Return ``True`` if ``self`` preserves orientation and ``False``
        otherwise.

        EXAMPLES::

            sage: PD = HyperbolicPlane().PD()
            sage: PD.get_isometry(matrix([[-I, 0], [0, I]])).preserves_orientation()
            True
            sage: PD.get_isometry(matrix([[0, I], [I, 0]])).preserves_orientation()
            False
        """

class HyperbolicIsometryKM(HyperbolicIsometry):
    """
    Create a hyperbolic isometry in the KM model.

    INPUT:

    - a matrix in `SO(2,1)`

    EXAMPLES::

        sage: HyperbolicPlane().KM().get_isometry(identity_matrix(3))
        Isometry in KM
        [1 0 0]
        [0 1 0]
        [0 0 1]
    """

def moebius_transform(A, z):
    """
    Given a matrix ``A`` in `GL(2, \\CC)` and a point ``z`` in the complex
    plane return the Möbius transformation action of ``A`` on ``z``.

    INPUT:

    - ``A`` -- a `2 \\times 2` invertible matrix over the complex numbers
    - ``z`` -- a complex number or infinity

    OUTPUT: a complex number or infinity

    EXAMPLES::

        sage: from sage.geometry.hyperbolic_space.hyperbolic_model import moebius_transform
        sage: moebius_transform(matrix(2,[1,2,3,4]),2 + I)
        -2/109*I + 43/109
        sage: y = var('y')
        sage: moebius_transform(matrix(2,[1,0,0,1]),x + I*y)
        x + I*y

    The matrix must be square and `2 \\times 2`::

        sage: moebius_transform(matrix([[3,1,2],[1,2,5]]),I)
        Traceback (most recent call last):
        ...
        TypeError: A must be an invertible 2x2 matrix over the complex numbers or a symbolic ring

        sage: moebius_transform(identity_matrix(3),I)
        Traceback (most recent call last):
        ...
        TypeError: A must be an invertible 2x2 matrix over the complex numbers or a symbolic ring

    The matrix can be symbolic or can be a matrix over the real
    or complex numbers, but must be provably invertible::

        sage: a,b,c,d = var('a,b,c,d')
        sage: moebius_transform(matrix(2,[a,b,c,d]),I)
        (I*a + b)/(I*c + d)
        sage: moebius_transform(matrix(2,[1,b,c,b*c+1]),I)
        (b + I)/(b*c + I*c + 1)
        sage: moebius_transform(matrix(2,[0,0,0,0]),I)
        Traceback (most recent call last):
        ...
        TypeError: A must be an invertible 2x2 matrix over the complex numbers or a symbolic ring
    """
