from sage.arith.misc import crt as crt, gcd as gcd, next_prime as next_prime, previous_prime as previous_prime
from sage.arith.srange import srange as srange
from sage.misc.lazy_import import lazy_import as lazy_import
from sage.misc.misc_c import prod as prod
from sage.misc.mrange import xmrange as xmrange
from sage.parallel.ncpus import ncpus as ncpus
from sage.parallel.use_fork import p_iter_fork as p_iter_fork
from sage.rings.integer_ring import ZZ as ZZ
from sage.schemes.generic.scheme import Scheme as Scheme

def enum_projective_rational_field(X, B):
    """
    Enumerate projective, rational points on scheme ``X`` of height up to
    bound ``B``.

    INPUT:

    - ``X`` -- a scheme or set of abstract rational points of a scheme

    - ``B`` -- a positive integer bound

    OUTPUT:

    A list containing the projective points of ``X`` of height up to ``B``,
    sorted.

    EXAMPLES::

        sage: P.<X,Y,Z> = ProjectiveSpace(2, QQ)
        sage: C = P.subscheme([X + Y - Z])
        sage: from sage.schemes.projective.projective_rational_point import enum_projective_rational_field
        sage: enum_projective_rational_field(C(QQ), 6)
        [(-5 : 6 : 1), (-4 : 5 : 1), (-3 : 4 : 1), (-2 : 3 : 1),
         (-3/2 : 5/2 : 1), (-1 : 1 : 0), (-1 : 2 : 1), (-2/3 : 5/3 : 1),
         (-1/2 : 3/2 : 1), (-1/3 : 4/3 : 1), (-1/4 : 5/4 : 1),
         (-1/5 : 6/5 : 1), (0 : 1 : 1), (1/6 : 5/6 : 1), (1/5 : 4/5 : 1),
         (1/4 : 3/4 : 1), (1/3 : 2/3 : 1), (2/5 : 3/5 : 1), (1/2 : 1/2 : 1),
         (3/5 : 2/5 : 1), (2/3 : 1/3 : 1), (3/4 : 1/4 : 1), (4/5 : 1/5 : 1),
         (5/6 : 1/6 : 1), (1 : 0 : 1), (6/5 : -1/5 : 1), (5/4 : -1/4 : 1),
         (4/3 : -1/3 : 1), (3/2 : -1/2 : 1), (5/3 : -2/3 : 1), (2 : -1 : 1),
         (5/2 : -3/2 : 1), (3 : -2 : 1), (4 : -3 : 1), (5 : -4 : 1),
         (6 : -5 : 1)]
        sage: enum_projective_rational_field(C,6) == enum_projective_rational_field(C(QQ),6)
        True

    ::

        sage: P3.<W,X,Y,Z> = ProjectiveSpace(3, QQ)
        sage: enum_projective_rational_field(P3, 1)
        [(-1 : -1 : -1 : 1), (-1 : -1 : 0 : 1), (-1 : -1 : 1 : 0), (-1 : -1 : 1 : 1),
         (-1 : 0 : -1 : 1), (-1 : 0 : 0 : 1), (-1 : 0 : 1 : 0), (-1 : 0 : 1 : 1),
         (-1 : 1 : -1 : 1), (-1 : 1 : 0 : 0), (-1 : 1 : 0 : 1), (-1 : 1 : 1 : 0),
         (-1 : 1 : 1 : 1), (0 : -1 : -1 : 1), (0 : -1 : 0 : 1), (0 : -1 : 1 : 0),
         (0 : -1 : 1 : 1), (0 : 0 : -1 : 1), (0 : 0 : 0 : 1), (0 : 0 : 1 : 0),
         (0 : 0 : 1 : 1), (0 : 1 : -1 : 1), (0 : 1 : 0 : 0), (0 : 1 : 0 : 1),
         (0 : 1 : 1 : 0), (0 : 1 : 1 : 1), (1 : -1 : -1 : 1), (1 : -1 : 0 : 1),
         (1 : -1 : 1 : 0), (1 : -1 : 1 : 1), (1 : 0 : -1 : 1), (1 : 0 : 0 : 0),
         (1 : 0 : 0 : 1), (1 : 0 : 1 : 0), (1 : 0 : 1 : 1), (1 : 1 : -1 : 1),
         (1 : 1 : 0 : 0), (1 : 1 : 0 : 1), (1 : 1 : 1 : 0), (1 : 1 : 1 : 1)]

    ALGORITHM:

    We just check all possible projective points in correct dimension
    of projective space to see if they lie on ``X``.

    AUTHORS:

    - John Cremona and Charlie Turner (06-2010)
    """
def enum_projective_number_field(X, **kwds):
    """
    Enumerates projective points on scheme ``X`` defined over a number field.

    Simply checks all of the points of absolute height of at most ``B``
    and adds those that are on the scheme to the list.

    This algorithm computes 2 lists: L containing elements x in `K` such that
    H_k(x) <= B, and a list L' containing elements x in `K` that, due to
    floating point issues,
    may be slightly larger then the bound. This can be controlled
    by lowering the tolerance.

    ALGORITHM:

    This is an implementation of the revised algorithm (Algorithm 4) in
    [DK2013]_. Algorithm 5 is used for imaginary quadratic fields.

    INPUT: keyword arguments:

    - ``bound`` -- a real number

    - ``tolerance`` -- a rational number in (0,1] used in Doyle-Krumm
      algorithm-4

    - ``precision`` -- the precision to use for computing the elements of
      bounded height of number fields

    OUTPUT: a sorted list containing the projective points of ``X`` of absolute
    height up to ``B``

    EXAMPLES::

        sage: # needs sage.rings.number_field
        sage: from sage.schemes.projective.projective_rational_point import enum_projective_number_field
        sage: u = QQ['u'].0
        sage: K = NumberField(u^3 - 5, 'v')
        sage: P.<x,y,z> = ProjectiveSpace(K, 2)
        sage: X = P.subscheme([x - y])
        sage: enum_projective_number_field(X(K), bound=RR(5^(1/3)), prec=2^10)          # needs sage.symbolic
        [(0 : 0 : 1), (1 : 1 : 0), (-1 : -1 : 1), (1 : 1 : 1)]

    ::

        sage: # needs sage.rings.number_field
        sage: u = QQ['u'].0
        sage: K = NumberField(u^2 + 3, 'v')
        sage: A.<x,y> = ProjectiveSpace(K, 1)
        sage: X = A.subscheme(x - y)
        sage: enum_projective_number_field(X, bound=2)
        [(1 : 1)]
    """
def enum_projective_finite_field(X):
    """
    Enumerates projective points on scheme ``X`` defined over a finite field.

    INPUT:

    - ``X`` -- a scheme defined over a finite field or a set of abstract
      rational points of such a scheme

    OUTPUT:

    A list containing the projective points of ``X`` over the finite field,
    sorted.

    EXAMPLES::

        sage: from sage.schemes.projective.projective_rational_point import enum_projective_finite_field
        sage: F = GF(53)
        sage: P.<X,Y,Z> = ProjectiveSpace(2, F)
        sage: len(enum_projective_finite_field(P(F)))
        2863
        sage: 53^2 + 53 + 1
        2863

    ::

        sage: # needs sage.rings.finite_rings
        sage: F = GF(9, 'a')
        sage: P.<X,Y,Z> = ProjectiveSpace(2,F)
        sage: C = Curve(X^3 - Y^3 + Z^2*Y)                                              # needs sage.schemes
        sage: enum_projective_finite_field(C(F))                                        # needs sage.schemes
        [(0 : 0 : 1), (0 : 1 : 1), (0 : 2 : 1), (1 : 1 : 0), (a + 1 : 2*a : 1),
         (a + 1 : 2*a + 1 : 1), (a + 1 : 2*a + 2 : 1), (2*a + 2 : a : 1),
         (2*a + 2 : a + 1 : 1), (2*a + 2 : a + 2 : 1)]

    ::

        sage: F = GF(5)
        sage: P2F.<X,Y,Z> = ProjectiveSpace(2, F)
        sage: enum_projective_finite_field(P2F)
        [(0 : 0 : 1), (0 : 1 : 0), (0 : 1 : 1), (0 : 2 : 1), (0 : 3 : 1), (0 : 4 : 1),
         (1 : 0 : 0), (1 : 0 : 1), (1 : 1 : 0), (1 : 1 : 1), (1 : 2 : 1), (1 : 3 : 1),
         (1 : 4 : 1), (2 : 0 : 1), (2 : 1 : 0), (2 : 1 : 1), (2 : 2 : 1), (2 : 3 : 1),
         (2 : 4 : 1), (3 : 0 : 1), (3 : 1 : 0), (3 : 1 : 1), (3 : 2 : 1), (3 : 3 : 1),
         (3 : 4 : 1), (4 : 0 : 1), (4 : 1 : 0), (4 : 1 : 1), (4 : 2 : 1), (4 : 3 : 1),
         (4 : 4 : 1)]

    ALGORITHM:

    Checks all points in projective space to see if they lie on ``X``.

    .. WARNING::

        If ``X`` is defined over an infinite field, this code will not finish!

    AUTHORS:

    - John Cremona and Charlie Turner (06-2010).
    """
def sieve(X, bound):
    """
    Return the list of all projective, rational points on scheme ``X`` of
    height up to ``bound``.

    Height of a projective point `X = (x_1, x_2,\\dots, x_n)` is given by
    `H_X = \\max(y_1, y_2,\\dots, y_n)`, where the values `y_i`
    are the normalized coordinates such that all `y_i` are integers and
    `\\gcd(y_1, y_2,\\dots, y_n) = 1`.

    ALGORITHM:

    Main idea behind the algorithm is to find points modulo primes
    and then reconstruct them using chinese remainder theorem.
    We find modulo primes parallelly and then lift them and apply
    LLL in parallel.

    For the algorithm to work correctly, sufficient primes need
    to be present, these are calculated using the bound given in
    this([Hutz2015]_) paper.

    INPUT:

    - ``X`` -- a scheme with ambient space defined over projective space

    - ``bound`` -- positive integer bound

    OUTPUT:

    A list containing the projective rational points of ``X`` of height
    up to ``bound``, sorted

    EXAMPLES::

        sage: from sage.schemes.projective.projective_rational_point import sieve
        sage: P.<x,y,z,q> = ProjectiveSpace(QQ, 3)
        sage: Y = P.subscheme([x^2 - 3^2*y^2 + z*q, x + z + 4*q])
        sage: sorted(sieve(Y, 12))              # long time                             # needs sage.libs.singular
        [(-4 : -4/3 : 0 : 1), (-4 : 4/3 : 0 : 1),
         (-1 : -1/3 : 1 : 0), (-1 : 1/3 : 1 : 0)]

    ::

        sage: from sage.schemes.projective.projective_rational_point import sieve
        sage: E = EllipticCurve('37a')                                                  # needs sage.schemes
        sage: sorted(sieve(E, 14))              # long time                             # needs sage.libs.singular sage.schemes
        [(0 : 1 : 0),
         (-1 : -1 : 1),
         (-1 : 0 : 1),
         (0 : -1 : 1),
         (0 : 0 : 1),
         (1/4 : -5/8 : 1),
         (1/4 : -3/8 : 1),
         (1 : -1 : 1),
         (1 : 0 : 1),
         (2 : -3 : 1),
         (2 : 2 : 1),
         (6 : 14 : 1)]

    TESTS:

    Algorithm works even if coefficients are fraction::

        sage: from sage.schemes.projective.projective_rational_point import sieve
        sage: P.<x,y,z> = ProjectiveSpace(2, QQ)
        sage: X = P.subscheme(3*x - 3/2*y)
        sage: sieve(X, 3)                                                               # needs sage.libs.singular
        [(-1 : -2 : 1), (-1/2 : -1 : 1), (-1/3 : -2/3 : 1), (0 : 0 : 1),
         (1/3 : 2/3 : 1), (1/2 : 1 : 0), (1/2 : 1 : 1), (1 : 2 : 1)]
    """
