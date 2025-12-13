from sage.categories.cartesian_product import CartesianProductsCategory as CartesianProductsCategory
from sage.categories.category import Category as Category
from sage.categories.category_with_axiom import CategoryWithAxiom_over_base_ring as CategoryWithAxiom_over_base_ring
from sage.categories.commutative_additive_groups import CommutativeAdditiveGroups as CommutativeAdditiveGroups
from sage.categories.homset import Hom as Hom
from sage.categories.magmas import Magmas as Magmas
from sage.categories.magmatic_algebras import MagmaticAlgebras as MagmaticAlgebras
from sage.categories.morphism import SetMorphism as SetMorphism
from sage.categories.rings import Rings as Rings
from sage.misc.abstract_method import abstract_method as abstract_method
from sage.misc.cachefunc import cached_method as cached_method
from sage.misc.lazy_attribute import lazy_attribute as lazy_attribute

class UnitalAlgebras(CategoryWithAxiom_over_base_ring):
    """
    The category of non-associative algebras over a given base ring.

    A non-associative algebra over a ring `R` is a module over `R`
    which is also a unital magma.

    .. WARNING::

        Until :issue:`15043` is implemented, :class:`Algebras` is the
        category of associative unital algebras; thus, unlike the name
        suggests, :class:`UnitalAlgebras` is not a subcategory of
        :class:`Algebras` but of
        :class:`~.magmatic_algebras.MagmaticAlgebras`.

    EXAMPLES::

        sage: from sage.categories.unital_algebras import UnitalAlgebras
        sage: C = UnitalAlgebras(ZZ); C
        Category of unital algebras over Integer Ring

    TESTS::

        sage: from sage.categories.magmatic_algebras import MagmaticAlgebras
        sage: C is MagmaticAlgebras(ZZ).Unital()
        True
        sage: TestSuite(C).run()
    """
    class ParentMethods:
        def from_base_ring(self, r):
            """
            Return the canonical embedding of ``r`` into ``self``.

            INPUT:

            - ``r`` -- an element of ``self.base_ring()``

            EXAMPLES::

                sage: A = AlgebrasWithBasis(QQ).example(); A                            # needs sage.combinat sage.modules
                An example of an algebra with basis:
                 the free algebra on the generators ('a', 'b', 'c') over Rational Field
                sage: A.from_base_ring(1)                                               # needs sage.combinat sage.modules
                B[word: ]
            """
        def __init_extra__(self) -> None:
            """
            Declare the canonical coercion from ``self.base_ring()``
            to ``self``, if there has been none before.

            EXAMPLES::

                sage: A = AlgebrasWithBasis(QQ).example(); A                            # needs sage.combinat sage.modules
                An example of an algebra with basis:
                 the free algebra on the generators ('a', 'b', 'c') over Rational Field
                sage: coercion_model = sage.structure.element.get_coercion_model()
                sage: coercion_model.discover_coercion(QQ, A)                           # needs sage.combinat sage.modules
                ((map internal to coercion system -- copy before use)
                 Generic morphism:
                   From: Rational Field
                   To:   An example of an algebra with basis:
                          the free algebra on the generators ('a', 'b', 'c') over Rational Field,
                 None)
                sage: A(1)          # indirect doctest                                  # needs sage.combinat sage.modules
                B[word: ]

            TESTS:

            Ensure that :issue:`28328` is fixed and that non-associative
            algebras are supported::

                sage: # needs sage.modules
                sage: class Foo(CombinatorialFreeModule):
                ....:     def one(self):
                ....:         return self.monomial(0)
                sage: from sage.categories.magmatic_algebras import MagmaticAlgebras
                sage: C = MagmaticAlgebras(QQ).WithBasis().Unital()
                sage: F = Foo(QQ, (1,), category=C)
                sage: F(0)
                0
                sage: F(3)
                3*B[0]
            """
    class WithBasis(CategoryWithAxiom_over_base_ring):
        class ParentMethods:
            def one_basis(self) -> None:
                """
                When the one of an algebra with basis is an element of
                this basis, this optional method can return the index of
                this element. This is used to provide a default
                implementation of :meth:`.one`, and an optimized default
                implementation of :meth:`.from_base_ring`.

                EXAMPLES::

                    sage: # needs sage.combinat sage.modules
                    sage: A = AlgebrasWithBasis(QQ).example()
                    sage: A.one_basis()
                    word:
                    sage: A.one()
                    B[word: ]
                    sage: A.from_base_ring(4)
                    4*B[word: ]
                """
            @cached_method
            def one_from_one_basis(self):
                """
                Return the one of the algebra, as per
                :meth:`Monoids.ParentMethods.one()
                <sage.categories.monoids.Monoids.ParentMethods.one>`

                By default, this is implemented from
                :meth:`.one_basis`, if available.

                EXAMPLES::

                    sage: # needs sage.combinat sage.modules
                    sage: A = AlgebrasWithBasis(QQ).example()
                    sage: A.one_basis()
                    word:
                    sage: A.one_from_one_basis()
                    B[word: ]
                    sage: A.one()
                    B[word: ]

                TESTS:

                Try to check that :issue:`5843` Heisenbug is fixed::

                    sage: # needs sage.combinat sage.modules
                    sage: A = AlgebrasWithBasis(QQ).example()
                    sage: B = AlgebrasWithBasis(QQ).example(('a', 'c'))
                    sage: A == B
                    False
                    sage: Aone = A.one_from_one_basis
                    sage: Bone = B.one_from_one_basis
                    sage: Aone is Bone
                    False

                Even if called in the wrong order, they should returns their
                respective one::

                    sage: Bone().parent() is B                                          # needs sage.combinat sage.modules
                    True
                    sage: Aone().parent() is A                                          # needs sage.combinat sage.modules
                    True
                """
            @lazy_attribute
            def one(self):
                """
                Return the multiplicative unit element.

                EXAMPLES::

                    sage: A = AlgebrasWithBasis(QQ).example()                           # needs sage.combinat sage.modules
                    sage: A.one_basis()                                                 # needs sage.combinat sage.modules
                    word:
                    sage: A.one()                                                       # needs sage.combinat sage.modules
                    B[word: ]
                """
            @lazy_attribute
            def from_base_ring(self):
                """
                TESTS::

                    sage: A = AlgebrasWithBasis(QQ).example()                           # needs sage.combinat sage.modules
                    sage: A.from_base_ring(3)                                           # needs sage.combinat sage.modules
                    3*B[word: ]
                """
            def from_base_ring_from_one_basis(self, r):
                """
                Implement the canonical embedding from the ground ring.

                INPUT:

                - ``r`` -- an element of the coefficient ring

                EXAMPLES::

                    sage: # needs sage.combinat sage.modules
                    sage: A = AlgebrasWithBasis(QQ).example()
                    sage: A.from_base_ring_from_one_basis(3)
                    3*B[word: ]
                    sage: A.from_base_ring(3)
                    3*B[word: ]
                    sage: A(3)
                    3*B[word: ]
                """
    class CartesianProducts(CartesianProductsCategory):
        """
        The category of unital algebras constructed as Cartesian products
        of unital algebras.

        This construction gives the direct product of algebras. See
        discussion on:

         - http://groups.google.fr/group/sage-devel/browse_thread/thread/35a72b1d0a2fc77a/348f42ae77a66d16#348f42ae77a66d16
         - :wikipedia:`Direct_product`
        """
        def extra_super_categories(self):
            """
            A Cartesian product of algebras is endowed with a natural
            unital algebra structure.

            EXAMPLES::

                sage: from sage.categories.unital_algebras import UnitalAlgebras
                sage: C = UnitalAlgebras(QQ).CartesianProducts()
                sage: C.extra_super_categories()
                [Category of unital algebras over Rational Field]
                sage: sorted(C.super_categories(), key=str)
                [Category of Cartesian products of distributive magmas and additive magmas,
                 Category of Cartesian products of unital magmas,
                 Category of Cartesian products of vector spaces over Rational Field,
                 Category of unital algebras over Rational Field]
            """
        class ParentMethods:
            @cached_method
            def one(self):
                """
                Return the multiplicative unit element.

                EXAMPLES::

                    sage: # needs sage.graphs sage.modules
                    sage: S2 = simplicial_complexes.Sphere(2)
                    sage: H = S2.cohomology_ring(QQ)
                    sage: C = cartesian_product([H, H])
                    sage: one = C.one()
                    sage: one
                    B[(0, (0, 0))] + B[(1, (0, 0))]
                    sage: one == one * one
                    True
                    sage: all(b == b * one for b in C.basis())
                    True
                """
