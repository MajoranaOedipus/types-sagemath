from sage.functions.other import imag as imag, real as real
from sage.geometry.hyperbolic_space.hyperbolic_isometry import HyperbolicIsometry as HyperbolicIsometry
from sage.matrix.constructor import matrix as matrix
from sage.misc.latex import latex as latex
from sage.modules.free_module_element import vector as vector
from sage.rings.cc import CC as CC
from sage.rings.infinity import infinity as infinity
from sage.rings.real_mpfr import RR as RR
from sage.structure.element import Element as Element, Matrix as Matrix
from sage.structure.richcmp import op_NE as op_NE, richcmp as richcmp
from sage.symbolic.constants import I as I

class HyperbolicPoint(Element):
    """
    Abstract base class for hyperbolic points.  This class should never
    be instantiated.

    INPUT:

    - ``model`` -- the model of the hyperbolic space
    - ``coordinates`` -- the coordinates of a hyperbolic point in the
      appropriate model
    - ``is_boundary`` -- whether the point is a boundary point
    - ``check`` -- boolean (default: ``True``); if ``True``, then check to make sure
      the coordinates give a valid point in the model

    EXAMPLES:

    Comparison between different models is performed via coercion::

        sage: UHP = HyperbolicPlane().UHP()
        sage: p = UHP.get_point(.2 + .3*I); p
        Point in UHP 0.200000000000000 + 0.300000000000000*I

        sage: PD = HyperbolicPlane().PD()
        sage: q = PD.get_point(0.2 + 0.3*I); q
        Point in PD 0.200000000000000 + 0.300000000000000*I

        sage: p == q
        False
        sage: PD(p)
        Point in PD 0.231213872832370 - 0.502890173410405*I

        sage: bool(p.coordinates() == q.coordinates())
        True

    Similarly for boundary points::

        sage: p = UHP.get_point(-1); p
        Boundary point in UHP -1

        sage: q = PD.get_point(-1); q
        Boundary point in PD -1

        sage: p == q
        True
        sage: PD(p)
        Boundary point in PD -1

    It is an error to specify a point that does not lie in the
    appropriate model::

        sage: HyperbolicPlane().UHP().get_point(0.2 - 0.3*I)
        Traceback (most recent call last):
        ...
        ValueError: 0.200000000000000 - 0.300000000000000*I is not a valid point in the UHP model

        sage: HyperbolicPlane().PD().get_point(1.2)
        Traceback (most recent call last):
        ...
        ValueError: 1.20000000000000 is not a valid point in the PD model

        sage: HyperbolicPlane().KM().get_point((1,1))
        Traceback (most recent call last):
        ...
        ValueError: (1, 1) is not a valid point in the KM model

        sage: HyperbolicPlane().HM().get_point((1, 1, 1))
        Traceback (most recent call last):
        ...
        ValueError: (1, 1, 1) is not a valid point in the HM model

    It is an error to specify an interior point of hyperbolic space as a
    boundary point::

        sage: HyperbolicPlane().UHP().get_point(0.2 + 0.3*I, is_boundary=True)
        Traceback (most recent call last):
        ...
        ValueError: 0.200000000000000 + 0.300000000000000*I is not a valid boundary point in the UHP model

    TESTS:

    In the PD model, the coordinates of a point are in the unit disk
    in the complex plane `\\CC`::

        sage: HyperbolicPlane().PD().get_point(0)
        Point in PD 0
        sage: HyperbolicPlane().PD().get_point(1)
        Boundary point in PD 1

    In the KM model, the coordinates of a point are in the unit disk
    in the real plane `\\RR^2`::

        sage: HyperbolicPlane().KM().get_point((0,0))
        Point in KM (0, 0)
        sage: HyperbolicPlane().KM().get_point((1,0))
        Boundary point in KM (1, 0)

    In the HM model, the coordinates of a point are on the
    hyperboloid given by `x^2 + y^2 - z^2 = -1`::

        sage: HyperbolicPlane().HM().get_point((0,0,1))
        Point in HM (0, 0, 1)
        sage: HyperbolicPlane().HM().get_point((0,0,2))
        Traceback (most recent call last):
        ...
        ValueError: (0, 0, 2) is not a valid point in the HM model
        sage: HyperbolicPlane().HM().get_point((1,0,0), is_boundary=True)
        Traceback (most recent call last):
        ...
        NotImplementedError: boundary points are not implemented in the HM model
    """
    def __init__(self, model, coordinates, is_boundary, check: bool = True, **graphics_options) -> None:
        """
        See ``HyperbolicPoint`` for full documentation.

        EXAMPLES::

            sage: p = HyperbolicPlane().UHP().get_point(I)
            sage: TestSuite(p).run()
            sage: p1 = HyperbolicPlane().KM().get_point((0,0))
            sage: p2 = HyperbolicPlane().KM().get_point([0,0])
            sage: p1 == p2
            True
        """
    def __rmul__(self, other):
        """
        Implement the action of matrices on points of hyperbolic space.

        EXAMPLES::

            sage: A = matrix(2, [0, 1, 1, 0])
            sage: A = HyperbolicPlane().UHP().get_isometry(A)
            sage: A * HyperbolicPlane().UHP().get_point(2 + I)
            Point in UHP 1/5*I + 2/5

        We also lift matrices into isometries::

            sage: B = diagonal_matrix([-1, -1, 1])
            sage: B = HyperbolicPlane().HM().get_isometry(B)                            # needs scipy
            sage: B * HyperbolicPlane().HM().get_point((0, 1, sqrt(2)))
            Point in HM (0, -1, sqrt(2))
        """
    def coordinates(self):
        """
        Return the coordinates of the point.

        EXAMPLES::

            sage: HyperbolicPlane().UHP().get_point(2 + I).coordinates()
            I + 2

            sage: HyperbolicPlane().PD().get_point(1/2 + 1/2*I).coordinates()
            1/2*I + 1/2

            sage: HyperbolicPlane().KM().get_point((1/3, 1/4)).coordinates()
            (1/3, 1/4)

            sage: HyperbolicPlane().HM().get_point((0,0,1)).coordinates()
            (0, 0, 1)
        """
    def model(self):
        """
        Return the model to which the :class:`HyperbolicPoint` belongs.

        EXAMPLES::

            sage: HyperbolicPlane().UHP().get_point(I).model()
            Hyperbolic plane in the Upper Half Plane Model

            sage: HyperbolicPlane().PD().get_point(0).model()
            Hyperbolic plane in the Poincare Disk Model

            sage: HyperbolicPlane().KM().get_point((0,0)).model()
            Hyperbolic plane in the Klein Disk Model

            sage: HyperbolicPlane().HM().get_point((0,0,1)).model()
            Hyperbolic plane in the Hyperboloid Model
        """
    def to_model(self, model):
        """
        Convert ``self`` to the ``model``.

        INPUT:

        - ``other`` -- (a string representing) the image model

        EXAMPLES::

            sage: UHP = HyperbolicPlane().UHP()
            sage: PD = HyperbolicPlane().PD()
            sage: PD.get_point(1/2+I/2).to_model(UHP)
            Point in UHP I + 2
            sage: PD.get_point(1/2+I/2).to_model('UHP')
            Point in UHP I + 2
        """
    def is_boundary(self):
        """
        Return ``True`` if ``self`` is a boundary point.

        EXAMPLES::

            sage: PD = HyperbolicPlane().PD()
            sage: p = PD.get_point(0.5+.2*I)
            sage: p.is_boundary()
            False
            sage: p = PD.get_point(I)
            sage: p.is_boundary()
            True
        """
    def update_graphics(self, update: bool = False, **options) -> None:
        '''
        Update the graphics options of a :class:`HyperbolicPoint`.
        If ``update`` is ``True``, update rather than overwrite.

        EXAMPLES::

            sage: p = HyperbolicPlane().UHP().get_point(I); p.graphics_options()
            {}

            sage: p.update_graphics(color = "red"); p.graphics_options()
            {\'color\': \'red\'}

            sage: p.update_graphics(color = "blue"); p.graphics_options()
            {\'color\': \'blue\'}

            sage: p.update_graphics(True, size = 20); p.graphics_options()
            {\'color\': \'blue\', \'size\': 20}
        '''
    def graphics_options(self):
        """
        Return the graphics options of the current point.

        EXAMPLES::

            sage: p = HyperbolicPlane().UHP().get_point(2 + I, color='red')
            sage: p.graphics_options()
            {'color': 'red'}
        """
    def symmetry_involution(self):
        """
        Return the involutory isometry fixing the given point.

        EXAMPLES::

            sage: z = HyperbolicPlane().UHP().get_point(3 + 2*I)
            sage: z.symmetry_involution()
            Isometry in UHP
            [  3/2 -13/2]
            [  1/2  -3/2]

            sage: HyperbolicPlane().UHP().get_point(I).symmetry_involution()
            Isometry in UHP
            [ 0 -1]
            [ 1  0]

            sage: HyperbolicPlane().PD().get_point(0).symmetry_involution()
            Isometry in PD
            [-I  0]
            [ 0  I]

            sage: HyperbolicPlane().KM().get_point((0, 0)).symmetry_involution()
            Isometry in KM
            [-1  0  0]
            [ 0 -1  0]
            [ 0  0  1]

            sage: HyperbolicPlane().HM().get_point((0,0,1)).symmetry_involution()
            Isometry in HM
            [-1  0  0]
            [ 0 -1  0]
            [ 0  0  1]

            sage: p = HyperbolicPlane().UHP().random_element()
            sage: A = p.symmetry_involution()
            sage: p.dist(A*p)  # abs tol 1e-10
            0

            sage: A.preserves_orientation()
            True

            sage: A*A == HyperbolicPlane().UHP().get_isometry(identity_matrix(2))       # needs scipy
            True
        """
    def show(self, boundary: bool = True, **options):
        """
        Plot ``self``.

        EXAMPLES::

            sage: HyperbolicPlane().PD().get_point(0).show()                            # needs sage.plot
            Graphics object consisting of 2 graphics primitives
            sage: HyperbolicPlane().KM().get_point((0,0)).show()                        # needs sage.plot
            Graphics object consisting of 2 graphics primitives
            sage: HyperbolicPlane().HM().get_point((0,0,1)).show()                      # needs sage.plot
            Graphics3d Object
        """

class HyperbolicPointUHP(HyperbolicPoint):
    """
    A point in the UHP model.

    INPUT:

    - the coordinates of a point in the unit disk in the complex plane `\\CC`

    EXAMPLES::

        sage: HyperbolicPlane().UHP().get_point(2*I)
        Point in UHP 2*I

        sage: HyperbolicPlane().UHP().get_point(1)
        Boundary point in UHP 1
    """
    def symmetry_involution(self):
        """
        Return the involutory isometry fixing the given point.

        EXAMPLES::

            sage: HyperbolicPlane().UHP().get_point(3 + 2*I).symmetry_involution()
            Isometry in UHP
            [  3/2 -13/2]
            [  1/2  -3/2]
        """
    def show(self, boundary: bool = True, **options):
        """
        Plot ``self``.

        EXAMPLES::

            sage: HyperbolicPlane().UHP().get_point(I).show()
            Graphics object consisting of 2 graphics primitives
            sage: HyperbolicPlane().UHP().get_point(0).show()                           # needs sage.plot
            Graphics object consisting of 2 graphics primitives
            sage: HyperbolicPlane().UHP().get_point(infinity).show()
            Traceback (most recent call last):
            ...
            NotImplementedError: can...t draw the point infinity
        """
