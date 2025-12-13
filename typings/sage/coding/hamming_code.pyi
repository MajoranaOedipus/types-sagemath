from .linear_code import AbstractLinearCode as AbstractLinearCode
from sage.matrix.matrix_space import MatrixSpace as MatrixSpace
from sage.misc.cachefunc import cached_method as cached_method
from sage.rings.integer import Integer as Integer
from sage.schemes.projective.projective_space import ProjectiveSpace as ProjectiveSpace

class HammingCode(AbstractLinearCode):
    """
    Representation of a Hamming code.

    INPUT:

    - ``base_field`` -- the base field over which ``self`` is defined

    - ``order`` -- the order of ``self``

    EXAMPLES::

        sage: C = codes.HammingCode(GF(7), 3)
        sage: C
        [57, 54] Hamming Code over GF(7)
    """
    def __init__(self, base_field, order) -> None:
        """
        TESTS:

        If ``base_field`` is not a finite field, an exception is raised::

            sage: codes.HammingCode(RR, 3)
            Traceback (most recent call last):
            ...
            ValueError: base_field has to be a finite field

        If ``order`` is not a Sage Integer or a Python int, an exception is raised::

            sage: codes.HammingCode(GF(3), 3.14)
            Traceback (most recent call last):
            ...
            ValueError: order has to be a Sage Integer or a Python int
        """
    def __eq__(self, other):
        """
        Test equality of Hamming Code objects.

        EXAMPLES::

            sage: C1 = codes.HammingCode(GF(7), 3)
            sage: C2 = codes.HammingCode(GF(7), 3)
            sage: C1 == C2
            True
        """
    def __hash__(self):
        """
        Return the hash of ``self``.

        EXAMPLES::

            sage: C1 = codes.HammingCode(GF(7), 3)
            sage: C2 = codes.HammingCode(GF(7), 3)
            sage: hash(C1) == hash(C2)
            True
        """
    @cached_method
    def parity_check_matrix(self):
        """
        Return a parity check matrix of ``self``.

        The construction of the parity check matrix in case ``self``
        is not a binary code is not really well documented.
        Regarding the choice of projective geometry, one might check:

        - the note over section 2.3 in [Rot2006]_, pages 47-48
        - the dedicated paragraph in [HP2003]_, page 30

        EXAMPLES::

            sage: C = codes.HammingCode(GF(3), 3)
            sage: C.parity_check_matrix()
            [1 0 1 1 0 1 0 1 1 1 0 1 1]
            [0 1 1 2 0 0 1 1 2 0 1 1 2]
            [0 0 0 0 1 1 1 1 1 2 2 2 2]
        """
    def minimum_distance(self):
        """
        Return the minimum distance of ``self``.

        It is always 3 as ``self`` is a Hamming Code.

        EXAMPLES::

            sage: C = codes.HammingCode(GF(7), 3)
            sage: C.minimum_distance()
            3
        """
