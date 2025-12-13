from sage.categories.category_with_axiom import CategoryWithAxiom as CategoryWithAxiom
from sage.categories.semigroups import Semigroups as Semigroups

class HTrivialSemigroups(CategoryWithAxiom):
    def Finite_extra_super_categories(self):
        """
        Implement the fact that a finite `H`-trivial is aperiodic.

        EXAMPLES::

            sage: Semigroups().HTrivial().Finite_extra_super_categories()
            [Category of aperiodic semigroups]
            sage: Semigroups().HTrivial().Finite() is Semigroups().Aperiodic().Finite()
            True
        """
    def Inverse_extra_super_categories(self):
        """
        Implement the fact that an `H`-trivial inverse semigroup is `J`-trivial.

        .. TODO::

            Generalization for inverse semigroups.

            Recall that there are two invertibility axioms for a semigroup `S`:

            - One stating the existence, for all `x`, of a local inverse
              `y` satisfying `x=xyx` and `y=yxy`;
            - One stating the existence, for all `x`, of a global
              inverse `y` satisfying `xy=yx=1`, where `1` is the unit
              of `S` (which must of course exist).

            It is sufficient to have local inverses for `H`-triviality
            to imply `J`-triviality. However, at this stage, only the
            second axiom is implemented in Sage (see
            :meth:`Magmas.Unital.SubcategoryMethods.Inverse`). Therefore
            this fact is only implemented for semigroups with global
            inverses, that is groups. However the trivial group is the
            unique `H`-trivial group, so this is rather boring.

        EXAMPLES::

            sage: Semigroups().HTrivial().Inverse_extra_super_categories()
            [Category of j trivial semigroups]
            sage: Monoids().HTrivial().Inverse()
            Category of h trivial groups
        """
