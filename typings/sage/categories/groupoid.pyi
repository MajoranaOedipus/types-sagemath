from sage.categories.category import CategoryWithParameters as CategoryWithParameters
from sage.categories.sets_cat import Sets as Sets

class Groupoid(CategoryWithParameters):
    """
    The category of groupoids, for a set (usually a group) `G`.

    FIXME:

     - Groupoid or Groupoids ?
     - definition and link with :wikipedia:`Groupoid`
     - Should Groupoid inherit from Category_over_base?

    EXAMPLES::

        sage: Groupoid(DihedralGroup(3))
        Groupoid with underlying set Dihedral group of order 6 as a permutation group
    """
    def __init__(self, G=None) -> None:
        """
        TESTS::

            sage: S8 = SymmetricGroup(8)
            sage: C = Groupoid(S8)
            sage: TestSuite(C).run()
        """
    def super_categories(self):
        """
        EXAMPLES::

            sage: Groupoid(DihedralGroup(3)).super_categories()
            [Category of sets]
        """
    @classmethod
    def an_instance(cls):
        """
        Return an instance of this class.

        EXAMPLES::

            sage: Groupoid.an_instance() # indirect doctest
            Groupoid with underlying set Symmetric group of order 8! as a permutation group
        """
