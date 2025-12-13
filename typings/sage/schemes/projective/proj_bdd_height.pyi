from _typeshed import Incomplete
from collections.abc import Generator
from sage.arith.functions import lcm as lcm
from sage.arith.misc import gcd as gcd
from sage.misc.lazy_import import lazy_import as lazy_import
from sage.rings.integer import Integer as Integer
from sage.rings.rational_field import QQ as QQ

def ZZ_points_of_bounded_height(PS, dim, bound) -> Generator[Incomplete, None, Incomplete]:
    """
    Return an iterator of the points in ``self`` of absolute multiplicative
    height of at most ``bound`` in the rational field.

    INPUT:

    - ``PS`` -- a projective space

    - ``dim`` -- positive integer

    - ``bound`` -- positive integer

    OUTPUT: an iterator of points of bounded height

    EXAMPLES::

        sage: from sage.schemes.projective.proj_bdd_height import ZZ_points_of_bounded_height
        sage: PS = ProjectiveSpace(ZZ, 1)
        sage: sorted(list(ZZ_points_of_bounded_height(PS, 1, 1)))
        [(-1 : -1), (-1 : 0), (-1 : 1), (0 : -1)]
        sage: len(list(ZZ_points_of_bounded_height(PS, 1, 5)))
        40
        sage: sorted(list(ZZ_points_of_bounded_height(PS, 1, 2)))
        [(-2 : -1), (-2 : 1), (-1 : -2), (-1 : -1),
         (-1 : 0), (-1 : 1), (-1 : 2), (0 : -1)]
        sage: PS = ProjectiveSpace(ZZ, 2)
        sage: sorted(list(ZZ_points_of_bounded_height(PS, 2, 1)))
        [(-1 : -1 : -1), (-1 : -1 : 0), (-1 : -1 : 1), (-1 : 0 : -1),
         (-1 : 0 : 0), (-1 : 0 : 1), (-1 : 1 : -1), (-1 : 1 : 0),
         (-1 : 1 : 1), (0 : -1 : -1), (0 : -1 : 0), (0 : -1 : 1),
         (0 : 0 : -1)]

    There are no points of negative height::

        sage: from sage.schemes.projective.proj_bdd_height import ZZ_points_of_bounded_height
        sage: PS = ProjectiveSpace(ZZ, 1)
        sage: list(ZZ_points_of_bounded_height(PS, 1, -3))
        []
    """
def QQ_points_of_bounded_height(PS, dim, bound, normalize: bool = False) -> Generator[Incomplete, None, Incomplete]:
    """
    Return an iterator of the points in ``self`` of absolute multiplicative
    height of at most ``bound`` in the rational field.

    INPUT:

    - ``PS`` -- a projective space

    - ``dim`` -- positive integer

    - ``bound`` -- a real number

    - ``normalize`` -- boolean (default: ``False``); whether to
      normalize the coordinates of returned points

    OUTPUT: an iterator of points of bounded height

    EXAMPLES::

        sage: from sage.schemes.projective.proj_bdd_height import QQ_points_of_bounded_height
        sage: PS = ProjectiveSpace(QQ, 1)
        sage: sorted(list(QQ_points_of_bounded_height(PS, 1, 1)))
        [(-1 : 1), (0 : 1), (1 : 0), (1 : 1)]
        sage: len(list(QQ_points_of_bounded_height(PS, 1, 5)))
        40
        sage: sorted(list(QQ_points_of_bounded_height(PS, 1, 2)))
        [(-2 : 1), (-1 : 1), (-1/2 : 1), (0 : 1),
         (1/2 : 1), (1 : 0), (1 : 1), (2 : 1)]
        sage: sorted(list(QQ_points_of_bounded_height(PS, 1, 2, normalize=True)))
        [(-2 : 1), (-1 : 1), (-1 : 2), (0 : 1),
         (1 : 0), (1 : 1), (1 : 2), (2 : 1)]

    There are no points of negative height::

        sage: from sage.schemes.projective.proj_bdd_height import QQ_points_of_bounded_height
        sage: PS = ProjectiveSpace(QQ, 1)
        sage: list(QQ_points_of_bounded_height(PS, 1, -3))
        []
    """
def IQ_points_of_bounded_height(PS, K, dim, bound) -> Generator[Incomplete, None, Incomplete]:
    """
    Return an iterator of the points in ``self`` of absolute multiplicative
    height of at most ``bound`` in the imaginary quadratic field ``K``.

    INPUT:

    - ``PS`` -- a projective space

    - ``K`` -- a number field

    - ``dim`` -- a positive integer

    - ``bound`` -- a real number

    OUTPUT: an iterator of points of bounded height

    EXAMPLES:

        sage: # needs sage.rings.number_field
        sage: from sage.schemes.projective.proj_bdd_height import IQ_points_of_bounded_height
        sage: CF.<a> = CyclotomicField(3)
        sage: P.<x,y,z> = ProjectiveSpace(CF, 2)
        sage: len(list(IQ_points_of_bounded_height(P, CF, 2, -1)))
        0
        sage: len(list(IQ_points_of_bounded_height(P, CF, 2, 1)))
        57
    """
def points_of_bounded_height(PS, K, dim, bound, prec: int = 53) -> Generator[Incomplete, None, Incomplete]:
    """
    Return an iterator of the points in ``K`` with dimension ``dim`` of
    absolute multiplicative height of at most ``bound``.

    ALGORITHM:

    This is an implementation of Algorithm 6 in [Krumm2016]_.

    INPUT:

    - ``PS`` -- a projective space

    - ``K`` -- a number field

    - ``dim`` -- positive integer

    - ``bound`` -- a real number

    - ``prec`` -- (default: 53) a positive integer

    OUTPUT: an iterator of points of bounded height

    EXAMPLES::

        sage: from sage.schemes.projective.proj_bdd_height import points_of_bounded_height
        sage: x = polygen(ZZ, 'x')

        sage: # needs sage.geometry.polyhedron sage.libs.pari sage.rings.number_field
        sage: K.<a> = NumberField(x^3 - 7)
        sage: P.<x,y,z> = ProjectiveSpace(K, 2)
        sage: sorted(list(points_of_bounded_height(P, K, 2, 1)))
        [(0 : 0 : 1), (0 : 1 : 0), (1 : 0 : 0), (0 : -1 : 1), (0 : 1 : 1),
         (-1 : 0 : 1), (1 : 0 : 1), (1 : 1 : 0), (-1 : 1 : 0), (-1 : -1 : 1),
         (-1 : 1 : 1), (1 : -1 : 1), (1 : 1 : 1)]

    ::

        sage: # needs sage.geometry.polyhedron sage.libs.pari sage.rings.number_field
        sage: R.<x> = QQ[]
        sage: K.<a> = NumberField(3*x^2 + 1)
        sage: O = K.maximal_order()
        sage: P.<z,w> = ProjectiveSpace(O, 1)
        sage: len(list(P.points_of_bounded_height(bound=2)))
        44

    ::

        sage: # needs sage.geometry.polyhedron sage.libs.pari sage.rings.number_field
        sage: R.<x> = QQ[]
        sage: K.<a> = NumberField(3*x^2 + 1)
        sage: O = K.maximal_order()
        sage: P.<z,w> = ProjectiveSpace(O, 1)
        sage: sorted(list(P.points_of_bounded_height(bound=1)))
        [(-1 : 1), (-3/2*a - 1/2 : 1), (3/2*a - 1/2 : 1), (0 : 1),
         (-3/2*a + 1/2 : 0), (-3/2*a + 1/2 : 1), (3/2*a + 1/2 : 1), (1 : 1)]

    ::

        sage: # needs sage.geometry.polyhedron sage.libs.pari sage.rings.number_field
        sage: R.<x> = QQ[]
        sage: K.<z> = NumberField(x^2 - 2)
        sage: R2.<y> = K[]
        sage: L.<w> = K.extension(y^2 - 3)
        sage: P.<a,b> = ProjectiveSpace(L, 1)
        sage: len(list(P.points_of_bounded_height(bound=2)))
        256
    """
