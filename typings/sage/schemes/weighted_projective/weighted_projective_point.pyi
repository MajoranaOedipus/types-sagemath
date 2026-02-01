from sage.categories.fields import Fields as Fields
from sage.misc.misc_c import prod as prod
from sage.rings.fraction_field import FractionField as FractionField
from sage.schemes.generic.morphism import SchemeMorphism as SchemeMorphism, SchemeMorphism_point as SchemeMorphism_point
from sage.structure.richcmp import op_EQ as op_EQ, op_NE as op_NE, richcmp as richcmp
from sage.structure.sequence import Sequence as Sequence

class SchemeMorphism_point_weighted_projective_ring(SchemeMorphism_point):
    """
    A rational point of weighted projective space over a ring.

    INPUT:

    - ``X`` -- a homset of a subscheme of an ambient weighted projective space over a ring `R`.

    - ``v`` -- a list or tuple of coordinates in `R`.

    - ``check`` -- boolean (default: ``True``); Whether to check the input for consistency.

    EXAMPLES::

        sage: WP = WeightedProjectiveSpace(2, ZZ)
        sage: WP(2, 3, 4)
        (2 : 3 : 4)
    """
    def __init__(self, X, v, check: bool = True) -> None:
        """
        The Python constructor.

        EXAMPLES::

            sage: WP = WeightedProjectiveSpace([3, 4, 5], QQ)
            sage: P1 = WP(2, 3, 4); P1
            (2 : 3 : 4)
            sage: P2 = WP(2000, 30000, 400000); P2
            (2000 : 30000 : 400000)
            sage: P1 == P2
            True

        The point constructor normalises coordinates at the last position with
        weight `1`::

            sage: WP = WeightedProjectiveSpace([3, 1, 4, 1], QQ)
            sage: P = WP(8, 3, 16, 2); P
            (1 : 3/2 : 1 : 1)
            sage: P == WP(1, 3 / 2, 1, 1)
            True
        """
    def __hash__(self):
        """
        Compute the hash value of this point.

        We attempt to normalise the coordinates of this point over the field of
        fractions of the base ring. If this is not possible, return the hash of
        the parent. See :meth:`normalize_coordinates` for more details.

        OUTPUT: Integer.

        .. SEEALSO ::

            :meth:`normalize_coordinates`

        EXAMPLES::

            sage: WP = WeightedProjectiveSpace([1, 3, 1], QQ)
            sage: hash(WP(6, 24, 2)) == hash(WP(3, 3, 1))
            True
            sage: WP = WeightedProjectiveSpace([1, 3, 1], ZZ)
            sage: hash(WP(6, 24, 2)) == hash(WP(3, 3, 1))
            True
        """
    def scale_by(self, t) -> None:
        """
        Scale the coordinates of the point by ``t``.

        A :exc:`TypeError` occurs if the point is not in the
        base_ring of the codomain after scaling.

        INPUT:

        - ``t`` -- a ring element

        OUTPUT: none

        EXAMPLES::

            sage: WP = WeightedProjectiveSpace([3, 4, 5], ZZ)
            sage: P = WP([8, 16, 32]); P
            (8 : 16 : 32)
            sage: P.scale_by(1 / 2); P
            (1 : 1 : 1)
            sage: P.scale_by(1 / 3); P
            Traceback (most recent call last):
            ...
            TypeError: ...
        """
    def normalize_coordinates(self) -> None:
        """
        Normalise coordinates of this weighted projective point if possible.

        Currently, this method checks if (1) the ambient weighted projective
        space is defined over a field and (2) the weight of any index is `1`.
        If so, the last of which is rescaled to `1`.

        EXAMPLES::

            sage: WP = WeightedProjectiveSpace([3, 1, 5], QQ)
            sage: P = WP([8, 16, 32]); P
            (1/512 : 1 : 1/32768)
            sage: P.scale_by(13); P
            (2197/512 : 13 : 371293/32768)
            sage: P.normalize_coordinates(); P
            (1/512 : 1 : 1/32768)

        ::

            sage: WP = WeightedProjectiveSpace([3, 4, 5], ZZ)
            sage: P = WP([8, 16, 32]); P
            (8 : 16 : 32)
            sage: P.normalize_coordinates(); P
            (8 : 16 : 32)
        """
