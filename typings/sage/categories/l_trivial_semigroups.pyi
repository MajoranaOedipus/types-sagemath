from sage.categories.category_with_axiom import CategoryWithAxiom as CategoryWithAxiom
from sage.categories.magmas import Magmas as Magmas
from sage.categories.semigroups import Semigroups as Semigroups

class LTrivialSemigroups(CategoryWithAxiom):
    def extra_super_categories(self):
        """
        Implement the fact that a `L`-trivial semigroup is `H`-trivial.

        EXAMPLES::

            sage: Semigroups().LTrivial().extra_super_categories()
            [Category of h trivial semigroups]
        """
    def RTrivial_extra_super_categories(self):
        """
        Implement the fact that an `L`-trivial and `R`-trivial semigroup
        is `J`-trivial.

        EXAMPLES::

            sage: Semigroups().LTrivial().RTrivial_extra_super_categories()
            [Category of j trivial magmas]

        TESTS::

            sage: Semigroups().LTrivial().RTrivial() is Semigroups().JTrivial()
            True
        """
    def Commutative_extra_super_categories(self):
        """
        Implement the fact that a commutative `R`-trivial semigroup is `J`-trivial.

        EXAMPLES::

            sage: Semigroups().LTrivial().Commutative_extra_super_categories()
            [Category of j trivial semigroups]

        TESTS::

            sage: Semigroups().LTrivial().Commutative() is Semigroups().JTrivial().Commutative()
            True
        """
