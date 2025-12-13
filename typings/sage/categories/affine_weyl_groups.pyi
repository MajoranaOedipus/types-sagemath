from sage.categories.category_singleton import Category_singleton as Category_singleton
from sage.categories.finite_enumerated_sets import FiniteEnumeratedSets as FiniteEnumeratedSets
from sage.categories.weyl_groups import WeylGroups as WeylGroups
from sage.misc.cachefunc import cached_method as cached_method

class AffineWeylGroups(Category_singleton):
    '''
    The category of affine Weyl groups.

    .. TODO:: add a description of this category

    .. SEEALSO::

        - :wikipedia:`Affine_weyl_group`
        - :class:`WeylGroups`, :class:`WeylGroup`

    EXAMPLES::

        sage: C = AffineWeylGroups(); C
        Category of affine Weyl groups
        sage: C.super_categories()
        [Category of infinite Weyl groups]

        sage: C.example()
        NotImplemented
        sage: W = WeylGroup(["A", 4, 1]); W                                             # needs sage.combinat sage.groups
        Weyl Group of type [\'A\', 4, 1] (as a matrix group acting on the root space)
        sage: W.category()                                                              # needs sage.combinat sage.groups
        Category of irreducible affine Weyl groups

    TESTS::

        sage: TestSuite(C).run()
    '''
    def super_categories(self):
        """
        EXAMPLES::

            sage: AffineWeylGroups().super_categories()
            [Category of infinite Weyl groups]
        """
    def additional_structure(self) -> None:
        """
        Return ``None``.

        Indeed, the category of affine Weyl groups defines no
        additional structure: affine Weyl groups are a special class
        of Weyl groups.

        .. SEEALSO:: :meth:`Category.additional_structure`

        .. TODO:: Should this category be a :class:`CategoryWithAxiom`?

        EXAMPLES::

            sage: AffineWeylGroups().additional_structure()
        """
    class ParentMethods:
        @cached_method
        def special_node(self):
            """
            Return the distinguished special node of the underlying
            Dynkin diagram.

            EXAMPLES::

                sage: W = WeylGroup(['A', 3, 1])                                        # needs sage.combinat sage.groups
                sage: W.special_node()                                                  # needs sage.combinat sage.groups
                0
            """
        def affine_grassmannian_elements_of_given_length(self, k):
            """
            Return the affine Grassmannian elements of length `k`.

            This is returned as a finite enumerated set.

            EXAMPLES::

                sage: W = WeylGroup(['A', 3, 1])                                        # needs sage.combinat sage.groups
                sage: [x.reduced_word()                                                 # needs sage.combinat sage.groups
                ....:  for x in W.affine_grassmannian_elements_of_given_length(3)]
                [[2, 1, 0], [3, 1, 0], [2, 3, 0]]

            .. SEEALSO::

                :meth:`AffineWeylGroups.ElementMethods.is_affine_grassmannian`
            """
    class ElementMethods:
        def is_affine_grassmannian(self):
            """
            Test whether ``self`` is affine Grassmannian.

            An element of an affine Weyl group is *affine Grassmannian*
            if any of the following equivalent properties holds:

            - all reduced words for ``self`` end with 0.
            - ``self`` is the identity, or 0 is its single right descent.
            - ``self`` is a minimal coset representative for W / cl W.

            EXAMPLES::

                sage: # needs sage.combinat sage.groups
                sage: W = WeylGroup(['A', 3, 1])
                sage: w = W.from_reduced_word([2,1,0])
                sage: w.is_affine_grassmannian()
                True
                sage: w = W.from_reduced_word([2,0])
                sage: w.is_affine_grassmannian()
                False
                sage: W.one().is_affine_grassmannian()
                True
            """
        def affine_grassmannian_to_core(self):
            """
            Bijection between affine Grassmannian elements of type `A_k^{(1)}` and `(k+1)`-cores.

            INPUT:

            - ``self`` -- an affine Grassmannian element of some affine Weyl group of type `A_k^{(1)}`

            Recall that an element `w` of an affine Weyl group is
            affine Grassmannian if all its all reduced words end in 0, see :meth:`is_affine_grassmannian`.

            OUTPUT:

            - a `(k+1)`-core

            .. SEEALSO:: :meth:`affine_grassmannian_to_partition`

            EXAMPLES::

                sage: # needs sage.combinat sage.groups
                sage: W = WeylGroup(['A', 2, 1])
                sage: w = W.from_reduced_word([0,2,1,0])
                sage: la = w.affine_grassmannian_to_core(); la
                [4, 2]
                sage: type(la)
                <class 'sage.combinat.core.Cores_length_with_category.element_class'>
                sage: la.to_grassmannian() == w
                True

                sage: w = W.from_reduced_word([0,2,1])                                  # needs sage.combinat sage.groups
                sage: w.affine_grassmannian_to_core()                                   # needs sage.combinat sage.groups
                Traceback (most recent call last):
                ...
                ValueError: this only works on type 'A' affine Grassmannian elements
            """
        def affine_grassmannian_to_partition(self):
            """
            Bijection between affine Grassmannian elements of type `A_k^{(1)}`
            and `k`-bounded partitions.

            INPUT:

            - ``self`` is affine Grassmannian element of the affine Weyl group of type `A_k^{(1)}` (i.e. all reduced words end in 0)

            OUTPUT: `k`-bounded partition

            .. SEEALSO:: :meth:`affine_grassmannian_to_core`

            EXAMPLES::

                sage: # needs sage.combinat sage.groups
                sage: k = 2
                sage: W = WeylGroup(['A', k, 1])
                sage: w = W.from_reduced_word([0,2,1,0])
                sage: la = w.affine_grassmannian_to_partition(); la
                [2, 2]
                sage: la.from_kbounded_to_grassmannian(k) == w
                True
            """
