from _typeshed import Incomplete
from sage.categories.additive_monoids import AdditiveMonoids as AdditiveMonoids
from sage.categories.algebra_functor import AlgebrasCategory as AlgebrasCategory
from sage.categories.category_with_axiom import CategoryWithAxiom as CategoryWithAxiom, CategoryWithAxiom_singleton as CategoryWithAxiom_singleton
from sage.cpython.getattr import raw_getattr as raw_getattr
from sage.misc.lazy_import import LazyImport as LazyImport

Groups: Incomplete

class AdditiveGroups(CategoryWithAxiom_singleton):
    """
    The category of additive groups.

    An *additive group* is a set with an internal binary operation `+` which
    is associative, admits a zero, and where every element can be negated.

    EXAMPLES::

        sage: from sage.categories.additive_groups import AdditiveGroups
        sage: from sage.categories.additive_monoids import AdditiveMonoids
        sage: AdditiveGroups()
        Category of additive groups
        sage: AdditiveGroups().super_categories()
        [Category of additive inverse additive unital additive magmas,
         Category of additive monoids]
        sage: AdditiveGroups().all_super_categories()
        [Category of additive groups,
         Category of additive inverse additive unital additive magmas,
         Category of additive monoids,
         Category of additive unital additive magmas,
         Category of additive semigroups,
         Category of additive magmas,
         Category of sets,
         Category of sets with partial maps,
         Category of objects]

        sage: AdditiveGroups().axioms()
        frozenset({'AdditiveAssociative', 'AdditiveInverse', 'AdditiveUnital'})
        sage: AdditiveGroups() is AdditiveMonoids().AdditiveInverse()
        True

    TESTS::

        sage: C = AdditiveGroups()
        sage: TestSuite(C).run()
    """
    class Algebras(AlgebrasCategory):
        class ParentMethods:
            group: Incomplete
    class Finite(CategoryWithAxiom):
        class Algebras(AlgebrasCategory):
            extra_super_categories: Incomplete
            class ParentMethods:
                __init_extra__: Incomplete
    AdditiveCommutative: Incomplete
