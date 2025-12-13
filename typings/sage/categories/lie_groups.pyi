from sage.categories.category_types import Category_over_base_ring as Category_over_base_ring
from sage.categories.groups import Groups as Groups
from sage.categories.manifolds import Manifolds as Manifolds
from sage.misc.cachefunc import cached_method as cached_method

class LieGroups(Category_over_base_ring):
    """
    The category of Lie groups.

    A Lie group is a topological group with a smooth manifold structure.

    EXAMPLES::

        sage: from sage.categories.lie_groups import LieGroups
        sage: C = LieGroups(QQ); C
        Category of Lie groups over Rational Field

    TESTS::

        sage: TestSuite(C).run(skip='_test_category_over_bases')
    """
    @cached_method
    def super_categories(self):
        """
        EXAMPLES::

            sage: from sage.categories.lie_groups import LieGroups
            sage: LieGroups(QQ).super_categories()
            [Category of topological groups,
             Category of smooth manifolds over Rational Field]
        """
    def additional_structure(self) -> None:
        """
        Return ``None``.

        Indeed, the category of Lie groups defines no new
        structure: a morphism of topological spaces and of smooth
        manifolds is a morphism as Lie groups.

        .. SEEALSO:: :meth:`Category.additional_structure`

        EXAMPLES::

            sage: from sage.categories.lie_groups import LieGroups
            sage: LieGroups(QQ).additional_structure()
        """
