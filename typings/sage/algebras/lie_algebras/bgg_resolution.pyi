from sage.homology.chain_complex import ChainComplex_class as ChainComplex_class
from sage.matrix.constructor import matrix as matrix
from sage.misc.cachefunc import cached_function as cached_function
from sage.rings.integer_ring import ZZ as ZZ
from sage.structure.unique_representation import UniqueRepresentation as UniqueRepresentation

class BGGResolution(UniqueRepresentation, ChainComplex_class):
    """
    The BGG resolution of a simple module.

    We realize the BGG resolution as a chain complex, where the `(-1)`-th
    factor corresponds to  the finite dimensional simple module `L_{\\lambda}`
    and the `i`-th factor (`i \\geq 0`) corresponds to

    .. MATH::

        M_i := \\bigoplus_{\\substack{w \\in W \\\\ \\ell(w) = i}} M_{w\\lambda}.

    Since the morphisms can be defined in terms of the image of the
    highest weight vectors, we only encode this information as a
    (finite) chain complex. We do not include the final natural projection
    map `p: M_{\\lambda} \\to L_{\\lambda}` since the highest weight vector of
    weight `\\lambda` only occurs in `M_{\\lambda}` and `L_{\\lambda}`.

    INPUT:

    - ``L`` -- a simple module

    EXAMPLES::

        sage: g = LieAlgebra(QQ, cartan_type=['A', 2])
        sage: La = g.cartan_type().root_system().weight_lattice().fundamental_weights()
        sage: L = g.simple_module(La[1] + 4*La[2])
        sage: res = L.bgg_resolution()
        sage: ascii_art(res)
                                [ 1 -1]       [1]
                    [1 1]       [-1  1]       [1]
         0 <-- C_0 <------ C_1 <-------- C_2 <---- C_3 <-- 0

        sage: g = LieAlgebra(QQ, cartan_type=['D', 4])
        sage: La = g.cartan_type().root_system().weight_lattice().fundamental_weights()
        sage: L = g.simple_module(La[1] + La[2] + 3*La[3])
        sage: res = L.bgg_resolution()
        sage: w0 = WeylGroup(g.cartan_type(), prefix='s').long_element()
        sage: all(res.differential(i) * res.differential(i+1) == 0
        ....:     for i in range(w0.length()))
        True
    """
    def __init__(self, L) -> None:
        """
        Initialize ``self``.

        EXAMPLES::

            sage: g = LieAlgebra(QQ, cartan_type=['B', 2])
            sage: La = g.cartan_type().root_system().weight_lattice().fundamental_weights()
            sage: L = g.simple_module(La[1] + La[2])
            sage: res = L.bgg_resolution()
            sage: TestSuite(res).run()
        """
    def simple_module(self):
        """
        Return the simple module `L_{\\lambda}` defining ``self``.

        EXAMPLES::

            sage: g = LieAlgebra(QQ, cartan_type=['C', 2])
            sage: La = g.cartan_type().root_system().weight_lattice().fundamental_weights()
            sage: L = g.simple_module(La[1] + La[2])
            sage: res = L.bgg_resolution()
            sage: res.simple_module() is L
            True
        """
    def module_order(self, i):
        """
        Return a tuple of Weyl group elements of length ``i``
        determining the ordering of the direct sum defining the
        differential matrix.

        EXAMPLES::

            sage: g = LieAlgebra(QQ, cartan_type=['G', 2])
            sage: La = g.cartan_type().root_system().weight_lattice().fundamental_weights()
            sage: L = g.simple_module(La[1])
            sage: res = L.bgg_resolution()
            sage: [res.module_order(i) for i in range(7)]
            [[1],
             [s2, s1],
             [s2*s1, s1*s2],
             [s1*s2*s1, s2*s1*s2],
             [s1*s2*s1*s2, s2*s1*s2*s1],
             [s1*s2*s1*s2*s1, s2*s1*s2*s1*s2],
             [s2*s1*s2*s1*s2*s1]]
        """

@cached_function
def build_differentials(W):
    """
    Construct the differentials for the BGG resolution corresponding
    to the Weyl group `W`.

    ALGORITHM:

    We use the fact that (parabolic) Bruhat order is built locally
    from squares, all values defining the differential are `+1` or `-1`,
    and the product over the two different paths must sum to `0`.
    This is outlined in Ch. 6 of [Humphreys08]_.

    This only depends on the Coxeter group `W`. There is no stabilizer
    for any dominant integral weight `\\lambda` undert the dot action
    (i.e., the stabilizer of `\\lambda + \\rho` is empty).

    EXAMPLES::

        sage: from sage.algebras.lie_algebras.bgg_resolution import build_differentials
        sage: W = WeylGroup(['B', 2], prefix='s')
        sage: D, O = build_differentials(W)
        sage: D
        {0: [],
         1: [-1  1],
         2: [1 1]
            [1 1],
         3: [ 1 -1]
            [-1  1],
         4: [1]
            [1],
         5: []}
        sage: O
        {0: [1],
         1: [s2, s1],
         2: [s2*s1, s1*s2],
         3: [s2*s1*s2, s1*s2*s1],
         4: [s2*s1*s2*s1]}
    """
