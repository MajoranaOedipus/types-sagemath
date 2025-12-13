from sage.categories.category_with_axiom import CategoryWithAxiom as CategoryWithAxiom
from sage.categories.semigroups import Semigroups as Semigroups

class JTrivialSemigroups(CategoryWithAxiom):
    def extra_super_categories(self):
        """
        Implement the fact that a `J`-trivial semigroup is `L` and `R`-trivial.

        EXAMPLES::

            sage: Semigroups().JTrivial().extra_super_categories()
            [Category of l trivial semigroups, Category of r trivial semigroups]
        """
