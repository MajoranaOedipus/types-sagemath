from sage.categories.category_singleton import Category_singleton as Category_singleton
from sage.categories.sets_cat import Sets as Sets

class PointedSets(Category_singleton):
    """
    The category of pointed sets.

    EXAMPLES::

        sage: PointedSets()
        Category of pointed sets

    TESTS::

        sage: TestSuite(PointedSets()).run()
    """
    def super_categories(self):
        """
        EXAMPLES::

            sage: PointedSets().super_categories()
            [Category of sets]
        """
