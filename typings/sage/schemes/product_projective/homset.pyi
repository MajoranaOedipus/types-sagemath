from sage.categories.fields import Fields as Fields
from sage.categories.number_fields import NumberFields as NumberFields
from sage.misc.misc_c import prod as prod
from sage.misc.mrange import xmrange as xmrange
from sage.rings.finite_rings.finite_field_base import FiniteField as FiniteField
from sage.rings.rational_field import RationalField as RationalField
from sage.schemes.generic.algebraic_scheme import AlgebraicScheme_subscheme as AlgebraicScheme_subscheme
from sage.schemes.generic.homset import SchemeHomset_points as SchemeHomset_points

class SchemeHomset_points_product_projective_spaces_ring(SchemeHomset_points):
    """
    Set of rational points of a product of projective spaces.

    INPUT: See :class:`~sage.schemes.generic.homset.SchemeHomset_generic`.

    EXAMPLES::

        sage: from sage.schemes.product_projective.homset import SchemeHomset_points_product_projective_spaces_ring
        sage: SchemeHomset_points_product_projective_spaces_ring(
        ....:     Spec(QQ), ProductProjectiveSpaces([1, 1], QQ, 'z'))
        Set of rational points of Product of projective spaces P^1 x P^1 over Rational Field
    """

class SchemeHomset_points_product_projective_spaces_field(SchemeHomset_points_product_projective_spaces_ring):
    def points(self, **kwds):
        """
        Return some or all rational points of a projective scheme.

        Over a finite field, all points are returned. Over an infinite field, all points satisfying the bound
        are returned. For a zero-dimensional subscheme, all points are returned regardless of whether the base
        ring is a field or not.

        For number fields, this uses the
        Doyle-Krumm algorithm 4 (algorithm 5 for imaginary quadratic) for
        computing algebraic numbers up to a given height [DK2013]_ or
        uses the chinese remainder theorem and points modulo primes
        for larger bounds.

        The algorithm requires floating point arithmetic, so the user is
        allowed to specify the precision for such calculations.
        Additionally, due to floating point issues, points
        slightly larger than the bound may be returned. This can be controlled
        by lowering the tolerance.


        INPUT:

        - ``bound`` -- a real number

        - ``tolerance`` -- a rational number in (0,1] used in Doyle-Krumm
          algorithm 4

        - ``precision`` -- the precision to use for computing the elements of
          bounded height of number fields

        - ``algorithm`` -- either ``'sieve'`` or ``'enumerate'`` algorithms can
          be used over `\\QQ`. If not specified, ``'enumerate'`` is used only
          for small height bounds

        OUTPUT: list of rational points of the projective scheme

        EXAMPLES::

            sage: P.<x,y,z,w> = ProductProjectiveSpaces([1, 1], QQ)
            sage: X = P.subscheme([x - y, z^2 - 2*w^2])
            sage: X(P.base_ring()).points()                                             # needs sage.libs.singular
            []

        ::

            sage: u = QQ['u'].0
            sage: K = NumberField(u^2 - 2, 'v')                                         # needs sage.rings.number_field
            sage: P.<x,y,z,w> = ProductProjectiveSpaces([1, 1], K)                      # needs sage.rings.number_field
            sage: X = P.subscheme([x^2 - y^2, z^2 - 2*w^2])
            sage: sorted(X(P.base_ring()).points())                                     # needs sage.libs.singular sage.rings.number_field
            [(-1 : 1 , -v : 1), (-1 : 1 , v : 1), (1 : 1 , -v : 1), (1 : 1 , v : 1)]

        ::

            sage: u = QQ['u'].0
            sage: K = NumberField(u^2 + 1, 'v')                                         # needs sage.rings.number_field
            sage: P.<x,y,z,w> = ProductProjectiveSpaces([1, 1], K)                      # needs sage.rings.number_field
            sage: P(K).points(bound=1)                                                  # needs sage.libs.singular sage.rings.number_field
            [(-1 : 1 , -1 : 1), (-1 : 1 , -v : 1), (-1 : 1 , 0 : 1), (-1 : 1 , v : 1),
             (-1 : 1 , 1 : 0), (-1 : 1 , 1 : 1), (-v : 1 , -1 : 1), (-v : 1 , -v : 1),
             (-v : 1 , 0 : 1), (-v : 1 , v : 1), (-v : 1 , 1 : 0), (-v : 1 , 1 : 1),
             (0 : 1 , -1 : 1), (0 : 1 , -v : 1), (0 : 1 , 0 : 1), (0 : 1 , v : 1),
             (0 : 1 , 1 : 0), (0 : 1 , 1 : 1), (v : 1 , -1 : 1), (v : 1 , -v : 1),
             (v : 1 , 0 : 1), (v : 1 , v : 1), (v : 1 , 1 : 0), (v : 1 , 1 : 1),
             (1 : 0 , -1 : 1), (1 : 0 , -v : 1), (1 : 0 , 0 : 1), (1 : 0 , v : 1),
             (1 : 0 , 1 : 0), (1 : 0 , 1 : 1), (1 : 1 , -1 : 1), (1 : 1 , -v : 1),
             (1 : 1 , 0 : 1), (1 : 1 , v : 1), (1 : 1 , 1 : 0), (1 : 1 , 1 : 1)]

        ::

            sage: P.<x,y,z,u,v> = ProductProjectiveSpaces([2, 1], GF(3))
            sage: P(P.base_ring()).points()
            [(0 : 0 : 1 , 0 : 1), (0 : 0 : 1 , 1 : 0), (0 : 0 : 1 , 1 : 1), (0 : 0 : 1 , 2 : 1),
             (0 : 1 : 0 , 0 : 1), (0 : 1 : 0 , 1 : 0), (0 : 1 : 0 , 1 : 1), (0 : 1 : 0 , 2 : 1),
             (0 : 1 : 1 , 0 : 1), (0 : 1 : 1 , 1 : 0), (0 : 1 : 1 , 1 : 1), (0 : 1 : 1 , 2 : 1),
             (0 : 2 : 1 , 0 : 1), (0 : 2 : 1 , 1 : 0), (0 : 2 : 1 , 1 : 1), (0 : 2 : 1 , 2 : 1),
             (1 : 0 : 0 , 0 : 1), (1 : 0 : 0 , 1 : 0), (1 : 0 : 0 , 1 : 1), (1 : 0 : 0 , 2 : 1),
             (1 : 0 : 1 , 0 : 1), (1 : 0 : 1 , 1 : 0), (1 : 0 : 1 , 1 : 1), (1 : 0 : 1 , 2 : 1),
             (1 : 1 : 0 , 0 : 1), (1 : 1 : 0 , 1 : 0), (1 : 1 : 0 , 1 : 1), (1 : 1 : 0 , 2 : 1),
             (1 : 1 : 1 , 0 : 1), (1 : 1 : 1 , 1 : 0), (1 : 1 : 1 , 1 : 1), (1 : 1 : 1 , 2 : 1),
             (1 : 2 : 1 , 0 : 1), (1 : 2 : 1 , 1 : 0), (1 : 2 : 1 , 1 : 1), (1 : 2 : 1 , 2 : 1),
             (2 : 0 : 1 , 0 : 1), (2 : 0 : 1 , 1 : 0), (2 : 0 : 1 , 1 : 1), (2 : 0 : 1 , 2 : 1),
             (2 : 1 : 0 , 0 : 1), (2 : 1 : 0 , 1 : 0), (2 : 1 : 0 , 1 : 1), (2 : 1 : 0 , 2 : 1),
             (2 : 1 : 1 , 0 : 1), (2 : 1 : 1 , 1 : 0), (2 : 1 : 1 , 1 : 1), (2 : 1 : 1 , 2 : 1),
             (2 : 2 : 1 , 0 : 1), (2 : 2 : 1 , 1 : 0), (2 : 2 : 1 , 1 : 1), (2 : 2 : 1 , 2 : 1)]

        ::

            sage: PP.<x,y,z,u,v> = ProductProjectiveSpaces([2, 1], QQ)
            sage: X = PP.subscheme([x + y, u*u - v*u])
            sage: X.rational_points(bound=2)                                            # needs sage.libs.singular
            [(-2 : 2 : 1 , 0 : 1),
             (-2 : 2 : 1 , 1 : 1),
             (-1 : 1 : 0 , 0 : 1),
             (-1 : 1 : 0 , 1 : 1),
             (-1 : 1 : 1 , 0 : 1),
             (-1 : 1 : 1 , 1 : 1),
             (-1/2 : 1/2 : 1 , 0 : 1),
             (-1/2 : 1/2 : 1 , 1 : 1),
             (0 : 0 : 1 , 0 : 1),
             (0 : 0 : 1 , 1 : 1),
             (1/2 : -1/2 : 1 , 0 : 1),
             (1/2 : -1/2 : 1 , 1 : 1),
             (1 : -1 : 1 , 0 : 1),
             (1 : -1 : 1 , 1 : 1),
             (2 : -2 : 1 , 0 : 1),
             (2 : -2 : 1 , 1 : 1)]

        better to enumerate with low codimension::

            sage: PP.<x,y,z,u,v,a,b,c> = ProductProjectiveSpaces([2, 1, 2], QQ)
            sage: X = PP.subscheme([x*u^2*a, b*z*u*v, z*v^2*c])
            sage: len(X.rational_points(bound=1, algorithm='enumerate'))                # needs sage.libs.singular
            232
        """
