from _typeshed import Incomplete
from sage.categories.category_with_axiom import CategoryWithAxiom_over_base_ring as CategoryWithAxiom_over_base_ring
from sage.categories.filtered_modules import FilteredModulesCategory as FilteredModulesCategory
from sage.categories.homset import Hom as Hom
from sage.categories.modules_with_basis import ModulesWithBasis as ModulesWithBasis
from sage.categories.super_modules import SuperModulesCategory as SuperModulesCategory
from sage.categories.tensor import tensor as tensor
from sage.misc.abstract_method import abstract_method as abstract_method
from sage.misc.lazy_attribute import lazy_attribute as lazy_attribute
from sage.misc.lazy_import import LazyImport as LazyImport

class CoalgebrasWithBasis(CategoryWithAxiom_over_base_ring):
    """
    The category of coalgebras with a distinguished basis.

    EXAMPLES::

        sage: CoalgebrasWithBasis(ZZ)
        Category of coalgebras with basis over Integer Ring
        sage: sorted(CoalgebrasWithBasis(ZZ).super_categories(), key=str)
        [Category of coalgebras over Integer Ring,
         Category of modules with basis over Integer Ring]

    TESTS::

        sage: TestSuite(CoalgebrasWithBasis(ZZ)).run()
    """
    Graded: Incomplete
    class Filtered(FilteredModulesCategory):
        """
        Category of filtered coalgebras.
        """
    class ParentMethods:
        def coproduct_on_basis(self, i) -> None:
            """
            The coproduct of the algebra on the basis (optional).

            INPUT:

            - ``i`` -- the indices of an element of the basis of ``self``

            Returns the coproduct of the corresponding basis elements
            If implemented, the coproduct of the algebra is defined
            from it by linearity.

            EXAMPLES::

                sage: A = HopfAlgebrasWithBasis(QQ).example(); A                        # needs sage.groups sage.modules
                An example of Hopf algebra with basis:
                 the group algebra of the Dihedral group of order 6
                  as a permutation group over Rational Field
                sage: (a, b) = A._group.gens()                                          # needs sage.groups sage.modules
                sage: A.coproduct_on_basis(a)                                           # needs sage.groups sage.modules
                B[(1,2,3)] # B[(1,2,3)]
            """
        @lazy_attribute
        def coproduct(self):
            """
            If :meth:`coproduct_on_basis` is available, construct the
            coproduct morphism from ``self`` to ``self`` `\\otimes`
            ``self`` by extending it by linearity. Otherwise, use
            :meth:`~Coalgebras.Realizations.ParentMethods.coproduct_by_coercion`,
            if available.

            EXAMPLES::

                sage: # needs sage.groups sage.modules
                sage: A = HopfAlgebrasWithBasis(QQ).example(); A
                An example of Hopf algebra with basis:
                 the group algebra of the Dihedral group of order 6
                  as a permutation group over Rational Field
                sage: a, b = A.algebra_generators()
                sage: a, A.coproduct(a)
                (B[(1,2,3)], B[(1,2,3)] # B[(1,2,3)])
                sage: b, A.coproduct(b)
                (B[(1,3)], B[(1,3)] # B[(1,3)])
            """
        def counit_on_basis(self, i) -> None:
            """
            The counit of the algebra on the basis (optional).

            INPUT:

            - ``i`` -- the indices of an element of the basis of ``self``

            Returns the counit of the corresponding basis elements
            If implemented, the counit of the algebra is defined
            from it by linearity.

            EXAMPLES::

                sage: A = HopfAlgebrasWithBasis(QQ).example(); A                        # needs sage.groups sage.modules
                An example of Hopf algebra with basis:
                 the group algebra of the Dihedral group of order 6
                  as a permutation group over Rational Field
                sage: (a, b) = A._group.gens()                                          # needs sage.groups sage.modules
                sage: A.counit_on_basis(a)                                              # needs sage.groups sage.modules
                1
            """
        @lazy_attribute
        def counit(self):
            """
            If :meth:`counit_on_basis` is available, construct the
            counit morphism from ``self`` to ``self`` `\\otimes`
            ``self`` by extending it by linearity

            EXAMPLES::

                sage: # needs sage.groups sage.modules
                sage: A = HopfAlgebrasWithBasis(QQ).example(); A
                An example of Hopf algebra with basis:
                 the group algebra of the Dihedral group of order 6
                  as a permutation group over Rational Field
                sage: a, b = A.algebra_generators()
                sage: a, A.counit(a)
                (B[(1,2,3)], 1)
                sage: b, A.counit(b)
                (B[(1,3)], 1)
            """
    class ElementMethods:
        def coproduct_iterated(self, n: int = 1):
            """
            Apply ``n`` coproducts to ``self``.

            .. TODO::

                Remove dependency on ``modules_with_basis`` methods.

            EXAMPLES::

                sage: Psi = NonCommutativeSymmetricFunctions(QQ).Psi()                  # needs sage.combinat sage.modules
                sage: Psi[2,2].coproduct_iterated(0)                                    # needs sage.combinat sage.modules
                Psi[2, 2]
                sage: Psi[2,2].coproduct_iterated(2)                                    # needs sage.combinat sage.modules
                Psi[] # Psi[] # Psi[2, 2] + 2*Psi[] # Psi[2] # Psi[2]
                 + Psi[] # Psi[2, 2] # Psi[] + 2*Psi[2] # Psi[] # Psi[2]
                 + 2*Psi[2] # Psi[2] # Psi[] + Psi[2, 2] # Psi[] # Psi[]

            TESTS::

                sage: p = SymmetricFunctions(QQ).p()                                    # needs sage.combinat sage.modules
                sage: p[5,2,2].coproduct_iterated()                                     # needs sage.combinat sage.modules
                p[] # p[5, 2, 2] + 2*p[2] # p[5, 2] + p[2, 2] # p[5]
                 + p[5] # p[2, 2] + 2*p[5, 2] # p[2] + p[5, 2, 2] # p[]
                sage: p([]).coproduct_iterated(3)                                       # needs sage.combinat sage.modules
                p[] # p[] # p[] # p[]

            ::

                sage: Psi = NonCommutativeSymmetricFunctions(QQ).Psi()                  # needs sage.combinat sage.modules
                sage: Psi[2,2].coproduct_iterated(0)                                    # needs sage.combinat sage.modules
                Psi[2, 2]
                sage: Psi[2,2].coproduct_iterated(3)                                    # needs sage.combinat sage.modules
                Psi[] # Psi[] # Psi[] # Psi[2, 2] + 2*Psi[] # Psi[] # Psi[2] # Psi[2]
                 + Psi[] # Psi[] # Psi[2, 2] # Psi[] + 2*Psi[] # Psi[2] # Psi[] # Psi[2]
                 + 2*Psi[] # Psi[2] # Psi[2] # Psi[] + Psi[] # Psi[2, 2] # Psi[] # Psi[]
                 + 2*Psi[2] # Psi[] # Psi[] # Psi[2] + 2*Psi[2] # Psi[] # Psi[2] # Psi[]
                 + 2*Psi[2] # Psi[2] # Psi[] # Psi[] + Psi[2, 2] # Psi[] # Psi[] # Psi[]

            ::

                sage: # needs sage.combinat sage.graphs sage.modules
                sage: m = SymmetricFunctionsNonCommutingVariables(QQ).m()
                sage: m[[1,3],[2]].coproduct_iterated(2)
                m{} # m{} # m{{1, 3}, {2}} + m{} # m{{1}} # m{{1, 2}}
                 + m{} # m{{1, 2}} # m{{1}} + m{} # m{{1, 3}, {2}} # m{}
                 + m{{1}} # m{} # m{{1, 2}} + m{{1}} # m{{1, 2}} # m{}
                 + m{{1, 2}} # m{} # m{{1}} + m{{1, 2}} # m{{1}} # m{}
                 + m{{1, 3}, {2}} # m{} # m{}
                sage: m[[]].coproduct_iterated(3), m[[1,3],[2]].coproduct_iterated(0)
                (m{} # m{} # m{} # m{}, m{{1, 3}, {2}})
            """
    class Super(SuperModulesCategory):
        def extra_super_categories(self):
            """
            EXAMPLES::

                sage: C = Coalgebras(ZZ).WithBasis().Super()
                sage: sorted(C.super_categories(), key=str)  # indirect doctest
                [Category of graded coalgebras with basis over Integer Ring,
                 Category of super coalgebras over Integer Ring,
                 Category of super modules with basis over Integer Ring]
            """
