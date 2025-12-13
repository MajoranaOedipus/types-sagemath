from sage.categories.category import Category as Category, CategoryWithParameters as CategoryWithParameters, JoinCategory as JoinCategory
from sage.categories.category_singleton import Category_singleton as Category_singleton
from sage.categories.category_with_axiom import CategoryWithAxiom as CategoryWithAxiom
from sage.categories.covariant_functorial_construction import FunctorialConstructionCategory as FunctorialConstructionCategory
from sage.misc.cachefunc import cached_method as cached_method

class HomsetsCategory(FunctorialConstructionCategory, CategoryWithParameters):
    @classmethod
    def default_super_categories(cls, category):
        '''
        Return the default super categories of ``category.Homsets()``.

        INPUT:

        - ``cls`` -- the category class for the functor `F`
        - ``category`` -- a category `Cat`

        OUTPUT: a category

        As for the other functorial constructions, if ``category``
        implements a nested ``Homsets`` class, this method is used in
        combination with ``category.Homsets().extra_super_categories()``
        to compute the super categories of ``category.Homsets()``.

        EXAMPLES:

        If ``category`` has one or more full super categories, then
        the join of their respective homsets category is returned. In
        this example, this join consists of a single category::

            sage: from sage.categories.homsets import HomsetsCategory
            sage: from sage.categories.additive_groups import AdditiveGroups

            sage: C = AdditiveGroups()
            sage: C.full_super_categories()
            [Category of additive inverse additive unital additive magmas,
             Category of additive monoids]
            sage: H = HomsetsCategory.default_super_categories(C); H
            Category of homsets of additive monoids
            sage: type(H)
            <class \'sage.categories.additive_monoids.AdditiveMonoids.Homsets_with_category\'>

        and, given that nothing specific is currently implemented for
        homsets of additive groups, ``H`` is directly the category
        thereof::

            sage: C.Homsets()
            Category of homsets of additive monoids

        Similarly for rings: a ring homset is just a homset of unital
        magmas and additive magmas::

            sage: Rings().Homsets()
            Category of homsets of unital magmas and additive unital additive magmas

        Otherwise, if ``category`` implements a nested class
        ``Homsets``, this method returns the category of all homsets::

            sage: AdditiveMagmas.Homsets
            <class \'sage.categories.additive_magmas.AdditiveMagmas.Homsets\'>
            sage: HomsetsCategory.default_super_categories(AdditiveMagmas())
            Category of homsets

        which gives one of the super categories of
        ``category.Homsets()``::

            sage: AdditiveMagmas().Homsets().super_categories()
            [Category of additive magmas, Category of homsets]
            sage: AdditiveMagmas().AdditiveUnital().Homsets().super_categories()
            [Category of additive unital additive magmas, Category of homsets]

        the other coming from ``category.Homsets().extra_super_categories()``::

            sage: AdditiveMagmas().Homsets().extra_super_categories()
            [Category of additive magmas]

        Finally, as a last resort, this method returns a stub category
        modelling the homsets of this category::

            sage: hasattr(Posets, "Homsets")
            False
            sage: H = HomsetsCategory.default_super_categories(Posets()); H
            Category of homsets of posets
            sage: type(H)
            <class \'sage.categories.homsets.HomsetsOf_with_category\'>
            sage: Posets().Homsets()
            Category of homsets of posets

        TESTS::

            sage: Objects().Homsets().super_categories()
            [Category of homsets]
            sage: Sets().Homsets().super_categories()
            [Category of homsets]
            sage: (Magmas() & Posets()).Homsets().super_categories()
            [Category of homsets]
        '''
    @cached_method
    def base(self):
        """
        If this homsets category is subcategory of a category with a base, return that base.

        .. TODO:: Is this really useful?

        EXAMPLES::

            sage: ModulesWithBasis(ZZ).Homsets().base()
            Integer Ring
        """

class HomsetsOf(HomsetsCategory):
    """
    Default class for homsets of a category.

    This is used when a category `C` defines some additional structure
    but not a homset category of its own. Indeed, unlike for covariant
    functorial constructions, we cannot represent the homset category
    of `C` by just the join of the homset categories of its super
    categories.

    EXAMPLES::

        sage: C = (Magmas() & Posets()).Homsets(); C
        Category of homsets of magmas and posets
        sage: type(C)
        <class 'sage.categories.homsets.HomsetsOf_with_category'>

    TESTS::

        sage: TestSuite(C).run()
        sage: C = Rings().Homsets()
        sage: TestSuite(C).run(skip=['_test_category_graph'])
        sage: TestSuite(C).run()
    """
    def super_categories(self):
        """
        Return the super categories of ``self``.

        A stub homset category admits a single super category, namely
        the category of all homsets.

        EXAMPLES::

            sage: C = (Magmas() & Posets()).Homsets(); C
            Category of homsets of magmas and posets
            sage: type(C)
            <class 'sage.categories.homsets.HomsetsOf_with_category'>
            sage: C.super_categories()
            [Category of homsets]
        """

class Homsets(Category_singleton):
    """
    The category of all homsets.

    EXAMPLES::

        sage: from sage.categories.homsets import Homsets
        sage: Homsets()
        Category of homsets

    This is a subcategory of ``Sets()``::

        sage: Homsets().super_categories()
        [Category of sets]

    By this, we assume that all homsets implemented in Sage are sets,
    or equivalently that we only implement locally small categories.
    See :wikipedia:`Category_(mathematics)`.

    :issue:`17364`: every homset category shall be a subcategory of the
    category of all homsets::

        sage: Schemes().Homsets().is_subcategory(Homsets())
        True
        sage: AdditiveMagmas().Homsets().is_subcategory(Homsets())
        True
        sage: AdditiveMagmas().AdditiveUnital().Homsets().is_subcategory(Homsets())
        True

    This is tested in :meth:`HomsetsCategory._test_homsets_category`.
    """
    def super_categories(self):
        """
        Return the super categories of ``self``.

        EXAMPLES::

            sage: from sage.categories.homsets import Homsets
            sage: Homsets()
            Category of homsets
        """
    class SubcategoryMethods:
        def Endset(self):
            """
            Return the subcategory of the homsets of ``self`` that are endomorphism sets.

            EXAMPLES::

                sage: Sets().Homsets().Endset()
                Category of endsets of sets

                sage: Posets().Homsets().Endset()
                Category of endsets of posets
            """
    class Endset(CategoryWithAxiom):
        """
        The category of all endomorphism sets.

        This category serves too purposes: making sure that the
        ``Endset`` axiom is implemented in the category where it's
        defined, namely ``Homsets``, and specifying that ``Endsets``
        are monoids.

        EXAMPLES::

            sage: from sage.categories.homsets import Homsets
            sage: Homsets().Endset()
            Category of endsets
        """
        def extra_super_categories(self):
            """
            Implement the fact that endsets are monoids.

            .. SEEALSO:: :meth:`CategoryWithAxiom.extra_super_categories`

            EXAMPLES::

                sage: from sage.categories.homsets import Homsets
                sage: Homsets().Endset().extra_super_categories()
                [Category of monoids]
            """
        class ParentMethods:
            def is_endomorphism_set(self):
                """
                Return ``True`` as ``self`` is in the category
                of ``Endsets``.

                EXAMPLES::

                    sage: P.<t> = ZZ[]
                    sage: E = End(P)
                    sage: E.is_endomorphism_set()
                    True
                """
    class ParentMethods:
        def is_endomorphism_set(self):
            """
            Return ``True`` if the domain and codomain of ``self`` are the same
            object.

            EXAMPLES::

                sage: P.<t> = ZZ[]
                sage: f = P.hom([1/2*t])
                sage: f.parent().is_endomorphism_set()
                False
                sage: g = P.hom([2*t])
                sage: g.parent().is_endomorphism_set()
                True
            """
