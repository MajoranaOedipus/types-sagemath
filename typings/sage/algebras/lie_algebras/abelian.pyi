from sage.algebras.lie_algebras.lie_algebra import InfinitelyGeneratedLieAlgebra as InfinitelyGeneratedLieAlgebra
from sage.algebras.lie_algebras.lie_algebra_element import LieAlgebraElement as LieAlgebraElement
from sage.algebras.lie_algebras.structure_coefficients import LieAlgebraWithStructureCoefficients as LieAlgebraWithStructureCoefficients
from sage.categories.lie_algebras import LieAlgebras as LieAlgebras
from sage.rings.infinity import infinity as infinity
from sage.rings.polynomial.polynomial_ring_constructor import PolynomialRing as PolynomialRing
from sage.sets.family import Family as Family
from sage.structure.indexed_generators import IndexedGenerators as IndexedGenerators, standardize_names_index_set as standardize_names_index_set

class AbelianLieAlgebra(LieAlgebraWithStructureCoefficients):
    """
    An abelian Lie algebra.

    A Lie algebra `\\mathfrak{g}` is abelian if `[x, y] = 0` for all
    `x, y \\in \\mathfrak{g}`.

    EXAMPLES::

        sage: L.<x, y> = LieAlgebra(QQ, abelian=True)
        sage: L.bracket(x, y)
        0
    """
    @staticmethod
    def __classcall_private__(cls, R, names=None, index_set=None, category=None, **kwds):
        """
        Normalize input to ensure a unique representation.

        TESTS::

            sage: L1 = LieAlgebra(QQ, 'x,y', {})
            sage: L2.<x, y> = LieAlgebra(QQ, abelian=True)
            sage: L1 is L2
            True
        """
    def __init__(self, R, names, index_set, category, **kwds) -> None:
        """
        Initialize ``self``.

        EXAMPLES::

            sage: L = LieAlgebra(QQ, 3, 'x', abelian=True)
            sage: TestSuite(L).run()
        """
    def is_abelian(self):
        """
        Return ``True`` since ``self`` is an abelian Lie algebra.

        EXAMPLES::

            sage: L = LieAlgebra(QQ, 3, 'x', abelian=True)
            sage: L.is_abelian()
            True
        """
    is_nilpotent = is_abelian
    is_solvable = is_abelian
    class Element(LieAlgebraWithStructureCoefficients.Element): ...

class InfiniteDimensionalAbelianLieAlgebra(InfinitelyGeneratedLieAlgebra, IndexedGenerators):
    """
    An infinite dimensional abelian Lie algebra.

    A Lie algebra `\\mathfrak{g}` is abelian if `[x, y] = 0` for all
    `x, y \\in \\mathfrak{g}`.
    """
    def __init__(self, R, index_set, prefix: str = 'L', **kwds) -> None:
        """
        Initialize ``self``.

        EXAMPLES::

            sage: L = LieAlgebra(QQ, index_set=ZZ, abelian=True)
            sage: TestSuite(L).run()
        """
    def dimension(self):
        """
        Return the dimension of ``self``, which is `\\infty`.

        EXAMPLES::

            sage: L = lie_algebras.abelian(QQ, index_set=ZZ)
            sage: L.dimension()
            +Infinity
        """
    def is_abelian(self):
        """
        Return ``True`` since ``self`` is an abelian Lie algebra.

        EXAMPLES::

            sage: L = lie_algebras.abelian(QQ, index_set=ZZ)
            sage: L.is_abelian()
            True
        """
    is_nilpotent = is_abelian
    is_solvable = is_abelian
    class Element(LieAlgebraElement): ...
