from _typeshed import Incomplete
from sage.categories.category_with_axiom import CategoryWithAxiom_over_base_ring as CategoryWithAxiom_over_base_ring
from sage.categories.tensor import TensorProductsCategory as TensorProductsCategory
from sage.misc.abstract_method import abstract_method as abstract_method
from sage.misc.cachefunc import cached_method as cached_method
from sage.misc.lazy_attribute import lazy_attribute as lazy_attribute
from sage.misc.lazy_import import LazyImport as LazyImport

class HopfAlgebrasWithBasis(CategoryWithAxiom_over_base_ring):
    """
    The category of Hopf algebras with a distinguished basis.

    EXAMPLES::

        sage: C = HopfAlgebrasWithBasis(QQ)
        sage: C
        Category of Hopf algebras with basis over Rational Field
        sage: C.super_categories()
        [Category of Hopf algebras over Rational Field,
         Category of bialgebras with basis over Rational Field]

    We now show how to use a simple Hopf algebra, namely the group algebra of the dihedral group
    (see also AlgebrasWithBasis)::

        sage: A = C.example(); A                                                        # needs sage.groups
        An example of Hopf algebra with basis: the group algebra of the
         Dihedral group of order 6 as a permutation group over Rational Field
        sage: A.rename('A')                                                             # needs sage.groups
        sage: A.category()                                                              # needs sage.groups
        Category of finite dimensional Hopf algebras with basis over Rational Field

        sage: A.one_basis()                                                             # needs sage.groups
        ()
        sage: A.one()                                                                   # needs sage.groups
        B[()]

        sage: A.base_ring()                                                             # needs sage.groups
        Rational Field
        sage: A.basis().keys()                                                          # needs sage.groups
        Dihedral group of order 6 as a permutation group

        sage: # needs sage.groups
        sage: [a,b] = A.algebra_generators()
        sage: a, b
        (B[(1,2,3)], B[(1,3)])
        sage: a^3, b^2
        (B[()], B[()])
        sage: a*b
        B[(1,2)]

        sage: A.product           # todo: not quite ...                                 # needs sage.groups
        <bound method MagmaticAlgebras.WithBasis.ParentMethods._product_from_product_on_basis_multiply of A>
        sage: A.product(b, b)                                                           # needs sage.groups
        B[()]

        sage: A.zero().coproduct()                                                      # needs sage.groups
        0
        sage: A.zero().coproduct().parent()                                             # needs sage.groups
        A # A
        sage: a.coproduct()                                                             # needs sage.groups
        B[(1,2,3)] # B[(1,2,3)]

        sage: TestSuite(A).run(verbose=True)                                            # needs sage.groups
        running ._test_additive_associativity() . . . pass
        running ._test_an_element() . . . pass
        running ._test_antipode() . . . pass
        running ._test_associativity() . . . pass
        running ._test_cardinality() . . . pass
        running ._test_category() . . . pass
        running ._test_characteristic() . . . pass
        running ._test_construction() . . . pass
        running ._test_distributivity() . . . pass
        running ._test_elements() . . .
          Running the test suite of self.an_element()
          running ._test_category() . . . pass
          running ._test_eq() . . . pass
          running ._test_monomial_coefficients() . . . pass
          running ._test_new() . . . pass
          running ._test_nonzero_equal() . . . pass
          running ._test_not_implemented_methods() . . . pass
          running ._test_pickling() . . . pass
          pass
        running ._test_elements_eq_reflexive() . . . pass
        running ._test_elements_eq_symmetric() . . . pass
        running ._test_elements_eq_transitive() . . . pass
        running ._test_elements_neq() . . . pass
        running ._test_eq() . . . pass
        running ._test_new() . . . pass
        running ._test_not_implemented_methods() . . . pass
        running ._test_one() . . . pass
        running ._test_pickling() . . . pass
        running ._test_prod() . . . pass
        running ._test_some_elements() . . . pass
        running ._test_zero() . . . pass
        sage: A.__class__                                                               # needs sage.groups
        <class 'sage.categories.examples.hopf_algebras_with_basis.MyGroupAlgebra_with_category'>
        sage: A.element_class                                                           # needs sage.groups
        <class 'sage.categories.examples.hopf_algebras_with_basis.MyGroupAlgebra_with_category.element_class'>

    Let us look at the code for implementing A::

        sage: A??                               # not implemented                       # needs sage.groups

    TESTS::

        sage: TestSuite(A).run()                                                        # needs sage.groups
        sage: TestSuite(C).run()
    """
    def example(self, G=None):
        """
        Return an example of algebra with basis::

            sage: HopfAlgebrasWithBasis(QQ['x']).example()                              # needs sage.groups
            An example of Hopf algebra with basis: the group algebra of the
            Dihedral group of order 6 as a permutation group
            over Univariate Polynomial Ring in x over Rational Field

        An other group can be specified as optional argument::

            sage: HopfAlgebrasWithBasis(QQ).example(SymmetricGroup(4))                  # needs sage.groups
            An example of Hopf algebra with basis: the group algebra of the
            Symmetric group of order 4! as a permutation group over Rational Field
        """
    FiniteDimensional: Incomplete
    Filtered: Incomplete
    Graded: Incomplete
    Super: Incomplete
    class ParentMethods:
        def antipode_on_basis(self, x) -> None:
            """
            The antipode of the Hopf algebra on the basis (optional).

            INPUT:

            - ``x`` -- an index of an element of the basis of ``self``

            Returns the antipode of the basis element indexed by ``x``.

            If this method is implemented, then :meth:`antipode` is defined
            from this by linearity.

            EXAMPLES::

                sage: # needs sage.groups
                sage: A = HopfAlgebrasWithBasis(QQ).example()
                sage: W = A.basis().keys(); W
                Dihedral group of order 6 as a permutation group
                sage: w = W.gen(0); w
                (1,2,3)
                sage: A.antipode_on_basis(w)
                B[(1,3,2)]
            """
        @lazy_attribute
        def antipode(self):
            """
            The antipode of this Hopf algebra.

            If :meth:`.antipode_basis` is available, this constructs the
            antipode morphism from ``self`` to ``self`` by extending it by
            linearity. Otherwise, :meth:`self.antipode_by_coercion` is used, if
            available.

            EXAMPLES::

                sage: # needs sage.groups
                sage: A = HopfAlgebrasWithBasis(ZZ).example(); A
                An example of Hopf algebra with basis: the group algebra of the
                 Dihedral group of order 6 as a permutation group over Integer Ring
                sage: A = HopfAlgebrasWithBasis(QQ).example()
                sage: [a,b] = A.algebra_generators()
                sage: a, A.antipode(a)
                (B[(1,2,3)], B[(1,3,2)])
                sage: b, A.antipode(b)
                (B[(1,3)], B[(1,3)])

            TESTS::

                sage: all(A.antipode(x) * x == A.one() for x in A.basis())              # needs sage.groups
                True
            """
    class ElementMethods: ...
    class TensorProducts(TensorProductsCategory):
        """
        The category of Hopf algebras with basis constructed by tensor product of Hopf algebras with basis
        """
        @cached_method
        def extra_super_categories(self):
            """
            EXAMPLES::

                sage: C = HopfAlgebrasWithBasis(QQ).TensorProducts()
                sage: C.extra_super_categories()
                [Category of Hopf algebras with basis over Rational Field]
                sage: sorted(C.super_categories(), key=str)
                [Category of Hopf algebras with basis over Rational Field,
                 Category of tensor products of Hopf algebras over Rational Field,
                 Category of tensor products of algebras with basis over Rational Field]
            """
        class ParentMethods: ...
        class ElementMethods: ...
