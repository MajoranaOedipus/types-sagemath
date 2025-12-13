from sage.schemes.generic.point import SchemeTopologicalPoint_prime_ideal as SchemeTopologicalPoint_prime_ideal
from sage.structure.richcmp import richcmp as richcmp

class CurveClosedPoint(SchemeTopologicalPoint_prime_ideal):
    """
    Base class of closed points of curves.
    """

class IntegralCurveClosedPoint(CurveClosedPoint):
    """
    Closed points of integral curves.

    INPUT:

    - ``curve`` -- the curve to which the closed point belongs

    - ``prime_ideal`` -- a prime ideal

    - ``degree`` -- degree of the closed point

    EXAMPLES::

        sage: # needs sage.rings.finite_rings
        sage: F.<a> = GF(4)
        sage: P.<x,y> = AffineSpace(F, 2)
        sage: C = Curve(y^2 + y - x^3)
        sage: C.closed_points()
        [Point (x, y),
         Point (x, y + 1),
         Point (x + a, y + a),
         Point (x + a, y + (a + 1)),
         Point (x + (a + 1), y + a),
         Point (x + (a + 1), y + (a + 1)),
         Point (x + 1, y + a),
         Point (x + 1, y + (a + 1))]
    """
    def __init__(self, curve, prime_ideal, degree) -> None:
        """
        Initialize.

        TESTS::

            sage: # needs sage.rings.finite_rings
            sage: F.<a> = GF(4)
            sage: P.<x,y> = AffineSpace(F, 2)
            sage: C = Curve(y^2 + y - x^3)
            sage: p = C([0,0]); p
            (0, 0)
            sage: loads(dumps(p)) == p
            True
        """
    def __hash__(self):
        """
        Return the hash of ``self``.

        EXAMPLES::

            sage: # needs sage.rings.finite_rings
            sage: F.<a> = GF(4)
            sage: P.<x,y> = AffineSpace(F, 2)
            sage: C = Curve(y^2 + y - x^3)
            sage: pts = C.closed_points()
            sage: p = pts[0]
            sage: {p: 1}
            {Point (x, y): 1}
        """
    def curve(self):
        """
        Return the curve to which this point belongs.

        EXAMPLES::

            sage: # needs sage.rings.finite_rings
            sage: F.<a> = GF(4)
            sage: P.<x,y> = AffineSpace(F, 2)
            sage: C = Curve(y^2 + y - x^3)
            sage: pts = C.closed_points()
            sage: p = pts[0]
            sage: p.curve()
            Affine Plane Curve over Finite Field in a of size 2^2 defined by x^3 + y^2 + y
        """
    def degree(self):
        """
        Return the degree of the point.

        EXAMPLES::

            sage: # needs sage.rings.finite_rings
            sage: F.<a> = GF(4)
            sage: P.<x,y> = AffineSpace(F, 2)
            sage: C = Curve(y^2 + y - x^3)
            sage: pts = C.closed_points()
            sage: p = pts[0]
            sage: p.degree()
            1
        """
    def places(self):
        """
        Return all places on this closed point.

        EXAMPLES::

            sage: # needs sage.rings.finite_rings
            sage: F.<a> = GF(4)
            sage: P.<x,y> = AffineSpace(F, 2)
            sage: C = Curve(y^2 + y - x^3)
            sage: pts = C.closed_points()
            sage: p = pts[0]
            sage: p.places()
            [Place (x, y)]
        """
    def place(self):
        """
        Return a place on this closed point.

        If there are more than one, arbitrary one is chosen.

        EXAMPLES::

            sage: # needs sage.rings.finite_rings
            sage: F.<a> = GF(4)
            sage: P.<x,y> = AffineSpace(F, 2)
            sage: C = Curve(y^2 + y - x^3)
            sage: pts = C.closed_points()
            sage: p = pts[0]
            sage: p.place()
            Place (x, y)
        """

class IntegralAffineCurveClosedPoint(IntegralCurveClosedPoint):
    """
    Closed points of affine curves.
    """
    def rational_point(self):
        """
        Return the rational point if this closed point is of degree `1`.

        EXAMPLES::

            sage: # needs sage.rings.finite_rings
            sage: A.<x,y> = AffineSpace(GF(3^2), 2)
            sage: C = Curve(y^2 - x^5 - x^4 - 2*x^3 - 2*x - 2)
            sage: C.closed_points()
            [Point (x, y + (z2 + 1)),
             Point (x, y + (-z2 - 1)),
             Point (x + (z2 + 1), y + (z2 - 1)),
             Point (x + (z2 + 1), y + (-z2 + 1)),
             Point (x - 1, y + (z2 + 1)),
             Point (x - 1, y + (-z2 - 1)),
             Point (x + (-z2 - 1), y + z2),
             Point (x + (-z2 - 1), y + (-z2)),
             Point (x + 1, y + 1),
             Point (x + 1, y - 1)]
            sage: [p.rational_point() for p in _]
            [(0, 2*z2 + 2),
             (0, z2 + 1),
             (2*z2 + 2, 2*z2 + 1),
             (2*z2 + 2, z2 + 2),
             (1, 2*z2 + 2),
             (1, z2 + 1),
             (z2 + 1, 2*z2),
             (z2 + 1, z2),
             (2, 2),
             (2, 1)]
            sage: set(_) == set(C.rational_points())
            True
        """
    def projective(self, i: int = 0):
        """
        Return the point in the projective closure of the curve, of which this
        curve is the ``i``-th affine patch.

        INPUT:

        - ``i`` -- integer

        EXAMPLES::

            sage: F.<a> = GF(2)
            sage: A.<x,y> = AffineSpace(F, 2)
            sage: C = Curve(y^2 + y - x^3, A)
            sage: p1, p2 = C.closed_points()
            sage: p1
            Point (x, y)
            sage: p2
            Point (x, y + 1)
            sage: p1.projective()
            Point (x1, x2)
            sage: p2.projective(0)
            Point (x1, x0 + x2)
            sage: p2.projective(1)
            Point (x0, x1 + x2)
            sage: p2.projective(2)
            Point (x0, x1 + x2)
        """

class IntegralProjectiveCurveClosedPoint(IntegralCurveClosedPoint):
    """
    Closed points of projective plane curves.
    """
    def rational_point(self):
        """
        Return the rational point if this closed point is of degree `1`.

        EXAMPLES::

            sage: # needs sage.rings.finite_rings
            sage: F.<a> = GF(4)
            sage: P.<x,y,z> = ProjectiveSpace(F, 2)
            sage: C = Curve(x^3*y + y^3*z + x*z^3)
            sage: C.closed_points()
            [Point (x, z),
             Point (x, y),
             Point (y, z),
             Point (x + a*z, y + (a + 1)*z),
             Point (x + (a + 1)*z, y + a*z)]
            sage: [p.rational_point() for p in _]
            [(0 : 1 : 0), (0 : 0 : 1), (1 : 0 : 0), (a : a + 1 : 1), (a + 1 : a : 1)]
            sage: set(_) == set(C.rational_points())
            True
        """
    def affine(self, i=None):
        """
        Return the point in the ``i``-th affine patch of the curve.

        INPUT:

        - ``i`` -- integer; if not specified, it is chosen automatically

        EXAMPLES::

            sage: F.<a> = GF(2)
            sage: P.<x,y,z> = ProjectiveSpace(F, 2)
            sage: C = Curve(x^3*y + y^3*z + x*z^3)
            sage: p1, p2, p3 = C.closed_points()
            sage: p1.affine()
            Point (x, z)
            sage: p2.affine()
            Point (x, y)
            sage: p3.affine()
            Point (y, z)
            sage: p3.affine(0)
            Point (y, z)
            sage: p3.affine(1)
            Traceback (most recent call last):
            ...
            ValueError: not in the affine patch
        """
