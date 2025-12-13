from sage.arith.misc import binomial as binomial
from sage.combinat.combination import rank as rank
from sage.homology.chain_complex import ChainComplex_class as ChainComplex_class
from sage.matrix.constructor import matrix as matrix
from sage.rings.integer_ring import ZZ as ZZ
from sage.structure.parent import Parent as Parent
from sage.structure.unique_representation import UniqueRepresentation as UniqueRepresentation

class KoszulComplex(ChainComplex_class, UniqueRepresentation):
    """
    A Koszul complex.

    Let `R` be a ring and consider `x_1, x_2, \\ldots, x_n \\in R`. The
    *Koszul complex* `K_*(x_1, \\ldots, x_n)` is given by defining a
    chain complex structure on the exterior algebra `\\bigwedge^n R` with
    the basis `e_{i_1} \\wedge \\cdots \\wedge e_{i_a}`. The differential is
    given by

    .. MATH::

        \\partial(e_{i_1} \\wedge \\cdots \\wedge e_{i_a}) =
        \\sum_{r=1}^a (-1)^{r-1} x_{i_r} e_{i_1} \\wedge \\cdots \\wedge
        \\hat{e}_{i_r} \\wedge \\cdots \\wedge e_{i_a},

    where `\\hat{e}_{i_r}` denotes the omitted factor.

    Alternatively we can describe the Koszul complex by considering the
    basic complex `K_{x_i}`

    .. MATH::

        0 \\rightarrow R \\xrightarrow{x_i} R \\rightarrow 0.

    Then the Koszul complex is given by
    `K_*(x_1, \\ldots, x_n) = \\bigotimes_i K_{x_i}`.

    INPUT:

    - ``R`` -- the base ring
    - ``elements`` -- tuple of elements of `R`

    EXAMPLES::

        sage: R.<x,y,z> = QQ[]
        sage: K = KoszulComplex(R, [x,y])
        sage: ascii_art(K)
                                [-y]
                    [x y]       [ x]
         0 <-- C_0 <------ C_1 <----- C_2 <-- 0
        sage: K = KoszulComplex(R, [x,y,z])
        sage: ascii_art(K)
                                  [-y -z  0]       [ z]
                                  [ x  0 -z]       [-y]
                    [x y z]       [ 0  x  y]       [ x]
         0 <-- C_0 <-------- C_1 <----------- C_2 <----- C_3 <-- 0
        sage: K = KoszulComplex(R, [x+y*z,x+y-z])
        sage: ascii_art(K)
                                                [-x - y + z]
                    [  y*z + x x + y - z]       [   y*z + x]
         0 <-- C_0 <---------------------- C_1 <------------- C_2 <-- 0

    REFERENCES:

    - :wikipedia:`Koszul_complex`
    """
    @staticmethod
    def __classcall_private__(cls, R=None, elements=None):
        """
        Normalize input to ensure a unique representation.

        TESTS::

            sage: R.<x,y,z> = QQ[]
            sage: K1 = KoszulComplex(R, [x,y,z])
            sage: K2 = KoszulComplex(R, (x,y,z))
            sage: K3 = KoszulComplex((x,y,z))
            sage: K1 is K2 and K2 is K3
            True

        Check some corner cases::

            sage: K1 = KoszulComplex(ZZ)
            sage: K2 = KoszulComplex(())
            sage: K3 = KoszulComplex(ZZ, [])
            sage: K1 is K2 and K2 is K3
            True
            sage: K1 is KoszulComplex()
            True
        """
    def __init__(self, R, elements) -> None:
        """
        Initialize ``self``.

        EXAMPLES::

            sage: R.<x,y,z> = QQ[]
            sage: K = KoszulComplex(R, [x,y])
            sage: TestSuite(K).run()
        """
