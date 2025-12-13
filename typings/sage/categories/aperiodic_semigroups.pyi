from sage.categories.category_with_axiom import CategoryWithAxiom as CategoryWithAxiom
from sage.categories.semigroups import Semigroups as Semigroups

class AperiodicSemigroups(CategoryWithAxiom):
    def extra_super_categories(self):
        """
        Implement the fact that an aperiodic semigroup is `H`-trivial.

        EXAMPLES::

            sage: Semigroups().Aperiodic().extra_super_categories()
            [Category of h trivial semigroups]
        """
