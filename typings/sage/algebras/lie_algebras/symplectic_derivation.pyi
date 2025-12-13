from sage.algebras.lie_algebras.lie_algebra import InfinitelyGeneratedLieAlgebra as InfinitelyGeneratedLieAlgebra
from sage.algebras.lie_algebras.lie_algebra_element import LieAlgebraElement as LieAlgebraElement
from sage.categories.lie_algebras import LieAlgebras as LieAlgebras
from sage.combinat.partition import Partitions as Partitions
from sage.sets.disjoint_union_enumerated_sets import DisjointUnionEnumeratedSets as DisjointUnionEnumeratedSets
from sage.sets.family import Family as Family
from sage.sets.non_negative_integers import NonNegativeIntegers as NonNegativeIntegers
from sage.structure.indexed_generators import IndexedGenerators as IndexedGenerators

class SymplecticDerivationLieAlgebra(InfinitelyGeneratedLieAlgebra, IndexedGenerators):
    """
    The symplectic derivation Lie algebra.

    Fix a `g \\geq 4` and let `R` be a commutative ring. Let `H = R^{2g}`
    be equipped with a symplectic form `\\mu` with the basis
    `a_1, \\ldots, a_g, b_1, \\ldots, b_g` such that

    .. MATH::

        \\mu(a_i, a_j) = \\mu(b_i, b_j) = 0,
        \\qquad\\qquad
        \\mu(a_i, b_j) = -\\mu(b_j, a_i) = \\delta_{ij},

    for all `i, j`. The *symplectic derivation Lie algebra* is the Lie
    algebra

    .. MATH::

        \\mathfrak{c}_g := \\bigoplus_{w \\geq 0} S^{w+2} H

    with the Lie bracket on basis elements

    .. MATH::

        [x_1 \\cdots x_{m+2}, y_1 \\cdots y_{n+2}] =
        \\sum_{i,j} \\mu(x_i, y_j) x_1 \\cdots \\widehat{x}_i \\cdots x_{m+2}
        \\cdot y_1 \\cdots \\widehat{y}_j \\cdots y_{n+2},

    where `\\widehat{z}` denotes that factor is missing. When `R = \\QQ`, this
    corresponds to the classical Poisson bracket on `C^{\\infty}(\\RR^{2g})`
    restricted to polynomials with coefficients in `\\QQ`.

    EXAMPLES::

        sage: L = lie_algebras.SymplecticDerivation(QQ, 5)
        sage: elts = L.some_elements()
        sage: list(elts)
        [a1*a2, b1*b3, a1*a1*a2, b3*b4,
         a1*a4*b3, a1*a2 - 1/2*a1*a2*a2*a5 + a1*a1*a2*b1*b4]
        sage: [[elts[i].bracket(elts[j]) for i in range(len(elts))]
        ....:  for j in range(len(elts))]
        [[0, -a2*b3, 0, 0, 0, -a1*a1*a2*a2*b4],
         [a2*b3, 0, 2*a1*a2*b3, 0, a4*b3*b3, a2*b3 - 1/2*a2*a2*a5*b3 + 2*a1*a2*b1*b3*b4],
         [0, -2*a1*a2*b3, 0, 0, 0, -2*a1*a1*a1*a2*a2*b4],
         [0, 0, 0, 0, a1*b3*b3, 0],
         [0, -a4*b3*b3, 0, -a1*b3*b3, 0, -a1*a1*a1*a2*b1*b3 - a1*a1*a2*a4*b3*b4],
         [a1*a1*a2*a2*b4, -a2*b3 + 1/2*a2*a2*a5*b3 - 2*a1*a2*b1*b3*b4, 2*a1*a1*a1*a2*a2*b4,
          0, a1*a1*a1*a2*b1*b3 + a1*a1*a2*a4*b3*b4, 0]]
        sage: x = L.monomial(Partition([8,8,6,6,4,2,2,1,1,1])); x
        a1*a1*a1*a2*a2*a4*b1*b1*b3*b3
        sage: [L[x, elt] for elt in elts]
        [-2*a1*a1*a1*a2*a2*a2*a4*b1*b3*b3,
         3*a1*a1*a2*a2*a4*b1*b1*b3*b3*b3,
         -4*a1*a1*a1*a1*a2*a2*a2*a4*b1*b3*b3,
         a1*a1*a1*a2*a2*b1*b1*b3*b3*b3,
         -2*a1*a1*a1*a2*a2*a4*a4*b1*b3*b3*b3,
         -2*a1*a1*a1*a2*a2*a2*a4*b1*b3*b3 + a1*a1*a1*a2*a2*a2*a2*a4*a5*b1*b3*b3
          + a1*a1*a1*a1*a1*a2*a2*a2*b1*b1*b1*b3*b3 - a1*a1*a1*a1*a2*a2*a2*a4*b1*b1*b3*b3*b4]

    REFERENCES:

    - [Harako2020]_
    """
    def __init__(self, R, g) -> None:
        """
        Initialize ``self``.

        EXAMPLES::

            sage: L = lie_algebras.SymplecticDerivation(QQ, 5)
            sage: TestSuite(L).run()
        """
    def degree_on_basis(self, x):
        """
        Return the degree of the basis element indexed by ``x``.

        EXAMPLES::

            sage: L = lie_algebras.SymplecticDerivation(QQ, 5)
            sage: L.degree_on_basis([5,2,1])
            1
            sage: L.degree_on_basis([1,1])
            0
            sage: elt = L.monomial(Partition([5,5,2,1])) + 3*L.monomial(Partition([3,3,2,1]))
            sage: elt.degree()
            2
        """
    def bracket_on_basis(self, x, y):
        """
        Return the bracket of basis elements indexed by ``x`` and ``y``,
        where ``i < j``.

        EXAMPLES::

            sage: L = lie_algebras.SymplecticDerivation(QQ, 5)
            sage: L.bracket_on_basis([5,2,1], [5,1,1])
            0
            sage: L.bracket_on_basis([6,1], [3,1,1])
            -2*a1*a1*a3
            sage: L.bracket_on_basis([9,2,1], [4,1,1])
            -a1*a1*a1*a2
            sage: L.bracket_on_basis([5,5,2], [6,1,1])
            0
            sage: L.bracket_on_basis([5,5,5], [10,3])
            3*a3*a5*a5
            sage: L.bracket_on_basis([10,10,10], [5,3])
            -3*a3*b5*b5
        """
    def some_elements(self):
        """
        Return some elements of ``self``.

        EXAMPLES::

            sage: L = lie_algebras.SymplecticDerivation(QQ, 5)
            sage: L.some_elements()
            [a1*a2, b1*b3, a1*a1*a2, b3*b4, a1*a4*b3,
             a1*a2 - 1/2*a1*a2*a2*a5 + a1*a1*a2*b1*b4]
        """
    class Element(LieAlgebraElement): ...
