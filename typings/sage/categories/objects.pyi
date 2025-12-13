from sage.categories.category_singleton import Category_singleton as Category_singleton
from sage.categories.homsets import HomsetsCategory as HomsetsCategory
from sage.misc.cachefunc import cached_method as cached_method

class Objects(Category_singleton):
    """
    The category of all objects
    the basic category

    EXAMPLES::

        sage: Objects()
        Category of objects
        sage: Objects().super_categories()
        []

    TESTS::

        sage: TestSuite(Objects()).run()
    """
    def additional_structure(self) -> None:
        """
        Return ``None``.

        Indeed, by convention, the category of objects defines no
        additional structure.

        .. SEEALSO:: :meth:`Category.additional_structure`

        EXAMPLES::

            sage: Objects().additional_structure()
        """
    def super_categories(self):
        """
        EXAMPLES::

            sage: Objects().super_categories()
            []
        """
    def __contains__(self, x) -> bool:
        """
        Anything is in the category of objects.

        EXAMPLES::

            sage: int(1) in Objects()
            True
            sage: ZZ     in Objects()
            True
            sage: 2/3    in Objects()
            True
        """
    class SubcategoryMethods:
        @cached_method
        def Homsets(self):
            """
            Return the category of homsets between objects of this category.

            EXAMPLES::

                sage: Sets().Homsets()
                Category of homsets of sets

                sage: Rings().Homsets()
                Category of homsets of unital magmas and additive unital additive magmas

            .. NOTE:: Background

                Information, code, documentation, and tests about the
                category of homsets of a category ``Cs`` should go in
                the nested class ``Cs.Homsets``. They will then be
                made available to homsets of any subcategory of
                ``Cs``.

                Assume, for example, that homsets of ``Cs`` are ``Cs``
                themselves. This information can be implemented in the
                method ``Cs.Homsets.extra_super_categories`` to make
                ``Cs.Homsets()`` a subcategory of ``Cs()``.

                Methods about the homsets themselves should go in the
                nested class ``Cs.Homsets.ParentMethods``.

                Methods about the morphisms can go in the nested class
                ``Cs.Homsets.ElementMethods``. However it's generally
                preferable to put them in the nested class
                ``Cs.MorphimMethods``; indeed they will then apply to
                morphisms of all subcategories of ``Cs``, and not only
                full subcategories.


            .. SEEALSO::

                :class:`~.covariant_functorial_construction.FunctorialConstruction`

            .. TODO::

                - Design a mechanism to specify that an axiom is
                  compatible with taking subsets. Examples:
                  ``Finite``, ``Associative``, ``Commutative`` (when
                  meaningful), but not ``Infinite`` nor ``Unital``.

                - Design a mechanism to specify that, when `B` is a
                  subcategory of `A`, a `B`-homset is a subset of the
                  corresponding `A` homset. And use it to recover all
                  the relevant axioms from homsets in super categories.

                - For instances of redundant code due to this missing
                  feature, see:

                  - :meth:`AdditiveMonoids.Homsets.extra_super_categories`
                  - :meth:`HomsetsCategory.extra_super_categories`
                    (slightly different nature)
                  - plus plenty of spots where this is not implemented.
            """
        @cached_method
        def Endsets(self):
            """
            Return the category of endsets between objects of this category.

            EXAMPLES::

                sage: Sets().Endsets()
                Category of endsets of sets

                sage: Rings().Endsets()
                Category of endsets of unital magmas and additive unital additive magmas

            .. SEEALSO::

                - :meth:`Homsets`
            """
    class ParentMethods:
        """
        Methods for all category objects
        """
