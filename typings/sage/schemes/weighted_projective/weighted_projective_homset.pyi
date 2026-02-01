from sage.schemes.generic.homset import SchemeHomset_points as SchemeHomset_points

class SchemeHomset_points_weighted_projective_ring(SchemeHomset_points):
    """
    Set of rational points of a weighted projective variety over a ring.

    INPUT:

    See :class:`SchemeHomset_points`.

    EXAMPLES::

        sage: W = WeightedProjectiveSpace([3, 4, 5], QQ)
        sage: W.point_homset()
        Set of rational points of Weighted Projective Space of dimension 2 with weights (3, 4, 5) over Rational Field
        sage: W.an_element().parent() is W.point_homset()
        True
    """
