from sage.categories.category_with_axiom import CategoryWithAxiom_over_base_ring as CategoryWithAxiom_over_base_ring
from sage.categories.graded_modules import GradedModulesCategory as GradedModulesCategory
from sage.categories.tensor import tensor as tensor
from sage.categories.with_realizations import WithRealizationsCategory as WithRealizationsCategory
from sage.misc.cachefunc import cached_method as cached_method

class GradedHopfAlgebrasWithBasis(GradedModulesCategory):
    """
    The category of graded Hopf algebras with a distinguished basis.

    EXAMPLES::

        sage: C = GradedHopfAlgebrasWithBasis(ZZ); C
        Category of graded Hopf algebras with basis over Integer Ring
        sage: C.super_categories()
        [Category of filtered Hopf algebras with basis over Integer Ring,
         Category of graded algebras with basis over Integer Ring,
         Category of graded coalgebras with basis over Integer Ring]

        sage: C is HopfAlgebras(ZZ).WithBasis().Graded()
        True
        sage: C is HopfAlgebras(ZZ).Graded().WithBasis()
        False

    TESTS::

        sage: TestSuite(C).run()
    """
    def example(self):
        """
        Return an example of a graded Hopf algebra with
        a distinguished basis.

        TESTS::

            sage: GradedHopfAlgebrasWithBasis(QQ).example()                             # needs sage.modules
            An example of a graded connected Hopf algebra with basis over Rational Field
        """
    class ParentMethods: ...
    class ElementMethods: ...
    class WithRealizations(WithRealizationsCategory):
        @cached_method
        def super_categories(self):
            """
            EXAMPLES::

                sage: GradedHopfAlgebrasWithBasis(QQ).WithRealizations().super_categories()
                [Join of Category of Hopf algebras over Rational Field
                 and Category of graded algebras over Rational Field
                 and Category of graded coalgebras over Rational Field]

            TESTS::

                sage: TestSuite(GradedHopfAlgebrasWithBasis(QQ).WithRealizations()).run()
            """
    class Connected(CategoryWithAxiom_over_base_ring):
        def example(self):
            """
            Return an example of a graded connected Hopf algebra with
            a distinguished basis.

            TESTS::

                sage: GradedHopfAlgebrasWithBasis(QQ).Connected().example()             # needs sage.modules
                An example of a graded connected Hopf algebra with basis over Rational Field
            """
        class ParentMethods:
            def counit_on_basis(self, i):
                """
                The default counit of a graded connected Hopf algebra.

                INPUT:

                - ``i`` -- an element of the index set

                OUTPUT: an element of the base ring

                .. MATH::

                    c(i) := \\begin{cases}
                    1 & \\hbox{if $i$ indexes the $1$ of the algebra}\\\\\n                    0 & \\hbox{otherwise}.
                    \\end{cases}

                EXAMPLES::

                    sage: H = GradedHopfAlgebrasWithBasis(QQ).Connected().example()     # needs sage.modules
                    sage: H.monomial(4).counit()  # indirect doctest                    # needs sage.modules
                    0
                    sage: H.monomial(0).counit()  # indirect doctest                    # needs sage.modules
                    1
                """
            @cached_method
            def antipode_on_basis(self, index):
                """
                The antipode on the basis element indexed by ``index``.

                INPUT:

                - ``index`` -- an element of the index set

                For a graded connected Hopf algebra, we can define
                an antipode recursively by

                .. MATH::

                    S(x) := -\\sum_{x^L \\neq x} S(x^L) \\times x^R

                when `|x| > 0`, and by `S(x) = x` when `|x| = 0`.

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
        class ElementMethods: ...
