from sage.categories.algebra_functor import AlgebrasCategory as AlgebrasCategory
from sage.categories.category_with_axiom import CategoryWithAxiom as CategoryWithAxiom

class FiniteGroups(CategoryWithAxiom):
    """
    The category of finite (multiplicative) groups.

    EXAMPLES::

        sage: C = FiniteGroups(); C
        Category of finite groups
        sage: C.super_categories()
        [Category of finite monoids, Category of groups]
        sage: C.example()
        General Linear Group of degree 2 over Finite Field of size 3

    TESTS::

        sage: TestSuite(C).run()
    """
    def example(self):
        """
        Return an example of finite group, as per
        :meth:`Category.example`.

        EXAMPLES::

            sage: G = FiniteGroups().example(); G
            General Linear Group of degree 2 over Finite Field of size 3
        """
    class ParentMethods:
        def semigroup_generators(self):
            """
            Return semigroup generators for ``self``.

            For finite groups, the group generators are also semigroup
            generators. Hence, this default implementation calls
            :meth:`~sage.categories.groups.Groups.ParentMethods.group_generators`.

            EXAMPLES::

                sage: A = AlternatingGroup(4)
                sage: A.semigroup_generators()
                Family ((1,2,3), (2,3,4))
            """
        def monoid_generators(self):
            """
            Return monoid generators for ``self``.

            For finite groups, the group generators are also monoid
            generators. Hence, this default implementation calls
            :meth:`~sage.categories.groups.Groups.ParentMethods.group_generators`.

            EXAMPLES::

                sage: A = AlternatingGroup(4)
                sage: A.monoid_generators()
                Family ((1,2,3), (2,3,4))
            """
        def cardinality(self):
            """
            Return the cardinality of ``self``, as per
            :meth:`EnumeratedSets.ParentMethods.cardinality`.

            This default implementation calls :meth:`.order` if
            available, and otherwise resorts to
            :meth:`._cardinality_from_iterator`. This is for backward
            compatibility only. Finite groups should override this
            method instead of :meth:`.order`.

            EXAMPLES:

            We need to use a finite group which uses this default
            implementation of cardinality::

                sage: G = groups.misc.SemimonomialTransformation(GF(5), 3); G           # needs sage.rings.number_field
                Semimonomial transformation group over Finite Field of size 5 of degree 3
                sage: G.cardinality.__module__                                          # needs sage.rings.number_field
                'sage.categories.finite_groups'
                sage: G.cardinality()                                                   # needs sage.rings.number_field
                384
            """
        def some_elements(self):
            """
            Return some elements of ``self``.

            EXAMPLES::

                sage: A = AlternatingGroup(4)
                sage: A.some_elements()
                Family ((1,2,3), (2,3,4))
            """
        def cayley_graph_disabled(self, connecting_set=None):
            """

            AUTHORS:

            - Bobby Moretti (2007-08-10)

            - Robert Miller (2008-05-01): editing
            """
        def conjugacy_classes(self) -> None:
            """
            Return a list with all the conjugacy classes of the group.

            This will eventually be a fall-back method for groups not defined
            over GAP. Right now, it just raises a
            :exc:`NotImplementedError`, until we include a non-GAP
            way of listing the conjugacy classes representatives.

            EXAMPLES::

                sage: from sage.groups.group import FiniteGroup
                sage: G = FiniteGroup()
                sage: G.conjugacy_classes()
                Traceback (most recent call last):
                ...
                NotImplementedError: Listing the conjugacy classes for group <sage.groups.group.FiniteGroup object at ...> is not implemented
            """
        def conjugacy_classes_representatives(self):
            """
            Return a list of the conjugacy classes representatives of the group.

            EXAMPLES::

                sage: G = SymmetricGroup(3)
                sage: G.conjugacy_classes_representatives()                             # needs sage.combinat
                [(), (1,2), (1,2,3)]
            """
    class ElementMethods: ...
    class Algebras(AlgebrasCategory):
        def extra_super_categories(self):
            """
            Implement Maschke's theorem.

            In characteristic 0 all finite group algebras are semisimple.

            EXAMPLES::

                sage: FiniteGroups().Algebras(QQ).is_subcategory(Algebras(QQ).Semisimple())
                True
                sage: FiniteGroups().Algebras(FiniteField(7)).is_subcategory(Algebras(FiniteField(7)).Semisimple())
                False
                sage: FiniteGroups().Algebras(ZZ).is_subcategory(Algebras(ZZ).Semisimple())
                False
                sage: FiniteGroups().Algebras(Fields()).is_subcategory(Algebras(Fields()).Semisimple())
                False

                sage: Cat = CommutativeAdditiveGroups().Finite()
                sage: Cat.Algebras(QQ).is_subcategory(Algebras(QQ).Semisimple())
                True
                sage: Cat.Algebras(GF(7)).is_subcategory(Algebras(GF(7)).Semisimple())
                False
                sage: Cat.Algebras(ZZ).is_subcategory(Algebras(ZZ).Semisimple())
                False
                sage: Cat.Algebras(Fields()).is_subcategory(Algebras(Fields()).Semisimple())
                False
            """
        class ParentMethods:
            def __init_extra__(self) -> None:
                """
                Implement Maschke's theorem.

                EXAMPLES::

                    sage: G = groups.permutation.Dihedral(8)
                    sage: A = G.algebra(GF(5))
                    sage: A in Algebras.Semisimple
                    True
                    sage: A = G.algebra(Zmod(4))
                    sage: A in Algebras.Semisimple
                    False

                    sage: G = groups.misc.AdditiveCyclic(4)                             # needs sage.rings.number_field
                    sage: Cat = CommutativeAdditiveGroups().Finite()
                    sage: A = G.algebra(GF(5), category=Cat)
                    sage: A in Algebras.Semisimple
                    True
                    sage: A = G.algebra(GF(2), category=Cat)
                    sage: A in Algebras.Semisimple
                    False
                """
