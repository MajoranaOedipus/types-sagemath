from sage.arith.misc import crt as crt, next_prime as next_prime, previous_prime as previous_prime
from sage.misc.lazy_import import lazy_import as lazy_import
from sage.misc.misc_c import prod as prod
from sage.misc.mrange import xmrange as xmrange
from sage.parallel.ncpus import ncpus as ncpus
from sage.parallel.use_fork import p_iter_fork as p_iter_fork
from sage.rings.integer_ring import ZZ as ZZ
from sage.schemes.generic.scheme import Scheme as Scheme
from sage.schemes.product_projective.space import ProductProjectiveSpaces_ring as ProductProjectiveSpaces_ring

def enum_product_projective_rational_field(X, B):
    """
    Enumerate projective, rational points on scheme ``X`` of height up to
    bound ``B``.

    INPUT:

    - ``X`` -- a scheme or set of abstract rational points of a scheme

    - ``B`` -- positive integer bound

    OUTPUT:

    A list containing the product projective points of ``X`` of height up
    to ``B``, sorted.

    EXAMPLES::

        sage: PP.<x0,x1,x2,x3,x4> = ProductProjectiveSpaces([1, 2], QQ)
        sage: from sage.schemes.product_projective.rational_point import \\\n        ....:   enum_product_projective_rational_field
        sage: enum_product_projective_rational_field(PP, 1)
        [(-1 : 1 , -1 : -1 : 1), (-1 : 1 , -1 : 0 : 1), (-1 : 1 , -1 : 1 : 0),
         (-1 : 1 , -1 : 1 : 1), (-1 : 1 , 0 : -1 : 1), (-1 : 1 , 0 : 0 : 1),
         (-1 : 1 , 0 : 1 : 0), (-1 : 1 , 0 : 1 : 1), (-1 : 1 , 1 : -1 : 1),
         (-1 : 1 , 1 : 0 : 0), (-1 : 1 , 1 : 0 : 1), (-1 : 1 , 1 : 1 : 0),
         (-1 : 1 , 1 : 1 : 1), (0 : 1 , -1 : -1 : 1), (0 : 1 , -1 : 0 : 1),
         (0 : 1 , -1 : 1 : 0), (0 : 1 , -1 : 1 : 1), (0 : 1 , 0 : -1 : 1),
         (0 : 1 , 0 : 0 : 1), (0 : 1 , 0 : 1 : 0), (0 : 1 , 0 : 1 : 1),
         (0 : 1 , 1 : -1 : 1), (0 : 1 , 1 : 0 : 0), (0 : 1 , 1 : 0 : 1),
         (0 : 1 , 1 : 1 : 0), (0 : 1 , 1 : 1 : 1), (1 : 0 , -1 : -1 : 1),
         (1 : 0 , -1 : 0 : 1), (1 : 0 , -1 : 1 : 0), (1 : 0 , -1 : 1 : 1),
         (1 : 0 , 0 : -1 : 1), (1 : 0 , 0 : 0 : 1), (1 : 0 , 0 : 1 : 0),
         (1 : 0 , 0 : 1 : 1), (1 : 0 , 1 : -1 : 1), (1 : 0 , 1 : 0 : 0),
         (1 : 0 , 1 : 0 : 1), (1 : 0 , 1 : 1 : 0), (1 : 0 , 1 : 1 : 1),
         (1 : 1 , -1 : -1 : 1), (1 : 1 , -1 : 0 : 1), (1 : 1 , -1 : 1 : 0),
         (1 : 1 , -1 : 1 : 1), (1 : 1 , 0 : -1 : 1), (1 : 1 , 0 : 0 : 1),
         (1 : 1 , 0 : 1 : 0), (1 : 1 , 0 : 1 : 1), (1 : 1 , 1 : -1 : 1),
         (1 : 1 , 1 : 0 : 0), (1 : 1 , 1 : 0 : 1), (1 : 1 , 1 : 1 : 0),
         (1 : 1 , 1 : 1 : 1)]

    ::

        sage: PP.<x,y,z,u,v> = ProductProjectiveSpaces([2, 1], QQ)
        sage: X = PP.subscheme([x^2 + x*y + y*z, u*u - v*u])
        sage: from sage.schemes.product_projective.rational_point import \\\n        ....:   enum_product_projective_rational_field
        sage: enum_product_projective_rational_field(X, 4)
        [(-2 : 4 : 1 , 0 : 1), (-2 : 4 : 1 , 1 : 1), (-1 : 1 : 0 , 0 : 1),
         (-1 : 1 : 0 , 1 : 1), (-2/3 : -4/3 : 1 , 0 : 1), (-2/3 : -4/3 : 1 , 1 : 1),
         (-1/2 : -1/2 : 1 , 0 : 1), (-1/2 : -1/2 : 1 , 1 : 1),
         (0 : 0 : 1 , 0 : 1), (0 : 0 : 1 , 1 : 1), (0 : 1 : 0 , 0 : 1),
         (0 : 1 : 0 , 1 : 1), (1 : -1/2 : 1 , 0 : 1), (1 : -1/2 : 1 , 1 : 1)]
    """
def enum_product_projective_number_field(X, **kwds):
    """
    Enumerates product projective points on scheme ``X`` defined over a number field.

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

    OUTPUT:

    A list containing the product projective points of ``X`` of
    absolute height up to ``B``, sorted.

    EXAMPLES::

        sage: # needs sage.rings.number_field
        sage: u = QQ['u'].0
        sage: K = NumberField(u^2 + 2, 'v')
        sage: PP.<x,y,z,w> = ProductProjectiveSpaces([1, 1], K)
        sage: X = PP.subscheme([x^2 + 2*y^2])
        sage: from sage.schemes.product_projective.rational_point import \\\n        ....:   enum_product_projective_number_field
        sage: enum_product_projective_number_field(X, bound=1.5)
        [(-v : 1 , -1 : 1), (-v : 1 , -v : 1), (-v : 1 , -1/2*v : 1),
         (-v : 1 , 0 : 1), (-v : 1 , 1/2*v : 1), (-v : 1 , v : 1),
         (-v : 1 , 1 : 0), (-v : 1 , 1 : 1), (v : 1 , -1 : 1),
         (v : 1 , -v : 1), (v : 1 , -1/2*v : 1), (v : 1 , 0 : 1),
         (v : 1 , 1/2*v : 1), (v : 1 , v : 1), (v : 1 , 1 : 0),
         (v : 1 , 1 : 1)]
    """
def enum_product_projective_finite_field(X):
    """
    Enumerates projective points on scheme ``X`` defined over a finite field.

    INPUT:

    - ``X`` -- a scheme defined over a finite field or a set of abstract
      rational points of such a scheme

    OUTPUT:

    A list containing the projective points of ``X`` over the finite field,
    sorted.

    EXAMPLES::

        sage: PP.<x,y,z,w> = ProductProjectiveSpaces([1, 1], GF(3))
        sage: from sage.schemes.product_projective.rational_point import \\\n        ....:   enum_product_projective_finite_field
        sage: enum_product_projective_finite_field(PP)
        [(0 : 1 , 0 : 1), (0 : 1 , 1 : 0), (0 : 1 , 1 : 1),
         (0 : 1 , 2 : 1), (1 : 0 , 0 : 1), (1 : 0 , 1 : 0),
         (1 : 0 , 1 : 1), (1 : 0 , 2 : 1), (1 : 1 , 0 : 1),
         (1 : 1 , 1 : 0), (1 : 1 , 1 : 1), (1 : 1 , 2 : 1),
         (2 : 1 , 0 : 1), (2 : 1 , 1 : 0), (2 : 1 , 1 : 1),
         (2 : 1 , 2 : 1)]

    ::

        sage: PP.<x0,x1,x2,x3> = ProductProjectiveSpaces([1, 1], GF(17))
        sage: X = PP.subscheme([x0^2 + 2*x1^2])
        sage: from sage.schemes.product_projective.rational_point import \\\n        ....:   enum_product_projective_finite_field
        sage: len(enum_product_projective_finite_field(X))
        36
    """
def sieve(X, bound):
    """
    Return the list of all rational points on scheme
    ``X`` of height up to ``bound``.

    ALGORITHM:

    Main idea behind the algorithm is to find points modulo primes
    and then reconstruct them using chinese remainder theorem.
    We compute the points modulo primes parallelly and then lift
    them via chinese remainder theorem in parallel. The LLL reduction
    algorithm is applied to each component of the points, and finally
    the result is merged and converted to a point on the subscheme.

    For the algorithm to work correctly, sufficient primes need
    to be chosen, these are determined using the bounds dependent
    on the bound given in [Hutz2015]_.

    INPUT:

    - ``X`` -- a scheme with ambient space defined over a product of projective spaces

    - ``bound`` -- positive integer bound

    OUTPUT:

    A list containing the rational points of ``X`` of height
    up to ``bound``, sorted

    EXAMPLES::

        sage: from sage.schemes.product_projective.rational_point import sieve
        sage: PP.<x,y,z,u,v> = ProductProjectiveSpaces([2, 1], QQ)
        sage: X = PP.subscheme([x^2 + y^2 - x*z, u*u - v*u])
        sage: sieve(X, 2)                                                               # needs sage.libs.singular
        [(0 : 0 : 1 , 0 : 1), (0 : 0 : 1 , 1 : 1), (1/2 : -1/2 : 1 , 0 : 1),
         (1/2 : -1/2 : 1 , 1 : 1), (1/2 : 1/2 : 1 , 0 : 1), (1/2 : 1/2 : 1 , 1 : 1),
         (1 : 0 : 1 , 0 : 1), (1 : 0 : 1 , 1 : 1)]
    """
