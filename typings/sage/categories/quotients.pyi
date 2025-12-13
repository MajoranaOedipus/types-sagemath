from sage.categories.category import Category as Category
from sage.categories.covariant_functorial_construction import RegressiveCovariantConstructionCategory as RegressiveCovariantConstructionCategory

class QuotientsCategory(RegressiveCovariantConstructionCategory):
    @classmethod
    def default_super_categories(cls, category):
        """
        Return the default super categories of ``category.Quotients()``.

        Mathematical meaning: if `A` is a quotient of `B` in the
        category `C`, then `A` is also a subquotient of `B` in the
        category `C`.

        INPUT:

        - ``cls`` -- the class ``QuotientsCategory``
        - ``category`` -- a category `Cat`

        OUTPUT: a (join) category

        In practice, this returns ``category.Subquotients()``, joined
        together with the result of the method
        :meth:`RegressiveCovariantConstructionCategory.default_super_categories() <sage.categories.covariant_functorial_construction.RegressiveCovariantConstructionCategory.default_super_categories>`
        (that is the join of ``category`` and ``cat.Quotients()`` for
        each ``cat`` in the super categories of ``category``).

        EXAMPLES:

        Consider ``category=Groups()``, which has ``cat=Monoids()`` as
        super category. Then, a subgroup of a group `G` is
        simultaneously a subquotient of `G`, a group by itself, and a
        quotient monoid of ``G``::

            sage: Groups().Quotients().super_categories()
            [Category of groups, Category of subquotients of monoids, Category of quotients of semigroups]

        Mind the last item above: there is indeed currently nothing
        implemented about quotient monoids.

        This resulted from the following call::

            sage: sage.categories.quotients.QuotientsCategory.default_super_categories(Groups())
            Join of Category of groups and Category of subquotients of monoids and Category of quotients of semigroups
        """
