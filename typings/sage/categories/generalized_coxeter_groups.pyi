from sage.categories.category_singleton import Category_singleton as Category_singleton
from sage.categories.category_with_axiom import CategoryWithAxiom as CategoryWithAxiom
from sage.categories.complex_reflection_or_generalized_coxeter_groups import ComplexReflectionOrGeneralizedCoxeterGroups as ComplexReflectionOrGeneralizedCoxeterGroups
from sage.misc.cachefunc import cached_method as cached_method

class GeneralizedCoxeterGroups(Category_singleton):
    """
    The category of generalized Coxeter groups.

    A generalized Coxeter group is a group with a presentation of
    the following form:

    .. MATH::

        \\langle s_i \\mid s_i^{p_i}, s_i s_j \\cdots = s_j s_i \\cdots \\rangle,

    where `p_i > 1`, `i \\in I`, and the factors in the braid relation
    occur `m_{ij} = m_{ji}` times for all `i \\neq j \\in I`.

    EXAMPLES::

        sage: from sage.categories.generalized_coxeter_groups import GeneralizedCoxeterGroups
        sage: C = GeneralizedCoxeterGroups(); C
        Category of generalized Coxeter groups

    TESTS::

        sage: TestSuite(C).run()
    """
    @cached_method
    def super_categories(self):
        """
        EXAMPLES::

            sage: from sage.categories.generalized_coxeter_groups import GeneralizedCoxeterGroups
            sage: GeneralizedCoxeterGroups().super_categories()
            [Category of complex reflection or generalized Coxeter groups]
        """
    def additional_structure(self) -> None:
        """
        Return ``None``.

        Indeed, all the structure generalized Coxeter groups have in
        addition to groups (simple reflections, ...) is already
        defined in the super category.

        .. SEEALSO:: :meth:`Category.additional_structure`

        EXAMPLES::

            sage: from sage.categories.generalized_coxeter_groups import GeneralizedCoxeterGroups
            sage: GeneralizedCoxeterGroups().additional_structure()
        """
    class Finite(CategoryWithAxiom):
        """
        The category of finite generalized Coxeter groups.
        """
        def extra_super_categories(self):
            """
            Implement that a finite generalized Coxeter group is a
            well-generated complex reflection group.

            EXAMPLES::

                sage: from sage.categories.generalized_coxeter_groups import GeneralizedCoxeterGroups
                sage: from sage.categories.complex_reflection_groups import ComplexReflectionGroups

                sage: Cat = GeneralizedCoxeterGroups().Finite()
                sage: Cat.extra_super_categories()
                [Category of well generated finite complex reflection groups]
                sage: Cat.is_subcategory(ComplexReflectionGroups().Finite().WellGenerated())
                True
            """
