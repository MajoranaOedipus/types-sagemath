from sage.categories.category_with_axiom import CategoryWithAxiom_over_base_ring as CategoryWithAxiom_over_base_ring
from sage.categories.filtered_modules import FilteredModulesCategory as FilteredModulesCategory
from sage.categories.tensor import tensor as tensor
from sage.categories.with_realizations import WithRealizationsCategory as WithRealizationsCategory
from sage.misc.cachefunc import cached_method as cached_method

class FilteredHopfAlgebrasWithBasis(FilteredModulesCategory):
    """
    The category of filtered Hopf algebras with a distinguished basis.

    A filtered Hopf algebra with basis over a commutative ring `R`
    is a filtered Hopf algebra over `R` (that is, a Hopf algebra
    equipped with a module filtration such that all structure
    maps of the Hopf algebra respect the filtration) equipped with
    an `R`-module basis that makes it a filtered `R`-module with
    basis (see
    :class:`~sage.categories.filtered_modules_with_basis.FilteredModulesWithBasis`
    for the notion of a filtered module with basis).

    EXAMPLES::

        sage: C = HopfAlgebrasWithBasis(ZZ).Filtered(); C
        Category of filtered Hopf algebras with basis over Integer Ring
        sage: C.super_categories()
        [Category of Hopf algebras with basis over Integer Ring,
         Category of filtered algebras with basis over Integer Ring,
         Category of filtered coalgebras with basis over Integer Ring]

        sage: C is HopfAlgebras(ZZ).WithBasis().Filtered()
        True
        sage: C is HopfAlgebras(ZZ).Filtered().WithBasis()
        False

    TESTS::

        sage: TestSuite(C).run()
    """
    class WithRealizations(WithRealizationsCategory):
        @cached_method
        def super_categories(self):
            """
            EXAMPLES::

                sage: HopfAlgebrasWithBasis(QQ).Filtered().WithRealizations().super_categories()
                [Join of Category of Hopf algebras over Rational Field
                     and Category of filtered algebras over Rational Field
                     and Category of filtered coalgebras over Rational Field]

            TESTS::

                sage: TestSuite(HopfAlgebrasWithBasis(QQ).Filtered().WithRealizations()).run()
            """
    class Connected(CategoryWithAxiom_over_base_ring):
        class ParentMethods:
            @cached_method
            def antipode_on_basis(self, index):
                """
                The antipode on the basis element indexed by ``index``.

                INPUT:

                - ``index`` -- an element of the index set

                For a filtered connected Hopf algebra, we can define
                an antipode recursively by

                .. MATH::

                    S(x) := -\\sum_{x^L \\neq x} S(x^L) \\times x^R + \\epsilon(x)

                for all `x`, using the Sweedler notation.
                Also, `S(x) = x` for all `x` with `|x| = 0`.

                TESTS::

                    sage: # needs sage.modules
                    sage: H = GradedHopfAlgebrasWithBasis(QQ).Connected().example()
                    sage: H.monomial(0).antipode()  # indirect doctest
                    P0
                    sage: H.monomial(1).antipode()  # indirect doctest
                    -P1
                    sage: H.monomial(2).antipode()  # indirect doctest
                    P2
                    sage: H.monomial(3).antipode()  # indirect doctest
                    -P3
                """
            def antipode(self, elem):
                """
                Return the antipode of ``self`` applied to ``elem``.

                TESTS::

                    sage: H = GradedHopfAlgebrasWithBasis(QQ).Connected().example()     # needs sage.modules
                    sage: H.antipode(H.monomial(14))                                    # needs sage.modules
                    P14

                    sage: H.monomial(0).antipode()                                      # needs sage.modules
                    P0
                    sage: H.monomial(2).antipode()                                      # needs sage.modules
                    P2
                    sage: (2*H.monomial(1) + 3*H.monomial(4)).antipode()                # needs sage.modules
                    -2*P1 + 3*P4
                """
        class ElementMethods: ...
