from sage.categories.algebras import Algebras as Algebras
from sage.categories.lie_algebras import LieAlgebras as LieAlgebras
from sage.combinat.free_module import CombinatorialFreeModule as CombinatorialFreeModule
from sage.monoids.indexed_free_monoid import IndexedFreeAbelianMonoid as IndexedFreeAbelianMonoid
from sage.sets.family import Family as Family

class AbelianLieAlgebra(CombinatorialFreeModule):
    """
    An example of a Lie algebra: the abelian Lie algebra.

    This class illustrates a minimal implementation of a Lie algebra with
    a distinguished basis.
    """
    def __init__(self, R, gens) -> None:
        """
        EXAMPLES::

            sage: L = LieAlgebras(QQ).WithBasis().example()
            sage: TestSuite(L).run()
        """
    def lie_algebra_generators(self):
        """
        Return the generators of ``self`` as a Lie algebra.

        EXAMPLES::

            sage: L = LieAlgebras(QQ).WithBasis().example()
            sage: L.lie_algebra_generators()
            Lazy family (Term map from Partitions to
             An example of a Lie algebra: the abelian Lie algebra on the
             generators indexed by Partitions over Rational
             Field(i))_{i in Partitions}
        """
    def bracket_on_basis(self, x, y):
        """
        Return the Lie bracket on basis elements indexed by ``x`` and ``y``.

        EXAMPLES::

            sage: L = LieAlgebras(QQ).WithBasis().example()
            sage: L.bracket_on_basis(Partition([4,1]), Partition([2,2,1]))
            0
        """
    class Element(CombinatorialFreeModule.Element):
        def lift(self):
            """
            Return the lift of ``self`` to the universal enveloping algebra.

            EXAMPLES::

                sage: L = LieAlgebras(QQ).WithBasis().example()
                sage: elt = L.an_element()
                sage: elt.lift()
                3*P[F[2]] + 2*P[F[1]] + 2*P[F[]]
            """
Example = AbelianLieAlgebra

class IndexedPolynomialRing(CombinatorialFreeModule):
    """
    Polynomial ring whose generators are indexed by an arbitrary set.

    .. TODO::

        Currently this is just used as the universal enveloping algebra
        for the example of the abelian Lie algebra. This should be
        factored out into a more complete class.
    """
    def __init__(self, R, indices, **kwds) -> None:
        """
        Initialize ``self``.

        EXAMPLES::

            sage: L = LieAlgebras(QQ).WithBasis().example()
            sage: UEA = L.universal_enveloping_algebra()
            sage: TestSuite(UEA).run()
        """
    def one_basis(self):
        """
        Return the index of element `1`.

        EXAMPLES::

            sage: L = LieAlgebras(QQ).WithBasis().example()
            sage: UEA = L.universal_enveloping_algebra()
            sage: UEA.one_basis()
            1
            sage: UEA.one_basis().parent()
            Free abelian monoid indexed by Partitions
        """
    def product_on_basis(self, x, y):
        """
        Return the product of the monomials indexed by ``x`` and ``y``.

        EXAMPLES::

            sage: L = LieAlgebras(QQ).WithBasis().example()
            sage: UEA = L.universal_enveloping_algebra()
            sage: I = UEA._indices
            sage: UEA.product_on_basis(I.an_element(), I.an_element())
            P[F[]^4*F[1]^4*F[2]^6]
        """
    def algebra_generators(self):
        """
        Return the algebra generators of ``self``.

        EXAMPLES::

            sage: L = LieAlgebras(QQ).WithBasis().example()
            sage: UEA = L.universal_enveloping_algebra()
            sage: UEA.algebra_generators()
            Lazy family (algebra generator map(i))_{i in Partitions}
        """
