from sage.categories.category_singleton import Category_singleton as Category_singleton
from sage.categories.generalized_coxeter_groups import GeneralizedCoxeterGroups as GeneralizedCoxeterGroups
from sage.misc.cachefunc import cached_method as cached_method

class ShephardGroups(Category_singleton):
    """
    The category of Shephard groups.

    EXAMPLES::

        sage: from sage.categories.shephard_groups import ShephardGroups
        sage: C = ShephardGroups(); C
        Category of shephard groups

    TESTS::

        sage: TestSuite(C).run()
    """
    @cached_method
    def super_categories(self):
        """
        EXAMPLES::

            sage: from sage.categories.shephard_groups import ShephardGroups
            sage: ShephardGroups().super_categories()
            [Category of finite generalized Coxeter groups]
        """
