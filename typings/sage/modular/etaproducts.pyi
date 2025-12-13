from _typeshed import Incomplete
from sage.arith.misc import divisors as divisors, euler_phi as euler_phi, gcd as gcd, is_square as is_square, prime_divisors as prime_divisors
from sage.categories.groups import Groups as Groups
from sage.matrix.constructor import matrix as matrix
from sage.modules.free_module import FreeModule as FreeModule
from sage.rings.finite_rings.integer_mod import Mod as Mod
from sage.rings.finite_rings.integer_mod_ring import IntegerModRing as IntegerModRing
from sage.rings.integer import Integer as Integer
from sage.rings.integer_ring import ZZ as ZZ
from sage.rings.polynomial.polynomial_ring_constructor import PolynomialRing as PolynomialRing
from sage.rings.power_series_ring import PowerSeriesRing as PowerSeriesRing
from sage.rings.rational_field import QQ as QQ
from sage.structure.element import Element as Element
from sage.structure.formal_sum import FormalSum as FormalSum
from sage.structure.parent import Parent as Parent
from sage.structure.richcmp import op_EQ as op_EQ, op_NE as op_NE, richcmp as richcmp, richcmp_method as richcmp_method
from sage.structure.sage_object import SageObject as SageObject
from sage.structure.unique_representation import UniqueRepresentation as UniqueRepresentation

def EtaGroup(level):
    """
    Create the group of eta products of the given level.

    EXAMPLES::

        sage: EtaGroup(12)
        Group of eta products on X_0(12)
        sage: EtaGroup(1/2)
        Traceback (most recent call last):
        ...
        TypeError: Level (=1/2) must be a positive integer
        sage: EtaGroup(0)
        Traceback (most recent call last):
        ...
        ValueError: Level (=0) must be a positive integer
    """

class EtaGroupElement(Element):
    def __init__(self, parent, rdict) -> None:
        """
        Create an eta product object. Usually called implicitly via
        EtaGroup_class.__call__ or the EtaProduct factory function.

        EXAMPLES::

            sage: EtaProduct(8, {1:24, 2:-24})
            Eta product of level 8 : (eta_1)^24 (eta_2)^-24
            sage: g = _; g == loads(dumps(g))
            True
            sage: TestSuite(g).run()
        """
    def __invert__(self):
        """
        Return the inverse of ``self``.

        EXAMPLES::

            sage: eta1, eta2 = EtaGroup(4).basis()
            sage: ~eta2  # indirect doctest
            Eta product of level 4 : (eta_1)^-16 (eta_2)^24 (eta_4)^-8
        """
    def is_one(self) -> bool:
        """
        Return whether ``self`` is the one of the monoid.

        EXAMPLES::

            sage: e = EtaProduct(3, {3:12, 1:-12})
            sage: e.is_one()
            False
            sage: e.parent().one().is_one()
            True
            sage: ep = EtaProduct(5, {})
            sage: ep.is_one()
            True
            sage: ep.parent().one() == ep
            True
        """
    def level(self) -> Integer:
        """
        Return the level of this eta product.

        EXAMPLES::

            sage: e = EtaProduct(3, {3:12, 1:-12})
            sage: e.level()
            3
            sage: EtaProduct(12, {6:6, 2:-6}).level() # not the lcm of the d's
            12
            sage: EtaProduct(36, {6:6, 2:-6}).level() # not minimal
            36
        """
    def q_expansion(self, n):
        """
        Return the `q`-expansion of ``self`` at the cusp at infinity.

        INPUT:

        - ``n`` -- integer; number of terms to calculate

        OUTPUT:

        A power series over `\\ZZ` in the variable `q`, with a *relative*
        precision of `1 + O(q^n)`.

        ALGORITHM: Calculates eta to (n/m) terms, where m is the smallest
        integer dividing self.level() such that self.r(m) != 0. Then
        multiplies.

        EXAMPLES::

            sage: EtaProduct(36, {6:6, 2:-6}).q_expansion(10)
            q + 6*q^3 + 27*q^5 + 92*q^7 + 279*q^9 + O(q^11)
            sage: R.<q> = ZZ[[]]
            sage: EtaProduct(2,{2:24,1:-24}).q_expansion(100) == delta_qexp(101)(q^2)/delta_qexp(101)(q)
            True
        """
    def qexp(self, n):
        """
        Alias for ``self.q_expansion()``.

        EXAMPLES::

            sage: e = EtaProduct(36, {6:8, 3:-8})
            sage: e.qexp(10)
            q + 8*q^4 + 36*q^7 + O(q^10)
            sage: e.qexp(30) == e.q_expansion(30)
            True
        """
    def order_at_cusp(self, cusp: CuspFamily) -> Integer:
        """
        Return the order of vanishing of ``self`` at the given cusp.

        INPUT:

        - ``cusp`` -- a :class:`CuspFamily` object

        OUTPUT: integer

        EXAMPLES::

            sage: e = EtaProduct(2, {2:24, 1:-24})
            sage: e.order_at_cusp(CuspFamily(2, 1)) # cusp at infinity
            1
            sage: e.order_at_cusp(CuspFamily(2, 2)) # cusp 0
            -1
        """
    def divisor(self):
        """
        Return the divisor of ``self``, as a formal sum of CuspFamily objects.

        EXAMPLES::

            sage: e = EtaProduct(12, {1:-336, 2:576, 3:696, 4:-216, 6:-576, 12:-144})
            sage: e.divisor() # FormalSum seems to print things in a random order?
            -131*(Inf) - 50*(c_{2}) + 11*(0) + 50*(c_{6}) + 169*(c_{4}) - 49*(c_{3})
            sage: e = EtaProduct(2^8, {8:1,32:-1})
            sage: e.divisor() # random
            -(c_{2}) - (Inf) - (c_{8,2}) - (c_{8,3}) - (c_{8,4}) - (c_{4,2})
             - (c_{8,1}) - (c_{4,1}) + (c_{32,4}) + (c_{32,3}) + (c_{64,1})
             + (0) + (c_{32,2}) + (c_{64,2}) + (c_{128}) + (c_{32,1})
        """
    def degree(self) -> Integer:
        """
        Return the degree of ``self`` as a map `X_0(N) \\to \\mathbb{P}^1`.

        This is the sum of all the positive coefficients in the divisor
        of ``self``.

        EXAMPLES::

            sage: e = EtaProduct(12, {1:-336, 2:576, 3:696, 4:-216, 6:-576, 12:-144})
            sage: e.degree()
            230
        """
    def r(self, d) -> Integer:
        """
        Return the exponent `r_d` of `\\eta(q^d)` in ``self``.

        EXAMPLES::

            sage: e = EtaProduct(12, {2:24, 3:-24})
            sage: e.r(3)
            -24
            sage: e.r(4)
            0
        """

class EtaGroup_class(UniqueRepresentation, Parent):
    """
    The group of eta products of a given level under multiplication.

    TESTS::

        sage: TestSuite(EtaGroup(12)).run()

        sage: EtaGroup(12) == EtaGroup(12)
        True
        sage: EtaGroup(12) == EtaGroup(13)
        False

        sage: EtaGroup(12) != EtaGroup(12)
        False
        sage: EtaGroup(12) != EtaGroup(13)
        True
    """
    def __init__(self, level) -> None:
        """
        Create the group of eta products of a given level, which must be a
        positive integer.

        EXAMPLES::

            sage: G = EtaGroup(12); G # indirect doctest
            Group of eta products on X_0(12)
            sage: TestSuite(G).run()
        """
    def one(self) -> EtaGroupElement:
        """
        Return the identity element of ``self``.

        EXAMPLES::

            sage: EtaGroup(12).one()
            Eta product of level 12 : 1
        """
    def level(self) -> Integer:
        """
        Return the level of ``self``.

        EXAMPLES::

            sage: EtaGroup(10).level()
            10
        """
    def basis(self, reduce: bool = True) -> list:
        '''
        Produce a basis for the free abelian group of eta-products of level
        N (under multiplication), attempting to find basis vectors of the
        smallest possible degree.

        INPUT:

        - ``reduce`` -- boolean (default: ``True``); whether or not to apply
          LLL-reduction to the calculated basis

        EXAMPLES::

            sage: EtaGroup(5).basis()
            [Eta product of level 5 : (eta_1)^6 (eta_5)^-6]
            sage: EtaGroup(12).basis()
            [Eta product of level 12 : (eta_1)^-3 (eta_2)^2 (eta_3)^1 (eta_4)^-1 (eta_6)^-2 (eta_12)^3,
             Eta product of level 12 : (eta_1)^-4 (eta_2)^2 (eta_3)^4 (eta_6)^-2,
             Eta product of level 12 : (eta_1)^6 (eta_2)^-9 (eta_3)^-2 (eta_4)^3 (eta_6)^3 (eta_12)^-1,
             Eta product of level 12 : (eta_1)^-1 (eta_2)^3 (eta_3)^3 (eta_4)^-2 (eta_6)^-9 (eta_12)^6,
             Eta product of level 12 : (eta_1)^3 (eta_3)^-1 (eta_4)^-3 (eta_12)^1]
            sage: EtaGroup(12).basis(reduce=False) # much bigger coefficients
            [Eta product of level 12 : (eta_1)^384 (eta_2)^-576 (eta_3)^-696 (eta_4)^216 (eta_6)^576 (eta_12)^96,
             Eta product of level 12 : (eta_2)^24 (eta_12)^-24,
             Eta product of level 12 : (eta_1)^-40 (eta_2)^116 (eta_3)^96 (eta_4)^-30 (eta_6)^-80 (eta_12)^-62,
             Eta product of level 12 : (eta_1)^-4 (eta_2)^-33 (eta_3)^-4 (eta_4)^1 (eta_6)^3 (eta_12)^37,
             Eta product of level 12 : (eta_1)^15 (eta_2)^-24 (eta_3)^-29 (eta_4)^9 (eta_6)^24 (eta_12)^5]

        ALGORITHM: An eta product of level `N` is uniquely
        determined by the integers `r_d` for `d | N` with
        `d < N`, since `\\sum_{d | N} r_d = 0`. The valid
        `r_d` are those that satisfy two congruences modulo 24,
        and one congruence modulo 2 for every prime divisor of N. We beef
        up the congruences modulo 2 to congruences modulo 24 by multiplying
        by 12. To calculate the kernel of the ensuing map
        `\\ZZ^m \\to (\\ZZ/24\\ZZ)^n`
        we lift it arbitrarily to an integer matrix and calculate its Smith
        normal form. This gives a basis for the lattice.

        This lattice typically contains "large" elements, so by default we
        pass it to the reduce_basis() function which performs
        LLL-reduction to give a more manageable basis.
        '''
    def reduce_basis(self, long_etas) -> list:
        """
        Produce a more manageable basis via LLL-reduction.

        INPUT:

        - ``long_etas`` -- a list of EtaGroupElement objects (which
          should all be of the same level)

        OUTPUT:

        - a new list of EtaGroupElement objects having
          hopefully smaller norm

        ALGORITHM: We define the norm of an eta-product to be the
        `L^2` norm of its divisor (as an element of the free
        `\\ZZ`-module with the cusps as basis and the
        standard inner product). Applying LLL-reduction to this gives a
        basis of hopefully more tractable elements. Of course we'd like to
        use the `L^1` norm as this is just twice the degree, which
        is a much more natural invariant, but `L^2` norm is easier
        to work with!

        EXAMPLES::

            sage: EtaGroup(4).reduce_basis([ EtaProduct(4, {1:8,2:24,4:-32}), EtaProduct(4, {1:8, 4:-8})])
            [Eta product of level 4 : (eta_1)^8 (eta_4)^-8,
             Eta product of level 4 : (eta_1)^-8 (eta_2)^24 (eta_4)^-16]
        """
    Element = EtaGroupElement

def EtaProduct(level, dic) -> EtaGroupElement:
    """
    Create an :class:`EtaGroupElement` object representing the function
    `\\prod_{d | N} \\eta(q^d)^{r_d}`.

    This checks the criteria of Ligozat to ensure that this product
    really is the `q`-expansion of a meromorphic function on `X_0(N)`.

    INPUT:

    - ``level`` -- integer; the N such that this eta
      product is a function on `X_0(N)`

    - ``dic`` -- a dictionary indexed by divisors of N such that the
      coefficient of `\\eta(q^d)` is r[d]. Only nonzero coefficients need be
      specified. If Ligozat's criteria are not satisfied, a :exc:`ValueError`
      will be raised.

    OUTPUT:

    An EtaGroupElement object, whose parent is the EtaGroup of level N and
    whose coefficients are the given dictionary.

    .. NOTE::

        The dictionary ``dic`` does not uniquely specify N. It is
        possible for two EtaGroupElements with different `N`'s to
        be created with the same dictionary, and these represent different
        objects (although they will have the same `q`-expansion at
        the cusp `\\infty`).

    EXAMPLES::

        sage: EtaProduct(3, {3:12, 1:-12})
        Eta product of level 3 : (eta_1)^-12 (eta_3)^12
        sage: EtaProduct(3, {3:6, 1:-6})
        Traceback (most recent call last):
        ...
        ValueError: sum d r_d (=12) is not 0 mod 24
        sage: EtaProduct(3, {4:6, 1:-6})
        Traceback (most recent call last):
        ...
        ValueError: 4 does not divide 3
    """
def num_cusps_of_width(N, d) -> Integer:
    """
    Return the number of cusps on `X_0(N)` of width ``d``.

    INPUT:

    - ``N`` -- integer; the level

    - ``d`` -- integer; an integer dividing `N`, the cusp width

    EXAMPLES::

        sage: from sage.modular.etaproducts import num_cusps_of_width
        sage: [num_cusps_of_width(18,d) for d in divisors(18)]
        [1, 1, 2, 2, 1, 1]
        sage: num_cusps_of_width(4,8)
        Traceback (most recent call last):
        ...
        ValueError: N and d must be positive integers with d|N
    """
def AllCusps(N) -> list:
    """
    Return a list of CuspFamily objects corresponding to the cusps of
    `X_0(N)`.

    INPUT:

    - ``N`` -- integer; the level

    EXAMPLES::

        sage: AllCusps(18)
        [(Inf), (c_{2}), (c_{3,1}), (c_{3,2}), (c_{6,1}), (c_{6,2}), (c_{9}), (0)]
        sage: AllCusps(0)
        Traceback (most recent call last):
        ...
        ValueError: N must be positive
    """

class CuspFamily(SageObject):
    """
    A family of elliptic curves parametrising a region of `X_0(N)`.
    """
    label: Incomplete
    def __init__(self, N, width, label=None) -> None:
        """
        Create the cusp of width d on X_0(N) corresponding to the family
        of Tate curves `(\\CC_p/q^d, \\langle \\zeta q\\rangle)`.

        Here `\\zeta` is a primitive root of unity of order `r` with
        `\\mathrm{lcm}(r,d) = N`. The cusp does not store zeta, so we
        store an arbitrary label instead.

        EXAMPLES::

            sage: CuspFamily(8, 4)
            (c_{4})
            sage: CuspFamily(16, 4, '1')
            (c_{4,1})
        """
    def __richcmp__(self, other, op) -> bool:
        '''
        EXAMPLES::

            sage: a = CuspFamily(16, 4, "1"); a
            (c_{4,1})
            sage: b = CuspFamily(16, 4, "2"); b
            (c_{4,2})
            sage: c = CuspFamily(8, 8); c
            (0)
            sage: a == a
            True
            sage: a == b
            False
            sage: a != b
            True
            sage: a == c
            False
            sage: a < c
            False
            sage: a > c
            True
            sage: a != "foo"
            True
        '''
    def __hash__(self):
        """
        EXAMPLES::

            sage: hash(CuspFamily(10, 1))  # random
            -4769758480201659164
        """
    def width(self) -> Integer:
        """
        Return the width of this cusp.

        EXAMPLES::

            sage: e = CuspFamily(10, 1)
            sage: e.width()
            1
        """
    def level(self) -> Integer:
        """
        Return the level of this cusp.

        EXAMPLES::

            sage: e = CuspFamily(10, 1)
            sage: e.level()
            10
        """
    def sage_cusp(self) -> None:
        """
        Return the corresponding element of `\\mathbb{P}^1(\\QQ)`.

        EXAMPLES::

            sage: CuspFamily(10, 1).sage_cusp() # not implemented
            Infinity
        """

def qexp_eta(ps_ring, prec):
    """
    Return the `q`-expansion of `\\eta(q) / q^{1/24}`.

    Here `\\eta(q)` is Dedekind's function

    .. MATH::

        \\eta(q) = q^{1/24}\\prod_{n=1}^\\infty (1-q^n).

    The result is an element of ``ps_ring``, with precision ``prec``.

    INPUT:

    - ``ps_ring`` -- PowerSeriesRing; a power series ring

    - ``prec`` -- integer; the number of terms to compute

    OUTPUT: an element of ``ps_ring`` which is the `q`-expansion of
    `\\eta(q)/q^{1/24}` truncated to prec terms.

    ALGORITHM: We use the Euler identity

    .. MATH::

         \\eta(q) = q^{1/24}( 1 + \\sum_{n \\ge 1} (-1)^n (q^{n(3n+1)/2} + q^{n(3n-1)/2})

    to compute the expansion.

    EXAMPLES::

        sage: from sage.modular.etaproducts import qexp_eta
        sage: qexp_eta(ZZ[['q']], 100)
        1 - q - q^2 + q^5 + q^7 - q^12 - q^15 + q^22 + q^26 - q^35 - q^40 + q^51 + q^57 - q^70 - q^77 + q^92 + O(q^100)
    """
def eta_poly_relations(eta_elements, degree, labels=['x1', 'x2'], verbose: bool = False):
    """
    Find polynomial relations between eta products.

    INPUT:

    - ``eta_elements`` -- list; a list of EtaGroupElement objects.
      Not implemented unless this list has precisely two elements. degree

    - ``degree`` -- integer; the maximal degree of polynomial to look for

    - ``labels`` -- list of strings; labels to use for the polynomial returned

    - ``verbose`` -- boolean (default: ``False``); if ``True``, prints information as
      it goes

    OUTPUT: list of polynomials which is a Groebner basis for the
    part of the ideal of relations between eta_elements which is
    generated by elements up to the given degree; or None, if no
    relations were found.

    ALGORITHM: An expression of the form
    `\\sum_{0 \\le i,j \\le d} a_{ij} x^i y^j` is zero if and
    only if it vanishes at the cusp infinity to degree at least
    `v = d(deg(x) + deg(y))`. For all terms up to `q^v`
    in the `q`-expansion of this expression to be zero is a
    system of `v + k` linear equations in `d^2`
    coefficients, where `k` is the number of nonzero negative
    coefficients that can appear.

    Solving these equations and calculating a basis for the solution
    space gives us a set of polynomial relations, but this is generally
    far from a minimal generating set for the ideal, so we calculate a
    Groebner basis.

    As a test, we calculate five extra terms of `q`-expansion
    and check that this doesn't change the answer.

    EXAMPLES::

        sage: from sage.modular.etaproducts import eta_poly_relations
        sage: t = EtaProduct(26, {2:2,13:2,26:-2,1:-2})
        sage: u = EtaProduct(26, {2:4,13:2,26:-4,1:-2})
        sage: eta_poly_relations([t, u], 3)
        sage: eta_poly_relations([t, u], 4)
        [x1^3*x2 - 13*x1^3 - 4*x1^2*x2 - 4*x1*x2 - x2^2 + x2]

    Use ``verbose=True`` to see the details of the computation::

        sage: eta_poly_relations([t, u], 3, verbose=True)
        Trying to find a relation of degree 3
        Lowest order of a term at infinity = -12
        Highest possible degree of a term = 15
        Trying all coefficients from q^-12 to q^15 inclusive
        No polynomial relation of order 3 valid for 28 terms
        Check:
        Trying all coefficients from q^-12 to q^20 inclusive
        No polynomial relation of order 3 valid for 33 terms

    ::

        sage: eta_poly_relations([t, u], 4, verbose=True)
        Trying to find a relation of degree 4
        Lowest order of a term at infinity = -16
        Highest possible degree of a term = 20
        Trying all coefficients from q^-16 to q^20 inclusive
        Check:
        Trying all coefficients from q^-16 to q^25 inclusive
        [x1^3*x2 - 13*x1^3 - 4*x1^2*x2 - 4*x1*x2 - x2^2 + x2]
    """
