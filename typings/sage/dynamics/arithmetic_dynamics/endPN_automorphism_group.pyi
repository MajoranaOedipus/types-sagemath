from sage.arith.functions import lcm as lcm
from sage.arith.misc import CRT as CRT, divisors as divisors, gcd as gcd, is_square as is_square
from sage.combinat.permutation import Arrangements as Arrangements
from sage.combinat.subset import Subsets as Subsets
from sage.matrix.constructor import matrix as matrix
from sage.misc.functional import sqrt as sqrt
from sage.misc.lazy_import import lazy_import as lazy_import
from sage.misc.misc_c import prod as prod
from sage.parallel.use_fork import p_iter_fork as p_iter_fork
from sage.rings.finite_rings.finite_field_constructor import GF as GF
from sage.rings.finite_rings.integer_mod_ring import Integers as Integers
from sage.rings.integer_ring import ZZ as ZZ
from sage.rings.polynomial.polynomial_ring_constructor import PolynomialRing as PolynomialRing
from sage.rings.rational_field import QQ as QQ
from sage.sets.primes import Primes as Primes
from sage.sets.set import Set as Set
from sage.structure.element import Matrix as Matrix

def automorphism_group_QQ_fixedpoints(rational_function, return_functions: bool = False, iso_type: bool = False):
    """
    Compute the automorphism group for ``rational_function`` via the method of
    fixed points.

    ALGORITHM:

    See Algorithm 3 in Faber-Manes-Viray [FMV]_.

    INPUT:

    - ``rational_function`` -- Rational Function defined over `\\ZZ` or `\\QQ`

    - ``return_functions`` -- boolean value; ``True`` will return elements in
      the automorphism group as linear fractional transformations. ``False``
      will return elements as `PGL_2` matrices.

    - ``iso_type`` -- boolean; ``True`` will cause the classification of the
      finite automorphism group to also be returned

    OUTPUT: list of automorphisms that make up the automorphism group
    of ``rational_function``

    EXAMPLES::

        sage: F.<z> = PolynomialRing(QQ)
        sage: rational_function = (z^2 - 2*z - 2)/(-2*z^2 - 2*z + 1)
        sage: from sage.dynamics.arithmetic_dynamics.endPN_automorphism_group import automorphism_group_QQ_fixedpoints
        sage: automorphism_group_QQ_fixedpoints(rational_function, True)
        [z, 1/z, -z - 1, -z/(z + 1), (-z - 1)/z, -1/(z + 1)]

    ::

        sage: F.<z> = PolynomialRing(QQ)
        sage: rational_function = (z^2 + 2*z)/(-2*z - 1)
        sage: from sage.dynamics.arithmetic_dynamics.endPN_automorphism_group import automorphism_group_QQ_fixedpoints
        sage: automorphism_group_QQ_fixedpoints(rational_function)
        [
          [1 0]  [-1 -1]  [-2  0]  [0 2]  [-1 -1]  [ 0 -1]
          [0 1], [ 0  1], [ 2  2], [2 0], [ 1  0], [ 1  1]
        ]

    ::

        sage: F.<z> = PolynomialRing(QQ)
        sage: rational_function = (z^2 - 4*z - 3)/(-3*z^2 - 2*z + 2)
        sage: from sage.dynamics.arithmetic_dynamics.endPN_automorphism_group import automorphism_group_QQ_fixedpoints
        sage: automorphism_group_QQ_fixedpoints(rational_function, True, True)
        ([z, (-z - 1)/z, -1/(z + 1)], 'Cyclic of order 3')
    """
def height_bound(polynomial):
    """
    Compute the maximum height of the coefficients of an automorphism.

    This bounds sets the termination criteria for the Chinese Remainder Theorem step.

    Let `f` be a square-free polynomial with coefficients in `K`
    Let `F` be an automorphism of `\\mathbb{P}^1_{Frac(R)}` that permutes the roots of `f`
    This function returns a bound on the height of `F`,
    when viewed as an element of `\\mathbb{P}^3`

    In [FMV]_ it is proven that `ht(F) <= 6^{[K:Q]}*M`, where `M` is the Mahler measure of `f`
    M is bounded above by `H(f)`, so we return the floor of `6*H(f)`
    (since `ht(F)` is an integer)

    INPUT:

    - ``polynomial`` -- a univariate polynomial

    OUTPUT: a positive integer

    EXAMPLES::

        sage: R.<z> = PolynomialRing(QQ)
        sage: f = z^3 + 2*z + 6
        sage: from sage.dynamics.arithmetic_dynamics.endPN_automorphism_group import height_bound
        sage: height_bound(f)
        413526
    """
def PGL_repn(rational_function):
    """
    Take a linear fraction transformation and represent it as a 2x2 matrix.

    INPUT:

    - ``rational_function`` -- a linear fraction transformation

    OUTPUT: a 2x2 matrix representing ``rational_function``

    EXAMPLES::

        sage: R.<z> = PolynomialRing(QQ)
        sage: f = (2*z-1)/(3-z)
        sage: from sage.dynamics.arithmetic_dynamics.endPN_automorphism_group import PGL_repn
        sage: PGL_repn(f)
        [-2  1]
        [ 1 -3]
    """
def PGL_order(A):
    """
    Find the multiplicative order of a linear fractional transformation that
    has a finite order as an element of `PGL_2(R)`.

    ``A`` can be represented either as a rational function or a 2x2 matrix

    INPUT:

    - ``A`` -- a linear fractional transformation

    OUTPUT: a positive integer

    EXAMPLES::

        sage: M = matrix([[0,2], [2,0]])
        sage: from sage.dynamics.arithmetic_dynamics.endPN_automorphism_group import PGL_order
        sage: PGL_order(M)
        2

    ::

        sage: R.<x> = PolynomialRing(QQ)
        sage: from sage.dynamics.arithmetic_dynamics.endPN_automorphism_group import PGL_order
        sage: PGL_order(-1/x)
        2
    """
def CRT_helper(automorphisms, moduli):
    """
    Lift the given list of automorphisms to `Zmod(M)`.

    Given a list of automorphisms over various `Zmod(p^k)` find a list
    of automorphisms over `Zmod(M)` where `M=\\prod p^k` that surjects
    onto every tuple of automorphisms from the various `Zmod(p^k)`.

    INPUT:

    - ``automorphisms`` -- list of lists of automorphisms over various `Zmod(p^k)`

    - ``moduli`` -- list of the various `p^k`

    OUTPUT: list of automorphisms over `Zmod(M)`

    EXAMPLES::

        sage: from sage.dynamics.arithmetic_dynamics.endPN_automorphism_group import CRT_helper
        sage: CRT_helper([[matrix([[4,0], [0,1]]), matrix([[0,1], [1,0]])]], [5])
        ([
        [4 0]  [0 1]
        [0 1], [1 0]
        ], 5)
    """
def CRT_automorphisms(automorphisms, order_elts, degree, moduli):
    """
    Compute a maximal list of automorphisms over `Zmod(M)`.

    Given a list of automorphisms over various `Zmod(p^k)`, a list of the
    elements orders, an integer degree, and a list of the `p^k` values compute
    a maximal list of automorphisms over `Zmod(M)`, such that for every `j` in ``len(moduli)``,
    each element reduces mod ``moduli[j]`` to one of the elements in ``automorphisms[j]`` that
    has order = ``degree``

    INPUT:

    - ``automorphisms`` -- list of lists of automorphisms over various `Zmod(p^k)`

    - ``order_elts`` -- list of lists of the orders of the elements of ``automorphisms``

    - ``degree`` -- positive integer

    - ``moduli`` -- list of prime powers, i.e., `p^k`

    OUTPUT: list containing a list of automorphisms over `Zmod(M)` and the
    product of the moduli

    EXAMPLES::

        sage: aut = [[matrix([[1,0], [0,1]]), matrix([[0,1], [1,0]])]]
        sage: ords = [[1,2]]
        sage: degree = 2
        sage: mods = [5]
        sage: from sage.dynamics.arithmetic_dynamics.endPN_automorphism_group import CRT_automorphisms
        sage: CRT_automorphisms(aut,ords,degree,mods)
        ([
        [0 1]
        [1 0]
        ], 5)
    """
def valid_automorphisms(automorphisms_CRT, rational_function, ht_bound, M, return_functions: bool = False):
    """
    Check if automorphism mod `p^k` lifts to automorphism over `\\ZZ`.

    Checks whether an element that is an automorphism of ``rational_function`` modulo `p^k` for various
    `p` s and `k` s can be lifted to an automorphism over `\\ZZ`. It uses the fact that every
    automorphism has height at most ``ht_bound``

    INPUT:

    - ``automorphisms`` -- list of lists of automorphisms over various `Zmod(p^k)`

    - ``rational_function`` -- a one variable rational function

    - ``ht_bound`` -- positive integer

    - ``M`` -- positive integer, a product of prime powers

    - ``return_functions`` -- boolean (default: ``False``)

    OUTPUT: list of automorphisms over `\\ZZ`

    EXAMPLES::

        sage: R.<z> = PolynomialRing(QQ)
        sage: F = z^2
        sage: from sage.dynamics.arithmetic_dynamics.endPN_automorphism_group import valid_automorphisms
        sage: valid_automorphisms([matrix(GF(5), [[0,1],[1,0]])], F, 48, 5, True)
        [1/z]
    """
def remove_redundant_automorphisms(automorphisms, order_elts, moduli, integral_autos):
    """
    If an element of `Aut_{F_p}` has been lifted to `\\QQ`
    remove that element from `Aut_{F_p}`.

    We don't want to attempt to lift that element again unnecessarily.

    INPUT:

    - ``automorphisms`` -- list of lists of automorphisms

    - ``order_elts`` -- list of lists of the orders of the elements of ``automorphisms``

    - ``moduli`` -- list of prime powers

    - ``integral_autos`` -- list of known automorphisms

    OUTPUT: list of automorphisms

    EXAMPLES::

        sage: auts = [[matrix([[1,0],[0,1]]), matrix([[6,0],[0,1]]), matrix([[0,1],[1,0]]),
        ....:          matrix([[6,1],[1,1]]), matrix([[1,1],[1,6]]), matrix([[0,6],[1,0]]),
        ....:          matrix([[1,6],[1,1]]), matrix([[6,6],[1,6]])]]
        sage: ord_elts = [[1, 2, 2, 2, 2, 2, 4, 4]]
        sage: mods = [7]
        sage: R.<x> = PolynomialRing(QQ)
        sage: int_auts = [-1/x]
        sage: from sage.dynamics.arithmetic_dynamics.endPN_automorphism_group import remove_redundant_automorphisms
        sage: remove_redundant_automorphisms(auts, ord_elts, mods, int_auts)
        [[
        [1 0]  [6 0]  [0 1]  [6 1]  [1 1]  [1 6]  [6 6]
        [0 1], [0 1], [1 0], [1 1], [1 6], [1 1], [1 6]
        ]]
    """
def automorphism_group_QQ_CRT(rational_function, prime_lower_bound: int = 4, return_functions: bool = True, iso_type: bool = False):
    """
    Determines the complete group of rational automorphisms (under the conjugation action
    of `PGL(2,\\QQ)`) for a rational function of one variable.

    See [FMV]_ for details.

    INPUT:

    - ``rational_function`` -- a rational function of a univariate polynomial ring over `\\QQ`

    - ``prime_lower_bound`` -- (default: 4) a positive integer; a lower bound for the primes to use for
      the Chinese Remainder Theorem step

    - ``return_functions`` -- boolean (default: ``True``); ``True`` returns
      linear fractional transformations ``False`` returns elements of `PGL(2,\\QQ)`

    - ``iso_type`` -- boolean (default: ``False``); ``True`` returns the
      isomorphism type of the automorphism group

    OUTPUT: a complete list of automorphisms of ``rational_function``

    EXAMPLES::

        sage: R.<z> = PolynomialRing(QQ)
        sage: f = (3*z^2 - 1)/(z^3 - 3*z)
        sage: from sage.dynamics.arithmetic_dynamics.endPN_automorphism_group import automorphism_group_QQ_CRT
        sage: sorted(automorphism_group_QQ_CRT(f, 4, True))
        [-1/z,
         1/z,
         (-z - 1)/(z - 1),
         (-z + 1)/(z + 1),
         (z - 1)/(z + 1),
         (z + 1)/(z - 1),
         -z,
         z]

    ::

        sage: R.<z> = PolynomialRing(QQ)
        sage: f = (3*z^2 - 1)/(z^3 - 3*z)
        sage: from sage.dynamics.arithmetic_dynamics.endPN_automorphism_group import automorphism_group_QQ_CRT
        sage: sorted(automorphism_group_QQ_CRT(f, 4, False))
        [
        [-1 -1]  [-1  0]  [-1  1]  [ 0 -1]  [0 1]  [ 1 -1]  [1 0]  [ 1  1]
        [ 1 -1], [ 0  1], [ 1  1], [ 1  0], [1 0], [ 1  1], [0 1], [ 1 -1]
        ]
    """
def automorphism_group_FF(rational_function, absolute: bool = False, iso_type: bool = False, return_functions: bool = False):
    """
    This function computes automorphism groups over finite fields.

    ALGORITHM:

    See Algorithm 4 in Faber-Manes-Viray [FMV]_.

    INPUT:

    - ``rational_function`` -- a rational function defined over the fraction field
        of a polynomial ring in one variable with finite field coefficients

    - ``absolute`` -- boolean (default: ``False``); ``True`` returns the
      absolute automorphism group and a field of definition

    - ``iso_type`` -- boolean (default: ``False``); ``True`` returns the
      isomorphism type of the automorphism group

    - ``return_functions`` -- boolean (default: ``False``); ``True`` returns
      linear fractional transformations ``False`` returns elements of `PGL(2)`

    OUTPUT: list of automorphisms of ``rational_function``

    EXAMPLES::

        sage: R.<x> = PolynomialRing(GF(5^2, 't'))
        sage: from sage.dynamics.arithmetic_dynamics.endPN_automorphism_group import automorphism_group_FF
        sage: automorphism_group_FF((x^2+x+1)/(x+1))
        [
        [1 0]  [4 3]
        [0 1], [0 1]
        ]

    ::

        sage: R.<x> = PolynomialRing(GF(2^5, 't'))
        sage: from sage.dynamics.arithmetic_dynamics.endPN_automorphism_group import automorphism_group_FF
        sage: automorphism_group_FF(x^(5), True, False, True)
        [Univariate Polynomial Ring in w over Finite Field in b of size 2^5, [w, 1/w]]

    ::

        sage: R.<x> = PolynomialRing(GF(2^5, 't'))
        sage: from sage.dynamics.arithmetic_dynamics.endPN_automorphism_group import automorphism_group_FF
        sage: automorphism_group_FF(x^(5), False, False, True)
        [x, 1/x]
    """
def field_descent(sigma, y):
    """
    Function for descending an element in a field `E` to a subfield `F`.

    Here `F`, `E` must be finite fields or number fields. This function determines
    the unique image of subfield which is ``y`` by the embedding ``sigma`` if it exists.
    Otherwise returns ``None``.
    This functionality is necessary because Sage does not keep track of subfields.

    INPUT:

    - ``sigma`` -- an embedding sigma: `F` -> `E` of fields

    - ``y`` --an element of the field `E`

    OUTPUT: the unique element of the subfield if it exists, otherwise ``None``

    EXAMPLES::

        sage: R = GF(11^2,'b')
        sage: RR = GF(11)
        sage: s = RR.Hom(R)[0]
        sage: from sage.dynamics.arithmetic_dynamics.endPN_automorphism_group import field_descent
        sage: field_descent(s, R(1))
        1
    """
def rational_function_coefficient_descent(rational_function, sigma, poly_ring):
    """
    Function for descending the coefficients of a rational function from field `E`
    to a subfield `F`.

    Here `F`, `E` must be finite fields or number fields.
    It determines the unique rational function in fraction field of
    ``poly_ring`` which is the image of ``rational_function`` by ``sigma``,
    if it exists, and otherwise returns ``None``.

    INPUT:

    - ``rational_function``--a rational function with coefficients in a field `E`

    - ``sigma`` -- a field embedding sigma: `F` -> `E`

    - ``poly_ring`` -- a polynomial ring `R` with coefficients in `F`

    OUTPUT: a rational function with coefficients in the fraction field of ``poly_ring``
    if it exists, and otherwise ``None``

    EXAMPLES::

        sage: T.<z> = PolynomialRing(GF(11^2,'b'))
        sage: S.<y> = PolynomialRing(GF(11))
        sage: s = S.base_ring().hom(T.base_ring())
        sage: f = (3*z^3 - z^2)/(z-1)
        sage: from sage.dynamics.arithmetic_dynamics.endPN_automorphism_group import rational_function_coefficient_descent
        sage: rational_function_coefficient_descent(f,s,S)
        (3*y^3 + 10*y^2)/(y + 10)
    """
def rational_function_coerce(rational_function, sigma, S_polys):
    """
    Function for coercing a rational function defined over a ring `R` to have
    coefficients in a second ring ``S_polys``.

    The fraction field of polynomial ring ``S_polys`` will contain the new rational function.

    INPUT:

    - ``rational_function`` -- rational function with coefficients in `R`

    - ``sigma`` -- a ring homomorphism sigma: `R` -> ``S_polys``

    - ``S_polys`` -- a polynomial ring

    OUTPUT: a rational function with coefficients in ``S_polys``

    EXAMPLES::

        sage: R.<y> = PolynomialRing(QQ)
        sage: S.<z> = PolynomialRing(ZZ)
        sage: s = S.hom([z],R)
        sage: f = (3*z^2 + 1)/(z^3-1)
        sage: from sage.dynamics.arithmetic_dynamics.endPN_automorphism_group import rational_function_coerce
        sage: rational_function_coerce(f,s,R)
        (3*y^2 + 1)/(y^3 - 1)
    """
def rational_function_reduce(rational_function):
    """
    Force Sage to divide out common factors in numerator and denominator
    of rational function.

    INPUT:

    - ``rational_function`` -- rational function `= F/G` in univariate polynomial ring

    OUTPUT: rational function -- `(F/\\gcd(F,G)) / (G/\\gcd(F,G))`

    EXAMPLES::

        sage: R.<z> = PolynomialRing(GF(7))
        sage: f = ((z-1)*(z^2+z+1))/((z-1)*(z^3+1))
        sage: from sage.dynamics.arithmetic_dynamics.endPN_automorphism_group import rational_function_reduce
        sage: rational_function_reduce(f)
        (z^2 + z + 1)/(z^3 + 1)
    """
def three_stable_points(rational_function, invariant_list):
    """
    Implementation of Algorithm 1 for automorphism groups from
    Faber-Manes-Viray [FMV]_.

    INPUT:

    - ``rational_function`` -- rational function `\\phi` defined over finite
      field `E`

    - ``invariant_list`` -- list of at least `3` points of `\\mathbb{P}^1(E)` that
      is stable under `Aut_{\\phi}(E)`

    OUTPUT: list of automorphisms

    EXAMPLES::

        sage: R.<z> = PolynomialRing(GF(5^2,'t'))
        sage: f = z^3
        sage: L = [[0,1],[4,1],[1,1],[1,0]]
        sage: from sage.dynamics.arithmetic_dynamics.endPN_automorphism_group import three_stable_points
        sage: three_stable_points(f,L)
        [z, 4*z, 1/z, 4/z]
    """
def automorphism_group_FF_alg2(rational_function):
    """
    Implementation of algorithm for determining the absolute automorphism
    group over a finite field, given an invariant set, see [FMV]_.

    INPUT:

    - ``rational_function`` -- a rational function defined over a finite field

    OUTPUT: absolute automorphism group of ``rational_function`` and a ring of definition

    EXAMPLES::

        sage: R.<z> = PolynomialRing(GF(7^2,'t'))
        sage: f = (3*z^3 - z^2)/(z-1)
        sage: from sage.dynamics.arithmetic_dynamics.endPN_automorphism_group import automorphism_group_FF_alg2
        sage: automorphism_group_FF_alg2(f)
        [Univariate Polynomial Ring in w over Finite Field in b of size 7^2, [w, 5/w]]

    ::

        sage: R.<z> = PolynomialRing(GF(5^3,'t'))
        sage: f = (3456*z^(4))
        sage: from sage.dynamics.arithmetic_dynamics.endPN_automorphism_group import automorphism_group_FF_alg2
        sage: automorphism_group_FF_alg2(f)
        [Univariate Polynomial Ring in w over Finite Field in b of size 5^6,
         [w,
          (3*b^5 + 4*b^4 + 3*b^2 + 2*b + 1)*w,
          (2*b^5 + b^4 + 2*b^2 + 3*b + 3)*w,
          1/w,
          (3*b^5 + 4*b^4 + 3*b^2 + 2*b + 1)/w,
          (2*b^5 + b^4 + 2*b^2 + 3*b + 3)/w]]
    """
def order_p_automorphisms(rational_function, pre_image):
    """
    Determine the order-p automorphisms given the input data.

    This is algorithm 4 in Faber-Manes-Viray [FMV]_.

    INPUT:

    - ``rational_function`` -- rational function defined over finite field `F`

    - ``pre_image`` -- set of triples `[x, L, f]`, where `x` is an `F`-rational
        fixed point of ``rational_function``, `L` is the list of `F`-rational
        pre-images of `x` (excluding `x`), and `f` is the polynomial defining
        the full set of pre-images of `x` (again excluding `x` itself)

    OUTPUT: set of automorphisms of order `p` defined over `F`

    EXAMPLES::

        sage: R.<x> = PolynomialRing(GF(11))
        sage: f = x^11
        sage: L = [[[0, 1], [], 1], [[10, 1], [], 1], [[9, 1], [], 1],
        ....: [[8, 1], [],1], [[7, 1], [], 1], [[6, 1], [], 1], [[5, 1], [], 1],
        ....: [[4, 1], [], 1],[[3, 1], [], 1], [[2, 1], [], 1], [[1, 1], [], 1],
        ....: [[1, 0], [], 1]]
        sage: from sage.dynamics.arithmetic_dynamics.endPN_automorphism_group import order_p_automorphisms
        sage: order_p_automorphisms(f,L)
        [x/(x + 1), 6*x/(x + 6), 3*x/(x + 3), 7*x/(x + 7), 9*x/(x + 9), 10*x/(x
        + 10), 5*x/(x + 5), 8*x/(x + 8), 4*x/(x + 4), 2*x/(x + 2), 10/(x + 2),
        (5*x + 10)/(x + 7), (2*x + 10)/(x + 4), (6*x + 10)/(x + 8), (8*x +
        10)/(x + 10), (9*x + 10)/x, (4*x + 10)/(x + 6), (7*x + 10)/(x + 9), (3*x
        + 10)/(x + 5), (x + 10)/(x + 3), (10*x + 7)/(x + 3), (4*x + 7)/(x + 8),
        (x + 7)/(x + 5), (5*x + 7)/(x + 9), (7*x + 7)/x, (8*x + 7)/(x + 1), (3*x
        + 7)/(x + 7), (6*x + 7)/(x + 10), (2*x + 7)/(x + 6), 7/(x + 4), (9*x +
        2)/(x + 4), (3*x + 2)/(x + 9), 2/(x + 6), (4*x + 2)/(x + 10), (6*x +
        2)/(x + 1), (7*x + 2)/(x + 2), (2*x + 2)/(x + 8), (5*x + 2)/x, (x +
        2)/(x + 7), (10*x + 2)/(x + 5), (8*x + 6)/(x + 5), (2*x + 6)/(x + 10),
        (10*x + 6)/(x + 7), (3*x + 6)/x, (5*x + 6)/(x + 2), (6*x + 6)/(x + 3),
        (x + 6)/(x + 9), (4*x + 6)/(x + 1), 6/(x + 8), (9*x + 6)/(x + 6), (7*x +
        8)/(x + 6), (x + 8)/x, (9*x + 8)/(x + 8), (2*x + 8)/(x + 1), (4*x +
        8)/(x + 3), (5*x + 8)/(x + 4), 8/(x + 10), (3*x + 8)/(x + 2), (10*x +
        8)/(x + 9), (8*x + 8)/(x + 7), (6*x + 8)/(x + 7), 8/(x + 1), (8*x +
        8)/(x + 9), (x + 8)/(x + 2), (3*x + 8)/(x + 4), (4*x + 8)/(x + 5), (10*x
        + 8)/x, (2*x + 8)/(x + 3), (9*x + 8)/(x + 10), (7*x + 8)/(x + 8), (5*x +
        6)/(x + 8), (10*x + 6)/(x + 2), (7*x + 6)/(x + 10), 6/(x + 3), (2*x +
        6)/(x + 5), (3*x + 6)/(x + 6), (9*x + 6)/(x + 1), (x + 6)/(x + 4), (8*x
        + 6)/x, (6*x + 6)/(x + 9), (4*x + 2)/(x + 9), (9*x + 2)/(x + 3), (6*x +
        2)/x, (10*x + 2)/(x + 4), (x + 2)/(x + 6), (2*x + 2)/(x + 7), (8*x +
        2)/(x + 2), 2/(x + 5), (7*x + 2)/(x + 1), (5*x + 2)/(x + 10), (3*x +
        7)/(x + 10), (8*x + 7)/(x + 4), (5*x + 7)/(x + 1), (9*x + 7)/(x + 5),
        7/(x + 7), (x + 7)/(x + 8), (7*x + 7)/(x + 3), (10*x + 7)/(x + 6), (6*x
        + 7)/(x + 2), (4*x + 7)/x, (2*x + 10)/x, (7*x + 10)/(x + 5), (4*x +
        10)/(x + 2), (8*x + 10)/(x + 6), (10*x + 10)/(x + 8), 10/(x + 9), (6*x +
        10)/(x + 4), (9*x + 10)/(x + 7), (5*x + 10)/(x + 3), (3*x + 10)/(x + 1),
        x + 1, x + 2, x + 4, x + 8, x + 5, x + 10, x + 9, x + 7, x + 3, x + 6]
    """
def automorphisms_fixing_pair(rational_function, pair, quad):
    """
    Compute the set of automorphisms with order prime to the characteristic
    that fix the pair, excluding the identity.

    INPUT:

    - ``rational_function`` -- rational function defined over finite field `E`

    - ``pair`` -- a pair of points of `\\mathbb{P}^1(E)`

    - ``quad`` -- boolean; an indicator if this is a quadratic pair of points

    OUTPUT: set of automorphisms with order prime to characteristic defined over `E` that fix
    the pair, excluding the identity

    EXAMPLES::

        sage: R.<z> = PolynomialRing(GF(7^2, 't'))
        sage: f = (z^2 + 5*z + 5)/(5*z^2 + 5*z + 1)
        sage: L = [[4, 1], [2, 1]]
        sage: from sage.dynamics.arithmetic_dynamics.endPN_automorphism_group import automorphisms_fixing_pair
        sage: sorted(automorphisms_fixing_pair(f, L, False))
        [6/(z + 1), (6*z + 6)/z]
    """
def automorphism_group_FF_alg3(rational_function):
    """
    Implementation of Algorithm 3 in the paper by Faber/Manes/Viray [FMV]_
    for computing the automorphism group over a finite field.

    INPUT:

    - ``rational_function`` -- a rational function defined over a finite field `F`

    OUTPUT: list of `F`-rational automorphisms of ``rational_function``

    EXAMPLES::

        sage: R.<z> = PolynomialRing(GF(5^3,'t'))
        sage: f = 3456*z^4
        sage: from sage.dynamics.arithmetic_dynamics.endPN_automorphism_group import automorphism_group_FF_alg3
        sage: automorphism_group_FF_alg3(f)
        [z, 1/z]
    """
def which_group(list_of_elements):
    """
    Given a finite subgroup of `PGL_2` determine its isomorphism class.

    This function makes heavy use of the classification of finite subgroups of `PGL(2,K)`.

    INPUT:

    - ``list_of_elements`` -- a finite list of elements of `PGL(2,K)`
      that we know a priori form a group

    OUTPUT: string; the isomorphism type of the group

    EXAMPLES::

        sage: R.<x> = PolynomialRing(GF(7,'t'))
        sage: G = [x, 6*x/(x + 1), 6*x + 6, 1/x, (6*x + 6)/x, 6/(x + 1)]
        sage: from sage.dynamics.arithmetic_dynamics.endPN_automorphism_group import which_group
        sage: which_group(G)
        'Dihedral of order 6'
    """
def conjugating_set_initializer(f, g):
    """
    Return a conjugation invariant set together with information
    to reduce the combinatorics of checking all possible conjugations.

    This function constructs the invariant pair (``source``, ``possible_targets``)
    necessary for the conjugating set algorithm described in [FMV2014]_.
    Let `f` and `g` be dynamical systems on `\\mathbb{P}^n`.
    An invariant pair is a pair of two sets `U`, `V` such that
    `|U| = |V|` and for all `\\phi \\in PGL` such that `f^\\phi = g`,
    `\\phi(u) \\in V` for all `u \\in U`. Invariant pairs can be used
    to determine all conjugations from `f` to `g`. For details
    in the `\\mathbb{P}^1` case, see [FMV2014]_.

    Additionally, this function keeps track of multipliers to reduce the combinatorics.
    This information is then passed to ``conjugating_set_helper`` or
    ``is_conjugate_helper``, which check all possible conjugations determined
    by the invariant pair.

    Do not call this function directly, instead use ``f.conjugating_set(g)``.

    INPUT:

    - ``f`` -- a rational function of degree at least 2, and the same
      degree as ``g``

    - ``g`` -- a nonconstant rational function of the same
      degree as ``f``

    OUTPUT:

    A tuple of the form (``source``, ``possible_targets``).

    - ``source`` -- a conjugation invariant set of `n+2` points of the domain of `f`,
      of which no `n+1` are linearly dependent. Used to specify a possible conjugation
      from `f` to `g`.

    - ``possible_targets`` -- list of tuples of the form (``points``, ``repeated``). ``points``
      is a list of ``points`` which are possible targets for point(s) in ``source``. ``repeated``
      specifies how many points in ``source`` have points in ``points`` as their possible target.

    EXAMPLES:

    We check that ``source`` has no `n+1` linearly dependent points, and that
    ``possible_targets`` tracks multiplier information::

        sage: P.<x,y,z> = ProjectiveSpace(QQ, 2)
        sage: f = DynamicalSystem([
        ....:         8*x^7 - 35*x^4*y^3 - 35*x^4*z^3 - 7*x*y^6 - 140*x*y^3*z^3 - 7*x*z^6,
        ....:         -7*x^6*y - 35*x^3*y^4 - 140*x^3*y*z^3 + 8*y^7 - 35*y^4*z^3 - 7*y*z^6,
        ....:         -7*x^6*z - 140*x^3*y^3*z - 35*x^3*z^4 - 7*y^6*z - 35*y^3*z^4 + 8*z^7])
        sage: from sage.dynamics.arithmetic_dynamics.endPN_automorphism_group import conjugating_set_initializer
        sage: source, possible_targets = conjugating_set_initializer(f, f)
        sage: P.is_linearly_independent(source, 3)
        True
        sage: f.multiplier(possible_targets[0][0][0], 1) == f.multiplier(source[0], 1)
        True
    """
def greedy_independence_check(P, repeated_mult, point_to_mult):
    """
    Return an invariant pair together with information
    to reduce the combinatorics of checking all possible conjugations.

    Let `f` and `g` be dynamical systems on `\\mathbb{P}^n`.
    An invariant pair is a pair of two sets `U`, `V` such that
    `|U| = |V|` and for all `\\phi \\in PGL` such that `f^\\phi = g`,
    `\\phi(u) \\in V` for all `u \\in U`. Invariant pairs can be used
    to determine all conjugations from `f` to `g`. For details
    in the `\\mathbb{P}^1` case, see [FMV2014]_.

    This function may sometimes fail to find the invariant pair
    set even though one exists. It is useful, however, as it is fast
    and returns a set which usually minimizes the combinatorics of
    checking all conjugations.

    INPUT:

    - ``P`` -- a projective space

    - ``repeated_mult`` -- dictionary of integers to lists of points of
      the projective space ``P``. The list of points should be conjugation
      invariant. The keys are considered as weights, and this function attempts
      to minimize the total weight

    - ``point_to_mult`` -- dictionary of points of ``P`` to tuples of the form
      (multiplier, level), where multiplier is the characteristic polynomial
      of the multiplier of the point, and level is the number of preimages
      taken to find the point

    OUTPUT:

    If no set of `n+2` points of which all subsets of size `n+1` are linearly
    independent can be found, then ``None`` is returned.

    Otherwise, a tuple of the form (``source``, ``corresponding``) is returned.

    - ``source`` -- the set `U` of the conjugation invariant pair. A set of `n+2` points
      of the domain of `f`, of which no `n+1` are linearly dependent

    - ``corresponding`` -- list of tuples of the form ((multiplier, level), repeat) where the
      (multiplier, level) pair is the multiplier of a point in ``source`` and repeat
      specifies how many points in source have that (multiplier, level) pair. This
      information specifies the set `V` of the invariant pair.

    EXAMPLES::

        sage: from sage.dynamics.arithmetic_dynamics.endPN_automorphism_group import greedy_independence_check
        sage: P.<x,y> = ProjectiveSpace(QQ, 1)
        sage: repeated_mult = {2: [[P((0, 1)), P((1, 0))]], 1: [[P((1, 1))]]}
        sage: point_to_mult = {P((0, 1)): (x, 0), P((1, 0)): (x, 0), P((1, 1)): (x - 2, 0)}
        sage: greedy_independence_check(P, repeated_mult, point_to_mult)
        ([(1 : 1), (0 : 1), (1 : 0)], [[(x - 2, 0), 1], [(x, 0), 2]])
    """
def conjugating_set_helper(f, g, num_cpus, source, possible_targets):
    """
    Return the set of elements in PGL over the base ring
    that conjugates ``f`` to ``g``.

    This function takes as input the invariant pair
    and multiplier data from ``conjugating_set_initializer``.

    Do not call this function directly, instead use ``f.conjugate_set(g)``.

    INPUT:

    - ``f`` -- a rational function of degree at least 2, and the same
      degree as ``g``

    - ``g`` -- a rational function of the same degree as ``f``

    - ``num_cpus`` -- the number of threads to run in parallel

    - ``source`` -- list of `n+2` conjugation invariant points, of which
      no `n+1` are linearly dependent

    - ``possible_targets`` -- list of tuples of the form (``points``, ``repeated``). ``points``
      is a list of ``points`` which are possible targets for point(s) in ``source``. ``repeated``
      specifies how many points in ``source`` have points in ``points`` as their possible target.

    OUTPUT: list of elements of PGL which conjugate ``f`` to ``g``

    EXAMPLES::

        sage: P.<x,y> = ProjectiveSpace(QQ, 1)
        sage: f = DynamicalSystem([x^2, y^2])
        sage: source = [P((1, 1)), P((0, 1)), P((1, 0))]
        sage: possible_targets = [[[P((1, 1))], 1], [[P((0, 1)), P((1, 0))], 2]]
        sage: from sage.dynamics.arithmetic_dynamics.endPN_automorphism_group import conjugating_set_helper
        sage: sorted(conjugating_set_helper(f, f, 2, source, possible_targets))
        [
        [0 1]  [1 0]
        [1 0], [0 1]
        ]
    """
def is_conjugate_helper(f, g, num_cpus, source, possible_targets):
    """
    Return if ``f`` is conjugate to ``g``.

    This function takes as input the invariant pair
    and multiplier data from ``conjugating_set_initializer``.

    Do not call this function directly, instead use ``f.is_conjugate(g)``.

    INPUT:

    - ``f`` -- a rational function of degree at least 2, and the same
      degree as ``g``

    - ``g`` -- a rational function of the same degree as ``f``

    - ``num_cpus`` -- the number of threads to run in parallel

    - ``source`` -- list of `n+2` conjugation invariant points, of which
      no `n+1` are linearly dependent

    - ``possible_targets`` -- list of tuples of the form (``points``, ``repeated``). ``points``
      is a list of ``points`` which are possible targets for point(s) in ``source``. ``repeated``
      specifies how many points in ``source`` have points in ``points`` as their possible target.

    OUTPUT: ``True`` if ``f`` is conjugate to ``g``, ``False`` otherwise

    EXAMPLES::

        sage: P.<x,y> = ProjectiveSpace(QQ, 1)
        sage: f = DynamicalSystem([x^2, y^2])
        sage: source = [P((1, 1)), P((0, 1)), P((1, 0))]
        sage: possible_targets = [[[P((1, 1))], 1], [[P((0, 1)), P((1, 0))], 2]]
        sage: from sage.dynamics.arithmetic_dynamics.endPN_automorphism_group import is_conjugate_helper
        sage: is_conjugate_helper(f, f, 2, source, possible_targets)
        True
    """
