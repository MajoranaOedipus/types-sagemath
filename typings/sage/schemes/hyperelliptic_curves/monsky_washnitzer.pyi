from _typeshed import Incomplete
from sage.arith.misc import binomial as binomial
from sage.categories.algebras import Algebras as Algebras
from sage.categories.integral_domains import IntegralDomains as IntegralDomains
from sage.matrix.constructor import matrix as matrix
from sage.misc.cachefunc import cached_method as cached_method
from sage.misc.lazy_import import lazy_import as lazy_import
from sage.misc.misc import newton_method_sizes as newton_method_sizes
from sage.misc.profiler import Profiler as Profiler
from sage.misc.repr import repr_lincomb as repr_lincomb
from sage.modules.free_module import FreeModule as FreeModule
from sage.modules.free_module_element import FreeModuleElement as FreeModuleElement, vector as vector
from sage.modules.module import Module as Module
from sage.rings.infinity import Infinity as Infinity
from sage.rings.integer import Integer as Integer
from sage.rings.integer_ring import ZZ as ZZ
from sage.rings.laurent_series_ring import LaurentSeriesRing as LaurentSeriesRing
from sage.rings.polynomial.polynomial_element import Polynomial as Polynomial
from sage.rings.polynomial.polynomial_ring_constructor import PolynomialRing as PolynomialRing
from sage.rings.power_series_ring import PowerSeriesRing as PowerSeriesRing
from sage.rings.rational import Rational as Rational
from sage.rings.rational_field import QQ as QQ
from sage.schemes.elliptic_curves.constructor import EllipticCurve as EllipticCurve
from sage.schemes.elliptic_curves.ell_generic import EllipticCurve_generic as EllipticCurve_generic
from sage.schemes.hyperelliptic_curves.constructor import HyperellipticCurve as HyperellipticCurve
from sage.schemes.hyperelliptic_curves.hyperelliptic_generic import HyperellipticCurve_generic as HyperellipticCurve_generic
from sage.structure.element import ModuleElement as ModuleElement
from sage.structure.parent import Parent as Parent
from sage.structure.richcmp import richcmp as richcmp
from sage.structure.unique_representation import UniqueRepresentation as UniqueRepresentation

class SpecialCubicQuotientRingElement(ModuleElement):
    """
    An element of a :class:`SpecialCubicQuotientRing`.
    """
    def __init__(self, parent, p0, p1, p2, check: bool = True) -> None:
        """
        Construct the element `p_0 + p_1*x + p_2*x^2`, where
        the `p_i` are polynomials in `T`.

        INPUT:

        - ``parent`` -- a :class:`SpecialCubicQuotientRing`

        - ``p0``, ``p1``, ``p2`` -- coefficients; must be coercible
          into parent.poly_ring()

        - ``check`` -- boolean (default: ``True``); whether to carry
          out coercion

        EXAMPLES::

            sage: B.<t> = PolynomialRing(Integers(125))
            sage: R = monsky_washnitzer.SpecialCubicQuotientRing(t^3 - t + B(1/4))
            sage: from sage.schemes.hyperelliptic_curves.monsky_washnitzer import SpecialCubicQuotientRingElement
            sage: SpecialCubicQuotientRingElement(R, 2, 3, 4)
            (2) + (3)*x + (4)*x^2

        TESTS::

            sage: B.<t> = PolynomialRing(Integers(125))
            sage: R = monsky_washnitzer.SpecialCubicQuotientRing(t^3 - t + B(1/4))
            sage: TestSuite(R).run()
            sage: p = R.create_element(t, t^2 - 2, 3)
            sage: -p
            (124*T) + (124*T^2 + 2)*x + (122)*x^2
        """
    def coeffs(self):
        """
        Return list of three lists of coefficients, corresponding to the
        `x^0`, `x^1`, `x^2` coefficients.

        The lists are zero padded to the same length. The list entries
        belong to the base ring.

        EXAMPLES::

            sage: B.<t> = PolynomialRing(Integers(125))
            sage: R = monsky_washnitzer.SpecialCubicQuotientRing(t^3 - t + B(1/4))
            sage: p = R.create_element(t, t^2 - 2, 3)
            sage: p.coeffs()
            [[0, 1, 0], [123, 0, 1], [3, 0, 0]]
        """
    def __bool__(self) -> bool:
        """
        EXAMPLES::

            sage: B.<t> = PolynomialRing(Integers(125))
            sage: R = monsky_washnitzer.SpecialCubicQuotientRing(t^3 - t + B(1/4))
            sage: x, T = R.gens()
            sage: not x
            False
            sage: not T
            False
            sage: not R.create_element(0, 0, 0)
            True
        """
    def shift(self, n):
        """
        Return this element multiplied by `T^n`.

        EXAMPLES::

            sage: B.<t> = PolynomialRing(Integers(125))
            sage: R = monsky_washnitzer.SpecialCubicQuotientRing(t^3 - t + B(1/4))
            sage: f = R.create_element(2, t, t^2 - 3)
            sage: f
            (2) + (T)*x + (T^2 + 122)*x^2
            sage: f.shift(1)
            (2*T) + (T^2)*x + (T^3 + 122*T)*x^2
            sage: f.shift(2)
            (2*T^2) + (T^3)*x + (T^4 + 122*T^2)*x^2
        """
    def scalar_multiply(self, scalar):
        """
        Multiply this element by a scalar, i.e. just multiply each
        coefficient of `x^j` by the scalar.

        INPUT:

        - ``scalar`` -- either an element of ``base_ring``, or an
          element of ``poly_ring``

        EXAMPLES::

            sage: B.<t> = PolynomialRing(Integers(125))
            sage: R = monsky_washnitzer.SpecialCubicQuotientRing(t^3 - t + B(1/4))
            sage: x, T = R.gens()
            sage: f = R.create_element(2, t, t^2 - 3)
            sage: f
            (2) + (T)*x + (T^2 + 122)*x^2
            sage: f.scalar_multiply(2)
            (4) + (2*T)*x + (2*T^2 + 119)*x^2
            sage: f.scalar_multiply(t)
            (2*T) + (T^2)*x + (T^3 + 122*T)*x^2
        """
    def square(self):
        """
        Return the square of the element.

        EXAMPLES::

            sage: B.<t> = PolynomialRing(Integers(125))
            sage: R = monsky_washnitzer.SpecialCubicQuotientRing(t^3 - t + B(1/4))
            sage: x, T = R.gens()

        ::

            sage: f = R.create_element(1 + 2*t + 3*t^2, 4 + 7*t + 9*t^2, 3 + 5*t + 11*t^2)
            sage: f.square()
            (73*T^5 + 16*T^4 + 38*T^3 + 39*T^2 + 70*T + 120)
            + (121*T^5 + 113*T^4 + 73*T^3 + 8*T^2 + 51*T + 61)*x
            + (18*T^4 + 60*T^3 + 22*T^2 + 108*T + 31)*x^2
        """

class SpecialCubicQuotientRing(UniqueRepresentation, Parent):
    """
    Specialised class for representing the quotient ring
    `R[x,T]/(T - x^3 - ax - b)`, where `R` is an
    arbitrary commutative base ring (in which 2 and 3 are invertible),
    `a` and `b` are elements of that ring.

    Polynomials are represented internally in the form
    `p_0 + p_1 x + p_2 x^2` where the `p_i` are
    polynomials in `T`. Multiplication of polynomials always
    reduces high powers of `x` (i.e. beyond `x^2`) to
    powers of `T`.

    Hopefully this ring is faster than a general quotient ring because
    it uses the special structure of this ring to speed multiplication
    (which is the dominant operation in the frobenius matrix
    calculation). I haven't actually tested this theory though...

    .. TODO::

        Eventually we will want to run this in characteristic 3, so we
        need to: (a) Allow `Q(x)` to contain an `x^2` term, and (b) Remove
        the requirement that 3 be invertible. Currently this is used in
        the Toom-Cook algorithm to speed multiplication.

    EXAMPLES::

        sage: B.<t> = PolynomialRing(Integers(125))
        sage: R = monsky_washnitzer.SpecialCubicQuotientRing(t^3 - t + B(1/4))
        sage: R
        SpecialCubicQuotientRing over Ring of integers modulo 125
        with polynomial T = x^3 + 124*x + 94
        sage: TestSuite(R).run()

    Get generators::

        sage: x, T = R.gens()
        sage: x
        (0) + (1)*x + (0)*x^2
        sage: T
        (T) + (0)*x + (0)*x^2

    Coercions::

        sage: R(7)
        (7) + (0)*x + (0)*x^2

    Create elements directly from polynomials::

        sage: A = R.poly_ring()
        sage: A
        Univariate Polynomial Ring in T over Ring of integers modulo 125
        sage: z = A.gen()
        sage: R.create_element(z^2, z+1, 3)
        (T^2) + (T + 1)*x + (3)*x^2

    Some arithmetic::

        sage: x^3
        (T + 31) + (1)*x + (0)*x^2
        sage: 3 * x**15 * T**2 + x - T
        (3*T^7 + 90*T^6 + 110*T^5 + 20*T^4 + 58*T^3 + 26*T^2 + 124*T) +
        (15*T^6 + 110*T^5 + 35*T^4 + 63*T^2 + 1)*x +
        (30*T^5 + 40*T^4 + 8*T^3 + 38*T^2)*x^2

    Retrieve coefficients (output is zero-padded)::

        sage: x^10
        (3*T^2 + 61*T + 8) + (T^3 + 93*T^2 + 12*T + 40)*x + (3*T^2 + 61*T + 9)*x^2
        sage: (x^10).coeffs()
        [[8, 61, 3, 0], [40, 12, 93, 1], [9, 61, 3, 0]]

    .. TODO::

        write an example checking multiplication of these polynomials
        against Sage's ordinary quotient ring arithmetic. I cannot seem
        to get the quotient ring stuff happening right now...
    """
    def __init__(self, Q, laurent_series: bool = False) -> None:
        """
        Constructor.

        INPUT:

        - ``Q`` -- a polynomial of the form
          `Q(x) = x^3 + ax + b`, where `a`, `b` belong to a ring in which
          2, 3 are invertible.

        - ``laurent_series`` -- boolean (default: ``False``); whether or not to allow
          negative powers of `T`

        EXAMPLES::

            sage: B.<t> = PolynomialRing(Integers(125))
            sage: R = monsky_washnitzer.SpecialCubicQuotientRing(t^3 - t + B(1/4))
            sage: R
            SpecialCubicQuotientRing over Ring of integers modulo 125
            with polynomial T = x^3 + 124*x + 94

        ::

            sage: R = monsky_washnitzer.SpecialCubicQuotientRing(t^3 + 2*t^2 - t + B(1/4))
            Traceback (most recent call last):
            ...
            ValueError: Q (=t^3 + 2*t^2 + 124*t + 94) must be of the form x^3 + ax + b

        ::

            sage: B.<t> = PolynomialRing(Integers(10))
            sage: R = monsky_washnitzer.SpecialCubicQuotientRing(t^3 - t + 1)
            Traceback (most recent call last):
            ...
            ArithmeticError: 2 and 3 must be invertible in the coefficient ring
            (=Ring of integers modulo 10) of Q
        """
    def poly_ring(self):
        """
        Return the underlying polynomial ring in `T`.

        EXAMPLES::

            sage: B.<t> = PolynomialRing(Integers(125))
            sage: R = monsky_washnitzer.SpecialCubicQuotientRing(t^3 - t + B(1/4))
            sage: R.poly_ring()
            Univariate Polynomial Ring in T over Ring of integers modulo 125
        """
    def gens(self) -> tuple:
        """
        Return (x, T) where x and T are the generators of the ring
        (as elements *of this ring*).

        EXAMPLES::

            sage: B.<t> = PolynomialRing(Integers(125))
            sage: R = monsky_washnitzer.SpecialCubicQuotientRing(t^3 - t + B(1/4))
            sage: x, T = R.gens()
            sage: x
            (0) + (1)*x + (0)*x^2
            sage: T
            (T) + (0)*x + (0)*x^2
        """
    create_element: Incomplete
    @cached_method
    def one(self):
        """
        Return the unit of ``self``.

        EXAMPLES::

            sage: B.<t> = PolynomialRing(Integers(125))
            sage: R = monsky_washnitzer.SpecialCubicQuotientRing(t^3 - t + B(1/4))
            sage: R.one()
            (1) + (0)*x + (0)*x^2
        """
    Element = SpecialCubicQuotientRingElement

def transpose_list(input) -> list[list]:
    """
    INPUT:

    - ``input`` -- list of lists, each list of the same length

    OUTPUT: list of lists such that ``output[i][j] = input[j][i]``

    EXAMPLES::

        sage: from sage.schemes.hyperelliptic_curves.monsky_washnitzer import transpose_list
        sage: L = [[1, 2], [3, 4], [5, 6]]
        sage: transpose_list(L)
        [[1, 3, 5], [2, 4, 6]]
    """
def helper_matrix(Q):
    """
    Compute the (constant) matrix used to calculate the linear
    combinations of the `d(x^i y^j)` needed to eliminate the
    negative powers of `y` in the cohomology (i.e., in
    :func:`reduce_negative`).

    INPUT:

    - ``Q`` -- cubic polynomial

    EXAMPLES::

        sage: t = polygen(QQ,'t')
        sage: from sage.schemes.hyperelliptic_curves.monsky_washnitzer import helper_matrix
        sage: helper_matrix(t**3-4*t-691)
        [     64/12891731  -16584/12891731 4297329/12891731]
        [   6219/12891731     -32/12891731    8292/12891731]
        [    -24/12891731    6219/12891731     -32/12891731]
    """
def lift(x):
    """
    Try to call ``x.lift()``, presumably from the `p`-adics to `\\ZZ`.

    If this fails, it assumes the input is a power series, and tries to
    lift it to a power series over `\\QQ`.

    This function is just a very kludgy solution to the problem of
    trying to make the reduction code (below) work over both `\\ZZ_p` and
    `\\ZZ_p[[t]]`.

    EXAMPLES::

        sage: # needs sage.rings.padics
        sage: from sage.schemes.hyperelliptic_curves.monsky_washnitzer import lift
        sage: l = lift(Qp(13)(131)); l
        131
        sage: l.parent()
        Integer Ring
        sage: x = PowerSeriesRing(Qp(17),'x').gen()
        sage: l = lift(4 + 5*x + 17*x**6); l
        4 + 5*t + 17*t^6
        sage: l.parent()
        Power Series Ring in t over Rational Field
    """
def reduce_negative(Q, p, coeffs, offset, exact_form=None):
    """
    Apply cohomology relations to incorporate negative powers of
    `y` into the `y^0` term.

    INPUT:

    - ``p`` -- prime

    - ``Q`` -- cubic polynomial

    - ``coeffs`` -- list of length 3 lists. The
      `i`-th list ``[a, b, c]`` represents
      `y^{2(i - offset)} (a + bx + cx^2) dx/y`.

    - ``offset`` -- nonnegative integer

    OUTPUT:

    The reduction is performed in-place. The output is placed
    in coeffs[offset]. Note that coeffs[i] will be meaningless for i
    offset after this function is finished.

    EXAMPLES::

        sage: R.<x> = Integers(5^3)['x']
        sage: Q = x^3 - x + R(1/4)
        sage: coeffs = [[10, 15, 20], [1, 2, 3], [4, 5, 6], [7, 8, 9]]
        sage: coeffs = [[R.base_ring()(a) for a in row] for row in coeffs]
        sage: monsky_washnitzer.reduce_negative(Q, 5, coeffs, 3)
        sage: coeffs[3]
        [28, 52, 9]

    ::

        sage: R.<x> = Integers(7^3)['x']
        sage: Q = x^3 - x + R(1/4)
        sage: coeffs = [[7, 14, 21], [1, 2, 3], [4, 5, 6], [7, 8, 9]]
        sage: coeffs = [[R.base_ring()(a) for a in row] for row in coeffs]
        sage: monsky_washnitzer.reduce_negative(Q, 7, coeffs, 3)
        sage: coeffs[3]
        [245, 332, 9]
    """
def reduce_positive(Q, p, coeffs, offset, exact_form=None):
    """
    Apply cohomology relations to incorporate positive powers of
    `y` into the `y^0` term.

    INPUT:

    - ``Q`` -- cubic polynomial

    - ``coeffs`` -- list of length 3 lists. The
      `i`-th list [a, b, c] represents
      `y^{2(i - offset)} (a + bx + cx^2) dx/y`.

    - ``offset`` -- nonnegative integer

    OUTPUT:

    The reduction is performed in-place. The output is placed
    in coeffs[offset]. Note that coeffs[i] will be meaningless for i
    offset after this function is finished.

    EXAMPLES::

        sage: R.<x> = Integers(5^3)['x']
        sage: Q = x^3 - x + R(1/4)

    ::

        sage: coeffs = [[1, 2, 3], [10, 15, 20]]
        sage: coeffs = [[R.base_ring()(a) for a in row] for row in coeffs]
        sage: monsky_washnitzer.reduce_positive(Q, 5, coeffs, 0)
        sage: coeffs[0]
        [16, 102, 88]

    ::

        sage: coeffs = [[9, 8, 7], [10, 15, 20]]
        sage: coeffs = [[R.base_ring()(a) for a in row] for row in coeffs]
        sage: monsky_washnitzer.reduce_positive(Q, 5, coeffs, 0)
        sage: coeffs[0]
        [24, 108, 92]
    """
def reduce_zero(Q, coeffs, offset, exact_form=None):
    """
    Apply cohomology relation to incorporate `x^2 y^0` term
    into `x^0 y^0` and `x^1 y^0` terms.

    INPUT:

    - ``Q`` -- cubic polynomial

    - ``coeffs`` -- list of length 3 lists. The
      `i`-th list [a, b, c] represents
      `y^{2(i - offset)} (a + bx + cx^2) dx/y`.

    - ``offset`` -- nonnegative integer

    OUTPUT:

    The reduction is performed in-place. The output is placed
    in coeffs[offset]. This method completely ignores coeffs[i] for i
    != offset.

    EXAMPLES::

        sage: R.<x> = Integers(5^3)['x']
        sage: Q = x^3 - x + R(1/4)
        sage: coeffs = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        sage: coeffs = [[R.base_ring()(a) for a in row] for row in coeffs]
        sage: monsky_washnitzer.reduce_zero(Q, coeffs, 1)
        sage: coeffs[1]
        [6, 5, 0]
    """
def reduce_all(Q, p, coeffs, offset, compute_exact_form: bool = False):
    """
    Apply cohomology relations to reduce all terms to a linear
    combination of `dx/y` and `x dx/y`.

    INPUT:

    - ``Q`` -- cubic polynomial

    - ``coeffs`` -- list of length 3 lists. The
      `i`-th list [a, b, c] represents
      `y^{2(i - offset)} (a + bx + cx^2) dx/y`.

    - ``offset`` -- nonnegative integer

    OUTPUT:

    - ``A``, ``B`` -- pair such that the input differential is
      cohomologous to (A + Bx) dx/y

    .. NOTE::

        The algorithm operates in-place, so the data in coeffs is
        destroyed.

    EXAMPLES::

        sage: R.<x> = Integers(5^3)['x']
        sage: Q = x^3 - x + R(1/4)
        sage: coeffs = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        sage: coeffs = [[R.base_ring()(a) for a in row] for row in coeffs]
        sage: monsky_washnitzer.reduce_all(Q, 5, coeffs, 1)
        (21, 106)
    """
def frobenius_expansion_by_newton(Q, p, M):
    '''
    Compute the action of Frobenius on `dx/y` and on
    `x dx/y`, using Newton\'s method (as suggested in Kedlaya\'s
    paper [Ked2001]_).

    (This function does *not* yet use the cohomology relations - that
    happens afterwards in the "reduction" step.)

    More specifically, it finds `F_0` and `F_1` in
    the quotient ring `R[x, T]/(T - Q(x))`, such that

    .. MATH::

       F(  dx/y) = T^{-r} F0 dx/y, \\text{\\ and\\ } F(x dx/y) = T^{-r} F1 dx/y

    where

    .. MATH::

       r = ( (2M-3)p - 1 )/2.


    (Here `T` is `y^2 = z^{-2}`, and `R` is the
    coefficient ring of `Q`.)

    `F_0` and `F_1` are computed in the
    :class:`SpecialCubicQuotientRing` associated to `Q`, so all powers
    of `x^j` for `j \\geq 3` are reduced to powers of
    `T`.

    INPUT:

    - ``Q`` -- cubic polynomial of the form
      `Q(x) = x^3 + ax + b`, whose coefficient ring is a
      `Z/(p^M)Z`-algebra

    - ``p`` -- residue characteristic of the `p`-adic field

    - ``M`` -- `p`-adic precision of the coefficient ring
      (this will be used to determine the number of Newton iterations)

    OUTPUT:

    - ``F0``, ``F1`` -- elements of
      ``SpecialCubicQuotientRing(Q)``, as described above

    - ``r`` -- nonnegative integer, as described above

    EXAMPLES::

        sage: from sage.schemes.hyperelliptic_curves.monsky_washnitzer import frobenius_expansion_by_newton
        sage: R.<x> = Integers(5^3)[\'x\']
        sage: Q = x^3 - x + R(1/4)
        sage: frobenius_expansion_by_newton(Q,5,3)
        ((25*T^5 + 75*T^3 + 100*T^2 + 100*T + 100) + (5*T^6 + 80*T^5 + 100*T^3
        + 25*T + 50)*x + (55*T^5 + 50*T^4 + 75*T^3 + 25*T^2 + 25*T + 25)*x^2,
        (5*T^8 + 15*T^7 + 95*T^6 + 10*T^5 + 25*T^4 + 25*T^3 + 100*T^2 + 50)
        + (65*T^7 + 55*T^6 + 70*T^5 + 100*T^4 + 25*T^2 + 100*T)*x
        + (15*T^6 + 115*T^5 + 75*T^4 + 100*T^3 + 50*T^2 + 75*T + 75)*x^2, 7)
    '''
def frobenius_expansion_by_series(Q, p, M):
    '''
    Compute the action of Frobenius on `dx/y` and on `x dx/y`, using a
    series expansion.

    (This function computes the same thing as
    frobenius_expansion_by_newton(), using a different method.
    Theoretically the Newton method should be asymptotically faster,
    when the precision gets large. However, in practice, this functions
    seems to be marginally faster for moderate precision, so I\'m
    keeping it here until I figure out exactly why it is faster.)

    (This function does *not* yet use the cohomology relations - that
    happens afterwards in the "reduction" step.)

    More specifically, it finds F0 and F1 in the quotient ring
    `R[x, T]/(T - Q(x))`, such that
    `F(  dx/y) = T^{-r} F0 dx/y`, and
    `F(x dx/y) = T^{-r} F1 dx/y` where
    `r = ( (2M-3)p - 1 )/2`. (Here `T` is `y^2 = z^{-2}`,
    and `R` is the coefficient ring of `Q`.)

    `F_0` and `F_1` are computed in the
    :class:`SpecialCubicQuotientRing` associated to `Q`, so all powers
    of `x^j` for `j \\geq 3` are reduced to powers of
    `T`.

    It uses the sum

    .. MATH::

         F0 = \\sum_{k=0}^{M-2} \\binom{-1/2}{k} p x^{p-1} E^k T^{(M-2-k)p}

    and

    .. MATH::

         F1 = x^p F0,

     where `E = Q(x^p) - Q(x)^p`.

    INPUT:

    - ``Q`` -- cubic polynomial of the form
      `Q(x) = x^3 + ax + b`, whose coefficient ring is a
      `\\ZZ/(p^M)\\ZZ` -algebra

    - ``p`` -- residue characteristic of the `p`-adic field

    - ``M`` -- `p`-adic precision of the coefficient ring
      (this will be used to determine the number of terms in the
      series)

    OUTPUT:

    - ``F0``, ``F1`` -- elements of
      ``SpecialCubicQuotientRing(Q)``, as described above

    - ``r`` -- nonnegative integer, as described above

    EXAMPLES::

        sage: from sage.schemes.hyperelliptic_curves.monsky_washnitzer import frobenius_expansion_by_series
        sage: R.<x> = Integers(5^3)[\'x\']
        sage: Q = x^3 - x + R(1/4)
        sage: frobenius_expansion_by_series(Q,5,3)                                      # needs sage.libs.pari
        ((25*T^5 + 75*T^3 + 100*T^2 + 100*T + 100) + (5*T^6 + 80*T^5 + 100*T^3
        + 25*T + 50)*x + (55*T^5 + 50*T^4 + 75*T^3 + 25*T^2 + 25*T + 25)*x^2,
        (5*T^8 + 15*T^7 + 95*T^6 + 10*T^5 + 25*T^4 + 25*T^3 + 100*T^2 + 50)
        + (65*T^7 + 55*T^6 + 70*T^5 + 100*T^4 + 25*T^2 + 100*T)*x
        + (15*T^6 + 115*T^5 + 75*T^4 + 100*T^3 + 50*T^2 + 75*T + 75)*x^2, 7)
    '''
def adjusted_prec(p, prec):
    """
    Compute how much precision is required in ``matrix_of_frobenius`` to
    get an answer correct to ``prec`` `p`-adic digits.

    The issue is that the algorithm used in
    :func:`matrix_of_frobenius` sometimes performs divisions by `p`,
    so precision is lost during the algorithm.

    The estimate returned by this function is based on Kedlaya's result
    (Lemmas 2 and 3 of [Ked2001]_),
    which implies that if we start with `M` `p`-adic
    digits, the total precision loss is at most
    `1 + \\lfloor \\log_p(2M-3) \\rfloor` `p`-adic
    digits. (This estimate is somewhat less than the amount you would
    expect by naively counting the number of divisions by
    `p`.)

    INPUT:

    - ``p`` -- a prime ``p >= 5``

    - ``prec`` -- integer; desired output precision, ``prec >= 1``

    OUTPUT: adjusted precision (usually slightly more than ``prec``)

    EXAMPLES::

        sage: from sage.schemes.hyperelliptic_curves.monsky_washnitzer import adjusted_prec
        sage: adjusted_prec(5,2)
        3
    """
def matrix_of_frobenius(Q, p, M, trace=None, compute_exact_forms: bool = False):
    """
    Compute the matrix of Frobenius on Monsky-Washnitzer cohomology,
    with respect to the basis `(dx/y, x dx/y)`.

    INPUT:

    - ``Q`` -- cubic polynomial `Q(x) = x^3 + ax + b`
      defining an elliptic curve `E` by
      `y^2 = Q(x)`. The coefficient ring of `Q` should be a
      `\\ZZ/(p^M)\\ZZ`-algebra in which the matrix of
      frobenius will be constructed.

    - ``p`` -- prime >= 5 for which E has good reduction

    - ``M`` -- integer >= 2; `p` -adic precision of the coefficient ring

    - ``trace`` -- (optional) the trace of the matrix, if
      known in advance. This is easy to compute because it is just the
      `a_p` of the curve. If the trace is supplied,
      matrix_of_frobenius will use it to speed the computation (i.e. we
      know the determinant is `p`, so we have two conditions, so
      really only column of the matrix needs to be computed. it is
      actually a little more complicated than that, but that's the basic
      idea.) If trace=None, then both columns will be computed
      independently, and you can get a strong indication of correctness
      by verifying the trace afterwards.

      .. WARNING::

          THE RESULT WILL NOT NECESSARILY BE CORRECT TO M p-ADIC
          DIGITS. If you want prec digits of precision, you need to use
          the function adjusted_prec(), and then you need to reduce the
          answer mod `p^{\\mathrm{prec}}` at the end.

    OUTPUT:

    `2 \\times 2` matrix of Frobenius acting on Monsky-Washnitzer cohomology,
    with entries in the coefficient ring of ``Q``.

    EXAMPLES:

    A simple example::

        sage: p = 5
        sage: prec = 3
        sage: M = monsky_washnitzer.adjusted_prec(p, prec); M
        4
        sage: R.<x> = PolynomialRing(Integers(p**M))
        sage: A = monsky_washnitzer.matrix_of_frobenius(x^3 - x + R(1/4), p, M)
        sage: A
        [340  62]
        [ 70 533]

    But the result is only accurate to ``prec`` digits::

        sage: B = A.change_ring(Integers(p**prec))
        sage: B
        [90 62]
        [70 33]

    Check trace (123 = -2 mod 125) and determinant::

        sage: B.det()
        5
        sage: B.trace()
        123
        sage: EllipticCurve([-1, 1/4]).ap(5)
        -2

    Try using the trace to speed up the calculation::

        sage: A = monsky_washnitzer.matrix_of_frobenius(x^3 - x + R(1/4),
        ....:                                           p, M, -2)
        sage: A
        [ 90  62]
        [320 533]

    Hmmm... it looks different, but that's because the trace of our
    first answer was only -2 modulo `5^3`, not -2 modulo
    `5^5`. So the right answer is::

        sage: A.change_ring(Integers(p**prec))
        [90 62]
        [70 33]

    Check it works with only one digit of precision::

        sage: p = 5
        sage: prec = 1
        sage: M = monsky_washnitzer.adjusted_prec(p, prec)
        sage: R.<x> = PolynomialRing(Integers(p**M))
        sage: A = monsky_washnitzer.matrix_of_frobenius(x^3 - x + R(1/4), p, M)
        sage: A.change_ring(Integers(p))
        [0 2]
        [0 3]

    Here is an example that is particularly badly conditioned for
    using the trace trick::

        sage: # needs sage.libs.pari
        sage: p = 11
        sage: prec = 3
        sage: M = monsky_washnitzer.adjusted_prec(p, prec)
        sage: R.<x> = PolynomialRing(Integers(p**M))
        sage: A = monsky_washnitzer.matrix_of_frobenius(x^3 + 7*x + 8, p, M)
        sage: A.change_ring(Integers(p**prec))
        [1144  176]
        [ 847  185]

    The problem here is that the top-right entry is divisible by 11,
    and the bottom-left entry is divisible by `11^2`. So when
    you apply the trace trick, neither `F(dx/y)` nor
    `F(x dx/y)` is enough to compute the whole matrix to the
    desired precision, even if you try increasing the target precision
    by one. Nevertheless, ``matrix_of_frobenius`` knows
    how to get the right answer by evaluating `F((x+1) dx/y)`
    instead::

        sage: A = monsky_washnitzer.matrix_of_frobenius(x^3 + 7*x + 8, p, M, -2)
        sage: A.change_ring(Integers(p**prec))
        [1144  176]
        [ 847  185]

    The running time is about ``O(p*prec**2)`` (times some logarithmic
    factors), so it is feasible to run on fairly large primes, or
    precision (or both?!?!)::

        sage: # long time, needs sage.libs.pari
        sage: p = 10007
        sage: prec = 2
        sage: M = monsky_washnitzer.adjusted_prec(p, prec)
        sage: R.<x> = PolynomialRing(Integers(p**M))
        sage: A = monsky_washnitzer.matrix_of_frobenius(x^3 - x + R(1/4), p, M)
        sage: B = A.change_ring(Integers(p**prec)); B
        [74311982 57996908]
        [95877067 25828133]
        sage: B.det()
        10007
        sage: B.trace()
        66
        sage: EllipticCurve([-1, 1/4]).ap(10007)
        66

    ::

        sage: # long time, needs sage.libs.pari
        sage: p = 5
        sage: prec = 300
        sage: M = monsky_washnitzer.adjusted_prec(p, prec)
        sage: R.<x> = PolynomialRing(Integers(p**M))
        sage: A = monsky_washnitzer.matrix_of_frobenius(x^3 - x + R(1/4), p, M)
        sage: B = A.change_ring(Integers(p**prec))
        sage: B.det()
        5
        sage: -B.trace()
        2
        sage: EllipticCurve([-1, 1/4]).ap(5)
        -2

    Let us check consistency of the results for a range of precisions::

        sage: # long time, needs sage.libs.pari
        sage: p = 5
        sage: max_prec = 60
        sage: M = monsky_washnitzer.adjusted_prec(p, max_prec)
        sage: R.<x> = PolynomialRing(Integers(p**M))
        sage: A = monsky_washnitzer.matrix_of_frobenius(x^3 - x + R(1/4), p, M)
        sage: A = A.change_ring(Integers(p**max_prec))
        sage: result = []
        sage: for prec in range(1, max_prec):
        ....:     M = monsky_washnitzer.adjusted_prec(p, prec)
        ....:     R.<x> = PolynomialRing(Integers(p^M),'x')
        ....:     B = monsky_washnitzer.matrix_of_frobenius(x^3 - x + R(1/4), p, M)
        ....:     B = B.change_ring(Integers(p**prec))
        ....:     result.append(B == A.change_ring(Integers(p**prec)))
        sage: result == [True] * (max_prec - 1)
        True

    The remaining examples discuss what happens when you take the
    coefficient ring to be a power series ring; i.e. in effect you're
    looking at a family of curves.

    The code does in fact work...

    ::

        sage: # needs sage.libs.pari
        sage: p = 11
        sage: prec = 3
        sage: M = monsky_washnitzer.adjusted_prec(p, prec)
        sage: S.<t> = PowerSeriesRing(Integers(p**M), default_prec=4)
        sage: a = 7 + t + 3*t^2
        sage: b = 8 - 6*t + 17*t^2
        sage: R.<x> = PolynomialRing(S)
        sage: Q = x**3 + a*x + b
        sage: A = monsky_washnitzer.matrix_of_frobenius(Q, p, M)            # long time
        sage: B = A.change_ring(PowerSeriesRing(Integers(p**prec), 't',     # long time
        ....:                                   default_prec=4)); B
        [1144 + 264*t + 841*t^2 + 1025*t^3 + O(t^4)  176 + 1052*t + 216*t^2 + 523*t^3 + O(t^4)]
        [   847 + 668*t + 81*t^2 + 424*t^3 + O(t^4)   185 + 341*t + 171*t^2 + 642*t^3 + O(t^4)]

    The trace trick should work for power series rings too, even in the
    badly-conditioned case. Unfortunately I do not know how to compute
    the trace in advance, so I am not sure exactly how this would help.
    Also, I suspect the running time will be dominated by the
    expansion, so the trace trick will not really speed things up anyway.
    Another problem is that the determinant is not always p::

        sage: B.det()                                               # long time
        11 + 484*t^2 + 451*t^3 + O(t^4)

    However, it appears that the determinant always has the property
    that if you substitute t - 11t, you do get the constant series p
    (mod p\\*\\*prec). Similarly for the trace. And since the parameter
    only really makes sense when it is divisible by p anyway, perhaps
    this is not a problem after all.
    """
def matrix_of_frobenius_hyperelliptic(Q, p=None, prec=None, M=None):
    """
    Compute the matrix of Frobenius on Monsky-Washnitzer cohomology,
    with respect to the basis `(dx/2y, x dx/2y, ...x^{d-2} dx/2y)`, where
    `d` is the degree of `Q`.

    INPUT:

    - ``Q`` -- monic polynomial `Q(x)`

    - ``p`` -- prime `\\geq 5` for which `E` has good reduction

    - ``prec`` -- (optional) `p`-adic precision of the coefficient ring

    - ``M`` -- (optional) adjusted `p`-adic precision of the coefficient ring

    OUTPUT:

    `(d-1)` x `(d-1)` matrix `M` of Frobenius on Monsky-Washnitzer cohomology,
    and list of differentials \\{f_i \\} such that

    .. MATH::

        \\phi^* (x^i dx/2y) = df_i + M[i]*vec(dx/2y, ..., x^{d-2} dx/2y)

    EXAMPLES::

        sage: # needs sage.rings.padics
        sage: p = 5
        sage: prec = 3
        sage: R.<x> = QQ['x']
        sage: A,f = monsky_washnitzer.matrix_of_frobenius_hyperelliptic(x^5 - 2*x + 3, p, prec)
        sage: A
        [            4*5 + O(5^3)       5 + 2*5^2 + O(5^3) 2 + 3*5 + 2*5^2 + O(5^3)     2 + 5 + 5^2 + O(5^3)]
        [      3*5 + 5^2 + O(5^3)             3*5 + O(5^3)             4*5 + O(5^3)         2 + 5^2 + O(5^3)]
        [    4*5 + 4*5^2 + O(5^3)     3*5 + 2*5^2 + O(5^3)       5 + 3*5^2 + O(5^3)     2*5 + 2*5^2 + O(5^3)]
        [            5^2 + O(5^3)       5 + 4*5^2 + O(5^3)     4*5 + 3*5^2 + O(5^3)             2*5 + O(5^3)]
    """

class SpecialHyperellipticQuotientElement(ModuleElement):
    """
    Element in the Hyperelliptic quotient ring.

    EXAMPLES::

        sage: R.<x> = QQ['x']
        sage: E = HyperellipticCurve(x^5 - 36*x + 1)
        sage: x,y = E.monsky_washnitzer_gens()
        sage: MW = x.parent()
        sage: MW(x + x**2 + y - 77)
        -(77-y)*1 + x + x^2
    """
    def __init__(self, parent, val: int = 0, offset: int = 0, check: bool = True) -> None:
        """
        Elements in the Hyperelliptic quotient ring.

        EXAMPLES::

            sage: R.<x> = QQ['x']
            sage: E = HyperellipticCurve(x^5 - 36*x + 1)
            sage: x,y = E.monsky_washnitzer_gens()
            sage: MW = x.parent()
            sage: elt = MW(x + x**2 + y - 77)
            sage: TestSuite(elt).run()
        """
    def change_ring(self, R):
        """
        Return the same element after changing the base ring to `R`.

        EXAMPLES::

            sage: R.<x> = QQ['x']
            sage: E = HyperellipticCurve(x^5 - 36*x + 1)
            sage: x,y = E.monsky_washnitzer_gens()
            sage: MW = x.parent()
            sage: z = MW(x + x**2 + y - 77)
            sage: z.change_ring(AA).parent()                                            # needs sage.rings.number_field
            SpecialHyperellipticQuotientRing K[x,y,y^-1] / (y^2 = x^5 - 36*x + 1)
            over Algebraic Real Field
        """
    def __call__(self, *x):
        """
        Evaluate ``self`` at given arguments.

        EXAMPLES::

            sage: R.<x> = QQ['x']
            sage: E = HyperellipticCurve(x^5 - 36*x + 1)
            sage: x,y = E.monsky_washnitzer_gens()
            sage: MW = x.parent()
            sage: z = MW(x + x**2 + y - 77); z
            -(77-y)*1 + x + x^2
            sage: z(66)
            4345 + y
            sage: z(5,4)
            -43
        """
    def __invert__(self):
        """
        Return the inverse of ``self``.

        The general element in our ring is not invertible, but `y` may
        be. We do not want to pass to the fraction field.

        EXAMPLES::

            sage: R.<x> = QQ['x']
            sage: E = HyperellipticCurve(x^5 - 36*x + 1)
            sage: x,y = E.monsky_washnitzer_gens()
            sage: MW = x.parent()
            sage: z = y**(-1)  # indirect doctest
            sage: z.parent()
            SpecialHyperellipticQuotientRing K[x,y,y^-1] / (y^2 = x^5 - 36*x + 1)
            over Rational Field

            sage: z = (x+y)**(-1)  # indirect doctest
            Traceback (most recent call last):
            ...
            ZeroDivisionError: element not invertible
        """
    def __bool__(self) -> bool:
        """
        Return ``True`` iff ``self`` is not zero.

        EXAMPLES::

            sage: R.<x> = QQ['x']
            sage: E = HyperellipticCurve(x^5 - 3*x + 1)
            sage: x,y = E.monsky_washnitzer_gens()
            sage: bool(x)
            True
        """
    def __eq__(self, other):
        """
        Return ``True`` iff ``self`` is equal to ``other``.

        EXAMPLES::

            sage: R.<x> = QQ['x']
            sage: E = HyperellipticCurve(x^5 - 3*x + 1)
            sage: x,y = E.monsky_washnitzer_gens()
            sage: x == y  # indirect doctest
            False
        """
    def __lshift__(self, k):
        """
        Return the left shift of ``self`` by `k`.

        EXAMPLES::

            sage: R.<x> = QQ['x']
            sage: E = HyperellipticCurve(x^5 - 3*x + 1)
            sage: x,y = E.monsky_washnitzer_gens()
            sage: x.__lshift__(3)
            y^3*x
        """
    def __rshift__(self, k):
        """
        Return the right shift of ``self`` by `k`.

        EXAMPLES::

            sage: R.<x> = QQ['x']
            sage: E = HyperellipticCurve(x^5 - 3*x + 1)
            sage: x,y = E.monsky_washnitzer_gens()
            sage: y.__rshift__(3)
            (y^-2)*1
        """
    def truncate_neg(self, n):
        """
        Return ``self`` minus its terms of degree less than `n` wrt `y`.

        EXAMPLES::

            sage: R.<x> = QQ['x']
            sage: E = HyperellipticCurve(x^5 - 3*x + 1)
            sage: x,y = E.monsky_washnitzer_gens()
            sage: (x + 3*y + 7*x*2*y**4).truncate_neg(1)
            3*y*1 + 14*y^4*x
        """
    def diff(self):
        """
        Return the differential of ``self``.

        EXAMPLES::

            sage: R.<x> = QQ['x']
            sage: E = HyperellipticCurve(x^5 - 3*x + 1)
            sage: x,y = E.monsky_washnitzer_gens()
            sage: (x + 3*y).diff()
            (-(9-2*y)*1 + 15*x^4) dx/2y
        """
    def extract_pow_y(self, k):
        """
        Return the coefficients of `y^k` in ``self`` as a list.

        EXAMPLES::

            sage: R.<x> = QQ['x']
            sage: E = HyperellipticCurve(x^5 - 3*x + 1)
            sage: x,y = E.monsky_washnitzer_gens()
            sage: (x + 3*y + 9*x*y).extract_pow_y(1)
            [3, 9, 0, 0, 0]
        """
    def min_pow_y(self):
        """
        Return the minimal degree of ``self`` with respect to `y`.

        EXAMPLES::

            sage: R.<x> = QQ['x']
            sage: E = HyperellipticCurve(x^5 - 3*x + 1)
            sage: x,y = E.monsky_washnitzer_gens()
            sage: (x + 3*y).min_pow_y()
            0
        """
    def max_pow_y(self):
        """
        Return the maximal degree of ``self`` with respect to `y`.

        EXAMPLES::

            sage: R.<x> = QQ['x']
            sage: E = HyperellipticCurve(x^5 - 3*x + 1)
            sage: x,y = E.monsky_washnitzer_gens()
            sage: (x + 3*y).max_pow_y()
            1
        """
    def coeffs(self, R=None):
        """
        Return the raw coefficients of this element.

        INPUT:

        - ``R`` -- an (optional) base-ring in which to cast the coefficients

        OUTPUT:

        - ``coeffs`` -- list of coefficients of powers of `x` for each power
          of `y`

        - ``n`` -- an offset indicating the power of `y` of the first list
          element

        EXAMPLES::

            sage: R.<x> = QQ['x']
            sage: E = HyperellipticCurve(x^5 - 3*x + 1)
            sage: x,y = E.monsky_washnitzer_gens()
            sage: x.coeffs()
            ([(0, 1, 0, 0, 0)], 0)
            sage: y.coeffs()
            ([(0, 0, 0, 0, 0), (1, 0, 0, 0, 0)], 0)

            sage: a = sum(n*x^n for n in range(5)); a
            x + 2*x^2 + 3*x^3 + 4*x^4
            sage: a.coeffs()
            ([(0, 1, 2, 3, 4)], 0)
            sage: a.coeffs(Qp(7))                                                       # needs sage.rings.padics
            ([(0, 1 + O(7^20), 2 + O(7^20), 3 + O(7^20), 4 + O(7^20))], 0)
            sage: (a*y).coeffs()
            ([(0, 0, 0, 0, 0), (0, 1, 2, 3, 4)], 0)
            sage: (a*y^-2).coeffs()
            ([(0, 1, 2, 3, 4), (0, 0, 0, 0, 0), (0, 0, 0, 0, 0)], -2)

        Note that the coefficient list is transposed compared to how they
        are stored and printed::

            sage: a*y^-2
            (y^-2)*x + (2*y^-2)*x^2 + (3*y^-2)*x^3 + (4*y^-2)*x^4

        A more complicated example::

            sage: a = x^20*y^-3 - x^11*y^2; a
            (y^-3-4*y^-1+6*y-4*y^3+y^5)*1 - (12*y^-3-36*y^-1+36*y+y^2-12*y^3-2*y^4+y^6)*x
             + (54*y^-3-108*y^-1+54*y+6*y^2-6*y^4)*x^2 - (108*y^-3-108*y^-1+9*y^2)*x^3
             + (81*y^-3)*x^4
            sage: raw, offset = a.coeffs()
            sage: a.min_pow_y()
            -3
            sage: offset
            -3
            sage: raw
            [(1, -12, 54, -108, 81),
             (0, 0, 0, 0, 0),
             (-4, 36, -108, 108, 0),
             (0, 0, 0, 0, 0),
             (6, -36, 54, 0, 0),
             (0, -1, 6, -9, 0),
             (-4, 12, 0, 0, 0),
             (0, 2, -6, 0, 0),
             (1, 0, 0, 0, 0),
             (0, -1, 0, 0, 0)]
            sage: sum(c * x^i * y^(j+offset)
            ....:     for j, L in enumerate(raw) for i, c in enumerate(L)) == a
            True

        Can also be used to construct elements::

            sage: a.parent()(raw, offset) == a
            True
        """

class SpecialHyperellipticQuotientRing(UniqueRepresentation, Parent):
    """
    The special hyperelliptic quotient ring.
    """
    def __init__(self, Q, R=None, invert_y: bool = True) -> None:
        """
        Initialize ``self``.

        TESTS::

            sage: R.<x> = QQ['x']
            sage: E = HyperellipticCurve(x^5 - 3*x + 1)
            sage: from sage.schemes.hyperelliptic_curves.monsky_washnitzer import SpecialHyperellipticQuotientRing
            sage: HQR = SpecialHyperellipticQuotientRing(E)
            sage: TestSuite(HQR).run()                                                  # needs sage.rings.real_interval_field

        Check that caching works::

            sage: HQR is SpecialHyperellipticQuotientRing(E)
            True
        """
    def base_extend(self, R):
        """
        Return the base extension of ``self`` to the ring ``R`` if possible.

        EXAMPLES::

            sage: R.<x> = QQ['x']
            sage: E = HyperellipticCurve(x^5 - 3*x + 1)
            sage: x,y = E.monsky_washnitzer_gens()
            sage: x.parent().base_extend(UniversalCyclotomicField())                    # needs sage.libs.gap
            SpecialHyperellipticQuotientRing K[x,y,y^-1] / (y^2 = x^5 - 3*x + 1)
            over Universal Cyclotomic Field
            sage: x.parent().base_extend(ZZ)
            Traceback (most recent call last):
            ...
            TypeError: no such base extension
        """
    def change_ring(self, R):
        """
        Return the analog of ``self`` over the ring ``R``.

        EXAMPLES::

            sage: R.<x> = QQ['x']
            sage: E = HyperellipticCurve(x^5 - 3*x + 1)
            sage: x,y = E.monsky_washnitzer_gens()
            sage: x.parent().change_ring(ZZ)
            SpecialHyperellipticQuotientRing K[x,y,y^-1] / (y^2 = x^5 - 3*x + 1)
            over Integer Ring
        """
    @cached_method
    def one(self):
        """
        Return the unit of ``self``.

        EXAMPLES::

            sage: R.<x> = QQ['x']
            sage: E = HyperellipticCurve(x^5 - 3*x + 1)
            sage: x,y = E.monsky_washnitzer_gens()
            sage: x.parent().one()
            1
        """
    @cached_method
    def zero(self):
        """
        Return the zero of ``self``.

        EXAMPLES::

            sage: R.<x> = QQ['x']
            sage: E = HyperellipticCurve(x^5 - 3*x + 1)
            sage: x,y = E.monsky_washnitzer_gens()
            sage: x.parent().zero()
            0
        """
    def gens(self) -> tuple:
        """
        Return the generators of ``self``.

        EXAMPLES::

            sage: R.<x> = QQ['x']
            sage: E = HyperellipticCurve(x^5 - 3*x + 1)
            sage: x,y = E.monsky_washnitzer_gens()
            sage: x.parent().gens()
            (x, y*1)
        """
    def x(self):
        """
        Return the generator `x` of ``self``.

        EXAMPLES::

            sage: R.<x> = QQ['x']
            sage: E = HyperellipticCurve(x^5 - 3*x + 1)
            sage: x,y = E.monsky_washnitzer_gens()
            sage: x.parent().x()
            x
        """
    def y(self):
        """
        Return the generator `y` of ``self``.

        EXAMPLES::

            sage: R.<x> = QQ['x']
            sage: E = HyperellipticCurve(x^5 - 3*x + 1)
            sage: x,y = E.monsky_washnitzer_gens()
            sage: x.parent().y()
            y*1
        """
    def monomial(self, i, j, b=None):
        """
        Return `b y^j x^i`, computed quickly.

        EXAMPLES::

            sage: R.<x> = QQ['x']
            sage: E = HyperellipticCurve(x^5 - 3*x + 1)
            sage: x,y = E.monsky_washnitzer_gens()
            sage: x.parent().monomial(4,5)
            y^5*x^4
        """
    def monomial_diff_coeffs(self, i, j):
        '''
        Compute coefficients of the basis representation of `d(x^iy^j)`.

        The key here is that the formula for `d(x^iy^j)` is messy
        in terms of `i`, but varies nicely with `j`.

        .. MATH::

             d(x^iy^j) = y^{j-1} (2ix^{i-1}y^2 + j (A_i(x) + B_i(x)y^2)) \\frac{dx}{2y},

        where `A,B` have degree at most `n-1` for each
        `i`. Pre-compute `A_i, B_i` for each `i`
        the "hard" way, and the rest are easy.

        EXAMPLES::

            sage: R.<x> = QQ[\'x\']
            sage: E = HyperellipticCurve(x^5 - 3*x + 1)
            sage: x,y = E.monsky_washnitzer_gens()
            sage: x.parent().monomial_diff_coeffs(2,3)
            ((0, -15, 36, 0, 0), (0, 19, 0, 0, 0))
        '''
    def monomial_diff_coeffs_matrices(self):
        """
        Compute tables of coefficients of the basis representation
        of `d(x^iy^j)` for small `i`, `j`.

        EXAMPLES::

            sage: R.<x> = QQ['x']
            sage: E = HyperellipticCurve(x^5 - 3*x + 1)
            sage: x,y = E.monsky_washnitzer_gens()
            sage: x.parent().monomial_diff_coeffs_matrices()
            (
            [0 5 0 0 0]  [0 2 0 0 0]
            [0 0 5 0 0]  [0 0 4 0 0]
            [0 0 0 5 0]  [0 0 0 6 0]
            [0 0 0 0 5]  [0 0 0 0 8]
            [0 0 0 0 0], [0 0 0 0 0]
            )
        """
    def Q(self):
        """
        Return the defining polynomial of the underlying hyperelliptic curve.

        EXAMPLES::

            sage: R.<x> = QQ['x']
            sage: E = HyperellipticCurve(x^5-2*x+1)
            sage: x,y = E.monsky_washnitzer_gens()
            sage: x.parent().Q()
            x^5 - 2*x + 1
        """
    def curve(self):
        """
        Return the underlying hyperelliptic curve.

        EXAMPLES::

            sage: R.<x> = QQ['x']
            sage: E = HyperellipticCurve(x^5 - 3*x + 1)
            sage: x,y = E.monsky_washnitzer_gens()
            sage: x.parent().curve()
            Hyperelliptic Curve over Rational Field defined by y^2 = x^5 - 3*x + 1
        """
    def degree(self):
        """
        Return the degree of the underlying hyperelliptic curve.

        EXAMPLES::

            sage: R.<x> = QQ['x']
            sage: E = HyperellipticCurve(x^5 - 3*x + 1)
            sage: x,y = E.monsky_washnitzer_gens()
            sage: x.parent().degree()
            5
        """
    def prime(self):
        """
        Return the stored prime number `p`.

        EXAMPLES::

            sage: R.<x> = QQ['x']
            sage: E = HyperellipticCurve(x^5 - 3*x + 1)
            sage: x,y = E.monsky_washnitzer_gens()
            sage: x.parent().prime() is None
            True
        """
    def monsky_washnitzer(self):
        """
        Return the stored Monsky-Washnitzer differential ring.

        EXAMPLES::

            sage: R.<x> = QQ['x']
            sage: E = HyperellipticCurve(x^5 - 3*x + 1)
            sage: x,y = E.monsky_washnitzer_gens()
            sage: type(x.parent().monsky_washnitzer())
            <class 'sage.schemes.hyperelliptic_curves.monsky_washnitzer.MonskyWashnitzerDifferentialRing_with_category'>
        """
    def is_field(self, proof: bool = True) -> bool:
        """
        Return ``False`` as ``self`` is not a field.

        EXAMPLES::

            sage: R.<x> = QQ['x']
            sage: E = HyperellipticCurve(x^5 - 3*x + 1)
            sage: x,y = E.monsky_washnitzer_gens()
            sage: x.parent().is_field()
            False
        """
    Element = SpecialHyperellipticQuotientElement
SpecialHyperellipticQuotientRing_class = SpecialHyperellipticQuotientRing

class MonskyWashnitzerDifferential(ModuleElement):
    """
    An element of the Monsky-Washnitzer ring of differentials, of
    the form `F dx/2y`.

    EXAMPLES::

        sage: R.<x> = QQ['x']
        sage: C = HyperellipticCurve(x^5 - 4*x + 4)
        sage: x,y = C.monsky_washnitzer_gens()
        sage: MW = C.invariant_differential().parent()
        sage: MW(x)
        x dx/2y
        sage: MW(y)
        y*1 dx/2y
        sage: MW(x, 10)
        y^10*x dx/2y
    """
    def __init__(self, parent, val, offset: int = 0) -> None:
        """
        Initialize ``self``.

        INPUT:

        - ``parent`` -- Monsky-Washnitzer differential ring (instance of class
          :class:`~MonskyWashnitzerDifferentialRing`

        - ``val`` -- element of the base ring, or list of coefficients

        - ``offset`` -- (default: 0) if nonzero, shift val by `y^\\text{offset}`

        EXAMPLES::

            sage: R.<x> = QQ['x']
            sage: C = HyperellipticCurve(x^5 - 4*x + 4)
            sage: x,y = C.monsky_washnitzer_gens()
            sage: MW = C.invariant_differential().parent()
            sage: elt = MW(x)
            sage: TestSuite(elt).run()
        """
    def __neg__(self):
        """
        Return the additive inverse of ``self``.

        EXAMPLES::

            sage: R.<x> = QQ['x']
            sage: C = HyperellipticCurve(x^5 - 4*x + 4)
            sage: x,y = C.monsky_washnitzer_gens()
            sage: w = C.invariant_differential()
            sage: -w
            -1 dx/2y
            sage: -((y-x)*w)
            (-y*1 + x) dx/2y
        """
    def coeff(self):
        """
        Return `A`, where this element is `A dx/2y`.

        EXAMPLES::

            sage: R.<x> = QQ['x']
            sage: C = HyperellipticCurve(x^5 - 4*x + 4)
            sage: x,y = C.monsky_washnitzer_gens()
            sage: w = C.invariant_differential()
            sage: w
            1 dx/2y
            sage: w.coeff()
            1
            sage: (x*y*w).coeff()
            y*x
        """
    def __bool__(self) -> bool:
        """
        EXAMPLES::

            sage: R.<x> = QQ['x']
            sage: C = HyperellipticCurve(x^5 - 4*x + 4)
            sage: x,y = C.monsky_washnitzer_gens()
            sage: w = C.invariant_differential()
            sage: not w
            False
            sage: not 0*w
            True
            sage: not x*y*w
            False
        """
    def extract_pow_y(self, k):
        """
        Return the power of `y` in `A` where ``self`` is `A dx/2y`.

        EXAMPLES::

            sage: R.<x> = QQ['x']
            sage: C = HyperellipticCurve(x^5 - 3*x + 1)
            sage: x,y = C.monsky_washnitzer_gens()
            sage: A = y^5 - x*y^3
            sage: A.extract_pow_y(5)
            [1, 0, 0, 0, 0]
            sage: (A * C.invariant_differential()).extract_pow_y(5)
            [1, 0, 0, 0, 0]
        """
    def min_pow_y(self):
        """
        Return the minimum power of `y` in `A` where ``self`` is `A dx/2y`.

        EXAMPLES::

            sage: R.<x> = QQ['x']
            sage: C = HyperellipticCurve(x^5 - 3*x + 1)
            sage: x,y = C.monsky_washnitzer_gens()
            sage: w = y^5 * C.invariant_differential()
            sage: w.min_pow_y()
            5
            sage: w = (x^2*y^4 + y^5) * C.invariant_differential()
            sage: w.min_pow_y()
            4
        """
    def max_pow_y(self):
        """
        Return the maximum power of `y` in `A` where ``self`` is `A dx/2y`.

        EXAMPLES::

            sage: R.<x> = QQ['x']
            sage: C = HyperellipticCurve(x^5 - 3*x + 1)
            sage: x,y = C.monsky_washnitzer_gens()
            sage: w = y^5 * C.invariant_differential()
            sage: w.max_pow_y()
            5
            sage: w = (x^2*y^4 + y^5) * C.invariant_differential()
            sage: w.max_pow_y()
            5
        """
    def reduce_neg_y(self):
        """
        Use homology relations to eliminate negative powers of `y`.

        EXAMPLES::

            sage: R.<x> = QQ['x']
            sage: C = HyperellipticCurve(x^5 - 3*x + 1)
            sage: x,y = C.monsky_washnitzer_gens()
            sage: (y^-1).diff().reduce_neg_y()
            ((y^-1)*1, 0 dx/2y)
            sage: (y^-5*x^2+y^-1*x).diff().reduce_neg_y()
            ((y^-1)*x + (y^-5)*x^2, 0 dx/2y)
        """
    def reduce_neg_y_fast(self, even_degree_only: bool = False):
        """
        Use homology relations to eliminate negative powers of `y`.

        EXAMPLES::

            sage: R.<x> = QQ['x']
            sage: E = HyperellipticCurve(x^5 - 3*x + 1)
            sage: x, y = E.monsky_washnitzer_gens()
            sage: (y^-1).diff().reduce_neg_y_fast()
            ((y^-1)*1, 0 dx/2y)
            sage: (y^-5*x^2+y^-1*x).diff().reduce_neg_y_fast()
            ((y^-1)*x + (y^-5)*x^2, 0 dx/2y)

        It leaves nonnegative powers of `y` alone::

            sage: y.diff()
            (-3*1 + 5*x^4) dx/2y
            sage: y.diff().reduce_neg_y_fast()
            (0, (-3*1 + 5*x^4) dx/2y)
        """
    def reduce_neg_y_faster(self, even_degree_only: bool = False):
        """
        Use homology relations to eliminate negative powers of `y`.

        EXAMPLES::

            sage: R.<x> = QQ['x']
            sage: C = HyperellipticCurve(x^5 - 3*x + 1)
            sage: x,y = C.monsky_washnitzer_gens()
            sage: (y^-1).diff().reduce_neg_y()
            ((y^-1)*1, 0 dx/2y)
            sage: (y^-5*x^2+y^-1*x).diff().reduce_neg_y_faster()
            ((y^-1)*x + (y^-5)*x^2, 0 dx/2y)
        """
    def reduce_pos_y(self):
        """
        Use homology relations to eliminate positive powers of `y`.

        EXAMPLES::

            sage: R.<x> = QQ['x']
            sage: C = HyperellipticCurve(x^3-4*x+4)
            sage: x,y = C.monsky_washnitzer_gens()
            sage: (y^2).diff().reduce_pos_y()
            (y^2*1, 0 dx/2y)
            sage: (y^2*x).diff().reduce_pos_y()
            (y^2*x, 0 dx/2y)
            sage: (y^92*x).diff().reduce_pos_y()
            (y^92*x, 0 dx/2y)
            sage: w = (y^3 + x).diff()
            sage: w += w.parent()(x)
            sage: w.reduce_pos_y_fast()
            (y^3*1 + x, x dx/2y)
        """
    def reduce_pos_y_fast(self, even_degree_only: bool = False):
        """
        Use homology relations to eliminate positive powers of `y`.

        EXAMPLES::

            sage: R.<x> = QQ['x']
            sage: E = HyperellipticCurve(x^3 - 4*x + 4)
            sage: x, y = E.monsky_washnitzer_gens()
            sage: y.diff().reduce_pos_y_fast()
            (y*1, 0 dx/2y)
            sage: (y^2).diff().reduce_pos_y_fast()
            (y^2*1, 0 dx/2y)
            sage: (y^2*x).diff().reduce_pos_y_fast()
            (y^2*x, 0 dx/2y)
            sage: (y^92*x).diff().reduce_pos_y_fast()
            (y^92*x, 0 dx/2y)
            sage: w = (y^3 + x).diff()
            sage: w += w.parent()(x)
            sage: w.reduce_pos_y_fast()
            (y^3*1 + x, x dx/2y)
        """
    def reduce(self):
        """
        Use homology relations to find `a` and `f` such that this element is
        equal to `a + df`, where `a` is given in terms of the `x^i dx/2y`.

        EXAMPLES::

            sage: R.<x> = QQ['x']
            sage: C = HyperellipticCurve(x^5 - 4*x + 4)
            sage: x,y = C.monsky_washnitzer_gens()
            sage: w = (y*x).diff()
            sage: w.reduce()
            (y*x, 0 dx/2y)

            sage: w = x^4 * C.invariant_differential()
            sage: w.reduce()
            (1/5*y*1, 4/5*1 dx/2y)

            sage: w = sum(QQ.random_element() * x^i * y^j
            ....:         for i in [0..4] for j in [-3..3]) * C.invariant_differential()
            sage: f, a = w.reduce()
            sage: f.diff() + a - w
            0 dx/2y
        """
    def reduce_fast(self, even_degree_only: bool = False):
        """
        Use homology relations to find `a` and `f` such that this element is
        equal to `a + df`, where `a` is given in terms of the `x^i dx/2y`.

        EXAMPLES::

            sage: R.<x> = QQ['x']
            sage: E = HyperellipticCurve(x^3 - 4*x + 4)
            sage: x, y = E.monsky_washnitzer_gens()
            sage: x.diff().reduce_fast()
            (x, (0, 0))
            sage: y.diff().reduce_fast()
            (y*1, (0, 0))
            sage: (y^-1).diff().reduce_fast()
            ((y^-1)*1, (0, 0))
            sage: (y^-11).diff().reduce_fast()
            ((y^-11)*1, (0, 0))
            sage: (x*y^2).diff().reduce_fast()
            (y^2*x, (0, 0))
        """
    def coeffs(self, R=None):
        """
        Used to obtain the raw coefficients of a differential, see
        :meth:`SpecialHyperellipticQuotientElement.coeffs`

        INPUT:

        - ``R`` -- an (optional) base ring in which to cast the coefficients

        OUTPUT: the raw coefficients of `A` where ``self`` is `A dx/2y`

        EXAMPLES::

            sage: R.<x> = QQ['x']
            sage: C = HyperellipticCurve(x^5 - 4*x + 4)
            sage: x,y = C.monsky_washnitzer_gens()
            sage: w = C.invariant_differential()
            sage: w.coeffs()
            ([(1, 0, 0, 0, 0)], 0)
            sage: (x*w).coeffs()
            ([(0, 1, 0, 0, 0)], 0)
            sage: (y*w).coeffs()
            ([(0, 0, 0, 0, 0), (1, 0, 0, 0, 0)], 0)
            sage: (y^-2*w).coeffs()
            ([(1, 0, 0, 0, 0), (0, 0, 0, 0, 0), (0, 0, 0, 0, 0)], -2)
        """
    def coleman_integral(self, P, Q):
        """
        Compute the definite integral of ``self`` from `P` to `Q`.

        INPUT:

        - `P`, `Q` -- two points on the underlying curve

        OUTPUT: `\\int_P^Q \\text{self}`

        EXAMPLES::

            sage: K = pAdicField(5,7)
            sage: E = EllipticCurve(K,[-31/3,-2501/108]) #11a
            sage: P = E(K(14/3), K(11/2))
            sage: w = E.invariant_differential()
            sage: w.coleman_integral(P, 2*P)
            O(5^6)

            sage: Q = E([3,58332])
            sage: w.coleman_integral(P,Q)
            2*5 + 4*5^2 + 3*5^3 + 4*5^4 + 3*5^5 + O(5^6)
            sage: w.coleman_integral(2*P,Q)
            2*5 + 4*5^2 + 3*5^3 + 4*5^4 + 3*5^5 + O(5^6)
            sage: (2*w).coleman_integral(P, Q) == 2*(w.coleman_integral(P, Q))
            True
        """
    integrate = coleman_integral

class MonskyWashnitzerDifferentialRing(UniqueRepresentation, Module):
    """
    A ring of Monsky--Washnitzer differentials over ``base_ring``.
    """
    def __init__(self, base_ring) -> None:
        """
        Initialize ``self``.

        TESTS::

            sage: R.<x> = QQ['x']
            sage: E = HyperellipticCurve(x^5 - 3*x + 1)
            sage: from sage.schemes.hyperelliptic_curves.monsky_washnitzer import SpecialHyperellipticQuotientRing, MonskyWashnitzerDifferentialRing
            sage: S = SpecialHyperellipticQuotientRing(E)
            sage: DR = MonskyWashnitzerDifferentialRing(S)
            sage: TestSuite(DR).run()                                                   # needs sage.rings.real_interval_field

        Check that caching works::

            sage: DR is MonskyWashnitzerDifferentialRing(S)
            True
        """
    def invariant_differential(self):
        """
        Return `dx/2y` as an element of ``self``.

        EXAMPLES::

            sage: R.<x> = QQ['x']
            sage: C = HyperellipticCurve(x^5 - 4*x + 4)
            sage: MW = C.invariant_differential().parent()
            sage: MW.invariant_differential()
            1 dx/2y
        """
    def base_extend(self, R):
        """
        Return a new differential ring which is ``self`` base-extended to `R`.

        INPUT:

        - ``R`` -- ring

        OUTPUT:

        Self, base-extended to `R`.

        EXAMPLES::

            sage: R.<x> = QQ['x']
            sage: C = HyperellipticCurve(x^5 - 4*x + 4)
            sage: MW = C.invariant_differential().parent()
            sage: MW.base_ring()
            SpecialHyperellipticQuotientRing K[x,y,y^-1] / (y^2 = x^5 - 4*x + 4)
             over Rational Field
            sage: MW.base_extend(Qp(5,5)).base_ring()                                   # needs sage.rings.padics
            SpecialHyperellipticQuotientRing K[x,y,y^-1] / (y^2 = (1 + O(5^5))*x^5
                        + (1 + 4*5 + 4*5^2 + 4*5^3 + 4*5^4 + O(5^5))*x + 4 + O(5^5))
             over 5-adic Field with capped relative precision 5
        """
    def change_ring(self, R):
        """
        Return a new differential ring which is ``self`` with the coefficient
        ring changed to `R`.

        INPUT:

        - ``R`` -- ring of coefficients

        OUTPUT: ``self`` with the coefficient ring changed to `R`

        EXAMPLES::

            sage: R.<x> = QQ['x']
            sage: C = HyperellipticCurve(x^5 - 4*x + 4)
            sage: MW = C.invariant_differential().parent()
            sage: MW.base_ring()
            SpecialHyperellipticQuotientRing K[x,y,y^-1] / (y^2 = x^5 - 4*x + 4)
             over Rational Field
            sage: MW.change_ring(Qp(5,5)).base_ring()                                   # needs sage.rings.padics
            SpecialHyperellipticQuotientRing K[x,y,y^-1] / (y^2 = (1 + O(5^5))*x^5
                        + (1 + 4*5 + 4*5^2 + 4*5^3 + 4*5^4 + O(5^5))*x + 4 + O(5^5))
             over 5-adic Field with capped relative precision 5
        """
    def degree(self):
        """
        Return the degree of `Q(x)`, where the model of the underlying
        hyperelliptic curve of ``self`` is given by `y^2 = Q(x)`.

        EXAMPLES::

            sage: R.<x> = QQ['x']
            sage: C = HyperellipticCurve(x^5 - 4*x + 4)
            sage: MW = C.invariant_differential().parent()
            sage: MW.Q()
            x^5 - 4*x + 4
            sage: MW.degree()
            5
        """
    def dimension(self):
        """
        Return the dimension of ``self``.

        EXAMPLES::

            sage: # needs sage.rings.padics
            sage: R.<x> = QQ['x']
            sage: C = HyperellipticCurve(x^5 - 4*x + 4)
            sage: K = Qp(7,5)
            sage: CK = C.change_ring(K)
            sage: MW = CK.invariant_differential().parent()
            sage: MW.dimension()
            4
        """
    def Q(self):
        """
        Return `Q(x)` where the model of the underlying hyperelliptic curve
        of ``self`` is given by `y^2 = Q(x)`.

        EXAMPLES::

            sage: R.<x> = QQ['x']
            sage: C = HyperellipticCurve(x^5 - 4*x + 4)
            sage: MW = C.invariant_differential().parent()
            sage: MW.Q()
            x^5 - 4*x + 4
        """
    @cached_method
    def x_to_p(self, p):
        """
        Return and cache `x^p`, reduced via the relations coming from the
        defining polynomial of the hyperelliptic curve.

        EXAMPLES::

            sage: R.<x> = QQ['x']
            sage: C = HyperellipticCurve(x^5 - 4*x + 4)
            sage: MW = C.invariant_differential().parent()
            sage: MW.x_to_p(3)
            x^3
            sage: MW.x_to_p(5)
            -(4-y^2)*1 + 4*x
            sage: MW.x_to_p(101) is MW.x_to_p(101)
            True
        """
    @cached_method
    def frob_Q(self, p):
        """
        Return and cache `Q(x^p)`, which is used in computing the image of
        `y` under a `p`-power lift of Frobenius to `A^{\\dagger}`.

        EXAMPLES::

            sage: R.<x> = QQ['x']
            sage: C = HyperellipticCurve(x^5 - 4*x + 4)
            sage: MW = C.invariant_differential().parent()
            sage: MW.frob_Q(3)
            -(60-48*y^2+12*y^4-y^6)*1 + (192-96*y^2+12*y^4)*x - (192-48*y^2)*x^2 + 60*x^3
            sage: MW.Q()(MW.x_to_p(3))                                                  # needs sage.rings.real_interval_field
            -(60-48*y^2+12*y^4-y^6)*1 + (192-96*y^2+12*y^4)*x - (192-48*y^2)*x^2 + 60*x^3
            sage: MW.frob_Q(11) is MW.frob_Q(11)
            True
        """
    def frob_invariant_differential(self, prec, p):
        """
        Kedlaya's algorithm allows us to calculate the action of Frobenius on
        the Monsky-Washnitzer cohomology. First we lift `\\phi` to `A^{\\dagger}`
        by setting

        .. MATH::

            \\phi(x) = x^p,
            \\qquad\\qquad
            \\phi(y) = y^p \\sqrt{1  + \\frac{Q(x^p) - Q(x)^p}{Q(x)^p}}.

        Pulling back the differential `dx/2y`, we get

        .. MATH::

           \\phi^*(dx/2y) = px^{p-1} y(\\phi(y))^{-1} dx/2y
           = px^{p-1} y^{1-p} \\sqrt{1+ \\frac{Q(x^p) - Q(x)^p}{Q(x)^p}} dx/2y.

        Use Newton's method to calculate the square root.

        EXAMPLES::

            sage: R.<x> = QQ['x']
            sage: C = HyperellipticCurve(x^5 - 4*x + 4)
            sage: prec = 2
            sage: p = 7
            sage: MW = C.invariant_differential().parent()
            sage: MW.frob_invariant_differential(prec, p)
            ((67894400*y^-20-81198880*y^-18+40140800*y^-16-10035200*y^-14+1254400*y^-12-62720*y^-10)*1
             - (119503944*y^-20-116064242*y^-18+43753472*y^-16-7426048*y^-14+514304*y^-12-12544*y^-10+1568*y^-8-70*y^-6-7*y^-4)*x
             + (78905288*y^-20-61014016*y^-18+16859136*y^-16-2207744*y^-14+250880*y^-12-37632*y^-10+3136*y^-8-70*y^-6)*x^2
             - (39452448*y^-20-26148752*y^-18+8085490*y^-16-2007040*y^-14+376320*y^-12-37632*y^-10+1568*y^-8)*x^3
             + (21102144*y^-20-18120592*y^-18+8028160*y^-16-2007040*y^-14+250880*y^-12-12544*y^-10)*x^4) dx/2y
        """
    def frob_basis_elements(self, prec, p):
        """
        Return the action of a `p`-power lift of Frobenius on the basis.

        .. MATH::

            \\{ dx/2y, x dx/2y, ..., x^{d-2} dx/2y \\},

        where `d` is the degree of the underlying hyperelliptic curve.

        EXAMPLES::

            sage: R.<x> = QQ['x']
            sage: C = HyperellipticCurve(x^5 - 4*x + 4)
            sage: prec = 1
            sage: p = 5
            sage: MW = C.invariant_differential().parent()
            sage: MW.frob_basis_elements(prec, p)
            [((92000*y^-14-74200*y^-12+32000*y^-10-8000*y^-8+1000*y^-6-50*y^-4)*1
              - (194400*y^-14-153600*y^-12+57600*y^-10-9600*y^-8+600*y^-6)*x
              + (204800*y^-14-153600*y^-12+38400*y^-10-3200*y^-8)*x^2
              - (153600*y^-14-76800*y^-12+9600*y^-10)*x^3
              + (63950*y^-14-18550*y^-12+1600*y^-10-400*y^-8+50*y^-6+5*y^-4)*x^4) dx/2y,
             (-(1391200*y^-14-941400*y^-12+302000*y^-10-76800*y^-8+14400*y^-6-1320*y^-4+30*y^-2)*1
              + (2168800*y^-14-1402400*y^-12+537600*y^-10-134400*y^-8+16800*y^-6-720*y^-4)*x
              - (1596800*y^-14-1433600*y^-12+537600*y^-10-89600*y^-8+5600*y^-6)*x^2
              + (1433600*y^-14-1075200*y^-12+268800*y^-10-22400*y^-8)*x^3
              - (870200*y^-14-445350*y^-12+63350*y^-10-3200*y^-8+600*y^-6-30*y^-4-5*y^-2)*x^4) dx/2y,
             ((19488000*y^-14-15763200*y^-12+4944400*y^-10-913800*y^-8+156800*y^-6-22560*y^-4+1480*y^-2-10)*1
              - (28163200*y^-14-18669600*y^-12+5774400*y^-10-1433600*y^-8+268800*y^-6-25440*y^-4+760*y^-2)*x
              + (15062400*y^-14-12940800*y^-12+5734400*y^-10-1433600*y^-8+179200*y^-6-8480*y^-4)*x^2
              - (12121600*y^-14-11468800*y^-12+4300800*y^-10-716800*y^-8+44800*y^-6)*x^3
              + (9215200*y^-14-6952400*y^-12+1773950*y^-10-165750*y^-8+5600*y^-6-720*y^-4+10*y^-2+5)*x^4) dx/2y,
             (-(225395200*y^-14-230640000*y^-12+91733600*y^-10-18347400*y^-8+2293600*y^-6-280960*y^-4+31520*y^-2-1480-10*y^2)*1
              + (338048000*y^-14-277132800*y^-12+89928000*y^-10-17816000*y^-8+3225600*y^-6-472320*y^-4+34560*y^-2-720)*x
              - (172902400*y^-14-141504000*y^-12+58976000*y^-10-17203200*y^-8+3225600*y^-6-314880*y^-4+11520*y^-2)*x^2
              + (108736000*y^-14-109760000*y^-12+51609600*y^-10-12902400*y^-8+1612800*y^-6-78720*y^-4)*x^3
              - (85347200*y^-14-82900000*y^-12+31251400*y^-10-5304150*y^-8+367350*y^-6-8480*y^-4+760*y^-2+10-5*y^2)*x^4) dx/2y]
        """
    @cached_method
    def helper_matrix(self):
        """
        We use this to solve for the linear combination of
        `x^i y^j` needed to clear all terms with `y^{j-1}`.

        EXAMPLES::

            sage: R.<x> = QQ['x']
            sage: C = HyperellipticCurve(x^5 - 4*x + 4)
            sage: MW = C.invariant_differential().parent()
            sage: MW.helper_matrix()
            [ 256/2101  320/2101  400/2101  500/2101  625/2101]
            [-625/8404  -64/2101  -80/2101 -100/2101 -125/2101]
            [-125/2101 -625/8404  -64/2101  -80/2101 -100/2101]
            [-100/2101 -125/2101 -625/8404  -64/2101  -80/2101]
            [ -80/2101 -100/2101 -125/2101 -625/8404  -64/2101]
        """
    Element = MonskyWashnitzerDifferential
MonskyWashnitzerDifferentialRing_class = MonskyWashnitzerDifferentialRing
