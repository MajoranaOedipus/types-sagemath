from sage.rings.integer_ring import ZZ as ZZ
from sage.rings.rational_field import QQ as QQ
from sage.schemes.generic.scheme import Scheme as Scheme

def enum_affine_rational_field(X, B):
    """
    Enumerates affine rational points on scheme ``X`` up to bound ``B``.

    INPUT:

    - ``X`` -- a scheme or set of abstract rational points of a scheme
    - ``B`` -- a positive integer bound

    OUTPUT:

    - a list containing the affine points of ``X`` of height up to ``B``,
      sorted.

    EXAMPLES::

        sage: A.<x,y,z> = AffineSpace(3, QQ)
        sage: from sage.schemes.affine.affine_rational_point import enum_affine_rational_field
        sage: enum_affine_rational_field(A(QQ), 1)
        [(-1, -1, -1), (-1, -1, 0), (-1, -1, 1), (-1, 0, -1), (-1, 0, 0), (-1, 0, 1),
         (-1, 1, -1), (-1, 1, 0), (-1, 1, 1), (0, -1, -1), (0, -1, 0), (0, -1, 1),
         (0, 0, -1), (0, 0, 0), (0, 0, 1), (0, 1, -1), (0, 1, 0), (0, 1, 1), (1, -1, -1),
         (1, -1, 0), (1, -1, 1), (1, 0, -1), (1, 0, 0), (1, 0, 1), (1, 1, -1), (1, 1, 0),
         (1, 1, 1)]

    ::

        sage: A.<w,x,y,z> = AffineSpace(4, QQ)
        sage: S = A.subscheme([x^2 - y*z + 1, w^3 + z + y^2])
        sage: enum_affine_rational_field(S(QQ), 1)
        [(0, 0, -1, -1)]
        sage: enum_affine_rational_field(S(QQ), 2)
        [(0, 0, -1, -1), (1, -1, -1, -2), (1, 1, -1, -2)]

    ::

        sage: A.<x,y> = AffineSpace(2, QQ)
        sage: C = Curve(x^2 + y - x)                                                    # needs sage.libs.singular
        sage: enum_affine_rational_field(C, 10)         # long time (3 s)               # needs sage.libs.singular
        [(-2, -6), (-1, -2), (-2/3, -10/9), (-1/2, -3/4), (-1/3, -4/9),
         (0, 0), (1/3, 2/9), (1/2, 1/4), (2/3, 2/9), (1, 0),
         (4/3, -4/9), (3/2, -3/4), (5/3, -10/9), (2, -2), (3, -6)]

    AUTHORS:

    - David R. Kohel <kohel@maths.usyd.edu.au>: original version.

    - Charlie Turner (06-2010): small adjustments.

    - Raman Raghukul 2018: updated.
    """
def enum_affine_number_field(X, **kwds):
    """
    Enumerates affine points on scheme ``X`` defined over a number field. Simply checks all of the
    points of absolute height up to ``B`` and adds those that are on the scheme to the list.

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

    - ``tolerance`` -- a rational number in (0,1] used in Doyle-Krumm algorithm-4

    - ``precision`` -- the precision to use for computing the elements of bounded height of number fields

    OUTPUT:

    - a list containing the affine points of ``X`` of absolute height up to ``B``,
      sorted.

    EXAMPLES::

        sage: # needs sage.rings.number_field
        sage: from sage.schemes.affine.affine_rational_point import enum_affine_number_field
        sage: u = QQ['u'].0
        sage: K = NumberField(u^2 + 2, 'v')
        sage: A.<x,y,z> = AffineSpace(K, 3)
        sage: X = A.subscheme([y^2 - x])
        sage: enum_affine_number_field(X(K), bound=2**0.5)
        [(0, 0, -1), (0, 0, -v), (0, 0, -1/2*v), (0, 0, 0), (0, 0, 1/2*v),
         (0, 0, v), (0, 0, 1), (1, -1, -1), (1, -1, -v), (1, -1, -1/2*v),
         (1, -1, 0), (1, -1, 1/2*v), (1, -1, v), (1, -1, 1), (1, 1, -1),
         (1, 1, -v), (1, 1, -1/2*v), (1, 1, 0), (1, 1, 1/2*v), (1, 1, v), (1, 1, 1)]

    ::

        sage: # needs sage.rings.number_field
        sage: from sage.schemes.affine.affine_rational_point import enum_affine_number_field
        sage: u = QQ['u'].0
        sage: K = NumberField(u^2 + 3, 'v')
        sage: A.<x,y> = AffineSpace(K, 2)
        sage: X = A.subscheme(x - y)
        sage: enum_affine_number_field(X, bound=3**0.25)
        [(-1, -1), (-1/2*v - 1/2, -1/2*v - 1/2), (1/2*v - 1/2, 1/2*v - 1/2),
         (0, 0), (-1/2*v + 1/2, -1/2*v + 1/2), (1/2*v + 1/2, 1/2*v + 1/2), (1, 1)]
    """
def enum_affine_finite_field(X):
    """
    Enumerates affine points on scheme ``X`` defined over a finite field.

    INPUT:

    - ``X`` -- a scheme defined over a finite field or a set of abstract
      rational points of such a scheme

    OUTPUT:

    - a list containing the affine points of ``X`` over the finite field,
      sorted.

    EXAMPLES::

        sage: from sage.schemes.affine.affine_rational_point import enum_affine_finite_field
        sage: F = GF(7)
        sage: A.<w,x,y,z> = AffineSpace(4, F)
        sage: C = A.subscheme([w^2 + x + 4, y*z*x - 6, z*y + w*x])
        sage: enum_affine_finite_field(C(F))
        []
        sage: C = A.subscheme([w^2 + x + 4, y*z*x - 6])
        sage: enum_affine_finite_field(C(F))
        [(0, 3, 1, 2), (0, 3, 2, 1), (0, 3, 3, 3), (0, 3, 4, 4), (0, 3, 5, 6),
         (0, 3, 6, 5), (1, 2, 1, 3), (1, 2, 2, 5), (1, 2, 3, 1), (1, 2, 4, 6),
         (1, 2, 5, 2), (1, 2, 6, 4), (2, 6, 1, 1), (2, 6, 2, 4), (2, 6, 3, 5),
         (2, 6, 4, 2), (2, 6, 5, 3), (2, 6, 6, 6), (3, 1, 1, 6), (3, 1, 2, 3),
         (3, 1, 3, 2), (3, 1, 4, 5), (3, 1, 5, 4), (3, 1, 6, 1), (4, 1, 1, 6),
         (4, 1, 2, 3), (4, 1, 3, 2), (4, 1, 4, 5), (4, 1, 5, 4), (4, 1, 6, 1),
         (5, 6, 1, 1), (5, 6, 2, 4), (5, 6, 3, 5), (5, 6, 4, 2), (5, 6, 5, 3),
         (5, 6, 6, 6), (6, 2, 1, 3), (6, 2, 2, 5), (6, 2, 3, 1), (6, 2, 4, 6),
         (6, 2, 5, 2), (6, 2, 6, 4)]

    ::

        sage: A.<x,y,z> = AffineSpace(3, GF(3))
        sage: S = A.subscheme(x + y)
        sage: enum_affine_finite_field(S)
        [(0, 0, 0), (0, 0, 1), (0, 0, 2), (1, 2, 0), (1, 2, 1), (1, 2, 2),
         (2, 1, 0), (2, 1, 1), (2, 1, 2)]

    ALGORITHM:

    Checks all points in affine space to see if they lie on X.

    .. WARNING::

        If ``X`` is defined over an infinite field, this code will not finish!

    AUTHORS:

    - John Cremona and Charlie Turner (06-2010)
    """
