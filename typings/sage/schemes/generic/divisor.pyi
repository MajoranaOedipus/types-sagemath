from sage.misc.latex import latex as latex
from sage.misc.lazy_import import lazy_import as lazy_import
from sage.misc.repr import repr_lincomb as repr_lincomb
from sage.misc.search import search as search
from sage.rings.integer_ring import ZZ as ZZ
from sage.schemes.affine.affine_space import AffineSpace_generic as AffineSpace_generic
from sage.schemes.projective.projective_space import ProjectiveSpace_ring as ProjectiveSpace_ring
from sage.structure.formal_sum import FormalSum as FormalSum

def CurvePointToIdeal(C, P):
    """
    Return the vanishing ideal of a point on a curve.

    EXAMPLES::

        sage: x,y = AffineSpace(2, QQ, names='xy').gens()
        sage: C = Curve(y^2 - x^9 - x)
        sage: from sage.schemes.generic.divisor import CurvePointToIdeal
        sage: CurvePointToIdeal(C, (0,0))
        Ideal (x, y) of Multivariate Polynomial Ring in x, y over Rational Field
    """
def is_Divisor(x):
    '''
    Test whether ``x`` is an instance of :class:`Divisor_generic`.

    INPUT:

    - ``x`` -- anything

    OUTPUT: boolean

    EXAMPLES::

        sage: from sage.schemes.generic.divisor import is_Divisor
        sage: x,y = AffineSpace(2, GF(5), names=\'xy\').gens()
        sage: C = Curve(y^2 - x^9 - x)
        sage: is_Divisor(C.divisor([]))
        doctest:warning...
        DeprecationWarning: The function is_Divisor is deprecated;
        use \'isinstance(..., Divisor_generic)\' instead.
        See https://github.com/sagemath/sage/issues/38277 for details.
        True
        sage: is_Divisor("Ceci n\'est pas un diviseur")
        False
    '''

class Divisor_generic(FormalSum):
    """
    A Divisor.

    TESTS::

        sage: E = EllipticCurve([1, 2])
        sage: P = E(-1, 0)
        sage: Q = E(1, 2)
        sage: Pd = E.divisor(P)
        sage: Qd = E.divisor(Q)
        sage: Pd + Qd == Qd + Pd
        True
        sage: Pd != Qd
        True
        sage: C = EllipticCurve([2, 1])
        sage: R = C(1, 2)
        sage: Rd = C.divisor(R)
        sage: Qd == Rd
        False
        sage: Rd == Qd
        False
        sage: Qd == (2 * (Qd * 1/2))
        True
        sage: Qd == 1/2 * Qd
        False
    """
    def __init__(self, v, parent, check: bool = True, reduce: bool = True) -> None:
        """
        Construct a :class:`Divisor_generic`.

        INPUT:

        INPUT:

        - ``v`` -- object; usually a list of pairs ``(coefficient,divisor)``

        - ``parent`` -- FormalSums(R) module (default: FormalSums(ZZ))

        - ``check`` -- boolean (default: ``True``); whether to coerce
          coefficients into base ring. Setting it to ``False`` can
          speed up construction.

        - ``reduce`` -- reduce (default: ``True``); whether to combine
          common terms. Setting it to ``False`` can speed up
          construction.

        .. WARNING::

            The coefficients of the divisor must be in the base ring
            and the terms must be reduced. If you set ``check=False``
            and/or ``reduce=False`` it is your responsibility to pass
            a valid object ``v``.

        EXAMPLES::

            sage: from sage.schemes.generic.divisor import Divisor_generic
            sage: from sage.schemes.generic.divisor_group import DivisorGroup
            sage: Divisor_generic( [(4,5)], DivisorGroup(Spec(ZZ)), False, False)
            4*V(5)
        """
    def scheme(self):
        """
        Return the scheme that this divisor is on.

        EXAMPLES::

            sage: A.<x, y> = AffineSpace(2, GF(5))
            sage: C = Curve(y^2 - x^9 - x)
            sage: pts = C.rational_points(); pts
            [(0, 0), (2, 2), (2, 3), (3, 1), (3, 4)]
            sage: D = C.divisor(pts[0])*3 - C.divisor(pts[1]); D
            3*(x, y) - (x - 2, y - 2)
            sage: D.scheme()
            Affine Plane Curve over Finite Field of size 5 defined by -x^9 + y^2 - x
        """

class Divisor_curve(Divisor_generic):
    """
    For any curve `C`, use ``C.divisor(v)`` to
    construct a divisor on `C`. Here `v` can be either

    - a rational point on `C`

    - a list of rational points

    - a list of 2-tuples `(c,P)`, where `c` is an
      integer and `P` is a rational point

    TODO: Divisors shouldn't be restricted to rational points. The
    problem is that the divisor group is the formal sum of the group of
    points on the curve, and there's no implemented notion of point on
    `E/K` that has coordinates in `L`. This is what
    should be implemented, by adding an appropriate class to
    ``schemes/generic/morphism.py``.

    EXAMPLES::

        sage: E = EllipticCurve([0, 0, 1, -1, 0])
        sage: P = E(0,0)
        sage: 10*P
        (161/16 : -2065/64 : 1)
        sage: D = E.divisor(P)
        sage: D
        (x, y)
        sage: 10*D
        10*(x, y)
        sage: E.divisor([P, P])
        2*(x, y)
        sage: E.divisor([(3,P), (-4,5*P)])
        3*(x, y) - 4*(x - 1/4*z, y + 5/8*z)
    """
    def __init__(self, v, parent=None, check: bool = True, reduce: bool = True) -> None:
        """
        Construct a divisor on a curve.

        INPUT:

        - ``v`` -- list of pairs ``(c, P)``, where ``c`` is an
          integer and ``P`` is a point on a curve. The P's must all
          lie on the same curve.

        To create the divisor 0 use ``[(0, P)]``, so as to give the curve.

        EXAMPLES::

            sage: E = EllipticCurve([0, 0, 1, -1, 0])
            sage: P = E(0,0)
            sage: from sage.schemes.generic.divisor import Divisor_curve
            sage: from sage.schemes.generic.divisor_group import DivisorGroup
            sage: Divisor_curve([(1, P)], parent=DivisorGroup(E))
            (x, y)
        """
    def support(self) -> list:
        """
        Return the support of this divisor, which is the set of points that
        occur in this divisor with nonzero coefficients.

        EXAMPLES::

            sage: A = AffineSpace(2, GF(5), names='xy')
            sage: x, y = A.gens()
            sage: C = Curve(y^2 - x^9 - x)
            sage: pts = C.rational_points(); pts
            [(0, 0), (2, 2), (2, 3), (3, 1), (3, 4)]
            sage: D = C.divisor_group()([(3, pts[0]), (-1, pts[1])]); D
            3*(x, y) - (x - 2, y - 2)
            sage: D.support()
            [(0, 0), (2, 2)]

        TESTS:

        This checks that :issue:`10732` is fixed::

            sage: R.<x, y, z> = GF(5)[]
            sage: C = Curve(x^7 + y^7 + z^7)
            sage: pts = C.rational_points()
            sage: D = C.divisor([(2, pts[0])])
            sage: D.support()
            [(0 : 4 : 1)]
            sage: (D + D).support()
            [(0 : 4 : 1)]
            sage: E = C.divisor([(-3, pts[1]), (1, pts[2])])
            sage: (D - 2*E).support()
            [(0 : 4 : 1), (1 : 2 : 1), (2 : 1 : 1)]
            sage: (D - D).support()
            []
        """
    def coefficient(self, P):
        """
        Return the coefficient of a given point P in this divisor.

        EXAMPLES::

            sage: x,y = AffineSpace(2, GF(5), names='xy').gens()
            sage: C = Curve(y^2 - x^9 - x)
            sage: pts = C.rational_points(); pts
            [(0, 0), (2, 2), (2, 3), (3, 1), (3, 4)]
            sage: D = C.divisor(pts[0])
            sage: D.coefficient(pts[0])
            1
            sage: D = C.divisor([(3, pts[0]), (-1, pts[1])]); D
            3*(x, y) - (x - 2, y - 2)
            sage: D.coefficient(pts[0])
            3
            sage: D.coefficient(pts[1])
            -1
        """
