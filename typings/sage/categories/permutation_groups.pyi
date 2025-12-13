from _typeshed import Incomplete
from sage.categories.category import Category as Category
from sage.categories.groups import Groups as Groups
from sage.misc.cachefunc import cached_method as cached_method
from sage.misc.lazy_import import LazyImport as LazyImport

class PermutationGroups(Category):
    """
    The category of permutation groups.

    A *permutation group* is a group whose elements are concretely
    represented by permutations of some set. In other words, the group
    comes endowed with a distinguished action on some set.

    This distinguished action should be preserved by permutation group
    morphisms. For details, see
    :wikipedia:`Permutation_group#Permutation_isomorphic_groups`.

    .. TODO:: shall we accept only permutations with finite support or not?

    EXAMPLES::

        sage: PermutationGroups()
        Category of permutation groups
        sage: PermutationGroups().super_categories()
        [Category of groups]

    The category of permutation groups defines additional structure
    that should be preserved by morphisms, namely the distinguished
    action::

        sage: PermutationGroups().additional_structure()
        Category of permutation groups

    TESTS::

        sage: C = PermutationGroups()
        sage: TestSuite(C).run()
    """
    @cached_method
    def super_categories(self):
        """
        Return a list of the immediate super categories of ``self``.

        EXAMPLES::

            sage: PermutationGroups().super_categories()
            [Category of groups]
        """
    Finite: Incomplete
