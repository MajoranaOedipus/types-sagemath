from sage.categories.category_with_axiom import CategoryWithAxiom as CategoryWithAxiom
from sage.categories.semigroups import Semigroups as Semigroups

class RTrivialSemigroups(CategoryWithAxiom):
    def extra_super_categories(self):
        """
        Implement the fact that a `R`-trivial semigroup is `H`-trivial.

        EXAMPLES::

            sage: Semigroups().RTrivial().extra_super_categories()
            [Category of h trivial semigroups]
        """
    def Commutative_extra_super_categories(self):
        """
        Implement the fact that a commutative `R`-trivial semigroup is `J`-trivial.

        EXAMPLES::

            sage: Semigroups().RTrivial().Commutative_extra_super_categories()
            [Category of j trivial semigroups]

        TESTS::

            sage: Semigroups().RTrivial().Commutative() is Semigroups().JTrivial().Commutative()
            True
        """
