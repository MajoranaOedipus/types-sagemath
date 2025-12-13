from sage.arith.misc import GCD as GCD
from sage.rings.polynomial.polynomial_ring_constructor import PolynomialRing as PolynomialRing
from sage.schemes.curves.affine_curve import AffinePlaneCurve as AffinePlaneCurve
from sage.structure.category_object import normalize_names as normalize_names

class CyclicCover_generic(AffinePlaneCurve):
    def __init__(self, AA, r, f, names=None) -> None:
        '''
        Cyclic covers over a general ring.

        INPUT:

        - ``A`` -- ambient affine space

        - ``r`` -- degree of the cover

        - ``f`` -- univariate polynomial

        - ``names`` -- (default: ``["x","y"]``); names for the
          coordinate functions

        TESTS::

            sage: ZZx.<x> = ZZ[]
            sage: C = CyclicCover(5, x^5 + x + 1); C
            Cyclic Cover of P^1 over Integer Ring defined by y^5 = x^5 + x + 1
            sage: C.genus()
            6
            sage: D = C.projective_closure(); D
            Projective Plane Curve over Integer Ring defined by x0^5 + x0^4*x1 + x1^5 - x2^5
            sage: D.change_ring(QQ).genus()
            6
            sage: C.change_ring(GF(5))
            Traceback (most recent call last):
            ...
            ValueError: As the characteristic divides the order of the cover,
            this model is not smooth.


            sage: GF7x.<x> = GF(7)[]
            sage: C = CyclicCover(3, x^9 + x + 1)
            sage: C
            Cyclic Cover of P^1 over Finite Field of size 7 defined by y^3 = x^9 + x + 1
            sage: C.genus()
            7
            sage: C.projective_closure()
            Traceback (most recent call last):
            ...
            NotImplementedError: Weighted Projective Space is not implemented
        '''
    def change_ring(self, R):
        """
        Return this CyclicCover over a new base ring R.

        EXAMPLES::

            sage: ZZx.<x> = ZZ[]
            sage: C = CyclicCover(5, x^5 + x + 1)
            sage: C.change_ring(GF(5))
            Traceback (most recent call last):
            ...
            ValueError: As the characteristic divides the order of the cover,
            this model is not smooth.
            sage: C.change_ring(GF(3))
            Traceback (most recent call last):
            ...
            ValueError: Not a smooth Cyclic Cover of P^1: singularity in the
            provided affine patch.
            sage: C.change_ring(GF(17))
            Cyclic Cover of P^1 over Finite Field of size 17 defined by y^5 = x^5 + x + 1
        """
    base_extend = change_ring
    def __eq__(self, other):
        """
        Test of equality.

        EXAMPLES::

            sage: ZZx.<x> = ZZ[]
            sage: C0 = CyclicCover(5, x^5 + x + 1)
            sage: C1 = C0.change_ring(QQ)
            sage: C1 == C0
            False
            sage: C2 = CyclicCover(3, x^5 + x + 1)
            sage: C2 == C0
            False
            sage: C3 = CyclicCover(5, x^6 + x + 1)
            sage: C3 == C0
            False
            sage: C0 == CyclicCover(5, x^5 + x + 1)
            True
        """
    def __ne__(self, other):
        """
        Test of not equality.

        EXAMPLES::

            sage: ZZx.<x> = ZZ[]
            sage: C0 = CyclicCover(5, x^5 + x + 1)
            sage: C1 = C0.change_ring(QQ)
            sage: C1 != C0
            True
            sage: C2 = CyclicCover(3, x^5 + x + 1)
            sage: C2 != C0
            True
            sage: C3 = CyclicCover(5, x^6 + x + 1)
            sage: C3 != C0
            True
            sage: C0 != CyclicCover(5, x^5 + x + 1)
            False
        """
    def order(self):
        """
        The order of the cover.

        EXAMPLES::

            sage: ZZx.<x> = ZZ[]
            sage: CyclicCover(5, x^5 + x + 1).order()
            5
            sage: CyclicCover(3, x^5 + x + 1).order()
            3
        """
    def genus(self):
        """
        The geometric genus of the curve.

        EXAMPLES::

            sage: ZZx.<x> = ZZ[]
            sage: CyclicCover(5, x^5 + x + 1).genus()
            6
            sage: CyclicCover(3, x^5 + x + 1).genus()
            4
        """
    def projective_closure(self, **kwds):
        """
        Return the projective closure of this affine curve.

        EXAMPLES::

            sage: GF7x.<x> = GF(7)[]
            sage: CyclicCover(3, x^9 + x + 1).projective_closure()
            Traceback (most recent call last):
            ...
            NotImplementedError: Weighted Projective Space is not implemented

            sage: ZZx.<x> = ZZ[]
            sage: CyclicCover(5, x^5 + x + 1).projective_closure()
            Projective Plane Curve over Integer Ring defined by x0^5 + x0^4*x1 + x1^5 - x2^5
        """
    def cover_polynomial(self, K=None, var: str = 'x'):
        """
        Return the polynomial defining the cyclic cover.

        EXAMPLES::

            sage: ZZx.<x> = ZZ[]; CyclicCover(5, x^5 + x + 1).cover_polynomial()
            x^5 + x + 1
        """
    def is_singular(self):
        """
        Return if this curve is singular or not.

        This just checks that the characteristic of the ring does not divide the
        order of the cover and that the defining polynomial of the cover is
        square free.

        EXAMPLES::

            sage: R.<x> = QQ[]
            sage: CyclicCover(3, x^5 + x + 1).is_singular()
            False
            sage: CyclicCover(3, (x^5 + x + 1)^2, check_smooth=False).is_singular()
            True
        """
    def is_smooth(self):
        """
        Return if this curve is smooth or not.

        This just checks that the characteristic of the ring does not divide the
        order of the cover and that the defining polynomial of the cover is
        square free.

        EXAMPLES::

            sage: R.<x> = QQ[]
            sage: CyclicCover(3, x^5 + x + 1).is_smooth()
            True
            sage: CyclicCover(3, (x^5 + x + 1)^2, check_smooth=False).is_smooth()
            False
        """
