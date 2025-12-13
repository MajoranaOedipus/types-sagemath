from sage.categories.hopf_algebras_with_basis import HopfAlgebrasWithBasis as HopfAlgebrasWithBasis
from sage.categories.tensor import tensor as tensor
from sage.combinat.free_module import CombinatorialFreeModule as CombinatorialFreeModule
from sage.misc.cachefunc import cached_method as cached_method
from sage.sets.family import Family as Family

class MyGroupAlgebra(CombinatorialFreeModule):
    """
    An example of a Hopf algebra with basis: the group algebra of a group.

    This class illustrates a minimal implementation of a Hopf algebra with basis.
    """
    def __init__(self, R, G) -> None:
        """
        EXAMPLES::

            sage: from sage.categories.examples.hopf_algebras_with_basis import MyGroupAlgebra
            sage: A = MyGroupAlgebra(QQ, DihedralGroup(6))
            sage: A.category()
            Category of finite dimensional Hopf algebras with basis over Rational Field
            sage: TestSuite(A).run()
        """
    @cached_method
    def one_basis(self):
        """
        Return the one of the group, which index the one of this algebra,
        as per :meth:`AlgebrasWithBasis.ParentMethods.one_basis`.

        EXAMPLES::

            sage: A = HopfAlgebrasWithBasis(QQ).example()
            sage: A.one_basis()
            ()
            sage: A.one()
            B[()]
        """
    def product_on_basis(self, g1, g2):
        """
        Product, on basis elements, as per
        :meth:`AlgebrasWithBasis.ParentMethods.product_on_basis`.

        The product of two basis elements is induced by the product of
        the corresponding elements of the group.

        EXAMPLES::

            sage: A = HopfAlgebrasWithBasis(QQ).example()
            sage: (a, b) = A._group.gens()
            sage: a*b
            (1,2)
            sage: A.product_on_basis(a, b)
            B[(1,2)]
        """
    @cached_method
    def algebra_generators(self):
        """
        Return the generators of this algebra, as per :meth:`~.magmatic_algebras.MagmaticAlgebras.ParentMethods.algebra_generators`.

        They correspond to the generators of the group.

        EXAMPLES::

            sage: A = HopfAlgebrasWithBasis(QQ).example(); A
            An example of Hopf algebra with basis: the group algebra of the Dihedral group of order 6 as a permutation group over Rational Field
            sage: A.algebra_generators()
            Finite family {(1,2,3): B[(1,2,3)], (1,3): B[(1,3)]}
        """
    def coproduct_on_basis(self, g):
        """
        Coproduct, on basis elements, as per :meth:`HopfAlgebrasWithBasis.ParentMethods.coproduct_on_basis`.

        The basis elements are group like: `\\Delta(g) = g \\otimes g`.

        EXAMPLES::

            sage: A = HopfAlgebrasWithBasis(QQ).example()
            sage: (a, b) = A._group.gens()
            sage: A.coproduct_on_basis(a)
            B[(1,2,3)] # B[(1,2,3)]
        """
    def counit_on_basis(self, g):
        """
        Counit, on basis elements, as per :meth:`HopfAlgebrasWithBasis.ParentMethods.counit_on_basis`.

        The counit on the basis elements is 1.

        EXAMPLES::

            sage: A = HopfAlgebrasWithBasis(QQ).example()
            sage: (a, b) = A._group.gens()
            sage: A.counit_on_basis(a)
            1
        """
    def antipode_on_basis(self, g):
        """
        Antipode, on basis elements, as per :meth:`HopfAlgebrasWithBasis.ParentMethods.antipode_on_basis`.

        It is given, on basis elements, by `\\nu(g) = g^{-1}`

        EXAMPLES::

            sage: A = HopfAlgebrasWithBasis(QQ).example()
            sage: (a, b) = A._group.gens()
            sage: A.antipode_on_basis(a)
            B[(1,3,2)]
        """
