from sage.algebras.lie_algebras.lie_algebra import InfinitelyGeneratedLieAlgebra as InfinitelyGeneratedLieAlgebra
from sage.algebras.lie_algebras.lie_algebra_element import LieAlgebraElement as LieAlgebraElement
from sage.categories.lie_algebras import LieAlgebras as LieAlgebras
from sage.misc.cachefunc import cached_method as cached_method
from sage.rings.integer_ring import ZZ as ZZ
from sage.sets.disjoint_union_enumerated_sets import DisjointUnionEnumeratedSets as DisjointUnionEnumeratedSets
from sage.sets.family import Family as Family
from sage.sets.finite_enumerated_set import FiniteEnumeratedSet as FiniteEnumeratedSet
from sage.structure.indexed_generators import IndexedGenerators as IndexedGenerators

class RankTwoHeisenbergVirasoro(InfinitelyGeneratedLieAlgebra, IndexedGenerators):
    """
    The rank 2 Heisenberg-Virasoro algebra.

    The *rank 2 Heisenberg-Virasoro* (Lie) algebra is the Lie algebra
    `L` spaned by the elements

    .. MATH::

        \\{t^{\\alpha}, E(\\alpha) \\mid \\alpha \\in \\ZZ^2 \\setminus \\{(0,0)\\} \\}
        \\cup \\{K_1, K_2, K_3, K_4\\},

    which satisfy the relations

    .. MATH::

        \\begin{aligned}
        \\mbox{ } [t^{\\alpha}, t^{\\beta}] & = [K_i, L] = 0,
        \\\\\n        [t^{\\alpha}, E(\\beta)] & =
          \\det\\begin{pmatrix} \\beta \\\\ \\alpha \\end{pmatrix} t^{\\alpha+\\beta}
          + \\delta_{\\alpha,-\\beta} (\\alpha_1 K_1 + \\alpha_2 K_2),
        \\\\\n        [E(\\alpha), E(\\beta)] & =
          \\det\\begin{pmatrix} \\beta \\\\ \\alpha \\end{pmatrix} E(\\alpha+\\beta)
          + \\delta_{\\alpha,-\\beta} (\\alpha_1 K_3 + \\alpha_2 K_4),
        \\end{aligned}

    where `\\alpha = (\\alpha_1, \\alpha_2)` and `\\delta_{xy}` is the
    Kronecker delta.

    EXAMPLES::

        sage: L = lie_algebras.RankTwoHeisenbergVirasoro(QQ)
        sage: K1,K2,K3,K4 = L.K()
        sage: E2m1 = L.E(2,-1)
        sage: Em21 = L.E(-2,1)
        sage: t2m1 = L.t(2,-1)
        sage: t53 = L.t(5,3)

        sage: Em21.bracket(t2m1)
        -2*K1 + K2
        sage: t53.bracket(E2m1)
        11*t(7, 2)
        sage: E2m1.bracket(Em21)
        2*K3 - K4
        sage: E2m1.bracket(t2m1)
        0

        sage: all(x.bracket(y) == 0 for x in [K1,K2,K3,K4] for y in [E2m1, Em21, t2m1])
        True

    REFERENCES:

    - [LT2018]_
    """
    def __init__(self, R) -> None:
        """
        Initialize ``self``.

        EXAMPLES::

            sage: L = lie_algebras.RankTwoHeisenbergVirasoro(QQ)
            sage: TestSuite(L).run()
        """
    @cached_method
    def K(self, i=None):
        """
        Return the basis element `K_i` of ``self``.

        EXAMPLES::

            sage: L = lie_algebras.RankTwoHeisenbergVirasoro(QQ)
            sage: L.K(1)
            K1
            sage: list(L.K())
            [K1, K2, K3, K4]
        """
    def t(self, a, b):
        """
        Return the basis element `t^{(a,b)}` of ``self``.

        EXAMPLES::

            sage: L = lie_algebras.RankTwoHeisenbergVirasoro(QQ)
            sage: L.t(1,-2)
            t(1, -2)
        """
    def E(self, a, b):
        """
        Return the basis element `E(a,b)` of ``self``.

        EXAMPLES::

            sage: L = lie_algebras.RankTwoHeisenbergVirasoro(QQ)
            sage: L.E(1,-2)
            E(1, -2)
        """
    def bracket_on_basis(self, i, j):
        """
        Return the bracket of basis elements indexed by ``i`` and ``j``,
        where ``i < j``.

        EXAMPLES::

            sage: L = lie_algebras.RankTwoHeisenbergVirasoro(QQ)
            sage: v = L._v
            sage: L.bracket_on_basis(('K',2), ('t', v(3,-1)))
            0
            sage: L.bracket_on_basis(('K', 4), ('E', v(3,-1)))
            0
            sage: L.bracket_on_basis(('t', v(3,-1)), ('t', v(4,3)))
            0
            sage: L.bracket_on_basis(('t', v(3,-1)), ('E', v(4,3)))
            -13*t(7, 2)
            sage: L.bracket_on_basis(('t', v(2,2)),  ('E', v(1,1)))
            0
            sage: L.bracket_on_basis(('t', v(3,-1)), ('E', v(-3,1)))
            3*K1 - K2
            sage: L.bracket_on_basis(('E', v(3,-1)), ('E', v(4,3)))
            -13*E(7, 2)
            sage: L.bracket_on_basis(('E', v(2,2)),  ('E', v(1,1)))
            0
            sage: L.bracket_on_basis(('E', v(3,-1)), ('E', v(-3,1)))
            3*K3 - K4
        """
    def some_elements(self):
        """
        Return some elements of ``self``.

        EXAMPLES::

            sage: L = lie_algebras.RankTwoHeisenbergVirasoro(QQ)
            sage: L.some_elements()
            [E(1, 1), E(-2, -2), E(0, 1),
             t(1, 1), t(4, -1), t(2, 3),
             K2, K4,
             K3 - 1/2*t(-1, 3) + E(1, -3) + E(2, 2)]
        """
    class Element(LieAlgebraElement): ...
