from _typeshed import Incomplete
from sage.categories.commutative_rings import CommutativeRings as CommutativeRings
from sage.categories.fields import Fields as Fields
from sage.categories.number_fields import NumberFields as NumberFields
from sage.misc.cachefunc import cached_method as cached_method
from sage.misc.functional import sqrt as sqrt
from sage.misc.lazy_import import lazy_import as lazy_import
from sage.misc.mrange import xmrange as xmrange
from sage.rings.finite_rings.finite_field_constructor import GF as GF
from sage.rings.fraction_field import FractionField as FractionField
from sage.rings.integer_ring import ZZ as ZZ
from sage.rings.polynomial.polynomial_ring_constructor import PolynomialRing as PolynomialRing
from sage.rings.rational_field import QQ as QQ
from sage.rings.real_mpfr import RealField as RealField
from sage.schemes.generic.algebraic_scheme import AlgebraicScheme_subscheme as AlgebraicScheme_subscheme
from sage.schemes.product_projective.space import ProductProjectiveSpaces as ProductProjectiveSpaces
from sage.schemes.product_projective.subscheme import AlgebraicScheme_subscheme_product_projective as AlgebraicScheme_subscheme_product_projective

def WehlerK3Surface(polys):
    """
    Define a K3 Surface over `\\mathbb{P}^2 \\times \\mathbb{P}^2` defined as
    the intersection of a bilinear and biquadratic form. [Weh1998]_

    INPUT:

    - ``polys`` -- bilinear and biquadratic polynomials as a tuple or list

    OUTPUT: :class:`WehlerK3Surface_ring`

    EXAMPLES::

        sage: PP.<x0,x1, x2, y0, y1, y2> = ProductProjectiveSpaces([2, 2], QQ)
        sage: L = x0*y0 + x1*y1 - x2*y2
        sage: Q = x0*x1*y1^2 + x2^2*y0*y2
        sage: WehlerK3Surface([L, Q])
        Closed subscheme of Product of projective spaces P^2 x P^2 over Rational
        Field defined by:
         x0*y0 + x1*y1 - x2*y2,
         x0*x1*y1^2 + x2^2*y0*y2
    """
def random_WehlerK3Surface(PP):
    """
    Produces a random K3 surface in `\\mathbb{P}^2 \\times \\mathbb{P}^2` defined as the
    intersection of a bilinear and biquadratic form. [Weh1998]_

    INPUT:

    - ``PP`` -- projective space cartesian product

    OUTPUT: :class:`WehlerK3Surface_ring`

    EXAMPLES::

        sage: PP.<x0, x1, x2, y0, y1, y2> = ProductProjectiveSpaces([2, 2], GF(3))
        sage: w = random_WehlerK3Surface(PP)
        sage: type(w)
        <class 'sage.dynamics.arithmetic_dynamics.wehlerK3.WehlerK3Surface_finite_field_with_category'>
    """

class WehlerK3Surface_ring(AlgebraicScheme_subscheme_product_projective):
    """
    A K3 surface in `\\mathbb{P}^2 \\times \\mathbb{P}^2` defined as the
    intersection of a bilinear and biquadratic form. [Weh1998]_

    EXAMPLES::

        sage: R.<x,y,z,u,v,w> = PolynomialRing(QQ, 6)
        sage: L = x*u - y*v
        sage: Q = x*y*v^2 + z^2*u*w
        sage: WehlerK3Surface([L, Q])
        Closed subscheme of Product of projective spaces P^2 x P^2 over Rational
        Field defined by:
          x*u - y*v,
          x*y*v^2 + z^2*u*w
    """
    L: Incomplete
    Q: Incomplete
    def __init__(self, polys) -> None: ...
    def change_ring(self, R):
        """
        Changes the base ring on which the Wehler K3 Surface is defined.

        INPUT:

        - ``R`` -- ring

        OUTPUT: K3 Surface defined over input ring

        EXAMPLES::

            sage: PP.<x0,x1,x2,y0,y1,y2> = ProductProjectiveSpaces([2, 2], GF(3))
            sage: L = x0*y0 + x1*y1 - x2*y2
            sage: Q = x0*x1*y1^2 + x2^2*y0*y2
            sage: W = WehlerK3Surface([L, Q])
            sage: W.base_ring()
            Finite Field of size 3
            sage: T = W.change_ring(GF(7))
            sage: T.base_ring()
            Finite Field of size 7
        """
    @cached_method
    def Gpoly(self, component, k):
        """
        Return the G polynomials  `G^*_k`.

        They are defined as:
        `G^*_k = \\left(L^*_j\\right)^2Q^*_{ii}-L^*_iL^*_jQ^*_{ij}+\\left(L^*_i\\right)^2Q^*_{jj}`
        where `(i, j, k)` is some permutation of `(0, 1, 2)` and `*` is either
        `x` (``component=1``) or `y` (``component=0``).

        INPUT:

        - ``component`` -- integer; 0 or 1

        - ``k`` -- integer; 0, 1 or 2

        OUTPUT: polynomial in terms of either `y` (``component=0``) or `x` (``component=1``)

        EXAMPLES::

            sage: R.<x0,x1,x2,y0,y1,y2> = PolynomialRing(ZZ, 6)
            sage: Y = x0*y0 + x1*y1 - x2*y2
            sage: Z = x0^2*y0*y1 + x0^2*y2^2 - x0*x1*y1*y2 + x1^2*y2*y1 \\\n            ....: + x2^2*y2^2 + x2^2*y1^2 + x1^2*y2^2
            sage: X = WehlerK3Surface([Z, Y])
            sage: X.Gpoly(1, 0)
            x0^2*x1^2 + x1^4 - x0*x1^2*x2 + x1^3*x2 + x1^2*x2^2 + x2^4
        """
    @cached_method
    def Hpoly(self, component, i, j):
        """
        Return the H polynomials defined as `H^*_{ij}`.

        This polynomial is defined by:

        `H^*_{ij} = 2L^*_iL^*_jQ^*_{kk}-L^*_iL^*_kQ^*_{jk} - L^*_jL^*_kQ^*_{ik}+\\left(L^*_k\\right)^2Q^*_{ij}`
        where {i, j, k} is some permutation of (0, 1, 2) and * is either y (``component=0``) or x (``component=1``).

        INPUT:

        - ``component`` -- integer; 0 or 1

        - ``i`` -- integer; 0, 1 or 2

        - ``j`` -- integer; 0, 1 or 2

        OUTPUT: polynomial in terms of either y (``component=0``) or x (``component=1``)

        EXAMPLES::

            sage: R.<x0,x1,x2,y0,y1,y2> = PolynomialRing(ZZ, 6)
            sage: Y = x0*y0 + x1*y1 - x2*y2
            sage: Z = x0^2*y0*y1 + x0^2*y2^2 - x0*x1*y1*y2 + x1^2*y2*y1 \\\n            ....: + x2^2*y2^2 + x2^2*y1^2 + x1^2*y2^2
            sage: X = WehlerK3Surface([Z, Y])
            sage: X.Hpoly(0, 1, 0)
             2*y0*y1^3 + 2*y0*y1*y2^2 - y1*y2^3
        """
    def Lxa(self, a):
        """
        Function will return the L polynomial defining the fiber, given by `L^{x}_{a}`.

        This polynomial is defined as:

        `L^{x}_{a} = \\{(a, y) \\in \\mathbb{P}^{2} \\times \\mathbb{P}^{2} \\colon L(a, y) = 0\\}`.

        Notation and definition from: [CS1996]_

        INPUT:

        - ``a`` -- point in `\\mathbb{P}^2`

        OUTPUT: a polynomial representing the fiber

        EXAMPLES::

            sage: PP.<x0,x1,x2,y0,y1,y2> = ProductProjectiveSpaces([2, 2], QQ)
            sage: Z = x0^2*y0^2 + 3*x0*x1*y0^2 + x1^2*y0^2 + 4*x0^2*y0*y1 \\\n            ....: + 3*x0*x1*y0*y1 - 2*x2^2*y0*y1 - \\\n            ....: x0^2*y1^2 + 2*x1^2*y1^2 - x0*x2*y1^2 - 4*x1*x2*y1^2 \\\n            ....: + 5*x0*x2*y0*y2 - 4*x1*x2*y0*y2 + 7*x0^2*y1*y2 \\\n            ....: + 4*x1^2*y1*y2 + x0*x1*y2^2 + 3*x2^2*y2^2
            sage: Y = x0*y0 + x1*y1 + x2*y2
            sage: X = WehlerK3Surface([Z, Y])
            sage: T = PP(1, 1, 0, 1, 0, 0)
            sage: X.Lxa(T[0])
            y0 + y1
        """
    def Qxa(self, a):
        """
        Function will return the Q polynomial defining a fiber given by `Q^{x}_{a}`.

        This polynomial is defined as:

        `Q^{x}_{a} = \\{(a,y) \\in \\mathbb{P}^{2} \\times \\mathbb{P}^{2} \\colon Q(a,y) = 0\\}`.

        Notation and definition from: [CS1996]_

        INPUT:

        - ``a`` -- point in `\\mathbb{P}^2`

        OUTPUT: a polynomial representing the fiber

        EXAMPLES::

           sage: PP.<x0,x1,x2,y0,y1,y2> = ProductProjectiveSpaces([2, 2], QQ)
           sage: Z = x0^2*y0^2 + 3*x0*x1*y0^2 + x1^2*y0^2 + 4*x0^2*y0*y1 + 3*x0*x1*y0*y1 \\\n           ....: - 2*x2^2*y0*y1 - x0^2*y1^2 + 2*x1^2*y1^2 - x0*x2*y1^2 - 4*x1*x2*y1^2 \\\n           ....: + 5*x0*x2*y0*y2 \\\n           ....: - 4*x1*x2*y0*y2 + 7*x0^2*y1*y2 + 4*x1^2*y1*y2 + x0*x1*y2^2 + 3*x2^2*y2^2
           sage: Y = x0*y0 + x1*y1 + x2*y2
           sage: X = WehlerK3Surface([Z, Y])
           sage: T = PP(1, 1, 0, 1, 0, 0)
           sage: X.Qxa(T[0])
           5*y0^2 + 7*y0*y1 + y1^2 + 11*y1*y2 + y2^2
        """
    def Sxa(self, a):
        """
        Function will return fiber by `S^{x}_{a}`.

        This function is defined as:

        `S^{x}_{a} = L^{x}_{a} \\cap Q^{x}_{a}`.

        Notation and definition from: [CS1996]_

        INPUT:

        - ``a`` -- point in `\\mathbb{P}^2`

        OUTPUT: a subscheme representing the fiber

        EXAMPLES::

           sage: PP.<x0,x1,x2,y0,y1,y2> = ProductProjectiveSpaces([2, 2], QQ)
           sage: Z = x0^2*y0^2 + 3*x0*x1*y0^2 + x1^2*y0^2 + 4*x0^2*y0*y1 \\\n           ....: + 3*x0*x1*y0*y1 \\\n           ....: - 2*x2^2*y0*y1 - x0^2*y1^2 + 2*x1^2*y1^2 - x0*x2*y1^2 - 4*x1*x2*y1^2 \\\n           ....: + 5*x0*x2*y0*y2 \\\n           ....: - 4*x1*x2*y0*y2 + 7*x0^2*y1*y2 + 4*x1^2*y1*y2 + x0*x1*y2^2 + 3*x2^2*y2^2
           sage: Y = x0*y0 + x1*y1 + x2*y2
           sage: Y = x0*y0 + x1*y1 + x2*y2
           sage: X = WehlerK3Surface([Z, Y])
           sage: T = PP(1, 1, 0, 1, 0, 0)
           sage: X.Sxa(T[0])
           Closed subscheme of Projective Space of dimension 2 over Rational Field defined by:
             y0 + y1,
             5*y0^2 + 7*y0*y1 + y1^2 + 11*y1*y2 + y2^2
        """
    def Lyb(self, b):
        """
        Function will return a fiber by `L^{y}_{b}`.

        This polynomial is defined as:

        `L^{y}_{b} = \\{(x,b) \\in \\mathbb{P}^{2} \\times \\mathbb{P}^{2} \\colon L(x,b) = 0\\}`.

        Notation and definition from: [CS1996]_

        INPUT:

        - ``b`` -- point in projective space

        OUTPUT: a polynomial representing the fiber

        EXAMPLES::

           sage: PP.<x0,x1,x2,y0,y1,y2> = ProductProjectiveSpaces([2, 2], QQ)
           sage: Z =x0^2*y0^2 + 3*x0*x1*y0^2 + x1^2*y0^2 + 4*x0^2*y0*y1 \\\n           ....: + 3*x0*x1*y0*y1 \\\n           ....: - 2*x2^2*y0*y1 - x0^2*y1^2 + 2*x1^2*y1^2 - x0*x2*y1^2 - 4*x1*x2*y1^2 \\\n           ....: + 5*x0*x2*y0*y2 \\\n           ....: - 4*x1*x2*y0*y2 + 7*x0^2*y1*y2 + 4*x1^2*y1*y2 + x0*x1*y2^2 + 3*x2^2*y2^2
           sage: Y = x0*y0 + x1*y1 + x2*y2
           sage: Y = x0*y0 + x1*y1 + x2*y2
           sage: X = WehlerK3Surface([Z, Y])
           sage: T = PP(1, 1, 0, 1, 0, 0)
           sage: X.Lyb(T[1])
           x0
        """
    def Qyb(self, b):
        """

        Function will return a fiber by `Q^{y}_{b}`.

        This polynomial is defined as:

        `Q^{y}_{b} = \\{(x,b) \\in \\mathbb{P}^{2} \\times \\mathbb{P}^{2} \\colon Q(x,b) = 0\\}`.

        Notation and definition from: [CS1996]_

        INPUT:

        - ``b`` -- point in projective space

        OUTPUT: a polynomial representing the fiber

        EXAMPLES::

            sage: PP.<x0,x1,x2,y0,y1,y2> = ProductProjectiveSpaces([2, 2], QQ)
            sage: Z = x0^2*y0^2 + 3*x0*x1*y0^2 + x1^2*y0^2 + 4*x0^2*y0*y1 \\\n            ....: + 3*x0*x1*y0*y1 - 2*x2^2*y0*y1 - x0^2*y1^2 + 2*x1^2*y1^2 - x0*x2*y1^2 \\\n            ....: - 4*x1*x2*y1^2 + 5*x0*x2*y0*y2 - 4*x1*x2*y0*y2 + 7*x0^2*y1*y2 \\\n            ....: + 4*x1^2*y1*y2 + x0*x1*y2^2 + 3*x2^2*y2^2
            sage: Y = x0*y0 + x1*y1 + x2*y2
            sage: X = WehlerK3Surface([Z, Y])
            sage: T = PP(1, 1, 0, 1, 0, 0)
            sage: X.Qyb(T[1])
            x0^2 + 3*x0*x1 + x1^2
        """
    def Syb(self, b):
        """
        Function will return fiber by `S^{y}_{b}`.

        This function is defined by:

        `S^{y}_{b} = L^{y}_{b} \\cap Q^{y}_{b}`.

        Notation and definition from: [CS1996]_

        INPUT:

        - ``b`` -- point in `\\mathbb{P}^2`

        OUTPUT: a subscheme representing the fiber

        EXAMPLES::

           sage: PP.<x0,x1,x2,y0,y1,y2> = ProductProjectiveSpaces([2, 2], QQ)
           sage: Z = x0^2*y0^2 + 3*x0*x1*y0^2 + x1^2*y0^2 + 4*x0^2*y0*y1 + \\\n           ....: 3*x0*x1*y0*y1 - 2*x2^2*y0*y1 - x0^2*y1^2 + 2*x1^2*y1^2 - x0*x2*y1^2 \\\n           ....: - 4*x1*x2*y1^2 + 5*x0*x2*y0*y2 - 4*x1*x2*y0*y2 + 7*x0^2*y1*y2 \\\n           ....: + 4*x1^2*y1*y2 + x0*x1*y2^2 + 3*x2^2*y2^2
           sage: Y = x0 * y0 + x1 * y1 + x2 * y2
           sage: X = WehlerK3Surface([Z, Y])
           sage: T = PP(1, 1, 0, 1, 0, 0)
           sage: X.Syb(T[1])
           Closed subscheme of Projective Space of dimension 2 over Rational Field defined by:
             x0,
             x0^2 + 3*x0*x1 + x1^2
        """
    def Ramification_poly(self, i):
        """
        Function will return the Ramification polynomial  `g^*`.

        This polynomial is defined by:

        `g^* = \\frac{\\left(H^*_{ij}\\right)^2 - 4G^*_iG^*_j}{\\left(L^*_k\\right)^2}`.

        The roots of this polynomial will either be degenerate fibers or fixed points
        of the involutions `\\sigma_x` or `\\sigma_y` for more information, see [CS1996]_.

        INPUT:

        - ``i`` -- integer; either 0 (polynomial in y) or 1 (polynomial in x)

        OUTPUT: polynomial in the coordinate ring of the ambient space

        EXAMPLES::

            sage: PP.<x0,x1,x2,y0,y1,y2> = ProductProjectiveSpaces([2, 2], QQ)
            sage: Z = (x0^2*y0^2 + 3*x0*x1*y0^2 + x1^2*y0^2 + 4*x0^2*y0*y1 + 3*x0*x1*y0*y1
            ....:      - 2*x2^2*y0*y1 - x0^2*y1^2 + 2*x1^2*y1^2 - x0*x2*y1^2 - 4*x1*x2*y1^2
            ....:      + 5*x0*x2*y0*y2 - 4*x1*x2*y0*y2 + 7*x0^2*y1*y2 + 4*x1^2*y1*y2
            ....:      + x0*x1*y2^2 + 3*x2^2*y2^2)
            sage: Y = x0*y0 + x1*y1 + x2*y2
            sage: X = WehlerK3Surface([Z, Y])
            sage: X.Ramification_poly(0)
            8*y0^5*y1 - 24*y0^4*y1^2 + 48*y0^2*y1^4 - 16*y0*y1^5 + y1^6 + 84*y0^3*y1^2*y2
            + 46*y0^2*y1^3*y2 - 20*y0*y1^4*y2 + 16*y1^5*y2 + 53*y0^4*y2^2 + 56*y0^3*y1*y2^2
            - 32*y0^2*y1^2*y2^2 - 80*y0*y1^3*y2^2 - 92*y1^4*y2^2 - 12*y0^2*y1*y2^3
            - 168*y0*y1^2*y2^3 - 122*y1^3*y2^3 + 14*y0^2*y2^4 + 8*y0*y1*y2^4 - 112*y1^2*y2^4
            + y2^6
        """
    @cached_method
    def is_degenerate(self):
        """
        Function will return ``True`` if there is a fiber (over the algebraic closure of the
        base ring) of dimension greater than 0 and ``False`` otherwise.

        OUTPUT: boolean

        EXAMPLES::

            sage: R.<x0,x1,x2,y0,y1,y2> = PolynomialRing(ZZ, 6)
            sage: Y = x0*y0 + x1*y1 - x2*y2
            sage: Z = x0^2*y0*y1 + x0^2*y2^2 - x0*x1*y1*y2 + x1^2*y2*y1 + x2^2*y2^2 + \\\n            ....: x2^2*y1^2 + x1^2*y2^2
            sage: X = WehlerK3Surface([Z, Y])
            sage: X.is_degenerate()
            True

        ::

            sage: PP.<x0,x1,x2,y0,y1,y2> = ProductProjectiveSpaces([2, 2], QQ)
            sage: Z = x0^2*y0^2 + 3*x0*x1*y0^2 + x1^2*y0^2 + 4*x0^2*y0*y1 + 3*x0*x1*y0*y1 - \\\n            ....: 2*x2^2*y0*y1 - x0^2*y1^2 + 2*x1^2*y1^2 - x0*x2*y1^2 -4*x1*x2*y1^2 + 5*x0*x2*y0*y2 - \\\n            ....: 4*x1*x2*y0*y2 + 7*x0^2*y1*y2 + 4*x1^2*y1*y2 + x0*x1*y2^2 + 3*x2^2*y2^2
            sage: Y = x0*y0 + x1*y1 + x2*y2
            sage: X = WehlerK3Surface([Z, Y])
            sage: X.is_degenerate()
            False

        ::

            sage: PP.<x0,x1,x2,y0,y1,y2> = ProductProjectiveSpaces([2, 2], GF(3))
            sage: Z = x0^2*y0^2 + 3*x0*x1*y0^2 + x1^2*y0^2 + 4*x0^2*y0*y1 + 3*x0*x1*y0*y1 - \\\n            ....: 2*x2^2*y0*y1 - x0^2*y1^2 + 2*x1^2*y1^2 - x0*x2*y1^2 -4*x1*x2*y1^2 + 5*x0*x2*y0*y2 - \\\n            ....: 4*x1*x2*y0*y2 + 7*x0^2*y1*y2 + 4*x1^2*y1*y2 + x0*x1*y2^2 + 3*x2^2*y2^2
            sage: Y = x0*y0 + x1*y1 + x2*y2
            sage: X = WehlerK3Surface([Z, Y])
            sage: X.is_degenerate()
            True
        """
    def degenerate_fibers(self):
        """
        Return the (rational) degenerate fibers of the surface defined over
        the base ring, or the fraction field of the base ring if it is not a field.

        ALGORITHM:

        The criteria for degeneracy by the common vanishing of the polynomials
        ``self.Gpoly(1, 0)``, ``self.Gpoly(1, 1)``, ``self.Gpoly(1, 2)``,
        ``self.Hpoly(1, 0, 1)``, ``self.Hpoly(1, 0, 2)``,
        ``self.Hpoly(1, 1, 2)`` (for the first component), is from Proposition 1.4
        in the following article: [CS1996]_.

        This function finds the common solution through elimination via Groebner bases
        by using the .variety() function on the three affine charts in each component.

        OUTPUT: the output is a list of lists where the elements of lists are
        points in the appropriate projective space.
        The first list is the points whose pullback by the projection to the
        first component (projective space) is dimension greater than 0.
        The second list is points in the second component

        EXAMPLES::

            sage: R.<x0,x1,x2,y0,y1,y2> = PolynomialRing(ZZ, 6)
            sage: Y = x0*y0 + x1*y1 - x2*y2
            sage: Z = x0^2*y0*y1 + x0^2*y2^2 - x0*x1*y1*y2 + x1^2*y2*y1 + x2^2*y2^2\\\n            ....: + x2^2*y1^2 + x1^2*y2^2
            sage: X = WehlerK3Surface([Z, Y])
            sage: X.degenerate_fibers()
            [[], [(1 : 0 : 0)]]

        ::

            sage: PP.<x0,x1,x2,y0,y1,y2> = ProductProjectiveSpaces([2, 2], QQ)
            sage: Z = (x0^2*y0^2 + 3*x0*x1*y0^2 + x1^2*y0^2 + 4*x0^2*y0*y1 + 3*x0*x1*y0*y1
            ....:      - 2*x2^2*y0*y1 - x0^2*y1^2 + 2*x1^2*y1^2 - x0*x2*y1^2 - 4*x1*x2*y1^2
            ....:      + 5*x0*x2*y0*y2 - 4*x1*x2*y0*y2 + 7*x0^2*y1*y2 + 4*x1^2*y1*y2
            ....:      + x0*x1*y2^2 + 3*x2^2*y2^2)
            sage: Y = x0*y0 + x1*y1 + x2*y2
            sage: X = WehlerK3Surface([Z, Y])
            sage: X.degenerate_fibers()
            [[], []]

        ::

            sage: PP.<x0,x1,x2,y0,y1,y2> = ProductProjectiveSpaces([2, 2], QQ)
            sage: R = PP.coordinate_ring()
            sage: l = y0*x0 + y1*x1 + (y0 - y1)*x2
            sage: q = (y1*y0 + y2^2)*x0^2 + ((y0^2 - y2*y1)*x1 + (y0^2 + (y1^2 - y2^2))*x2)*x0 \\\n            ....: + (y2*y0 + y1^2)*x1^2 + (y0^2 + (-y1^2 + y2^2))*x2*x1
            sage: X = WehlerK3Surface([l,q])
            sage: X.degenerate_fibers()
            [[(-1 : 1 : 1), (0 : 0 : 1)], [(-1 : -1 : 1), (0 : 0 : 1)]]
        """
    @cached_method
    def degenerate_primes(self, check: bool = True):
        """
        Determine which primes `p` ``self`` has degenerate fibers over `\\GF{p}`.

        If ``check`` is ``False``, then may return primes that do not have degenerate fibers.
        Raises an error if the surface is degenerate.
        Works only for ``ZZ`` or ``QQ``.

        INPUT:

        - ``check`` -- boolean (default: ``True``); whether the primes are verified

        ALGORITHM:

        `p` is a prime of bad reduction if and only if the defining
        polynomials of ``self`` plus the G and H polynomials have a common
        zero. Or stated another way, `p` is a prime of bad reduction if
        and only if the radical of the ideal defined by the defining
        polynomials of ``self`` plus the G and H polynomials is not
        `(x_0,x_1,\\ldots,x_N)`.  This happens if and only if some
        power of each `x_i` is not in the ideal defined by the
        defining polynomials of ``self`` (with G and H). This last condition
        is what is checked. The lcm of the coefficients of the monomials `x_i` in
        a Groebner basis is computed. This may return extra primes.

        OUTPUT: list of primes

        EXAMPLES::

            sage: R.<x0,x1,x2,y0,y1,y2> = PolynomialRing(QQ, 6)
            sage: L =  y0*x0 + (y1*x1 + y2*x2)
            sage: Q = (2*y0^2 + y2*y0 + (2*y1^2 + y2^2))*x0^2 + ((y0^2 + y1*y0 + \\\n            ....: (y1^2 + 2*y2*y1 + y2^2))*x1 + (2*y1^2 + y2*y1 + y2^2)*x2)*x0 + ((2*y0^2\\\n            ....: + (y1 + 2*y2)*y0 + (2*y1^2 + y2*y1))*x1^2 + ((2*y1 + 2*y2)*y0 + (y1^2 + \\\n            ....: y2*y1 + 2*y2^2))*x2*x1 + (2*y0^2 + y1*y0 + (2*y1^2 + y2^2))*x2^2)
            sage: X = WehlerK3Surface([L, Q])
            sage: X.degenerate_primes()
            [2, 3, 5, 11, 23, 47, 48747691, 111301831]
        """
    def is_smooth(self):
        """
        Function will return the status of the smoothness of the surface.

        ALGORITHM:

        Checks to confirm that all of the 2x2 minors of the Jacobian generated from
        the biquadratic and bilinear forms have no common vanishing points.

        OUTPUT: boolean

        EXAMPLES::

            sage: R.<x0,x1,x2,y0,y1,y2> = PolynomialRing(ZZ, 6)
            sage: Y = x0*y0 + x1*y1 - x2*y2
            sage: Z = x0^2*y0*y1 + x0^2*y2^2 - x0*x1*y1*y2 + x1^2*y2*y1 +\\\n            ....: x2^2*y2^2 + x2^2*y1^2 + x1^2*y2^2
            sage: X = WehlerK3Surface([Z, Y])
            sage: X.is_smooth()
            False

        ::

            sage: PP.<x0,x1,x2,y0,y1,y2> = ProductProjectiveSpaces([2, 2], QQ)
            sage: Z = x0^2*y0^2 + 3*x0*x1*y0^2 + x1^2*y0^2 + 4*x0^2*y0*y1 + \\\n            ....: 3*x0*x1*y0*y1 - 2*x2^2*y0*y1 - x0^2*y1^2 + 2*x1^2*y1^2 - x0*x2*y1^2 \\\n            ....: - 4*x1*x2*y1^2 + 5*x0*x2*y0*y2 - 4*x1*x2*y0*y2 + 7*x0^2*y1*y2 + 4*x1^2*y1*y2 \\\n            ....: + x0*x1*y2^2 + 3*x2^2*y2^2
            sage: Y = x0*y0 + x1*y1 + x2*y2
            sage: X = WehlerK3Surface([Z, Y])
            sage: X.is_smooth()
            True
        """
    def sigmaX(self, P, **kwds):
        '''
        Function returns the involution on the  Wehler K3 surface induced by the double covers.

        In particular, it fixes the projection to the first coordinate and swaps the
        two points in the fiber, i.e. `(x, y) \\to (x, y\')`.
        Note that in the degenerate case, while we can split fiber into pairs of points,
        it is not always possibleto distinguish them, using this algorithm.

        ALGORITHM:

        Refer to Section 6: "An algorithm to compute `\\sigma_x`, `\\sigma_y`, `\\phi`,
        and `\\psi`" in [CS1996FH2015.
        For the degenerate case refer to [FH2015]_.

        INPUT:

        - ``P`` -- a point in `\\mathbb{P}^2 \\times \\mathbb{P}^2`

        kwds:

        - ``check`` -- boolean (default: ``True``); checks to see if point is on the surface

        - ``normalize`` -- boolean (default: ``True``); normalizes the point

        OUTPUT: a point on the K3 surface

        EXAMPLES::

            sage: PP.<x0,x1,x2,y0,y1,y2> = ProductProjectiveSpaces([2, 2], QQ)
            sage: Z = x0^2*y0^2 + 3*x0*x1*y0^2 + x1^2*y0^2 + 4*x0^2*y0*y1 +\\\n            ....: 3*x0*x1*y0*y1 -2*x2^2*y0*y1 - x0^2*y1^2 + 2*x1^2*y1^2 - x0*x2*y1^2 -\\\n            ....: 4*x1*x2*y1^2 + 5*x0*x2*y0*y2 -4*x1*x2*y0*y2 + 7*x0^2*y1*y2 +\\\n            ....: 4*x1^2*y1*y2 + x0*x1*y2^2 + 3*x2^2*y2^2
            sage: Y = x0*y0 + x1*y1 + x2*y2
            sage: X = WehlerK3Surface([Z, Y])
            sage: T = PP(0, 0, 1, 1, 0, 0)
            sage: X.sigmaX(T)
            (0 : 0 : 1 , 0 : 1 : 0)

        degenerate examples::

            sage: PP.<x0,x1,x2,y0,y1,y2> = ProductProjectiveSpaces([2, 2], QQ)
            sage: l = y0*x0 + y1*x1 + (y0 - y1)*x2
            sage: q = (y1*y0)*x0^2 + ((y0^2)*x1 + (y0^2 + (y1^2 - y2^2))*x2)*x0\\\n            ....: + (y2*y0 + y1^2)*x1^2 + (y0^2 + (-y1^2 + y2^2))*x2*x1
            sage: X = WehlerK3Surface([l, q])
            sage: X.sigmaX(X([1, 0, 0, 0, 1, -2]))
            (1 : 0 : 0 , 0 : 1/2 : 1)
            sage: X.sigmaX(X([1, 0, 0, 0, 0, 1]))
            (1 : 0 : 0 , 0 : 0 : 1)
            sage: X.sigmaX(X([-1, 1, 1, -1, -1, 1]))
            (-1 : 1 : 1 , 2 : 2 : 1)
            sage: X.sigmaX(X([0, 0, 1, 1, 1, 0]))
            (0 : 0 : 1 , 1 : 1 : 0)
            sage: X.sigmaX(X([0, 0, 1, 1, 1, 1]))
            (0 : 0 : 1 , -1 : -1 : 1)

        Case where we cannot distinguish the two points::

            sage: PP.<y0,y1,y2,x0,x1,x2>=ProductProjectiveSpaces([2, 2], GF(3))
            sage: l = x0*y0 + x1*y1 + x2*y2
            sage: q = (-3*x0^2*y0^2 + 4*x0*x1*y0^2 - 3*x0*x2*y0^2 - 5*x0^2*y0*y1
            ....:      - 190*x0*x1*y0*y1 - 5*x1^2*y0*y1 + 5*x0*x2*y0*y1 + 14*x1*x2*y0*y1
            ....:      + 5*x2^2*y0*y1 - x0^2*y1^2 - 6*x0*x1*y1^2 - 2*x1^2*y1^2
            ....:      + 2*x0*x2*y1^2 - 4*x2^2*y1^2 + 4*x0^2*y0*y2 - x1^2*y0*y2
            ....:      + 3*x0*x2*y0*y2 + 6*x1*x2*y0*y2 - 6*x0^2*y1*y2 - 4*x0*x1*y1*y2
            ....:      - x1^2*y1*y2 + 51*x0*x2*y1*y2 - 7*x1*x2*y1*y2 - 9*x2^2*y1*y2
            ....:      - x0^2*y2^2 - 4*x0*x1*y2^2 + 4*x1^2*y2^2 - x0*x2*y2^2
            ....:      + 13*x1*x2*y2^2 - x2^2*y2^2)
            sage: X = WehlerK3Surface([l, q])
            sage: P = X([1, 0, 0, 0, 1, 1])
            sage: X.sigmaX(X.sigmaX(P))
            Traceback (most recent call last):
            ...
            ValueError: cannot distinguish points in the degenerate fiber
        '''
    def sigmaY(self, P, **kwds):
        '''
        Return the involution on the Wehler K3 surfaces induced by the double covers.

        In particular, it fixes the projection to the second coordinate and swaps
        the two points in the fiber, i.e. `(x,y) \\to (x\',y)`.
        Note that in the degenerate case, while we can split the fiber into two points,
        it is not always possible to distinguish them, using this algorithm.

        ALGORITHM:

        Refer to Section 6: "An algorithm to compute `\\sigma_x`, `\\sigma_y`, `\\phi`,
        and `\\psi`" in [CS1996]_.
        For the degenerate case refer to [FH2015]_.

        INPUT:

        - ``P`` -- a point in `\\mathbb{P}^2 \\times \\mathbb{P}^2`

        kwds:

        - ``check`` -- boolean (default: ``True``); checks to see if point is on the surface

        - ``normalize`` -- boolean (default: ``True``); normalizes the point

        OUTPUT: a point on the K3 surface

        EXAMPLES::

            sage: PP.<x0,x1,x2,y0,y1,y2> = ProductProjectiveSpaces([2, 2], QQ)
            sage: Z = x0^2*y0^2 + 3*x0*x1*y0^2 + x1^2*y0^2 + 4*x0^2*y0*y1 + \\\n            ....: 3*x0*x1*y0*y1 -2*x2^2*y0*y1 - x0^2*y1^2 + 2*x1^2*y1^2 - x0*x2*y1^2 \\\n            ....: - 4*x1*x2*y1^2 + 5*x0*x2*y0*y2 - 4*x1*x2*y0*y2 + 7*x0^2*y1*y2 + 4*x1^2*y1*y2 \\\n            ....: + x0*x1*y2^2 + 3*x2^2*y2^2
            sage: Y = x0*y0 + x1*y1 + x2*y2
            sage: X = WehlerK3Surface([Z, Y])
            sage: T = PP(0, 0, 1, 1, 0, 0)
            sage: X.sigmaY(T)
            (0 : 0 : 1 , 1 : 0 : 0)

        degenerate examples::

            sage: PP.<x0,x1,x2,y0,y1,y2> = ProductProjectiveSpaces([2, 2], QQ)
            sage: l = y0*x0 + y1*x1 + (y0 - y1)*x2
            sage: q = (y1*y0)*x0^2 + ((y0^2)*x1 + (y0^2 + (y1^2 - y2^2))*x2)*x0 +\\\n            ....: (y2*y0 + y1^2)*x1^2 + (y0^2 + (-y1^2 + y2^2))*x2*x1
            sage: X = WehlerK3Surface([l, q])
            sage: X.sigmaY(X([1, -1, 0 ,-1, -1, 1]))
            (1/10 : -1/10 : 1 , -1 : -1 : 1)
            sage: X.sigmaY(X([0, 0, 1, -1, -1, 1]))
            (-4 : 4 : 1 , -1 : -1 : 1)
            sage: X.sigmaY(X([1, 2, 0, 0, 0, 1]))
            (-3 : -3 : 1 , 0 : 0 : 1)
            sage: X.sigmaY(X([1, 1, 1, 0, 0, 1]))
            (1 : 0 : 0 , 0 : 0 : 1)

        Case where we cannot distinguish the two points::

            sage: PP.<x0,x1,x2,y0,y1,y2>=ProductProjectiveSpaces([2, 2], GF(3))
            sage: l = x0*y0 + x1*y1 + x2*y2
            sage: q = (-3*x0^2*y0^2 + 4*x0*x1*y0^2 - 3*x0*x2*y0^2 - 5*x0^2*y0*y1
            ....:      - 190*x0*x1*y0*y1 - 5*x1^2*y0*y1 + 5*x0*x2*y0*y1 + 14*x1*x2*y0*y1
            ....:      + 5*x2^2*y0*y1 - x0^2*y1^2 - 6*x0*x1*y1^2 - 2*x1^2*y1^2 + 2*x0*x2*y1^2
            ....:      - 4*x2^2*y1^2 + 4*x0^2*y0*y2 - x1^2*y0*y2 + 3*x0*x2*y0*y2
            ....:      + 6*x1*x2*y0*y2 - 6*x0^2*y1*y2 - 4*x0*x1*y1*y2 - x1^2*y1*y2
            ....:      + 51*x0*x2*y1*y2 - 7*x1*x2*y1*y2 - 9*x2^2*y1*y2 - x0^2*y2^2
            ....:      - 4*x0*x1*y2^2 + 4*x1^2*y2^2 - x0*x2*y2^2 + 13*x1*x2*y2^2 - x2^2*y2^2)
            sage: X = WehlerK3Surface([l ,q])
            sage: P = X([0, 1, 1, 1, 0, 0])
            sage: X.sigmaY(X.sigmaY(P))
            Traceback (most recent call last):
            ...
            ValueError: cannot distinguish points in the degenerate fiber
        '''
    def phi(self, a, **kwds):
        '''
        Evaluates the function `\\phi = \\sigma_y \\circ \\sigma_x`.

        ALGORITHM:

        Refer to Section 6: "An algorithm to compute `\\sigma_x`, `\\sigma_y`,
        `\\phi`, and `\\psi`" in [CS1996]_.

        For the degenerate case refer to [FH2015]_.

        INPUT:

        - ``a`` -- point in `\\mathbb{P}^2 \\times \\mathbb{P}^2`

        kwds:

        - ``check`` -- boolean (default: ``True``); checks to see if point is on the surface

        - ``normalize`` -- boolean (default: ``True``); normalizes the point

        OUTPUT: a point on this surface

        EXAMPLES::

            sage: PP.<x0,x1,x2,y0,y1,y2> = ProductProjectiveSpaces([2, 2], QQ)
            sage: Z = x0^2*y0^2 + 3*x0*x1*y0^2 + x1^2*y0^2 + 4*x0^2*y0*y1 + \\\n            ....: 3*x0*x1*y0*y1 -2*x2^2*y0*y1 - x0^2*y1^2 + 2*x1^2*y1^2 - x0*x2*y1^2 \\\n            ....: - 4*x1*x2*y1^2 + 5*x0*x2*y0*y2 -4*x1*x2*y0*y2 + 7*x0^2*y1*y2 + 4*x1^2*y1*y2 \\\n            ....: + x0*x1*y2^2 + 3*x2^2*y2^2
            sage: Y = x0*y0 + x1*y1 + x2*y2
            sage: X = WehlerK3Surface([Z, Y])
            sage: T = PP([0, 0, 1, 1 ,0, 0])
            sage: X.phi(T)
            (-1 : 0 : 1 , 0 : 1 : 0)
        '''
    def psi(self, a, **kwds):
        '''
        Evaluates the function `\\psi = \\sigma_x \\circ \\sigma_y`.

        ALGORITHM:

        Refer to Section 6: "An algorithm to compute `\\sigma_x`, `\\sigma_y`,
        `\\phi`, and `\\psi`" in [CS1996]_.

        For the degenerate case refer to [FH2015]_.

        INPUT:

        - ``a`` -- point in `\\mathbb{P}^2 \\times \\mathbb{P}^2`

        kwds:

        - ``check`` -- boolean (default: ``True``); checks to see if point is on the surface

        - ``normalize`` -- boolean (default: ``True``); normalizes the point

        OUTPUT: a point on this surface

        EXAMPLES::

            sage: PP.<x0,x1,x2,y0,y1,y2> = ProductProjectiveSpaces([2, 2], QQ)
            sage: Z = x0^2*y0^2 + 3*x0*x1*y0^2 + x1^2*y0^2 + 4*x0^2*y0*y1 + \\\n            ....: 3*x0*x1*y0*y1 -2*x2^2*y0*y1 - x0^2*y1^2 + 2*x1^2*y1^2 - x0*x2*y1^2 \\\n            ....: - 4*x1*x2*y1^2 + 5*x0*x2*y0*y2 - 4*x1*x2*y0*y2 + 7*x0^2*y1*y2 + 4*x1^2*y1*y2 \\\n            ....: + x0*x1*y2^2 + 3*x2^2*y2^2
            sage: Y = x0*y0 + x1*y1 + x2*y2
            sage: X = WehlerK3Surface([Z, Y])
            sage: T = PP([0, 0, 1, 1, 0, 0])
            sage: X.psi(T)
            (0 : 0 : 1 , 0 : 1 : 0)
        '''
    def lambda_plus(self, P, v, N, m, n, prec: int = 100):
        """
        Evaluates the  local canonical height plus function of Call-Silverman at
        the place ``v`` for ``P`` with ``N`` terms of the series.

        Use ``v = 0`` for the archimedean place. Must be over `\\ZZ` or `\\QQ`.

        ALGORITHM:

        Sum over local heights using convergent series, for more details,
        see section 4 of [CS1996]_.

        INPUT:

        - ``P`` -- a surface point

        - ``N`` -- positive integer; number of terms of the series to use

        - ``v`` -- nonnegative integer; a place, use v = 0 for the Archimedean place

        - ``m``, ``n`` -- positive integers; we compute the local height for
          the divisor `E_{mn}^{+}`. These must be indices of nonzero
          coordinates of the point ``P``

        - ``prec`` -- (default: 100) float point or `p`-adic precision

        OUTPUT: a real number

        EXAMPLES::

            sage: PP.<x0,x1,x2,y0,y1,y2> = ProductProjectiveSpaces([2, 2], QQ)
            sage: Z = x0^2*y0^2 + 3*x0*x1*y0^2 + x1^2*y0^2 + 4*x0^2*y0*y1 + 3*x0*x1*y0*y1\\\n            ....: - 2*x2^2*y0*y1 - x0^2*y1^2 + 2*x1^2*y1^2 - x0*x2*y1^2 -4*x1*x2*y1^2 + 5*x0*x2*y0*y2\\\n            ....: - 4*x1*x2*y0*y2 + 7*x0^2*y1*y2 + 4*x1^2*y1*y2 + x0*x1*y2^2 + 3*x2^2*y2^2
            sage: Y = x0*y0 + x1*y1 + x2*y2
            sage: X = WehlerK3Surface([Z, Y])
            sage: P = X([0, 0, 1, 1, 0, 0])
            sage: X.lambda_plus(P, 0, 10, 2, 0)
            0.89230705169161608922595928129
        """
    def lambda_minus(self, P, v, N, m, n, prec: int = 100):
        """
        Evaluates the local canonical height minus function of Call-Silverman
        at the place ``v`` for ``P`` with ``N`` terms of the series.

        Use ``v = 0`` for the Archimedean place. Must be over `\\ZZ` or `\\QQ`.

        ALGORITHM:

        Sum over local heights using convergent series, for more details,
        see section 4 of [CS1996]_.

        INPUT:

        - ``P`` -- a projective point

        - ``N`` -- positive integer. number of terms of the series to use

        - ``v`` -- nonnegative integer. a place, use v = 0 for the Archimedean place

        - ``m``, ``n`` -- positive integers; we compute the local height for
          the divisor `E_{mn}^{+}`. These must be indices of nonzero
          coordinates of the point ``P``.

        - ``prec`` -- (default: 100) float point or `p`-adic precision

        OUTPUT: a real number

        EXAMPLES::

            sage: PP.<x0,x1,x2,y0,y1,y2> = ProductProjectiveSpaces([2, 2], QQ)
            sage: Z = x0^2*y0^2 + 3*x0*x1*y0^2 + x1^2*y0^2 + 4*x0^2*y0*y1 + 3*x0*x1*y0*y1 \\\n            ....: - 2*x2^2*y0*y1 - x0^2*y1^2 + 2*x1^2*y1^2 - x0*x2*y1^2 -4*x1*x2*y1^2 + 5*x0*x2*y0*y2\\\n            ....: - 4*x1*x2*y0*y2 + 7*x0^2*y1*y2 + 4*x1^2*y1*y2 + x0*x1*y2^2 + 3*x2^2*y2^2
            sage: Y = x0*y0 + x1*y1 + x2*y2
            sage: X = WehlerK3Surface([Z, Y])
            sage: P = X([0, 0, 1, 1, 0, 0])
            sage: X.lambda_minus(P, 2, 20, 2, 0, 200)
            -0.18573351672047135037172805779671791488351056677474271893705
        """
    def canonical_height_plus(self, P, N, badprimes=None, prec: int = 100):
        """
        Evaluates the canonical height plus function of Call-Silverman
        for ``P`` with ``N`` terms of the series of the local heights.

        Must be over `\\ZZ` or `\\QQ`.

        ALGORITHM:

        Sum over the lambda plus heights (local heights) in a convergent series,
        for more detail see section 7 of [CS1996]_.

        INPUT:

        - ``P`` -- a surface point

        - ``N`` -- positive integer. Number of terms of the series to use

        - ``badprimes`` -- (optional) list of integer primes (where the surface is degenerate)

        - ``prec`` -- (default: 100) float point or `p`-adic precision

        OUTPUT: a real number

        EXAMPLES::

            sage: set_verbose(None)
            sage: R.<x0,x1,x2,y0,y1,y2> = PolynomialRing(QQ, 6)
            sage: L =  (-y0 - y1)*x0 + (-y0*x1 - y2*x2)
            sage: Q = (-y2*y0 - y1^2)*x0^2 + ((-y0^2 - y2*y0 + (-y2*y1 - y2^2))*x1 + \\\n            ....: (-y0^2 - y2*y1)*x2)*x0 + ((-y0^2 - y2*y0 - y2^2)*x1^2 + (-y2*y0 - y1^2)*x2*x1 \\\n            ....: + (-y0^2 + (-y1 - y2)*y0)*x2^2)
            sage: X = WehlerK3Surface([L, Q])
            sage: P = X([1, 0, -1, 1, -1, 0]) #order 16
            sage: X.canonical_height_plus(P, 5)  # long time
            0.00000000000000000000000000000

        Call-Silverman Example::

            sage: set_verbose(None)
            sage: PP.<x0,x1,x2,y0,y1,y2> = ProductProjectiveSpaces([2, 2], QQ)
            sage: Z = x0^2*y0^2 + 3*x0*x1*y0^2 + x1^2*y0^2 + 4*x0^2*y0*y1 + \\\n            ....: 3*x0*x1*y0*y1 - 2*x2^2*y0*y1 - x0^2*y1^2 + 2*x1^2*y1^2 - x0*x2*y1^2 \\\n            ....: - 4*x1*x2*y1^2 + 5*x0*x2*y0*y2 -4*x1*x2*y0*y2 + 7*x0^2*y1*y2 + 4*x1^2*y1*y2 \\\n            ....: + x0*x1*y2^2 + 3*x2^2*y2^2
            sage: Y = x0*y0 + x1*y1 + x2*y2
            sage: X = WehlerK3Surface([Z, Y])
            sage: P = X([0, 1, 0, 0, 0, 1])
            sage: X.canonical_height_plus(P, 4) # long time
            0.14752753298983071394400412161
        """
    def canonical_height_minus(self, P, N, badprimes=None, prec: int = 100):
        """
        Evaluates the canonical height minus function of Call-Silverman
        for ``P`` with ``N`` terms of the series of the local heights.

        Must be over `\\ZZ` or `\\QQ`.

        ALGORITHM:

        Sum over the lambda minus heights (local heights) in a convergent series,
        for more detail see section 7 of [CS1996]_.

        INPUT:

        - ``P`` -- a surface point

        - ``N`` -- positive integer (number of terms of the series to use)

        - ``badprimes`` -- (optional) list of integer primes (where the surface is degenerate)

        - ``prec`` -- (default: 100) float point or `p`-adic precision

        OUTPUT: a real number

        EXAMPLES::

            sage: set_verbose(None)
            sage: R.<x0,x1,x2,y0,y1,y2> = PolynomialRing(QQ, 6)
            sage: L =  (-y0 - y1)*x0 + (-y0*x1 - y2*x2)
            sage: Q = (-y2*y0 - y1^2)*x0^2 + ((-y0^2 - y2*y0 + (-y2*y1 - y2^2))*x1\\\n            ....: + (-y0^2 - y2*y1)*x2)*x0 + ((-y0^2 - y2*y0 - y2^2)*x1^2 + (-y2*y0 - y1^2)*x2*x1\\\n            ....: + (-y0^2 + (-y1 - y2)*y0)*x2^2)
            sage: X = WehlerK3Surface([L, Q])
            sage: P = X([1, 0, -1, 1, -1, 0]) #order 16
            sage: X.canonical_height_minus(P, 5)  # long time
            0.00000000000000000000000000000

        Call-Silverman example::

            sage: set_verbose(None)
            sage: PP.<x0,x1,x2,y0,y1,y2> = ProductProjectiveSpaces([2, 2], QQ)
            sage: Z = x0^2*y0^2 + 3*x0*x1*y0^2 + x1^2*y0^2 + 4*x0^2*y0*y1 +\\\n            ....: 3*x0*x1*y0*y1 - 2*x2^2*y0*y1 - x0^2*y1^2 + 2*x1^2*y1^2 - x0*x2*y1^2 - \\\n            ....: 4*x1*x2*y1^2 + 5*x0*x2*y0*y2 - 4*x1*x2*y0*y2 + 7*x0^2*y1*y2 + 4*x1^2*y1*y2 + \\\n            ....: x0*x1*y2^2 + 3*x2^2*y2^2
            sage: Y = x0*y0 + x1*y1 + x2*y2
            sage: X = WehlerK3Surface([Z, Y])
            sage: P = X([0, 1, 0, 0, 0, 1])
            sage: X.canonical_height_minus(P, 4) # long time
            0.55073705369676788175590206734
        """
    def canonical_height(self, P, N, badprimes=None, prec: int = 100):
        """
        Evaluates the canonical height for ``P`` with ``N`` terms of the series of the local
        heights.

        ALGORITHM:

        The sum of the canonical height minus and canonical height plus,
        for more info see section 4 of [CS1996]_.

        INPUT:

        - ``P`` -- a surface point

        - ``N`` -- positive integer (number of terms of the series to use)

        - ``badprimes`` -- (optional) list of integer primes (where the surface is degenerate)

        - ``prec`` -- (default: 100) float point or `p`-adic precision

        OUTPUT: a real number

        EXAMPLES::

            sage: set_verbose(None)
            sage: R.<x0,x1,x2,y0,y1,y2> = PolynomialRing(QQ, 6)
            sage: L =  (-y0 - y1)*x0 + (-y0*x1 - y2*x2)
            sage: Q = (-y2*y0 - y1^2)*x0^2 + ((-y0^2 - y2*y0 + (-y2*y1 - y2^2))*x1 + \\\n            ....: (-y0^2 - y2*y1)*x2)*x0 + ((-y0^2 - y2*y0 - y2^2)*x1^2 + (-y2*y0 - y1^2)*x2*x1 \\\n            ....: + (-y0^2 + (-y1 - y2)*y0)*x2^2)
            sage: X = WehlerK3Surface([L, Q])
            sage: P = X([1, 0, -1, 1,- 1, 0]) #order 16
            sage: X.canonical_height(P, 5)  # long time
            0.00000000000000000000000000000

        Call-Silverman example::

            sage: set_verbose(None)
            sage: PP.<x0,x1,x2,y0,y1,y2> = ProductProjectiveSpaces([2, 2], QQ)
            sage: Z = x0^2*y0^2 + 3*x0*x1*y0^2 + x1^2*y0^2 + 4*x0^2*y0*y1 + 3*x0*x1*y0*y1 - \\\n            ....: 2*x2^2*y0*y1 - x0^2*y1^2 + 2*x1^2*y1^2 - x0*x2*y1^2 - 4*x1*x2*y1^2 + 5*x0*x2*y0*y2 \\\n            ....: -4*x1*x2*y0*y2 + 7*x0^2*y1*y2 + 4*x1^2*y1*y2 + x0*x1*y2^2 + 3*x2^2*y2^2
            sage: Y = x0*y0 + x1*y1 + x2*y2
            sage: X = WehlerK3Surface([Z, Y])
            sage: P = X(0, 1, 0, 0, 0, 1)
            sage: X.canonical_height(P, 4)
            0.69826458668659859569990618895
        """
    def fiber(self, p, component):
        """
        Return the fibers [y (component = 1) or x (Component = 0)] of
        a point on a K3 Surface.

        This will work for nondegenerate fibers only.

        For algorithm, see [Hutz2007]_.

        INPUT:

        - ``p`` -- a point in `\\mathbb{P}^2`

        OUTPUT: the corresponding fiber (as a list)

        EXAMPLES::

            sage: R.<x0,x1,x2,y0,y1,y2> = PolynomialRing(ZZ, 6)
            sage: Y = x0*y0 + x1*y1 - x2*y2
            sage: Z = y0^2*x0*x1 + y0^2*x2^2 - y0*y1*x1*x2 + y1^2*x2*x1 + y2^2*x2^2 +\\\n            ....: y2^2*x1^2 + y1^2*x2^2
            sage: X = WehlerK3Surface([Z, Y])
            sage: Proj = ProjectiveSpace(QQ, 2)
            sage: P = Proj([1, 0, 0])
            sage: X.fiber(P, 1)
            Traceback (most recent call last):
            ...
            TypeError: fiber is degenerate

        ::

            sage: P.<x0,x1,x2,y0,y1,y2> = ProductProjectiveSpaces([2, 2], QQ)
            sage: Z = x0^2*y0^2 + 3*x0*x1*y0^2 + x1^2*y0^2 + 4*x0^2*y0*y1 + 3*x0*x1*y0*y1 - \\\n            ....: 2*x2^2*y0*y1 - x0^2*y1^2 + 2*x1^2*y1^2 - x0*x2*y1^2 -4*x1*x2*y1^2 + 5*x0*x2*y0*y2 - \\\n            ....: 4*x1*x2*y0*y2 + 7*x0^2*y1*y2 + 4*x1^2*y1*y2 + x0*x1*y2^2 + 3*x2^2*y2^2
            sage: Y = x0*y0 + x1*y1 + x2*y2
            sage: X = WehlerK3Surface([Z, Y])
            sage: Proj = P[0]
            sage: T = Proj([0, 0, 1])
            sage: X.fiber(T, 1)
            [(0 : 0 : 1 , 0 : 1 : 0), (0 : 0 : 1 , 2 : 0 : 0)]

        ::

            sage: PP.<x0,x1,x2,y0,y1,y2> = ProductProjectiveSpaces([2, 2], GF(7))
            sage: L = x0*y0 + x1*y1 - 1*x2*y2
            sage: Q = ((2*x0^2 + x2*x0 + (2*x1^2 + x2^2))*y0^2
            ....:      + ((x0^2 + x1*x0 +(x1^2 + 2*x2*x1 + x2^2))*y1
            ....:         + (2*x1^2 + x2*x1 + x2^2)*y2)*y0
            ....:      + ((2*x0^2 + (x1 + 2*x2)*x0 + (2*x1^2 + x2*x1))*y1^2
            ....:         + ((2*x1 + 2*x2)*x0 + (x1^2 + x2*x1 + 2*x2^2))*y2*y1
            ....:         + (2*x0^2 + x1*x0 + (2*x1^2 + x2^2))*y2^2))
            sage: W = WehlerK3Surface([L, Q])
            sage: W.fiber([4, 0, 1], 0)
            [(0 : 1 : 0 , 4 : 0 : 1), (4 : 0 : 2 , 4 : 0 : 1)]
        """
    def nth_iterate_phi(self, P, n, **kwds):
        """
        Compute the `n`-th iterate for the phi function.

        INPUT:

        - ``P`` -- a point in `\\mathbb{P}^2 \\times \\mathbb{P}^2`

        - ``n`` -- integer

        kwds:

        - ``check`` -- boolean (default: ``True``); checks to see if point is
          on the surface

        - ``normalize`` -- boolean (default: ``False``); normalizes the point

        OUTPUT: the `n`-th iterate of the point given the phi function (if `n`
        is positive), or the psi function (if `n` is negative)

        EXAMPLES::

            sage: PP.<x0,x1,x2,y0,y1,y2> = ProductProjectiveSpaces([2, 2], QQ)
            sage: L = x0*y0 + x1*y1 + x2*y2
            sage: Q = x1^2*y0^2 + 2*x2^2*y0*y1 + x0^2*y1^2 - x0*x1*y2^2
            sage: W = WehlerK3Surface([L, Q])
            sage: T = W([-1, -1, 1, 1, 0, 1])
            sage: W.nth_iterate_phi(T, 7)
            (-1 : 0 : 1 , 1 : -2 : 1)

        ::

            sage: PP.<x0,x1,x2,y0,y1,y2> = ProductProjectiveSpaces([2, 2], QQ)
            sage: L = x0*y0 + x1*y1 + x2*y2
            sage: Q = x1^2*y0^2 + 2*x2^2*y0*y1 + x0^2*y1^2 - x0*x1*y2^2
            sage: W = WehlerK3Surface([L, Q])
            sage: T = W([-1, -1, 1, 1, 0, 1])
            sage: W.nth_iterate_phi(T, -7)
            (1 : 0 : 1 , -1 : 2 : 1)

        ::

            sage: R.<x0,x1,x2,y0,y1,y2>=PolynomialRing(QQ, 6)
            sage: L = (-y0 - y1)*x0 + (-y0*x1 - y2*x2)
            sage: Q = (-y2*y0 - y1^2)*x0^2 + ((-y0^2 - y2*y0 + (-y2*y1 - y2^2))*x1 + (-y0^2 - y2*y1)*x2)*x0 \\\n            ....: + ((-y0^2 - y2*y0 - y2^2)*x1^2 + (-y2*y0 - y1^2)*x2*x1 + (-y0^2 + (-y1 - y2)*y0)*x2^2)
            sage: X = WehlerK3Surface([L, Q])
            sage: P = X([1, 0, -1, 1, -1, 0])
            sage: X.nth_iterate_phi(P, 8) == X.nth_iterate_psi(P, 8)
            True
        """
    def nth_iterate_psi(self, P, n, **kwds):
        """
        Compute the `n`-th iterate for the psi function.

        INPUT:

        - ``P`` -- a point in `\\mathbb{P}^2 \\times \\mathbb{P}^2`

        - ``n`` -- integer

        kwds:

        - ``check`` -- boolean (default: ``True``); checks to see if point is on the surface

        - ``normalize`` -- boolean (default: ``False``); normalizes the point

        OUTPUT: the `n`-th iterate of the point given the psi function (if `n` is positive),
        or the phi function (if `n` is negative)

        EXAMPLES::

            sage: PP.<x0,x1,x2,y0,y1,y2> = ProductProjectiveSpaces([2, 2], QQ)
            sage: L = x0*y0 + x1*y1 + x2*y2
            sage: Q = x1^2*y0^2 + 2*x2^2*y0*y1 + x0^2*y1^2 - x0*x1*y2^2
            sage: W = WehlerK3Surface([L, Q])
            sage: T = W([-1, -1, 1, 1, 0, 1])
            sage: W.nth_iterate_psi(T, -7)
            (-1 : 0 : 1 , 1 : -2 : 1)

        ::

            sage: PP.<x0,x1,x2,y0,y1,y2> = ProductProjectiveSpaces([2, 2], QQ)
            sage: L = x0*y0 + x1*y1 + x2*y2
            sage: Q = x1^2*y0^2 + 2*x2^2*y0*y1 + x0^2*y1^2 - x0*x1*y2^2
            sage: W = WehlerK3Surface([L, Q])
            sage: T = W([-1, -1, 1, 1, 0, 1])
            sage: W.nth_iterate_psi(T, 7)
            (1 : 0 : 1 , -1 : 2 : 1)
        """
    def orbit_phi(self, P, N, **kwds):
        """
        Return the orbit of the `\\phi` function defined by
        `\\phi = \\sigma_y \\circ \\sigma_x`.

        This function is defined in [CS1996]_.

        INPUT:

        - ``P`` -- point on the K3 surface

        - ``N`` -- nonnegative integer or list or tuple of two nonnegative integers

        kwds:

        - ``check`` -- boolean (default: ``True``); checks to see if point is on the surface

        - ``normalize`` -- boolean (default: ``False``); normalizes the point

        OUTPUT: list of points in the orbit

        EXAMPLES::

            sage: PP.<x0,x1,x2,y0,y1,y2> = ProductProjectiveSpaces([2, 2], QQ)
            sage: Z = x0^2*y0^2 + 3*x0*x1*y0^2 + x1^2*y0^2 + 4*x0^2*y0*y1 + \\\n            ....: 3*x0*x1*y0*y1 -2*x2^2*y0*y1 - x0^2*y1^2 + 2*x1^2*y1^2 - x0*x2*y1^2 - \\\n            ....: 4*x1*x2*y1^2 + 5*x0*x2*y0*y2 - 4*x1*x2*y0*y2 + 7*x0^2*y1*y2 + 4*x1^2*y1*y2 + \\\n            ....: x0*x1*y2^2 + 3*x2^2*y2^2
            sage: Y = x0*y0 + x1*y1 + x2*y2
            sage: X = WehlerK3Surface([Z, Y])
            sage: T = PP(0, 0, 1, 1, 0, 0)
            sage: X.orbit_phi(T,2, normalize = True)
            [(0 : 0 : 1 , 1 : 0 : 0), (-1 : 0 : 1 , 0 : 1 : 0), (-12816/6659 : 55413/6659 : 1 , 1 : 1/9 : 1)]
            sage: X.orbit_phi(T,[2,3], normalize = True)
            [(-12816/6659 : 55413/6659 : 1 , 1 : 1/9 : 1),
            (7481279673854775690938629732119966552954626693713001783595660989241/18550615454277582153932951051931712107449915856862264913424670784695
            : 3992260691327218828582255586014718568398539828275296031491644987908/18550615454277582153932951051931712107449915856862264913424670784695 :
            1 , -117756062505511/54767410965117 : -23134047983794359/37466994368025041 : 1)]
        """
    def orbit_psi(self, P, N, **kwds):
        """
        Return the orbit of the `\\psi` function defined by
        `\\psi = \\sigma_x \\circ \\sigma_y`.

        This function is defined in [CS1996]_.

        INPUT:

        - ``P`` -- a point on the K3 surface

        - ``N`` -- nonnegative integer or list or tuple of two nonnegative integers

        kwds:

        - ``check`` -- boolean (default: ``True``); checks to see if point is on the surface

        - ``normalize`` -- boolean (default: ``False``); normalizes the point

        OUTPUT: list of points in the orbit

        EXAMPLES::

            sage: PP.<x0,x1,x2,y0,y1,y2> = ProductProjectiveSpaces([2, 2], QQ)
            sage: Z = x0^2*y0^2 + 3*x0*x1*y0^2 + x1^2*y0^2 + 4*x0^2*y0*y1 + \\\n            ....: 3*x0*x1*y0*y1 -2*x2^2*y0*y1 - x0^2*y1^2 + 2*x1^2*y1^2 - x0*x2*y1^2 - \\\n            ....: 4*x1*x2*y1^2 + 5*x0*x2*y0*y2 -4*x1*x2*y0*y2 + 7*x0^2*y1*y2 + 4*x1^2*y1*y2 + \\\n            ....: x0*x1*y2^2 + 3*x2^2*y2^2
            sage: Y = x0*y0 + x1*y1 + x2*y2
            sage: X = WehlerK3Surface([Z, Y])
            sage: T = X(0, 0, 1, 1, 0, 0)
            sage: X.orbit_psi(T, 2, normalize=True)
            [(0 : 0 : 1 , 1 : 0 : 0), (0 : 0 : 1 , 0 : 1 : 0), (-1 : 0 : 1 , 1 : 1/9 : 1)]
            sage: X.orbit_psi(T,[2,3], normalize=True)
            [(-1 : 0 : 1 , 1 : 1/9 : 1),
            (-12816/6659 : 55413/6659 : 1 , -117756062505511/54767410965117 : -23134047983794359/37466994368025041 : 1)]
        """
    def is_isomorphic(self, right):
        """
        Check to see if two K3 surfaces have the same defining ideal.

        INPUT:

        - ``right`` -- the K3 surface to compare to the original

        OUTPUT: boolean

        EXAMPLES::

            sage: PP.<x0,x1,x2,y0,y1,y2> = ProductProjectiveSpaces([2, 2], QQ)
            sage: Z = x0^2*y0^2 + 3*x0*x1*y0^2 + x1^2*y0^2 + 4*x0^2*y0*y1 + \\\n            ....: 3*x0*x1*y0*y1 -2*x2^2*y0*y1 - x0^2*y1^2 + 2*x1^2*y1^2 - x0*x2*y1^2 \\\n            ....: -4*x1*x2*y1^2 + 5*x0*x2*y0*y2 - 4*x1*x2*y0*y2 + 7*x0^2*y1*y2 + 4*x1^2*y1*y2 \\\n            ....: + x0*x1*y2^2 + 3*x2^2*y2^2
            sage: Y = x0*y0 + x1*y1 + x2*y2
            sage: X = WehlerK3Surface([Z, Y])
            sage: W = WehlerK3Surface([Z + Y^2, Y])
            sage: X.is_isomorphic(W)
            True

        ::

            sage: R.<x,y,z,u,v,w> = PolynomialRing(QQ, 6)
            sage: L = x*u - y*v
            sage: Q = x*y*v^2 + z^2*u*w
            sage: W1 = WehlerK3Surface([L, Q])
            sage: PP.<x0,x1,x2,y0,y1,y2> = ProductProjectiveSpaces([2, 2], QQ)
            sage: L = x0*y0 + x1*y1 + x2*y2
            sage: Q = x1^2*y0^2 + 2*x2^2*y0*y1 + x0^2*y1^2 - x0*x1*y2^2
            sage: W2 = WehlerK3Surface([L, Q])
            sage: W1.is_isomorphic(W2)
            False
        """
    def is_symmetric_orbit(self, orbit):
        """
        Check to see if the orbit is symmetric (i.e. if one of the points on the
        orbit is fixed by '\\sigma_x' or '\\sigma_y').

        INPUT:

        - ``orbit`` -- a periodic cycle of either psi or phi

        OUTPUT: boolean

        EXAMPLES::

            sage: PP.<x0,x1,x2,y0,y1,y2> = ProductProjectiveSpaces([2, 2], GF(7))
            sage: Z = x0^2*y0^2 + 3*x0*x1*y0^2 + x1^2*y0^2 + 4*x0^2*y0*y1 + 3*x0*x1*y0*y1 \\\n            ....: -2*x2^2*y0*y1 - x0^2*y1^2 + 2*x1^2*y1^2 - x0*x2*y1^2 -4*x1*x2*y1^2 + 5*x0*x2*y0*y2 \\\n            ....: -4*x1*x2*y0*y2 + 7*x0^2*y1*y2 + 4*x1^2*y1*y2 + x0*x1*y2^2 + 3*x2^2*y2^2
            sage: Y = x0*y0 + x1*y1 + x2*y2
            sage: X = WehlerK3Surface([Z, Y])
            sage: T = PP([0, 0, 1, 1, 0, 0])
            sage: orbit = X.orbit_psi(T, 4)
            sage: X.is_symmetric_orbit(orbit)
            True

        ::

            sage: PP.<x0,x1,x2,y0,y1,y2> = ProductProjectiveSpaces([2, 2], QQ)
            sage: L = x0*y0 + x1*y1 + x2*y2
            sage: Q = x1^2*y0^2 + 2*x2^2*y0*y1 + x0^2*y1^2 - x0*x1*y2^2
            sage: W = WehlerK3Surface([L, Q])
            sage: T = W([-1, -1, 1, 1, 0, 1])
            sage: Orb = W.orbit_phi(T, 7)
            sage: W.is_symmetric_orbit(Orb)
            False
        """

class WehlerK3Surface_field(WehlerK3Surface_ring): ...

class WehlerK3Surface_finite_field(WehlerK3Surface_field):
    def cardinality(self):
        """
        Count the total number of points on the K3 surface.

        ALGORITHM:

        Enumerate points over `\\mathbb{P}^2`, and then count the points on the fiber of
        each of those points.

        OUTPUT: integer; total number of points on the surface

        EXAMPLES::

            sage: PP.<x0,x1,x2,y0,y1,y2> = ProductProjectiveSpaces([2, 2], GF(7))
            sage: Z = x0^2*y0^2 + 3*x0*x1*y0^2 + x1^2*y0^2 + 4*x0^2*y0*y1 + \\\n            ....: 3*x0*x1*y0*y1 - 2*x2^2*y0*y1 - x0^2*y1^2 + 2*x1^2*y1^2 - x0*x2*y1^2 \\\n            ....: - 4*x1*x2*y1^2 + 5*x0*x2*y0*y2 -4*x1*x2*y0*y2 + 7*x0^2*y1*y2 + 4*x1^2*y1*y2 \\\n            ....: + x0*x1*y2^2 + 3*x2^2*y2^2
            sage: Y = x0*y0 + x1*y1 + x2*y2
            sage: X = WehlerK3Surface([Z, Y])
            sage: X.cardinality()
            55
        """
