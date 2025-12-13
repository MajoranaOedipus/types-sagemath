from sage.categories.category_types import Category_over_base_ring as Category_over_base_ring
from sage.categories.category_with_axiom import CategoryWithAxiom_over_base_ring as CategoryWithAxiom_over_base_ring
from sage.categories.covariant_functorial_construction import RegressiveCovariantConstructionCategory as RegressiveCovariantConstructionCategory
from sage.misc.cachefunc import cached_method as cached_method

class FilteredModulesCategory(RegressiveCovariantConstructionCategory, Category_over_base_ring):
    def __init__(self, base_category) -> None:
        """
        EXAMPLES::

            sage: C = Algebras(QQ).Filtered()
            sage: C
            Category of filtered algebras over Rational Field
            sage: C.base_category()
            Category of algebras over Rational Field
            sage: sorted(C.super_categories(), key=str)
            [Category of algebras over Rational Field,
             Category of filtered vector spaces over Rational Field]

            sage: AlgebrasWithBasis(QQ).Filtered().base_ring()
            Rational Field
            sage: HopfAlgebrasWithBasis(QQ).Filtered().base_ring()
            Rational Field
        """

class FilteredModules(FilteredModulesCategory):
    """
    The category of filtered modules over a given ring `R`.

    A *filtered module* over a ring `R` with a totally ordered
    indexing set `I` (typically `I = \\NN`) is an `R`-module `M` equipped
    with a family `(F_i)_{i \\in I}` of `R`-submodules satisfying
    `F_i \\subseteq F_j` for all `i,j \\in I` having `i \\leq j`, and
    `M = \\bigcup_{i \\in I} F_i`. This family is called a *filtration*
    of the given module `M`.

    EXAMPLES::

        sage: Modules(ZZ).Filtered()
        Category of filtered modules over Integer Ring
        sage: Modules(ZZ).Filtered().super_categories()
        [Category of modules over Integer Ring]

    TESTS::

        sage: TestSuite(Modules(ZZ).Filtered()).run()

    REFERENCES:

    - :wikipedia:`Filtration_(mathematics)`
    """
    def extra_super_categories(self):
        """
        Add :class:`VectorSpaces` to the super categories of ``self`` if
        the base ring is a field.

        EXAMPLES::

            sage: Modules(QQ).Filtered().is_subcategory(VectorSpaces(QQ))
            True
            sage: Modules(ZZ).Filtered().extra_super_categories()
            []

        This makes sure that ``Modules(QQ).Filtered()`` returns an
        instance of :class:`FilteredModules` and not a join category of
        an instance of this class and of ``VectorSpaces(QQ)``::

            sage: type(Modules(QQ).Filtered())
            <class 'sage.categories.vector_spaces.VectorSpaces.Filtered_with_category'>

        .. TODO::

            Get rid of this workaround once there is a more systematic
            approach for the alias ``Modules(QQ)`` -> ``VectorSpaces(QQ)``.
            Probably the latter should be a category with axiom, and
            covariant constructions should play well with axioms.
        """
    class SubcategoryMethods:
        @cached_method
        def Connected(self):
            """
            Return the full subcategory of the connected objects of ``self``.

            A filtered `R`-module `M` with filtration
            `(F_0, F_1, F_2, \\ldots)` (indexed by `\\NN`)
            is said to be *connected* if `F_0` is isomorphic
            to `R`.

            EXAMPLES::

                sage: Modules(ZZ).Filtered().Connected()
                Category of filtered connected modules over Integer Ring
                sage: Coalgebras(QQ).Filtered().Connected()
                Category of filtered connected coalgebras over Rational Field
                sage: AlgebrasWithBasis(QQ).Filtered().Connected()
                Category of filtered connected algebras with basis over Rational Field

            TESTS::

                sage: TestSuite(Modules(ZZ).Filtered().Connected()).run()
                sage: Coalgebras(QQ).Filtered().Connected.__module__
                'sage.categories.filtered_modules'
            """
    class Connected(CategoryWithAxiom_over_base_ring): ...
