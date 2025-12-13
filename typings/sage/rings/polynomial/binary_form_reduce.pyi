from sage.matrix.constructor import matrix as matrix
from sage.misc.lazy_import import lazy_import as lazy_import
from sage.misc.misc_c import prod as prod
from sage.modules.free_module_element import vector as vector
from sage.rings.cc import CC as CC
from sage.rings.complex_interval_field import ComplexIntervalField as ComplexIntervalField
from sage.rings.complex_mpfr import ComplexField as ComplexField
from sage.rings.integer_ring import ZZ as ZZ
from sage.rings.laurent_series_ring import LaurentSeriesRing as LaurentSeriesRing
from sage.rings.polynomial.polynomial_ring_constructor import PolynomialRing as PolynomialRing
from sage.rings.rational_field import QQ as QQ
from sage.rings.real_mpfr import RealField as RealField

def covariant_z0(F, z0_cov: bool = False, prec: int = 53, emb=None, error_limit: float = 1e-06):
    """
    Return the covariant and Julia invariant from Cremona-Stoll [CS2003]_.

    In [CS2003]_ and [HS2018]_ the Julia invariant is denoted as `\\Theta(F)`
    or `R(F, z(F))`. Note that you may get faster convergence if you first move
    `z_0(F)` to the fundamental domain before computing the true covariant

    INPUT:

    - ``F`` -- binary form of degree at least 3 with no multiple roots

    - ``z0_cov`` -- boolean, compute only the `z_0` invariant. Otherwise, solve
      the minimization problem

    - ``prec`` -- positive integer. precision to use in CC

    - ``emb`` -- embedding into CC

    - ``error_limit`` -- sets the error tolerance (default: 0.000001)

    OUTPUT: a complex number, a real number

    EXAMPLES::

        sage: from sage.rings.polynomial.binary_form_reduce import covariant_z0
        sage: R.<x,y> = QQ[]
        sage: F = 19*x^8 - 262*x^7*y + 1507*x^6*y^2 - 4784*x^5*y^3 + 9202*x^4*y^4\\\n        ....: - 10962*x^3*y^5 + 7844*x^2*y^6 - 3040*x*y^7 + 475*y^8
        sage: covariant_z0(F, prec=80, z0_cov=True)
        (1.3832330115323681438175 + 0.31233552177413614978744*I,
         3358.4074848663492819259)
        sage: F = -x^8 + 6*x^7*y - 7*x^6*y^2 - 12*x^5*y^3 + 27*x^4*y^4\\\n        ....: - 4*x^3*y^5 - 19*x^2*y^6 + 10*x*y^7 - 5*y^8
        sage: covariant_z0(F, prec=80)
        (0.64189877107807122203366 + 1.1852516565091601348355*I,
        3134.5148284344627168276)

    ::

        sage: R.<x,y> = QQ[]
        sage: covariant_z0(x^3 + 2*x^2*y - 3*x*y^2, z0_cov=True)[0]
        0.230769230769231 + 0.799408065031789*I
        sage: -1/covariant_z0(-y^3 + 2*y^2*x + 3*y*x^2, z0_cov=True)[0]
        0.230769230769231 + 0.799408065031789*I

    ::

        sage: R.<x,y> = QQ[]
        sage: covariant_z0(2*x^2*y - 3*x*y^2, z0_cov=True)[0]
        0.750000000000000 + 1.29903810567666*I
        sage: -1/covariant_z0(-x^3 - x^2*y + 2*x*y^2, z0_cov=True)[0] + 1
        0.750000000000000 + 1.29903810567666*I

    ::

        sage: R.<x,y> = QQ[]
        sage: covariant_z0(x^2*y - x*y^2, prec=100) # tol 1e-28
         (0.50000000000000000000000000003 + 0.86602540378443864676372317076*I,
         1.5396007178390020386910634147)

    TESTS::

        sage: R.<x,y>=QQ[]
        sage: covariant_z0(x^2 + 24*x*y + y^2)
        Traceback (most recent call last):
        ...
        ValueError: must be at least degree 3
        sage: covariant_z0((x+y)^3, z0_cov=True)
        Traceback (most recent call last):
        ...
        ValueError: cannot have multiple roots for z0 invariant
        sage: covariant_z0(x^3 + 3*x*y + y)
        Traceback (most recent call last):
        ...
        TypeError: must be a binary form
        sage: covariant_z0(-2*x^2*y^3 + 3*x*y^4 + 127*y^5)
        Traceback (most recent call last):
        ...
        ValueError: cannot have a root with multiplicity >= 5/2
        sage: covariant_z0((x^2+2*y^2)^2)
        Traceback (most recent call last):
        ...
        ValueError: must have at least 3 distinct roots
    """
def epsinv(F, target, prec: int = 53, target_tol: float = 0.001, z=None, emb=None):
    """
    Compute a bound on the hyperbolic distance.

    The true minimum will be within the computed bound.
    It is computed as the inverse of epsilon_F from [HS2018]_.

    INPUT:

    - ``F`` -- binary form of degree at least 3 with no multiple roots

    - ``target`` -- positive real number; the value we want to attain, i.e.,
      the value we are taking the inverse of

    - ``prec`` -- positive integer; precision to use in CC

    - ``target_tol`` -- positive real number; the tolerance with which we
      attain the target value

    - ``z`` -- complex number; ``z_0`` covariant for F

    - ``emb`` -- embedding into CC

    OUTPUT: a real number delta satisfying  target + target_tol > eps_F(delta) > target.

    EXAMPLES::

        sage: from sage.rings.polynomial.binary_form_reduce import epsinv
        sage: R.<x,y> = QQ[]
        sage: epsinv(-2*x^3 + 2*x^2*y + 3*x*y^2 + 127*y^3, 31.5022020249597) # tol 1e-12
        4.02520895942207
    """
def get_bound_poly(F, prec: int = 53, norm_type: str = 'norm', emb=None):
    """
    The hyperbolic distance from `j` which must contain the smallest poly.

    This defines the maximum possible distance from `j` to the `z_0` covariant
    in the hyperbolic 3-space for which the associated `F` could have smaller
    coefficients.

    INPUT:

    - ``F`` -- binary form of degree at least 3 with no multiple roots

    - ``prec`` -- positive integer. precision to use in CC

    - ``norm_type`` -- string, either norm or height

    - ``emb`` -- embedding into CC

    OUTPUT: a positive real number

    EXAMPLES::

        sage: from sage.rings.polynomial.binary_form_reduce import get_bound_poly
        sage: R.<x,y> = QQ[]
        sage: F = -2*x^3 + 2*x^2*y + 3*x*y^2 + 127*y^3
        sage: get_bound_poly(F) # tol 1e-12
        28.0049336543295
        sage: get_bound_poly(F, norm_type='height') # tol 1e-11
        111.890642019092
    """
def smallest_poly(F, prec: int = 53, norm_type: str = 'norm', emb=None):
    """
    Determine the poly with smallest coefficients in `SL(2,\\Z)` orbit of ``F``.

    Smallest can be in the sense of `L_2` norm or height.
    The method is the algorithm in Hutz-Stoll [HS2018]_.

    ``F`` needs to be a binary form with no multiple roots of degree
    at least 3. It should already be reduced in the sense of
    Cremona-Stoll [CS2003]_.

    INPUT:

    - ``F`` -- binary form of degree at least 3 with no multiple roots

    - ``norm_type`` -- string; ``'norm'`` or ``'height'`` controlling what
      ``smallest`` means for the coefficients

    OUTPUT: pair [poly, matrix]

    EXAMPLES::

        sage: from sage.rings.polynomial.binary_form_reduce import smallest_poly
        sage: R.<x,y> = QQ[]
        sage: F = -x^8 + 6*x^7*y - 7*x^6*y^2 - 12*x^5*y^3 + 27*x^4*y^4\\\n        ....: - 4*x^3*y^5 - 19*x^2*y^6 + 10*x*y^7 - 5*y^8
        sage: smallest_poly(F, prec=100) #long time
        [
        -x^8 - 2*x^7*y + 7*x^6*y^2 + 16*x^5*y^3 + 2*x^4*y^4 - 2*x^3*y^5 + 4*x^2*y^6 - 5*y^8,
        <BLANKLINE>
        [1 1]
        [0 1]
        ]

    ::

        sage: from sage.rings.polynomial.binary_form_reduce import smallest_poly, get_bound_poly
        sage: R.<x,y> = QQ[]
        sage: F = -2*x^3 + 2*x^2*y + 3*x*y^2 + 127*y^3
        sage: smallest_poly(F)
        [
                                               [1 4]
        -2*x^3 - 22*x^2*y - 77*x*y^2 + 43*y^3, [0 1]
        ]
        sage: F0, M = smallest_poly(F, norm_type='height')
        sage: F0, M  # random
        (
                                                [5 4]
        -58*x^3 - 47*x^2*y + 52*x*y^2 + 43*y^3, [1 1]
        )
        sage: M in SL2Z, F0 == R.hom(M * vector([x, y]))(F)
        (True, True)
        sage: get_bound_poly(F0, norm_type='height')  # tol 1e-12
        23.3402702199809

    An example with a multiple root::

        sage: R.<x,y> = QQ[]
        sage: F = -16*x^7 - 114*x^6*y - 345*x^5*y^2 - 599*x^4*y^3 - 666*x^3*y^4\\\n        ....: - 481*x^2*y^5 - 207*x*y^6 - 40*y^7
        sage: F.reduced_form()
        (
                                                              [-1 -1]
        -x^5*y^2 - 24*x^3*y^4 - 3*x^2*y^5 - 2*x*y^6 + 16*y^7, [ 1  0]
        )
    """
