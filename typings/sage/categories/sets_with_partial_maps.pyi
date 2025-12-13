from sage.categories.category_singleton import Category_singleton as Category_singleton
from sage.categories.objects import Objects as Objects

class SetsWithPartialMaps(Category_singleton):
    """
    The category whose objects are sets and whose morphisms are
    maps that are allowed to raise a :exc:`ValueError` on some inputs.

    This category is equivalent to the category of pointed sets,
    via the equivalence sending an object X to X union {error},
    a morphism f to the morphism of pointed sets that sends x
    to f(x) if f does not raise an error on x, or to error if it
    does.

    EXAMPLES::

        sage: SetsWithPartialMaps()
        Category of sets with partial maps

        sage: SetsWithPartialMaps().super_categories()
        [Category of objects]

    TESTS::

        sage: TestSuite(SetsWithPartialMaps()).run()
    """
    def super_categories(self):
        """
        EXAMPLES::

            sage: SetsWithPartialMaps().super_categories()
            [Category of objects]
        """
