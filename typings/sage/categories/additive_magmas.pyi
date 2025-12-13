from _typeshed import Incomplete
from sage.categories.algebra_functor import AlgebrasCategory as AlgebrasCategory
from sage.categories.cartesian_product import CartesianProductsCategory as CartesianProductsCategory
from sage.categories.category_singleton import Category_singleton as Category_singleton
from sage.categories.category_with_axiom import CategoryWithAxiom as CategoryWithAxiom
from sage.categories.homsets import HomsetsCategory as HomsetsCategory
from sage.categories.sets_cat import Sets as Sets
from sage.categories.with_realizations import WithRealizationsCategory as WithRealizationsCategory
from sage.misc.abstract_method import abstract_method as abstract_method
from sage.misc.cachefunc import cached_method as cached_method
from sage.misc.lazy_import import LazyImport as LazyImport
from typing import Self

class AdditiveMagmas(Category_singleton):
    """
    The category of additive magmas.

    An additive magma is a set endowed with a binary operation `+`.

    EXAMPLES::

        sage: AdditiveMagmas()
        Category of additive magmas
        sage: AdditiveMagmas().super_categories()
        [Category of sets]
        sage: AdditiveMagmas().all_super_categories()
        [Category of additive magmas,
         Category of sets,
         Category of sets with partial maps,
         Category of objects]

    The following axioms are defined by this category::

        sage: AdditiveMagmas().AdditiveAssociative()
        Category of additive semigroups
        sage: AdditiveMagmas().AdditiveUnital()
        Category of additive unital additive magmas
        sage: AdditiveMagmas().AdditiveCommutative()
        Category of additive commutative additive magmas
        sage: AdditiveMagmas().AdditiveUnital().AdditiveInverse()
        Category of additive inverse additive unital additive magmas
        sage: C = AdditiveMagmas().AdditiveAssociative().AdditiveCommutative(); C
        Category of commutative additive semigroups
        sage: C.AdditiveUnital()
        Category of commutative additive monoids
        sage: C.AdditiveUnital().AdditiveInverse()
        Category of commutative additive groups

    TESTS::

        sage: C = AdditiveMagmas()
        sage: TestSuite(C).run()
    """
    def super_categories(self):
        """
        EXAMPLES::

            sage: AdditiveMagmas().super_categories()
            [Category of sets]
        """
    class SubcategoryMethods:
        @cached_method
        def AdditiveAssociative(self):
            """
            Return the full subcategory of the additive associative
            objects of ``self``.

            An :class:`additive magma <AdditiveMagmas>` `M` is
            *associative* if, for all `x,y,z \\in M`,

            .. MATH:: x + (y + z) = (x + y) + z

            .. SEEALSO:: :wikipedia:`Associative_property`

            EXAMPLES::

                sage: AdditiveMagmas().AdditiveAssociative()
                Category of additive semigroups

            TESTS::

                sage: TestSuite(AdditiveMagmas().AdditiveAssociative()).run()
                sage: Rings().AdditiveAssociative.__module__
                'sage.categories.additive_magmas'
            """
        @cached_method
        def AdditiveCommutative(self):
            """
            Return the full subcategory of the commutative objects of ``self``.

            An :class:`additive magma <AdditiveMagmas>` `M` is
            *commutative* if, for all `x,y \\in M`,

            .. MATH:: x + y = y + x

            .. SEEALSO:: :wikipedia:`Commutative_property`

            EXAMPLES::

                sage: AdditiveMagmas().AdditiveCommutative()
                Category of additive commutative additive magmas
                sage: C = AdditiveMagmas().AdditiveAssociative().AdditiveUnital()
                sage: C.AdditiveCommutative()
                Category of commutative additive monoids
                sage: C.AdditiveCommutative() is CommutativeAdditiveMonoids()
                True

            TESTS::

                sage: TestSuite(AdditiveMagmas().AdditiveCommutative()).run()
                sage: Rings().AdditiveCommutative.__module__
                'sage.categories.additive_magmas'
            """
        @cached_method
        def AdditiveUnital(self):
            """
            Return the subcategory of the unital objects of ``self``.

            An :class:`additive magma <AdditiveMagmas>` `M` is *unital*
            if it admits an element `0`, called *neutral element*,
            such that for all `x \\in M`,

            .. MATH:: 0 + x = x + 0 = x

            This element is necessarily unique, and should be provided
            as ``M.zero()``.

            .. SEEALSO:: :wikipedia:`Unital_magma#unital`

            EXAMPLES::

                sage: AdditiveMagmas().AdditiveUnital()
                Category of additive unital additive magmas
                sage: from sage.categories.additive_semigroups import AdditiveSemigroups
                sage: AdditiveSemigroups().AdditiveUnital()
                Category of additive monoids
                sage: CommutativeAdditiveMonoids().AdditiveUnital()
                Category of commutative additive monoids

            TESTS::

                sage: TestSuite(AdditiveMagmas().AdditiveUnital()).run()
                sage: CommutativeAdditiveSemigroups().AdditiveUnital.__module__
                'sage.categories.additive_magmas'
            """
    AdditiveAssociative: Incomplete
    class ParentMethods:
        def summation(self, x, y):
            """
            Return the sum of ``x`` and ``y``.

            The binary addition operator of this additive magma.

            INPUT:

            - ``x``, ``y`` -- elements of this additive magma

            EXAMPLES::

                sage: S = CommutativeAdditiveSemigroups().example()
                sage: (a,b,c,d) = S.additive_semigroup_generators()
                sage: S.summation(a, b)
                a + b

            A parent in ``AdditiveMagmas()`` must
            either implement :meth:`.summation` in the parent class or
            ``_add_`` in the element class. By default, the addition
            method on elements ``x._add_(y)`` calls
            ``S.summation(x,y)``, and reciprocally.

            As a bonus effect, ``S.summation`` by itself models the
            binary function from ``S`` to ``S``::

                sage: bin = S.summation
                sage: bin(a,b)
                a + b

            Here, ``S.summation`` is just a bound method. Whenever
            possible, it is recommended to enrich ``S.summation`` with
            extra mathematical structure. Lazy attributes can come
            handy for this.

            .. TODO:: Add an example.
            """
        summation_from_element_class_add = summation
        def __init_extra__(self) -> None:
            """
            TESTS::

                sage: S = CommutativeAdditiveSemigroups().example()
                sage: (a,b,c,d) = S.additive_semigroup_generators()
                sage: a + b # indirect doctest
                a + b
                sage: a.__class__._add_ == a.__class__._add_parent
                True
            """
        def addition_table(self, names: str = 'letters', elements=None):
            """
            Return a table describing the addition operation.

            .. NOTE::

                The order of the elements in the row and column
                headings is equal to the order given by the table's
                :meth:`~sage.matrix.operation_table.OperationTable.column_keys`
                method.  The association can also be retrieved with the
                :meth:`~sage.matrix.operation_table.OperationTable.translation`
                method.

            INPUT:

            - ``names`` -- the type of names used:

              * ``'letters'`` -- lowercase ASCII letters are used
                for a base 26 representation of the elements'
                positions in the list given by
                :meth:`~sage.matrix.operation_table.OperationTable.column_keys`,
                padded to a common width with leading 'a's.
              * ``'digits'`` -- base 10 representation of the
                elements' positions in the list given by
                :meth:`~sage.matrix.operation_table.OperationTable.column_keys`,
                padded to a common width with leading zeros.
              * ``'elements'`` -- the string representations
                of the elements themselves.
              * a list - a list of strings, where the length
                of the list equals the number of elements.

            - ``elements`` -- (default: ``None``)  A list of
              elements of the additive magma, in forms that
              can be coerced into the structure, eg. their
              string representations. This may be used to
              impose an alternate ordering on the elements,
              perhaps when this is used in the context of a
              particular structure. The default is to use
              whatever ordering the ``S.list`` method returns.
              Or the ``elements`` can be a subset which is
              closed under the operation. In particular,
              this can be used when the base set is infinite.

            OUTPUT:

            The addition table as an object of the class
            :class:`~sage.matrix.operation_table.OperationTable`
            which defines several methods for manipulating and
            displaying the table.  See the documentation there
            for full details to supplement the documentation
            here.

            EXAMPLES:

            All that is required is that an algebraic structure
            has an addition defined.The default is to represent
            elements as lowercase ASCII letters.  ::

                sage: R = IntegerModRing(5)
                sage: R.addition_table()                                                # needs sage.modules
                +  a b c d e
                 +----------
                a| a b c d e
                b| b c d e a
                c| c d e a b
                d| d e a b c
                e| e a b c d

            The ``names`` argument allows displaying the elements in
            different ways.  Requesting ``elements`` will use the
            representation of the elements of the set.  Requesting
            ``digits`` will include leading zeros as padding.  ::

                sage: R = IntegerModRing(11)
                sage: P = R.addition_table(names='elements'); P                         # needs sage.modules
                 +   0  1  2  3  4  5  6  7  8  9 10
                  +---------------------------------
                 0|  0  1  2  3  4  5  6  7  8  9 10
                 1|  1  2  3  4  5  6  7  8  9 10  0
                 2|  2  3  4  5  6  7  8  9 10  0  1
                 3|  3  4  5  6  7  8  9 10  0  1  2
                 4|  4  5  6  7  8  9 10  0  1  2  3
                 5|  5  6  7  8  9 10  0  1  2  3  4
                 6|  6  7  8  9 10  0  1  2  3  4  5
                 7|  7  8  9 10  0  1  2  3  4  5  6
                 8|  8  9 10  0  1  2  3  4  5  6  7
                 9|  9 10  0  1  2  3  4  5  6  7  8
                10| 10  0  1  2  3  4  5  6  7  8  9

                sage: T = R.addition_table(names='digits'); T                           # needs sage.modules
                +  00 01 02 03 04 05 06 07 08 09 10
                  +---------------------------------
                00| 00 01 02 03 04 05 06 07 08 09 10
                01| 01 02 03 04 05 06 07 08 09 10 00
                02| 02 03 04 05 06 07 08 09 10 00 01
                03| 03 04 05 06 07 08 09 10 00 01 02
                04| 04 05 06 07 08 09 10 00 01 02 03
                05| 05 06 07 08 09 10 00 01 02 03 04
                06| 06 07 08 09 10 00 01 02 03 04 05
                07| 07 08 09 10 00 01 02 03 04 05 06
                08| 08 09 10 00 01 02 03 04 05 06 07
                09| 09 10 00 01 02 03 04 05 06 07 08
                10| 10 00 01 02 03 04 05 06 07 08 09

            Specifying the elements in an alternative order can provide
            more insight into how the operation behaves.  ::

                sage: S = IntegerModRing(7)
                sage: elts = [0, 3, 6, 2, 5, 1, 4]
                sage: S.addition_table(elements=elts)                                   # needs sage.modules
                +  a b c d e f g
                 +--------------
                a| a b c d e f g
                b| b c d e f g a
                c| c d e f g a b
                d| d e f g a b c
                e| e f g a b c d
                f| f g a b c d e
                g| g a b c d e f

            The ``elements`` argument can be used to provide
            a subset of the elements of the structure.  The subset
            must be closed under the operation.  Elements need only
            be in a form that can be coerced into the set.  The
            ``names`` argument can also be used to request that
            the elements be represented with their usual string
            representation.  ::

                sage: T = IntegerModRing(12)
                sage: elts = [0, 3, 6, 9]
                sage: T.addition_table(names='elements', elements=elts)                 # needs sage.modules
                +  0 3 6 9
                 +--------
                0| 0 3 6 9
                3| 3 6 9 0
                6| 6 9 0 3
                9| 9 0 3 6

            The table returned can be manipulated in various ways.  See
            the documentation for
            :class:`~sage.matrix.operation_table.OperationTable` for more
            comprehensive documentation. ::

                sage: # needs sage.modules
                sage: R = IntegerModRing(3)
                sage: T = R.addition_table()
                sage: T.column_keys()
                (0, 1, 2)
                sage: sorted(T.translation().items())
                [('a', 0), ('b', 1), ('c', 2)]
                sage: T.change_names(['x', 'y', 'z'])
                sage: sorted(T.translation().items())
                [('x', 0), ('y', 1), ('z', 2)]
                sage: T
                +  x y z
                 +------
                x| x y z
                y| y z x
                z| z x y
            """
    class ElementMethods: ...
    class Homsets(HomsetsCategory):
        def extra_super_categories(self):
            """
            Implement the fact that a homset between two magmas is a magma.

            EXAMPLES::

                sage: AdditiveMagmas().Homsets().extra_super_categories()
                [Category of additive magmas]
                sage: AdditiveMagmas().Homsets().super_categories()
                [Category of additive magmas, Category of homsets]
            """
    class CartesianProducts(CartesianProductsCategory):
        def extra_super_categories(self):
            """
            Implement the fact that a Cartesian product of additive magmas is
            an additive magma.

            EXAMPLES::

                sage: C = AdditiveMagmas().CartesianProducts()
                sage: C.extra_super_categories()
                [Category of additive magmas]
                sage: C.super_categories()
                [Category of additive magmas, Category of Cartesian products of sets]
                sage: C.axioms()
                frozenset()
            """
        class ElementMethods: ...
    class Algebras(AlgebrasCategory):
        def extra_super_categories(self):
            """
            EXAMPLES::

                sage: AdditiveMagmas().Algebras(QQ).extra_super_categories()
                [Category of magmatic algebras with basis over Rational Field]

                sage: AdditiveMagmas().Algebras(QQ).super_categories()
                [Category of magmatic algebras with basis over Rational Field,
                 Category of set algebras over Rational Field]
            """
        class ParentMethods:
            @cached_method
            def algebra_generators(self):
                """
                The generators of this algebra, as per
                :meth:`MagmaticAlgebras.ParentMethods.algebra_generators()
                <.magmatic_algebras.MagmaticAlgebras.ParentMethods.algebra_generators>`.

                They correspond to the generators of the additive semigroup.

                EXAMPLES::

                    sage: S = CommutativeAdditiveSemigroups().example(); S
                    An example of a commutative semigroup:
                     the free commutative semigroup generated by ('a', 'b', 'c', 'd')
                    sage: A = S.algebra(QQ)                                             # needs sage.modules
                    sage: A.algebra_generators()                                        # needs sage.modules
                    Family (B[a], B[b], B[c], B[d])

                .. TODO::

                    This doctest does not actually test this method,
                    but rather the method of the same name for
                    ``AdditiveSemigroups``. Find a better doctest!
                """
            def product_on_basis(self, g1, g2):
                """
                Product, on basis elements, as per
                :meth:`MagmaticAlgebras.WithBasis.ParentMethods.product_on_basis()
                <.magmatic_algebras.MagmaticAlgebras.WithBasis.ParentMethods.product_on_basis>`.

                The product of two basis elements is induced by the
                addition of the corresponding elements of the group.

                EXAMPLES::

                    sage: S = CommutativeAdditiveSemigroups().example(); S
                    An example of a commutative semigroup:
                     the free commutative semigroup generated by ('a', 'b', 'c', 'd')
                    sage: A = S.algebra(QQ)                                             # needs sage.modules
                    sage: a, b, c, d = A.algebra_generators()                           # needs sage.modules
                    sage: a * d * b                                                     # needs sage.modules
                    B[a + b + d]

                .. TODO::

                    This doctest does not actually test this method,
                    but rather the method of the same name for
                    ``AdditiveSemigroups``. Find a better doctest!
                """
    class AdditiveCommutative(CategoryWithAxiom):
        class CartesianProducts(CartesianProductsCategory):
            def extra_super_categories(self):
                """
                Implement the fact that a Cartesian product of commutative
                additive magmas is a commutative additive magma.

                EXAMPLES::

                    sage: C = AdditiveMagmas().AdditiveCommutative().CartesianProducts()
                    sage: C.extra_super_categories()
                    [Category of additive commutative additive magmas]
                    sage: C.axioms()
                    frozenset({'AdditiveCommutative'})
                """
        class Algebras(AlgebrasCategory):
            def extra_super_categories(self):
                """
                Implement the fact that the algebra of a commutative additive
                magmas is commutative.

                EXAMPLES::

                    sage: C = AdditiveMagmas().AdditiveCommutative().Algebras(QQ)
                    sage: C.extra_super_categories()
                    [Category of commutative magmas]

                    sage: C.super_categories()
                    [Category of additive magma algebras over Rational Field,
                     Category of commutative magmas]
                """
    class AdditiveUnital(CategoryWithAxiom):
        def additional_structure(self) -> Self:
            """
            Return whether ``self`` is a structure category.

            .. SEEALSO:: :meth:`Category.additional_structure`

            The category of unital additive magmas defines the zero as
            additional structure, and this zero shall be preserved by
            morphisms.

            EXAMPLES::

                sage: AdditiveMagmas().AdditiveUnital().additional_structure()
                Category of additive unital additive magmas
            """
        class SubcategoryMethods:
            @cached_method
            def AdditiveInverse(self):
                """
                Return the full subcategory of the additive inverse objects
                of ``self``.

                An inverse :class:`additive magma <AdditiveMagmas>` is
                a :class:`unital additive magma <AdditiveMagmas.Unital>`
                such that every element admits both an additive
                inverse on the left and on the right. Such an additive
                magma is also called an *additive loop*.

                .. SEEALSO::

                    :wikipedia:`Inverse_element`, :wikipedia:`Quasigroup`

                EXAMPLES::

                    sage: AdditiveMagmas().AdditiveUnital().AdditiveInverse()
                    Category of additive inverse additive unital additive magmas
                    sage: from sage.categories.additive_monoids import AdditiveMonoids
                    sage: AdditiveMonoids().AdditiveInverse()
                    Category of additive groups

                TESTS::

                    sage: TestSuite(AdditiveMagmas().AdditiveUnital().AdditiveInverse()).run()
                    sage: CommutativeAdditiveMonoids().AdditiveInverse.__module__
                    'sage.categories.additive_magmas'
                """
        class ParentMethods:
            @cached_method
            def zero(self):
                """
                Return the zero of this additive magma, that is the unique
                neutral element for `+`.

                The default implementation is to coerce ``0`` into ``self``.

                It is recommended to override this method because the
                coercion from the integers:

                - is not always meaningful (except for `0`), and
                - often uses ``self.zero()`` otherwise.

                EXAMPLES::

                    sage: S = CommutativeAdditiveMonoids().example()
                    sage: S.zero()
                    0
                """
            def is_empty(self):
                """
                Return whether this set is empty.

                Since this set is an additive magma it has a zero element and
                hence is not empty. This method thus always returns ``False``.

                EXAMPLES::

                    sage: # needs sage.modules
                    sage: A = AdditiveAbelianGroup([3, 3])
                    sage: A in AdditiveMagmas()
                    True
                    sage: A.is_empty()
                    False

                    sage: B = CommutativeAdditiveMonoids().example()
                    sage: B.is_empty()
                    False

                TESTS:

                We check that the method ``is_empty`` is inherited from this
                category in both examples above::

                    sage: A.is_empty.__module__                                         # needs sage.modules
                    'sage.categories.additive_magmas'
                    sage: B.is_empty.__module__
                    'sage.categories.additive_magmas'
                """
        class ElementMethods:
            @abstract_method
            def __bool__(self) -> bool:
                """
                Return whether ``self`` is not zero.

                All parents in the category ``CommutativeAdditiveMonoids()``
                should implement this method.

                .. NOTE:: This is currently not useful because this method is
                   overridden by ``Element``.

                TESTS::

                    sage: S = CommutativeAdditiveMonoids().example()
                    sage: bool(S.zero())
                    False
                    sage: bool(S.an_element())
                    True
                """
            def __neg__(self):
                """
                Return the negation of ``self``, if it exists.

                This top-level implementation delegates the job to
                ``_neg_``, for those additive unital magmas which may
                choose to implement it instead of ``__neg__`` for
                consistency.

                EXAMPLES::

                    sage: F = CombinatorialFreeModule(QQ, ['a', 'b'])                   # needs sage.modules
                    sage: a, b = F.basis()                                              # needs sage.modules
                    sage: -b                                                            # needs sage.modules
                    -B['b']

                TESTS::

                    sage: # needs sage.modules
                    sage: F = CombinatorialFreeModule(ZZ, ['a', 'b'])
                    sage: a, b = F.gens()
                    sage: FF = cartesian_product((F, F))
                    sage: x = cartesian_product([a, 2*a-3*b]); x
                    B[(0, 'a')] + 2*B[(1, 'a')] - 3*B[(1, 'b')]
                    sage: x.parent() is FF
                    True
                    sage: -x
                    -B[(0, 'a')] - 2*B[(1, 'a')] + 3*B[(1, 'b')]
                """
        class Homsets(HomsetsCategory):
            def extra_super_categories(self):
                """
                Implement the fact that a homset between two unital additive
                magmas is a unital additive magma.

                EXAMPLES::

                    sage: AdditiveMagmas().AdditiveUnital().Homsets().extra_super_categories()
                    [Category of additive unital additive magmas]
                    sage: AdditiveMagmas().AdditiveUnital().Homsets().super_categories()
                    [Category of additive unital additive magmas, Category of homsets]
                """
            class ParentMethods:
                @cached_method
                def zero(self):
                    """
                    EXAMPLES::

                        sage: R = QQ['x']
                        sage: H = Hom(ZZ, R, AdditiveMagmas().AdditiveUnital())
                        sage: f = H.zero()
                        sage: f
                        Generic morphism:
                          From: Integer Ring
                          To:   Univariate Polynomial Ring in x over Rational Field
                        sage: f(3)
                        0
                        sage: f(3) is R.zero()
                        True

                    TESTS:

                        sage: TestSuite(f).run()
                    """
        class AdditiveInverse(CategoryWithAxiom):
            class CartesianProducts(CartesianProductsCategory):
                def extra_super_categories(self):
                    """
                    Implement the fact that a Cartesian product of additive magmas
                    with inverses is an additive magma with inverse.

                    EXAMPLES::

                        sage: C = AdditiveMagmas().AdditiveUnital().AdditiveInverse().CartesianProducts()
                        sage: C.extra_super_categories()
                        [Category of additive inverse additive unital additive magmas]
                        sage: sorted(C.axioms())
                        ['AdditiveInverse', 'AdditiveUnital']
                    """
                class ElementMethods: ...
        class CartesianProducts(CartesianProductsCategory):
            def extra_super_categories(self):
                """
                Implement the fact that a Cartesian product of unital additive
                magmas is a unital additive magma.

                EXAMPLES::

                    sage: C = AdditiveMagmas().AdditiveUnital().CartesianProducts()
                    sage: C.extra_super_categories()
                    [Category of additive unital additive magmas]
                    sage: C.axioms()
                    frozenset({'AdditiveUnital'})
                """
            class ParentMethods:
                def zero(self):
                    """
                    Return the zero of this group.

                    EXAMPLES::

                        sage: GF(8, 'x').cartesian_product(GF(5)).zero()                # needs sage.rings.finite_rings
                        (0, 0)
                    """
        class Algebras(AlgebrasCategory):
            def extra_super_categories(self):
                """
                EXAMPLES::

                    sage: C = AdditiveMagmas().AdditiveUnital().Algebras(QQ)
                    sage: C.extra_super_categories()
                    [Category of unital magmas]

                    sage: C.super_categories()
                    [Category of additive magma algebras over Rational Field,
                     Category of unital algebras with basis over Rational Field]
                """
            class ParentMethods:
                @cached_method
                def one_basis(self):
                    """
                    Return the zero of this additive magma, which index the
                    one of this algebra, as per
                    :meth:`AlgebrasWithBasis.ParentMethods.one_basis()
                    <sage.categories.algebras_with_basis.AlgebrasWithBasis.ParentMethods.one_basis>`.

                    EXAMPLES::

                        sage: # needs sage.modules
                        sage: S = CommutativeAdditiveMonoids().example(); S
                        An example of a commutative monoid:
                         the free commutative monoid generated by ('a', 'b', 'c', 'd')
                        sage: A = S.algebra(ZZ)
                        sage: A.one_basis()
                        0
                        sage: A.one()
                        B[0]
                        sage: A(3)
                        3*B[0]
                    """
        class WithRealizations(WithRealizationsCategory):
            class ParentMethods:
                def zero(self):
                    """
                    Return the zero of this unital additive magma.

                    This default implementation returns the zero of the
                    realization of ``self`` given by
                    :meth:`~Sets.WithRealizations.ParentMethods.a_realization`.

                    EXAMPLES::

                        sage: A = Sets().WithRealizations().example(); A                # needs sage.modules
                        The subset algebra of {1, 2, 3} over Rational Field
                        sage: A.zero.__module__                                         # needs sage.modules
                        'sage.categories.additive_magmas'
                        sage: A.zero()                                                  # needs sage.modules
                        0

                    TESTS::

                        sage: A.zero() is A.a_realization().zero()                      # needs sage.modules
                        True
                        sage: A._test_zero()                                            # needs sage.modules
                    """
