from _typeshed import Incomplete
from sage.categories.additive_semigroups import AdditiveSemigroups as AdditiveSemigroups
from sage.categories.category_with_axiom import CategoryWithAxiom_singleton as CategoryWithAxiom_singleton
from sage.categories.homsets import HomsetsCategory as HomsetsCategory
from sage.misc.lazy_import import LazyImport as LazyImport

class AdditiveMonoids(CategoryWithAxiom_singleton):
    """
    The category of additive monoids.

    An *additive monoid* is a unital :class:`additive semigroup
    <sage.categories.additive_semigroups.AdditiveSemigroups>`, that
    is a set endowed with a binary operation `+` which is associative
    and admits a zero (see :wikipedia:`Monoid`).

    EXAMPLES::

        sage: from sage.categories.additive_monoids import AdditiveMonoids
        sage: C = AdditiveMonoids(); C
        Category of additive monoids
        sage: C.super_categories()
        [Category of additive unital additive magmas, Category of additive semigroups]
        sage: sorted(C.axioms())
        ['AdditiveAssociative', 'AdditiveUnital']
        sage: from sage.categories.additive_semigroups import AdditiveSemigroups
        sage: C is AdditiveSemigroups().AdditiveUnital()
        True

    TESTS::

        sage: C.Algebras(QQ).is_subcategory(AlgebrasWithBasis(QQ))
        True
        sage: TestSuite(C).run()
    """
    AdditiveCommutative: Incomplete
    AdditiveInverse: Incomplete
    class ParentMethods:
        def sum(self, args):
            """
            Return the sum of the elements in ``args``, as an element
            of ``self``.

            INPUT:

            - ``args`` -- list (or iterable) of elements of ``self``

            EXAMPLES::

                sage: S = CommutativeAdditiveMonoids().example()
                sage: (a,b,c,d) = S.additive_semigroup_generators()
                sage: S.sum((a,b,a,c,a,b))
                3*a + 2*b + c
                sage: S.sum(())
                0
                sage: S.sum(()).parent() == S
                True

            TESTS:

            The following should be reasonably fast (0.5s each)::

                sage: R.<x,y> = QQ[]
                sage: ignore = R.sum(
                ....:     QQ.random_element()*x^i*y^j for i in range(200) for j in range(200))
                sage: ignore = R.sum([
                ....:     QQ.random_element()*x^i*y^j for i in range(200) for j in range(200)])

            Summing an empty iterator::

                sage: R.sum(1 for i in range(0))
                0
            """
    class Homsets(HomsetsCategory):
        def extra_super_categories(self):
            """
            Implement the fact that a homset between two monoids is
            associative.

            EXAMPLES::

                sage: from sage.categories.additive_monoids import AdditiveMonoids
                sage: AdditiveMonoids().Homsets().extra_super_categories()
                [Category of additive semigroups]
                sage: AdditiveMonoids().Homsets().super_categories()
                [Category of homsets of additive unital additive magmas, Category of additive monoids]

            .. TODO::

                This could be deduced from
                :meth:`AdditiveSemigroups.Homsets.extra_super_categories`.
                See comment in :meth:`Objects.SubcategoryMethods.Homsets`.
            """
