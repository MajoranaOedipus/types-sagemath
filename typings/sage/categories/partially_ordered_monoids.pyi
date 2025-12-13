from sage.categories.basic import Monoids as Monoids, Posets as Posets
from sage.categories.category_singleton import Category_singleton as Category_singleton

class PartiallyOrderedMonoids(Category_singleton):
    """
    The category of partially ordered monoids, that is partially ordered sets
    which are also monoids, and such that multiplication preserves the
    ordering: `x \\leq y` implies `x*z < y*z` and `z*x < z*y`.

    See :wikipedia:`Ordered_monoid`

    EXAMPLES::

        sage: PartiallyOrderedMonoids()
        Category of partially ordered monoids
        sage: PartiallyOrderedMonoids().super_categories()
        [Category of posets, Category of monoids]

    TESTS::

        sage: TestSuite(PartiallyOrderedMonoids()).run()
    """
    def super_categories(self):
        """
        EXAMPLES::

            sage: PartiallyOrderedMonoids().super_categories()
            [Category of posets, Category of monoids]
        """
    class ParentMethods: ...
    class ElementMethods: ...

OrderedMonoids = PartiallyOrderedMonoids