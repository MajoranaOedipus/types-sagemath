from sage.categories.category_with_axiom import CategoryWithAxiom as CategoryWithAxiom
from sage.categories.magmas import Magmas as Magmas
from sage.misc.abstract_method import abstract_method as abstract_method

class FinitelyGeneratedMagmas(CategoryWithAxiom):
    """
    The category of finitely generated (multiplicative) magmas.

    See :meth:`Magmas.SubcategoryMethods.FinitelyGeneratedAsMagma` for
    details.

    EXAMPLES::

        sage: C = Magmas().FinitelyGeneratedAsMagma(); C
        Category of finitely generated magmas
        sage: C.super_categories()
        [Category of magmas]
        sage: sorted(C.axioms())
        ['FinitelyGeneratedAsMagma']

    TESTS::

        sage: TestSuite(C).run()
    """
    class ParentMethods:
        @abstract_method
        def magma_generators(self) -> None:
            """
            Return distinguished magma generators for ``self``.

            OUTPUT: a finite family

            This method should be implemented by all
            :class:`finitely generated magmas <FinitelyGeneratedMagmas>`.

            EXAMPLES::

                sage: S = FiniteSemigroups().example()
                sage: S.magma_generators()
                Family ('a', 'b', 'c', 'd')
            """
