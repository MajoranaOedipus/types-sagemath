from sage.categories.algebras import Algebras as Algebras
from sage.combinat.free_module import CombinatorialFreeModule as CombinatorialFreeModule
from sage.misc.cachefunc import cached_method as cached_method
from typing import Self

class CellularBasis(CombinatorialFreeModule):
    """
    The cellular basis of a cellular algebra, in the sense of
    Graham and Lehrer [GrLe1996]_.

    INPUT:

    - ``A`` -- the cellular algebra

    EXAMPLES:

    We compute a cellular basis and do some basic computations::

        sage: S = SymmetricGroupAlgebra(QQ, 3)
        sage: C = S.cellular_basis()
        sage: C
        Cellular basis of Symmetric group algebra of order 3
         over Rational Field
        sage: len(C.basis())
        6
        sage: len(S.basis())
        6
        sage: a,b,c,d,e,f = C.basis()
        sage: f
        C([3], [[1, 2, 3]], [[1, 2, 3]])
        sage: c
        C([2, 1], [[1, 3], [2]], [[1, 2], [3]])
        sage: d
        C([2, 1], [[1, 2], [3]], [[1, 3], [2]])
        sage: f * f
        C([3], [[1, 2, 3]], [[1, 2, 3]])
        sage: f * c
        0
        sage: d * c
        C([2, 1], [[1, 2], [3]], [[1, 2], [3]])
        sage: c * d
        C([2, 1], [[1, 3], [2]], [[1, 3], [2]])
        sage: S(f)
        1/6*[1, 2, 3] + 1/6*[1, 3, 2] + 1/6*[2, 1, 3] + 1/6*[2, 3, 1]
         + 1/6*[3, 1, 2] + 1/6*[3, 2, 1]
        sage: S(d)
        1/4*[1, 3, 2] - 1/4*[2, 3, 1] + 1/4*[3, 1, 2] - 1/4*[3, 2, 1]
        sage: B = list(S.basis())
        sage: B[2]
        [2, 1, 3]
        sage: C(B[2])
        -C([1, 1, 1], [[1], [2], [3]], [[1], [2], [3]])
         + C([2, 1], [[1, 2], [3]], [[1, 2], [3]])
         - C([2, 1], [[1, 3], [2]], [[1, 3], [2]])
         + C([3], [[1, 2, 3]], [[1, 2, 3]])
    """
    def __init__(self, A, to_algebra=None, from_algebra=None, **kwargs) -> None:
        """
        Initialize ``self``.

        EXAMPLES::

            sage: S = SymmetricGroupAlgebra(QQ, 3)
            sage: C = S.cellular_basis()
            sage: TestSuite(C).run()
        """
    def cellular_basis_of(self):
        """
        Return the defining algebra of ``self``.

        EXAMPLES::

            sage: S = SymmetricGroupAlgebra(QQ, 3)
            sage: C = S.cellular_basis()
            sage: C.cellular_basis_of() is S
            True
        """
    def cell_poset(self):
        """
        Return the cell poset of ``self``.

        EXAMPLES::

            sage: S = SymmetricGroupAlgebra(QQ, 3)
            sage: C = S.cellular_basis()
            sage: C.cell_poset()
            Finite poset containing 3 elements
        """
    def cell_module_indices(self, la):
        """
        Return the indices of the cell module of ``self``
        indexed by ``la`` .

        This is the finite set `M(\\lambda)`.

        EXAMPLES::

            sage: S = SymmetricGroupAlgebra(QQ, 3)
            sage: C = S.cellular_basis()
            sage: C.cell_module_indices([2,1])
            Standard tableaux of shape [2, 1]
        """
    def cellular_basis(self) -> Self:
        """
        Return the cellular basis of ``self``, which is ``self``.

        EXAMPLES::

            sage: S = SymmetricGroupAlgebra(QQ, 3)
            sage: C = S.cellular_basis()
            sage: C.cellular_basis() is C
            True
        """
    @cached_method
    def one(self):
        """
        Return the element `1` in ``self``.

        EXAMPLES::

            sage: S = SymmetricGroupAlgebra(QQ, 3)
            sage: C = S.cellular_basis()
            sage: C.one()
            C([1, 1, 1], [[1], [2], [3]], [[1], [2], [3]])
             + C([2, 1], [[1, 2], [3]], [[1, 2], [3]])
             + C([2, 1], [[1, 3], [2]], [[1, 3], [2]])
             + C([3], [[1, 2, 3]], [[1, 2, 3]])
        """
    @cached_method
    def product_on_basis(self, x, y):
        """
        Return the product of basis indices by ``x`` and ``y``.

        EXAMPLES::

            sage: S = SymmetricGroupAlgebra(QQ, 3)
            sage: C = S.cellular_basis()
            sage: la = Partition([2,1])
            sage: s = StandardTableau([[1,2],[3]])
            sage: t = StandardTableau([[1,3],[2]])
            sage: C.product_on_basis((la, s, t), (la, s, t))
            0

        TESTS::

            sage: C5.<z5> = CyclotomicField(5)
            sage: TL = TemperleyLiebAlgebra(2, z5 + ~z5, C5)
            sage: m = TL.cell_module(0)
            sage: c = m.basis().keys()[0]
            sage: B = TL.cellular_basis()
            sage: B.product_on_basis((0, c, c), (0, c, c))
            (-z5^3-z5^2-1)*C(0, {{1, 2}}, {{1, 2}})

            sage: p = TL(B.monomial((0,c,c))) * TL(B.monomial((0,c,c)))
        """
