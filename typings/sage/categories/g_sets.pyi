from sage.categories.category import Category as Category
from sage.categories.sets_cat import Sets as Sets

class GSets(Category):
    """
    The category of `G`-sets, for a group `G`.

    EXAMPLES::

        sage: S = SymmetricGroup(3)                                                     # needs sage.groups
        sage: GSets(S)                                                                  # needs sage.groups
        Category of G-sets for Symmetric group of order 3! as a permutation group

    TODO: should this derive from Category_over_base?
    """
    def __init__(self, G) -> None:
        """
        TESTS::

            sage: S8 = SymmetricGroup(8)                                                # needs sage.groups
            sage: TestSuite(GSets(S8)).run()                                            # needs sage.groups
        """
    def super_categories(self):
        """
        EXAMPLES::

            sage: GSets(SymmetricGroup(8)).super_categories()                           # needs sage.groups
            [Category of sets]
        """
    @classmethod
    def an_instance(cls):
        """
        Return an instance of this class.

        EXAMPLES::

            sage: GSets.an_instance()  # indirect doctest                               # needs sage.groups
            Category of G-sets for Symmetric group of order 8! as a permutation group
        """
