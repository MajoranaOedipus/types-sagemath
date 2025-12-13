from .linear_code import AbstractLinearCode as AbstractLinearCode, LinearCodeGeneratorMatrixEncoder as LinearCodeGeneratorMatrixEncoder
from sage.matrix.constructor import matrix as matrix
from sage.rings.finite_rings.finite_field_constructor import GF as GF

class GolayCode(AbstractLinearCode):
    """
    Representation of a Golay Code.

    INPUT:

    - ``base_field`` -- the base field over which the code is defined;
      can only be ``GF(2)`` or ``GF(3)``

    - ``extended`` -- boolean (default: ``True``); if set to ``True``, creates
      an extended Golay code

    EXAMPLES::

        sage: codes.GolayCode(GF(2))
        [24, 12, 8] Extended Golay code over GF(2)

    Another example with the perfect binary Golay code::

        sage: codes.GolayCode(GF(2), False)
        [23, 12, 7]  Golay code over GF(2)

    TESTS:

        sage: G = codes.GolayCode(GF(2),False)
        sage: G0 = codes.GolayCode(GF(2),True)
        sage: G0prime = G.extended_code()
        sage: G0.generator_matrix() * G0prime.parity_check_matrix().transpose() == 0
        True

        sage: G0perp = G0.dual_code()
        sage: G0.generator_matrix() * G0perp.generator_matrix().transpose() == 0
        True

        sage: G = codes.GolayCode(GF(3),False)
        sage: G0 = codes.GolayCode(GF(3),True)
        sage: G0prime = G.extended_code()
        sage: G0.generator_matrix() * G0prime.parity_check_matrix().transpose() == 0
        True

        sage: G0perp = G0.dual_code()
        sage: G0.generator_matrix() * G0perp.generator_matrix().transpose() == 0
        True
    """
    def __init__(self, base_field, extended: bool = True) -> None:
        """
        TESTS:

        If ``base_field`` is not ``GF(2)`` or ``GF(3)``, an error is raised::

            sage: C = codes.GolayCode(ZZ, true)
            Traceback (most recent call last):
            ...
            ValueError: finite_field must be either GF(2) or GF(3)
        """
    def __eq__(self, other):
        """
        Test equality between Golay Code objects.

        EXAMPLES::

            sage: C1 = codes.GolayCode(GF(2))
            sage: C2 = codes.GolayCode(GF(2))
            sage: C1.__eq__(C2)
            True
        """
    def dual_code(self):
        """
        Return the dual code of ``self``.

        If ``self`` is an extended Golay code, ``self`` is returned.
        Otherwise, it returns the output of
        :meth:`sage.coding.linear_code_no_metric.AbstractLinearCodeNoMetric.dual_code`

        EXAMPLES::

            sage: C = codes.GolayCode(GF(2), extended=True)
            sage: Cd = C.dual_code(); Cd
            [24, 12, 8] Extended Golay code over GF(2)

            sage: Cd == C
            True
        """
    def minimum_distance(self):
        """
        Return the minimum distance of ``self``.

        The minimum distance of Golay codes is already known,
        and is thus returned immediately without computing anything.

        EXAMPLES::

            sage: C = codes.GolayCode(GF(2))
            sage: C.minimum_distance()
            8
        """
    def covering_radius(self):
        """
        Return the covering radius of ``self``.

        The covering radius of a linear code `C` is the smallest
        integer `r` s.t. any element of the ambient space of `C` is at most at
        distance `r` to `C`.

        The covering radii of all Golay codes are known, and are thus returned
        by this method without performing any computation

        EXAMPLES::

            sage: C = codes.GolayCode(GF(2))
            sage: C.covering_radius()
            4
            sage: C = codes.GolayCode(GF(2),False)
            sage: C.covering_radius()
            3
            sage: C = codes.GolayCode(GF(3))
            sage: C.covering_radius()
            3
            sage: C = codes.GolayCode(GF(3),False)
            sage: C.covering_radius()
            2
        """
    def weight_distribution(self):
        """
        Return the list whose `i`-th entry is the number of words of weight `i`
        in ``self``.

        The weight distribution of all Golay codes are known, and are thus returned
        by this method without performing any computation
        MWS (67, 69)

        EXAMPLES::

            sage: C = codes.GolayCode(GF(3))
            sage: C.weight_distribution()
            [1, 0, 0, 0, 0, 0, 264, 0, 0, 440, 0, 0, 24]

        TESTS::

            sage: C = codes.GolayCode(GF(2))
            sage: C.weight_distribution() == super(codes.GolayCode, C).weight_distribution()
            True

            sage: C = codes.GolayCode(GF(2), extended=False)
            sage: C.weight_distribution() == super(codes.GolayCode, C).weight_distribution()
            True

            sage: C = codes.GolayCode(GF(3))
            sage: C.weight_distribution() == super(codes.GolayCode, C).weight_distribution()        # needs sage.libs.gap
            True

            sage: C = codes.GolayCode(GF(3), extended=False)
            sage: C.weight_distribution() == super(codes.GolayCode, C).weight_distribution()        # needs sage.libs.gap
            True
        """
    def generator_matrix(self):
        """
        Return a generator matrix of ``self``.

        Generator matrices of all Golay codes are known, and are thus returned
        by this method without performing any computation

        EXAMPLES::

            sage: C = codes.GolayCode(GF(2), extended=True)
            sage: C.generator_matrix()
            [1 0 0 0 0 0 0 0 0 0 0 0 1 0 1 0 1 1 1 0 0 0 1 1]
            [0 1 0 0 0 0 0 0 0 0 0 0 1 1 1 1 1 0 0 1 0 0 1 0]
            [0 0 1 0 0 0 0 0 0 0 0 0 1 1 0 1 0 0 1 0 1 0 1 1]
            [0 0 0 1 0 0 0 0 0 0 0 0 1 1 0 0 0 1 1 1 0 1 1 0]
            [0 0 0 0 1 0 0 0 0 0 0 0 1 1 0 0 1 1 0 1 1 0 0 1]
            [0 0 0 0 0 1 0 0 0 0 0 0 0 1 1 0 0 1 1 0 1 1 0 1]
            [0 0 0 0 0 0 1 0 0 0 0 0 0 0 1 1 0 0 1 1 0 1 1 1]
            [0 0 0 0 0 0 0 1 0 0 0 0 1 0 1 1 0 1 1 1 1 0 0 0]
            [0 0 0 0 0 0 0 0 1 0 0 0 0 1 0 1 1 0 1 1 1 1 0 0]
            [0 0 0 0 0 0 0 0 0 1 0 0 0 0 1 0 1 1 0 1 1 1 1 0]
            [0 0 0 0 0 0 0 0 0 0 1 0 1 0 1 1 1 0 0 0 1 1 0 1]
            [0 0 0 0 0 0 0 0 0 0 0 1 0 1 0 1 1 1 0 0 0 1 1 1]
        """
    def parity_check_matrix(self):
        """
        Return the parity check matrix of ``self``.

        The parity check matrix of a linear code `C` corresponds to the
        generator matrix of the dual code of `C`.

        Parity check matrices of all Golay codes are known, and are thus returned
        by this method without performing any computation.

        EXAMPLES::

            sage: C = codes.GolayCode(GF(3), extended=False)
            sage: C.parity_check_matrix()
            [1 0 0 0 0 1 2 2 2 1 0]
            [0 1 0 0 0 0 1 2 2 2 1]
            [0 0 1 0 0 2 1 2 0 1 2]
            [0 0 0 1 0 1 1 0 1 1 1]
            [0 0 0 0 1 2 2 2 1 0 1]
        """
