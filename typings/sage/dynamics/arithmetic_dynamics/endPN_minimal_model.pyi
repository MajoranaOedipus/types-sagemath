from sage.arith.misc import gcd as gcd
from sage.functions.hyperbolic import cosh as cosh
from sage.matrix.constructor import matrix as matrix
from sage.matrix.matrix_space import MatrixSpace as MatrixSpace
from sage.rings.cc import CC as CC
from sage.rings.complex_mpfr import ComplexField as ComplexField
from sage.rings.finite_rings.integer_mod_ring import Zmod as Zmod
from sage.rings.integer_ring import ZZ as ZZ
from sage.rings.polynomial.binary_form_reduce import covariant_z0 as covariant_z0, epsinv as epsinv
from sage.rings.polynomial.polynomial_ring_constructor import PolynomialRing as PolynomialRing
from sage.rings.rational_field import QQ as QQ
from sage.schemes.affine.affine_space import AffineSpace as AffineSpace

def bCheck(c, v, p, b):
    """
    Compute a lower bound on the value of ``b``.

    This value is needed for a transformation
    `A(z) = z*p^k + b` to satisfy `ord_p(Res(\\phi^A)) < ord_p(Res(\\phi))` for a
    rational map `\\phi`. See Theorem 3.3.5 in [Molnar]_.

    INPUT:

    - ``c`` -- list of polynomials in `b`. See v for their use

    - ``v`` -- list of rational numbers, where we are considering the inequalities
      `ord_p(c[i]) > v[i]`

    - ``p`` -- a prime

    - ``b`` -- local variable

    OUTPUT: ``bval`` -- integer; lower bound in Theorem 3.3.5

    EXAMPLES::

        sage: R.<b> = PolynomialRing(QQ)
        sage: from sage.dynamics.arithmetic_dynamics.endPN_minimal_model import bCheck
        sage: bCheck(11664*b^2 + 70227*b + 76059, 15/2, 3, b)
        -1
    """
def scale(c, v, p):
    """
    Create scaled integer polynomial with respect to prime ``p``.

    Given an integral polynomial ``c``, we can write `c = p^i*c'`, where ``p`` does not
    divide ``c``. Return ``c'`` and `v - i` where `i` is the smallest valuation of the
    coefficients of `c`.

    INPUT:

    - ``c`` -- integer polynomial

    - ``v`` -- integer; the bound on the exponent from :func:`blift`

    - ``p`` -- a prime

    OUTPUT:

    - boolean -- the new exponent bound is 0 or negative

    - the scaled integer polynomial

    - an integer the new exponent bound

    EXAMPLES::

        sage: R.<b> = PolynomialRing(QQ)
        sage: from sage.dynamics.arithmetic_dynamics.endPN_minimal_model import scale
        sage: scale(24*b^3 + 108*b^2 + 162*b + 81, 1, 3)
        [False, 8*b^3 + 36*b^2 + 54*b + 27, 0]
    """
def blift(LF, Li, p, k, S=None, all_orbits: bool = False):
    """
    Search for a solution to the given list of inequalities.

    If found, lift the solution to
    an appropriate valuation. See Lemma 3.3.6 in [Molnar]_

    INPUT:

    - ``LF`` -- list of integer polynomials in one variable (the normalized coefficients)

    - ``Li`` -- integer; the bound on coefficients

    - ``p`` -- a prime

    - ``k`` -- the scaling factor that makes the solution a ``p``-adic integer

    - ``S`` -- polynomial ring to use

    - ``all_orbits`` -- boolean; whether or not to use ``==`` in the
      inequalities to find all orbits

    OUTPUT:

    - boolean -- whether or not the lift is successful

    - integer -- the lift

    EXAMPLES::

        sage: R.<b> = PolynomialRing(QQ)
        sage: from sage.dynamics.arithmetic_dynamics.endPN_minimal_model import blift
        sage: blift([8*b^3 + 12*b^2 + 6*b + 1, 48*b^2 + 483*b + 117, 72*b + 1341,
        ....:        -24*b^2 + 411*b + 99, -144*b + 1233, -216*b], 2, 3, 2)
        [[True, 4]]
    """
def affine_minimal(vp, return_transformation: bool = False, D=None, quick: bool = False):
    """
    Determine if given map is affine minimal.

    Given vp a scheme morphism on the projective line over the rationals,
    this procedure determines if `\\phi` is minimal. In particular, it determines
    if the map is affine minimal, which is enough to decide if it is minimal
    or not. See Proposition 2.10 in [BM2012]_.

    INPUT:

    - ``vp`` -- dynamical system on the projective line

    - ``D`` -- list of primes, in case one only wants to check minimality
      at those specific primes

    - ``return_transformation`` -- boolean (default: ``False``); this
      signals a return of the `PGL_2` transformation to conjugate
      this map to the calculated models

    - ``quick`` -- boolean value. If true the algorithm terminates once
      algorithm determines F/G is not minimal, otherwise algorithm only
      terminates once a minimal model has been found

    OUTPUT: ``newvp`` -- dynamical system on the projective line

    - ``conj`` -- linear fractional transformation which conjugates ``vp`` to ``newvp``

    EXAMPLES::

        sage: PS.<X,Y> = ProjectiveSpace(QQ, 1)
        sage: vp = DynamicalSystem_projective([X^2 + 9*Y^2, X*Y])
        sage: from sage.dynamics.arithmetic_dynamics.endPN_minimal_model import affine_minimal
        sage: affine_minimal(vp, True)
        (
        Dynamical System of Projective Space of dimension 1 over Rational Field
              Defn: Defined on coordinates by sending (X : Y) to (X^2 + Y^2 : X*Y)
        ,
        [3 0]
        [0 1]
        )
    """
def Min(Fun, p, ubRes, conj, all_orbits: bool = False):
    """
    Local loop for :func:`affine_minimal`, where we check minimality at the prime `p`.

    First we bound the possible `k` in our transformations `A = zp^k + b`.
    See Theorems 3.3.2 and 3.3.3 in [Molnar]_.

    INPUT:

    - ``Fun`` -- a dynamical system on projective space

    - ``p`` -- a prime

    - ``ubRes`` -- integer; the upper bound needed for Th. 3.3.3 in [Molnar]_

    - ``conj`` -- a 2x2 matrix keeping track of the conjugation

    - ``all_orbits`` -- boolean; whether or not to use ``==`` in the
      inequalities to find all orbits

    OUTPUT:

    - boolean -- ``True`` if ``Fun`` is minimal at ``p``, ``False`` otherwise

    - a dynamical system on projective space minimal at ``p``

    EXAMPLES::

        sage: P.<x,y> = ProjectiveSpace(QQ, 1)
        sage: f = DynamicalSystem_projective([149*x^2 + 39*x*y + y^2,
        ....:                                 -8*x^2 + 137*x*y + 33*y^2])
        sage: from sage.dynamics.arithmetic_dynamics.endPN_minimal_model import Min
        sage: Min(f, 3, -27000000, matrix(QQ,[[1, 0],[0, 1]]))
        [
        Dynamical System of Projective Space of dimension 1 over Rational Field
          Defn: Defined on coordinates by sending (x : y) to
                (157*x^2 + 72*x*y + 3*y^2 : -24*x^2 + 121*x*y + 54*y^2)        ,
        <BLANKLINE>
        [3 1]
        [0 1]
        ]
    """
def BM_all_minimal(vp, return_transformation: bool = False, D=None):
    """
    Determine a representative in each `SL(2,\\ZZ)` orbit with minimal
    resultant.

    This function modifies the Bruin-Molnar algorithm ([BM2012]_) to solve
    in the inequalities as ``<=`` instead of ``<``. Among the list of
    solutions is all conjugations that preserve the resultant. From that
    list the `SL(2,\\ZZ)` orbits are identified and one representative from
    each orbit is returned. This function assumes that the given model is
    a minimal model.

    INPUT:

    - ``vp`` -- a minimal model of a dynamical system on the projective line

    - ``return_transformation`` -- boolean (default: ``False``); this
      signals a return of the ``PGL_2`` transformation to conjugate ``vp``
      to the calculated minimal model

    - ``D`` -- list of primes, in case one only wants to check minimality
      at those specific primes

    OUTPUT:

    List of pairs ``[f, m]`` where ``f`` is a dynamical system and ``m`` is a
    `2 \\times 2` matrix.

    EXAMPLES::

        sage: P.<x,y> = ProjectiveSpace(QQ,1)
        sage: f = DynamicalSystem([x^3 - 13^2*y^3, x*y^2])
        sage: from sage.dynamics.arithmetic_dynamics.endPN_minimal_model import BM_all_minimal
        sage: BM_all_minimal(f)
        [Dynamical System of Projective Space of dimension 1 over Rational Field
           Defn: Defined on coordinates by sending (x : y) to
                 (x^3 - 169*y^3 : x*y^2),
         Dynamical System of Projective Space of dimension 1 over Rational Field
           Defn: Defined on coordinates by sending (x : y) to
                 (13*x^3 - y^3 : x*y^2)]

    ::

        sage: P.<x,y> = ProjectiveSpace(QQ,1)
        sage: f = DynamicalSystem([x^3 - 6^2*y^3, x*y^2])
        sage: from sage.dynamics.arithmetic_dynamics.endPN_minimal_model import BM_all_minimal
        sage: BM_all_minimal(f, D=[3])
        [Dynamical System of Projective Space of dimension 1 over Rational Field
           Defn: Defined on coordinates by sending (x : y) to
                 (x^3 - 36*y^3 : x*y^2),
         Dynamical System of Projective Space of dimension 1 over Rational Field
           Defn: Defined on coordinates by sending (x : y) to
                 (3*x^3 - 4*y^3 : x*y^2)]

    ::

        sage: P.<x,y> = ProjectiveSpace(QQ,1)
        sage: f = DynamicalSystem([x^3 - 4^2*y^3, x*y^2])
        sage: from sage.dynamics.arithmetic_dynamics.endPN_minimal_model import BM_all_minimal
        sage: cl = BM_all_minimal(f, return_transformation=True)
        sage: all(f.conjugate(m) == g for g, m in cl)
        True
    """
def HS_minimal(f, return_transformation: bool = False, D=None):
    """
    Compute a minimal model for the given projective dynamical system.

    This function implements the algorithm in Hutz-Stoll [HS2018]_.
    A representative with minimal resultant in the conjugacy class
    of ``f`` returned.

    INPUT:

    - ``f`` -- dynamical system on the projective line with minimal resultant

    - ``return_transformation`` -- boolean (default: ``False``); this
      signals a return of the `PGL_2` transformation to conjugate
      this map to the calculated models

    - ``D`` -- list of primes, in case one only wants to check minimality
      at those specific primes

    OUTPUT:

    - a dynamical system
    - (optional) a `2 \\times 2` matrix

    EXAMPLES::

        sage: P.<x,y> = ProjectiveSpace(QQ,1)
        sage: f = DynamicalSystem([x^3 - 6^2*y^3, x^2*y])
        sage: m = matrix(QQ,2,2,[5,1,0,1])
        sage: g = f.conjugate(m)
        sage: g.normalize_coordinates()
        sage: g.resultant().factor()
        2^4 * 3^4 * 5^12
        sage: from sage.dynamics.arithmetic_dynamics.endPN_minimal_model import HS_minimal
        sage: HS_minimal(g).resultant().factor()
        2^4 * 3^4
        sage: HS_minimal(g, D=[2]).resultant().factor()
        2^4 * 3^4 * 5^12
        sage: F,m = HS_minimal(g, return_transformation=True)
        sage: g.conjugate(m) == F
        True
    """
def HS_all_minimal_p(p, f, m=None, return_transformation: bool = False):
    """
    Find a representative in each distinct `SL(2,\\ZZ)` orbit with
    minimal `p`-resultant.

    This function implements the algorithm in Hutz-Stoll [HS2018]_.
    A representatives in each distinct `SL(2,\\ZZ)` orbit with minimal
    valuation with respect to the prime ``p`` is returned. The input
    ``f`` must have minimal resultant in its conjugacy class.

    INPUT:

    - ``p`` -- a prime

    - ``f`` -- dynamical system on the projective line with minimal resultant

    - ``m`` -- (optional) `2 \\times 2` matrix associated with ``f``

    - ``return_transformation`` -- boolean (default: ``False``); this
      signals a return of the ``PGL_2`` transformation to conjugate ``vp``
      to the calculated minimal model

    OUTPUT:

    List of pairs ``[f, m]`` where ``f`` is a dynamical system and ``m`` is a
    `2 \\times 2` matrix.

    EXAMPLES::

        sage: P.<x,y> = ProjectiveSpace(QQ,1)
        sage: f = DynamicalSystem([x^5 - 6^4*y^5, x^2*y^3])
        sage: from sage.dynamics.arithmetic_dynamics.endPN_minimal_model import HS_all_minimal_p
        sage: HS_all_minimal_p(2, f)
        [Dynamical System of Projective Space of dimension 1 over Rational Field
           Defn: Defined on coordinates by sending (x : y) to
                 (x^5 - 1296*y^5 : x^2*y^3),
         Dynamical System of Projective Space of dimension 1 over Rational Field
           Defn: Defined on coordinates by sending (x : y) to
                 (4*x^5 - 162*y^5 : x^2*y^3)]
        sage: cl = HS_all_minimal_p(2, f, return_transformation=True)
        sage: all(f.conjugate(m) == g for g, m in cl)
        True
    """
def HS_all_minimal(f, return_transformation: bool = False, D=None):
    """
    Determine a representative in each `SL(2,\\ZZ)` orbit with minimal resultant.

    This function implements the algorithm in Hutz-Stoll [HS2018]_.
    A representative in each distinct `SL(2,\\ZZ)` orbit is returned.
    The input ``f`` must have minimal resultant in its conjugacy class.

    INPUT:

    - ``f`` -- dynamical system on the projective line with minimal resultant

    - ``return_transformation`` -- boolean (default: ``False``); this
      signals a return of the ``PGL_2`` transformation to conjugate ``vp``
      to the calculated minimal model

    - ``D`` -- list of primes, in case one only wants to check minimality
      at those specific primes

    OUTPUT:

    List of pairs ``[f, m]``, where ``f`` is a dynamical system and ``m``
    is a `2 \\times 2` matrix.

    EXAMPLES::

        sage: P.<x,y> = ProjectiveSpace(QQ,1)
        sage: f = DynamicalSystem([x^3 - 6^2*y^3, x^2*y])
        sage: from sage.dynamics.arithmetic_dynamics.endPN_minimal_model import HS_all_minimal
        sage: HS_all_minimal(f)
        [Dynamical System of Projective Space of dimension 1 over Rational Field
           Defn: Defined on coordinates by sending (x : y) to
                 (x^3 - 36*y^3 : x^2*y),
         Dynamical System of Projective Space of dimension 1 over Rational Field
           Defn: Defined on coordinates by sending (x : y) to
                 (9*x^3 - 12*y^3 : 9*x^2*y),
         Dynamical System of Projective Space of dimension 1 over Rational Field
           Defn: Defined on coordinates by sending (x : y) to
                 (4*x^3 - 18*y^3 : 4*x^2*y),
         Dynamical System of Projective Space of dimension 1 over Rational Field
           Defn: Defined on coordinates by sending (x : y) to
                 (36*x^3 - 6*y^3 : 36*x^2*y)]
        sage: HS_all_minimal(f, D=[3])
        [Dynamical System of Projective Space of dimension 1 over Rational Field
           Defn: Defined on coordinates by sending (x : y) to
                 (x^3 - 36*y^3 : x^2*y),
         Dynamical System of Projective Space of dimension 1 over Rational Field
           Defn: Defined on coordinates by sending (x : y) to
                 (9*x^3 - 12*y^3 : 9*x^2*y)]

    ::

        sage: P.<x,y> = ProjectiveSpace(QQ,1)
        sage: f = DynamicalSystem([x^3 - 6^2*y^3, x*y^2])
        sage: from sage.dynamics.arithmetic_dynamics.endPN_minimal_model import HS_all_minimal
        sage: cl = HS_all_minimal(f, return_transformation=True)
        sage: all(f.conjugate(m) == g for g, m in cl)
        True
    """
def get_bound_dynamical(F, f, m: int = 1, dynatomic: bool = True, prec: int = 53, emb=None):
    """
    The hyperbolic distance from `j` which must contain the smallest map.

    This defines the maximum possible distance from `j` to the `z_0` covariant
    of the associated binary form `F` in the hyperbolic 3-space
    for which the map `f` could have smaller coefficients.

    INPUT:

    - ``F`` -- binary form of degree at least 3 with no multiple roots associated
      to ``f``

    - ``f`` -- a dynamical system on `P^1`

    - ``m`` -- positive integer. the period used to create ``F``

    - ``dynatomic`` -- boolean. whether ``F`` is the periodic points or the
      formal periodic points of period ``m`` for ``f``

    - ``prec`` -- positive integer. precision to use in CC

    - ``emb`` -- embedding into CC

    OUTPUT: a positive real number

    EXAMPLES::

        sage: from sage.dynamics.arithmetic_dynamics.endPN_minimal_model import get_bound_dynamical
        sage: P.<x,y> = ProjectiveSpace(QQ,1)
        sage: f = DynamicalSystem([50*x^2 + 795*x*y + 2120*y^2, 265*x^2 + 106*y^2])
        sage: get_bound_dynamical(f.dynatomic_polynomial(1), f)
        35.5546923182219
    """
def smallest_dynamical(f, dynatomic: bool = True, start_n: int = 1, prec: int = 53, emb=None, algorithm: str = 'HS', check_minimal: bool = True):
    """
    Determine the poly with smallest coefficients in `SL(2,\\ZZ)` orbit of ``F``.

    Smallest is in the sense of global height.
    The method is the algorithm in Hutz-Stoll [HS2018]_.
    A binary form defining the periodic points is associated to ``f``.
    From this polynomial a bound on the search space can be determined.

    ``f`` should already be a minimal model or finding the orbit
    representatives may give wrong results.

    INPUT:

    - ``f`` -- a dynamical system on `P^1`

    - ``dynatomic`` -- boolean. whether ``F`` is the periodic points or the
      formal periodic points of period ``m`` for ``f``

    - ``start_n`` -- positive integer. the period used to start trying to
      create associate binary form ``F``

    - ``prec`` -- positive integer. precision to use in CC

    - ``emb`` -- embedding into CC

    - ``algorithm`` -- (optional) string; either ``'BM'`` for the Bruin-Molnar
      algorithm or ``'HS'`` for the Hutz-Stoll algorithm. If not specified,
      properties of the map are utilized to choose how to compute minimal
      orbit representatives

    - ``check_minimal`` -- (default: ``True``), boolean, whether to check
      if this map is a minimal model

    OUTPUT: pair [dynamical system, matrix]

    EXAMPLES::

        sage: from sage.dynamics.arithmetic_dynamics.endPN_minimal_model import smallest_dynamical
        sage: P.<x,y> = ProjectiveSpace(QQ,1)
        sage: f = DynamicalSystem([50*x^2 + 795*x*y + 2120*y^2, 265*x^2 + 106*y^2])
        sage: smallest_dynamical(f)  # long time
        [
        Dynamical System of Projective Space of dimension 1 over Rational Field
          Defn: Defined on coordinates by sending (x : y) to
                (-480*x^2 - 1125*x*y + 1578*y^2 : 265*x^2 + 1060*x*y + 1166*y^2),
        <BLANKLINE>
        [1 2]
        [0 1]
        ]
    """
