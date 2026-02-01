from sage.categories.fields import Fields as Fields
from sage.categories.map import Map as Map
from sage.misc.latex import latex as latex
from sage.misc.prandom import shuffle as shuffle
from sage.rings.integer import Integer as Integer
from sage.rings.integer_ring import ZZ as ZZ
from sage.rings.polynomial.multi_polynomial_ring_base import MPolynomialRing_base as MPolynomialRing_base
from sage.rings.polynomial.polynomial_ring import PolynomialRing_generic as PolynomialRing_generic
from sage.rings.polynomial.polynomial_ring_constructor import PolynomialRing as PolynomialRing
from sage.rings.polynomial.term_order import TermOrder as TermOrder
from sage.schemes.generic.ambient_space import AmbientSpace as AmbientSpace
from sage.schemes.projective.projective_space import ProjectiveSpace as ProjectiveSpace
from sage.schemes.weighted_projective.weighted_projective_homset import SchemeHomset_points_weighted_projective_ring as SchemeHomset_points_weighted_projective_ring
from sage.structure.all import UniqueRepresentation as UniqueRepresentation
from sage.structure.category_object import normalize_names as normalize_names

def WeightedProjectiveSpace(weights, R=None, names=None):
    """
    Return a weighted projective space with the given ``weights`` over the ring ``R``.

    EXAMPLES::

        sage: WP = WeightedProjectiveSpace([1, 3, 1]); WP
        Weighted Projective Space of dimension 2 with weights (1, 3, 1) over Integer Ring
    """

class WeightedProjectiveSpace_ring(UniqueRepresentation, AmbientSpace):
    """
    Weighted projective space with the given ``weights`` over the ring `R`.

    EXAMPLES::

        sage: WeightedProjectiveSpace(Zp(5), [1, 3, 1], 'y')                        # needs sage.rings.padics
        Weighted Projective Space of dimension 2 with weights (1, 3, 1) over 5-adic Ring with
        capped relative precision 20
        sage: WeightedProjectiveSpace(QQ, 5, 'y')
        Projective Space of dimension 5 over Rational Field
        sage: _ is ProjectiveSpace(QQ, 5, 'y')
        True
    """
    @staticmethod
    def __classcall__(cls, weights: tuple[Integer], R=..., names=None): ...
    def __init__(self, weights: tuple[Integer], R=..., names=None) -> None:
        """
        Initialization function.
        """
    def weights(self) -> tuple[Integer]:
        """
        Return the tuple of weights of this weighted projective space.

        EXAMPLES::

            sage: WeightedProjectiveSpace(QQ, [1, 3, 1]).weights()
            (1, 3, 1)
        """
    def ngens(self) -> Integer:
        """
        Return the number of generators of this weighted projective space.

        This is the number of variables in the coordinate ring of ``self``.

        EXAMPLES::

            sage: WeightedProjectiveSpace(QQ, [1, 3, 1]).ngens()
            3
            sage: WeightedProjectiveSpace(ZZ, 5).ngens()
            6
        """
    def coordinate_ring(self) -> PolynomialRing_generic:
        """
        Return the coordinate ring of this weighted projective space.

        EXAMPLES::

            sage: WP = WeightedProjectiveSpace(GF(19^2, 'α'), [1, 3, 4, 1], 'abcd')
            sage: # needs sage.rings.finite_rings
            sage: R = WP.coordinate_ring(); R
            Multivariate Polynomial Ring in a, b, c, d over Finite Field in α of size 19^2
            sage: R.term_order()
            Weighted degree reverse lexicographic term order with weights (1, 3, 4, 1)

        ::

            sage: WP = WeightedProjectiveSpace(QQ, [1, 1, 1], ['alpha', 'beta', 'gamma'])
            sage: R = WP.coordinate_ring(); R
            Multivariate Polynomial Ring in alpha, beta, gamma over Rational Field
            sage: R.term_order()
            Weighted degree reverse lexicographic term order with weights (1, 1, 1)
        """
    def point(self, v, check: bool = True):
        """
        Create a point on this weighted projective space.

        INPUT:

        INPUT:

        - ``v`` -- anything that defines a point

        - ``check`` -- boolean (default: ``True``); whether
          to check the defining data for consistency

        OUTPUT: A point of this weighted projective space.

        EXAMPLES::

            sage: WP = WeightedProjectiveSpace(QQ, [1, 3, 1])
            sage: WP.point([2, 3, 1])
            (2 : 3 : 1)
        """
    def change_ring(self, R):
        """
        Return a weighted projective space over ring ``R``.

        INPUT:

        - ``R`` -- commutative ring or morphism

        OUTPUT: weighted projective space over ``R``.
        If ``R`` is a morphism, return a weighted projective space over its codomain.

        .. NOTE::

            There is no need to have any relation between ``R`` and the base ring
            of this space, if you want to have such a relation, use
            ``self.base_extend(R)`` instead.

        EXAMPLES::

            sage: WP = WeightedProjectiveSpace([1, 3, 1], ZZ); WP
            Weighted Projective Space of dimension 2 with weights (1, 3, 1) over Integer Ring
            sage: WP.change_ring(QQ)
            Weighted Projective Space of dimension 2 with weights (1, 3, 1) over Rational Field
            sage: WP.change_ring(GF(5))
            Weighted Projective Space of dimension 2 with weights (1, 3, 1) over Finite Field of size 5
        """
    def subscheme(self, *_, **__) -> None: ...
    def curve(self, F):
        """
        Return a curve defined by ``F`` in this weighted projective space.

        INPUT:

        - ``F`` -- a polynomial, or a list or tuple of polynomials in
          the coordinate ring of this weighted projective space

        EXAMPLES::

            sage: WP.<x, y, z> = WeightedProjectiveSpace([1, 3, 1], QQ)
            sage: WP.curve(y^2 - x^5 * z - 3 * x^2 * z^4 - 2 * z^6)                     # needs sage.schemes
            Weighted Projective Curve over Rational Field defined by y^2 - x^5*z - 3*x^2*z^4 - 2*z^6
        """
